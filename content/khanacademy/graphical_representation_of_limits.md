---
title: Graphical representation of limits
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

This article provides an [[introduction_to_limits | explanation of limits]] using graphical examples <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Understanding Limits with `x^2`

The notation for a limit, such as "the limit as x approaches 2 of x squared," asks what value the expression `x` squared approaches as `x` approaches 2 <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>, <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

Consider the function `f(x) = x^2`:
*   When `x` is equal to 2, the expression `x^2` is equal to 4 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   Graphically, as `x` approaches 2 from both sides (from numbers less than 2 and from numbers greater than 2), the expression `x^2` approaches 4 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   Moving along the curve of `x^2` closer and closer to `x=2`, the `f(x)` value gets closer and closer to 4 <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   In this simple case, one might assume the limit is the same as directly evaluating the function at that point (e.g., `f(2) = 4`) <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Limits with Discontinuities

To illustrate the purpose of limits, consider a new function `f(x)` defined as:
*   `f(x) = x^2` when `x` is not equal to 2 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   `f(x) = 3` when `x` is equal to 2 <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

This function is a slight variation of `x^2`. Graphically, it looks like the `x^2` curve, but at `x=2`:
*   There is a "hole" or "gap" in the graph at the point where `x=2` and `f(x)=4`, because the function is not defined as `x^2` at `x=2` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>, <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   Instead, at `x=2`, the function `f(x)` is defined as 3, creating an isolated point at `(2,3)` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

Now, consider the limit as `x` approaches 2 for this new `f(x)`:
*   As `x` approaches 2 from the left side (numbers less than 2), `f(x)` approaches values near 4 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>, <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   Similarly, as `x` approaches 2 from the right side, `f(x)` also approaches 4 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>, <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   Therefore, the limit as `x` approaches 2 for this `f(x)` is 4 <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>, <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

### Key Distinction

This example highlights the [[differences_between_limits_and_function_evaluation | difference between a limit and direct function evaluation]]:
*   In this case, the limit as `x` approaches 2 of `f(x)` (which is 4) does *not* equal `f(2)` (which is 3) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   Limits are useful for functions where, at a certain point, the function might not be defined or it "jumps" up or down <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>, <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Even when the function has [[graphing_functions_with_discontinuities | discontinuities]], the limit describes the value the function *approaches* <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

## Further Exploration

Understanding limits intuitively through graphical representation provides a foundation for more formal definitions and concepts in calculus, such as [[using_limits_to_find_the_derivative | derivatives and integrals]] <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.