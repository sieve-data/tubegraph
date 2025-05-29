---
title: Definition and application of derivatives
videoId: rAof9Ld5sOg
---

From: [[khanacademy]] <br/> 

This article explores the concept of [[introduction_to_derivatives | derivatives]], beginning with the familiar idea of the slope of a straight line and progressing to how to determine the instantaneous slope of a curve. The discussion introduces the [[definition_and_explanation_of_limits | concept of limits]] as a fundamental tool for defining the derivative.

## Slope of a Straight Line

For a straight line, the slope is consistent across its entire length <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. It is calculated as the change in y divided by the change in x <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This can be expressed as `delta y` (Δy) divided by `delta x` (Δx) <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. An example of such a line follows the standard [[definition_and_examples_of_equations | equation]] `y = mx + b` <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## The Challenge of Curves

Unlike a straight line, the slope of a curve is not constant; it changes at different points along the curve <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. For instance, the curve `y = x^2` starts almost flat but becomes progressively steeper <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Since the slope is continuously changing, there is no single slope for the entire curve <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Instantaneous Slope and Tangent Lines

To understand the slope of a curve at a specific point, we aim to find the slope of the curve *at that given point* <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. This instantaneous slope is defined as the slope of the tangent line to the curve at that point <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. A tangent line touches the curve at exactly one point, and its slope matches the curve's slope at that precise location <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

For a [[definition_of_a_function | function]] `f(x)`, if we want to find the slope at `x = a`, we can approximate it using a secant line <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. A secant line connects two points on the curve: `(a, f(a))` and a nearby point `(a + h, f(a + h))` <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

The slope of this secant line is calculated using the standard slope formula:
$$ \text{Slope}_{\text{secant}} = \frac{\text{Change in y}}{\text{Change in x}} = \frac{f(a + h) - f(a)}{(a + h) - a} = \frac{f(a + h) - f(a)}{h} $$ <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>

## The Role of Limits in Derivatives

To get the exact slope of the tangent line (the instantaneous slope), the distance `h` between the two points on the secant line must approach zero <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This is where [[definition_and_explanation_of_limits | limits]] become crucial <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

The [[using_limits_to_find_the_derivative | derivative]] is formally defined as the limit of the secant line's slope as `h` approaches 0:

> The [[concept_of_derivatives_and_differential_calculus | derivative]] is nothing more than the slope of a curve at an exact point. <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>

This definition is highly useful as it allows us to find the slope of any continuous curve at a specific point, a capability that extends beyond just straight lines <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.