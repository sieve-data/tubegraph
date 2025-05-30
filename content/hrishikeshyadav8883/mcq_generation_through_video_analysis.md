---
title: MCQ generation through video analysis
videoId: kBuuFu2WNkg
---

From: [[hrishikeshyadav8883]] <br/> 

This article outlines how to build a [[video_content_quiz_generation | video content quiz generator]] that analyzes video content to generate multiple-choice questions (MCQs) for assessment purposes <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The process involves video analysis and subsequent MCQ generation based on the analyzed content <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Application Walkthrough

The demo application allows users to upload educational videos, such as one on the PCA (Principal Component Analysis) concept <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Video Preparation
For optimal performance, video content should ideally be 20 to 30 minutes long <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Longer videos can be trimmed into multiple segments for processing <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Indexing Process
Upon video upload, an indexing process begins <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This involves using 12 Labs' Maringo 2.6 embedding engine to embed or index the video <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. After indexing, the system generates text from the video by analyzing both visuals and spoken content <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This text generation is powered by the Pegasus model <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

## Technical Implementation

The application is built using Streamlit, with core functionalities encapsulated in `app.py` and `utils.py` files <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Core Libraries and Setup
Necessary libraries include Streamlit, 12 Labs SDK, and `re` (for regular expressions) <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Essential environment variables, such as the 12 Labs API Key and Index ID, must be loaded <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. The API Key can be generated from the 12 Labs playground <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. When creating an index, both Maringo 2.6 and Pegasus models should be selected for open-ended generation <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Key Functions

#### Upload and Index
The `upload_and_index` function handles video file uploads (supporting MP4) and checks if the video has already been indexed <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The main functionality here involves `create_task` and `wait_for_task` functions, which manage the video indexing process <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. The `wait_for_task` function continuously monitors the task status (pending, indexing, ready) <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

#### MCQ Generation
Once indexing is complete, the application generates MCQs using `client.generate.text` from the 12 Labs SDK <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. The prompt structure provided to the model includes:
1.  **Role:** Defines the model's persona (e.g., "educational content analyzer") <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
2.  **Objective:** Specifies the task the model needs to perform <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
3.  **Response Format:** Requests the output in a JSON format with specific question (Q1, Q2, Q3), option, and correct answer keys <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
A robust JSON parsing mechanism using regular expressions is implemented to handle the model's response <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

#### User Score Calculation
The application also includes functionality to calculate the user's score based on their answers <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>, providing an end-to-end assessment <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

### Streamlit Application Flow
The `generate_quiz` function calls the MCQ generation logic <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Streamlit's session state is utilized to manage the quiz progression seamlessly without page refreshes <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Radio buttons display the answer options <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. Upon submission, visual feedback (balloons) is provided, and a reset state allows restarting the quiz <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. Custom CSS can be added for styling <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

## Demo Results
After indexing a PCA lecture video, the system successfully generated MCQs like:
*   "What is the primary focus of the video?" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>
*   "Which of the following statement about principal component analysis is true?" <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>
*   "What is the purpose of using PCA in regression?" <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>

The application displays user answers, correct answers, and can be extended to include detailed explanations <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Potential Use Cases
This technology has various [[use_cases_for_video_understanding | use cases for video understanding]], including:
*   Teachers or administrators creating assessments for students <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   Students practicing content they have learned <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   Video content creators or YouTubers generating quizzes for their audience <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.