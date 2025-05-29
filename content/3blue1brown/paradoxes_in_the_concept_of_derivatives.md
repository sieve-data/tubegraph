---
title: Paradoxes in the concept of derivatives
videoId: 9vKqVkMQHKk
---

From: [[3blue1brown]] <br/> 

The goal of understanding derivatives is to explain [[understanding_what_a_derivative_is | what a derivative is]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. However, this topic contains subtleties and potential for paradoxes if not approached carefully <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. A common description of the derivative is that it measures an "instantaneous rate of change" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Yet, this phrase is an oxymoron <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## The Core Paradox: Instantaneous Change

Change inherently occurs between separate points in time <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. When considering only a single instant, there isn't any room for change to happen <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Recognizing the "nonsense" of an "instantaneous rate of change" helps appreciate the ingenuity of the fathers of calculus in capturing this idea with a sensible mathematical concept: the derivative <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Illustrative Example: Car Motion

Consider a car that starts at point A, speeds up, and then slows to a stop at point B, 100 meters away, over 10 seconds <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This motion can be graphed with distance traveled on the vertical axis and time on the horizontal axis <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This distance function is often named `s(t)` <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

*   Initially, the curve is shallow as the car is slow to start <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   As the car speeds up, the slope of the graph becomes steeper, indicating more distance covered per second <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Towards the end, as it slows down, the curve shallows out again <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

The car's velocity as a function of time might look like a bump, starting small, building to a maximum, and then returning to zero <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. These two curves (distance vs. time and velocity vs. time) are related <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The challenge is to understand this relationship precisely <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Velocity at a Single Moment

Intuitively, velocity at a given moment feels clear—it's what a speedometer shows <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It seems logical that velocity is higher when the distance function is steeper (more distance per unit time) <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. However, the idea of velocity at a *single moment* is paradoxical <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. A snapshot of a car cannot tell you its speed; you need two separate points in time to compute the change in distance divided by the change in time <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This highlights the conflict: we want to associate velocity with individual points in time, but its computation requires comparing two separate points <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## Resolving the Paradox

### Real-World Approximation

A car's speedometer "side-steps" the paradox <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. It doesn't compute speed at a single instant but rather over a very small amount of time <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. For example, at 3 seconds, it might measure the distance traveled between 3 seconds and 3.01 seconds, then divide that tiny distance (`ds`) by the tiny time interval (`dt`) (e.g., 0.01 seconds) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This `ds/dt` ratio represents the slope between two very close points on the distance vs. time graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### The Pure Mathematical Derivative

The concept of `ds/dt` (a tiny change in `s` over a tiny change in `t`) is almost the definition of a derivative <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. In pure mathematics, the derivative is not this ratio for a *specific* choice of `dt`, but rather **whatever that ratio approaches as your choice for `dt` approaches 0** <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

#### Geometric Interpretation
As `dt` approaches 0, and the two points on the graph approach each other, the slope of the line passing through them approaches the slope of a line **tangent** to the graph at the single point `t` <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Therefore, the true pure math derivative is equal to the slope of a line tangent to the graph at a single point <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This is a key [[geometric_interpretation_of_derivatives | geometric interpretation of derivatives]].

It's important to note that this doesn't mean `dt` is infinitely small or that you plug in 0 for `dt`. `dt` always remains a finitely small, non-zero value that merely approaches 0 <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. This "sneaky backdoor way" allows for reasonable discussion about the rate of change at a single point in time, without needing to touch the paradox of change in an instant <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### Notation
In calculus, the notation `ds/dt` (using the letter 'd') announces the intention that eventually one will consider what happens as `dt` approaches 0 <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Though written as a fraction, it technically represents the limit of that fraction as `dt` becomes infinitesimally small <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### Example: The Derivative of `t³`

Let's say the distance function `s(t)` is exactly `t³` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. To compute the velocity `ds/dt` at a specific time, say `t=2` <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>:

1.  Calculate the change in distance: `s(2 + dt) - s(2)` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
2.  Substitute `t³`: `(2 + dt)³ - 2³` <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
3.  Expand `(2 + dt)³`: `2³ + 3(2²)dt + 3(2)(dt)² + (dt)³` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
4.  Subtract `2³`: `3(2²)dt + 3(2)(dt)² + (dt)³` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
5.  Divide by `dt`: `3(2²) + 3(2)dt + (dt)²` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
6.  As `dt` approaches 0, the terms with `dt` in them vanish, leaving `3(2²)` <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
7.  So, at `t=2`, the derivative (velocity) is `12` <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

More generally, the derivative of `t³` is `3t²` <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This example demonstrates how considering what the ratio approaches as `dt` approaches 0 simplifies the problem, making [[calculating_derivatives_and_their_applications | computing derivatives]] more tractable <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

## Re-examining the Paradox with `t³`

Consider the car traveling according to `s(t) = t³` at time `t=0` (the start) <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. Is the car moving at `t=0`? <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>

*   **Argument 1 (Derivative):** The derivative is `3t²`. At `t=0`, `3(0)² = 0`. Visually, the tangent line at `t=0` is flat, suggesting the car's instantaneous velocity is 0. This implies it's not moving <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   **Argument 2 (Intuition):** If the car doesn't start moving at `t=0`, when does it start moving? This leads to a paradox <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

### Resolution: Best Constant Approximation

The issue is that the question "Is the car moving at time t=0?" refers to "change in a moment," which doesn't exist <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The derivative doesn't measure this <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

Instead, when the derivative of a distance function is 0, it means that the **best constant approximation for the car's velocity around that point is 0 m/s** <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. For instance, between 0 and 0.1 seconds, the car *does* move (0.001 m), resulting in an average speed of 0.01 m/s <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The derivative being 0 means that for smaller and smaller time nudges, this average speed ratio approaches 0 <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. This doesn't mean the car is static, only that approximating its movement with a constant velocity of 0 is the best approximation <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

Whenever "instantaneous rate of change" is used, it should be understood as a conceptual shorthand for the **best constant approximation for a rate of change** <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.