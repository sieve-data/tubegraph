---
title: Tangent line and instantaneous slope
videoId: rAof9Ld5sOg
---

From: [[khanacademy]] <br/> 

Derivatives are a mathematical concept that allows for finding the slope of a curve at a specific point, which is a significant advancement beyond finding the [[slope_of_a_straight_line | slope of a straight line]] <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Slope of a Straight Line

For a [[slope_of_a_straight_line | straight line]], the [[slope_of_a_line_in_algebra | slope]] is consistent across its entire length <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. It is calculated as the [[finding_slope_between_two_points | change in y divided by the change in x]] (Δy/Δx) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This is straightforward because the line's steepness does not vary <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. A straight line can be represented by the [[slopeintercept_form | standard equation y = mx + b]] <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Slope of a Curve

Unlike a straight line, the [[understanding_tangent_and_slope_on_a_curve | slope of a curve]] is constantly changing <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. For instance, in a curve like y = x², the slope starts nearly flat and becomes increasingly steep <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Therefore, there isn't a single slope for the entire curve <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### The Tangent Line

To address this, the concept of the [[understanding_tangent_and_slope_on_a_curve | slope at a given point]] on a curve is introduced <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. This is defined as the slope of a [[understanding_tangent_and_slope_on_a_curve | tangent line]] to the curve at that specific point <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. A [[understanding_tangent_and_slope_on_a_curve | tangent line]] just touches the curve at that exact point, sharing the same slope as the curve at that instant <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## Approximating Instantaneous Slope

To find the [[slope_and_its_relation_to_average_and_instantaneous_speed | instantaneous slope]] at a specific point (a, f(a)) on a curve (e.g., y = x²), one can approximate it using a [[slope_of_a_straight_line | secant line]] <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

1.  **Choose two points**: Select the point of interest (a, f(a)) and another nearby point on the curve, (a+h, f(a+h)), where 'h' represents a small horizontal distance from 'a' <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
2.  **Calculate Secant Line Slope**: The slope of the [[slope_of_a_straight_line | secant line]] connecting these two points is calculated using the standard [[finding_slope_between_two_points | slope formula]]:
    $$ \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(a+h) - f(a)}{(a+h) - a} = \frac{f(a+h) - f(a)}{h} $$ <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>

This [[slope_of_a_straight_line | secant line's slope]] serves as an approximation of the [[understanding_tangent_and_slope_on_a_curve | curve's slope]] at point 'a' <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

## The Derivative: Finding Instantaneous Slope

The approximation becomes more accurate as 'h' gets smaller, bringing the second point closer to the first <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. To find the exact [[slope_and_its_relation_to_average_and_instantaneous_speed | instantaneous slope]] of the [[understanding_tangent_and_slope_on_a_curve | tangent line]], one must consider what happens as 'h' approaches zero <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

This concept leads to the definition of the [[understanding_tangent_and_slope_on_a_curve | derivative]]:
$$ f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h} $$ <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>

As 'h' approaches zero, the [[slope_of_a_straight_line | secant line]] effectively transforms into the [[understanding_tangent_and_slope_on_a_curve | tangent line]], providing the exact [[slope_and_its_relation_to_average_and_instantaneous_speed | instantaneous slope]] at that point on the curve <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The [[understanding_tangent_and_slope_on_a_curve | derivative]] is fundamentally the slope of a curve at an exact point <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This allows for finding the slope of almost any [[understanding_tangent_and_slope_on_a_curve | continuous curve]] at a specific point <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.