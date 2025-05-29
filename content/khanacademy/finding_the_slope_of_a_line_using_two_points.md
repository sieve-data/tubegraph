---
title: Finding the slope of a line using two points
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

The concept of the [[Slope of a line in algebra | slope of a line]] is initially introduced in algebra courses <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is a fundamental idea that describes the steepness and direction of a line on a coordinate plane <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## [[determining_slope | Determining Slope]] from Two Points

To find the [[finding_the_slope_of_a_line | slope of a line]], two points on that line are typically used <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. For a straight line, the slope remains consistent throughout its entire length <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Consider a line drawn on a coordinate plane with a y-axis (or f(x)-axis, where y = f(x)) and an x-axis <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

### Identifying Coordinates

1.  **First Point:** Let's take a point on the line where the x-coordinate is 'a' <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The corresponding y-coordinate would be 'f(a)', so the point is (a, f(a)) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
2.  **Second Point:** Take another point on the line where the x-coordinate is 'b' <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. The corresponding y-coordinate is 'f(b)', making the point (b, f(b)) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

For a straight line, the equation can be expressed as y = mx + b, where 'm' represents the slope <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Slope Formula

The [[properties of slope in linear equations | slope]] is defined as "rise over run" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>, or equivalently, the "change in y over change in x" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

To calculate this:

*   **Change in y (Rise):** This is the difference between the y-coordinates of the two points <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. If we start with the point (b, f(b)), the change in y is f(b) - f(a) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Change in x (Run):** This is the difference between the x-coordinates, keeping the order consistent with the y-coordinates <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. For the chosen order, the change in x is b - a <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

Therefore, the formula for the [[graph interpretation for slope calculation | slope]] (m) is:

$$m = \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(b) - f(a)}{b - a}$$ <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>

### Example Calculation

Let's use specific coordinates to illustrate the calculation <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>:

*   **Point 1:** (2, 3) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>
*   **Point 2:** (5, 7) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>

Applying the formula:

*   Change in y = 7 - 3 = 4 <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
*   Change in x = 5 - 2 = 3 <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>

The slope would be 4/3 <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

## Generalizing Slope to Curves

While the slope of a straight line is constant <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>, the slope of a curve is constantly changing <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For a curve, the slope at any given point is defined by the [[Slope of a curve and tangent lines | slope of the tangent line]] at that point <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

To find the slope at a single point on a curve, the concept of a "secant line" is introduced, which connects two points on the curve <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

If we have a curve y = f(x) and want to find the slope at a specific point (x₀, f(x₀)):

1.  **Define a second point:** Choose a second point (x₀ + h, f(x₀ + h)), where 'h' is a small difference in the x-coordinate <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
2.  **Calculate the slope of the secant line:** Using the standard slope formula <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>:
    $$m_{secant} = \frac{f(x_0 + h) - f(x_0)}{(x_0 + h) - x_0} = \frac{f(x_0 + h) - f(x_0)}{h}$$ <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>
3.  **Apply a limit:** To find the exact slope at the point (x₀, f(x₀)), we take the limit as 'h' approaches zero <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. This means the second point gets infinitesimally close to the first point, causing the secant line to become the tangent line <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

This limiting process defines the [[calculating_the_derivative_as_the_slope_of_tangent_line | derivative]] of the function, denoted as f'(x) <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. The derivative is itself a function that provides the slope of the curve at any given x-value <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.