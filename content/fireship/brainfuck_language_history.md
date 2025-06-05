---
title: Brainfuck language history
videoId: hdHjjBS4cs8
---

From: [[fireship]] <br/> 

Brainfuck is described as a minimal, esoteric programming language designed to challenge conventional thinking about software development <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While it is [[https://en.wikipedia.org/wiki/Turing_completeness | Turing complete]], its purpose is not to build actual software, but rather to exist as "a work of art that challenges the status quo" <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Origins and Purpose

Brainfuck was created in 1993 by Swiss physics student Urban Mueller <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. His primary goal was to design a language with the smallest possible compiler <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It was initially built for the Amiga 2.0 operating system, and its compiler famously weighs in at under 200 bytes <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### Fundamental Design

A Brainfuck program operates on a one-dimensional array of 30,000 bytes, with all values initially set to zero <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. It provides a movable pointer that can be manipulated using eight distinct [[commands_and_syntax_in_brainfuck | commands and syntax in Brainfuck]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The language intentionally omits common programming constructs such as variables, functions, and classes <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Getting Started

To [[how_to_write_and_run_a_brainfuck_program | write and run a Brainfuck program]], one would traditionally need to install Amiga OS <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Programs are saved with a `.bf` file extension <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Any characters in the code that are not one of the eight core commands are ignored, functioning as comments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### Example: "Hi Mom"

Writing a simple phrase like "Hi Mom" in Brainfuck demonstrates its low-level memory manipulation approach. It requires setting individual array cells to their corresponding ASCII characters by incrementing or decrementing values and moving the pointer <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. For instance, to output the letter 'H' (ASCII 104), the pointer is moved to a cell, its value adjusted, and then outputted <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This process of "manipulating memory like cavemen" continues for each desired character <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

Today, Brainfuck code can be run using various online interpreters <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.