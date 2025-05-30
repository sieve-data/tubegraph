---
title: Using Twelvelabs SDK and Marango engine
videoId: 9f2mScVn5ck
---

From: [[hrishikeshyadav8883]] <br/> 

This article explores how to build an Olympics Sports video clip classification application using the [[use_of_twelve_labs_sdk | Twelve Labs SDK]] and the [[functionality_of_pegasus_and_maringo_engines | Marango engine]].

## Application Demonstration

The application allows users to classify Olympic sports video clips by selecting predefined categories or adding custom ones <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

### Classification Process
When a category like "Aquatic Sports" is selected, the application queries an index where videos are stored <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>. It rapidly retrieves and displays top classified videos related to the selected category, showing video ID, classification, and score <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>. For example, selecting "Aquatic Sports" returns videos related to swimming events <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>, and selecting "Gymnastic events" provides relevant gymnastics clips <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>.

### Adding Custom Classes
Users can add new custom classes, such as "Wrestling," by providing a class name and an associated prompt (e.g., "wrestling competition") <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>. The application then classifies videos based on this new custom category, even if it wasn't a pre-existing combat sport classification <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

## Code Implementation Overview

The application is developed using Streamlit and leverages the [[tw_labs_sdk_integration | Twelve Labs SDK]].

### Key Dependencies
Essential dependencies include `streamlit` for the application interface, the [[use_of_twelve_labs_sdk | Twelve Labs SDK]], `requests`, `os`, and `dotenv` <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

### Core Functions
*   **Predefined Classes**: Initial classes like "Aquatic Sports" are defined with various prompts such as "swimming competition," "diving event," or "water polo match" <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.
*   **Custom Class Storage**: Custom classes added by users are stored using `st.cache_data` <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.
*   **Classification Endpoint**: The main utility function utilizes the `classify` endpoint, which takes an `index ID` and `selected classes` as parameters. The `index ID` specifies the location where video clips are stored <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.
*   **Video URL Retrieval**: After classification, video IDs are collected, and the `video information 2` endpoint is hit to retrieve the video URLs <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. These URLs, typically in M3U format, are then rendered for display <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

## Twelve Labs Index Creation with Marango Engine

To classify videos, an index must first be created on the [[twelvelabs_platform_and_capabilities | Twelve Labs playground]] <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.

### Engine Selection
When creating an index, users can choose between [[model_engines_used_marango_and_pegasus | Marango 2.6]] and [[use_of_pegasus_11_and_meringo_26_engines | Pegasus 1.1]] engines <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>. For classification tasks, the [[functionality_of_pegasus_and_maringo_engines | Marango]] engine is used, as it is designed for power search and classification <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>.

### Visual Parameters
When setting up an index, visual parameters can be configured. For video classification, "visual conversation" and "text in videos" are considered important <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>.

### Index Configuration Example
An index named "Olympics Clips 2" was created using the [[use_of_pegasus_11_and_meringo_26_engines | Marango 2.6]] engine, configured with "visual conversation" and "text in video" parameters <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. Videos can be directly uploaded to this index, and its index ID can be retrieved from the URL <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>.

## Potential Use Cases
This video classification approach can be adapted to build various [[building_an_interview_analyzer_with_twelve_labs | video search engines]] for diverse use cases, such as surveillance, or even for fun applications like a dance classifier <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>.