---
title: Building an interview analyzer with Twelve Labs
videoId: J2vGUEEjHWI
---

From: [[hrishikeshyadav8883]] <br/> 

An interview analyzer application, powered by [[twelvelabs_platform_and_capabilities | Twelve Labs]], can be built to evaluate interview responses. This application demonstrates the ease of integrating [[integration_of_the_twelve_labs_api | Twelve Labs]] capabilities to create a full-fledged product for user interaction <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Application Overview

The application features a "start interview" button that, when clicked, flashes a random question from a predefined list, such as "What are your great strengths?" <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. After a short delay, recording begins, allowing the user to provide their answer <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Core Functionality

The main functionality revolves around the `upload` process, which leverages [[twelvelabs_platform_and_capabilities | Twelve Labs]]'s engines for analysis <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Key Components

*   **API Connection**: The application uses API keys and URLs obtained from the [[twelvelabs_platform_and_capabilities | Twelve Labs playground]] <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Index Creation**: To enable video analysis, an index must be created on the [[twelvelabs_platform_and_capabilities | Twelve Labs platform]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   For classification or search, `Maringo 2.6` is selected <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
    *   For analysis and text generation, `Pegasus 2` is chosen <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   After creation, an index ID is generated and used in the application <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Video Processing**:
    *   The recorded video is stored <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
    *   A backend task is initiated to check the [[using_twelvelabs_for_video_indexing | indexing]] status every five seconds <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
    *   Once [[using_twelvelabs_for_video_indexing | indexing]] is complete, meaning the video has been embedded using the [[embedding_techniques_with_twelve_labs_and_milvus | embedding engine]] (Maringo 2.6) <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>, the application proceeds to generate analysis using the generative engine (Pegasus 1.1) <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Prompt Structure for Analysis

The prompt structure for the [[twelve_labs_video_embedding_and_retrieval | generative engine]] is crucial for obtaining desired analytical results <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. It typically includes:

1.  **Role Definition**: Assigning a role to the model, e.g., "You are an interviewer" <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
2.  **Objective**: Specifying the task, e.g., "analyze the video clip of the interview" <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
3.  **Response Format**: Defining the required format for the output, such as JSON <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Analysis Results

After processing, the application displays analysis results, which may include metrics like:
*   Confidence (e.g., 8) <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>
*   Clarity (e.g., 9) <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>
*   Speech rate (e.g., 7) <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>
*   Voice tone <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>
*   Body language assessment <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>
*   Key points from the response (e.g., "explained the concept clearly," "used appropriate examples," "maintained eye contact") <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>

## Technical Implementation

The application is built using a Flask framework, with dependencies such as Flask, Dotenv (for environment variables), and Requests <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The frontend is minimal, rendered via `index.html` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. The complete code is available on GitHub and linked in the related blog post <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

## Extensibility

This demo application can be extended for various purposes, such as:
*   Taking interviews for multiple people <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>
*   Generating leader board scores for shortlisting candidates <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>

For further queries, users can post on the [[twelvelabs_platform_and_capabilities | Twelve Labs]] Discord channel <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.