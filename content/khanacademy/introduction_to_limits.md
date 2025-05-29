---
title: Introduction to limits
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

A limit describes the value an expression or function "approaches" as the input variable gets closer and closer to a specific value <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. The notation for a limit is written as "the limit as x approaches 2 of x squared" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Understanding the Concept

To determine a limit, one considers what value the expression approaches as the input variable approaches a certain point from both directions (from values less than the point and from values greater than the point) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This can be visualized by moving along the curve of the function closer and closer to the expression's value at that point <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Simple Example: `f(x) = x^2`

Consider the function `f(x) = x^2`.
If we want to find the limit as `x` approaches 2 of `x^2`:
`lim (x->2) x^2`

By [[graph_interpretation_in_the_context_of_limits | graphing]] `x^2` and observing the values of `f(x)` as `x` gets closer to 2 from both sides, it becomes clear that the expression approaches 4 <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. In this simple case, just substituting 2 into the function (`f(2) = 2^2 = 4`) yields the same result as the limit <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Complex Example: Piecewise Function

The concept of a limit becomes more significant when dealing with functions that behave differently at specific points. Consider a piecewise function `f(x)` defined as:
*   `f(x) = x^2` when `x` does not equal 2 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   `f(x) = 3` when `x` equals 2 <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

When [[graph_interpretation_in_the_context_of_limits | graphing]] this function, it appears identical to `x^2` everywhere except at `x = 2`. At `x = 2`, there is a "hole" in the graph at `y = 4`, and instead, the function's value "jumps" to `y = 3` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

Now, let's find the limit as `x` approaches 2 of this new `f(x)`:
`lim (x->2) f(x)`

Even though `f(2)` is defined as 3, the limit is still 4. As `x` approaches 2 from the left-hand side (values less than 2), `f(x)` approaches 4 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>, <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. Similarly, as `x` approaches 2 from the right-hand side (values greater than 2), `f(x)` also approaches 4 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>, <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. Therefore, the limit as `x` approaches 2 for this function is 4 <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

In this case, the limit as `x` approaches 2 of `f(x)` (which is 4) does *not* equal `f(2)` (which is 3) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

## Distinguishing Limits and Function Evaluation

This example highlights the [[differences_between_limits_and_evaluating_functions | key distinction between limits and evaluating functions]] at a specific point <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. A limit describes what the function *intends* to be or *approaches* near a point, regardless of whether the function is actually defined at that point, or if its value "jumps" elsewhere <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. This [[understanding_limits_as_x_approaches_a_value | intuition for limits]] is foundational for more advanced calculus concepts <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

In subsequent lessons, a more formal mathematical (delta-epsilon) definition of a limit will be provided <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. Solving various problems will further build intuition <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. Limits are crucial for understanding [[introduction_to_derivatives | derivatives]] and integrals <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.