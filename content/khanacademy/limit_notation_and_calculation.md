---
title: Limit notation and calculation
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

Limits are a fundamental concept in mathematics, particularly in calculus, that describe the behavior of a [[mathematical_expressions | function]] as its input approaches a certain value. They provide a way to understand the value an [[mathematical_expressions | expression]] approaches, even if the [[mathematical_expressions | function]] itself is undefined or behaves unusually at that specific point <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Understanding Limit Notation

The notation for a limit is written as:
`lim (as x approaches c) of f(x)` <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
For example, "the limit as x approaches 2 of x squared" is written as `lim (x->2) x^2` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This asks: "What value does the [[mathematical_expressions | expression]] `x squared` approach as `x` approaches 2?" <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Calculating Limits: Examples

### Case 1: Continuous Function

Consider the [[mathematical_expressions | expression]] `x^2` <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
Graphically, `x^2` forms a parabola <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
When `x` is exactly 2, the [[mathematical_expressions | expression]] `x^2` equals 4 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

To find the limit as `x` approaches 2:
As `x` gets closer and closer to 2 from both the left (numbers less than 2) and the right (numbers greater than 2), the value of the [[mathematical_expressions | expression]] `x^2` approaches 4 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. In this simple case, the limit is 4 <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This is because if `f(x) = x^2`, then [[function_notation | f(2)]] = 4 <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### Case 2: Discontinuous Function

Limits become particularly useful when dealing with [[mathematical_expressions | functions]] that have "wrinkles" or discontinuities <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
Consider a new [[function_notation | function]], [[function_notation | f(x)]], defined as:
*   [[function_notation | f(x)]] = `x^2` when `x` is not equal to 2 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   [[function_notation | f(x)]] = `3` when `x` is equal to 2 <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

Graphically, this [[function_notation | function]] looks almost identical to `x^2`, but with a "hole" at `x = 2` where `f(x)` would normally be 4 <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Instead of 4, the [[function_notation | function]]'s value "jumps down" to 3 at `x = 2` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

To find the limit as `x` approaches 2 for this [[function_notation | function]]:
As `x` approaches 2 from the left side, the [[function_notation | f(x)]] values approach 4 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. Similarly, as `x` approaches 2 from the right side, the [[function_notation | f(x)]] values also approach 4 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

Therefore, even with the discontinuity, the limit as `x` approaches 2 for this [[function_notation | f(x)]] is 4 <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
In this case, the limit as `x` approaches 2 of [[function_notation | f(x)]] (which is 4) does *not* equal [[function_notation | f(2)]] (which is 3) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

## Why Limits Are Important

The concept of a limit is crucial because it allows us to analyze the behavior of [[mathematical_expressions | functions]] near a point, even if the [[mathematical_expressions | function]] itself is undefined or discontinuous at that exact point <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. This distinguishes limits from simply evaluating the [[function_notation | function]] at a given point <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

Limits form the foundation for more advanced calculus concepts such as derivatives and integrals <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. While this introduction provides an intuition, a more formal "delta-epsilon" definition of a limit also exists <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.