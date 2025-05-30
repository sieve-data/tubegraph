---
title: Functionality of Pegasus and Maringo engines
videoId: J2vGUEEjHWI
---

From: [[hrishikeshyadav8883]] <br/> 

The development of an interview analyzer application relies on the specific functionalities of the Maringo and Pegasus engines, which are part of the [[twelvelabs_platform_and_capabilities | TwelveLabs platform]] <a class="yt-timestamp" data-t="02:02:02">[02:02:02]</a>. These [[model_engines_used_marango_and_pegasus | model engines]] enable key processes like video embedding, indexing, analysis, and text generation <a class="yt-timestamp" data-t="04:06:06">[04:06:06]</a>.

## Maringo 2.6 Engine

The [[use_of_pegasus_11_and_meringo_26_engines | Maringo 2.6 engine]] serves as the primary **embedding engine** within the application architecture <a class="yt-timestamp" data-t="04:06:06">[04:06:06]</a>.

### Key Functions:
*   **Classification of Search** It is utilized for the classification of search operations <a class="yt-timestamp" data-t="02:39:39">[02:39:39]</a>.
*   **Video Embedding and Indexing** After a video is recorded and stored, Maringo 2.6 is responsible for indexing or embedding the recorded video <a class="yt-timestamp" data-t="04:36:20">[04:36:20]</a>. This process involves converting video content into a format that allows for efficient retrieval and analysis, which is crucial for [[embedding_techniques_with_twelve_labs_and_milvus | embedding techniques]].

## Pegasus Engine

The Pegasus engine, specifically mentioned as Pegasus 2 and Pegasus 1.1, functions as the **generative engine** <a class="yt-timestamp" data-t="04:09:09">[04:09:09]</a>.

### Key Functions:
*   **Video Analysis and Text Generation** The Pegasus engine is selected for tasks that involve generating, analyzing, and generating text from video content <a class="yt-timestamp" data-t="02:44:81">[02:44:81]</a>.
*   **Prompt-Based Generation** Once a video is indexed, the Pegasus engine uses a prompt structure to perform analysis and generate relevant output <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. This prompt instructs the model on its role (e.g., "interviewer") and objective (e.g., "analyze the video clip") <a class="yt-timestamp" data-t="05:06:06">[05:06:06]</a>. The prompt also specifies the desired format of the response, such as JSON, for application integration <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
*   **Interview Analysis** In the context of the interview analyzer, [[pegasus_11_video_analytics | Pegasus 1.1 video analytics]] provides results such as confidence levels, clarity, speech rate, voice tone, body language assessment, and identification of key points from the interview <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

Together, the [[using_twelvelabs_sdk_and_marango_engine | Maringo embedding engine]] and [[use_of_pegasus_11_and_meringo_26_engines | Pegasus generative engine]] form the core of the video processing and analysis capabilities, making it easy to build advanced applications like the interview analyzer <a class="yt-timestamp" data-t="02:44:81">[02:44:81]</a>, and contributing to capabilities like [[video_content_recommendation_engine | video content recommendation]] and [[automating_content_creator_workflows | automating content creator workflows]].