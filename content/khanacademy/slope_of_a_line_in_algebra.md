---
title: Slope of a line in algebra
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

The concept of [[slope_of_a_straight_line | slope of a line]] is typically introduced early in algebra studies <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Defining Slope for a Straight Line

To understand [[slope_of_a_straight_line | slope]], consider a coordinate plane with a y-axis (also referred to as the f(x)-axis where `y = f(x)`) <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a> and an x-axis <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. When a straight line is drawn on these axes <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, its slope is constant throughout its entire length <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Lines can be represented in [[slopeintercept_form | slope-intercept form]], `f(x) = mx + b` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>, where `m` is the slope.

### Calculation Method: Two Points

To find the [[finding_slope_between_two_points | slope of a line]], pick any two distinct points on that line <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
Let these points be:
*   Point 1: `(a, f(a))` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
*   Point 2: `(b, f(b))` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>

The [[definition_of_slope_as_change_in_y_over_change_in_x | slope]] is fundamentally defined as "rise over run" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>, or more formally, the [[definition_of_slope_as_change_in_y_over_change_in_x | change in y divided by the change in x]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

The formula for the slope `m` between two points `(x1, y1)` and `(x2, y2)` is:

$m = \frac{\text{change in y}}{\text{change in x}} = \frac{y_2 - y_1}{x_2 - x_1}$ <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>

Using the points `(a, f(a))` and `(b, f(b))`:

$m = \frac{f(b) - f(a)}{b - a}$ <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>

This calculation directly gives the value of `m` in the [[slopeintercept_form | y = mx + b]] equation <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Concrete Example of Finding Slope

Consider two points on a line: `(2, 3)` and `(5, 7)` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

*   Change in y (rise): `7 - 3 = 4` <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
*   Change in x (run): `5 - 2 = 3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>

The slope is $\frac{4}{3}$ <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

## Generalizing Slope to a Curve (Introduction to Calculus)

While the [[slope_of_a_straight_line | slope of a straight line]] is constant, the [[slope_of_a_curve | slope of a curve]] is continuously changing <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For a curve, the slope at any given point is defined by the [[understanding_tangent_and_slope_on_a_curve | slope of the tangent line]] at that specific point <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. The tangent line is a line that just barely touches the curve at one point <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

To conceptualize the [[slope_of_a_curve | slope of a curve]] at a single point, we start with the two-point slope definition and apply the concept of limits:

1.  **Define a point:** Let `(x₀, f(x₀))` be the point on the curve where we want to find the slope <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
2.  **Define a second point:** Choose a second point slightly away from the first, `(x₀ + h, f(x₀ + h))`, where `h` represents a small difference in the x-coordinate <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
3.  **Calculate the slope of the secant line:** The line connecting these two points is called a secant line <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Its slope is given by the familiar formula:
    $\text{Slope of secant} = \frac{\text{change in y}}{\text{change in x}} = \frac{f(x_0 + h) - f(x_0)}{(x_0 + h) - x_0}$ <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>
    This simplifies to:
    $\text{Slope of secant} = \frac{f(x_0 + h) - f(x_0)}{h}$ <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>
4.  **Take the limit:** To find the slope at the *single* point `(x₀, f(x₀))`, we imagine the second point getting infinitesimally close to the first point. This is achieved by taking the limit as `h` approaches zero:
    $\text{Slope of tangent} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$ <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>

This expression defines the derivative of the function `f(x)` at `x₀`, often denoted as `f'(x₀)` <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. The derivative is itself a function that tells you the [[slope_of_a_curve | slope of the curve]] at any given `x` value <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

> [!NOTE]
> The variable `h` is sometimes referred to as `Δx` (delta x) in other contexts, representing the change in x <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. The meaning remains the same.