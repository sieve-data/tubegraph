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

from __future__ import annotations

import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import List

import openai
import sieve
import webvtt
from dotenv import load_dotenv
from get_channel_vids import get_channel_id, get_channel_vids_filtered

# ---------------------------------------------------------------------------
# ENV / API clients
# ---------------------------------------------------------------------------
load_dotenv()
openai_client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.openai.com/v1",
)

gemini_client = openai.OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------
@dataclass(slots=True)
class Subtitle:
    text: str
    start: float
    end: float

    def __str__(self) -> str:  # human-friendly
        return f"{self.start:.3f} – {self.end:.3f} : {self.text}"


@dataclass(slots=True)
class Post:
    """Represents one finished (or in-progress) wiki-style article."""

    topic: str
    content: str
    filename: str
    video_id: str

    # helper to clone with new content (e.g. after adding backlinks)
    def with_content(self, new_content: str) -> "Post":
        return Post(self.topic, new_content, self.filename, self.video_id)


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
        subs_path = output_object["en"].path  # type: ignore[index]
    return subs_path


# ---------------------------------------------------------------------------
# LLM prompts
# ---------------------------------------------------------------------------
SYSTEM_PROMPT_TOPICS = """
You are a writer that is looking at a podcast/video and generating a list of
topics based on that podcast to write about. You will be given a transcript of a
YouTube video, and your goal is to output a set of topics that the
podcast/video has information on. Keep the number of topics to around 5 or LESS.
Return exactly this JSON shape:

{
  "topics": ["topic 1", "topic 2", ...]
}
"""

SYSTEM_PROMPT_POST = """
You are a writer creating a wiki-style article from a podcast episode. Write an
article (Markdown, with headings/sub-headings) **only** using information from
that episode. Include PLEASE INCLUDE timestamp references in THIS EXACT FORMAT:
<a class="yt-timestamp" data-t="HH:MM:SS">[HH:MM:SS]</a>
"""

SYSTEM_PROMPT_REFERENCE = """
You are an editor adding backlinks. Insert links in Markdown format
[[article_link | visible text]]. Keep everything else untouched and **return
only the modified article**, nothing extra.
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


def seconds_to_hms(seconds: float | int) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02}:{m:02}:{s:02}"


def write_post(topic: str, subtitles: List[Subtitle]) -> str:
    """Calls Gemini to draft the article."""
    joined_subs = "\n".join(f"{seconds_to_hms(s.start)}. {s.text}" for s in subtitles)

    completion = gemini_client.chat.completions.create(
        model="gemini-2.5-pro-preview-05-06",
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


def create_post(topic: str, subtitles: List[Subtitle], video_id: str) -> Post:
    content = write_post(topic, subtitles)
    filename = sanitize_string(topic)
    return Post(topic, content, filename, video_id)


def generate_posts(
    topics: List[str], subtitles: List[Subtitle], video_id: str
) -> List[Post]:
    posts: list[Post | None] = [None] * len(topics)
    with ThreadPoolExecutor() as ex:
        futures = {
            ex.submit(create_post, t, subtitles, video_id): i
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


def write_posts(posts: List[Post], output_dir: str = "dwarkesh_podcast") -> None:
    os.makedirs(output_dir, exist_ok=True)
    for post in posts:
        header = f"---\ntitle: {post.topic}\nvideoId: {post.video_id}\n---\n"
        with open(
            os.path.join(output_dir, f"{post.filename}.md"), "w", encoding="utf-8"
        ) as fh:
            fh.write(header + post.content)


def process_video(vid) -> List[Post]:
    """Process a single video dict and return the generated posts."""
    print("Processing", vid["title"])
    vid_url = f"https://www.youtube.com/watch?v={vid['videoId']}"
    video_id = get_youtube_video_id(vid_url)
    if video_id is None:
        print("Could not parse video ID – skipping.")
        return []

    subs_path = download_video(vid_url)
    subtitles = load_subtitles(subs_path)

    topics = generate_topics(subtitles, vid["title"])
    print("  → topics:", topics)

    posts = generate_posts(topics, subtitles, video_id)
    return posts


def main() -> None:
    channel_id = get_channel_id("DwarkeshPatel")
    vids_array = get_channel_vids_filtered(channel_id)

    all_posts: List[Post] = []

    # Choose a worker count that balances I/O and CPU‑bound work.
    # Adjust max_workers as needed for your environment.
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(process_video, vid) for vid in vids_array]
        for future in as_completed(futures):
            all_posts.extend(future.result())

    print("Adding cross-references…")
    all_posts = add_references(all_posts)

    print("Writing posts…")
    write_posts(all_posts)


if __name__ == "__main__":
    main()
