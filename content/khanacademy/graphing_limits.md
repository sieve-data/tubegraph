---
title: Graphing limits
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

[[understanding_the_concept_of_limits_in_calculus | Limits]] in calculus can be visually understood by [[calculating_limits_numerically_and_graphically | graphing functions]] and observing the behavior of the expression as the input approaches a specific value <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This approach helps to build intuition for the [[introduction_to_limits | concept of limits]] <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Understanding Limit Notation <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
The notation for a limit is typically written as "the limit as x approaches a certain value of an expression" <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. For example, `lim x→2 x²` asks what value the expression `x²` approaches as `x` approaches 2 <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Visualizing Limits with Continuous Functions
Consider the limit as `x` approaches 2 of `x²`:
```
lim x→2 x² <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>
```
To understand this graphically:
1.  **Graph the function:** The graph of `x²` is a parabola <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  **Identify the target x-value:** In this case, `x = 2` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
3.  **Observe the function's value:** When `x = 2`, `x² = 4` <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
4.  **Approach from both sides:** As `x` approaches 2 from values less than 2 (the left side) and from values greater than 2 (the right side), the value of the expression `x²` approaches 4 <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

> "The way I think about it is as you move on the curve closer and closer to the expression's value, what does the expression equal?" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>

In this simple case, the limit value (4) is equal to the function's value at that point, `f(2) = 4` <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This might seem obvious, but limits become crucial when functions are not continuous at a specific point <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Limits with Functions Having Discontinuities
[[graphing_functions_with_discontinuities | Graphing functions with discontinuities]] demonstrates the unique utility of limits. Consider a piecewise function `f(x)` defined as:
```
f(x) = x²  when x ≠ 2 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
f(x) = 3  when x = 2 <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>
```
To find the limit as `x` approaches 2 of `f(x)`:
```
lim x→2 f(x) <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>
```
1.  **Graph the function:**
    *   For `x ≠ 2`, the graph follows `x²` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
    *   At `x = 2`, there is a "hole" in the graph at `y = 4` because `f(x)` is not defined as `x²` at that exact point <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
    *   Instead, at `x = 2`, the function's value `f(2)` "jumps" to 3 <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   This creates a "gap" in the `x²` curve at `x=2`, with a single point at `(2,3)` <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

2.  **Observe the approach:**
    *   As `x` approaches 2 from the left side (numbers less than 2), `f(x)` approaches values close to 4 <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
    *   Similarly, as `x` approaches 2 from the right side (numbers greater than 2), `f(x)` also slowly approaches 4 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

Therefore, even with the discontinuity, the limit as `x` approaches 2 of `f(x)` is 4 <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

## Comparison of Limits and Function Values
This example highlights a key distinction:
*   `lim x→2 f(x) = 4` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>
*   `f(2) = 3` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>

In this case, the [[comparison_of_limits_and_function_values | limit as x approaches 2]] of `f(x)` does not equal `f(2)` <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This demonstrates the purpose of limits: they describe what a function *approaches* as the input gets arbitrarily close to a certain point, irrespective of whether the function is actually defined at that point, or if its value at that point is different from the surrounding trend <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. This concept is fundamental to [[the_concept_of_a_limit_in_finding_derivatives | derivatives]] and integrals <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.