---
title: Technical process of video notetaking app
videoId: 82cmUtrzoV4
---

From: [[hrishikeshyadav8883]] <br/> 

The [[ai_video_notetaking_applications | AI video notetaking application]], powered by [[using_twelve_labs_for_video_indexing | Twelve Labs]], demonstrates various [[use_cases_for_video_understanding | use cases of video understanding]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It's built on Streamlit <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, allowing users to add notes by providing a YouTube video URL <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Core Functionality

Users can perform actions such as:
*   Adding new notes by inputting a video URL <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   Searching through existing notes using keywords like "intro" or "horror" <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   Generating summaries of main points <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   Requesting scene-by-scene descriptions of video events <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This feature describes what is happening in the frame approximately every two to three seconds <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   Editing or deleting notes <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Use Cases
The application can be beneficial for:
*   Taking notes from lecture videos <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   Understanding video content beyond just transcription, especially for frames with visual information <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   Processing videos that lack spoken context but contain important visual elements like slides, text, graphs, or plots <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Technical Architecture

The application leverages [[using_twelve_labs_for_video_indexing | Twelve Labs]]'s video understanding capabilities through specific engines:
*   **Marango 2.6:** This engine is used for embedding <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a> and visual understanding <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Pegasus 1.1:** This engine is responsible for the generative part, specifically for conversations and visual contexts <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a> <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

These models assist in [[video_indexing_and_processing | indexing]] and enabling prompt-based interactions with videos <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Video Processing Workflow

When a user submits a video URL and a prompt (e.g., "summarize the points of this video") <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>, the process involves several stages:

1.  **URL Validation:** The application first checks if the provided YouTube URL is valid <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
2.  **Pending Status:** Initially, the video processing status is "pending" <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
3.  **Indexing Status:** The video then moves to an "indexing" status <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. This stage involves using the Marango and Pegasus engines for embedding and generative processing <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
4.  **Status Polling:** The application checks the video's status at five-second intervals <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
5.  **Ready Status:** Once processing is complete, the status changes to "ready," indicating that the video has been successfully indexed <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
6.  **Note Generation:** After indexing, the system proceeds to generate notes based on the user's prompt <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. This output can be edited or deleted by the user <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Underlying Mechanisms
The application utilizes a session state to save notes in a cache, though it does not connect to a permanent database in its demo form <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Integration with Twelve Labs Dashboard

Upon successful indexing, a `video.ID` is retrieved <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. This ID is crucial for connecting to the [[using_twelve_labs_for_video_indexing | Twelve Labs]] account dashboard <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. On the dashboard, users can:
*   View the indexed video <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   Inspect configuration settings <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   Perform direct actions like searching, classifying, or generating content (e.g., talks, summaries, highlights, chapters) for the video <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. This allows for further experimentation and development of custom applications <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.