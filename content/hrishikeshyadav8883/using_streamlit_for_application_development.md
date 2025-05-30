---
title: Using Streamlit for application development
videoId: 9f2mScVn5ck
---

From: [[hrishikeshyadav8883]] <br/> 

This article describes how to build an Olympics Sports video clips classification application using [[streamlit_application_development | Streamlit]]. The application allows users to select pre-defined sports categories or add custom ones to classify video clips.

## Application Overview

The demo application showcases a video classification system capable of identifying sports categories within video clips. Users can select from predefined classes such as "Aquatic Sports" or "Gymnastic events" to retrieve relevant videos <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The system provides immediate responses, displaying the video ID, its classified class, and a confidence score <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

A key feature is the ability to add custom classes, such as "wrestling," by providing a class name and a descriptive prompt <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This allows for very specific classifications, even if the category was not initially present in the dataset <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Building with Streamlit

The application is developed using [[streamlit_application_development | Streamlit]], which simplifies the frontend and interactive components <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### Installation

To set up [[streamlit_application_development | Streamlit]], users can create a virtual environment and install it using pip:
```bash
pip install streamlit
```
Official documentation is available for detailed installation instructions <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Key Components and Features

*   **Dependencies**: The application imports necessary dependencies, including the [[use_of_twelve_labs_sdk | Twelve Labs SDK]], `requests`, `os`, and `dotenv` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Background Setting**: A `page_element` is used for setting the background of the application <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Predefined Classes**: The application defines various sports categories (e.g., "Aquatic Sports") with multiple prompts (e.g., "swimming competition", "diving event", "water polo match") to enhance classification accuracy <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Custom Class Management**: The `st.cache_data` function is utilized to store custom classes added by the user, ensuring they persist across interactions <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Utility functions handle getting and adding these custom classes <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Video Classification Logic**:
    *   The `classify` endpoint is the core utility function, taking an `index_ID` (where video clips are stored) and `selected_classes` as parameters <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. It classifies all videos within the specified index <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
    *   Classification responses include video ID, thumbnail URL, score, duration, and ratio <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
    *   To retrieve the actual video URLs, a separate "video information" endpoint is hit using the collected video IDs <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   A utility function renders the video URLs, which are typically in m3u format <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Layout and UI**: The main function of the Streamlit application manages the CSS and layout, including tabbed sections for selecting classes and adding custom ones <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Index Creation with Twelve Labs

The application leverages [[using_twelvelabs_sdk_and_marango_engine | Twelve Labs]] for creating video indexes. This process is straightforward:
1.  Access the [[using_twelvelabs_sdk_and_marango_engine | Twelve Labs]] playground <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
2.  Select the **Marango 2.6** engine for power search and classification, as the application specifically focuses on classification <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
3.  Choose visual parameters like "visual conversation" and "text in videos" to be considered during indexing <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
4.  Provide an appropriate name (e.g., "Olympics Clips 2") and click "create" to generate the index <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
5.  Videos can then be directly uploaded to this index <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
6.  The `index_ID` can be retrieved from the URL of the created index in the [[using_twelvelabs_sdk_and_marango_engine | Twelve Labs]] playground <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

For the demo, an index named "Olympic Clips" was created with the Marango 2.6 engine, configured for visual conversation and text in video analysis <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

This approach can be applied to build various video search engines for use cases such as surveillance or dance classification <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.