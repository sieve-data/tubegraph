import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple

import openai
import sieve
import webvtt
from dotenv import load_dotenv

load_dotenv()

openai_client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.openai.com/v1",
)


class Subtitle:
    def __init__(self, text: str, start: float, end: float):  # Changed str to float
        self.text = text
        self.start = start
        self.end = end

    # nice-looking representations
    def __str__(self):
        # This formatting will now work correctly as start/end are floats
        return f"{self.start:.3f} – {self.end:.3f} : {self.text}"

    __repr__ = __str__


def load_subtitles(subtitles_path: str) -> List[Subtitle]:
    return [
        Subtitle(
            text=cap.text,
            start=cap.start_in_seconds,  # Use float attribute
            end=cap.end_in_seconds,  # Use float attribute
        )
        for cap in webvtt.read(subtitles_path)
    ]


def download_video(url):
    download_type = "subtitles"
    resolution = "720p"
    include_audio = True
    start_time = 0
    end_time = -1
    include_metadata = True
    metadata_fields = ["title", "duration"]
    include_subtitles = True
    subtitle_languages = ["en"]
    video_format = "mp4"
    audio_format = "mp3"
    subtitle_format = "vtt"

    youtube_downloader = sieve.function.get("sieve/youtube-downloader")
    output = youtube_downloader.run(
        url,
        download_type,
        resolution,
        include_audio,
        start_time,
        end_time,
        include_metadata,
        metadata_fields,
        include_subtitles,
        subtitle_languages,
        video_format,
        audio_format,
        subtitle_format,
    )

    for index, output_object in enumerate(output):
        if index == 0:
            title = output_object["title"]
        elif index == 1:
            subtitles_path = output_object["en"].path

    return title, subtitles_path


# download_video(
#     "https://www.youtube.com/watch?v=QFzgSmN8Ng8&list=PLd7-bHaQwnthaNDpZ32TtYONGVk95-fhF&index=4"
# )

SYSTEM_PROMPT_TOPICS = """
You are a writer that is looking at a podcast/video and generating a list of topics based on that podcast
to write about. You will be given a transcript of a Youtube video, and your goal is to output a set of topics
that the podcast/video has information on. Please return your response in a JSON array format like so: 

topics: {
    ["topic_1", "topic_2", ...]
}

"""


def generate_topics(subtitles: List[Subtitle], title) -> List[str]:
    joined_subs = "\n".join(f"{i + 1}. {obj.text}" for i, obj in enumerate(subtitles))
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT_TOPICS,
            },
            {
                "role": "user",
                "content": f"""
                The video is titled: {title}
                Generate a list of topics based on this transcript of a podcast: 
                {joined_subs}""",
            },
        ],
        response_format={"type": "json_object"},
    )

    result = completion.choices[0].message.content
    return json.loads(result)["topics"]


def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{int(hours):02}:{int(minutes):02}:{int(secs):02}"


SYSTEM_PROMPT_POST = """
You are a writer that is writing on a wiki style article based on a video/podcast and a given topic.
The topic is one of the things that is discussed in the video. Please write an article, 
ideally only using information from that video on the given topic. Please write your article
in markdown format, (with headings, subheadings, etc.). Additionally include reference timecodes
within the article to the relevant timestamps for the relevant info in the transcript. Please use
the following format for the timecodes: 
<a class="yt-timestamp" data-t="HH:MM:SS">[HH:MM:SS]</a>
"""


def write_post(post_topic: str, subtitles: List[Subtitle]) -> str:
    joined_subs = "\n".join(
        f"{seconds_to_hms(obj.start)}. {obj.text}" for i, obj in enumerate(subtitles)
    )

    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT_POST,
            },
            {
                "role": "user",
                "content": f"""
                        Here is the transcript for the video:
                        {joined_subs}
                        Please write an article based on this topic:
                        {post_topic}
                        """,
            },
        ],
    )
    result = completion.choices[0].message.content
    return result


SYSTEM_PROMPT_REFERENCE = """
You are an article editor that is going through an article and adding backlinks to other articles based on
a given set of topics. You will be given an article along with the topics and the topic links. Put the link
to the reference files in markdown format like [[article_link | text to display]]. So try to keep the links relevant 
and in context, 

for example. 
Kevin durant was recently [[kevin_durant_brooklyn_nets | drafted to the Nets]].

PLEASE return the article back with the backlinks embedded in the text. Keep everything in the post the same, and DON'T INCLUDE ANYTHING extra.
"""


def add_post_references(post: Tuple[str, str], reference_files: Tuple[str, str]) -> str:
    backlink_topics = "\n".join(
        f"{ref_title} - Article link : [[{ref_file}]]"
        for ref_file, ref_title in reference_files
    )
    post_data, filename = post

    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT_REFERENCE,
            },
            {
                "role": "user",
                "content": (
                    f"Here is the article:\n{post_data}\n"
                    f"Please add backlinks to the article based on the following topics:\n"
                    f"{backlink_topics}"
                ),
            },
        ],
        prediction={"type": "content", "content": post_data},
    )
    result = completion.choices[0].message.content
    return result, filename


def sanitize_string(text: str) -> str:
    # Remove all non-alphanumeric characters except spaces
    cleaned = re.sub(r"[^A-Za-z0-9 ]+", "", text)
    # Replace spaces with underscores
    underscored = cleaned.replace(" ", "_")
    return underscored.lower()


def get_youtube_video_id(url: str):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})(?:[?&]|$)", url)
    return match.group(1) if match else None


def create_post(topic, subtitles, video_id):
    post = write_post(topic, subtitles)
    filename = sanitize_string(topic)
    return post, filename


def generate_posts(topics, subtitles, video_id):
    posts: list[Tuple[str, str] | None] = [None] * len(topics)  # reserve slots
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(create_post, topic, subtitles, video_id): idx
            for idx, topic in enumerate(topics)
        }
        for future in as_completed(futures):
            idx = futures[future]
            try:
                posts[idx] = future.result()  # put result in correct slot
            except Exception as e:
                print(f"Error processing topic {topics[idx]}: {e}")
    return posts


def add_references(posts, reference_files):
    referenced_posts: list[Tuple[str, str] | None] = [None] * len(posts)
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(add_post_references, posts[i], reference_files): i
            for i in range(len(posts))
        }
        for future in as_completed(futures):
            idx = futures[future]
            try:
                referenced_posts[idx] = future.result()
            except Exception as e:
                print(f"Error processing post index {idx}: {e}")
    return referenced_posts


def write_posts(posts, topics, video_id):
    for (post_data, filename), topic in zip(posts, topics):
        post_header = f"""---\ntitle: {topic}\nvideoId: {video_id}\n---\n"""
        full_post = post_header + post_data
        with open(f"{filename}.md", "w") as f:
            f.write(full_post)


def main():
    print("downloading video")
    title, subs_path = download_video("https://www.youtube.com/watch?v=QFzgSmN8Ng8")
    subtitles = load_subtitles(subs_path)

    video_id = get_youtube_video_id("https://www.youtube.com/watch?v=QFzgSmN8Ng8")

    print("generating topics")
    topics = generate_topics(subtitles, title)

    print("creating posts")
    posts = generate_posts(topics, subtitles, video_id)

    reference_files = [
        (filename, topics[i]) for i, (full_post, filename) in enumerate(posts)
    ]

    print("adding refs")
    posts_referenced = add_references(posts, reference_files)

    write_posts(posts_referenced, topics, video_id)


main()
