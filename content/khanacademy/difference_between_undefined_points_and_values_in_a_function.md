---
title: Difference between undefined points and values in a function
videoId: riXcZT2ICjA
---

From: [[khanacademy]] <br/> 

The idea of a limit is fundamental to calculus <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. While seemingly complex, it is a very simple concept <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>: what value a function is [[comparison_of_limits_and_function_values | approaching]] as its input approaches a certain point, even if the function is not defined at that specific point.

## Undefined Points in Rational Functions

Consider the [[definition_of_a_function | function]] `f(x)` defined as:
`f(x) = (x - 1) / (x - 1)` <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>

While it might seem that `f(x)` simplifies to `1` (as anything divided by itself equals 1) <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, there's a critical difference. The original expression is [[excluding_values_to_avoid_undefined_expressions | undefined]] when the denominator is zero <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

If we attempt to evaluate `f(1)`:
`f(1) = (1 - 1) / (1 - 1) = 0 / 0` <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
Division by zero, including 0 divided by 0, is [[limits_with_undefined_or_jump_function_points | undefined]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

Therefore, `f(x)` can be expressed as `f(x) = 1` with the important [[excluding_values_to_avoid_undefined_expressions | constraint]] that `x` cannot be equal to 1 <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### Graphing `f(x)`

The graph of `f(x) = (x - 1) / (x - 1)` is a horizontal line `y = 1`, but with a hole (or discontinuity) at `x = 1` <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This signifies that the function is not defined at that specific point <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Limit vs. Function Value (Example 1)

Even though `f(1)` is [[limits_with_undefined_or_jump_function_points | undefined]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>, we can still ask what value the function is [[comparison_of_limits_and_function_values | approaching]] as `x` gets closer to 1 <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

As `x` approaches 1 from either the left or the right side, the value of `f(x)` is always 1 <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

The limit is denoted as:
`lim (x->1) f(x) = 1` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>

This notation asks what the function is [[comparison_of_limits_and_function_values | approaching]] as `x` gets infinitely close to 1, without actually being at 1 <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. In this case, the function is exactly 1 throughout the approach <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

## Undefined Points in Piecewise Functions

Consider another [[definition_of_a_function | function]], `g(x)`, defined piecewise as:
`g(x) = x^2` when `x != 2` <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>
`g(x) = 1` when `x = 2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>

This [[definition_of_a_function | function]] has a [[limits_with_undefined_or_jump_function_points | discontinuity]] <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Graphing `g(x)`

The graph of `g(x)` resembles a parabola `y = x^2` for all values of `x` except `x = 2` <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. At `x = 2`, there is a gap where the `x^2` curve would normally be (at `y = 4`), and instead, the [[definitions_of_points_and_line_segments | point]] `(2, 1)` is plotted <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

### Limit vs. Function Value (Example 2)

If asked to [[evaluating_expressions_with_different_variable_values | evaluate]] `g(2)`, by its [[definition_of_a_function | definition]], `g(2) = 1` <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

However, the limit question asks:
`lim (x->2) g(x)` <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>

This asks what `g(x)` is [[comparison_of_limits_and_function_values | approaching]] as `x` gets closer and closer to 2, from both directions <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

- As `x` approaches 2 from values less than 2 (e.g., 1.9, 1.99, 1.999), `g(x)` (which is `x^2` for these values) approaches 4 <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
  - `1.9^2 = 3.61` <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>
  - `1.99^2 = 3.96` <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
  - `1.999^2 = 3.996` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>
- As `x` approaches 2 from values greater than 2 (e.g., 2.1, 2.01, 2.001), `g(x)` also approaches 4 <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
  - `2.1^2 = 4.41` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>
  - `2.01^2 = 4.0401` <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>

Therefore, the limit is:
`lim (x->2) g(x) = 4` <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>

This example illustrates that the limit of a [[definition_of_a_function | function]] as `x` approaches a certain point can be different from, or even exist when, the function's actual value at that point is [[limits_with_undefined_or_jump_function_points | undefined]] or distinct <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. The limit describes the trend of the function's values in the vicinity of a point, not necessarily its value at the point itself.