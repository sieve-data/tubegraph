---
title: Use cases for video understanding
videoId: 82cmUtrzoV4
---

From: [[hrishikeshyadav8883]] <br/> 

An AI video note-taking application, powered by [[Twelve Labs video embedding and retrieval | Twelve Labs]], demonstrates various use cases for video understanding, allowing users to build solutions around it rapidly [00:00:04].

## AI Video Note-Taking Application

This application, built on Streamlit, functions as an AI video note-taker. Users can add new notes by inputting the URL of a YouTube or other video [00:00:41].

### Key Functionality and Examples

The application goes beyond simple transcription, focusing on deeper video analysis and understanding [00:02:32]:

*   **Video Summarization**: Users can prompt the application to "summarize the main points of this video," generating a concise summary of the content [00:01:09].
*   **Scene-by-Scene Description**: For visual-heavy content, such as a short film, the application can describe what is happening in the frame every two or three seconds [00:01:24].
*   **Lecture Video Analysis**: It is particularly useful for lecture videos where understanding extends beyond spoken words to visual elements like slides, text, graphs, or plots [00:02:25]. This is beneficial for videos that may lack a verbal context [00:02:47].
*   **Editing and Deletion**: Generated notes can be edited or deleted as needed [00:01:13].

### Underlying Technology

The application utilizes two primary engines from Twelve Labs to achieve its video understanding capabilities [00:03:07]:

*   **Marango 2.6**: This engine is used for embedding video data [00:03:17].
*   **Pegasus 1.1**: This engine handles the generative part of the process, including visual and conversational aspects [00:03:20].

These models work together for [[video_indexing_and_processing | indexing]] and prompting with the video content [00:03:24]. The process involves several stages: pending, [[video_indexing_and_processing | indexing]], and ready, before generating the desired output [00:03:33].

### Customization and Advanced Interactions

Users have the flexibility to define and build their own specific use cases [00:02:58]. Once a video is successfully [[video_indexing_and_processing | indexed]], its unique video ID allows for deeper interaction, enabling a "conversation" with the video content itself [00:05:05].

### Twelve Labs Dashboard Capabilities

The Twelve Labs dashboard offers further capabilities related to video understanding and processing [00:07:47]:

*   **Video Management**: Users can view [[video_indexing_and_processing | indexed]] videos and their configurations [00:07:59].
*   **Content Actions**: For [[video_indexing_and_processing | indexed]] videos, users can perform actions such as:
    *   Searching within the video [00:09:00].
    *   [[building_video_classification_applications | Classifying]] video content [00:09:00].
    *   Generating different types of content, including full talks, summaries, highlights, or chapters [00:09:03].

These features empower users to conduct experiments and build custom [[building_video_classification_applications | applications]] around video understanding [00:09:15].