---
title: Backing up content from social media platforms
videoId: VlQ4hGzydCc
---

From: [[humblelifeskills]] <br/> 

This guide outlines a method for backing up content, specifically from TikTok, using a combination of automation and download tools. The approach aims to provide users with a way to secure their content on their own machines, mitigating the risk of losing access if a platform were to shut down <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, a concern highlighted by past platform closures like Vine <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

## Tools Required

The process involves three main tools:
*   **Axiom.ai:** A browser automation tool used to scrape direct URLs from TikTok collection pages <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It functions as a scraper to extract the links <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **ytdlp:** An open-source downloader for batch downloading content from a list of URLs <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **aria2:** An external downloader that works in conjunction with ytdlp to manage downloads efficiently, including chunking based on connection speed <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## Step-by-Step Content Backup Process

### 1. Prepare Your TikTok Collection

Before using Axiom.ai, you must access your TikTok video collections.
*   **Mobile Access:** TikTok collection URLs are accessible from mobile devices, not directly from desktop <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Public Sharing:** To obtain the collection URL, you need to go into your collection on mobile, [[sharing_options_on_instagram | publicly share it]], and copy the link <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This link allows Axiom.ai to view your collection <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### 2. Set Up Axiom.ai for URL Extraction

Axiom.ai is a browser automation tool that can be installed as a Chrome extension and works with most browsers <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Download the JSON File:** Obtain a pre-configured JSON file (specifically for TikTok collection scraping) from assetstoday.gumroad.com <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. This file is a free download <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   **Import into Axiom.ai:**
    1.  Open Axiom.ai through its browser tab extension <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    2.  Create a new, blank automation <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
    3.  Go to the three buttons at the top, select "Settings," then "Share your Automation," and choose "Import an automation" <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    4.  Import the downloaded JSON file <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This will configure Axiom.ai to find the specific "div" elements on the TikTok collection page that contain the video URLs <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. The JSON file automatically selects the correct div <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Configure Axiom.ai Run:**
    1.  Ensure the "Max results" setting within Axiom.ai is higher than the total number of videos in your TikTok collection <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
    2.  You can optionally connect Axiom.ai to a Google Sheet to automatically generate a spreadsheet of the URLs <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. Alternatively, you can opt to display the links as a message <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
    3.  Run the automation <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This will scrape the direct URLs for each video in your collection <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### 3. Download Content with ytdlp and aria2

Once you have the list of direct URLs (either from a spreadsheet or displayed message):
*   **Create a Batch File:** Copy all the collected URLs into a text file, for example, `grab.txt` <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>, <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Run ytdlp:** Use ytdlp to point to this text file, initiating a batch download of all the videos <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>, <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Utilize aria2:** Incorporate aria2 as an external downloader to manage the downloading process more efficiently, especially for chunking and faster downloads <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>, <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

This process ensures that your content, which you created and deserve to have on your own machine, is backed up and safe from potential platform shutdowns <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.