---
title: Slope of a curve and tangent lines
videoId: rAof9Ld5sOg
---

From: [[khanacademy]] <br/> 

Derivatives mark a point where mathematics becomes considerably more engaging <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The concept of a derivative, while sounding complex, is fundamentally about finding the [[slope_of_a_line_in_algebra | slope]] of a curve at a specific point <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## [[understanding_slope_of_a_straight_line | Slope of a Straight Line]]

For a straight line, the [[finding_the_slope_of_a_line | slope]] is constant across the entire line <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. To [[determining_slope | determine the slope]] of a straight line, one can pick any two points on the line <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The slope is calculated as the change in y (Δy) divided by the change in x (Δx) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This is represented as Δy / Δx <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Slope of a Curve

Unlike straight lines, the [[slope_of_a_line_in_algebra | slope]] of a curve is not constant; it changes at different points along the curve <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. For example, in a curve like y = x², the slope starts almost flat, then becomes progressively steeper <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Since the slope is continuously changing, there is no single slope for the entire curve <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### [[slope_of_tangent_line_on_a_curve | Tangent Lines]]

To understand the [[slope_of_a_line_in_algebra | slope]] of a curve, we focus on the [[slope_of_tangent_line_on_a_curve | slope at a given point]] <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. The slope at a specific point on a curve is defined as the [[slope_of_tangent_line_on_a_curve | slope of a tangent line]] to that point <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. A tangent line touches the curve at exactly one point, and at that exact point, the curve and the tangent line have the same slope <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. The slope of the tangent line can vary along the curve; for instance, it might be negative at one point and positive at another <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Approximating with Secant Lines

To [[calculating_the_derivative_as_the_slope_of_tangent_line | calculate the slope]] of a tangent line at a specific point (e.g., x = a) on a curve, one can approximate it using a secant line <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. A secant line connects two points on the curve. By choosing a second point close to the first point (e.g., at x = a + h, where h is a small distance), the slope of the secant line between these two points provides an approximation of the tangent line's slope <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

The slope of this secant line is calculated using the standard [[finding_the_slope_of_a_line_using_two_points | slope formula]]:
Slope = (Change in y) / (Change in x) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>

Given two points:
*   (a, f(a)) <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>
*   (a + h, f(a + h)) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>

The slope of the secant line is:
$$ \frac{f(a+h) - f(a)}{(a+h) - a} = \frac{f(a+h) - f(a)}{h} $$ <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>

The closer 'h' gets to zero, the closer the second point gets to the first, and the better the approximation of the tangent line's slope becomes <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### The Derivative: Limit of the Secant Slope

To find the exact instantaneous [[slope_of_tangent_line_on_a_curve | slope of the curve]] at a point, we find the limit of the secant line's slope as 'h' approaches zero <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

$$ \text{Slope}_{\text{tangent}} = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h} $$ <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>

As h approaches 0, the secant line approaches the tangent line, and its slope becomes the exact [[calculating_the_derivative_as_the_slope_of_tangent_line | instantaneous slope]] at that point on the curve <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. This specific limit is the formal [[calculating_the_derivative_as_the_slope_of_tangent_line | definition of the derivative]] <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. The derivative is, therefore, the slope of a curve at an exact point <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This concept allows for [[graph_interpretation_for_slope_calculation | determining the slope]] of any continuous curve at any given point <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.