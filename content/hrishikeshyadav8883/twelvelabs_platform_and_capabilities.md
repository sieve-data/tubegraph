---
title: TwelveLabs platform and capabilities
videoId: 82cmUtrzoV4
---

From: [[hrishikeshyadav8883]] <br/> 

Twelve Labs offers a platform for video understanding, enabling the creation of applications that leverage advanced video analysis [00:00:14]. The platform is designed to facilitate faster development of solutions around video understanding [00:00:25].

## AI Video Note-Taking Application
An AI video note-taking application, built on Streamlit, serves as a demonstration of Twelve Labs' capabilities [00:00:41]. This application allows users to:
*   Add new notes by inputting a YouTube URL or any other video URL [00:00:46].
*   Search through existing notes [00:01:00].
*   Generate summaries of video content [00:01:09].
*   Obtain scene-by-scene descriptions of what is happening in the video frame [00:01:24].
*   Edit or delete notes [00:01:13].

This application can be particularly useful for various scenarios, such as taking notes on lecture videos or analyzing videos that primarily contain slides, text, graphs, or plots without much spoken context [00:02:20].

## Twelve Labs Engines
The platform utilizes specific engines to process and understand video content:
*   **Marango 2.6**: This engine is used for embedding [00:03:10].
*   **Pegasus 1.1**: This engine handles the generative aspects, including visual and conversational understanding [00:03:12], [00:05:22].

These models contribute to [[using_twelve_labs_for_video_indexing | indexing]] videos and enabling prompting capabilities [00:03:24].

## Video Processing Workflow
When a video is submitted for processing on the Twelve Labs platform, it undergoes several stages:
1.  **Pending Status**: Initially, the video task is in a pending state [00:03:35].
2.  **Indexing Status**: Following pending, the video moves to an indexing status where it's processed [00:03:38], [00:06:14]. The application checks the status every 5 seconds [00:04:30].
3.  **Ready Status**: Once [[using_twelve_labs_for_video_indexing | indexing]] is successful, the task status changes to "ready," indicating that the video has been indexed [00:04:42], [00:06:36].
4.  **Note Generation/Prompting**: After the video is indexed, the system proceeds to generate notes or text based on the user's prompt (e.g., "summarize the main points of this video") [00:04:44], [00:06:25].
The `task.ID` from the processing allows for retrieving the video ID, which is crucial for connecting to the video and having conversations with it [00:04:50].

## Twelve Labs Dashboard
The Twelve Labs dashboard provides a centralized interface for managing and experimenting with video data [00:07:47]. Users can:
*   View all configured indexes [00:07:57], such as those named by date and time [00:08:37].
*   Inspect the specific engines used for an index (e.g., Pegasus 1.1) [00:08:45].
*   View the uploaded video [00:08:56].
*   Perform actions on indexed videos, including search, classify, or generate content [00:09:00].
*   Utilize generation options such as creating talk/summary, highlights, or chapters from the video content [00:09:05].

The dashboard serves as a useful tool for experimentation before building full-fledged applications [00:09:12].