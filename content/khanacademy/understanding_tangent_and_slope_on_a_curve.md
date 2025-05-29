---
title: Understanding tangent and slope on a curve
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

The concept of [[slope_of_a_line_in_algebra | slope of a line]] is initially introduced early in algebra studies <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While straightforward for straight lines, understanding [[slope_of_a_curve | slope on a curve]] introduces new complexities and is a fundamental concept in calculus <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

## Review: Slope of a Straight Line

In algebra, to find the [[slope_of_a_straight_line | slope of a straight line]], one typically takes two points on the line <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Let's consider a line represented by `y = f(x)` (or `y = mx + b`) <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>, <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. If we pick two points, `(a, f(a))` and `(b, f(b))` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, the [[slope_of_a_straight_line | slope]] is defined as "rise over run" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>, or more formally, the [[definition_of_slope_as_change_in_y_over_change_in_x | change in y over change in x]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

The formula for finding [[finding_slope_between_two_points | slope between two points]] is:
`Slope = (Change in y) / (Change in x)` <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>

For the points `(a, f(a))` and `(b, f(b))`, this translates to:
`Slope = (f(b) - f(a)) / (b - a)` <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>, <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>

This calculation provides the [[consistent_calculation_of_slope_from_any_two_points | consistent slope]] for the entire straight line <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Example of Calculating Slope

If we have two points, for example, `(2, 3)` and `(5, 7)` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>, <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>:
`Change in y = 7 - 3 = 4` <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
`Change in x = 5 - 2 = 3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
`Slope = 4 / 3` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

## Understanding Slope on a Curve

Unlike a straight line, where the [[slope_of_a_straight_line | slope]] remains constant throughout <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>, the [[slope_of_a_curve | slope of a curve]] is continuously [[slope_of_a_curve | changing]] <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For example, a curve like `y = x²` has a negative slope on the left side, flattens out at the origin (slope of zero), and becomes increasingly positive on the right side <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>, <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>, <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

The [[understanding_slope_from_a_graph | slope of a curve]] at a specific point is defined as the [[tangent_line_and_instantaneous_slope | slope of the tangent line]] at that point <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. A tangent line is a straight line that *just barely touches* the curve at that single point <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

Since the [[slope_of_a_curve | slope]] changes from point to point on a curve, we cannot simply ask for "the slope of the curve." Instead, we ask for the [[tangent_line_and_instantaneous_slope | slope at a specific point]] along the curve <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Deriving the Slope of a Curve (The Derivative)

To find the [[tangent_line_and_instantaneous_slope | instantaneous slope]] at a single point on a curve, we adapt the algebraic definition of slope.

1.  **Define Two Points on the Curve**:
    Let's pick a point `(x₀, f(x₀))` on the curve `y = f(x)` <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. To use the two-point slope formula, we need a second point. We choose a second point that is `h` units away horizontally from `x₀`, so its x-coordinate is `x₀ + h` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. The y-coordinate for this second point is `f(x₀ + h)` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. So the two points are `(x₀, f(x₀))` and `(x₀ + h, f(x₀ + h))` <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

2.  **Calculate the Slope of the Secant Line**:
    A secant line is a line that intersects the curve at two points <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. The [[slope_of_a_line_in_algebra | slope of this secant line]] between `(x₀, f(x₀))` and `(x₀ + h, f(x₀ + h))` is given by the formula:
    `Slope_secant = (Change in y) / (Change in x)` <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>

    *   `Change in y = f(x₀ + h) - f(x₀)` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>
    *   `Change in x = (x₀ + h) - x₀ = h` <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>

    So, the slope of the secant line is:
    `Slope_secant = (f(x₀ + h) - f(x₀)) / h` <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>, <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>

3.  **Introduce the Concept of a Limit**:
    To find the [[tangent_line_and_instantaneous_slope | slope at a single point]], we need the two points to become infinitesimally close to each other <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This is achieved by taking the *limit* as `h` (the distance between the two x-coordinates) approaches zero <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. As `h` gets smaller, the secant line connecting the two points gets closer and closer to becoming the [[tangent_line_and_instantaneous_slope | tangent line]] at `x₀` <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>, <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

    The [[tangent_line_and_instantaneous_slope | instantaneous slope]] at `x₀` is therefore defined as:
    `Slope_tangent = lim (h→0) [ (f(x₀ + h) - f(x₀)) / h ]` <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>

    This expression represents the [[tangent_line_and_instantaneous_slope | slope of the tangent line]] at the point `x₀` <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

## The Derivative

This specific limit definition for the [[tangent_line_and_instantaneous_slope | instantaneous slope]] is called the **derivative** of the function `f(x)` <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. It is commonly denoted as `f'(x)` (read as "f prime of x") <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

The derivative `f'(x)` is itself another function <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. Given an x-value, `f'(x)` tells you the exact [[tangent_line_and_instantaneous_slope | slope of the tangent line]] (and thus the [[slope_of_a_curve | slope of the curve]]) at that specific point <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>, <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. This concept is fundamental to calculus and allows us to analyze the rate of change of any function, not just straight lines.