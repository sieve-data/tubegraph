---
title: Use of Twelve Labs SDK
videoId: z-_PJqjTZmM
---

From: [[hrishikeshyadav8883]] <br/> 

The [[TW Labs SDK integration | Twelve Labs SDK]] is instrumental in building applications that process and analyze video content, such as a YouTube chapter timestamp generator <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The entire application discussed is built on Streamlit, with file management handled by `tempfile` and core operations contained in `utils.py` <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>, <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>, <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Key Features and Operations

The application leverages the [[TW Labs SDK integration | Twelve Labs SDK]] for several functionalities:
*   **Initialization** The [[TW Labs SDK integration | Twelve Labs SDK]] client is initialized to interact with the [[twelvelabs_platform_and_capabilities | Twelve Labs platform]] <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Video Processing** The `process_video` function in `utils.py` is called, sending the client, video path, and video type (e.g., less than 30 minutes, or a longer "podcast" type) to handle video ingestion and processing <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>, <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>, <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Generating Timestamps and Chapters** The `client.generate_summarize` function is specifically used to create video chapters by setting the `type` parameter to 'chapter' <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>, <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>, <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. The raw timestamp results, provided in seconds, are then converted into a `minute:second` format suitable for YouTube highlights <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>, <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>, <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Fetching Existing Videos** The SDK provides an API for fetching existing videos, which only requires the `index ID` <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>, <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. This allows users to regenerate timestamps or segments for previously uploaded videos <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>, <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>, <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

## Setup and Configuration

To utilize the [[TW Labs SDK integration | Twelve Labs SDK]], two essential environment variables are needed: `API key` and `index ID` <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>, <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Obtaining API Key and Index ID

*   **API Key Generation** Users can generate their API key from the [[twelvelabs_platform_and_capabilities | Twelve Labs playground]] <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>, <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   **Index Creation** An index needs to be created on the [[twelvelabs_platform_and_capabilities | Twelve Labs platform]], typically by selecting the `Marango 2.6` engine for embedding and `Pegasus 1.1` engine for analysis <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>, <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. All videos pushed for embedding or [[using_twelvelabs_for_video_indexing | indexing]] will reside within this designated `index ID` <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

## Integration with Other Libraries

The [[TW Labs SDK integration | Twelve Labs SDK]] works in conjunction with other Python libraries:
*   `moviepy.editor`: Used for handling timestamp-based cutting and segmenting videos <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>, <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>, <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   `m3u8 library`: Used for manipulating `.m3u8` video streams which are initially retrieved from embedded videos <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>, <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   `YT-DLP`: Used for downloading videos from URLs, enabling local segmentation <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>, <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.