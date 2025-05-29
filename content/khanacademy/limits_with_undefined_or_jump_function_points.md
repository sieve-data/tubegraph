---
title: Limits with undefined or jump function points
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

[[Introduction to limits | Limits]] explore what value an expression approaches as an input approaches a certain point <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This concept becomes particularly useful when dealing with functions that have [[limits_approaching_a_point_of_discontinuity | discontinuities]] or [[difference_between_undefined_points_and_values_in_a_function | undefined points]].

## Basic Limit Example: Continuous Function

Consider the expression `x^2` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. To find the limit as `x` approaches 2, denoted as `lim (x->2) x^2`, we determine what value `x^2` approaches as `x` gets closer to 2 <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

[[Graphing limits | Graphing]] `x^2` shows a continuous curve <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>:
```
       |
     4 +       .
       |     .
     3 +   .
       | .
     2 +
       |
     1 +
       +-------------
       0   1   2   3
```
As `x` approaches 2 from either the left (numbers less than 2) or the right (numbers greater than 2), the value of `x^2` approaches 4 <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Thus, the limit as `x` approaches 2 for `x^2` is 4 <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. In this simple case, evaluating the function at `x=2` (i.e., `f(2) = 2^2 = 4`) yields the same result as the limit <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Limits with a Jump Discontinuity

The true utility of [[calculating_limits_numerically_and_graphically | limits]] becomes apparent with functions that are not continuous <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Consider a modified function `f(x)` defined as:
*   `f(x) = x^2` if `x ≠ 2` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
*   `f(x) = 3` if `x = 2` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

This function looks like `x^2` everywhere except at `x=2`. At `x=2`, there is a "gap" where the `x^2` curve would be, and the function's value "jumps" to 3 <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

The [[graphing_limits | graph]] illustrates this:
```
       |
     4 +       o  (hole where x^2 would be at x=2)
       |     .
     3 +   .   .  (point at x=2, y=3)
       | .
     2 +
       |
     1 +
       +-------------
       0   1   2   3
```
When `x=2`, the function `f(x)` is equal to 3 <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Evaluating the Limit at the Discontinuity

Now, let's find the limit as `x` approaches 2 for this new `f(x)`: `lim (x->2) f(x)` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

To evaluate this limit, we observe the function's behavior as `x` gets closer to 2, *without* considering the actual value *at* `x=2` <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   As `x` approaches 2 from the left (values less than 2), `f(x)` follows the `x^2` curve and approaches 4 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   Similarly, as `x` approaches 2 from the right (values greater than 2), `f(x)` also follows the `x^2` curve and approaches 4 <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

Since `f(x)` approaches the same value (4) from both sides, the limit as `x` approaches 2 for this `f(x)` is 4 <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>, <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Comparison of Limit and Function Value

In this example, the [[comparison_of_limits_and_function_values | limit]] as `x` approaches 2 is 4, but the function's value at `x=2` (`f(2)`) is 3 <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This demonstrates a key difference:
*   A limit describes the value a function *approaches* as the input gets arbitrarily close to a certain point <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   The function value describes the function's actual output *at* that specific point <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

This distinction is fundamental, especially when dealing with functions that are not defined at a particular point or exhibit a jump, as the limit can still exist even if the function value is different or nonexistent <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.