---
title: Function notation and usage
videoId: kvGsIo1TmsM
---

From: [[khanacademy]] <br/> 

A function is a concept that takes an input, processes it, and produces a given output based on what that input is <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Understanding Function Notation

Typically, `f(x)` is used to denote a function, where `x` represents the input [[understanding_algebraic_expressions|variable]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. While `f` is a commonly used name for a function, other letters can also be used <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. To evaluate a function for a specific input, you replace the [[understanding_algebraic_expressions|variable]] (or placeholder) in the function's definition with the desired input value <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### Examples of Functions

Functions can be defined in various ways, ranging from mathematical [[understanding_algebraic_expressions|equations]] to more abstract rules.

#### Conditional Mathematical Function
A function can have different rules based on the input's properties <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

For example:
`f(x) = x^2` if `x` is even <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>
`f(x) = x + 5` if `x` is odd <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>

*   **Evaluating `f(2)`**: Since 2 is even, we apply the `x^2` rule. `f(2)` is `2^2`, which equals 4 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Evaluating `f(3)`**: Since 3 is odd, we apply the `x + 5` rule. `f(3)` is `3 + 5`, which equals 8 <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

#### Abstract Rule-Based Function
Functions can also operate on non-numerical inputs or use abstract rules <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

For example:
`h(a)` = the next largest number that starts with the same letter as [[understanding_algebraic_expressions|variable]] `a` (assuming English language) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

*   **Evaluating `h(2)`**: '2' starts with 'T'. The next largest number starting with 'T' is '3' <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. So, `h(2) = 3` <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Evaluating `h(8)`**: '8' starts with 'E'. The next largest number starting with 'E' is '11' <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. So, `h(8) = 11` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This demonstrates the general and flexible nature of functions <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

#### Common Algebraic Equations as Functions
Many familiar [[understanding_algebraic_expressions|equations]] can be viewed as functions <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

For example, `y = x + 1` can be written as `f(x) = x + 1` <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Evaluating `f(0)`**: `f(0) = 0 + 1 = 1` <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **Evaluating `f(2)`**: `f(2) = 2 + 1 = 3` <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

This concept is often visualized using tables of inputs and outputs:
| x | y |
|---|---|
| 0 | 1 |
| 2 | 3 |
<a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>

Function notation clarifies that for any input `x`, the function 'munches on it' and produces an output that is `1` more than the input <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

## What Is Not a Function?

A relationship is **not** a function if a single input can produce more than one possible output <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. Each input must yield exactly one output <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

### Example: A Circle's Equation

Consider the [[understanding_algebraic_expressions|equation]] of a circle centered at the origin with radius 2: `x^2 + y^2 = 2^2`, or `x^2 + y^2 = 4` <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

Graphically, this is a circle on a coordinate plane <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>:
```
        ^ y
        |
    -2--+--2-> x
        |
        v
```
<a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>

If we try to input `x = 1` into this [[understanding_algebraic_expressions|equation]]:
1.  Substitute `x = 1`: `1^2 + y^2 = 4` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>
2.  Simplify: `1 + y^2 = 4` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
3.  Solve for `y^2`: `y^2 = 3` <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>
4.  Solve for `y`: `y = sqrt(3)` or `y = -sqrt(3)` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

Visually, for `x = 1`, there are two corresponding `y` values: positive [[square_root_symbol_and_terminology|square root]] of 3 and negative [[square_root_symbol_and_terminology|square root]] of 3 <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. Because a single input (`x=1`) yields two different outputs (`sqrt(3)` and `-sqrt(3)`), this relationship is not a function <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.