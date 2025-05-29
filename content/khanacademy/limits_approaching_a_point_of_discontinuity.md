---
title: Limits approaching a point of discontinuity
videoId: riXcZT2ICjA
---

From: [[khanacademy]] <br/> 

[[introduction_to_limits | Limits]] are a fundamental concept in calculus, which, despite their importance, represent a simple idea <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. They form the basis for all of calculus <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

The concept of a limit explores what a function is *approaching* as the input variable approaches a certain value, regardless of the function's actual value at that exact point <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. This is particularly useful when dealing with [[graphing_functions_with_discontinuities | functions that have discontinuities]].

## Functions Undefined at a Point

Consider the function `f(x)` defined as:
`f(x) = (x - 1) / (x - 1)` <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

While it might seem that `f(x)` simplifies to `1` because the numerator and denominator are the same <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, this is not entirely accurate. The expression `(x - 1) / (x - 1)` is [[limits_with_undefined_or_jump_function_points | undefined]] when `x = 1` because it results in `0/0` <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Therefore, `f(x)` can be defined as `f(x) = 1` with the important constraint that `x ≠ 1` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>, <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

### Graphing the Discontinuity

When [[graphing_functions_with_discontinuities | graphing this function]], it appears as a horizontal line at `y = 1` <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. However, at `x = 1`, there is a "gap" or a "hole" in the graph, represented by an open circle, to signify that the function is [[limits_with_undefined_or_jump_function_points | undefined]] at that point <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>, <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Limit vs. Function Value

*   **Function Value**: `f(1)` is [[limits_with_undefined_or_jump_function_points | undefined]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Limit**: The [[understanding_limit_notation | limit]] as `x` approaches `1` of `f(x)` asks what value the function is approaching as `x` gets infinitesimally close to `1`, from both the left and the right side <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. For `f(x) = (x - 1) / (x - 1)`, as `x` approaches `1`, `f(x)` is always `1` (as long as `x ≠ 1`) <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
    ```
    lim (x→1) f(x) = 1
    ```
    This demonstrates the distinction between the actual [[comparison_of_limits_and_function_values | function value]] at a point and the value the function is [[understanding_the_concept_of_limits_in_calculus | approaching]] <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## Functions with Jump Discontinuities

Another example involves a function with a "jump" discontinuity:

`g(x) = x²` when `x ≠ 2` <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>, <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>
`g(x) = 1` when `x = 2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>

### Graphing the Discontinuity

When [[graphing_functions_with_discontinuities | graphing]] `g(x)`, it largely follows the parabola `y = x²` <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. However, at `x = 2`, there is a gap in the parabola (an open circle) because the function's definition changes for that specific point <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. Instead, at `x = 2`, `g(x)` drops down to `1`, creating a distinct point that is off the parabola <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>, <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>, <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>, <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

### Limit vs. Function Value

*   **Function Value**: `g(2)` is equal to `1`, as per the explicit definition <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Limit**: The [[understanding_limit_notation | limit]] as `x` approaches `2` of `g(x)` asks what value `g(x)` is approaching as `x` gets closer and closer to `2` from both sides (e.g., `1.9, 1.99, 1.999` or `2.1, 2.01, 2.001`) <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>, <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
    *   Visually, by [[graphing_limits | drawing the graph]], it's clear that as `x` approaches `2`, `g(x)` approaches `4` <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>, <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>, <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
    *   Numerically, [[calculating_limits_numerically_and_graphically | calculating]] `g(x)` for values very close to `2` (like `1.9`, `1.99`, `1.999` or `2.1`, `2.01`, `2.001`) by squaring them (`x²`) shows the results approaching `4` <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>, <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>, <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>, <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>, <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>, <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>, <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>, <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>, <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>, <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>, <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
    ```
    lim (x→2) g(x) = 4
    ```
    Even though `g(2) = 1`, the [[the_concept_of_a_limit_in_finding_derivatives | limit]] of `g(x)` as `x` approaches `2` is `4` <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>, <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>, <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>, <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

> [!NOTE]
> The idea of a [[introduction_to_limits | limit]] focuses on the behavior of a function *around* a point, not necessarily *at* the point itself. This concept is crucial for [[understanding_the_concept_of_limits_in_calculus | understanding limits in calculus]] and is foundational for [[the_concept_of_a_limit_in_finding_derivatives | derivatives]].