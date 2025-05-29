---
title: Derivative of trigonometric functions with unit circle analysis
videoId: S0_qX4VJhMQ
---

From: [[3blue1brown]] <br/> 

Understanding the [[derivatives_and_integrals | derivatives]] of functions, particularly those with explicit formulas, is a fundamental step in calculus <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While it's easy to focus on memorizing rules, a deeper understanding comes from exploring the [[geometric_interpretation_of_derivatives | geometric interpretation of derivatives]] and the concept of tiny nudges <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>, <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This approach is particularly insightful for [[derivatives_of_trigonometric_and_exponential_functions | trigonometric functions]].

## Visualizing Sine on the Unit Circle

To understand the derivative of the sine function, it's essential to be familiar with its representation on the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]] <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

The [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]] is a circle with a radius of 1, centered at the origin <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   For a given angle `theta` (in radians), you imagine moving along the circle's circumference starting from the point (1,0) <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.
*   The distance traversed along the arc is `theta` <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
*   The value of `sine(theta)` is the vertical height of that point above the x-axis <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
*   As `theta` increases, this height oscillates between -1 and 1, creating the characteristic wave pattern when graphed <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>, <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.

## Derivative of Sine: Graphical Intuition

By observing the graph of `sine(theta)`, we can infer the shape of its derivative <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>:
*   At `theta = 0`, the slope of `sine(theta)` is positive because the function is increasing <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   As `sine(theta)` approaches its peak (e.g., at `theta = pi/2`), the slope decreases to 0 <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   When `sine(theta)` is decreasing (e.g., between `pi/2` and `3pi/2`), the slope is negative <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
*   The slope returns to 0 as the sine graph flattens out (e.g., at `theta = 3pi/2`) <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

This pattern of slopes perfectly aligns with the graph of `cosine(theta)` <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>, <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. Indeed, the derivative of `sine(theta)` is `cosine(theta)` <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. However, a graphical view alone doesn't provide the *precise* reasoning behind this fact <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>, <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

## Derivative of Sine: Unit Circle Analysis

To understand *why* the derivative of `sine(theta)` is precisely `cosine(theta)`, we must return to the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]] and consider tiny changes <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

1.  **Tiny Nudge**: Imagine a point on the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]] corresponding to `theta`. Now, take a tiny step `d(theta)` along the circumference <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
2.  **Change in Height**: This `d(theta)` step causes a change in the height (which is `sine(theta)`). Let's call this change `d(sine(theta))` <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
3.  **Approximation with a Triangle**: When zoomed in sufficiently close, the arc `d(theta)` can be approximated as the hypotenuse of a tiny right triangle <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>, <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
    *   The vertical side of this tiny triangle represents `d(sine(theta))`, the change in height <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
4.  **Similar Triangles**: This tiny triangle is similar to a larger triangle formed by the radius of the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]] (hypotenuse of length 1), the x-axis, and the vertical line representing `sine(theta)` <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>, <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.
    *   Crucially, the angle within the tiny triangle at the point of interest is `theta` <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
5.  **Ratio of Change**: The derivative of sine is the ratio of `d(sine(theta))` (tiny change in height) to `d(theta)` (tiny change in input) <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
    *   In the tiny right triangle, `d(sine(theta))` is the side adjacent to the angle `theta`, and `d(theta)` is the hypotenuse <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>, <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
    *   The ratio of the adjacent side to the hypotenuse is, by definition, the `cosine(theta)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>, <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

Therefore, the derivative of `sine(theta)` is `cosine(theta)` <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>, <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. This geometric understanding emphasizes how [[derivatives_of_simple_functions_and_their_intuition | derivatives]] fundamentally deal with "tiny nudges" <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>, <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

> [!challenge] Challenge
> Using a similar line of reasoning based on the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]], try to determine the derivative of `cosine(theta)` <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

Future discussions often involve [[taking_derivatives_of_complex_combinations_of_functions | taking derivatives of complex combinations of functions]], such as sums, products, or compositions of simple functions <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>, <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.