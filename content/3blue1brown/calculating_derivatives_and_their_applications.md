---
title: Calculating derivatives and their applications
videoId: 9vKqVkMQHKk
---

From: [[3blue1brown]] <br/> 

The primary goal of understanding derivatives is to explain [[understanding_what_a_derivative_is | what a derivative is]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This topic has subtleties and potential paradoxes if not approached carefully <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## The Paradox of Instantaneous Rate of Change

It's common to define the derivative as measuring an "instantaneous rate of change" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, this phrase is actually an oxymoron <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>, <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Change inherently occurs between separate points in time <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, and at a single instant, there is no room for change <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The cleverness of the founders of calculus lies in capturing this idea with a perfectly sensible mathematical concept: the derivative <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Illustrative Example: A Car's Motion

Consider a car that starts at point A, speeds up, and then slows to a stop at point B, 100 meters away, over the course of 10 seconds <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

This motion can be [[visualizing_derivatives_using_graphs | graphed]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:
*   The vertical axis represents the distance traveled <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   The horizontal axis represents time <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   At any time `t`, the height of the graph `s(t)` (a common notation for distance) indicates the total distance traveled <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

Characteristics of the distance-time graph `s(t)`:
*   Initially, the curve is shallow as the car is slow to start, meaning little distance is covered in the first second <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   As the car speeds up, the distance traveled per second increases, corresponding to a steeper slope on the graph <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Towards the end, as the car slows down, the curve shallows out again <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

The car's velocity (in meters per second) as a function of time can be plotted as a "bump" curve <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:
*   Velocity is very small at early times <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   It builds to a maximum velocity in the middle of the journey <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   It then slows back down to zero <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

These two curves (distance vs. time and velocity vs. time) are inherently related <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The core problem in [[understanding_what_a_derivative_is | understanding what a derivative is]] is to grasp the specific nature of this relationship <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Defining Velocity and Rates of Change

Intuitively, velocity at a given moment is what a speedometer shows <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It makes sense that velocity is higher when the distance function is steeper, indicating more distance covered per unit time <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

However, "velocity at a single moment" poses a conceptual problem <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. To calculate velocity, one needs two separate points in time to compare a change in distance with a change in time <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>, <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. Yet, a velocity function takes a single value of `t` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This apparent paradox was a central conflict for the pioneers of calculus <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### The Real-World Approach to Velocity

In reality, a car's speedometer side-steps this paradox <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. It measures how far the car travels in a very small amount of time (e.g., between 3 seconds and 3.01 seconds) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. It then computes speed as that tiny distance (`ds`) divided by that tiny time (`dt`) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. So, a physical car computes speed over a very small duration, not at a single point <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

Graphically, `dt` is a small step to the right on the time axis, and `ds` is the resulting change in the graph's height (distance) <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. The ratio `ds/dt` is the "rise over run" slope between two very close points on the graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This ratio `ds/dt` can be considered a function of `t`, providing velocity at any given time <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

For instance, to draw a velocity curve, a computer calculates `(s(t + dt) - s(t)) / dt` for many `t` values, using a small `dt` like 0.01 seconds <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This formula allows computing velocity from any distance function `s(t)` <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Calculating Derivatives: The Limit Process

The ratio `ds/dt` (tiny change in function value over tiny change in input) is *almost* [[computing_derivatives_of_functions | what a derivative is]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. In pure mathematics, the derivative is not this ratio for a specific `dt`, but rather **what that ratio approaches as your choice for `dt` approaches 0** <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

Visually, `ds/dt` is the slope of a line passing through two separate points on the graph <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. As `dt` approaches 0, these two points approach each other, and the slope of the line approaches the slope of a line **tangent** to the graph at the single point `t` being considered <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

Therefore, the pure mathematical derivative is equal to the slope of a line tangent to the graph at a single point <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. It is crucial to understand that this does *not* mean plugging in 0 for `dt`, nor does it imply `dt` is infinitely small <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. `dt` is always a finitely small, non-zero value that simply *approaches* 0 <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

This concept of letting `dt` approach 0 provides a way to reasonably discuss the rate of change at a single point in time, even though change in an instant makes no sense <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. It is best to think of this slope not as an instantaneous rate of change, but as the **best constant approximation for a rate of change around a point** <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### Notation

In calculus, `dt` refers to a tiny change in `t` with actual size, and `ds` refers to the resulting change in `s` <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. The notation `ds/dt` for the pure math derivative indicates the intention that `dt` is approaching 0, even if it's not strictly a fraction <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

### Algebraic Example: Derivative of t cubed

Let's find the velocity (ds/dt) for a distance function `s(t) = t^3` at `t=2` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>:

1.  **Set up the ratio:** `(s(2 + dt) - s(2)) / dt` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>
2.  **Substitute `s(t) = t^3`:** `((2 + dt)^3 - 2^3) / dt` <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>
3.  **Expand the numerator:** `(2^3 + 3*2^2*dt + 3*2*dt^2 + dt^3 - 2^3) / dt` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>
4.  **Simplify:** The `2^3` terms cancel out. Every remaining term in the numerator has a `dt`, which can be cancelled with the `dt` in the denominator <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
    *   `3*2^2 + 3*2*dt + dt^2` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>
5.  **Apply the limit as `dt` approaches 0:** The terms with `dt` in them (`3*2*dt` and `dt^2`) vanish as `dt` approaches 0 <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
6.  **Result:** `3*2^2 = 12` <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

This means the slope of the line tangent to the graph `s(t) = t^3` at `t=2` is 12 <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

More generally, the derivative of `t^3` as a function of `t` is `3t^2` <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This algebraic process shows that while starting with a "messy" ratio, letting `dt` approach 0 simplifies the problem significantly <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>, revealing the elegant result <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. This simplification is key to why [[applications_of_derivatives_in_realworld_phenomena | calculus becomes useful]] <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

## [[applications_of_derivatives_in_realworld_phenomena | Applications of Derivatives]]: Avoiding Paradoxes

Consider the `t^3` distance function for the car at `t=0` (the start of the journey) <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
*   [[computing_derivatives_of_functions | Computing the derivative]] (velocity) at `t=0` using `3t^2` gives `3*(0)^2 = 0` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   Visually, the tangent line to the graph at `t=0` is perfectly flat, suggesting the car's instantaneous velocity is 0, implying it's not moving <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
*   However, if it doesn't start moving at `t=0`, when does it start moving? This is the paradox <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

The issue is that the question "Is the car moving at `t=0`?" makes no sense because it references the idea of change in a single moment, which doesn't exist <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The derivative does not measure instantaneous change in that literal sense <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

What it means for the derivative of a distance function to be 0 is that the **best constant approximation for the car's velocity around that point is 0 m/s** <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. For example, between `t=0` and `t=0.1` seconds, the car *does* move (0.001 m), resulting in an average speed of 0.01 m/s <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The derivative being 0 means that for smaller and smaller time nudges, this average speed ratio approaches 0 <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. This doesn't mean the car is static; approximating its movement with a constant velocity of 0 is just an approximation <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

Therefore, when hearing the phrase "instantaneous rate of change," it should be understood as a conceptual shorthand for the **best constant approximation for rate of change** <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. Further exploration into [[visualizing_derivatives_using_graphs | visualizing derivatives using graphs]] and other contexts will continue to build on this fundamental understanding <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.