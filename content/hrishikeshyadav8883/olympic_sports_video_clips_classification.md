---
title: Olympic sports video clips classification
videoId: 9f2mScVn5ck
---

From: [[hrishikeshyadav8883]] <br/> 

This article demonstrates how to build an application for [[building_video_classification_applications | classifying video clips]] of Olympic sports using [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The application allows users to select pre-defined sports categories or add custom ones to retrieve relevant video content <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Application Demo Overview

The demo showcases a user interface where users can select classes to classify and retrieve top videos <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### Pre-defined Class Classification
When a sport like "Aquatic Sports" is selected, the application quickly processes the request and returns classified videos <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The response includes the video ID, the classified class, and a score <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. For example, selecting "Aquatic Sports" retrieves videos related to swimming competitions <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Similarly, selecting "Gymnastic Events" provides relevant gymnastics videos <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### [[creating_custom_classes_for_video_classification | Custom Class]] Classification
The application also supports adding new custom classes <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. For instance, a user can add "Wrestling" as a new class along with a prompt like "wrestling competition" <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. After adding the custom class, the system can classify and retrieve videos specifically related to wrestling, offering a very specific classification <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## Application Code Structure

The application's development is straightforward <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### Dependencies
Necessary dependencies include Streamlit for the application interface, the [[twelve_labs_video_embedding_and_retrieval | Twelve Labs SDK]], `requests`, `os`, and `Env` <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Streamlit can be installed via `pip install streamlit` <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Core Components
*   **Background Setting**: `page_element` is used for the application's background settings <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Pre-defined Classes**: Initial classes like "Aquatic Sports" are defined with various prompts such as "swimming competition," "diving event," and "water polo match" <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Custom Class Storage**: `st.cache_data` is used to store any custom classes added by the user, ensuring they persist <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Utility functions handle getting and adding these custom classes <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Classification Endpoint**: The main utility function utilizes the `classify` endpoint, which takes an `index_ID` (where video clips are stored in index form) and `selected_classes` as parameters <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This function classifies all videos within the specified index <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Video URL Retrieval**: The `classify` response provides video IDs, but to get the actual video URL, the `video_information` endpoint needs to be hit <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. This endpoint is used to collect the video IDs and retrieve their `m3u` formatted URLs <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Video Rendering**: A utility function is responsible for rendering the video content <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **User Interface**: The main function handles the CSS, layout, and tabs (for selecting classes and adding custom ones) of the application <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Creating an Index with Twelve Labs

To classify videos, an index needs to be created in the [[twelve_labs_video_embedding_and_retrieval | Twelve Labs playground]] <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### Index Configuration
*   **Engine Selection**: For classification and search, the `Marango 2.6` engine is required <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Another engine, [[pegasus_11_video_analytics | Pegasus 1.1]], is also available <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   **Visual Parameters**: Critical visual parameters for video analysis include "visual conversation" and "text in videos" <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **Index Creation**: By selecting the engine and visual parameters and providing a name (e.g., "Olympics Clips 2"), an index can be created <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Video Upload and Index ID**: Videos can be directly uploaded to the created index, and the index ID can be retrieved from the URL <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. An example index named "Olympic Clips" utilizes the `Marango 2.6` engine with visual conversation and text in video features enabled <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

## [[use_cases_for_video_understanding | Use Cases]]

This classification task can be applied to various scenarios beyond Olympic sports, such as:
*   Building a video search engine <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   [[cctv_footage_analysis | Surveillance]] applications <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   Developing a dance classifier <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   Solving any type of general video classification use case <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.