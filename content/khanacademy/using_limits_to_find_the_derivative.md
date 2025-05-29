---
title: Using limits to find the derivative
videoId: ANyVpMS3HL4
---

From: [[khanacademy]] <br/> 
## Using Limits to Find the Derivative

The concept of a slope, initially encountered in [[introduction_to_limits_in_calculus|algebra]], provides a foundation for understanding [[differential_calculus_and_rates_of_change|calculus]] concepts like the [[definition_and_application_of_derivatives|derivative]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While the slope of a straight line is consistent, the slope of a curve changes at every point <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Slope of a Line: An Algebra Review

In algebra, the slope of a line is defined as "rise over run," or the [[differential_calculus_and_rates_of_change|change in y over change in x]] (Δy/Δx) <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. To calculate this, two points on the line are selected <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

For example, if two points are `(a, f(a))` and `(b, f(b))` <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>:
*   The change in y (Δy) is `f(b) - f(a)` <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   The change in x (Δx) is `b - a` <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

Thus, the slope `m` is:
$$ m = \frac{f(b) - f(a)}{b - a} $$ <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

**Example**:
If a line passes through points `(2, 3)` and `(5, 7)` <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>:
*   Δy = `7 - 3 = 4` <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
*   Δx = `5 - 2 = 3` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>
*   Slope = `4/3` <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>

### Generalizing to Curves: The Challenge

Unlike lines, the slope of a curve (like `y = x^2`) is constantly changing <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. The slope at any given point on a curve is represented by the slope of the *tangent line* at that point, which is a line that just barely touches the curve <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This means a single slope value cannot describe the entire curve <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### From Secant Line to Tangent Line using Limits

To find the slope at a single point on a curve, the concept of a [[introduction_to_limits|limit]] is employed <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

1.  **Define Two Points on the Curve**:
    Start with a point `(x₀, f(x₀))` on the curve <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. Introduce a second point `(x₀ + h, f(x₀ + h))`, where `h` represents a small horizontal distance from `x₀` <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

2.  **Calculate the Slope of the Secant Line**:
    The line connecting these two points is called a *secant line* <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Its slope is calculated using the standard slope formula:
    $$ \text{Slope of secant} = \frac{f(x_0 + h) - f(x_0)}{(x_0 + h) - x_0} $$
    Simplifying the denominator:
    $$ \text{Slope of secant} = \frac{f(x_0 + h) - f(x_0)}{h} $$ <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>

3.  **Apply the Limit**:
    To find the slope at the single point `(x₀, f(x₀))`, we imagine the second point getting infinitely closer to the first point <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. This is achieved by taking the [[introduction_to_limits_in_calculus|limit]] as `h` approaches zero <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. As `h` gets smaller, the secant line more closely approximates the tangent line at `x₀` <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

### The Definition of the Derivative

The slope of the tangent line at a specific point `x₀` on a curve `f(x)` is called the [[introduction_to_derivatives|derivative]] of `f` at `x₀`, denoted as `f'(x₀)` <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

It is formally defined using the [[introduction_to_limits_in_calculus|limit]] as:
$$ f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} $$ <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>

This [[definition_and_explanation_of_limits|definition and application of derivatives]] yields a new function, `f'(x)`, which provides the slope of the curve at any given x-value <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. While this concept may initially seem abstract, applying it to specific examples helps make it more concrete <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.