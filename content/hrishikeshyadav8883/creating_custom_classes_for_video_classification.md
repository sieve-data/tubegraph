---
title: Creating custom classes for video classification
videoId: 9f2mScVn5ck
---

From: [[hrishikeshyadav8883]] <br/> 

Video classification applications can be enhanced by allowing users to define custom classes, enabling more specific and tailored content retrieval and analysis. This approach allows for detailed categorization beyond pre-defined categories <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## Demo: Adding a Custom Class
To add a new custom class within a video classification application, a user can provide a **class name** and a corresponding **prompt** <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

For example, to classify "wrestling" events:
1.  Enter "wrestling" as the class name <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
2.  Provide a specific prompt, such as "wrestling competition" <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  Click "add custom" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

Once added, selecting the "wrestling" class and initiating the classification process will retrieve highly specific videos related to wrestling, even if this category was not pre-defined <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Under the Hood: Technical Implementation
The process involves several key components:

### Dependencies
Essential dependencies for [[building_video_classification_applications | building video classification applications]] include:
*   Streamlit for the application interface <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] SDK <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   `requests` and `os` for general utilities <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   `python-dotenv` (`Env`) for environment variables <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### Class Storage and Retrieval
To ensure custom classes persist and are accessible across user sessions, they are stored.
```python
st.cache_data
```
The `st.cache_data` decorator is used to store custom classes added by the user <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Utility functions handle getting and adding these custom classes <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Classification Endpoint
The core functionality for classification relies on a `classify` endpoint, which takes an [[using_twelve_labs_for_video_indexing | index]] ID and the `selected_classes` (including custom ones) as parameters <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This endpoint processes all videos within the specified [[using_twelve_labs_for_video_indexing | index]] and returns classification results <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Video Retrieval and Rendering
After classification, the application receives video IDs, scores, and other metadata <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. To display the videos, a separate endpoint (`video_information_two`) is hit using the collected video IDs to obtain their URLs <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. A utility function then renders these video URLs, which are typically in m3u format <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Index Creation
An [[using_twelve_labs_for_video_indexing | index]] is a crucial part of the process, storing all video clips for classification <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   Indices can be created through the [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] playground <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   The `Marango 2.6` engine is recommended for power search and classification <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   Visual parameters such as "visual conversation" and "text in videos" should be considered when creating the [[using_twelve_labs_for_video_indexing | index]] <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   Videos can be uploaded directly to the created [[using_twelve_labs_for_video_indexing | index]] <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

Creating custom classes allows for a more versatile [[building_video_classification_applications | video classification application]], suitable for various [[use_cases_for_video_understanding | use cases]] like building custom video search engines or even specialized classifiers like dance classifiers <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.