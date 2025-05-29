---
title: Setting up and using ytdlp for downloading videos
videoId: VlQ4hGzydCc
---

From: [[humblelifeskills]] <br/> 

ytdlp is an open-source software tool primarily used for downloading video content <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. It is particularly useful for backing up personal content from online platforms <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Purpose of ytdlp

The main purpose of using ytdlp is to download and back up content that you have created and uploaded to centralized platforms, ensuring you retain copies on your own machine <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. This is critical because centralized platforms can shut down unexpectedly, leading to the loss of your content, as observed with platforms like Vine <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>, <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

## Workflow for Downloading TikTok Content

The process described involves a multi-tool approach to download content, specifically TikTok videos:

1.  **Extracting URLs with axiom.ai**:
    *   A JSON file from `wshforceaxiom` (a free download) is imported into axiom.ai, a browser automation tool <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This file pre-selects the necessary `div` table on a TikTok collection page <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
    *   To get the collection URL, you must access your collection on mobile, publicly share it, and copy the link <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
    *   Axiom.ai scrapes the direct URLs of videos from the specified collection page <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>, <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   The scraped URLs can be output to a Google Sheet (if connected) or displayed as a message with two columns of links <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   Ensure the "Max results" setting in axiom.ai is higher than the number of videos in your collection <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
2.  **Preparing the Batch File**:
    *   Once the URLs are extracted, they are copied into a text file, typically named `grab.txt` <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>, <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  **Downloading with ytdlp**:
    *   ytdlp is then used to process this `grab.txt` file <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
    *   The command points ytdlp to this external text file, allowing it to download the videos in a batch <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>, <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
    *   For faster downloads or if dealing with larger files, ytdlp can be configured to use [[using_aria2_as_an_external_downloader|Aria2]] as an external downloader <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. [[using_aria2_as_an_external_downloader|Aria2]] handles chunking based on your connection <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

> [!NOTE]
> The JSON file for axiom.ai, which includes the TikTok selector, can be obtained for free from `assetstoday.gumroad.com` <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

This method allows users to quickly and efficiently download their content to their local machines, ensuring they have a personal backup of their digital legacy <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.