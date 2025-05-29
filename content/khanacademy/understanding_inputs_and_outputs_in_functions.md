---
title: Understanding inputs and outputs in functions
videoId: kvGsIo1TmsM
---

From: [[khanacademy]] <br/> 

A function is an abstract concept that takes an input, processes it, and produces a single, specific output based on that input <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The function "munches" on the input and performs operations to yield the output <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Function Notation and Variables

Typically, `f(x)` is a common notation for a function, where `x` represents the input [[role_of_variables_in_expressions | variable]] and `f` is the name of the function <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Other variables can be used for both the function name and the input, such as `h(a)` <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. The input [[role_of_variables_in_expressions | variable]] serves as a placeholder to be replaced with the specific input value <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Example 1: Conditional Function

Consider a function defined as:
`f(x) = x^2` if `x` is even <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
`f(x) = x + 5` if `x` is odd <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>

To find the output for a given input:

*   **Input: 2**
    To evaluate `f(2)`, substitute `2` for `x`. Since `2` is even, use the first rule <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    `f(2) = 2^2 = 4` <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

*   **Input: 3**
    To evaluate `f(3)`, substitute `3` for `x`. Since `3` is odd, use the second rule <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
    `f(3) = 3 + 5 = 8` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Example 2: Abstract Function

Functions can be defined in very general ways, not just with mathematical expressions <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. For instance:
`h(a) =` the next largest number that starts with the same letter as [[role_of_variables_in_expressions | variable]] `a` (assuming English words for numbers) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>, <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>, <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

*   **Input: 2**
    `2` starts with `T`. The next largest number starting with `T` is `3` <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>, <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    `h(2) = 3` <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

*   **Input: 8**
    `8` starts with `E`. The next largest number starting with `E` is `11` (not `9` or `10`) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    `h(8) = 11` <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Relating to Traditional Equations

Many familiar equations are also functions <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. For example, `y = x + 1` can be written as `f(x) = x + 1` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

*   **Input: 0**
    `f(0) = 0 + 1 = 1` <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>, <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

*   **Input: 2**
    `f(2) = 2 + 1 = 3` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

This relationship can be represented in a table:
| x (Input) | y (Output) |
| :-------- | :--------- |
| 0         | 1          |
| 2         | 3          |
<a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>, <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>, <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

Function notation clarifies that the function takes an input (x), processes it (`x + 1`), and produces an output that is one more than the input <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## What is NOT a Function?

A key rule for [[definition_of_a_function | functions]] is that for any given input, there can only be **one possible output** <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>, <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### Example: A Circle

Consider the equation of a circle centered at the origin with radius 2: `x^2 + y^2 = 4` <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>, <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>, <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

Visually, if you pick an input value for `x`, there are often two corresponding `y` values <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

For example, if `x = 1`:
`1^2 + y^2 = 4` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>
`1 + y^2 = 4` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
`y^2 = 3` <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>
`y = ±√3` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>

For the single input `x = 1`, there are two outputs: `√3` and `-√3` <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>, <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. Because an input of `1` yields two different outputs, this relationship is **not a function** <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>, <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. This highlights the [[difference_between_functions_and_relations | distinction between functions and relations]].