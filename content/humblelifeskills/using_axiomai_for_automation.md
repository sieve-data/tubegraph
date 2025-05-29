---
title: Using Axiomai for automation
videoId: VlQ4hGzydCc
---

From: [[humblelifeskills]] <br/> 

Axiom.ai is a browser automation tool that allows users to perform tasks quickly without needing to write code <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. It functions by automating interactions within a web browser and is available as a Chrome extension, compatible with most browsers <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Purpose of Axiom.ai

The primary use case described for Axiom.ai is to extract content, specifically direct URLs of videos, from TikTok collection pages <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This enables users to create a spreadsheet of these URLs, which can then be used with external downloaders like ytdlp and [[using_aria2_as_an_external_downloader | Aria2]] to download the content <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. The goal is to allow users to back up their content from centralized platforms, especially in case of potential shutdowns <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Tools Used with Axiom.ai

Alongside Axiom.ai, the process involves:
*   **ytdlp**: An open-source piece of software used as a downloader <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
*   **[[using_aria2_as_an_external_downloader | Aria2]]**: An external downloader that processes lists of URLs in batches and can download files faster by chunking them based on connection <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## How to Use Axiom.ai for TikTok Content Retrieval

### 1. Obtain the Axiom.ai JSON File
A pre-configured JSON file, specifically designed for TikTok collection pages, is available for free download from `asset today.gomroad.com` <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>, <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This file contains the necessary TikTok selector already defined <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### 2. Install the Axiom.ai Chrome Extension
Install the Axiom.ai Chrome extension, which works with most browsers <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### 3. Get Your TikTok Collection URL
TikTok collections cannot be accessed from a desktop browser <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. To obtain the URL for your collection:
*   Go into your collection on the TikTok mobile app <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   Publicly share the collection <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   Copy the sharing link <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
This link will allow Axiom.ai to view your collection <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### 4. Import the JSON Automation into Axiom.ai
*   Navigate to your TikTok collection page in the browser <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Click on the Axiom.ai browser extension icon <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   To import the downloaded JSON file:
    *   Create a new blank automation <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
    *   Go to the three buttons at the top of the Axiom.ai interface <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   Select "Settings" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   Choose "Share your Automation" <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Click "Import an automation" and select the downloaded JSON file <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. This will overwrite the blank task <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

### 5. Configure and Run the Automation
*   The imported JSON automatically selects the necessary `div` elements on the TikTok page, which contain the direct video URLs <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>, <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   Ensure that the "Max Max results" setting is higher than the total number of videos in your collection <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   You can connect Axiom.ai to your Google Sheet to export the list of links <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>, or you can cancel this step and display the links directly as a message with two columns <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Run the automation by clicking "Run it" at the top <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>, <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. It will run in the cloud <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### 6. Download Content with ytdlp and Aria2
*   Once Axiom.ai provides the list of direct TikTok video URLs, copy these links into a text file, for example, named `grab.txt` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>, <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   Use ytdlp and point it to this text file, allowing it to process the URLs in a batch <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>, <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>, <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   [[using_aria2_as_an_external_downloader | Aria2]] can be used as an external downloader to go through the list batch by batch, facilitating faster downloads <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

This method provides a way to secure content that has been uploaded to centralized platforms, ensuring personal access even if the platform were to shut down <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>, <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.