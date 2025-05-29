---
title: Introduction to slope of a curve
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

The concept of [[understanding_slope_of_a_straight_line | slope]] is initially introduced in algebra, focusing on straight lines <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, in calculus, this idea is generalized to understand the [[slope_of_a_curve_and_tangent_lines | slope of a curve]], which behaves differently from that of a straight line <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

## Slope of a Straight Line (Algebra Review)

To find the [[finding the slope of a line | slope of a straight line]], two points on the line are selected <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. If these points are (a, f(a)) and (b, f(b)), the [[determining_slope | slope]] is defined as "rise over run" or "change in y over change in x" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Formula for Slope of a Line
The [[slope of a line in algebra | slope]] (m) is calculated using the formula:
```
m = (f(b) - f(a)) / (b - a)
```
*   `f(b) - f(a)` represents the change in y (rise) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   `b - a` represents the change in x (run) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

This formula consistently gives the same slope for any two points on a given straight line <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. For example, if the points are (2, 3) and (5, 7), the slope would be (7 - 3) / (5 - 2) = 4/3 <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## Understanding Slope of a Curve

Unlike straight lines, the [[understanding_slope_as_rate_of_change | slope of a curve]] is not constant; it changes at every point along the curve <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

For instance, consider the curve y = x² <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>:
*   On the left side (negative x-values), the slope is negative, indicating a downward trend <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   As x approaches 0, the slope becomes less negative, eventually flattening out at x=0, where the slope is zero (a horizontal tangent line) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   For positive x-values, the slope becomes positive and increasingly steeper, indicating an upward trend <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

The slope at a specific point on a curve is defined by the [[slope_of_tangent_line_on_a_curve | slope of the tangent line]] at that point <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. A tangent line is a straight line that "just barely touches" the curve at that single point <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Approaching the Slope of a Curve with a Secant Line

To find the slope at a single point on a curve, we start by using two points, similar to how we find the slope of a straight line <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

1.  **Define two points**: Let the first point be (x₀, f(x₀)) <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
2.  **Introduce a second point**: Define a second point by adding a small value `h` to x₀, making the second point (x₀ + h, f(x₀ + h)) <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
3.  **Form a secant line**: The line connecting these two points is called a secant line; it intersects the curve at two points <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

### Slope of the Secant Line
Using the standard slope formula, the slope of the secant line between (x₀, f(x₀)) and (x₀ + h, f(x₀ + h)) is:

$$
\text{Slope of Secant Line} = \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(x_0 + h) - f(x_0)}{(x_0 + h) - x_0}
$$

This simplifies to:

$$
\text{Slope of Secant Line} = \frac{f(x_0 + h) - f(x_0)}{h}
$$
<a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>

## The Derivative: Slope of the Tangent Line

The key insight in calculus is to determine the [[graph_interpretation_for_slope_calculation | slope at a single point]] by letting the second point get infinitely close to the first point <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. This is achieved by taking the limit of the secant line's slope as `h` approaches zero.

As `h` approaches 0, the secant line becomes the [[slope_of_tangent_line_on_a_curve | tangent line]] at the point (x₀, f(x₀)) <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

### Definition of the Derivative
The [[calculating_the_derivative_as_the_slope_of_tangent_line | derivative of a function]] `f(x)` at a specific point `x₀`, denoted as `f'(x₀)` (read as "f prime of x naught"), is defined as:

> <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>
>
> $$
> f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}
> $$

This formula provides the exact slope of the tangent line to the curve at the point `x₀` <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. Since the slope typically changes at every x-value on a curve, the derivative `f'(x)` is itself a function that returns the slope for any given `x` <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. This foundational concept allows us to precisely determine the instantaneous rate of change at any point on a curve.