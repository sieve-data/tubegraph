---
title: Introduction to derivatives in calculus
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

## Review of Slope of a Line
The idea of the slope of a line is initially introduced early in [[Introduction to algebra | algebra]] studies <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. For a line, where `y = f(x)`, the slope is consistent throughout <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

The slope of a line can be understood as:
*   "Rise over run" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   "Change in y over change in x" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

To find the slope between two points on a line, say (a, f(a)) and (b, f(b)):
*   The change in y is `f(b) - f(a)` <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   The change in x is `b - a` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

Thus, the formula for the slope (m) of a line is:
$$m = \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(b) - f(a)}{b - a}$$
For example, if a line passes through points (2, 3) and (5, 7), the slope would be `(7 - 3) / (5 - 2) = 4 / 3` <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This concept is fundamental to [[Differential Calculus and Its Applications | differential calculus]].

## Understanding Slope on a Curve
Unlike a straight line, the slope of a curve is constantly changing <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For instance, on a curve like `y = x^2`:
*   At a negative x-value, the slope is negative <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   As x increases, the slope becomes less negative <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   At x=0, the slope is flat (horizontal) <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   For positive x-values, the slope becomes increasingly positive <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

The slope at any specific point on a curve is defined by the slope of the *tangent line* at that point <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. A tangent line barely touches the curve at that single point <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. Because the slope varies along a curve, one cannot simply ask for "the slope for this curve"; it depends on the specific point <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

## Approaching the Derivative (Slope of a Tangent Line)
The challenge in finding the slope of a curve at a single point is that the traditional slope definition requires two points <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. To address this, we use an approximation approach involving a *secant line*.

### Slope of a Secant Line
Consider two points on a curve `y = f(x)`:
1.  A specific point `(x₀, f(x₀))` <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
2.  A second point slightly offset from the first, `(x₀ + h, f(x₀ + h))`, where `h` represents the horizontal distance between the points <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

The line connecting these two points is called a secant line, and it intersects the curve twice <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. The slope of this secant line is calculated using the standard slope formula:
$$ \text{Slope of secant line} = \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(x_0 + h) - f(x_0)}{(x_0 + h) - x_0} $$
This simplifies to:
$$ \text{Slope of secant line} = \frac{f(x_0 + h) - f(x_0)}{h} $$
<a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a> <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>

### Using Limits to Find the Tangent Slope
The key to finding the slope at a single point is to make the distance `h` between the two points infinitesimally small <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. As `h` approaches zero, the secant line approaches the tangent line at `x₀` <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>. This concept is formalized using [[Introduction to limits | limits]] <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

The slope of the tangent line at a point `x₀` is defined as the [[Definition of the Derivative | derivative]] of `f(x)` at `x₀`, denoted `f'(x₀)`:
$$ f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} $$
<a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a> <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>

This expression is also known as the [[Understanding Derivatives | difference quotient]] or the [[Introduction to Derivatives | definition of the derivative]]. Sometimes, `h` is replaced with `Δx` (delta x), representing a change in x <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

The derivative, `f'(x)`, is itself a function <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. It provides the slope of the original function `f(x)` at any given x-value <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. This foundational concept is central to [[Understanding differential equations and their solutions | calculus]].