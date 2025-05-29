---
title: Inspecting video elements using developer tools
videoId: g26WthoEXLs
---

From: [[dr_tutoriales]] <br/> 

This guide outlines a method to download videos from Facebook to a computer by inspecting the video element using browser developer tools <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Accessing the Video

1.  Navigate to the desired video on Facebook <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
2.  Modify the URL in the address bar:
    *   Remove the "www" part <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
    *   Remove the "http" part <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
    *   Replace these with an "m" to access the mobile version of the page on your computer <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Using Developer Tools to Find the Video Source

1.  Once on the mobile version of the video page, right-click on the video itself <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
2.  Select "Inspect" from the context menu <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This action will open a window on the right side of your screen, displaying the page's underlying code <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
3.  Play the video for two or three seconds <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a> <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
4.  Within the developer tools window, click the "inspect video" button (often represented by an arrow icon) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a> <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
5.  Hover your mouse over the video element in the code; it should highlight the video on the page <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a> <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
6.  Locate the `src` attribute within the highlighted video element, which contains the origin URL of the video <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a> <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
7.  Double-click on this `src` attribute's value to select the URL <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a> <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
8.  Copy the URL, ensuring you capture the full link starting from "HTTP" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## Downloading the Video

1.  Open a new browser tab <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
2.  Paste the copied URL into the address bar and press Enter <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This will open the video in its original, root Facebook version <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
3.  Click the three dots located on the video player <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
4.  Select "Download" from the options to save the video to your computer <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.