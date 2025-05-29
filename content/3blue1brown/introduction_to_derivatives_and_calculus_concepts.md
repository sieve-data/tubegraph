---
title: Introduction to derivatives and calculus concepts
videoId: 9vKqVkMQHKk
---

From: [[3blue1brown]] <br/> 

The primary goal of understanding derivatives is to explain what a derivative is <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This topic has subtlety and potential for paradoxes if not approached carefully <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. A secondary goal is to appreciate these paradoxes and learn how to avoid them <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## The Paradox of "Instantaneous Rate of Change"

It's common to define the derivative as measuring an "instantaneous rate of change" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, this phrase is an oxymoron <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Change inherently occurs between separate points in time <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>; at a single instant, there is no room for change <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Recognizing this "nonsense" aspect highlights the cleverness of the fathers of [[fundamental_concepts_of_calculus | calculus]] in capturing the intended idea with a sensible mathematical concept: the derivative <a class="yt-timestamp" data-t="00:00:51">[00:01:02]</a>.

## Modeling Motion: A Car Example

Consider a car that starts at point A, speeds up, and then slows to a stop at point B, 100 meters away, over 10 seconds <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Graphing Distance vs. Time

This motion can be graphed with the vertical axis representing distance traveled and the horizontal axis representing time <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. At any time *t*, the height of the graph `s(t)` (often named for distance) indicates the total distance traveled <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

*   **Initial Phase**: The curve is shallow as the car starts slow <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Speeding Up**: As the car speeds up, the distance traveled per second increases, corresponding to a steeper slope <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Slowing Down**: Towards the end, the curve shallows out again as the car slows <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Graphing Velocity vs. Time

The car's velocity (in meters per second) as a function of time might look like a bump <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Velocity is small initially, builds to a maximum, and then returns to zero <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. These two curves (distance and velocity) are related <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, and understanding this relationship is key to defining the derivative <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Understanding Velocity and its Paradox

Intuitively, velocity at a given moment is what a speedometer shows <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It should be higher when the distance function is steeper, indicating more distance traversed per unit time <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

However, "velocity at a single moment" makes no sense <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. To determine speed, one needs two separate points in time to compare a change in distance over a change in time <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This presents a paradox: how can a function for velocity take a single value of *t* if computing velocity requires two points <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>? This conflict is what the fathers of [[fundamental_concepts_of_calculus | calculus]] grappled with <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Resolving the Paradox: Tiny Changes and Limits

### Real-World Approximation (ds/dt)

A physical speedometer resolves the paradox by measuring distance over a very small, but finite, amount of time <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. For example, it computes speed between 3 seconds and 3.01 seconds <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

*   Let `dt` be a tiny change in time (e.g., 0.01 seconds) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   Let `ds` be the resulting tiny change in distance <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   Velocity is approximated by `ds / dt`, the tiny change in distance over the tiny change in time <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   Graphically, `ds / dt` represents the rise over run slope between two very close points on the distance vs. time graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This ratio `ds/dt` can be considered a function of *t*, giving velocity at any given time <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### The Pure Math Derivative: Approaching Zero

The concept of `ds / dt` – a tiny change in the function's value divided by the tiny change in input – is almost what a derivative is <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

Instead of looking at a specific, concrete change in time (like 0.01 seconds), the pure math derivative considers **whatever that ratio approaches as your choice for dt approaches 0** <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. This is where [[introduction_to_limits_in_calculus | limits]] come into play.

*   **Visual Intuition**: For any specific `dt`, `ds / dt` is the slope of a line passing through two separate points on the graph <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. As `dt` approaches 0, these two points approach each other, and the slope of the line approaches the slope of a line **tangent** to the graph at that single point *t* <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   The true derivative is not the slope between two nearby points, but the slope of a line tangent to the graph at a single point <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   It's important to note that this doesn't mean `dt` is infinitely small or that you plug in 0 for `dt` <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. `dt` is always a finitely small non-zero value that simply *approaches* 0 <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

This concept provides a "sneaky backdoor" to talk reasonably about the rate of change at a single point in time, without invoking the paradoxical notion of change in an instant <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. The derivative is best thought of as the **best constant approximation for a rate of change around a point** <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### Notation

In [[introduction_to_calculus_series | calculus]], `dt` and `ds` refer to tiny changes with actual size <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. However, when using the letter `d` in `ds/dt`, it signifies the intention that one will eventually consider what happens as `dt` approaches 0 <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. The true pure math derivative is written as `ds / dt`, even though it's technically not a fraction but rather what that fraction approaches for smaller and smaller nudges in *t* <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Calculating a Derivative: s(t) = t^3

Let's consider a distance function `s(t) = t^3` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. To compute the velocity `ds/dt` at a specific time, say *t* = 2:

1.  **Define the ratio**: The change in distance between `2` and `2 + dt` is `s(2 + dt) - s(2)`, divided by `dt` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
2.  **Substitute the function**: `((2 + dt)^3 - 2^3) / dt` <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
3.  **Expand algebraically**:
    `(8 + 3 * 4 * dt + 3 * 2 * dt^2 + dt^3 - 8) / dt` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>
    `(12dt + 6dt^2 + dt^3) / dt` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>
4.  **Simplify**: Divide all terms by `dt` <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
    `12 + 6dt + dt^2` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>
5.  **Apply the limit**: As `dt` approaches 0, the terms `6dt` and `dt^2` also approach 0 and can be ignored <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
    The result is `12` <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

This means the slope of the line tangent to the graph at `t = 2` is 12 <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. More generally, the derivative of `t^3` as a function of *t* is `3t^2` <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

While this algebraic process might seem complicated, it significantly simplifies the problem by allowing us to ignore many terms when considering the limit as `dt` approaches 0 <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. In practice, students learn to compute [[derivatives_of_simple_functions_and_their_intuition | derivatives of simple functions]] directly without re-deriving them each time <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

## The Paradox Revisited: Car Motion at t=0

Consider the `t^3` distance function for the car at `t = 0` (the start of the journey) <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

*   The derivative `3t^2` at `t = 0` gives a velocity of `0` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   This suggests the tangent line is flat, and the "instantaneous velocity" is 0, implying the car isn't moving <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
*   However, if it's not moving at `t=0`, when does it start moving <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>? This highlights the paradox <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.

The issue is that the question "Is the car moving at `t=0`?" makes no sense, as change in a moment doesn't exist <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The derivative being 0 means that the **best constant approximation** for the car's velocity *around* that point is 0 m/s <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

For example, between 0 and 0.1 seconds, the car *does* move (0.001 m), resulting in an average speed of 0.01 m/s <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. The derivative approaching 0 means that for smaller and smaller time nudges, this ratio of m/s approaches 0, but it doesn't mean the car is static <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. The constant velocity approximation is just that: an approximation <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

Therefore, "instantaneous rate of change" should be understood as a conceptual shorthand for the "best constant approximation for rate of change" <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. Further videos will explore [[understanding_the_meaning_and_computation_of_derivatives | the derivative]] in different contexts, how to compute it, and its utility <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.