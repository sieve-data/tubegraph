---
title: Slope of a curve using tangent lines
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

While the concept of [[Slope of a Straight Line | slope]] is first introduced in [[slope_of_a_line_in_algebra | algebra]] as a constant value for a straight line <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, understanding the [[Slope of a Curve | slope of a curve]] requires a more nuanced approach involving [[Tangent Line and Secant Line | tangent lines]] <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

## Slope of a Straight Line Review

The [[finding the slope of a line | slope of a straight line]] is consistent throughout its entire length <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It is defined as the "rise over run" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>, or the change in y divided by the change in x <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

To [[finding the slope of a line | find the slope]] between any two points (x₁, y₁) and (x₂, y₂) on a line:
*   The change in y (`Δy`) is y₂ - y₁ <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   The change in x (`Δx`) is x₂ - x₁ <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   The slope (m) = `Δy / Δx` = (y₂ - y₁) / (x₂ - x₁) <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

> [!EXAMPLE]
> Given points (2, 3) and (5, 7) on a line:
> *   Change in y = 7 - 3 = 4 <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
> *   Change in x = 5 - 2 = 3 <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
> *   Slope = 4/3 <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

## The Challenge with Curves

Unlike a straight line, the [[Slope of a Curve | slope of a curve]] is continuously changing <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For instance, on a curve like y = x², the slope is negative on one side, zero at the minimum point, and positive on the other side <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. Therefore, one cannot simply ask for "the slope of this curve" without specifying a particular point <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. The slope is different at every point along the curve <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

The slope of a curve at a specific point is defined by the [[Tangent Line and Secant Line | tangent line]] at that point <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. A tangent line touches the curve at only one point and indicates the instantaneous direction of the curve at that point <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Approximating with Secant Lines

To find the slope of a curve at a single point (x₀, f(x₀)), traditional [[using_different_points_to_determine_slope | two-point slope formulas]] are insufficient <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. Instead, we use a two-step process:

1.  **Define Two Points**: Select the point of interest (x₀, f(x₀)) and a second nearby point on the curve (x₀ + h, f(x₀ + h)), where `h` represents a small horizontal distance from x₀ <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
2.  **Calculate the Slope of the Secant Line**: A [[Tangent Line and Secant Line | secant line]] is a line that intersects the curve at two points <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. The [[secant_lines_and_their_slopes | slope of this secant line]] between (x₀, f(x₀)) and (x₀ + h, f(x₀ + h)) is calculated using the standard slope formula <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>:

    `Slope of Secant = (Change in y) / (Change in x)`
    `Slope of Secant = (f(x₀ + h) - f(x₀)) / ((x₀ + h) - x₀)`
    `Slope of Secant = (f(x₀ + h) - f(x₀)) / h` <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>

This secant line's slope is an approximation of the curve's slope at x₀ <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## The Concept of the Limit and the Derivative

To find the exact [[Slope of a Curve | slope of the curve]] at a single point, we consider what happens as the second point gets infinitely close to the first point <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. This is achieved by taking the [[understanding_the_concept_of_slope | limit]] as `h` approaches zero <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. As `h` approaches 0, the [[Tangent Line and Secant Line | secant line]] becomes the [[Tangent Line and Secant Line | tangent line]] at the point (x₀, f(x₀)) <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

This limit defines the **derivative** of the function, denoted as f'(x) or f prime of x <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>:

`f'(x) = Limit (as h → 0) of [(f(x + h) - f(x)) / h]` <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>

This formula provides a new function, f'(x), which represents the [[interpreting_slope_from_a_graph | slope of the tangent line]] (and thus the slope of the curve) at any given x-value <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. Since the slope changes at every point on a curve, the derivative is itself a function <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.