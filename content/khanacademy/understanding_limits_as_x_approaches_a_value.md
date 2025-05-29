---
title: Understanding limits as x approaches a value
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

The concept of a [[introduction_to_limits | limit]] describes what value an expression or function approaches as its input (`x`) gets closer and closer to a specific number <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This is distinct from simply evaluating the function at that exact point <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## How Limits are Written

A [[introduction_to_limits | limit]] is formally written as:
`limit as x approaches 'a' of f(x)` <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

This notation asks: "What value does the expression `f(x)` approach as `x` approaches 'a'?" <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## [[exploring_function_behavior_at_specific_points | Exploring Function Behavior at Specific Points]]

To understand the behavior of a function near a point, we observe what value the function approaches as `x` gets arbitrarily close to that point from both the left (numbers less than 'a') and the right (numbers greater than 'a') <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Example 1: `limit as x approaches 2 of x^2`

Consider the function `f(x) = x^2` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **[[graph_interpretation_in_the_context_of_limits | Graphically]]**, `x^2` forms a parabola <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   As `x` approaches 2, `x^2` approaches 4 <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   In this simple case, the [[introduction_to_limits | limit]] (4) is the same as evaluating the function at that point (`f(2) = 2^2 = 4`) <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This might make the concept seem obvious <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Example 2: When the Limit Differs from the Function Value

The utility of [[introduction_to_limits | limits]] becomes clear when evaluating functions with "wrinkles" or discontinuities <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

Consider a modified function `f(x)` defined as:
*   `f(x) = x^2` when `x ≠ 2` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   `f(x) = 3` when `x = 2` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

This function is almost identical to `x^2`, but at `x = 2`, its value "jumps" to 3 instead of 4 <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

*   **[[graph_interpretation_in_the_context_of_limits | Graphically]]**: The graph of `f(x)` looks like `x^2` with a "hole" at `(2, 4)` and a distinct point at `(2, 3)` <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Finding the limit**: To find the `limit as x approaches 2 of f(x)` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>:
    *   As `x` approaches 2 from the left (numbers less than 2), `f(x)` follows the `x^2` curve and approaches 4 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
    *   As `x` approaches 2 from the right (numbers greater than 2), `f(x)` also follows the `x^2` curve and approaches 4 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   Therefore, the [[introduction_to_limits | limit]] as `x` approaches 2 for this `f(x)` is 4 <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### [[differences_between_limits_and_evaluating_functions | Differences between Limits and Evaluating Functions]]

In the second example, we see a key distinction <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>:
*   The `limit as x approaches 2 of f(x) = 4` <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>
*   However, `f(2) = 3` (as defined for this specific function) <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

This illustrates that the value a function *approaches* (its limit) can be different from its actual value *at* that point <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. [[introduction_to_limits | Limits]] are crucial for understanding function behavior, especially where functions might be undefined or have discontinuities <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

Further study of [[introduction_to_limits | limits]] involves a more formal delta-epsilon definition <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, and their application in calculus, particularly in the understanding of derivatives and integrals <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.