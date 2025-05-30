---
title: TW Labs SDK integration
videoId: 4vL1YPG6Ndk
---

From: [[hrishikeshyadav8883]] <br/> 

The [[use_of_twelve_labs_sdk | Twelve Labs SDK]] enables the development of applications that analyze videos and prepare transcripts based on timestamps, allowing for interaction with the video [00:00:31]. One specific use case for the [[use_of_twelve_labs_sdk | SDK]] is building a video multilingual transcriber [00:00:05].

## Video Multilingual Transcriber Application

This application allows users to input a video in one language and convert its transcription into various other languages [00:00:20]. It can also generate transcripts at different difficulty levels (beginner, intermediate, advanced) [00:01:39].

The application's capabilities go beyond simple transcription:
*   **Video Analysis** The [[use_of_twelve_labs_sdk | SDK]] analyzes and understands the video content [00:01:22].
*   **Difficulty Adjustment** Users can set the difficulty level of the generated transcript to beginner or intermediate for better comprehension, especially useful for language learning [00:01:39].
*   **Educational Use** The tool can be leveraged for language learning or understanding critical videos, as it analyzes and understands the video beyond just transcript generation [00:01:06].
*   **Interactive Transcripts** The generated transcript is interactive, allowing users to click on a timestamp to jump to the corresponding part of the video [00:12:05].
*   **Downloadable Transcripts** Transcripts can be downloaded in PDF format [00:12:18].

## Setting Up the [[use_of_twelve_labs_sdk | Twelve Labs SDK]]

The application demonstrated is a Flask application with minimal HTML, CSS, and JavaScript, primarily focusing on Python and utility functions [00:04:31].

To get started:
1.  **API Key**: Obtain an API key from the [[twelvelabs_platform_and_capabilities | TwelveLabs platform]] by logging in and navigating to the API key section [00:05:04].
2.  **Environment Setup**: Load the secret API key by creating an `.env` file or using a secrets management system, such as in Replit [00:04:50].
3.  **Client Initialization**: Initialize the [[use_of_twelve_labs_sdk | Twelve Labs SDK]] client to make use of its functionalities [00:03:39].

## Core Process of [[use_of_twelve_labs_sdk | SDK]] Integration

The `process_video` utility function handles the core logic of the application:
1.  **Index ID Check**: The system first checks if an index ID is already present in the session. If it's a new session, a unique index ID is created using a UUID [00:06:04].
2.  **Engine Selection**: Two main engines from [[twelvelabs_platform_and_capabilities | TwelveLabs platform]] are utilized:
    *   **Maringo 2.6**: Used for [[twelve_labs_video_embedding_and_retrieval | video embedding and retrieval]] and [[using_twelvelabs_sdk_and_marango_engine | video indexing]], creating embeddings based on visual conversation, text, video, and logos [00:03:37, 00:06:50].
    *   **Pegasus 1.1**: Used to retrieve results from the indexed video [00:07:07].
3.  **Index Creation**: An index is created using `client.index.create`, providing the index name and the Maringo 2.6 engine [00:07:16].
4.  **Task Creation and [[using_twelve_labs_for_video_indexing | Video Indexing]]**: A task is created using `task.create` with the index ID and the video file path [00:08:00]. The system continuously checks the task status until indexing is complete and the status changes to "ready" [00:08:19].
5.  **Prompting for Results**: Once the video is indexed, the system sends a prompt to the Pegasus 1.1 engine to generate the transcript [00:08:37].
    *   **System Prompt**: A hidden system prompt captures the target language and difficulty level provided by the user [00:03:55].
    *   **Generation API**: The `generate` API is used with a temperature of 0.25 (for less creativity, focusing on the video's base content) and the video ID [00:09:08].
6.  **Response Handling**: The response contains the time and transcript, which can be parsed to prepare an interactive timestamp-based video experience [00:10:03].

Detailed code and architecture descriptions, along with a Replit link and GitHub repository, are available for further exploration and experimentation [00:01:57, 00:02:08, 00:02:19].