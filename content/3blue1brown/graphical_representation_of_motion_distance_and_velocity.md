---
title: Graphical representation of motion distance and velocity
videoId: 9vKqVkMQHKk
---

From: [[3blue1brown]] <br/> 

The concept of a derivative, while subtle and potentially paradoxical, is fundamentally about measuring rates of change, particularly as it relates to phenomena like motion <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. A common, yet oxymoronic, phrase used to describe a derivative is "instantaneous rate of change" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Change inherently occurs between separate points in time, making the idea of change at a single instant nonsensical <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Understanding this paradox helps in appreciating the cleverness of calculus in capturing this idea with the derivative <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Modeling Car Motion

To illustrate the derivative, consider a car that starts at point A, speeds up, and then slows to a stop at point B, 100 meters away, all within 10 seconds <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Distance vs. Time Graph (`s(t)`)

The car's motion can be graphed by letting the vertical axis represent the distance traveled and the horizontal axis represent time <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The height of the graph at any time `t` indicates the total distance the car has traveled after that amount of time <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This function is typically named `s(t)` <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

On this graph:
*   Initially, when the car is slow to start, the curve is shallow, as the distance traveled during the first second doesn't change much <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   As the car speeds up, the distance traveled per second increases, which corresponds to a steeper slope in the graph <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Towards the end, when the car slows down, the curve shallows out again <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

This demonstrates a [[velocity_and_distance_relationship | relationship between velocity and distance]] via the slope of the distance-time graph.

### Velocity vs. Time Graph (`v(t)`)

The car's velocity, measured in meters per second, can also be plotted as a function of time <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This graph might look like a bump:
*   At early times, the velocity is very small <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   Up to the middle of the journey, the car builds up to a maximum velocity, covering a relatively large distance each second <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   Then, it slows back down towards a speed of zero <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

These two curves (`s(t)` and `v(t)`) are inherently related; changing one implies a different form for the other <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Understanding the specific nature of this [[derivative_and_velocity_relationship | relationship]] is key <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## The Paradox of Instantaneous Velocity

Intuitively, we understand velocity at a given moment as what a speedometer shows <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It seems logical that higher velocity corresponds to a steeper distance function, meaning more distance covered per unit time <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

However, the concept of "velocity at a single moment" poses a paradox <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. To compute velocity, one needs two separate points in time to calculate the change in distance divided by the change in time <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. Yet, the velocity function `v(t)` takes only a single value of `t` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This conflict between desiring velocity at a single point and needing two points for computation was a challenge for the founders of calculus <a class="yt="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Speedometer's Solution

A physical speedometer bypasses this paradox <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. Instead of calculating speed at a single instant, it measures the distance traveled over a very small, finite amount of time, for example, between 3 seconds and 3.01 seconds <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The speed is then computed as that tiny distance divided by that tiny time <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

Let `dt` represent a tiny change in time (e.g., 0.01 seconds) and `ds` represent the resulting tiny change in distance <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. The velocity is then `ds` divided by `dt` <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Graphically, `dt` is a small step to the right on the distance-time graph, and `ds` is the corresponding change in height <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. Thus, `ds/dt` can be seen as the rise-over-run slope between two very close points on the graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This ratio `ds/dt` can be considered a function of `t` <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

To compute the velocity function, a computer might choose a small `dt` (e.g., 0.01), then for various times `t`, calculate `(s(t + dt) - s(t)) / dt` <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This gives the velocity around each point in time <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

## The Pure Mathematical Derivative

The concept of `ds/dt`—a tiny change in `s` divided by a tiny change in `t`—is almost the derivative <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. However, in pure mathematics, the derivative is not this ratio for a specific `dt`, but rather **what that ratio approaches as `dt` approaches 0** <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Visualizing the Derivative

[[Visualization in calculus | Visualizing]] this limit is crucial:
*   For any specific `dt`, `ds/dt` is the slope of a line passing through two separate points on the graph <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   As `dt` approaches 0, these two points approach each other, and the slope of the line approaches the slope of a line that is **tangent** to the graph at the specific point `t` being examined <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

Therefore, the true derivative is the slope of a line tangent to the graph at a single point <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. It's important to note that this does not mean `dt` becomes "infinitely small" or that `dt` is set to 0; `dt` is always a finitely small, non-zero value that is *approaching* 0 <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. This is a "sneaky backdoor" way to reasonably discuss the rate of change at a single point in time, even though change in an instant makes no literal sense <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

The healthiest way to think of this slope is not as an instantaneous rate of change, but as **the best constant approximation for a rate of change around a point** <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### Notation

In calculus, when letters like `d` are used (e.g., `ds/dt`), it signifies the intention that `dt` will eventually approach 0 <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. The pure mathematical derivative is written as `ds/dt`, even though it's technically not a simple fraction, but rather the limit of that fraction as `dt` shrinks <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### Example: Deriving Velocity from `s(t) = t^3`

Consider a distance function `s(t) = t^3` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. To compute the velocity `ds/dt` at a specific time, say `t=2`:
1.  Calculate the change in distance: `s(2 + dt) - s(2)` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
2.  Since `s(t) = t^3`, this becomes `(2 + dt)^3 - 2^3` <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
3.  Expand `(2 + dt)^3`: `2^3 + 3 * 2^2 * dt + 3 * 2 * (dt)^2 + (dt)^3` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
4.  Subtract `2^3` and divide by `dt`:
    `[ (2^3 + 3 * 2^2 * dt + 3 * 2 * (dt)^2 + (dt)^3) - 2^3 ] / dt`
    `= [ 3 * 2^2 * dt + 3 * 2 * (dt)^2 + (dt)^3 ] / dt` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>
    `= 3 * 2^2 + 3 * 2 * dt + (dt)^2` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>
5.  As `dt` approaches 0, the terms containing `dt` become negligible <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
6.  The result is `3 * 2^2 = 12` <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

This means the slope of the tangent line to the graph at `t=2` is 12 <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. More generally, the derivative of `t^3` as a function of `t` is `3t^2` <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This algebraic simplification by letting `dt` approach 0 is a core reason why calculus is so powerful <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

## Readdressing the Paradox: The Car at `t=0`

Using the `s(t) = t^3` example, consider the car's motion at `t=0` <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
*   The derivative `3t^2` at `t=0` is `3 * 0^2 = 0` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   Visually, the tangent line to the graph at `t=0` is perfectly flat <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. This suggests the "instantaneous velocity" is 0, implying the car is not moving <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   However, if it doesn't start moving at `t=0`, then when does it start moving? This leads to the paradox <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

The issue lies in the question itself, as "change in a moment" doesn't exist <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The derivative being 0 means that the **best constant approximation for the car's velocity around that point is 0 m/s** <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

For instance, between `t=0` and `t=0.1` seconds, the car *does* move (0.001 m), resulting in an average speed of 0.01 m/s <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. The derivative approaching 0 means that as `dt` becomes smaller, this average speed also approaches 0 <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. This doesn't mean the car is static; approximating its movement with a constant velocity of 0 is merely an approximation <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

Thus, "instantaneous rate of change" should be understood as a conceptual shorthand for "the best constant approximation for rate of change around a point" <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. This perspective resolves the paradox and provides a robust understanding of the derivative.