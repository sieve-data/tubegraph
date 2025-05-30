---
title: Security event detection with Twelve Labs
videoId: fHRdb8sGd-w
---

From: [[hrishikeshyadav8883]] <br/> 

This article explores a "Surveillance Analysis" application designed for CCTV footage analysis and detailed reporting, utilizing the [[twelvelabs_platform_and_capabilities | Twelve Labs platform]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The application aims to instantly pinpoint critical security events in surveillance footage, converting them into actionable insights <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## The Problem
Hours of surveillance footage often contain unnoticed critical security events <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The traditional method requires watching entire videos to find crucial moments like accidents or emergencies <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Solution Overview
The Surveillance Analysis tool provides a way to search and analyze video footage to extract specific incidents and generate detailed reports <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. It leverages the [[Integration of the Twelve Labs API | Twelve Labs API]] to perform searches <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Key Capabilities

### Intelligent Search and Identification
The application allows users to search for specific events, such as "car accident on Highway section" <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Search results display videos with a confidence score indicating the likelihood of the event being present <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. It also provides a green band indicating the particular timestamp where the incident occurred <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### Detailed Analysis and Reporting
For a detailed analysis of an incident, the system makes use of the Pegasus 1.1 model <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This model analyzes the video and provides an exact report describing what happened, why it happened, and details about the surrounding environment <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Users can view and download these reports <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Examples
*   **Car Accident**: A search for "car accident on Highway section" yields results showing road and car footage, often from dash cams <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. A detailed analysis might describe a truck carrying construction material causing a minor traffic jam <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **Paranormal Activity**: Searching for "Paranormal Activity identified" shows results from dark rooms or roads, focusing on abnormal activities <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Detailed analysis might describe static and unchanged environments, often associated with unoccupied spaces, and mention loud bangs <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

## Technical Implementation
The application is built as a Flask app with front-end HTML, CSS, and JavaScript <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. The showcased app is deployed on Render <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, and the code is available on Replit and GitHub <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Video Ingestion
Videos can be added in two ways:
1.  **Twelve Labs Playground**: Generate an API key, create an index with Pegasus 1.1, and directly upload videos <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
2.  **AWS S3 Integration**: For large volumes of footage stored in AWS S3 buckets, direct integration with [[twelvelabs_platform_and_capabilities | Twelve Labs]] is possible, connecting the index ID with the app <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Core Logic
The application utilizes the [[use_of_twelve_labs_sdk | Twelve Labs SDK]] to interact with the API <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

1.  **Search Function (`client.search`)**:
    *   Takes an `index_id` (containing indexed video footages) and a `query_text` (e.g., "car accident on the highway") <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
    *   `options` are set to `visual` <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
    *   Returns `video_id`, `score`, `confidence` (e.g., if > 0.7, it's high), `start` and `end clip` timestamps, and `video_URL` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. This represents the first stage of analysis <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

2.  **Report Generation (`client.generate.text`)**:
    *   For the second stage, generating detailed analytics, the Pegasus 1.1 model is used <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   `client.generate.text` provides an open-ended prompt <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
    *   When "detailed analysis" is clicked, the video ID is passed with a prompt: "Provide a detailed analysis of the key events, actions and notable elements in this video" <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
    *   This generates a proper detailed report <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

3.  **PDF Report Generation**:
    *   A `report_generator.py` file handles PDF creation using the ReportLab library <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
    *   The analysis text and other information are sent to a `generate_report` route to create the PDF <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

## Use Cases
Beyond the demonstrated examples, this tool can be adapted for various applications requiring video intelligence <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Potential use cases include:
*   Surveillance operator support <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>
*   [[Security management and analytics applications | Security analytics]] <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>
*   Private security operations <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>
*   Automated documentation and report generation <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>
*   Traffic surveillance and management <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>