---
title: Building video classification applications
videoId: 9f2mScVn5ck
---

From: [[hrishikeshyadav8883]] <br/> 

This article provides a walkthrough on how to build an Olympics Sports video clips classification application using [[Twelve Labs video embedding and retrieval | Twelve Labs]]. <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>

## Application Demo

The application allows users to classify video clips based on predefined or custom categories.

### Classifying Predefined Categories
Users can select from a list of predefined classes to retrieve top-classified videos. <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a> For example, selecting "Aquatic Sports" quickly yields results with video IDs, classified categories, and scores. <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a> <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a> Videos classified as "Aquatic Sports" might include a final swimming event. <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a> Similarly, selecting "Gymnastic events" will provide relevant gymnastic video results. <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>

### [[Creating custom classes for video classification | Creating Custom Classes]]
The application also supports adding new custom classes. <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a> For instance, a user can add "Wrestling" as a new class name, optionally providing a prompt like "wrestling competition". <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a> <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a> After adding and selecting the custom class, the application provides very specific classifications related to it, even if the category wasn't initially present as a combat sport. <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>

## Application Code Structure

The application is developed to be simple and easy to understand. <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>

### Dependencies
Essential dependencies include:
*   Streamlit for the application interface. <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a> (Install via `pip install streamlit`). <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>
*   [[Twelve Labs video embedding and retrieval | Twelve Labs]] SDK. <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   `requests`, `os`, and `dotenv`. <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>

### Key Components
*   **Page Elements**: Configures the background settings of the application. <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
*   **Predefined Classes**: Defined with various prompts to enhance classification, such as "swimming competition", "diving event", and "water polo match" for "Aquatic Sports". <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a> <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>
*   **Custom Class Storage**: Uses `st.cache_data` to store custom classes added by the user. <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a> Utility functions handle getting and adding custom classes. <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>
*   **Classification Endpoint (`classify_endpoint`)**: This is the main function that takes an `index_ID` (where video clips are stored in index form) and `selected_classes` as parameters. <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a> <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a> It classifies all videos present in the specified index. <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>
*   **Video URL Retrieval**: The classifier response provides video IDs and other parameters like thumbnail URL, score, and duration. <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a> To get the actual video URL, the `video_information` endpoint needs to be hit with the collected video IDs. <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>
*   **Video Rendering**: A utility function is used to render the video URLs, which are typically in `.m3u` format. <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>
*   **Main Function**: Manages the CSS, layout, and tab structure (e.g., "select classes" and "add custom classes") of the application. <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>

## [[Using Twelve Labs for video indexing | Creating an Index with Twelve Labs]]

To create an index for your video clips:
1.  Go to the [[Twelve Labs video embedding and retrieval | Twelve Labs]] playground. <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>
2.  Select the `marango 2.6` engine, which is suitable for power search and classification. <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a> The [[Pegasus 11 video analytics | Pegasus 1.1]] engine is also available but not needed for this classification task. <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>
3.  Choose the visual parameters for video analysis, such as "visual conversation" and "text in videos". <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
4.  Provide an appropriate name for your index, like "Olympics Clips 2", and click "create". <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>
5.  Upload videos directly to the created index. <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>
6.  Obtain the index ID from the URL after creation. <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>

> [!example] Index Details
> The "Olympic Clips" index used for the application has the `marango 2.6` engine and analyzes visual conversation and text within videos. <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>

## [[Use cases for video understanding | Use Cases]]

This video classification approach can be adapted to build various [[Video indexing and processing | video indexing and processing]] and search applications, including:
*   Video search engines. <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>
*   [[Automatic report generation from surveillance footage | Surveillance applications]]. <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>
*   Dance classifiers. <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>
*   Other [[Video segment generation and processing | video segment generation and processing]] and classification tasks. <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>

> [!info] Further Learning
> This example focuses on [[Evaluation of text to video models and applications | classification tasks]] but can be extended for other video understanding applications. <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>