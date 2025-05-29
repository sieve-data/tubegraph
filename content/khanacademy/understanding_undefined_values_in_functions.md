---
title: Understanding undefined values in functions
videoId: riXcZT2ICjA
---

From: [[khanacademy]] <br/> 

In mathematics, a [[Definition of a function | function]] can sometimes be "undefined" at specific points. This means that for certain input values (x-values), the [[Evaluating functions | function]] does not yield a defined output. Understanding these points is crucial, especially in calculus where the concept of a limit is built upon this idea <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Undefined Rational Expressions

Consider a [[Understanding mathematical equations | function]] defined as:
`f(x) = (x - 1) / (x - 1)` <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>

One might instinctively simplify this to `f(x) = 1` because the numerator and denominator are the same <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. However, this simplification is almost, but not entirely, true <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

The key difference lies in what happens when `x = 1`. If we substitute `x = 1` into the original [[Definition of a function | function]]:
`f(1) = (1 - 1) / (1 - 1) = 0 / 0` <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>, <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>

Any value divided by zero, including 0 divided by 0, is **undefined** <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Therefore, the [[Definition of a function | function]] `f(x) = (x - 1) / (x - 1)` is undefined when `x = 1` <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Graphing Undefined Points

When graphing `f(x) = (x - 1) / (x - 1)`, for any x-value other than 1, `f(x)` will equal 1 <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This creates a horizontal line at `y = 1`. However, at `x = 1`, there is a "gap" or a hole in the graph, signified by an open circle <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>, <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. This visually represents that the [[Definition of a function | function]] is not defined at that specific point <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

Thus, while `f(x) = (x - 1) / (x - 1)` is equal to 1 for all `x` values *other than 1*, it is crucial to add the constraint `x ≠ 1` to truly represent the original [[Definition of a function | function]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>, <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This concept is important for [[excluding_values_for_undefined_rational_expressions | excluding values for undefined rational expressions]].

## Comparing Undefined Points with Discontinuities

It's important to distinguish between a [[Definition of a function | function]] being "undefined" at a point and having a "discontinuity" where the value is explicitly defined but deviates from the surrounding curve.

Consider a piecewise [[Definition of a function | function]] `g(x)`:
`g(x) = x^2` when `x ≠ 2` <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>, <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>
`g(x) = 1` when `x = 2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>

This [[Definition of a function | function]] is discontinuous at `x = 2` <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>, <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Graphing a Discontinuous Function

The graph of `g(x)` largely follows the parabola `y = x^2`. However, at `x = 2`, there is a gap where the parabola would normally be (at `y = 2^2 = 4`), and instead, the [[Definition of a function | function]]'s value "drops down" to 1 <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>, <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>, <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>, <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>, <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

For this [[Definition of a function | function]], when asked to [[Evaluating functions | evaluate]] `g(2)`, you refer to the second part of its definition, which explicitly states `g(2) = 1` <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>, <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. This is different from the first example where `f(1)` was truly undefined due to an invalid mathematical operation.

### Connection to Limits

While `f(1)` is undefined and `g(2)` is explicitly defined as 1, the concept of a "limit" allows us to describe what the [[Definition of a function | function]] is "approaching" as `x` gets closer and closer to these points <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. This highlights the [[differences_between_limits_and_function_evaluation | differences between limits and function evaluation]].

*   For `f(x) = (x - 1) / (x - 1)`: The limit as `x` approaches 1 of `f(x)` is 1, because as `x` gets infinitely close to 1 (but not *at* 1), `f(x)` is always 1 <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>, <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>, <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>, <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   For `g(x)`: The limit as `x` approaches 2 of `g(x)` is 4. This is because as `x` gets closer and closer to 2 from either direction, the `x^2` part of the definition dictates the [[Understanding Variables | variable]]'s behavior, causing `g(x)` to approach 4, even though `g(2)` itself is 1 <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>, <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>, <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>, <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>, <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>, <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>, <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Numeric evaluation confirms this behavior <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>, <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.