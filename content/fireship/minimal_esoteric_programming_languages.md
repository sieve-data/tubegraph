---
title: minimal esoteric programming languages
videoId: hdHjjBS4cs8
---

From: [[fireship]] <br/> 

Brainf\*\*k is described as a [[lowlevel_systems_programming_languages | minimal esoteric programming language]] designed to challenge the user and is not intended for building actual software <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While it is [[lowlevel_systems_programming_languages | Turing complete]], its purpose is more akin to a work of art that critiques the status quo <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## History and Design Goals

Brainf\*\*k was created in 1993 by Swiss physics student Urban Mueller <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. His primary objective was to develop a language with the smallest possible compiler <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It was initially built for the Amiga 2.0 operating system, and its compiler is notably compact, weighing in at under 200 bytes <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Core Concepts

A Brainf\*\*k program operates on a 30,000-byte one-dimensional array, with all values initially set to zero <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The language provides a movable pointer to manipulate this array <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Brainf\*\*k is characterized by its extreme minimalism, as it does not require common programming constructs like variables, functions, or classes <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Commands

Brainf\*\*k utilizes only eight distinct commands to manipulate data:

*   **`<` and `>`**: Used to move the pointer left or right by one cell at a time <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **`+` and `-`**: Increment or decrement the value in the current cell pointed to <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **`.`**: Outputs the byte at the pointer's current location <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **`,`**: Accepts input and stores it at the pointer's current location <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **`[` and `]`**: Used to create loops <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. A loop continues until the original cell that initiated it returns to zero <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Program Execution

To run a Brainf\*\*k program, one would typically create a file ending in `.bf` (which stands for Brainf\*\*k) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Any characters in the file that are not one of the eight specified commands are ignored as comments <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. While traditionally designed for AmigaOS, programs can often be executed using various online interpreters <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

Programming in Brainf\*\*k involves manipulating memory like a "caveman" to achieve desired outputs, such as converting numbers to their corresponding ASCII characters <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. For example, to set an ASCII character, a cell's value is incremented, then a loop might decrement the current cell while incrementing another, and then the pointer moves back to the original cell, continuing until the original cell hits zero <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Once the desired ASCII value is at a cell, the pointer can be moved to it, incremented if needed, and then outputted using the `.` command <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.