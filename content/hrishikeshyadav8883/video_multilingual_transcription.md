---
title: Video multilingual transcription
videoId: 4vL1YPG6Ndk
---

From: [[hrishikeshyadav8883]] <br/> 

This article discusses the development of a video multilingual transcriber application using the [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] SDK. This application allows users to upload a video and generate a transcript in various languages and at different difficulty levels <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Application Overview
A video multilingual transcriber converts a video's content into a transcript, which can then be translated into multiple languages <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] SDK enables the analysis of video content to produce a timestamp-based transcript <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Users can interact with the video and its generated transcript within the application <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### Key Features
*   **Multilingual Transcription**: Convert transcripts into various languages such as German, French, Spanish, and English <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a> <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Difficulty Level Adjustment**: Transcripts can be generated for different understanding levels (Beginner, Intermediate, Advanced) <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a> <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Interactive Transcripts**: The generated transcript is interactive, allowing users to click on a timestamp to jump to that specific point in the video <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a> <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   **Transcript Download**: Transcripts can be downloaded in PDF format <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

## Use Cases for Video Understanding
This application offers several [[use_cases_for_video_understanding | use cases for video understanding]], including:
*   **Educational Purposes**: Facilitating [[language_learning_applications | language learning]] by providing transcripts at different difficulty levels <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a> <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Understanding Critical Videos**: Helping users understand complex or specialized videos by breaking down the vocabulary and providing easier-to-understand transcripts <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Beyond Basic Transcription**: The system analyzes and understands the video content, not just generates a literal transcript, allowing for more intelligent outputs like difficulty adjustment <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Technical Process of Video Notetaking App
The [[technical_process_of_video_notetaking_app | technical process]] involves several steps:

### 1. Video Indexing and Embedding Generation
When a video is uploaded, the first step is to generate an index for it <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This involves creating an embedded format of the video content <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

#### Twelve Labs Engines
Two main engines from [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] are utilized:
*   **Maringo 2.6**: Used for creating embeddings or indexing based on visual information, conversations, text, video content, and logos <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a> <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
*   **Pegasus 1.1**: Used to retrieve results from the generated index <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### 2. API Key and SDK Initialization
To use the [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] SDK, an API key is required <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This key is loaded from an environment file (`.env`) or a secrets manager <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. The [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] client is then initialized with this API key <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### 3. Index Creation
An index is created for each video <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. If it's a new session or the first upload, a new unique index ID is generated using a random UUID <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This index is created via `client.index.create` using the specified index name and engine (Maringo 2.6) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

### 4. Task Creation and Status Checking
Once the index ID is obtained, a task is created to process and index the video using `task.create` <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. The application continuously checks the status of this task, which transitions from "indexing" to "ready" upon completion <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### 5. Prompt Generation and Result Retrieval
After the video is indexed and ready, a system prompt is used to generate the desired transcript <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a> <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This prompt incorporates information about the target language and the selected difficulty level <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. The `generate` API is called with a low temperature (0.25) to ensure less creative and more accurate results based on the video's content <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. The video ID from the completed task is used to reference the specific video <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## Development and Code Structure
The application is built as a Flask web application, with a minimal front-end using HTML, CSS, and JavaScript <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a> <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. The core logic, including the interaction with the [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] SDK, is implemented in Python utility functions <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

*   **Python**: Handles the main logic, API calls, and video processing.
*   **JavaScript**: Manages form data handling and displaying the interactive, timestamp-based transcript <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **HTML**: Provides the basic structure and form for user input <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

Resources for exploring the code and architecture, including a blog, Replit link, and GitHub repository, are available <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Future Exploration
The project can be expanded into a complete [[language_learning_applications | language learning application]] or a more detailed application for understanding specific types of videos <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. Additional parameters and functionalities can be integrated to enhance its capabilities <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.