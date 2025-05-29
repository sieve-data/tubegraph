---
title: Concept of slope as rise over run
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

The idea of [[slope_of_a_line_in_algebra | slope]] is first encountered early in algebra studies <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It's a fundamental concept that describes the steepness and direction of a line or curve.

## Understanding Slope for a Straight Line

To understand [[slope_of_a_line_in_algebra | slope]], consider a coordinate system with a y-axis (also called the f(x)-axis) and an x-axis <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. If a straight line is drawn on these axes, its [[slope_of_a_straight_line | slope]] can be determined <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

The [[slope_of_a_line_in_algebra | slope]] of a line is consistently the same throughout its entire length <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. In algebra, this value corresponds to 'm' in the [[slopeintercept_form | slope-intercept form]] equation of a line, `y = f(x) = mx + b` <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

The most common ways to conceptualize [[slope_of_a_line_in_algebra | slope]] are:
*   **Rise over Run**: This visually represents the vertical change (rise) relative to the horizontal change (run) <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Change in Y over Change in X**: This is a more formal way of expressing rise over run, written as `Δy / Δx` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Calculating Slope from Two Points

To calculate the [[slope_of_a_line_in_algebra | slope]] of a line, two distinct points on that line are needed <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Let's consider two arbitrary points on a line: `(a, f(a))` and `(b, f(b))` <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

The [[definition_of_slope_as_change_in_y_over_change_in_x | change in y]] is the difference between the y-coordinates of the two points: `f(b) - f(a)` <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This represents the 'rise' <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

The [[definition_of_slope_as_change_in_y_over_change_in_x | change in x]] is the difference between the x-coordinates of the two points: `b - a` <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This represents the 'run' <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

Therefore, the [[slope_of_a_line_in_algebra | slope]] (m) is calculated as:
$m = \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(b) - f(a)}{b - a}$ <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

#### Example Calculation
For example, if we have two points: (2, 3) and (5, 7) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>:
*   Change in y = 7 - 3 = 4 <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
*   Change in x = 5 - 2 = 3 <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
*   Slope = 4/3 <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

This straightforward method for calculating [[slope_of_a_line_in_algebra | slope]] is a core concept from Algebra 1 <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The [[consistent_calculation_of_slope_from_any_two_points | slope remains consistent]] regardless of which two points are chosen on a straight line <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Generalizing Slope to Curves

In calculus, the concept of [[slope_of_a_line_in_algebra | slope]] is extended to curves, where the [[slope_of_a_curve | slope]] is constantly changing <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For instance, on a curve like `y = x²` <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>:
*   At negative x-values, the [[slope_of_a_curve | slope]] is negative and steep <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   As x approaches zero, the [[slope_of_a_curve | slope]] becomes less negative, eventually becoming flat (zero) at `x=0` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   For positive x-values, the [[slope_of_a_curve | slope]] becomes positive and increasingly steeper <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

Since the [[slope_of_a_curve | slope]] varies at every point on a curve, we cannot simply ask "what is the slope for this curve?" <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Instead, we refer to the [[slope_of_a_curve | slope]] *at a specific point* on the curve <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This is defined by the [[slope_of_a_curve | slope]] of the tangent line to the curve at that point <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. A tangent line is a line that just barely touches the curve at a single point <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Approximating Slope with a Secant Line

To find the [[slope_of_a_curve | slope]] at a single point `(x₀, f(x₀))` on a curve, we need to adapt the two-point [[definition_of_slope_as_change_in_y_over_change_in_x | slope]] formula <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. We introduce a second point that is a small horizontal distance `h` away from the first point: `(x₀ + h, f(x₀ + h))` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

The line connecting these two points is called a **secant line** <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. The [[slope_of_a_line_in_algebra | slope]] of this secant line is calculated using the familiar [[definition_of_slope_as_change_in_y_over_change_in_x | change in y over change in x]] formula <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>:

Slope of Secant Line $= \frac{f(x_0 + h) - f(x_0)}{(x_0 + h) - x_0}$ <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>

Simplifying the denominator:
Slope of Secant Line $= \frac{f(x_0 + h) - f(x_0)}{h}$ <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>

### The Limit and the Derivative

To find the exact [[slope_of_a_curve | slope]] at the single point `(x₀, f(x₀))`, we imagine the second point getting infinitesimally close to the first point <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. This is achieved by taking the **limit** of the secant line [[slope_of_a_line_in_algebra | slope]] as `h` approaches zero <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. As `h` gets smaller, the secant line approaches the tangent line at that point <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

This concept leads to the **definition of the derivative**:
$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$ <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>

This formula, $f'(x)$, represents the [[slope_of_a_curve | slope]] of the tangent line to the curve at any given point `x` <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. The derivative `f'(x)` is itself a function because the [[slope_of_a_curve | slope]] changes at different x-values on a curve <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

This transition from the consistent [[slope_of_a_straight_line | slope of a straight line]] to the varying [[slope_of_a_curve | slope of a curve]] via limits is a fundamental shift in understanding the concept of [[slope_of_a_line_in_algebra | slope]], marking the beginning of calculus <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.