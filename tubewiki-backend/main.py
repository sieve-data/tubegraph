"""Refactored version of podcast snippet generator.

Key improvements
----------------
1. Introduces **Post** dataclass so every article keeps its own
   ``topic``, ``content``, ``filename`` *and* ``video_id`` – no more loose
   tuples.
2. Thread-safe helpers now return / accept ``Post`` objects.
3. ``write_posts`` reads the ``video_id`` directly from each ``Post`` so the
   correct one is written to every Markdown header.
4. Removes now-unnecessary arguments that were only there to work around the
   tuple structure.
"""

import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import List, Literal, Union

import openai
import sieve
import webvtt
from dotenv import load_dotenv
from get_channel_vids import get_channel_id, get_channel_vids_filtered
from github import Github, GithubException

load_dotenv()
openai_client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.openai.com/v1",
)

gemini_client = openai.OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


# Constants for the target repository
GITHUB_REPO = "sieve-data/tubegraph"


def _get_repo():
    """Authenticate and return the PyGitHub Repository object."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN env-var missing; cannot push to GitHub.")
    gh = Github(token)
    try:
        return gh.get_repo(GITHUB_REPO)
    except GithubException as exc:
        raise RuntimeError(f"Cannot access repo {GITHUB_REPO}: {exc}") from exc


def create_pr_with_files(file_paths: List[str], username: str) -> str:
    """Upload `file_paths` to content/<username>/ in the repo & open a PR.

    Returns the html_url of the created pull‑request.
    """
    repo = _get_repo()
    default_branch = repo.default_branch

    # 1️⃣ create a dedicated branch off the default branch
    base_sha = repo.get_branch(default_branch).commit.sha
    branch_name = f"add-{username}-content-{int(time.time())}"
    repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base_sha)

    # 2️⃣ add / update every markdown file in that branch
    commit_prefix = f"Add TubeGraph posts for {username}:"
    for abs_path in file_paths:
        with open(abs_path, "rb") as fh:
            content_str = fh.read().decode()
        # Preserve the per‑username sub‑folder inside content/
        rel_name = os.path.basename(abs_path)
        dest_path = f"content/{username}/{rel_name}"
        try:
            repo.create_file(
                dest_path,
                f"{commit_prefix} {rel_name}",
                content_str,
                branch=branch_name,
            )
        except GithubException as exc:
            # If the file already exists in that branch (re‑runs) => update
            if exc.status == 422 and "file already exists" in str(exc.data):
                repo.update_file(
                    dest_path,
                    f"Update {rel_name}",
                    content_str,
                    repo.get_contents(dest_path, ref=branch_name).sha,
                    branch=branch_name,
                )
            else:
                raise

    # 3️⃣ open the pull‑request
    pr = repo.create_pull(
        title=f"Add TubeGraph posts for {username}",
        body="Automatically generated TubeGraph markdown files.",
        head=branch_name,
        base=default_branch,
    )
    return pr.html_url


@dataclass
class Subtitle:
    text: str
    start: float
    end: float

    def __str__(self) -> str:  # human-friendly
        return f"{self.start:.3f} – {self.end:.3f} : {self.text}"


@dataclass
class Post:
    """Represents one finished (or in-progress) wiki-style article."""

    topic: str
    content: str
    filename: str
    video_id: str
    video_title: str

    # helper to clone with new content (e.g. after adding backlinks)
    def with_content(self, new_content: str) -> "Post":
        return Post(
            self.topic, new_content, self.filename, self.video_id, self.video_title
        )


# ---------------------------------------------------------------------------
# Helpers – subtitles, I/O, formatting
# ---------------------------------------------------------------------------


def load_subtitles(subtitles_path: str) -> List[Subtitle]:
    return [
        Subtitle(text=cap.text, start=cap.start_in_seconds, end=cap.end_in_seconds)
        for cap in webvtt.read(subtitles_path)
    ]


def download_video(url: str) -> str:
    """Downloads *only the subtitles* for a given YouTube URL via Sieve."""
    youtube_downloader = sieve.function.get("sieve/youtube-downloader")

    output = youtube_downloader.run(
        url,
        "subtitles",  # download_type
        "720p",  # resolution – ignored for subtitle-only mode
        True,  # include_audio
        0,  # start_time
        -1,  # end_time
        False,  # include_metadata
        ["title", "duration"],  # metadata_fields
        True,  # include_subtitles
        ["en"],  # subtitle_languages
        "mp4",  # video_format
        "mp3",  # audio_format
        "vtt",  # subtitle_format
    )
    for output_object in output:
        if output_object["en"] is None:
            return "error"
        subs_path = output_object["en"].path  # type: ignore[index]
    return subs_path


# ---------------------------------------------------------------------------
# LLM prompts
# ---------------------------------------------------------------------------
SYSTEM_PROMPT_TOPICS = """
You are a writer that is looking at a podcast/video and generating a list of
topics based on that podcast to write about. You will be given a transcript of a
YouTube video, and your goal is to output a set of topics that the
podcast/video has information on. Also PLEASE do not include any special characters
in the article prompt. You can only use normal alphabet and normal dash (-).
Keep the number of topics to around 5 or LESS.  Return exactly this JSON shape:

