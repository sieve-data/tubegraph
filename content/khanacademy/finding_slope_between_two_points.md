---
title: Finding slope between two points
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

The idea of [[slope_of_a_line_in_algebra | slope of a line]] is a fundamental concept introduced early in algebra <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Understanding how to calculate it from any two points is crucial <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Defining Slope

To find the [[slope_of_a_straight_line | slope of a straight line]], two distinct points on that line are chosen <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. For a line on a coordinate plane with a y-axis (or f(x)-axis) and an x-axis <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, its slope is consistent throughout <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

The slope can be conceptualized as:
*   **Rise over Run** <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>
*   **Change in y over Change in x** <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>

For a line represented by the equation `y = f(x) = mx + b`, the calculated slope will be the value of `m` <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### General Formula

Consider two points on a line:
*   Point 1: `(a, f(a))` <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>, where `a` is the x-coordinate and `f(a)` is the corresponding y-coordinate <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   Point 2: `(b, f(b))` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, where `b` is the x-coordinate and `f(b)` is the corresponding y-coordinate <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

To find the change in y (rise), subtract the y-coordinates: `f(b) - f(a)` <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This represents the vertical distance between the two points <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

To find the change in x (run), subtract the x-coordinates: `b - a` <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. This represents the horizontal distance <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. It's important to be consistent; if `f(b)` is the first y-value in the numerator, `b` must be the first x-value in the denominator <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

Thus, the formula for [[consistent_calculation_of_slope_from_any_two_points | slope]] is:

```
Slope = (Change in y) / (Change in x) = (f(b) - f(a)) / (b - a)
```
<a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>, <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>

## Example Calculation

Let's use an [[examples_of_calculating_slope_from_various_points | example]] with specific coordinates <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>:
*   Point 1: `(2, 3)` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>
*   Point 2: `(5, 7)` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>

1.  **Change in y**: `7 - 3 = 4` <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
2.  **Change in x**: `5 - 2 = 3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>

Therefore, the slope is `4/3` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Generalizing to Curves (Introduction to Calculus)

While the [[slope_of_a_straight_line | slope of a straight line]] remains constant along its entire length <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>, the slope of a curve is constantly changing <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For a curve like `y = x^2` <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>, the slope varies at different points <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. The slope at any specific point on a curve is defined as the slope of the [[understanding_tangent_and_slope_on_a_curve | tangent line]] to the curve at that point <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

To find the slope at a single point on a curve, the concept of finding the slope between two points is generalized <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

### Slope of a Secant Line

1.  **Define a point**: Let's pick a point `(x₀, f(x₀))` on the curve <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
2.  **Define a second point**: Choose another point `(x₀ + h, f(x₀ + h))`, where `h` represents a small difference in the x-coordinate <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
3.  **Calculate the slope between these two points**: This line connecting the two points is called a secant line <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Using the same formula for slope:
    *   Change in y: `f(x₀ + h) - f(x₀)` <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>
    *   Change in x: `(x₀ + h) - x₀ = h` <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>
    *   Slope of the secant line: `(f(x₀ + h) - f(x₀)) / h` <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>

### Instantaneous Slope (The Derivative)

To find the slope at a *single* point (the [[tangent_line_and_instantaneous_slope | instantaneous slope]]), calculus introduces the concept of a limit <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. By making `h` (the distance between the two points) infinitesimally small, meaning `h` approaches `0` <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>, the secant line becomes increasingly similar to the tangent line at the point `x₀` <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

This limit is defined as the derivative of the function `f(x)` at `x₀`, often denoted as `f'(x₀)`:

```
f'(x₀) = Limit as h approaches 0 of (f(x₀ + h) - f(x₀)) / h
```
<a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>

This derivative `f'(x)` is itself a function that tells you the slope at any given x-value along the curve <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.