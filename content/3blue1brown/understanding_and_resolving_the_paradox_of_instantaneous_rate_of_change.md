---
title: Understanding and resolving the paradox of instantaneous rate of change
videoId: 9vKqVkMQHKk
---

From: [[3blue1brown]] <br/> 

The primary goal of understanding derivatives is to explain what a derivative is <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. However, this topic involves [[Paradoxes and subtleties in understanding derivatives | subtlety]] and potential for [[Paradoxes and subtleties in understanding derivatives | paradoxes]] if not approached carefully <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. A common misconception is that the derivative measures an "instantaneous rate of change," a phrase that is fundamentally an oxymoron <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Change inherently occurs between separate points in time; focusing on a single instant leaves no room for change <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Recognizing this "nonsense" phrase helps in appreciating the ingenuity of calculus pioneers in capturing the intended idea with the mathematically sensible derivative <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## The Problem with Instantaneous Velocity

To illustrate the concept, consider a car that starts at point A, speeds up, and then slows to a stop at point B, 100 meters away, over 10 seconds <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This motion can be graphed with the vertical axis representing distance traveled (often denoted as `s(t)`) and the horizontal axis representing time <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

- The curve's slope reflects the car's speed:
    - Shallow slope at the start indicates slow initial movement <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
    - Steeper slope as the car speeds up means more distance covered per second <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
    - Shallows out again towards the end as the car slows down <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

Plotting the car's velocity (in meters per second) as a function of time would show a bump curve, starting small, building to a maximum, then decreasing to zero <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. These two curves (distance vs. time and velocity vs. time) are related, and [[Understanding the meaning and computation of derivatives | understanding the meaning and computation of derivatives]] of this relationship is key to the [[derivative and velocity relationship | derivative and velocity relationship]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

Intuitively, velocity at a given moment feels clear, like what a car's speedometer shows <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. However, velocity at a *single moment* is illogical <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. To determine speed, one needs two separate points in time to compute the change in distance divided by the change in time <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This presents a [[Paradoxes and subtleties in understanding derivatives | paradox]]: we want to associate individual points in time with velocity, but computing velocity requires comparing two points <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This conflict was a central challenge for the founders of calculus <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Resolving the Paradox: The "Tiny Change" Approach

### Real-World Approximation
In the real world, a car's speedometer "side-steps" the paradox <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. It doesn't measure speed at a single instant, but rather over a very small time interval. For example, at 3 seconds into a journey, it might measure the distance traveled between 3 seconds and 3.01 seconds <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The speed is then computed as this tiny distance (`ds`) divided by that tiny time interval (`dt`) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

Graphically, `dt` is a small step horizontally on the distance-time graph, and `ds` is the resulting vertical change in height <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. Thus, `ds/dt` can be thought of as the "rise over run" slope between two very close points on the graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This ratio `ds/dt` is considered a function of `t`, representing velocity as a function of time <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### Pure Mathematical Definition: The Limit
While physical devices use a concrete small `dt`, in pure mathematics, the derivative is what the ratio `ds/dt` *approaches* as `dt` approaches 0 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

- **Visual Understanding**: As `dt` approaches 0, the two points on the graph get closer, and the slope of the line passing through them (a secant line) approaches the slope of a line tangent to the graph at that single point `t` <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
- **Key Distinction**: The derivative is *not* what happens when `dt` is infinitely small, nor does one plug in 0 for `dt`. `dt` always remains a finitely small, non-zero value, but its limit is considered as it approaches 0 <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
- **The "Sneaky Backdoor"**: This concept of letting `dt` approach 0 provides a "sneaky backdoor" to discuss the rate of change at a single point in time, without ever needing to define instantaneous change directly <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

Therefore, the derivative is best understood not as an instantaneous rate of change, but as the **best constant approximation for a rate of change around a point** <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

## Notation and Simplification

The notation `ds/dt` in calculus implies the intention of letting `dt` approach 0 <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. It's technically not a fraction but represents the value that fraction approaches <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

### Example: Distance Function s(t) = t³
Let's consider a distance function `s(t) = t³` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. To compute the velocity (derivative `ds/dt`) at a specific time, say `t = 2`:

1.  Calculate the tiny change in distance: `s(2 + dt) - s(2)` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
2.  Divide by `dt`: `((2 + dt)³ - 2³) / dt` <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
3.  Expand `(2 + dt)³`: `2³ + 3(2)²dt + 3(2)(dt)² + (dt)³` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
4.  Simplify the numerator: `(2³ + 12dt + 6(dt)² + (dt)³) - 2³ = 12dt + 6(dt)² + (dt)³` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
5.  Divide by `dt`: `(12dt + 6(dt)² + (dt)³) / dt = 12 + 6dt + (dt)²` <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
6.  Consider what happens as `dt` approaches 0: the terms with `dt` (e.g., `6dt` and `(dt)²`) vanish, leaving `12` <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

This shows that the derivative of `t³` at `t = 2` is `12` (or more generally, `3t²`) <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. This process of considering the limit as `dt` approaches 0 greatly simplifies the problem, allowing for clean expressions despite the initial complexity <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

## The Paradox Revisited: Car's Movement at t=0

Consider the car moving according to `s(t) = t³` at `t = 0`.
- The derivative `3t²` at `t = 0` yields a velocity of `0` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Visually, the tangent line to the graph at `t = 0` is perfectly flat <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. This suggests the car is not moving.
- However, if the car is truly not moving at `t = 0`, when does it start moving? <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>

This highlights the [[Paradoxical and nonintuitive mathematical truths | paradoxical and nonintuitive mathematical truths]] of calculus <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. The issue is that the question "Is the car moving at `t = 0`?" makes no sense, as it refers to change in a moment, which doesn't exist <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The derivative doesn't measure this.

The derivative being 0 at `t = 0` means that the best constant approximation for the car's velocity *around* that point is 0 m/s <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. For example, between `t = 0` and `t = 0.1` seconds, the car *does* move (0.001 m), resulting in an average speed of 0.01 m/s <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The derivative of 0 simply means that for smaller and smaller time intervals, this ratio approaches 0 <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. It does not imply the car is static, as the constant velocity approximation is just that—an approximation <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

Therefore, when hearing "instantaneous rate of change," it's best to interpret it as a conceptual shorthand for the **best constant approximation for rate of change** <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.