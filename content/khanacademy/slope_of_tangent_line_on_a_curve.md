---
title: Slope of tangent line on a curve
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

Initially, the concept of [[finding the slope of a line | slope of a line]] is introduced early in algebra <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article reviews how to find the [[finding the slope of a line | slope of a line]] and then generalizes this concept to find the slope of a curve at a specific point, which is known as the [[slope_of_a_curve_and_tangent_lines | slope of the tangent line]].

## Review: Slope of a Straight Line

To [[understanding_slope_of_a_straight_line | understand the slope of a straight line]], consider a line on a coordinate plane with a y-axis (or f(x)-axis) and an x-axis <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. If we have two points on this line, say `(a, f(a))` and `(b, f(b))` <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>, the slope of the line can be defined as:

> **Slope = Rise / Run** <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>
> or
> **Slope = Change in y / Change in x** <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>

Using the two points `(a, f(a))` and `(b, f(b))`, the formula for the [[finding the slope of a line using two points | slope]] is:

$$
\text{Slope} = \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(b) - f(a)}{b - a}
$$

For example, if the points are (2, 3) and (5, 7) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>, the slope would be:

$$
\text{Slope} = \frac{7 - 3}{5 - 2} = \frac{4}{3}
$$ <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

This slope is consistent throughout the entire line <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## [[introduction_to_slope_of_a_curve | Introduction to Slope of a Curve]]

Unlike a straight line where the slope is constant, the [[slope_of_a_curve_and_tangent_lines | slope of a curve]] is continuously changing <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For a curve like `y = x^2` <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>:
*   On the left side (negative x-values), the slope is negative <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   As you move towards the origin, the slope becomes less negative <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   At `x=0`, the slope is flat (horizontal) <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   On the right side (positive x-values), the slope becomes positive and increases <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

The slope at any given point on a curve is defined as the slope of the *tangent line* at that point <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. A tangent line is a line that just barely touches the curve at a single point <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Calculating the Slope of a Tangent Line (The Derivative)

To find the slope of a curve at a specific point, we can start by using two points, similar to how we found the slope of a straight line <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

1.  **Define Two Points on the Curve**:
    *   Let the point of interest be `(x₀, f(x₀))` <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
    *   Choose a second point slightly away from the first point, `(x₀ + h, f(x₀ + h))`, where `h` represents a small horizontal distance from `x₀` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

2.  **Calculate the Slope of the Secant Line**:
    The line connecting these two points is called a *secant line* <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Its slope is calculated using the standard slope formula:

    $$
    \text{Slope of Secant Line} = \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(x_0 + h) - f(x_0)}{(x_0 + h) - x_0}
    $$ <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>

    Simplifying the denominator:

    $$
    \text{Slope of Secant Line} = \frac{f(x_0 + h) - f(x_0)}{h}
    $$ <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>

3.  **Take the Limit as h Approaches Zero**:
    The key insight is to bring the second point infinitesimally close to the first point. This is achieved by taking the limit of the secant line's slope as `h` approaches 0 <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. As `h` gets smaller, the secant line more closely approximates the tangent line at the point of interest <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

    $$
    \text{Slope of Tangent Line} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}
    $$ <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>

    This expression represents the [[calculating the derivative as the slope of tangent line | derivative]] of the function `f(x)` at the point `x₀` <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. It is denoted as `f'(x₀)` (read as "f prime of x₀") <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

    The derivative `f'(x)` is itself a function, providing the slope of the tangent line at any given x-value on the curve <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
    Alternatively, `h` can be referred to as `Δx` (delta x), signifying a change in x <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. The concept remains identical <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

    This definition is fundamental to calculus and allows us to precisely determine the instantaneous rate of change (slope) of a curve at any point <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.