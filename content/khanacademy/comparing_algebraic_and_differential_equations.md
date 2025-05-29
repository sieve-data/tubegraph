---
title: Comparing algebraic and differential equations
videoId: 6o7b9yyhH7k
---

From: [[khanacademy]] <br/> 

This article contrasts [[types_of_differential_equations_ordinary_vs_partial | differential equations]] with traditional algebraic equations, focusing on the fundamental differences in their structure and, most importantly, the nature of their solutions.

## What is a Differential Equation?
A [[introduction_to_differential_equations | differential equation]] is an equation that expresses a relationship between a function and its derivatives <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. They are commonly used for modeling and simulating phenomena and understanding how they operate <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

### Examples of Differential Equations
Differential equations can be written in several notations:
*   **Standard notation**: For example, `y'' + 2y' = 3y` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Function notation**: If `y` is a function of `x`, this can be written as `y''(x) + 2y'(x) = 3y(x)` <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Leibniz notation**: This can also be expressed as `d²y/dx² + 2(dy/dx) = 3y` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

All these forms represent the same underlying relationship: finding functions where the second derivative of the function plus two times its first derivative equals three times the function itself <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Solutions to Differential Equations
Unlike algebraic equations, the [[functionbased_solutions_to_differential_equations | solution to a differential equation]] is a function or a class of functions, not just a numerical value or a set of values <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. There can often be more than one solution; sometimes, there's a whole class of functions that satisfy the equation <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

For the example differential equation `y'' + 2y' = 3y`, two functions that are solutions include:
*   `y1(x) = e^(-3x)` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>
    *   `y1'(x) = -3e^(-3x)` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>
    *   `y1''(x) = 9e^(-3x)` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>
    *   Substituting these into the equation yields `9e^(-3x) + 2(-3e^(-3x)) = 3e^(-3x)`, which simplifies to `9e^(-3x) - 6e^(-3x) = 3e^(-3x)`, or `3e^(-3x) = 3e^(-3x)` <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>, confirming `y1(x)` is a solution <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   `y2(x) = e^x` <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>
    *   `y2'(x) = e^x` <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>
    *   `y2''(x) = e^x` <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>
    *   Substituting these into the equation gives `e^x + 2(e^x) = 3e^x`, which simplifies to `3e^x = 3e^x` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>, confirming `y2(x)` is also a solution <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## What is an Algebraic Equation?
An algebraic equation (sometimes referred to as a "traditional equation") is a mathematical statement that equates two expressions, typically involving variables but not their derivatives <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Example of an Algebraic Equation
A common example is a quadratic equation: `x² + 3x + 2 = 0` <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Solutions to Algebraic Equations
The [[understanding_differential_equations_and_their_solutions | solutions]] to an algebraic equation are numbers or a set of numbers that satisfy the equation <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. For the example `x² + 3x + 2 = 0`, factoring it to `(x + 2)(x + 1) = 0` reveals the solutions are `x = -2` or `x = -1` <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. These solutions are specific numerical values.

## Key Distinction: Solution Type
The fundamental difference between [[introduction_to_differential_equations | differential equations]] and algebraic equations lies in the nature of their solutions:
*   **Differential Equations**: The solutions are functions or classes of functions <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Algebraic Equations**: The solutions are numbers or a set of numbers <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

In essence, a differential equation defines a relationship between a function and its derivatives, requiring a function as its answer <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. An algebraic equation defines a relationship between variables, requiring specific values as its answer <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.