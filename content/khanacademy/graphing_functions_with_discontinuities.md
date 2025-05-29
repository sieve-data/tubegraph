---
title: Graphing functions with discontinuities
videoId: riXcZT2ICjA
---

From: [[khanacademy]] <br/> 

The idea of a limit is a fundamental concept in calculus <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Despite its importance, it is a relatively simple idea <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. When [[graphing functions with discontinuities | graphing functions]] that have "gaps" or "holes," understanding limits helps describe the function's behavior near those points.

## Functions with a Removable Discontinuity (Hole)

Consider the function defined as `f(x) = (x - 1) / (x - 1)` <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
While it appears this could simplify to `f(x) = 1` because the numerator and denominator are the same <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, there's a crucial difference: `f(x) = (x - 1) / (x - 1)` is undefined when `x = 1` <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This is because if you substitute `x = 1`, you get `0/0`, which is an undefined form <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

Therefore, the function can be expressed as `f(x) = 1`, with the added constraint that `x ≠ 1` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
When [[graphing_rational_expressions | graphing this rational expression]], the function looks like the horizontal line `y = 1` <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. However, at `x = 1`, there is a discontinuity, which is represented by an open circle or "gap" on the graph <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This signifies that the function is not defined at that specific point <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

If asked what `f(1)` is, the answer is "undefined" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. However, the concept of a limit addresses what the function is *approaching* as `x` gets closer and closer to 1 <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
In this case, as `x` approaches 1 from either the left or the right side, `f(x)` is always equal to 1, or getting infinitely close to 1 <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

This is written using limit notation:
`lim (x→1) f(x) = 1` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>
This means that even though `f(1)` is undefined, the function's value approaches 1 as `x` gets infinitely close to 1 <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Functions with a Jump Discontinuity

Another type of discontinuity occurs in piecewise-defined functions. Consider the function `g(x)`:
*   `g(x) = x^2`, when `x ≠ 2` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>
*   `g(x) = 1`, when `x = 2` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>

When [[graphing_quadratic_functions_and_identifying_their_parabolic_shape | graphing this quadratic function]], for all `x` values except `x = 2`, the graph follows the parabola `y = x^2` <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. At `x = 2`, if it followed `x^2`, `y` would be `2^2 = 4`. However, at `x = 2`, the function is explicitly defined as `g(2) = 1` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

So, the graph will be a parabola `y = x^2` with a hole at `(2, 4)` and a single point at `(2, 1)` <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. This represents a "jump" or [[limits_approaching_a_point_of_discontinuity | discontinuity]] in the function <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

To evaluate `g(2)`, you refer directly to the definition for `x = 2`, which gives `g(2) = 1` <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
When considering the limit as `x` approaches 2 for `g(x)`, we look at what `g(x)` is approaching as `x` gets closer and closer to 2 from both sides, *without actually being 2* <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
From the [[graphical_representation_and_visual_understanding_of_functions | graphical representation]], as `x` approaches 2, the function `g(x)` approaches `4` <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

This is written as:
`lim (x→2) g(x) = 4` <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>
Despite `g(2)` being 1, the limit of `g(x)` as `x` approaches 2 is 4 <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### Calculating Limits Numerically and Graphically

[[calculating_limits_numerically_and_graphically | Calculating limits numerically]] involves evaluating the function at values increasingly close to the point of interest. For `g(x)` as `x` approaches 2:

*   **From the left (values less than 2):**
    *   `g(1.9) = 1.9^2 = 3.61` <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>
    *   `g(1.99) = 1.99^2 = 3.9601` <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
    *   `g(1.999) = 1.999^2 = 3.996001` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>
    *   As `x` gets closer to 2, `g(x)` gets closer to 4 <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

*   **From the right (values greater than 2):**
    *   `g(2.1) = 2.1^2 = 4.41` <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>
    *   `g(2.01) = 2.01^2 = 4.0401` <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>
    *   As `x` gets closer to 2, `g(x)` gets closer to 4 <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

Since the function approaches 4 from both directions, the [[graphing_limits | limit]] of `g(x)` as `x` approaches 2 is 4 <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. This demonstrates how to understand and [[graphing_equations | graph equations]] even when they have discontinuities.