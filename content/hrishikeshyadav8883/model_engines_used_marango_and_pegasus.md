---
title: Model engines used Marango and Pegasus
videoId: 82cmUtrzoV4
---

From: [[hrishikeshyadav8883]] <br/> 

The AI video note-taking application developed by [[12_labs | Twelve Labs]] leverages two primary model engines: Marango and Pegasus <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. These engines are crucial for the application's ability to understand, process, and generate insights from video content <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

## Specific Engines Used

The application utilizes [[use_of_pegasus_11_and_meringo_26_engines | Marango 2.6 and Pegasus 1.1]] to perform its video understanding tasks <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>, <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>. These engines are visible as configurable options within the [[12_labs | Twelve Labs]] dashboard <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>.

## Engine Functionality

Each engine plays a distinct role in the overall [[functionality_of_pegasus_and_maringo_engines | functionality of the application]]:

*   **Marango 2.6**: This engine is responsible for [[embedding_techniques_with_twelve_labs_and_milvus | embedding]] <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. [[using_twelvelabs_sdk_and_marango_engine | Marango]] facilitates the process of converting video data into a numerical format suitable for indexing and analysis.
*   **Pegasus 1.1**: This engine handles the generative part of the process <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. [[pegasus_11_video_analytics | Pegasus 1.1]] is described as being capable of visual and conversational tasks <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>, enabling the generation of summaries or scene-by-scene descriptions <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.

Together, these models assist in indexing video content and enabling prompting with the video <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

> [!NOTE] Processing stages
> The video processing pipeline involves distinct stages: initially "pending," then "indexing," before the video is considered "done" and the prompt generation phase begins <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. Once the video is successfully indexed, a video ID is retrieved, which is crucial for interacting with the processed video <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.