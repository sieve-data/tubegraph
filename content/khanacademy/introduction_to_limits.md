---
title: Introduction to limits
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

A [[definition_and_explanation_of_limits | limit]] describes what value an expression approaches as a variable gets closer to a certain number <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Basic Understanding: x-squared Example

Consider the [[definition_and_explanation_of_limits | limit]] as `x` approaches 2 of `x` squared <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This asks what value the expression `x` squared approaches as `x` gets closer to 2 <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

Using a [[graphical_representation_of_limits | graphical representation]] of `x` squared, as `x` approaches 2 from both the left (numbers less than 2) and the right (numbers greater than 2), the expression `x` squared approaches 4 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Therefore, the [[definition_and_explanation_of_limits | limit]] is 4 <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

At first glance, this might seem similar to simply evaluating the function at that point, as `f(2)` for `f(x) = x^2` also equals 4 <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>, <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## Distinction from Function Evaluation

The utility of [[definition_and_explanation_of_limits | limits]] becomes clear when considering functions that are not continuous or have "holes" <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>, <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

Consider a piecewise function `f(x)` defined as:
*   `f(x) = x^2` when `x` does not equal 2 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   `f(x) = 3` when `x` equals 2 <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

### Graphical Analysis of the Piecewise Function

This function's [[graphical_representation_of_limits | graph]] resembles `x` squared everywhere except at `x = 2` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. At `x = 2`, there is a "hole" at `(2, 4)` because `x` squared is not defined at `x = 2` for this function's first condition <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Instead, `f(2)` is defined as 3 <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

When determining the [[definition_and_explanation_of_limits | limit]] as `x` approaches 2 for this `f(x)`:
*   As `x` approaches 2 from the left, `f(x)` approaches 4 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>, <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   As `x` approaches 2 from the right, `f(x)` also approaches 4 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>, <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

Therefore, the [[definition_and_explanation_of_limits | limit]] of `f(x)` as `x` approaches 2 is 4 <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>, <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Key Takeaway: Differences between Limits and Function Evaluation

In this case, the [[definition_and_explanation_of_limits | limit]] (`4`) is different from the actual value of the function at that point (`f(2) = 3`) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This illustrates the [[differences_between_limits_and_function_evaluation | difference between a limit and evaluating a function]] at a point <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. [[definition_and_explanation_of_limits | Limits]] are crucial when functions might be undefined or jump at a certain point <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>, <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

More formal definitions, such as the delta-epsilon definition of a [[definition_and_explanation_of_limits | limit]], exist <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. Understanding [[definition_and_explanation_of_limits | limits]] is foundational for concepts like [[introduction_to_derivatives | derivatives]] and integrals <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.