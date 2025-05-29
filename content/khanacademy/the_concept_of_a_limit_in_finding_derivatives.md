---
title: The concept of a limit in finding derivatives
videoId: rAof9Ld5sOg
---

From: [[khanacademy]] <br/> 

[[introduction_to_derivatives | Derivatives]] mark a point where mathematics can become significantly more engaging <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. While the term "derivative" might sound complex <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, its core purpose is to determine the slope of a curve at a specific point <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Slope of a Straight Line vs. A Curve

### Straight Lines
For a straight line (e.g., `y = mx + b`), the slope is consistent across the entire line <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The slope is defined as the change in y (Δy) divided by the change in x (Δx) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a> <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### The Challenge of Curves
Unlike straight lines, the slope of a curve, such as `y = x²`, is constantly changing <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. The curve's slope can vary from almost flat to extremely steep <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This means there isn't a single slope for the entire curve <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

To address this, the concept of a [[definition_and_significance_of_the_derivative | derivative]] allows us to find the slope at any *given point* on the curve <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## The Role of the Tangent Line

The slope of a curve at a specific point is equivalent to the slope of a **tangent line** at that point <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. A tangent line touches the curve at exactly one point, sharing the same slope as the curve at that precise location <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a> <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Approximating with Secant Lines and Introducing Limits

To find the slope of this instantaneous tangent line, we use an approximation method involving **secant lines** <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

1.  **Pick a Point:** Choose a point `(a, f(a))` on the curve where you want to find the slope <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a> <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
2.  **Choose a Second Point:** Select another point `(a + h, f(a + h))` on the curve, a distance `h` away from the first point <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
3.  **Form a Secant Line:** Draw a straight line (a secant line) connecting these two points <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
4.  **Calculate Secant Slope:** The slope of this secant line is calculated using the standard slope formula (change in y / change in x):
    `[f(a + h) - f(a)] / [(a + h) - a]` which simplifies to `[f(a + h) - f(a)] / h` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a> <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
5.  **Improve Approximation:** This secant line slope is an approximation of the curve's slope at the first point <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. The closer `h` gets to zero (meaning the second point gets closer to the first point), the better the approximation becomes <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

## The [[definition_and_significance_of_the_derivative | Definition of the Derivative]] Using a [[introduction_to_limits | Limit]]

The breakthrough comes when we consider what happens as `h` approaches zero <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. If we could find the slope when `h` is exactly zero, that would be the instantaneous slope at that point on the curve <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This is where the concept of a [[understanding_the_concept_of_limits_in_calculus | limit]] becomes crucial <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

The [[definition_and_significance_of_the_derivative | definition of the derivative]] of a function `f(x)` at a point `a` is given by the [[understanding_limit_notation | limit]] of the secant line's slope as `h` approaches `0`:

> [!MATH]
> `f'(a) = lim (h -> 0) [f(a + h) - f(a)] / h` <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a> <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>

As `h` approaches `0`, the secant line's slope converges to the slope of the tangent line, providing the exact instantaneous slope of the curve at point `a` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a> <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

This definition allows us to find the slope of nearly any continuous curve at an exact point <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>, moving beyond just finding the slope of a straight line <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.