{
  "topics": ["topic 1", "topic 2", ...]
}
"""


SYSTEM_PROMPT_POST = """
You are a writer that is writing on a wiki style article based on a video/podcast and a given topic.
The topic is one of the things that is discussed in the video. Please write an article,
ideally only using information from that video on the given topic. Please write your article
in Obsidian flavored markdown format, (with headings, subheadings, etc.). You can also use callouts like so:
> [!info] Title
>
> This is a callout!
Additionally include reference timecodes within the article to the relevant timestamps for the relevant info in the transcript.
PLEASE ensure you use the following EXACT format for the timecodes:
<a class="yt-timestamp" data-t="HH:MM:SS">[HH:MM:SS]</a>
"""

SYSTEM_PROMPT_REFERENCE = """
You are an article editor that is going through an article and adding backlinks to other articles based on
a given set of topics. You will be given an article along with the topics and the topic links. Put the link
to the reference files in markdown format like [[article_link | text to display]]. So try to keep the links relevant
and in context, THIS IS SEPERATE from the timestamps, so do not change any of the timestamps. Only add in page links like below:

for example.
Kevin durant was recently [[kevin_durant_brooklyn_nets | drafted to the Nets]].

PLEASE return the article back with the backlinks embedded in the text. Keep everything in the post the same, and DON'T INCLUDE ANYTHING extra.
"""

# ---------------------------------------------------------------------------
# LLM wrappers
# ---------------------------------------------------------------------------


def generate_topics(subtitles: List[Subtitle], title: str) -> List[str]:
    joined_subs = "\n".join(f"{i + 1}. {s.text}" for i, s in enumerate(subtitles))

    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_TOPICS},
            {
                "role": "user",
                "content": (
                    f"The video is titled: {title}\nGenerate a list of topics based on this transcript:\n{joined_subs}"
                ),
            },
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(completion.choices[0].message.content)["topics"]


def seconds_to_hms(seconds: Union[float, int]) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02}:{m:02}:{s:02}"


def write_post(topic: str, subtitles: List[Subtitle]) -> str:
    """Calls Gemini to draft the article."""
    joined_subs = "\n".join(f"{seconds_to_hms(s.start)}. {s.text}" for s in subtitles)

    # completion = gemini_client.chat.completions.create(
    #     model="gemini-2.5-pro-preview-05-06",
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_POST},
            {
                "role": "user",
                "content": (
                    "Here is the transcript for the video:\n"
                    f"{joined_subs}\n\nWrite an article about: {topic}"
                ),
            },
        ],
    )
    return _remove_main_header(completion.choices[0].message.content)


def add_post_references(post: Post, reference_files: list[tuple[str, str]]) -> Post:
    backlink_topics = "\n".join(
        f"{title} – [[{fname}]]"
        for fname, title in reference_files
        if fname != post.filename
    )

    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_REFERENCE},
            {
                "role": "user",
                "content": (
                    f"Here is the article:\n{post.content}\n\nAdd backlinks using these topics:\n{backlink_topics}"
                ),
            },
        ],
        prediction={"type": "content", "content": post.content},
    )
    new_content = completion.choices[0].message.content
    return post.with_content(new_content)


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------


def _remove_main_header(md: str) -> str:
    return re.sub(r"^# .+\n", "", md, count=1, flags=re.MULTILINE)


def sanitize_string(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9 ]+", "", text).replace(" ", "_").lower()


def get_youtube_video_id(url: str) -> str | None:
    match = re.search(r"(?:v=|/)([0-9A-Za-z_-]{11})(?:[?&]|$)", url)
    return match.group(1) if match else None


# ---------------------------------------------------------------------------
# High-level orchestration helpers
# ---------------------------------------------------------------------------


def create_post(
    topic: str, subtitles: List[Subtitle], video_id: str, video_title: str
) -> Post:
    content = write_post(topic, subtitles)
    filename = sanitize_string(topic)
    return Post(topic, content, filename, video_id, video_title)


def generate_posts(
    topics: List[str], subtitles: List[Subtitle], video_id: str, video_title: str
) -> List[Post]:
    posts: List[Post | None] = [None] * len(topics)
    with ThreadPoolExecutor() as ex:
        futures = {
            ex.submit(create_post, t, subtitles, video_id, video_title): i
            for i, t in enumerate(topics)
        }
        for future in as_completed(futures):
            idx = futures[future]
            try:
                posts[idx] = future.result()
            except Exception as exc:  # noqa: BLE001
                print(f"Error generating post for topic {topics[idx]!r}: {exc}")
    return [p for p in posts if p is not None]  # type: ignore[return-value]


def add_references(posts: List[Post]) -> List[Post]:
    reference_files = [(p.filename, p.topic) for p in posts]

    posts_out: list[Post | None] = [None] * len(posts)
    with ThreadPoolExecutor() as ex:
        futures = {
            ex.submit(add_post_references, posts[i], reference_files): i
            for i in range(len(posts))
        }
        for future in as_completed(futures):
            idx = futures[future]
            try:
                posts_out[idx] = future.result()
            except Exception as exc:  # noqa: BLE001
                print(f"Error adding references for post index {idx}: {exc}")
    return [p for p in posts_out if p is not None]  # type: ignore[return-value]


def write_posts(posts: List[Post], username) -> None:
    all_markdowns = []
    os.makedirs(username, exist_ok=True)
    for post in posts:
        frontmatter = f"---\ntitle: {post.topic}\nvideoId: {post.video_id}\n---\n\nFrom: [[{username}]] <br/> \n"
        with open(
            os.path.join(username, f"{post.filename}.md"), "w", encoding="utf-8"
        ) as fh:
            all_markdowns.append(frontmatter + post.content)
            fh.write(frontmatter + post.content)
    return all_markdowns


def process_video(vid) -> List[Post]:
    """Process a single video dict and return the generated posts."""
    print("Processing", vid["title"])
    vid_url = f"https://www.youtube.com/watch?v={vid['videoId']}"
    video_id = get_youtube_video_id(vid_url)
    if video_id is None:
        print("Could not parse video ID – skipping.")
        return []

    subs_path = download_video(vid_url)
    if subs_path == "error":
        return []
    subtitles = load_subtitles(subs_path)

    topics = generate_topics(subtitles, vid["title"])
    print("  → topics:", topics)

    posts = generate_posts(topics, subtitles, video_id, vid["title"])
    return posts


def write_directory_post(all_posts: List[Post], username):
    frontmatter = f"---\ntitle: {username}\n---\n"
    # Group posts by (video_title, video_id)
    from collections import defaultdict

    grouped = defaultdict(list)
    for post in all_posts:
        grouped[(post.video_title, post.video_id)].append(post)

    sections = []
    for (video_title, video_id), posts in grouped.items():
        vid_url = f"https://www.youtube.com/watch?v={video_id}"
        header = f"### [{video_title}]({vid_url})"
        topics = "\n".join([f"- [[{post.filename} | {post.topic}]]" for post in posts])
        sections.append(f"{header}\n{topics}")

    content = frontmatter + "\n\n".join(sections)
    with open(os.path.join(username, f"{username}.md"), "w", encoding="utf-8") as fh:
        fh.write(content)
    return content


@sieve.function(
    name="create-tubegraph-pages",
    python_version="3.10",
    python_packages=[
        "openai",
        "python-dotenv",
        "sievedata",
        "webvtt-py",
        "isodate",
        "google-api-python-client",
        "PyGithub",
    ],
)
def get_items(
    username: str,
    min_vid_duration: int,
    sort_by: Literal["views", "upload_date"],
):
    channel_id = get_channel_id(username)
    print("getting, ", channel_id)
    vids_array = get_channel_vids_filtered(channel_id, sort_by, min_vid_duration)

    all_posts: List[Post] = []

    # Choose a worker count that balances I/O and CPU‑bound work.
    # Adjust max_workers as needed for your environment.
    with ThreadPoolExecutor(max_workers=25) as executor:
        futures = [executor.submit(process_video, vid) for vid in vids_array]
        for future in as_completed(futures):
            all_posts.extend(future.result())

    print("Adding cross-references…")
    all_posts = add_references(all_posts)

    print("Writing posts…")
    all_markdowns = write_posts(all_posts, username)
    directory_post = write_directory_post(all_posts, username)
    all_markdowns.append(directory_post)

    # Collect actual file paths
    file_paths = [os.path.join(username, f"{post.filename}.md") for post in all_posts]
    file_paths.append(os.path.join(username, f"{username}.md"))

    print("Creating pull‑request…")
    pr_url = create_pr_with_files(file_paths, username)
    print(f"✅ Opened PR: {pr_url}")

    return {"posts": all_markdowns, "pr_url": pr_url}
