---
title: Difference between functions and relations
videoId: kvGsIo1TmsM
---

From: [[khanacademy]] <br/> 

## What is a Function?

A [[definition_of_a_function | function]] is an abstract concept that takes an input, processes it, and produces a single, given output based on that input <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It "munches" on the input and does something to it <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

> [!definition] Key Characteristic of a Function
> For every input, there is **only one possible output** <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Function Notation

Functions are commonly denoted using notation like `f(x)` <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   `x` is typically the [[role_of_variables_in_expressions | variable]] used for the input into the [[definition_of_a_function | function]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   `f` is often the letter used for the name of the [[definition_of_a_function | function]], though other letters can be used <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

When evaluating `f(x)`, the [[role_of_variables_in_expressions | variable]] `x` acts as a placeholder for the input value <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. To evaluate `f(2)`, you replace every instance of `x` with `2` <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Examples of Functions

### Conditional Function Example
Consider the [[definition_of_a_function | function]] `f(x)` defined as:
*   `f(x) = x²` if `x` is even <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
*   `f(x) = x + 5` if `x` is odd <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>

Let's evaluate some inputs:
*   **f(2)**: Since 2 is even, `f(2) = 2² = 4` <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **f(3)**: Since 3 is odd, `f(3) = 3 + 5 = 8` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Abstract Function Example
Functions can be defined in very general ways, not just with numbers <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. For example, a [[definition_of_a_function | function]] `h(a)` could be defined as "the next largest number that starts with the same letter as [[role_of_variables_in_expressions | variable]] `a` (assuming English)" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Let's evaluate `h(a)`:
*   **h(2)**: `2` starts with 'T'. The next largest number starting with 'T' is `3` <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. So, `h(2) = 3` <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **h(8)**: `8` starts with 'E'. The next largest number starting with 'E' is `11` <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. So, `h(8) = 11` <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Traditional Algebraic Example
Many familiar algebraic [[difference_between_expressions_and_equations | equations]] can be viewed as [[definition_of_a_function | functions]] <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
For instance, `y = x + 1` can be written as `f(x) = x + 1` <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   If `x = 0`, then `f(0) = 0 + 1 = 1` <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   If `x = 2`, then `f(2) = 2 + 1 = 3` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

This relationship can also be represented in a table:
| x | y |
|---|---|
| 0 | 1 |
| 2 | 3 |
<a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>

Using [[definition_of_a_function | function]] notation makes it clear that the [[definition_of_a_function | function]] takes an input (`x`), processes it (`x + 1`), and produces an output (`y`) <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## What is Not a Function (A Relation)

A [[definition_of_a_function | function]] must produce only one possible output for any given input <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. If an input can lead to multiple outputs, the relationship is not a [[definition_of_a_function | function]]; it's merely a [[visual_representation_of_functions_and_circles | relation]] <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### Example: A Circle (Not a Function)

Consider the [[visual_representation_of_functions_and_circles | visual representation of functions and circles]] for the equation of a circle centered at the origin with radius 2: `x² + y² = 4` <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

Visually, if you pick an `x`-value (e.g., `x = 1`), there are two corresponding `y`-values on the circle: one positive and one negative <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

Let's solve for `y` when `x = 1`:
1.  `1² + y² = 4` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>
2.  `1 + y² = 4` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
3.  `y² = 3` <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>
4.  `y = √3` or `y = -√3` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>

For the input `x = 1`, there are two outputs: `√3` and `-√3` <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. Because a single input yields multiple outputs, this relationship (the circle) is **not a [[definition_of_a_function | function]]** <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. A [[definition_of_a_function | function]] can only have one output for a given input <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.