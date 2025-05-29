---
title: Chain rule in differentiation
videoId: qb40J4N1fa4
---

From: [[3blue1brown]] <br/> 

The [[Chain rule for function compositions | Chain rule]] is a fundamental concept in [[Calculating derivatives and their applications | calculating derivatives]] that applies when dealing with composite functions. It is used to determine the rate of change of one variable with respect to another when there are intermediate dependencies.

## Application in Related Rates Problems

The [[Chain rule for function compositions | Chain rule]] becomes crucial in problems involving "related rates," where quantities are changing over time and are related by an equation <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

Consider a 5-meter ladder against a wall, with the top initially 4 meters above the ground and the bottom 3 meters from the wall due to the Pythagorean theorem <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. If the top of the ladder is dropping at a rate of 1 meter per second, one might want to find the rate at which the bottom of the ladder is moving away from the wall <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

To solve this, let `y(t)` be the distance from the top of the ladder to the ground and `x(t)` be the distance from the bottom of the ladder to the wall <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. The relationship between these quantities is given by the Pythagorean theorem: `x(t)^2 + y(t)^2 = 5^2` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This equation holds true at all points in time <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

One approach to finding `dx/dt` (the rate at which x is changing with respect to time) would be to isolate `x(t)` and then take the derivative <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This method, while valid, "involves a couple layers of using the [[Chain rule for function compositions | chain rule]]" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

Alternatively, one can take the derivative of both sides of the equation `x(t)^2 + y(t)^2 = 5^2` with respect to time <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   The derivative of `x(t)^2` with respect to time `t` is `2 * x(t) * (dx/dt)` <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. This step demonstrates the [[Chain rule for function compositions | chain rule]] <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>, where the derivative of the outer function (`x^2`) is multiplied by the derivative of the inner function (`x` with respect to `t`).
*   Similarly, the rate at which `y(t)^2` is changing is `2 * y(t) * (dy/dt)` <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   The derivative of the constant `5^2` (which is 25) is 0 <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

Thus, differentiating both sides yields:
`2x(t) * (dx/dt) + 2y(t) * (dy/dt) = 0` <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
This equation signifies that `x^2 + y^2` must not change as the ladder moves <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
Given `y(t) = 4` meters and `x(t) = 3` meters at the start <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>, and `dy/dt = -1` meters per second (since the height is decreasing) <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>, one can solve for `dx/dt` which comes out to `4/3` meters per second <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Connection to Implicit Differentiation

The application of the [[Chain rule for function compositions | chain rule]] in related rates problems provides an intuitive understanding of why [[Implicit differentiation | implicit differentiation]] works for curves not explicitly defined as functions of x (e.g., `x^2 + y^2 = 5^2`) <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. When taking the derivative of an expression like `y^2` with respect to `x`, it becomes `2y * dy/dx` <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. This is effectively applying the [[Chain rule for function compositions | chain rule]], treating `y` as a function of `x` (even if implicitly defined).

## Combination with Product Rule

The [[Chain rule for function compositions | chain rule]] can also be combined with other [[Understanding derivatives of combined functions | derivative rules]], such as the [[Product rule in calculus | product rule in calculus]] <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. For example, to differentiate `sin(x) * y^2 = x` using [[Implicit differentiation | implicit differentiation]], the left side requires both the [[Product rule in calculus | product rule in calculus]] and the [[Chain rule for function compositions | chain rule]] <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   The derivative of `sin(x) * y^2` would be `sin(x) * (2y * dy)` (using the [[Chain rule for function compositions | chain rule]] for `y^2`) plus `y^2 * cos(x) * dx` <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
*   The right side `x` simply becomes `dx` <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.
*   Setting these equal, one can solve for `dy/dx` <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.