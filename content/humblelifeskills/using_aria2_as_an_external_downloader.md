---
title: Using Aria2 as an external downloader
videoId: VlQ4hGzydCc
---

From: [[humblelifeskills]] <br/> 

Aria2 is an external downloader that can be used in conjunction with other tools like [[setting_up_and_using_ytdlp_for_downloading_videos | ytdlp]] to manage and accelerate content downloads <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. It is particularly useful for batch processing and optimizing download speeds <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

## How it's Used

When downloading multiple content pieces, such as a collection of TikTok videos, you can use [[using_axiomai_for_automation | Axiom.ai]] to create a spreadsheet of direct URLs <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>, <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. These URLs are then copied into a text file, for example, named `grab.txt` <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.

Next, [[setting_up_and_using_ytdlp_for_downloading_videos | ytdlp]] is used to point to this `grab.txt` file <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>, <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>. Aria2 is then employed as the external downloader to process the list batch by batch <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

## Advantages of Aria2

*   **Batch Processing**: Aria2 can efficiently go through a list of URLs and download content in batches <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>, <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.
*   **Chunking Downloads**: It supports chunking, which means it can split downloads into smaller parts. This is beneficial even for smaller files that don't necessarily need to be chunked <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>, <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
*   **Faster Downloads**: Aria2 can download content faster by optimizing based on your internet connection <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.