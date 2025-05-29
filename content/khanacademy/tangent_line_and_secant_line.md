---
title: Tangent Line and Secant Line
videoId: rAof9Ld5sOg
---

From: [[khanacademy]] <br/> 

Derivatives are a mathematical concept that allow for the calculation of the slope of a curve at any given point <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This differs from the [[Slope of a Straight Line | slope of a straight line]], which remains constant across the entire line <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Slope of a Straight Line

For a straight line, the [[Slope of a line in algebra | slope]] is defined as the change in y divided by the change in x (Δy/Δx) <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This slope is consistent at every point on the line <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Slope of a Curve

Unlike a straight line, the slope of a curve, such as `y = x^2`, constantly changes <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. For instance, the curve `y = x^2` starts almost flat, then gets progressively steeper <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Since there is no single slope for the entire curve, calculus aims to determine the [[slope_of_a_curve_using_tangent_lines | slope at a specific point]] <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Tangent Line

The [[slope_of_a_curve_using_tangent_lines | slope of a curve at a given point]] is equivalent to the slope of a tangent line at that point <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. A tangent line touches the curve at exactly one point <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. The slope of this tangent line reflects the instantaneous slope of the curve at that specific point <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. As demonstrated, the slope of the tangent line can vary significantly along a curve; it might be negative at one point and positive and steeper at another <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Secant Line

To determine the slope of a curve at a specific point, one can use a [[secant_lines_and_their_slopes | secant line]] as an approximation <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. A [[secant_lines_and_their_slopes | secant line]] connects two distinct points on the curve <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

The slope of a [[secant_lines_and_their_slopes | secant line]] between two points, `(a, f(a))` and `(a + h, f(a + h))`, is calculated using the standard slope formula:
$$ \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(a + h) - f(a)}{(a + h) - a} = \frac{f(a + h) - f(a)}{h} $$
<a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a> <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>

### From Secant to Tangent: The Derivative

The approximation provided by a [[secant_lines_and_their_slopes | secant line]] improves as the two points it connects move closer together <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. If the distance `h` between the two points approaches zero, the [[secant_lines_and_their_slopes | secant line]] approaches the tangent line at that point <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

The [[slope_of_a_curve_using_tangent_lines | slope of the tangent line]] (and thus the instantaneous slope of the curve) is found by taking the limit of the [[secant_lines_and_their_slopes | secant line]]'s slope as `h` approaches zero <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>:
$$ \lim_{h \to 0} \frac{f(a + h) - f(a)}{h} $$
<a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>

This limit is precisely the definition of the derivative <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. The derivative, therefore, allows for finding the exact slope of a continuous curve at any given point <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.