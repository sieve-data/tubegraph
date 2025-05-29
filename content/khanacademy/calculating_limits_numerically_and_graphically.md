---
title: Calculating limits numerically and graphically
videoId: riXcZT2ICjA
---

From: [[khanacademy]] <br/> 

[[understanding_the_concept_of_limits_in_calculus | Limits]] are a foundational concept in calculus, forming the basis for the entire field <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Despite their importance, the [[introduction_to_limits | idea of a limit]] is relatively simple <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. It asks what a function is *approaching* as the input `x` gets closer and closer to a certain value, regardless of what the function actually *is* at that specific point <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Example 1: Function with a Hole

Consider the function `f(x)` defined as:
`f(x) = (x - 1) / (x - 1)` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

While it might seem that `f(x)` simplifies to `1` because the numerator and denominator are the same <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, there's a crucial difference: `f(x)` is [[limits_approaching_a_point_of_discontinuity | undefined]] when `x = 1` <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This is because substituting `x = 1` results in `0/0`, which is an undefined expression <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

To accurately represent the function, it can be stated as:
`f(x) = 1`, with the constraint that `x ≠ 1` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### [[graphing_functions_with_discontinuities | Graphing Functions with Discontinuities]]

[[graphing_limits | Graphing]] `f(x) = (x - 1) / (x - 1)` reveals a horizontal line at `y = 1` with a "hole" or "gap" at `x = 1` <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This signifies that the function is not defined at that specific point <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. If asked for `f(1)`, the answer is "undefined" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

### [[limits_approaching_a_point_of_discontinuity | Understanding Limits at a Discontinuity]]

When considering the limit, we ask what the function is *approaching* as `x` gets closer to `1` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
Visually, as `x` approaches `1` from either the left or the right side, the function's `y`-value is consistently `1` <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

Using [[understanding_limit_notation | limit notation]]:
`lim (x→1) f(x) = 1` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>

This notation simply asks what value the function approaches as `x` gets closer and closer to `1` <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Example 2: Piecewise Function with Discontinuity

Consider another function, `g(x)`, defined as a piecewise function:
*   `g(x) = x^2` when `x ≠ 2` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>
*   `g(x) = 1` when `x = 2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>

### [[graphing_functions_with_discontinuities | Graphing Functions with Discontinuities]]

[[graphing_limits | Graphing]] `g(x)` shows a parabola `y = x^2` for all `x` values except `x = 2` <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. At `x = 2`, the function's value "drops down" to `1` <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This creates a [[limits_approaching_a_point_of_discontinuity | discontinuity]] at `x = 2` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

When evaluating `g(2)`:
`g(2) = 1` (according to the function's definition) <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>

### Calculating Limits Graphically and Numerically

To find the limit of `g(x)` as `x` approaches `2`, we ask what value `g(x)` is approaching as `x` gets infinitely close to `2` <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

Using [[understanding_limit_notation | limit notation]]:
`lim (x→2) g(x)` <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>

#### Graphically
By observing the graph, as `x` values get closer to `2` (from either side), the `y`-values on the parabola `y = x^2` get closer to `4` (since `2^2 = 4`) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
Therefore, `lim (x→2) g(x) = 4` <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

#### Numerically
We can also approach the limit numerically by plugging in `x` values increasingly close to `2` (but not `2` itself) <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

| x (approaching from below) | g(x) = x² |
| :------------------------- | :---------- |
| 1.9                        | 3.61        |
| 1.99                       | 3.96        |
| 1.999                      | 3.996       |
| 1.9999999999               | ~4          |

| x (approaching from above) | g(x) = x² |
| :------------------------- | :---------- |
| 2.1                        | 4.41        |
| 2.01                       | 4.0401      |

As `x` gets closer to `2` from both directions, `g(x)` values consistently approach `4` <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

### [[comparison_of_limits_and_function_values | Comparison of Limits and Function Values]]

This example highlights a key distinction:
*   `g(2) = 1` (the actual function value at `x=2`) <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>
*   `lim (x→2) g(x) = 4` (what the function *approaches* as `x` gets close to `2`) <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>

The limit describes the trend of the function's behavior around a point, even if the function itself is discontinuous or undefined at that exact point <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This concept is fundamental to [[the_concept_of_a_limit_in_finding_derivatives | derivatives]] and other areas of calculus.