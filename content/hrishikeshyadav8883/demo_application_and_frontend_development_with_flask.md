---
title: Demo application and frontend development with Flask
videoId: J2vGUEEjHWI
---

From: [[hrishikeshyadav8883]] <br/> 

This article details the creation of an interview analyzer demo application, which is powered by Twelve Labs and built using Flask for the backend and a minimal frontend. The application aims to provide a straightforward way to analyze interview responses.

## Application Overview
The interview analyzer is designed for ease of use and serves as a foundation for a more extensive product <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

Key features include:
*   A "Start Interview" button to initiate the process <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   Randomly selected interview questions (e.g., "What are your great strengths?") <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   Automatic recording of responses <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   Analysis of the recorded video to provide metrics such as confidence, clarity, speech rate, voice tone, body language, and key points <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

## Backend Development with Flask
The application utilizes Flask to manage the backend functionalities, including API interactions, video processing, and data analysis.

### Dependencies
The Flask application requires several Python libraries:
*   `Flask`: For web framework capabilities <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   `Twelvelabs SDK`: For interacting with the Twelve Labs platform <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   `requests`: For making HTTP requests <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   `python-dotenv`: For loading environment variables (e.g., API keys) <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### API Integration
The application integrates with Twelve Labs services using API keys and index IDs <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. These can be obtained from the Twelve Labs playground <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

#### Creating a Twelve Labs Index
To analyze and generate text from videos, an index must be created on the Twelve Labs platform <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   For classification or search tasks, the `Maringo 2.6` model is typically selected <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   For analyzing and generating text, `Pegasus 2` is used <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
Once created, the index ID is provided for API interaction <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### Core Functionalities (Routes)
The Flask application defines several routes to manage different aspects of the interview process:

*   **`/` (Root Route)**: Renders the `index.html` template, which serves as the minimal frontend for the application <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. The complete frontend code is available on GitHub <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **`/get_question`**: This utility function randomly selects a question from a pre-defined list of interview questions <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **`/upload`**: This is the main functionality route responsible for processing the recorded interview video <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
    *   It utilizes the `Maringo 2.6` embedding engine and the `Pegasus 1.1` generative engine <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
    *   Once a video is recorded and stored, a processing task is created <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
    *   A backend task continuously checks the indexing status every five seconds <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   After indexing is complete, the generative engine is prompted to analyze the video <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

#### Prompt Structure for Analysis
The prompt sent to the generative model is structured to define its role and objective:
*   **Role**: Specifies the model's persona (e.g., "You are an interviewer") <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Objective**: Outlines the task to be performed (e.g., "analyze the video clip") <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Output Format**: Dictates the desired structure of the response, typically JSON, to facilitate application development <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

After the model generates a response, the application processes this response and displays the analysis results on the platform <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Frontend Development
The frontend is built with minimal HTML code, providing a user interface to interact with the Flask backend <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. The source code for the frontend is part of the overall project available on GitHub <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

## Potential Extensions
This demo application can be extended for various use cases:
*   Admin panels for managing multiple interviewees <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   Leaderboard systems for scoring and shortlisting candidates <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.