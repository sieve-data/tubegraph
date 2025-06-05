---
title: commands and syntax in Brainfuck
videoId: hdHjjBS4cs8
---

From: [[fireship]] <br/> 

Brainfuck is described as a minimal esoteric programming language designed to challenge the mind <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is Turing complete, but its purpose is not to build practical software; rather, it functions more like a work of art that questions the status quo <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Background
[[brainfuck_language_history|Brainfuck]] was created in 1993 by Swiss physics student Urban Mueller <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. His primary goal was to develop a language with the smallest possible compiler <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It was originally built for the Amiga 2.0 operating system, and its compiler weighs in at under 200 bytes <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Program Structure and Memory Model
A Brainfuck program operates on a 30,000-byte one-dimensional array <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. All values within this array are initialized to zero <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The language provides a movable pointer that can be manipulated to interact with the array <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Notably, Brainfuck does not require concepts like variables, functions, or classes <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## The Eight Commands
Brainfuck features eight distinct commands used to manipulate the data pointer and the values in the memory cells <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>:

*   **`<` (Less than sign)**: Moves the pointer one cell to the left <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **`>` (Greater than sign)**: Moves the pointer one cell to the right <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **`+` (Plus sign)**: Increments the value in the current cell by one <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **`-` (Minus sign)**: Decrements the value in the current cell by one <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **`.` (Period)**: Outputs the byte at the pointer's current location <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **`,` (Comma)**: Accepts input and stores it at the pointer's current location <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **`[` (Opening bracket)**: Marks the beginning of a loop. The loop executes as long as the value in the current cell is not zero <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **`]` (Closing bracket)**: Marks the end of a loop. If the value in the current cell is non-zero, the program returns to the corresponding opening bracket <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Syntax Rules
Any characters within a Brainfuck program that are not one of the eight specified commands are ignored and treated as comments <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## Example of Use
To print "Hi Mom" in Brainfuck, one must manipulate the 30,000 8-bit numbers in the array, setting each to its corresponding ASCII character value <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This involves incrementing and decrementing cell values and moving the pointer extensively. For instance, to get the letter 'H' (ASCII 104), a cell's value must be incremented until it reaches 104, then outputted using the `.` command <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This process of manipulating memory is continued until all necessary characters are outputted <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Running Brainfuck Programs
[[how_to_write_and_run_a_brainfuck_program|Brainfuck programs]] typically end with the `.bf` extension <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. To run Brainfuck code, it can be copied and pasted into one of the many available online interpreters <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.