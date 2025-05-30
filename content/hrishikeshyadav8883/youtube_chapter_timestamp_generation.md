---
title: YouTube chapter timestamp generation
videoId: z-_PJqjTZmM
---

From: [[hrishikeshyadav8883]] <br/> 

YouTube chapter timestamp generation addresses the common problem faced by content creators and YouTubers who spend significant time manually noting down timestamps for video highlights and chapters <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This tool automates the process, making it easier to add chapters to YouTube video descriptions <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Core Functionality

The application offers two main options for users:
*   **Upload a new video** <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>
*   **Select an existing video** <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>

Once a video is chosen, the processing begins <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Video Processing
The system leverages advanced AI models for efficient [[video_indexing_and_processing | video indexing and processing]]:
*   **Indexing and Embedding**: [[video_indexing_and_processing | Video indexing]] is performed using the Marango 2.6 engine, which generates embeddings <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Analysis**: Results are analyzed with the Pegasus 1.1 engine to produce structured snippets <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Output Format**: The generated snippets are provided in a proper format, ready to be copied and pasted directly into a YouTube video description, making highlights visible <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Segmented Video Clips**: The tool also generates [[video_segment_generation_and_processing | segmented video clips]], which can be useful for content creators <a class="yt_timestamp" data-t="00:01:48">[00:01:48]</a>.

## Technical Process of the Application
The application is built on Streamlit for its user interface <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a> and uses `tempfile` for file management <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### Key Libraries and SDKs
*   [[Twelve Labs video embedding and retrieval | Twelve Labs]] SDK: Used for video embedding and retrieval operations <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   `movie.editor`: A Python library utilized for handling timestamps and cutting video segments <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   `M3U library`: For video manipulation <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   `YT-DLP`: Used for downloading videos from URLs before segmenting <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### Application Flow
The application's core logic is managed within `utils.py`, which contains all operational and functional components <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

#### Session State Management
The application uses session state to remember important information such as video ID, video URL, and generated timestamps <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

#### Uploading and Processing Videos
When uploading a new video, users select the video type (less than 30 minutes or more than 30 minutes, commonly for podcasts) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. For videos longer than 30 minutes, the system trims and processes them in segments (e.g., first 30 minutes, then next 30 minutes) to provide a complete timestamp <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

#### Selecting Existing Videos
Users can select previously uploaded videos to regenerate timestamps or segments using their index ID <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

#### Generating Timestamps
The `generate_time_stamp` function uses the [[Twelve Labs video embedding and retrieval | Twelve Labs]] client's `generate.summarize` method with the type set to "chapter" to create chapter markers <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. The raw timestamp results, which are in seconds, are converted to the minute:second format required by YouTube highlights <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

#### Video Segment Creation
After a video is indexed, its embedded URL (in M3U8 format) is used to cut down segments, which are then converted to MP4 for easy sharing <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## Setup and Configuration
To use the application, an API key and index ID from [[Twelve Labs video embedding and retrieval | Twelve Labs]] are required <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. These can be generated from the [[Twelve Labs video embedding and retrieval | Twelve Labs]] playground by selecting the Marango 2.6 and Pegasus 1.1 engines <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This ensures all processed videos are linked to a specific index ID <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Demonstration
Once timestamps are generated, they are provided in a proper format that can be copied directly into the YouTube video description <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Upon saving the description, the video's highlights (chapters like "Introduction," "Tool Overview," "Segmentation," etc.) become visible on YouTube <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

The application code is available on GitHub and can be tested hands-on using a Replit link <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.