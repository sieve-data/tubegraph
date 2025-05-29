---
title: Understanding limit notation
videoId: W0VWO4asgmk
---

From: [[khanacademy]] <br/> 

The concept of a [[introduction_to_limits | limit]] is fundamental in calculus, often serving as an [[understanding_the_concept_of_limits_in_calculus | introduction to limits]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. [[Understanding the concept of limits in calculus | It asks what value an expression approaches as a variable gets closer to a specific number]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## How to Write Limit Notation

Limit notation is written as:
`lim x→c f(x)` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>

*   `lim`: Abbreviation for "limit" <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   `x→c`: Indicates that the variable `x` is approaching a specific value `c` (e.g., `x` approaches 2) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   `f(x)`: Represents the [[function_notation_and_usage | function]] or expression whose value is being observed <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

The entire notation asks: "What value does the expression `f(x)` approach as `x` approaches `c`?" <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>

## Examples of Understanding Limit Notation

### Example 1: Simple Function `x^2`

Consider the limit: `lim x→2 x^2` <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>

This notation asks what value `x^2` approaches as `x` approaches 2 <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

*   **Graphical Interpretation**: When [[graphing limits | graphing]] `y = x^2`, as `x` gets closer to 2 from both the left (numbers less than 2) and the right (numbers greater than 2), the value of `x^2` approaches 4 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Result**: `lim x→2 x^2 = 4` <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

In this simple case, the [[comparison_of_limits_and_function_values | limit is equal to the function's value]] at that point (e.g., if `f(x) = x^2`, then `f(2) = 4`) <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Example 2: Function with a Defined Point (Discontinuity)

Consider a [[limits_with_undefined_or_jump_function_points | function with a defined point different from its surrounding trend]]:
`f(x) = x^2` when `x ≠ 2` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>
`f(x) = 3` when `x = 2` <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>

Now, consider the limit: `lim x→2 f(x)` <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>

*   **Graphical Interpretation**: The graph of this function looks like `x^2` everywhere except at `x = 2`. At `x = 2`, there is a "hole" at `y = 4`, and the function's value "jumps" down to `y = 3` <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>, <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Calculating the Limit**: As `x` approaches 2 from both the left and right sides along the curve, the `f(x)` values approach 4, even though `f(2)` itself is 3 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>, <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Result**: `lim x→2 f(x) = 4` <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

This example highlights a key distinction: the [[comparison_of_limits_and_function_values | limit of a function as x approaches a point may not be equal to the function's value at that point]] (`lim x→2 f(x) ≠ f(2)` in this case, as `4 ≠ 3`) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. [[Limits are useful for understanding function behavior even when the function is undefined or jumps at a specific point]] <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Importance of Limits

The concept of a limit provides intuition for how a function behaves near a certain point, regardless of its exact value at that point <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This idea is crucial for understanding advanced calculus topics like [[the_concept_of_a_limit_in_finding_derivatives | derivatives]] and integrals <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. More formal definitions, such as the delta-epsilon definition, further solidify this concept <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. Practical application through [[calculating_limits_numerically_and_graphically | problem-solving]] helps build intuition for limits <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.