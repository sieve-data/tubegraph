---
title: Derivatives of trigonometric functions
videoId: S0_qX4VJhMQ
---

From: [[3blue1brown]] <br/> 

Understanding how to [[computing_derivatives_of_functions | compute derivatives]] of specific functions, such as [[trigonometry_in_relation_to_angles_and_triangles | trigonometric functions]], is crucial because many real-world phenomena are modeled using these mathematical expressions <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>, <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Developing fluency with the [[geometric_interpretation_of_derivatives | rates of change]] for these pure, abstract functions provides a language to discuss concrete situations that calculus models <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. It is important to remember that derivatives fundamentally involve examining tiny changes in one quantity and how they relate to a resulting tiny change in another quantity <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Derivative of the Sine Function

### Understanding Sine using the Unit Circle
To understand the [[derivatives_of_exponential_functions | derivative]] of the sine function, it is helpful to be familiar with how to think about [[trigonometry_in_relation_to_angles_and_triangles | trig functions]] using the [[introduction_to_trigonometric_functions | unit circle]] <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>, <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. The [[introduction_to_trigonometric_functions | unit circle]] is a circle with a radius of 1, centered at the origin <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

For a given value of theta (θ), such as 0.8, one can imagine walking around the circle, starting from the rightmost point, until traversing an arc length equal to theta <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>. This means the angle at the center is exactly theta radians, given the unit radius <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. The sine of theta (sin(θ)) is defined as the height of that point above the x-axis <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. As theta increases and one moves around the circle, the height (sin(θ)) oscillates between -1 and 1 <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. When plotted, the graph of sin(θ) versus θ forms a quintessential wave pattern <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>.

### Graphical Intuition
Observing the graph of the sine function can provide an initial sense of its derivative's shape <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>, <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>:
*   At θ = 0, the slope is positive because sin(θ) is increasing <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   As θ approaches its peak, the slope decreases to 0 <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   The slope becomes negative while sin(θ) is decreasing <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
*   The slope returns to 0 as the sine graph levels out before the next peak or valley <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

This pattern suggests that the derivative graph might be exactly the cosine of theta (cos(θ)), as its peaks and valleys align perfectly with those of the cosine function <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>, <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. Indeed, the derivative of sine is cosine <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

### Geometric Derivation
For a more precise understanding, it is necessary to look at what the function actually represents, rather than just its graph <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. Consider the walk around the [[introduction_to_trigonometric_functions | unit circle]] with an arc length of theta <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
1.  **Tiny Nudge:** Imagine a slight nudge, `dθ`, along the circumference of the circle <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>, <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
2.  **Change in Height:** This tiny step changes the sine of theta, resulting in `d(sin(θ))`, which is the change in height above the x-axis <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>, <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
3.  **Right Triangle:** When zoomed in closely, the circle appears as a straight line. A right triangle can be formed where the hypotenuse represents the `dθ` nudge, and the vertical side represents `d(sin(θ))` <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>, <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>, <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
4.  **Similar Triangles:** This tiny triangle is similar to the larger triangle formed by the radius of the [[introduction_to_trigonometric_functions | unit circle]] (hypotenuse of length 1) and the coordinates of the point (cos(θ), sin(θ)) <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>, <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The angle at the origin in the tiny triangle is precisely equal to theta radians <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.
5.  **Ratio:** The derivative of sine is the ratio `d(sin(θ)) / dθ`, which is the tiny change in height divided by the tiny change in the input <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>, <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. From the similar triangles, this ratio corresponds to the length of the side adjacent to the angle theta divided by the hypotenuse <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>, <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. This is exactly the definition of the cosine of theta <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>, <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

Therefore, the derivative of sin(θ) is cos(θ) <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>, <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

## Challenge: Derivative of Cosine
Readers are encouraged to attempt a similar line of reasoning to find the derivative of the cosine of theta <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

## Next Steps
After understanding the [[derivatives_of_exponential_functions | derivatives]] of simple functions like [[trigonometry_in_relation_to_angles and_triangles | trigonometric functions]], the next step is to learn how to find the [[understanding_derivatives_of_combined_functions | derivatives of functions]] that combine these simple forms, such as sums, products, or compositions <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>, <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>. The goal is to understand each rule geometrically to make it intuitively reasonable and more memorable <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.