---
title: Relationship between velocity and distance functions
videoId: 9vKqVkMQHKk
---

From: [[3blue1brown]] <br/> 

The primary goal of understanding the [[relationship_between_integrals_and_derivatives | derivative]] is to explain its nature <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This topic contains subtleties and potential paradoxes that require careful consideration <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

It is commonly stated that the derivative measures an instantaneous rate of change <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, this phrase is an oxymoron, as change occurs between separate points in time, and focusing on a single instant leaves no room for change <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The cleverness of calculus lies in capturing the essence of this idea with a sensible mathematical concept: the derivative <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## Car Motion: An Illustrative Example

Consider a car that starts at point A, speeds up, and then slows to a stop at point B, 100 meters away, over 10 seconds <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Distance vs. Time Graph
The car's motion can be graphed with the vertical axis representing distance traveled and the horizontal axis representing time <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. At any time 't', the graph's height indicates the total distance traveled by the car <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This distance function is typically named `s(t)` <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

*   Initially, the curve is shallow because the car is slow to start, meaning the distance traveled in the first second doesn't change much <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   As the car speeds up, the distance covered per second increases, resulting in a steeper slope on the graph <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Towards the end, as the car slows down, the curve shallows out again <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Velocity vs. Time Graph
If the car's velocity (in meters per second) is plotted as a function of time, it might appear as a "bump" curve <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Velocity is small at early times, builds to a maximum in the middle of the journey, and then decreases back to zero <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

These two curves, distance vs. time and velocity vs. time, are inherently related <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The core question in calculus is understanding the specific nature of this relationship: how does velocity depend on a distance vs. time function <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>?

## The Paradox of "Instantaneous Velocity"

Intuitively, velocity at a given moment is what a speedometer shows <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It makes sense that velocity is higher when the distance function is steeper, indicating more distance covered per unit time <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

However, the concept of velocity at a single moment is paradoxical <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. To compute velocity, one needs two separate points in time to compare the change in distance across those times, divided by the change in time <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. Velocity is defined as distance traveled per unit time <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This leads to a conflict: we want to associate individual points in time with a velocity, but calculation requires two points <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## Approximating Velocity with Tiny Changes

A car's speedometer side-steps this paradox by not computing speed at a single point, but rather over a very small amount of time <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. For example, at 3 seconds into a journey, the speedometer might measure the distance traveled between 3 seconds and 3.01 seconds <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The speed is then computed as that tiny distance divided by the tiny time (0.01 seconds) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

*   Let `dt` represent a tiny change in time (e.g., 0.01 seconds) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   Let `ds` represent the resulting tiny change in distance <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   Velocity at a point in time is `ds` divided by `dt` <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

Graphically, `dt` is a small step to the right on the distance vs. time graph, and `ds` is the resulting change in the height of the graph <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. Thus, `ds/dt` can be understood as the "rise over run" slope between two very close points on the graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This ratio `ds/dt` is considered a function of 't' <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

## The Pure Mathematical Derivative: The Limit

The ratio `ds/dt` (tiny change in function value divided by tiny change in input) is almost what a derivative is <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. In pure mathematics, the derivative is not this ratio for a specific `dt`, but rather **what that ratio approaches as your choice for `dt` approaches 0** <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

Visually, as `dt` approaches 0, and the two points on the graph approach each other, the slope of the line passing through them approaches the slope of a line that is **tangent to the graph at the single point** `t` <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Therefore, the true pure math derivative is the slope of a line tangent to the graph at a single point <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

It is crucial to understand that the derivative is not defined by plugging in `dt = 0`, nor by `dt` being "infinitely small" <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. `dt` is always a finitely small, non-zero value that simply *approaches* 0 <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This concept provides a "sneaky backdoor" to discuss rates of change at a single point in time, even though change in an instant makes no sense <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

The slope of the tangent line is best thought of not as an "instantaneous rate of change," but as **the best constant approximation for a rate of change around a point** <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### Notation
In calculus, the letter `d` in expressions like `ds/dt` signifies the intention that `dt` will eventually approach 0 <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. The pure math derivative is written as `ds/dt`, even though it's not a simple fraction, but rather the limit of that fraction as `dt` becomes smaller and smaller <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Deriving the Velocity Function: Example with `s(t) = t^3`

Consider a distance function `s(t) = t^3` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. To compute the velocity `ds/dt` at a specific time, like `t=2` <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>:

The tiny change in distance between `t=2` and `t=2+dt` is `s(2+dt) - s(2)`, which is then divided by `dt` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

`ds/dt = ( (2+dt)^3 - 2^3 ) / dt` <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>

Expanding `(2+dt)^3` yields `2^3 + 3*(2^2)*dt + 3*2*(dt^2) + dt^3` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
So, the numerator becomes `2^3 + 3*(2^2)*dt + 3*2*(dt^2) + dt^3 - 2^3` <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

The `2^3` terms cancel out <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. All remaining terms in the numerator have a `dt`, allowing cancellation with the `dt` in the denominator <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

This simplifies the ratio `ds/dt` to `3*(2^2) + 3*2*dt + dt^2` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

As `dt` approaches 0, the terms `3*2*dt` and `dt^2` approach 0 <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
Thus, the derivative at `t=2` is `3 * 2^2 = 12` <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

More generally, the derivative of `t^3` with respect to `t` is `3t^2` <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This simplification, achieved by considering the limit as `dt` approaches 0, highlights the power of calculus in simplifying complex problems <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

## Readdressing the Paradox with the Derivative

Using the `s(t) = t^3` example, consider the car's motion at `t=0` <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. The derivative `3t^2` at `t=0` yields `3*(0^2) = 0` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. This means the tangent line to the graph at `t=0` is flat, suggesting the car's instantaneous velocity is 0, implying it's not moving <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

However, if it's not moving at `t=0`, when does it start moving <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>? This question itself is paradoxical because it references "change in a moment," which doesn't exist <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The derivative does not measure actual change in an instant <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

Instead, when the derivative of a distance function is 0, it means that the **best constant approximation for the car's velocity around that point is 0 m/s** <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. For instance, between `t=0` and `t=0.1` seconds, the car *does* move (0.001 meters), resulting in an average speed of 0.01 m/s <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The derivative being 0 means that as `dt` gets smaller, this average speed approaches 0 <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. This is an approximation; it does not mean the car is static <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

Therefore, "instantaneous rate of change" should be understood as a conceptual shorthand for **the best constant approximation for rate of change** <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.