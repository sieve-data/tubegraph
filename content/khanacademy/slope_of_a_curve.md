---
title: Slope of a Curve
videoId: rAof9Ld5sOg
---

From: [[khanacademy]] <br/> 

The concept of a derivative is introduced when discussing the [[Slope of a Curve | slope of a curve]], moving beyond the simpler case of a straight line <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Slope of a Straight Line
For a [[Slope of a Straight Line | straight line]], the [[Slope of a line in algebra | slope]] is constant across the entire line <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. To [[finding the slope of a line | find the slope]], one selects any two points on the line <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The [[Understanding the concept of slope | slope]] is calculated as the [[understanding slope as change in y over change in x | change in y (Δy)]] divided by the [[understanding slope as change in y over change in x | change in x (Δx)]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This is expressed as Δy / Δx <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Straight lines typically follow the [[Slopeintercept form of a linear equation | standard y = mx + b form]] <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Slope of a Curve
Unlike a straight line, the [[Slope of a curve using tangent lines | slope of a curve]] (e.g., y = x²) is not constant; it changes at different points <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. For instance, a curve might be almost flat in one section and then become progressively steeper <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Therefore, there is no single slope for the entire curve <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

To understand the [[interpreting slope from a graph | slope of a curve]], one must consider the slope at a *given point* on that curve <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Tangent Lines
The [[Slope of a curve using tangent lines | slope of a curve at a given point]] is defined as the slope of the *tangent line* at that specific point <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. A tangent line touches the curve at exactly one point, and at that exact point, the curve and the tangent line share the same slope <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>, <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

### Approximating with Secant Lines
To find the slope of the tangent line, one can use [[Secant lines and their slopes | secant lines]] as an approximation <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. A secant line connects two points on the curve <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

Consider a point `a` on the curve, with coordinates `(a, f(a))` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
A second point `(a + h, f(a + h))` is chosen, where `h` represents a small distance from `a` along the x-axis <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>, <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

The slope of the [[Secant lines and their slopes | secant line]] connecting these two points is calculated using the standard [[Slope of a line in algebra | slope formula]]:
Slope = (Change in y) / (Change in x) <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>
Slope = `(f(a + h) - f(a)) / ((a + h) - a)` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>, <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>
Slope = `(f(a + h) - f(a)) / h` <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>, <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>

This formula provides an approximation of the tangent slope <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. The closer `h` gets to 0, the closer the secant line's slope approximates the instantaneous slope of the curve at point `a` <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>, <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

### The Derivative: Using Limits
To find the exact slope of the tangent line, and thus the exact slope of the curve at that point, a limit is applied to the secant line slope formula <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>, <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. The derivative is defined as:

`Limit as h approaches 0 of (f(a + h) - f(a)) / h` <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>, <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>

As `h` approaches 0, the secant line's slope becomes the slope of the tangent line, which represents the instantaneous slope of the curve at that specific point <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>, <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. This is the fundamental definition of the derivative <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>, <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

Derivatives allow for calculating the slope of nearly any continuous curve at any given point <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.