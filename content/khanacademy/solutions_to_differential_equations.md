---
title: Solutions to differential equations
videoId: 6o7b9yyhH7k
---

From: [[khanacademy]] <br/> 

A [[definition_and_basic_understanding_of_differential_equations | differential equation]] describes a relationship between a function and its derivatives <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Unlike algebraic equations, which yield numbers as solutions <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>, the solution to a [[introduction_to_differential_equations | differential equation]] is a function, or a class of functions <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. These equations are "super useful for modeling and simulating phenomena and understanding how they operate" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Defining a Differential Equation

An example of a [[introduction_to_differential_equations | differential equation]] is:
`y'' + 2y' = 3y` <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>

This can be written in various notations <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>:
*   **Function Notation**: `y''(x) + 2y'(x) = 3y(x)` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>
*   **Leibniz Notation**: `d^2y/dx^2 + 2dy/dx = 3y` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

All these forms ask: "Can I find functions where the second derivative of the function plus two times the first derivative of the function is equal to three times the function itself?" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

### Contrast with Algebraic Equations

A traditional algebraic equation, like `x^2 + 3x + 2 = 0` <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, has solutions that are numbers or a set of numbers (e.g., `x = -2` or `x = -1`) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. In contrast, solutions to [[introduction_to_differential_equations | differential equations]] are functions <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## [[examples_of_differential_equation_solutions | Examples of Differential Equation Solutions]]

There is often more than one solution to a [[introduction_to_differential_equations | differential equation]]; a "whole class of functions" can be a solution <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

Consider the differential equation: `y'' + 2y' = 3y`

### Solution 1: `y1(x) = e^(-3x)`

To verify this as a solution, we find its derivatives and substitute them into the equation:
*   First derivative: `y1'(x) = -3e^(-3x)` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>
*   Second derivative: `y1''(x) = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>

Substituting into the equation:
`9e^(-3x) + 2(-3e^(-3x)) = 3e^(-3x)` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>
`9e^(-3x) - 6e^(-3x) = 3e^(-3x)` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
`3e^(-3x) = 3e^(-3x)` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>

Since the equation holds true, `y1(x) = e^(-3x)` is indeed a solution <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Solution 2: `y2(x) = e^x`

To verify `y2(x) = e^x` as another solution:
*   First derivative: `y2'(x) = e^x` <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>
*   Second derivative: `y2''(x) = e^x` <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>

Substituting into the equation:
`e^x + 2(e^x) = 3e^x` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
`3e^x = 3e^x` <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>

This also holds true, confirming that `y2(x) = e^x` is another solution to the same [[introduction_to_differential_equations | differential equation]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

Further topics in [[introduction_to_differential_equations | differential equations]] involve exploring techniques for solving them, visualizing solutions, and understanding different classes of solutions <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.