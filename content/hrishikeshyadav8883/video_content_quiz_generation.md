---
title: Video content quiz generation
videoId: kBuuFu2WNkg
---

From: [[hrishikeshyadav8883]] <br/> 

A video content quiz generator is an application designed to automatically create multiple-choice questions (MCQs) from video content for assessment purposes <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This tool analyzes the video content and generates quizzes based on its visual and conversational elements <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## How it Works

The process involves several key stages, primarily leveraging [[Twelve Labs video embedding and retrieval | Twelve Labs]] technology <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>:

### Video Processing and Indexing

1.  **Video Upload**: Users upload educational or content videos, ideally around 20-30 minutes long for optimal performance <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Longer videos can be trimmed into multiple segments <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
2.  **Indexing**: Once uploaded, the [[video_segment_generation_and_processing | indexing process]] begins <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
    *   The Marango 2.6 embedding engine from [[Twelve Labs video embedding and retrieval | Twelve Labs]] is used to embed and index the video content <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
    *   This process involves analyzing both the visuals and the conversation/text within the video <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
    *   The Pegasus model is then used to generate text from this analyzed content <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
3.  **Task Management**: The system tracks the status of the indexing task (pending, indexing, ready) to ensure completion before quiz generation <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Quiz Generation

1.  **MCQ Generation**: After indexing, the system generates MCQs using `client.generate.text` from the [[Twelve Labs video embedding and retrieval | Twelve Labs]] SDK <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
2.  **Prompt Structure**: The generation process relies on a structured prompt given to the model <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>:
    *   **Role**: Assigns a behavior, such as "educational content analyzer" <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
    *   **Objective**: Specifies what the model needs to do (e.g., generate quiz questions) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
    *   **Response Format**: Defines the desired output structure, typically a JSON format with questions (e.g., Q1, Q2, Q3), options, and the correct answer for each <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
3.  **JSON Parsing**: The raw JSON response from the model is parsed using regex to ensure robustness <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Technical Details

The application is built using a [[automating_content_creator_workflows | Streamlit]] framework, incorporating [[Twelve Labs video embedding and retrieval | Twelve Labs]] for video intelligence <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Libraries and Tools

*   **[[automating_content_creator_workflows | Streamlit]]**: Used for building the web application interface <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **[[Twelve Labs video embedding and retrieval | Twelve Labs]] SDK**: Provides functionalities for video indexing, embedding (Marango 2.6), text generation (Pegasus), and quiz generation <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. API keys and index IDs are obtained from the [[Twelve Labs video embedding and retrieval | Twelve Labs]] playground <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   **Regex**: Utilized for parsing the JSON formatted MCQs to ensure accurate data extraction <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Code Structure

*   **`app.py`**: The main application file running on platforms like Replit, handling UI, video upload, and calling quiz generation functions <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **`utils.py`**: Contains core functionalities, including:
    *   Initializing the [[Twelve Labs video embedding and retrieval | Twelve Labs]] client <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   Handling API key and index ID configuration <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   Functions for creating and waiting for indexing tasks (`create_task`, `wait_for_task`) <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    *   The `generate_mcq` function, which structures the prompt and calls `client.generate.text` <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
    *   Parsing JSON responses and calculating user scores <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Session State**: [[automating_content_creator_workflows | Streamlit]]'s session state (`st.session_state`) is used to manage the quiz flow without page refreshes, maintaining consistency <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Demo Example

In a demonstration, a video about Principal Component Analysis (PCA) was uploaded <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. After indexing was complete <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>, the application generated MCQs specific to the PCA concept, such as "What is the primary focus of the video?" and "What is the purpose of using PCA in regression?" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. The application also calculates the user's score based on their answers <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## Potential Applications

This technology has diverse applications <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, including:

*   **Educational Assessments**: Teachers and administrators can use it to create assessments for students <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   **Student Practice**: Students can practice and test their understanding of learned content <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Content Creators/YouTubers**: [[automating_content_creator_workflows | Content creators]] or [[Video content recommendation engine | YouTubers]] can generate quizzes related to their videos for audience engagement or content reinforcement <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.

The flexibility of the prompt structure allows for detailed answers or conceptually rich explanations to be integrated into the quiz format <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.