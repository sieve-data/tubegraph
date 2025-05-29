---
title: Downloading TikTok collections
videoId: VlQ4hGzydCc
---

From: [[humblelifeskills]] <br/> 

This article outlines a method for [[backing_up_content_from_social_media_platforms | backing up content]] from TikTok collections, particularly useful if a platform is at risk of being shut down <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The process involves scraping video URLs and then using command-line tools to download them <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Tools Required

The following programs are used for this process:
*   **axiom.ai**: A browser automation tool that can scrape data without code <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. It functions as a scraper to extract direct URLs from TikTok collection pages <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **ytdlp**: An open-source downloader <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, specifically used here for [[setting_up_and_using_ytdlp_for_downloading_videos | downloading videos]] in batch <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **aria2**: An external downloader that works with ytdlp <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. It's beneficial for chunking downloads based on your connection, potentially speeding up the process <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Custom JSON file**: A pre-configured JSON file (available for free download from wshforce.gumroad.com) which has the correct TikTok selector already defined for axiom.ai <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Step-by-Step Process with Axiom.ai

### 1. Obtain TikTok Collection URL
*   TikTok collection URLs cannot be accessed from the desktop <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   To get the URL, go into your collection on mobile, set it to publicly share, and then copy the link via the [[sharing_options_on_instagram | sharing options]] <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This link allows you to view your collection on a desktop browser <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### 2. Set Up Axiom.ai
*   Install the axiom.ai Chrome extension, which works with most browsers <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   Import the custom JSON file (downloaded from Gumroad) into axiom.ai <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This file pre-selects the necessary div table on a TikTok collection page <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
    *   To import, create a new blank automation in Axiom, go to the three buttons at the top > Settings > Share your Automation > Import an automation <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. The imported file will overwrite the blank task <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   Ensure the "Max results" setting in Axiom is higher than the total number of videos in your collection <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### 3. Run the Axiom Automation
*   The automation scrapes each video's direct URL by identifying the div elements on the page <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   You can optionally connect axiom.ai to a Google Sheet to output the scraped links <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. Alternatively, you can choose to display the links in a message with two columns <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   Run the automation by clicking "Run" at the top <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

## Downloading with ytdlp and Aria2

### 1. Prepare URL List
*   Once you have the list of direct TikTok video URLs (e.g., from a spreadsheet), copy them <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   Paste these URLs into a plain text file named `grab.txt` <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### 2. Execute Download
*   Use ytdlp, pointing it to the `grab.txt` file <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>, <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   Utilize aria2 as an external downloader to manage the batch downloads <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Aria2 helps by chunking the downloads, which can speed up the process <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. The video files are generally not very large, so chunking might not always be strictly necessary but is a good feature to have <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

This process allows you to download all your content to your own machine, ensuring you retain access to it even if a centralized platform like TikTok were to shut down unexpectedly <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. This was a common issue with Vine, where users lost years of content when the platform closed <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.