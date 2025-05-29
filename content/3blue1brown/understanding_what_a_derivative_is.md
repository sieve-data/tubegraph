---
title: Understanding what a derivative is
videoId: 9vKqVkMQHKk
---

From: [[3blue1brown]] <br/> 

A derivative is a fundamental concept in calculus, with the primary goal of explaining what it represents <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This topic, however, involves subtleties and potential [[paradoxes_in_the_concept_of_derivatives | paradoxes]] that require careful consideration to avoid <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Misconception of "Instantaneous Rate of Change"

It is common to describe a derivative as measuring an "instantaneous rate of change" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, this phrase is an oxymoron <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Change inherently occurs between separate points in time <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, meaning that at a single instant, there is no room for change <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Recognizing this apparent "nonsense" highlights the cleverness of the founders of calculus in capturing the intended idea with a sensible mathematical concept: the derivative <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Illustrative Example: A Car's Motion

To understand derivatives, consider a car that starts at point A, speeds up, and then slows down to a stop at point B, 100 meters away, all within 10 seconds <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Graphing Distance Over Time
The car's motion can be graphed with time (t) on the horizontal axis and distance traveled (s(t)) on the vertical axis <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The height of the graph at any time `t` indicates the total distance the car has traveled <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

*   Initially, the curve is shallow as the car starts slowly <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   As the car speeds up, it covers more distance per second, corresponding to a steeper slope in the graph <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Towards the end, as it slows down, the curve flattens out again <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Graphing Velocity Over Time
The car's velocity (in meters per second) as a function of time might look like a bump <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Velocity is small at early times, builds to a maximum, and then decreases back to zero <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. These two curves (distance vs. time and velocity vs. time) are related <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, and understanding this relationship is key to defining the derivative <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### The Paradox of Velocity at a Single Moment
Intuitively, velocity at a given moment is what a speedometer shows <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It makes sense that velocity is higher when the distance function is steeper, indicating more distance covered per unit time <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. However, mathematically, velocity requires two separate points in time to compute: change in distance divided by change in time <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This presents a paradox: how can a function for velocity take only a single value of `t` if velocity fundamentally needs two points? <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>

## Resolving the Paradox: Tiny Changes and Limits

### Real-World Approximation
A physical speedometer side-steps the paradox by computing speed over a very small, but non-zero, amount of time <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. For example, at 3 seconds, it might measure the distance traveled between 3 seconds and 3.01 seconds <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. This is represented as `ds` (tiny change in distance) divided by `dt` (tiny change in time) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

[[visualizing_derivatives_using_graphs | Graphically]], this `ds/dt` ratio represents the rise over run slope between two very close points on the distance-time graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. By applying this to any point in time, `ds/dt` can be considered a function of `t`, representing velocity <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. For instance, to plot a velocity function, a computer might calculate `(s(t + dt) - s(t)) / dt` for a small `dt` (e.g., 0.01 seconds) across many values of `t` <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### The Pure Mathematical Derivative (The Limit)
The concept of `ds/dt` (a tiny change in function value over a tiny change in input) is *almost* what a derivative is <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. In pure mathematics, the derivative is not this ratio for a *specific* `dt`, but rather **what that ratio approaches as `dt` approaches 0** <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

[[geometric_interpretation_of_derivatives | Visually]], as `dt` approaches 0, the two points on the graph approach each other, and the slope of the line connecting them approaches the slope of a line that is **tangent** to the graph at that single point `t` <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. This means the derivative is equal to the slope of a tangent line to the graph at a single point <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. It's crucial to understand that `dt` never actually becomes zero; it just approaches zero <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

This [[derivative_definitions_and_their_relation_to_limits | limit concept]] provides a "backdoor" way to reasonably discuss the rate of change at a single point in time, even though change in an instant makes no sense <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Therefore, the derivative is best thought of as the **best constant approximation for a rate of change around a point** <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

## Calculating Derivatives: An Example
[[calculating_derivatives_and_their_applications | Calculating derivatives]] often involves algebraic manipulation. For a distance function `s(t) = t^3` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>, finding the velocity (`ds/dt`) at a specific time, say `t = 2`, involves the following steps:

1.  Set up the ratio: `(s(2 + dt) - s(2)) / dt` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
2.  Substitute the function: `((2 + dt)^3 - 2^3) / dt` <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
3.  Expand the numerator: `(2^3 + 3*2^2*dt + 3*2*dt^2 + dt^3 - 2^3) / dt` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
4.  Simplify by canceling `2^3` terms and dividing by `dt`: `(3*2^2 + 3*2*dt + dt^2)` <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
5.  Take the limit as `dt` approaches 0: The terms with `dt` vanish, leaving `3 * 2^2`, which is 12 <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

This shows that the slope of the tangent line at `t = 2` is 12 <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. More generally, the derivative of `t^3` is `3t^2` <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This simplification is why calculus becomes so useful; the process of taking the limit as `dt` approaches 0 eliminates much of the complexity <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

### Notation
In calculus, `dt` refers to a tiny change in `t` with actual size, and `ds` refers to the resulting change in `s` <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. However, the convention is that when `d` is used in `ds/dt`, it signifies the intention to see what happens as `dt` approaches 0, even though it's technically not a simple fraction <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## Readdressing the Paradox of Motion at an Instant

Consider the `s(t) = t^3` car motion at `t = 0` <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. The derivative `3t^2` at `t = 0` is `0` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Visually, the tangent line at this point is perfectly flat <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. This might suggest the car is not moving. However, if it isn't moving at `t = 0`, when does it start? This is the paradox <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

The issue is that the question "Is the car moving at time `t = 0`?" makes no sense, as it relies on the non-existent idea of change in a moment <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. The derivative being zero means that the *best constant approximation* for the car's velocity around that point is 0 meters per second <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. For example, between 0 and 0.1 seconds, the car *does* move (0.001 m), giving an average speed of 0.01 m/s <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The derivative being 0 means that for smaller and smaller time nudges, this ratio approaches 0 <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. It does not imply the car is static, only that approximating its movement with a constant velocity of 0 is the best approximation <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

Ultimately, when hearing "instantaneous rate of change," it should be understood as a conceptual shorthand for the **best constant approximation for rate of change** <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. Further exploration of derivatives involves examining their appearance in different contexts, methods of computation, and their utility in various [[applications_of_derivatives_in_realworld_phenomena | real-world applications]] <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>, often focusing on [[visualizing_derivatives_beyond_graphs | visual intuition]] <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.