---
title: Introduction to Derivatives
videoId: rAof9Ld5sOg
---

From: [[khanacademy]] <br/> 

The study of [[understanding_derivatives | derivatives]] marks a point where mathematics can become significantly more engaging <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. While the term "[[introduction_to_derivatives_in_calculus | derivatives]]" may sound complex, the core concept revolves around understanding rates of change <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Understanding Slope

### Straight Lines
For a straight line, the slope is constant across the entire line <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. It is defined as the change in `y` divided by the change in `x` <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This can be expressed as `delta y` (Δy) divided by `delta x` (Δx) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. For any two points on a straight line, `(x1, y1)` and `(x2, y2)`, the slope is `(y2 - y1) / (x2 - x1)` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Curves
Unlike straight lines, the slope of a curve is not constant; it changes at different points along the curve <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. For example, in a curve like `y = x²`, the slope might be nearly flat at one point and become increasingly steep further along the curve <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Therefore, there is no single slope for the entire curve <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

The challenge, then, is to determine the slope of a curve at a specific point <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## The Tangent Line Problem
The slope of a curve at a specific point is equivalent to the slope of a tangent line that touches the curve at exactly that point <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>, <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. This tangent line shares the same slope as the curve at their point of contact <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

To find this instantaneous slope, one can start by considering a secant line connecting two points on the curve <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. If one point is `(a, f(a))` and the other is `(a + h, f(a + h))`, the slope of this secant line is calculated using the standard slope formula <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>, <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>:

$$
\frac{f(a+h) - f(a)}{(a+h) - a} = \frac{f(a+h) - f(a)}{h}
$$
<a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>

This secant line provides an approximation of the slope at point `(a, f(a))` <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. The accuracy of this approximation improves as `h` (the horizontal distance between the two points) becomes smaller <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## The [[definition_of_the_derivative | Definition of the Derivative]]
To find the exact instantaneous slope at a specific point, one needs to determine what happens to the slope of the secant line as `h` approaches zero <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. This involves the concept of a [[introduction_to_limits | limit]] <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

The [[definition_of_the_derivative | derivative]] is defined as the [[introduction_to_limits | limit]] of the slope of the secant line as `h` approaches 0 <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>:

$$
\text{Derivative} = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}
$$
<a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>

This formula provides the instantaneous slope of the curve at point `a` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. In essence, the [[definition_of_the_derivative | derivative]] is nothing more than the slope of a curve at an exact point <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This powerful tool allows for calculating the slope of most continuous curves at any given point <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

In subsequent discussions, this [[definition_of_the_derivative | definition]] will be applied to specific functions like `x²` to demonstrate its practical use <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.