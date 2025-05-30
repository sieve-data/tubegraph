---
title: Creating and managing indexes on Twelve Labs platform
videoId: J2vGUEEjHWI
---

From: [[hrishikeshyadav8883]] <br/> 

The [[twelvelabs_platform_and_capabilities | Twelve Labs platform]] allows users to create and manage indexes, which are essential for processing and analyzing video content <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Prerequisites

To interact with the [[twelvelabs_platform_and_capabilities | Twelve Labs platform]] and manage indexes, you will need:
*   An API Key <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This can be obtained from the [[twelvelabs_platform_and_capabilities | Twelve Labs playground]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   The API URL for the [[twelvelabs_platform_and_capabilities | Twelve Labs platform]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   An Index ID <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, which is generated after an index is created on the platform <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Steps to Create an Index

1.  **Access the Platform**: Navigate to the [[twelvelabs_platform_and_capabilities | Twelve Labs platform]] <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
2.  **Initiate Index Creation**: Click on "create an index" <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
3.  **Name the Index**: Assign a name to your new index, for example, "interview test" <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>, <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
4.  **Select an Engine**: The choice of engine depends on the intended use case:
    *   **Maringo 2.6**: This engine is suitable if you are only performing classification or search functions <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>, <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
    *   **Pegasus 2**: Select this engine if your application requires analyzing and generating text from the video content <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. For generative tasks, Pegasus 1.1 is also used <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
5.  **Finalize Creation**: Click "create" to finalize the index setup <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
6.  **Retrieve Index ID**: Once the index is ready, you can obtain its unique Index ID from the platform <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Indexing Process

After creating an index, recorded videos can be processed:
*   When a video is stored, a task is created to begin the [[video_indexing_and_processing | indexing process]] <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   A backend task checks every five seconds to monitor the [[video_indexing_and_processing | indexing progress]] <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   Once [[video_indexing_and_processing | indexing]] is complete, the recorded video has been indexed or embedded using the selected embedding engine (e.g., Maringo 2.6) <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>, <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>, <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   After embedding, the system is ready to use the generative engine (e.g., Pegasus 1.1) to hit the "generate" function, which typically involves structured prompts to analyze the video content <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>, <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

> [!NOTE]
> The entire [[video_indexing_and_processing | indexing process]] for a video may take approximately three to four minutes, or even less <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.