---
title: Streamlit application development
videoId: kBuuFu2WNkg
---

From: [[hrishikeshyadav8883]] <br/> 

This article discusses the development of a video content quiz generator using Streamlit, focusing on how Streamlit facilitates the frontend and user interaction aspects of the application <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Overview of the Streamlit Application

The application is designed to analyze video content and generate multiple-choice questions for assessment purposes <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Users can upload educational videos, such as one about PCA concepts <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, and the application will generate quiz questions from it <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. The application supports MP4 file uploads <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Core Functionality
The main functionalities implemented in the Streamlit application include:
*   **Video Upload and Indexing**: Users upload video files, which are then indexed to generate text based on visual and conversational analysis <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Quiz Generation**: After indexing, the application generates multiple-choice questions (MCQs) in a JSON format with specific options and correct answers <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Quiz Display and Assessment**: The generated MCQs are displayed with radio buttons for answers <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>, and the application calculates the user's score based on their responses <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Streamlit Implementation Details

The application is built as a Streamlit application, typically running on platforms like Replit <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Library Imports
Essential libraries like Streamlit itself and a `utils` file are imported to manage various functionalities <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. The `utils.py` file contains the logic for interacting with the [[using_twelvelabs_sdk_and_marango_engine | Twelvelabs SDK]] and handling tasks like creating and waiting for indexing <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### User Interface and Interaction
*   **File Upload**: The application uses Streamlit's file uploader components, along with minimal custom HTML and CSS, to allow users to upload videos <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Dynamic Content**: When a quiz is submitted, visual feedback such as balloons floating is provided <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   **Session State Management**: Streamlit's session state (`st.session_state`) is crucial for running the quiz in an optimized manner, preventing unnecessary page refreshes and maintaining the quiz state <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. It is used to manage questions and responses <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Form Elements**: Radio buttons are used for displaying answer options in an MCQ format <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Customization**: The application allows for custom CSS to be added for background styling and button options <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Reset Functionality**: A "reset state" function is included to allow users to restart the quiz <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## Backend Integration with Streamlit

The Streamlit frontend integrates with a robust backend using the [[using_twelvelabs_sdk_and_marango_engine | Twelvelabs SDK]] to process video content:
*   **Video Indexing**: The Marango 2.6 embedding engine from [[using_twelvelabs_sdk_and_marango_engine | Twelvelabs]] is used to embed or index uploaded videos <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This process involves analyzing visuals and conversations within the video <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Text Generation**: The Pegasus engine is employed to generate text out of the indexed video content <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **API Key and Index ID**: The application requires a [[using_twelvelabs_sdk_and_marango_engine | Twelvelabs]] API Key and an index ID, which specifies where the video content will be indexed <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Prompt Engineering**: For generating MCQs, a structured prompt is used, defining the model's role (e.g., educational content analyzer), the objective, and the desired JSON response format <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **JSON Parsing**: Regular expressions (regex) are used to robustly parse the JSON-formatted MCQ responses received from the model <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Use Cases
This Streamlit application serves various purposes, including:
*   **Teacher/Admin Assessments**: Teachers or administrators can create assessments for students <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Student Practice**: Students can practice and self-assess based on learned content <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Content Creator Tools**: It can assist content creators and YouTubers in generating quizzes related to their video content <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.