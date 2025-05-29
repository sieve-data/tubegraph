---
title: Examples of differential equation solutions
videoId: 6o7b9yyhH7k
---

From: [[khanacademy]] <br/> 

A [[definition_and_basic_understanding_of_differential_equations | differential equation]] is a concept used for modeling and simulating phenomena to understand how they operate <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. At its core, a [[definition_and_basic_understanding_of_differential_equations | differential equation]] is a relationship between a function and its derivatives <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## What is a Solution to a Differential Equation?

Unlike traditional algebraic equations where [[solutions_to_differential_equations | solutions]] are numbers or a set of values <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>, the [[solutions_to_differential_equations | solution to a differential equation]] is a function or a class of functions <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. It is not just a single value or a set of values <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### Example Differential Equation

Consider the following [[definition_and_basic_understanding_of_differential_equations | differential equation]], expressed in various notations:
*   The second derivative of y plus two times the first derivative of y is equal to three times y <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   If y is a function of x, this can be written in function notation as:
    $y''(x) + 2y'(x) = 3y(x)$ <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>
*   Using Leibniz notation, it is:
    $\frac{d^2y}{dx^2} + 2\frac{dy}{dx} = 3y$ <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

All three forms represent the same relationship: finding functions where the second derivative plus two times the first derivative equals three times the function itself <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Verifying a Solution: Example 1

One [[solutions_to_differential_equations | solution]] to this [[definition_and_basic_understanding_of_differential_equations | differential equation]] is $y_1(x) = e^{-3x}$ <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

To verify this:
1.  Find the first derivative of $y_1$:
    $y_1'(x) = -3e^{-3x}$ <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>
2.  Find the second derivative of $y_1$:
    $y_1''(x) = 9e^{-3x}$ <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>
3.  Substitute these into the [[definition_and_basic_understanding_of_differential_equations | differential equation]] $y'' + 2y' = 3y$:
    $9e^{-3x} + 2(-3e^{-3x}) = 3(e^{-3x})$ <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>
    $9e^{-3x} - 6e^{-3x} = 3e^{-3x}$ <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
    $3e^{-3x} = 3e^{-3x}$ <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>

Since the equation holds true, $y_1(x) = e^{-3x}$ is indeed a [[solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Verifying a Solution: Example 2

Another [[solutions_to_differential_equations | solution]] to this [[definition_and_basic_understanding_of_differential_equations | differential equation]] is $y_2(x) = e^x$ <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

To verify this:
1.  Find the first derivative of $y_2$:
    $y_2'(x) = e^x$ <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>
2.  Find the second derivative of $y_2$:
    $y_2''(x) = e^x$ <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>
3.  Substitute these into the [[definition_and_basic_understanding_of_differential_equations | differential equation]] $y'' + 2y' = 3y$:
    $e^x + 2(e^x) = 3(e^x)$ <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>
    $3e^x = 3e^x$ <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>

This also holds true, confirming that $y_2(x) = e^x$ is a [[solutions_to_differential_equations | solution]] as well <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## Key Takeaways

*   The [[solutions_to_differential_equations | solutions]] to a [[definition_and_basic_understanding_of_differential_equations | differential equation]] are functions, or a class of functions <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   A single [[definition_and_basic_understanding_of_differential_equations | differential equation]] can have more than one [[solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Often, there is a whole class of functions that can be a [[solutions_to_differential_equations | solution]] <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

Further videos will explore what these [[solutions_to_differential_equations | solutions]] look like, classes of [[solutions_to_differential_equations | solutions]], techniques for solving them, and visualizing [[solutions_to_differential_equations | solutions to differential equations]] <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.