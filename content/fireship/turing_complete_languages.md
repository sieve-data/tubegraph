---
title: Turing complete languages
videoId: hdHjjBS4cs8
---

From: [[fireship]] <br/> 

A Turing complete language is one that can simulate any [[Turing machine]]. This means it can perform any computation that a universal computer can. Brainfuck, a [[minimal_esoteric_programming_languages|minimal esoteric programming language]], is an example of a Turing complete language <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Brainfuck Overview

Brainfuck was designed to be a language that "makes your brain hurt" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It is not intended for building actual software but rather serves as a "work of art that challenges the status quo" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

### Origin and Goal
Brainfuck was created in 1993 by Swiss physics student Urban Mueller <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Its primary goal was to create a language with the smallest possible compiler <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. The original compiler for the Amiga 2.0 operating system weighed in at under 200 bytes <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### Data Structure
A Brainfuck program operates on a 30,000-byte one-dimensional array, with all values initially set to zero <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. It uses a movable pointer to manipulate values within this array <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

### Commands
Brainfuck uses only eight distinct commands to manipulate data and control flow <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It intentionally lacks features like variables, functions, and classes <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Any characters not part of these eight commands are ignored as comments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

The commands are:
*   **`<`**: Move the pointer left by one cell <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **`>`**: Move the pointer right by one cell <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   **`+`**: Increment the value in the current cell <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **`-`**: Decrement the value in the current cell <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **`.`**: Output the byte at the pointer's current location <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **`,`**: Accept input and store it at the pointer's current location <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   **`[`**: Begin a loop <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The loop continues until the original cell goes back to zero, at which point it exits <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **`]`**: End a loop <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Example: "Hi Mom"
To say "Hi Mom" in Brainfuck, one must set each number in the array to its corresponding ASCII character value <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This involves a process of manipulating memory like "cavemen" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. For instance, to output 'H' (ASCII 104), a cell's value must be precisely set and then outputted using the `.` command <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

To run Brainfuck code, one can create a file ending in `.bf` and use one of the many available online interpreters <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.