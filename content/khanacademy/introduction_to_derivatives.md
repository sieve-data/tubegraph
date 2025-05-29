---
title: Introduction to derivatives
videoId: rAof9Ld5sOg
---

From: [[khanacademy]] <br/> 

Welcome to the presentation on [[concept_of_derivatives_and_differential_calculus | derivatives]] <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Math becomes significantly more engaging with this topic compared to earlier concepts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Understanding Slope: From Straight Lines to Curves

### Slope of a Straight Line
For a straight line, finding the slope is a straightforward process <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. It is defined as the change in `y` divided by the change in `x` <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, often represented as `Δy / Δx` <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. The slope remains constant across the entire length of a straight line <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. To calculate it, one can pick any two arbitrary points on the line, determine the change in their `y` coordinates (`Δy`), and divide it by the change in their `x` coordinates (`Δx`) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### The Challenge with Curves
Unlike straight lines, the slope of a curve, such as `y = x²`, is not constant; it continuously changes <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. For instance, a curve might start nearly flat and progressively become steeper <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This means there isn't a single slope for the entire curve <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. The objective then becomes to determine the slope *at a given point* on the curve <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. The slope at a specific point on a curve is equivalent to the slope of a tangent line at that point <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. A tangent line touches the curve at exactly one point and has the same slope as the curve at that precise location <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## Introducing the Derivative

The derivative is utilized to calculate the slope at any point along a curve <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. This is where the [[introduction_to_limits | concept of limits]] becomes essential and useful <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Approximating with Secant Lines
To find the slope at a specific point `(a, f(a))` on a curve, one can initially consider a second point nearby, `(a+h, f(a+h))` <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. The line connecting these two points is called a secant line <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. The slope of this secant line provides an approximation of the curve's slope at the first point <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

The slope of the secant line is calculated using the standard slope formula <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>:
> `(f(a + h) - f(a)) / ((a + h) - a)` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>

Simplifying this, the formula for the slope of the secant line is:
> `(f(a + h) - f(a)) / h` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>

### The Role of Limits
The accuracy of this approximation improves as `h` (the horizontal distance between the two points) becomes smaller <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. The ideal scenario is when `h` equals 0, which would yield the exact, instantaneous slope at the point `a` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

To achieve this, we use the [[introduction_to_limits_in_calculus | concept of limits]] by finding what happens to the slope of the secant line as `h` approaches 0 <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. As `h` approaches 0, the secant line gradually approaches the tangent line <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

The [[concept_of_derivatives_and_differential_calculus | definition of the derivative]] is precisely this limit:
> `Limit as h approaches 0 of (f(a + h) - f(a)) / h` <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>

### What the Derivative Represents
The derivative is fundamentally the slope of a curve at an exact point <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This concept is incredibly useful because it allows us to determine the slope of virtually any continuous curve at any given point <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

Future discussions will delve into applying this [[definition_and_application_of_derivatives | definition of the derivative]] to specific functions, such as `x²`, and explore various problems <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.