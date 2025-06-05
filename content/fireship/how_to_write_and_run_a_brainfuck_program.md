---
title: how to write and run a Brainfuck program
videoId: hdHjjBS4cs8
---

From: [[fireship]] <br/> 
Brainfuck is a minimal esoteric programming language that is Turing complete, though it is not designed for building actual software. Instead, it is considered more of a work of art that challenges conventional programming paradigms <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It was created in 1993 by Swiss physics student Urban Mueller, whose goal was to create a language with the smallest possible compiler <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The compiler for Brainfuck, built for the Amiga 2.0 operating system, weighs in at under 200 bytes <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Program Structure

A Brainfuck program operates on a 30,000-byte one-dimensional array, with all values initialized to zero <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. It provides a movable pointer that can be manipulated to interact with this array <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Brainfuck does not require constructs like variables, functions, or classes <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## [[commands_and_syntax_in_brainfuck|Commands and Syntax]]

Brainfuck utilizes eight distinct commands to manipulate the data pointer and the values in the array cells:

*   **`<`** and **`>`**: Used to move the pointer left or right by one cell at a time <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **`+`** and **`-`**: Used to increment or decrement the value in the current cell <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **`.`**: Outputs the byte at the pointer's current location <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **`,`**: Accepts input and stores it at the pointer's current location <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **`[`** and **`]`**: Used to create a loop <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The loop continues until the value in the cell at the opening bracket becomes zero, at which point it exits <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

Any characters within a Brainfuck file that are not one of these eight commands are ignored as comments <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## Writing a Brainfuck Program

To write a Brainfuck program, you create a file ending with the `.bf` extension <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The core task of writing a program involves manipulating the 30,000 8-bit numbers in the array, which are all initially set to zero <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>.

### Example: "Hi mom"

To output a string like "Hi mom," you need to set each number in the array to its corresponding ASCII character value <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>. This often involves:

1.  **Incrementing Cells**: Use `+` to increase a cell's value <a class="yt-timestamp" data-t="01:01:14">[01:01:14]</a>.
2.  **Looping for Efficiency**: For larger values, you can use loops `[]` to multiply or set values efficiently. For example, to set a value, you might increment one cell, enter a loop, decrement the current cell, move the pointer, increment another cell, then move back and close the loop. This process continues until the original cell reaches zero <a class="yt-timestamp" data-t="01:01:16">[01:01:32]</a>.
3.  **Moving the Pointer**: Use `<` and `>` to navigate between cells as you manipulate their values <a class="yt-timestamp" data-t="01:01:23">[01:01:23]</a>.
4.  **Outputting Characters**: Once a cell holds the desired ASCII value, move the pointer to it and use `.` to output the character <a class="yt-timestamp" data-t="01:01:39">[01:01:39]</a>. This process of manipulating memory is repeated for every character needed <a class="yt-timestamp" data-t="01:01:47">[01:01:47]</a>.

## Running a Brainfuck Program

To run your Brainfuck code, you can use one of the many online interpreters available <a class="yt-timestamp" data-t="01:01:52">[01:01:52]</a>. Simply copy and paste your code into the interpreter to execute it <a class="yt-timestamp" data-t="01:01:52">[01:01:52]</a>.