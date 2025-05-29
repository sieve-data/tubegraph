---
title: Concept of approaching values in calculus
videoId: riXcZT2ICjA
---

From: [[khanacademy]] <br/> 

The [[introduction_to_limits | idea of a limit]] is a fundamental concept in [[concept_of_derivatives_and_differential_calculus | calculus]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Despite its importance, it represents a very simple idea: determining what a function is "approaching" as its input approaches a certain value <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Understanding Limits Through Examples

### Example 1: Function with a Hole

Consider the function f(x) defined as:
f(x) = (x - 1) / (x - 1) <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

While this expression appears to simplify to 1, it's crucial to note that the function is undefined when x = 1 <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. If x = 1, the numerator becomes 1 - 1 = 0 and the denominator becomes 1 - 1 = 0, resulting in 0/0, which is undefined <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Therefore, f(x) can be expressed as:
f(x) = 1, with the constraint that x ≠ 1 <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

When graphed, this function is a horizontal line at y = 1, but with a "gap" or a hole at x = 1 <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

<div class="callout">
    **What is f(1)?**
    f(1) is undefined <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
</div>

<div class="callout">
    **What is the function approaching as x approaches 1?**
    As x gets infinitesimally closer to 1 (from either side, but not actually at 1), the function's value is consistently 1 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
    This is formally written as:
    Limit (lim) as x approaches 1 of f(x) = 1 <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
    This notation simply asks: "What is the function approaching as x gets closer and closer to 1?" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
</div>

### Example 2: Piecewise Function with Discontinuity

Consider a function g(x) defined as:
g(x) = x² when x ≠ 2 <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>
g(x) = 1 when x = 2 <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>

This function represents a parabola (y = x²) everywhere except at x = 2, where its value "drops" to 1 <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. There is a discontinuity at x = 2 <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

<div class="callout">
    **What is g(2)?**
    Based on the definition, g(2) = 1 <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
</div>

<div class="callout">
    **What is the limit as x approaches 2 of g(x)?**
    This asks what g(x) is approaching as x gets closer and closer to 2, regardless of the function's actual value at x=2 <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
    Visually from the graph, as x gets closer to 2 (from either the left or the right), the function's value on the parabola approaches 4 <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

    To illustrate numerically:
    *   If x = 1.9, g(x) = 1.9² = 3.61 <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>
    *   If x = 1.99, g(x) = 1.99² = 3.96 <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
    *   If x = 1.999, g(x) = 1.999² = 3.996 <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>
    *   If x = 2.1, g(x) = 2.1² = 4.41 <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>
    *   If x = 2.01, g(x) = 2.01² = 4.0401 <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>

    As x gets closer to 2, from both sides, the value of g(x) gets closer and closer to 4 <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>, <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
    Therefore, the limit as x approaches 2 of g(x) = 4 <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

    This example highlights that the limit of a function as x approaches a certain value does not necessarily equal the function's value at that exact point <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
</div>