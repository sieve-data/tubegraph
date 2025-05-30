---
title: Principal Component Analysis video tutorial
videoId: kBuuFu2WNkg
---

From: [[hrishikeshyadav8883]] <br/> 

This article details the process of generating a multiple-choice question (MCQ) quiz from a video tutorial focused on Principal Component Analysis (PCA) concepts using an AI-powered application. The application processes video content to create assessments, demonstrating its utility for educational purposes <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Application Overview

The demo application allows users to upload an educational video, such as a PCA concept tutorial <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The application then processes the video to generate assessment questions <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. For optimal performance, video content should ideally be around 20 to 30 minutes long; longer videos can be trimmed into multiple segments <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The application supports MP4 file uploads <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## How the Quiz is Generated

The core of the quiz generation process involves several steps powered by [[Twelve Labs video embedding and retrieval | Twelve Labs]]' engines:

1.  **Video Indexing**: Upon video upload, an indexing process begins <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This is handled by [[Twelve Labs video embedding and retrieval | Twelve Labs]]' Marango 2.6 embedding engine, which embeds or indexes the video content <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. The indexing status progresses from pending to indexing, and finally to ready <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
2.  **Text Generation**: After indexing, the system generates text by analyzing both the visuals and conversations within the video <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This is performed by [[pegasus_11_video_analytics | Pegasus]] <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
3.  **MCQ Generation**: Once the indexing is complete, MCQs are generated using the `client.generate.text` function <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The prompt structure provided to the model includes:
    *   Defining the model's role (e.g., "educational content analyzer") <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
    *   Specifying the objective (e.g., generating MCQs) <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
    *   Requesting a specific JSON response format containing questions (Q1, Q2, Q3), options, and the correct answer for each <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
    *   The raw JSON response is then parsed using regular expressions for robustness <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Demonstration with PCA Video

An uploaded PCA lecture video served as an example for the quiz generation <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. The application successfully generated MCQs relevant to the video content:

*   **Question 1**: "What is the primary focus of the video?" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>
    *   **Correct Answer**: "Principal Component Analysis" <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>
*   **Question 2**: "Which of the following statement about principal component analysis is true?" <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>
    *   **Correct Answer**: "It is used to reduce the dimensionality of a data set" <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>
*   **Question 3**: "What is the purpose of using PCA in regression?" <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>
    *   **Correct Answer**: "to actually reduce the number of" <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a> (The answer cut off in the transcript.)

The application also calculates the user's score based on their answers, providing an end-to-end assessment solution <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Building the Streamlit Application

The application is built using Streamlit, with the main logic in `app.py` and utility functions in `utils.py` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

*   **Libraries**: Necessary libraries include Streamlit and `utils.py` for functionalities like JSON parsing and task creation <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **API Key and Index ID**: Users need to obtain an API key from the [[Twelve Labs video embedding and retrieval | Twelve Labs]] playground and create an index ID, ensuring Marango 2.6 and [[pegasus_11_video_analytics | Pegasus]] are selected for open-ended generation <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. This index ID specifies where uploaded videos will be indexed <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Task Management**: Functions like `create_task` and `wait_for_task` manage the video processing workflow <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **User Interface**: Streamlit's `st.session_state` is used to manage the quiz flow and prevent page refreshes <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Radio buttons are used for answer selection, and upon submission, a score is calculated <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

This application demonstrates a practical [[use_cases_for_video_understanding | use case for video understanding]] in education, allowing teachers to create assessments or students to practice content learned from video tutorials <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.