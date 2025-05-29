---
title: Definition of the Derivative
videoId: rAof9Ld5sOg
---

From: [[khanacademy]] <br/> 

The concept of [[understanding_derivatives | derivatives]] marks a shift in mathematics, making it "a lot more fun" <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. While the term may sound complicated <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, the [[understanding_derivatives | derivative]] provides a way to understand the [[slope_of_a_curve | slope]] of curves, not just straight lines <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Slope of a Straight Line

Traditionally, the [[understanding_the_concept_of_slope | slope]] of a straight line is defined as the change in 'y' divided by the change in 'x' (Δy / Δx) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. For a straight line, this [[understanding_the_concept_of_slope | slope]] remains constant across the entire line <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. To calculate it, one can pick any two points on the line, determine the change in their y-coordinates (Δy) and x-coordinates (Δx), and divide Δy by Δx <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>, <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## The Challenge of Curves

Unlike straight lines, the [[slope_of_a_curve | slope of a curve]] (e.g., y = x²) is not constant; it continuously changes <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. A curve might start almost flat and then get progressively steeper <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>, <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This raises the question of how to determine the [[slope_of_a_curve | slope]] of a curve whose [[slope_of_a_curve | slope]] is constantly changing <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. There is no single [[slope_of_a_curve | slope]] for the entire curve <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Introducing the Tangent Line

To address this, the concept of finding the [[slope_of_a_curve | slope]] *at a given point* on a curve is introduced <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>, <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. The [[slope_of_a_curve | slope]] at a specific point on a curve is defined as the [[understanding_the_concept_of_slope | slope]] of a *tangent line* at that point <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>, <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. A tangent line is a straight line that just touches the curve at that exact point <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. At the point of tangency, the curve and the tangent line share the same [[understanding_the_concept_of_slope | slope]] <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>, <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

## The Role of Limits in Defining the Derivative

The [[understanding_derivatives | derivative]] provides the method to calculate this instantaneous [[understanding_the_concept_of_slope | slope]] <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. It leverages the concept of limits, which for the first time reveal their practical utility <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

To find the [[understanding_the_concept_of_slope | slope]] at a specific point `(a, f(a))` on a curve:

1.  **Secant Line Approximation**: Start by finding the [[understanding_the_concept_of_slope | slope]] of a *secant line* between two points on the curve <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. One point is `(a, f(a))`, and the other is `(a + h, f(a + h))`, where `h` represents a small horizontal distance from `a` <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>, <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>, <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>, <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
2.  **Secant Line Slope Formula**: The [[understanding_the_concept_of_slope | slope]] of this secant line is calculated using the standard [[understanding_the_the_concept_of_slope | slope]] formula:
    *   Change in y: `f(a + h) - f(a)` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>, <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>
    *   Change in x: `(a + h) - a = h` <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>, <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>, <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>
    *   So, the slope of the secant line is `(f(a + h) - f(a)) / h` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>, <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
    This secant line's [[understanding_the_concept_of_slope | slope]] provides an approximation of the curve's [[slope_of_a_curve | slope]] at `(a, f(a))` <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>, <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
3.  **Approaching the Tangent Line**: The closer `h` gets to zero, the closer the second point `(a + h, f(a + h))` gets to `(a, f(a))` <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>, <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. As `h` approaches zero, the secant line approaches the tangent line <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>, <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>, and its [[understanding_the_concept_of_slope | slope]] becomes a better approximation of the instantaneous [[slope_of_a_curve | slope]] at that point <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>, <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
4.  **The Definition of the Derivative**: To find the exact instantaneous [[slope_of_a_curve | slope]] at `(a, f(a))`, we take the limit of the secant line [[understanding_the_concept_of_slope | slope]] as `h` approaches zero <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>, <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>, <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. This limit is precisely the [[introduction_to_derivatives | definition of the derivative]]:

    > `f'(a) = lim (h -> 0) [f(a + h) - f(a)] / h` <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>, <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>

This formula defines the [[understanding_derivatives | derivative]] as the [[slope_of_a_curve | slope]] of a curve at an exact point <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>, <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This powerful tool allows us to find the [[slope_of_a_curve | slope]] for most continuous curves at any specific point <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>, <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.