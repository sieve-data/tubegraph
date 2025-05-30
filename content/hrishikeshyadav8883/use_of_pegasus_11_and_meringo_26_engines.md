---
title: Use of Pegasus 11 and Meringo 26 engines
videoId: 4vL1YPG6Ndk
---

From: [[hrishikeshyadav8883]] <br/> 

The video multilingual transcriber application leverages specific [[model_engines_used_marango_and_pegasus | model engines]] to provide its core [[functionality_of_pegasus_and_maringo_engines | functionality]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. These engines are essential for analyzing video content, preparing transcripts, and enabling interaction with the video <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. The application utilizes two primary engines: Maringo 2.6 and Pegasus 1.1 <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>.

## Maringo 2.6 Engine

The [[using_twelvelabs_sdk_and_marango_engine | Marango engine]], specifically version 2.6, is employed for the initial processing of video content <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.

*   **Purpose**: Maringo 2.6 is used for generating indexes and creating an embedded format of the video <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>. This is the first step in the video processing pipeline when a video is uploaded and submitted <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.
*   **Functionality**: It creates embeddings or indexing based on various elements within the video, including visual aspects, conversation, text, and logos <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>.
*   **Integration**: The application initiates index creation using `client.index.create`, specifying the Maringo 2.6 engine <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>. This process converts the video into an indexed format, making it searchable and analyzable <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

## Pegasus 1.1 Engine

After the video has been indexed by Maringo 2.6, the Pegasus 1.1 engine comes into play.

*   **Purpose**: [[pegasus_11_video_analytics | Pegasus 1.1]] is used to retrieve results from the generated index <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.
*   **Functionality**: It works in conjunction with a system prompt to provide the desired output, such as a transcript in a specific target language and difficulty level <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. The system prompt is applied behind the scenes, taking information about the target language (e.g., German, French, Spanish, English) and the user-selected difficulty level (beginner, intermediate, advanced) <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
*   **Integration**: Once the video indexing task is complete, the application uses Pegasus 1.1 with an API call (`generate api`) to process the indexed video ID and the system prompt to generate the transcript <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>. The temperature setting for generation is typically low (e.g., 0.25) to ensure the output remains faithful to the video's content <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.

These two engines are foundational to the application's ability to analyze and transcribe videos into multilingual formats with adjustable difficulty levels <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.