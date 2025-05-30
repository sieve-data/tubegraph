---
title: Integration of the Twelve Labs API
videoId: J2vGUEEjHWI
---

From: [[hrishikeshyadav8883]] <br/> 

This article details the [[tw_labs_sdk_integration | integration]] of the [[twelvelabs_platform_and_capabilities | Twelve Labs API]] to [[building_an_interview_analyzer_with_twelve_labs | build an interview analyzer]]. The process demonstrates how easily the API can be used to develop a full-fledged product for users <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Core Application Structure
The interview analyzer is built as a Flask application, utilizing Flask and `dotenv` for environment variable loading <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The front-end is minimal, consisting of an `index.html` template <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. The complete code for the application is available on GitHub <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

## Twelve Labs API Key and Index Configuration
To integrate the [[twelvelabs_platform_and_capabilities | Twelve Labs platform]], users need an API key, which can be obtained from the [[twelvelabs_platform_and_capabilities | Twelve Labs playground]] <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The integration also requires an API URL and an index ID <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### [[creating_and_managing_indexes_on_twelve_labs_platform | Creating and Managing Indexes]]
An index ID is obtained after [[creating_and_managing_indexes_on_twelve_labs_platform | creating an index on the Twelve Labs platform]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
The steps to [[creating_and_managing_indexes_on_twelve_labs_platform | create an index]] are:
1.  Navigate to the [[twelvelabs_platform_and_capabilities | Twelve Labs platform]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
2.  Click "create an index" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
3.  Assign a name to the index, such as "interview test" <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
4.  Select the appropriate engine:
    *   For classification or search functionality, Maringo 2.6 is used <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
    *   For analysis and text generation, Pegasus 2 is selected <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
5.  After creation, the index ID becomes available <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Video Processing and Analysis Workflow
The main functionality of the application involves video upload, indexing, and analysis using the [[use_of_twelve_labs_sdk | Twelve Labs SDK]].

### Video Upload and Indexing
When a video is recorded and stored, a task is created for its processing <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The backend continuously checks the status of this task every five seconds to ensure [[using_twelve_labs_for_video_indexing | video indexing]] is progressing <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. The [[twelve_labs_video_embedding_and_retrieval | embedding engine]], Maringo 2.6, is used to index or embed the recorded video <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Generative Analysis and Prompt Structure
Once [[using_twelve_labs_for_video_indexing | indexing]] is complete, the generative engine, Pegasus 1.1, is utilized to hit the `generate` endpoint for analysis <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. The key to this process is the prompt structure, which informs the model of its role and objective:
*   **Role:** Defines the model's persona (e.g., "You are an interview interviewer") <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Objective:** Specifies the task to be performed (e.g., "analyze the video clip of the interview") <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Response Format:** Crucially, the prompt dictates the desired format of the response, such as a JSON object, to facilitate application development <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Analysis Results
After processing, the [[twelvelabs_platform_and_capabilities | Twelve Labs API]] provides detailed analysis results shown on the application's platform <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. These results include metrics such as:
*   Confidence (e.g., 8) <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>
*   Clarity (e.g., 9) <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>
*   Speech rate (e.g., 7) <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>
*   Voice tone <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>
*   Body language assessment <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>
*   Key points extracted from the interview, tailored to the specific question asked <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>

## Extensibility
This demo application showcases the ease of [[tw_labs_sdk_integration | integrating the Twelve Labs API]] <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. It can be extended to support advanced features like managing interviews for multiple people, generating leaderboards for shortlisting candidates, or other similar functionalities <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

## Support
For any questions or further assistance, users can post on the [[twelvelabs_platform_and_capabilities | Twelve Labs]] Discord channel <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.