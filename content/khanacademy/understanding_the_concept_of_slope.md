---
title: Understanding the concept of slope
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 

The idea of [[Slope of a line in algebra | slope of a line]] is often introduced early in algebra studies <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It's a fundamental concept that describes the steepness and direction of a line.

## Slope of a Straight Line

For a straight line, the [[Slope of a line in algebra | slope]] is consistent throughout its entire length <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It can be thought of as "rise over run" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>, or more formally, as the [[understanding slope as change in y over change in x | change in y over the change in x]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

To [[finding the slope of a line | find the slope of a line]], one typically selects two distinct points on the line <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. If a line is represented by the function `y = f(x)` (or `f(x) = mx + b`), and two points are `(a, f(a))` and `(b, f(b))` <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>, the slope is calculated as follows:

$$
\text{Slope} = \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(b) - f(a)}{b - a}
$$

<a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a> <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

### Example Calculation for a Line
Consider two points on a line: `(2, 3)` and `(5, 7)` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   The change in y (rise) is `7 - 3 = 4` <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   The change in x (run) is `5 - 2 = 3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
Therefore, the [[Slope of a line in algebra | slope]] of this line is `4/3` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

The slope of a straight line remains constant regardless of which two points are chosen for the calculation <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a> <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This means there is [[consistency in calculating slope | consistency in calculating slope]] across the entire line.

## Slope of a Curve

Unlike straight lines, the [[Slope of a Curve | slope of a curve]] is not constant; it changes at different points along the curve <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. To understand the [[interpreting slope from a graph | slope of a curve]] at a specific point, the concept of a [[Slope of a curve using tangent lines | tangent line]] is used <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. A tangent line touches the curve at exactly one point, and its slope represents the slope of the curve at that particular point <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

For example, on a curve like `y = x²` <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>:
*   On the left side (negative x-values), the tangent lines show a negative slope <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   As x approaches 0, the slope becomes less negative <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   At `x = 0`, the slope is zero (the tangent line is horizontal) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   On the right side (positive x-values), the slope starts increasing and becomes positive <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

## Generalizing Slope to a Curve (Introduction to Derivatives)

To [[finding the slope of a line | find the slope]] at a single point on a curve, we start by using the two-point method from algebra <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
1.  **Select a point of interest:** Let this be `(x₀, f(x₀))` <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
2.  **Select a second point:** Choose a second point slightly displaced from the first, `(x₀ + h, f(x₀ + h))` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Here, `h` represents a small change in `x` <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
3.  **Calculate the slope of the secant line:** The line connecting these two points is called a secant line <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Its slope is given by the [[understanding slope as change in y over change in x | change in y over change in x]] <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>:
    $$
    \text{Slope of Secant} = \frac{f(x_0 + h) - f(x_0)}{(x_0 + h) - x_0} = \frac{f(x_0 + h) - f(x_0)}{h}
    $$
    <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a> <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>

4.  **Introduce the Limit:** To find the slope at the *single* point `(x₀, f(x₀))`, we imagine `h` becoming infinitesimally small, approaching zero <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. As `h` gets closer to zero, the second point gets closer to the first, and the secant line approaches the [[Slope of a curve using tangent lines | tangent line]] at `x₀` <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. This is expressed using a limit:
    $$
    \text{Slope at } x_0 = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}
    $$
    <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>

This limit, which represents the [[Slope of a curve using tangent lines | slope of the tangent line]] at a point `x₀` <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>, is known as the **derivative of f** at `x₀`, denoted as `f'(x₀)` <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. Since the slope of a curve changes at every x-value, the derivative `f'(x)` is itself a function that tells you the slope at any given point on the curve <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.