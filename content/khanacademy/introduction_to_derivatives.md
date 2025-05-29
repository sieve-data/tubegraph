---
title: Introduction to derivatives
videoId: rAof9Ld5sOg
---

From: [[khanacademy]] <br/> 

Welcome to the presentation on [[derivatives_and_calculus_terminology | derivatives]], a concept that makes math more engaging <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. While the term may sound complicated <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, the core idea relates to understanding the slope of lines and curves.

## Slope of a Straight Line

For a straight line, calculating the [[introduction_to_slope_of_a_curve | slope]] is straightforward <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The [[introduction_to_slope_of_a_curve | slope]] is consistently the "change in y divided by the change in x" (Δy/Δx) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This value remains constant across the entire straight line <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. To find it, one can select any two points on the line, determine the change in their y-coordinates (Δy) and x-coordinates (Δx), and divide Δy by Δx <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## The Challenge of a Curve's Slope

Unlike a straight line, the [[introduction_to_slope_of_a_curve | slope]] of a curve is not constant; it continuously changes <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. For example, consider the curve `y = x²` <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. At different points, its [[introduction_to_slope_of_a_curve | slope]] can vary from being almost flat to becoming increasingly steep <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This means there isn't a single [[introduction_to_slope_of_a_curve | slope]] for the entire curve <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

Instead, we aim to determine the "[[introduction_to_slope_of_a_curve | slope]] at a given point" on the curve <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This is conceptualized as the [[introduction_to_slope_of_a_curve | slope]] of a tangent line to the curve at that specific point <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. A tangent line touches the curve at exactly one point and shares the same instantaneous [[introduction_to_slope_of_a_curve | slope]] as the curve at that point <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## Finding the Slope of a Curve: Secant Lines and Limits

To find the instantaneous [[introduction_to_slope_of_a_curve | slope]] of a curve at a specific point `(a, f(a))` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>:

1.  **Secant Line Approximation**: We can start by approximating the [[introduction_to_slope_of_a_curve | slope]] using a secant line <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. A secant line connects two points on the curve. Let's pick a second point `(a + h, f(a + h))` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. The [[introduction_to_slope_of_a_curve | slope]] of this secant line is given by the familiar formula <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>:
    $$ \text{Slope} = \frac{\text{change in y}}{\text{change in x}} = \frac{f(a+h) - f(a)}{(a+h) - a} = \frac{f(a+h) - f(a)}{h} $$
    This formula represents the [[introduction_to_slope_of_a_curve | slope]] of the secant line between the two points <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

2.  **Refining with [[the_concept_of_a_limit_in_finding_derivatives | Limits]]**: The closer the second point `(a + h, f(a + h))` gets to the first point `(a, f(a))` (i.e., as `h` gets smaller) <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>, the better the secant line's [[introduction_to_slope_of_a_curve | slope]] approximates the tangent line's [[introduction_to_slope_of_a_curve | slope]] <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. To find the exact instantaneous [[introduction_to_slope_of_a_curve | slope]], we need to find what happens as `h` approaches `0` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This is where the concept of a [[introduction_to_limits | limit]] becomes essential <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

    The [[introduction_to_slope_of_a_curve | slope]] of the tangent line (the instantaneous [[introduction_to_slope_of_a_curve | slope]]) is defined as the [[the_concept_of_a_limit_in_finding_derivatives | limit]] of the secant line's [[introduction_to_slope_of_a_curve | slope]] as `h` approaches `0` <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>:
    $$ \text{Slope of Tangent Line} = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h} $$
    As `h` approaches `0`, the secant line converges to the tangent line <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>, giving us the exact [[introduction_to_slope_of_a_curve | slope]] at that instantaneous point on the curve <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

## Definition of the Derivative

This formula is precisely the [[definition_and_significance_of_the_derivative | definition of the derivative]] <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. The [[definition_and_significance_of_the_derivative | derivative]] is fundamentally the [[introduction_to_slope_of_a_curve | slope]] of a curve at an exact point <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This allows us to calculate the [[introduction_to_slope_of_a_curve | slope]] for nearly any continuous curve at any given point <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

In subsequent discussions, this [[definition_and_significance_of_the_derivative | definition]] will be applied to specific functions like `x²` to solve practical problems <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.