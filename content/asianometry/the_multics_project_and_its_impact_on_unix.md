---
title: The Multics project and its impact on Unix
videoId: HADp3emVABg
---

From: [[asianometry]] <br/> 

The [[the_creation_and_development_of_unix | creation and emergence of the operating system Unix]] was a special moment in technology history <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Its origins are deeply intertwined with the "Multiplexed Information and Computing Service," or Multics, project <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Beginnings of Multics

In 1965, scientists from Bell Labs collaborated with peers from MIT and General Electric on the Multics project <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The core idea behind Multics was to develop a general-purpose utility for sharing time on a computer system <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. At the time, computers were exceptionally expensive <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Time-sharing operating systems were created to enable multiple users to efficiently share limited computer resources <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Over time, these systems evolved into communication tools, connecting users with features like public profiles <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

General Electric, which had a business selling time shares for its computer systems, provided the Multics team with a GE 645 mainframe computer, simulated by a GE 635 <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

Multics experimented with several innovative concepts <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>:
*   **Arbitrary file names and directory structures** <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   **A virtual memory system** <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Virtual memory allows secondary storage, like a hard drive, to function as if it were part of the main memory (RAM) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This enables a computer to handle more data than its physical RAM would otherwise allow <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This was a significant improvement over existing file systems and is still used today <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

The Multics team aimed to integrate these ideas, which had previously been theoretical, into a single commercial product <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## The End of Multics

Retrospectively, the project was seen as "trying to boil the ocean" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Progress was slow, with excessive spending on too few people following a vague plan <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Frustrated by the lack of a workable product, Bell Labs formally withdrew from the Multics project in 1969 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Soon after, General Electric decided to exit the computer industry entirely, selling its division to Honeywell <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Multics' Legacy and the Birth of Unix

Despite the official end of Multics, a few scientists at the Bell Labs Computing Science Research Center—Ken Thompson, Dennis Ritchie, Rudd Canaday, Doug McIlroy, and J.F. Ossanna—continued working on concepts derived from the project <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. The termination of Multics meant losing access to the GE 635 computer they had been using <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

Ken Thompson had developed a space game called "Space Travel" for the GE 635, which simulated planetary movement <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. The game was enjoyable but expensive to play, costing $50-75 per session due to the computer timeshare fees <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. In 1969, Thompson found an unused graphics-capable PDP-7 minicomputer and decided to rewrite "Space Travel" for it <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This ambitious undertaking required him to re-implement fundamental components like a debugging subsystem and a floating-point arithmetic package from scratch <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The development process was tedious, involving carrying paper tapes from the GE computer OS to the PDP-7 <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### A New File System

After completing the game, Thompson focused on implementing ideas for a new file system he had discussed with Dennis Ritchie and Rudd Canaday <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. These ideas, originally sketched for the GE 635, aimed to organize files efficiently <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Being familiar with the PDP-7, Thompson quickly implemented this new file system in a day or two <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

Thompson and his colleagues then added a series of simple utilities, including functions for copying, printing, deleting, and editing files <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. They also created a basic command interpreter, known as a "shell," to run other programs <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

The concept of the "file" itself solidified, becoming an interface for data operations like reading or writing, independent of the file's content <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This abstraction of hardware differences was a "killer app" for [[unixs_internal_development_and_initial_use_at_bell_labs | Unix]], allowing users on any device to modify a file <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

By the end of the summer of 1969, Thompson had rewritten the entire system, making it distinct from the original GECOS operating system <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Initially, it wasn't even considered an operating system, but rather a "convenient platform for developing software" <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. Around 1970, team member Brian Kernighan suggested naming it "Unics," a "treacherous pun" on Multics. The spelling eventually changed to "Unix" <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.