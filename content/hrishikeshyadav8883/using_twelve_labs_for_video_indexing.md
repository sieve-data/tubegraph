---
title: Using Twelve Labs for video indexing
videoId: kBuuFu2WNkg
---

From: [[hrishikeshyadav8883]] <br/> 

This article discusses how to build a [[video_indexing_and_processing | video content quiz generator]] by leveraging [[TwelveLabs platform and capabilities | Twelve Labs]] to analyze video content and automatically generate multiple-choice questions for assessment purposes <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Overview of the Application

The application is built using Streamlit <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a> and runs on Replit <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. It supports MP4 video uploads <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. For optimal performance, video content should ideally be around 20-30 minutes long; longer videos can be trimmed into multiple segments <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## [[Video indexing and processing | Video Indexing]] Process with [[TwelveLabs platform and capabilities | Twelve Labs]]

Upon video upload, the [[video_indexing_and_processing | indexing process]] begins immediately <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. [[TwelveLabs platform and capabilities | Twelve Labs]] utilizes specific embedding engines for this:

*   **Maringo 2.6**: This engine is used for [[Twelve Labs video embedding and retrieval | embedding]] and [[video_indexing_and_processing | indexing]] the uploaded video <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Pegasus**: After [[video_indexing_and_processing | indexing]], Pegasus generates text based on a thorough analysis of the video's visuals and conversations <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Core Functionalities for [[Video indexing and processing | Indexing]]

The application's `utils.py` file contains the essential functions for interacting with the [[Integration of the Twelve Labs API | Twelve Labs API]] and managing the [[video_indexing_and_processing | indexing]] workflow:

*   **Necessary Imports**: Includes `twelvelabs` for [[Integration of the Twelve Labs API | API interaction]] and `re` (rejects) for parsing JSON responses <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **API Key and Index ID**:
    *   An API Key can be generated from the [[TwelveLabs platform and capabilities | Twelve Labs]] playground <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   An Index ID must be created in the [[TwelveLabs platform and capabilities | Twelve Labs]] playground, ensuring both Maringo 2.6 and Pegasus are selected for open-ended generation <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This Index ID is then stored in the application to direct where uploaded videos will be indexed <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Initializing the Client**: The [[TwelveLabs platform and capabilities | Twelve Labs]] client is initialized <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Temporary Directory**: A temporary directory is created for uploaded files <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **`createTask`**: This function initiates the [[video_indexing_and_processing | indexing]] task by specifying the Index ID and the local file path of the uploaded video <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **`waitForTask`**: This function monitors the task status, which progresses from "pending" to "indexing" and finally "ready" <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. It continuously checks until the task is ready <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

## Generating MCQs after [[Video indexing and processing | Indexing]]

Once [[video_indexing_and_processing | indexing]] is complete, the application proceeds to generate multiple-choice questions (MCQs):

*   **`client.generate.text`**: The [[Use of Twelve Labs SDK | SDK's]] `client.generate.text` function is used for this purpose <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Prompt Structure**: The prompt provided to the model follows a structured format:
    *   **Behavior/Role**: Defines the model's role (e.g., "educational content analyzer") <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
    *   **Objective**: Specifies the task the model needs to perform <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
    *   **Response Format**: Dictates the desired output format, typically JSON, including questions (Q1, Q2, Q3), options, and the correct answer for each <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Parsing JSON with RegEx**: The `parseJsonWithRegex` utility function ensures robust parsing of the JSON response from the model <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

This application provides an end-to-end solution for video content assessment, useful for teachers, students, or content creators <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.