---
title: Paradoxes and subtleties in understanding derivatives
videoId: 9vKqVkMQHKk
---

From: [[3blue1brown]] <br/> 

The primary goal of understanding [[introduction_to_derivatives_and_calculus_concepts | derivatives]] is to explain what a derivative is <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. However, this topic contains subtleties and potential paradoxes if not approached carefully <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. A secondary goal is to appreciate these paradoxes and learn how to avoid them <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## The "Instantaneous Rate of Change" Oxymoron

It's common to define the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] as measuring an "instantaneous rate of change" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, this phrase is an oxymoron <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Change inherently occurs between separate points in time <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>; at a single instant, there is no room for change <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The true cleverness of the "fathers of [[introduction_to_derivatives_and_calculus_concepts | calculus]]" lies in capturing the idea this phrase is meant to evoke, but with a "perfectly sensible piece of math" <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>: the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## Modeling Motion: A Car Example

Consider a car starting at point A, speeding up, and then slowing to a stop at point B, 100 meters away, over 10 seconds <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Distance vs. Time Graph
This motion can be graphed with the vertical axis representing distance traveled (`s(t)`) and the horizontal axis representing time (`t`) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The height of the graph at any time `t` indicates the total distance traveled <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   Initially, the curve is shallow as the car is slow to start <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   As the car speeds up, the slope of the graph becomes steeper, representing more distance traveled per second <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Towards the end, as it slows down, the curve shallows out again <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Velocity vs. Time Graph
The car's velocity (in meters per second) as a function of time might look like a bump <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   Early times show small velocity <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   Velocity builds to a maximum in the middle <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   Then it slows back down to zero <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

These two curves are related <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Understanding the specifics of how velocity depends on the distance function is key <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## The Paradox of Velocity at a Single Moment

Intuitively, we understand velocity at a given moment (like a speedometer reading) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, and it seems to correspond to the steepness of the distance function <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. However, velocity at a single moment "makes no sense" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. To compute velocity, one needs two separate points in time to compare change in distance over change in time <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This presents a paradox: we want to associate individual points in time with velocity, but computing velocity requires comparing two points <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. This conflict was grappled with by the "fathers of [[introduction_to_derivatives_and_calculus_concepts | calculus]]" <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Resolving the Paradox: Real World vs. Pure Math

### Real-World Approach (Speedometer)
A physical car's speedometer "side-steps" the paradox <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. It doesn't compute speed at a single point, but over a "very small amount of time" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. For example, it might measure the distance traveled between 3 seconds and 3.01 seconds (`ds`) and divide it by that tiny time difference (`dt`) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Graphically, this `ds/dt` is the "rise over run slope between two very close points" on the distance vs. time graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Pure Math Approach (The Derivative)
The ratio `ds/dt` (tiny change in `s` divided by tiny change in `t`) is "almost what a [[understanding_the_meaning_and_computation_of_derivatives | derivative]] is" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. In pure math, the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] is *not* this ratio for a specific `dt` <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. Instead, it's "whatever that ratio approaches as your choice for `dt` approaches 0" <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

#### Geometric Interpretation
As `dt` approaches 0, the two points used for the slope calculation approach each other <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. The slope of the line connecting these two points then approaches the "slope of a line that's tangent to the graph at whatever point `t` we're looking at" <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Thus, the "true honest-to-goodness pure math [[understanding_the_meaning_and_computation_of_derivatives | derivative]]" is equal to the slope of a line tangent to the graph at a single point <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

It's crucial to understand that this does not mean `dt` is "infinitely small" or that you "plug in 0 for `dt`" <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. `dt` is always a "finitely small non-zero value" that *approaches* 0 <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This approach is a "really sneaky backdoor way to talk reasonably about the rate of change at a single point in time" <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

#### Best Constant Approximation
Because "change in an instant still makes no sense," it's healthier to think of this slope not as an "instantaneous rate of change," but as "the best constant approximation for a rate of change around a point" <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### Notation
In [[introduction_to_derivatives_and_calculus_concepts | calculus]], the notation `d` (e.g., `dt`, `ds`) signifies the intention that `dt` will eventually approach 0 <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. The pure math [[understanding_the_meaning_and_computation_of_derivatives | derivative]] is written as `ds/dt`, even though it's technically not a simple fraction, but rather "whatever that fraction approaches for smaller and smaller nudges in t" <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Example: Derivative of t³ (s(t) = t³)

Let's compute the velocity, `ds/dt`, for the distance function `s(t) = t³` at `t = 2` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
The ratio `ds/dt` is calculated as `(s(t + dt) - s(t)) / dt` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
For `t=2` and `s(t) = t³`, this becomes:
`( (2 + dt)³ - 2³ ) / dt` <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>

Expanding `(2 + dt)³`:
`2³ + 3 * 2² * dt + 3 * 2 * dt² + dt³` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>

So the expression is:
`( 2³ + 3 * 2² * dt + 3 * 2 * dt² + dt³ - 2³ ) / dt` <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>

The `2³` terms cancel out <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. Everything remaining has a `dt` term, allowing cancellation with the `dt` in the denominator <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
Resulting expression:
`3 * 2² + 3 * 2 * dt + dt²` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>

Now, consider what happens as `dt` approaches 0 <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. The terms with `dt` in them (`3 * 2 * dt` and `dt²`) will also approach 0, so they can be ignored <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
What's left is `3 * 2² = 12` <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
This means the slope of the tangent line to the graph at `t = 2` is `12` <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

More generally, the [[derivatives_of_simple_functions_and_their_intuition | derivative]] of `t³` as a function of `t` is `3t²` <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This algebraic simplification, where considering `dt` approaching 0 eliminates much of the complexity, is "the heart of why [[introduction_to_derivatives_and_calculus_concepts | calculus]] becomes useful" <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

## The Paradox of Initial Motion (t=0)

Consider the car traveling according to `s(t) = t³` at `t = 0` <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
*   Using the [[derivatives_of_simple_functions_and_their_intuition | derivative]] `3t²`, at `t = 0`, the velocity is `3 * 0² = 0` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   Visually, the tangent line to the graph at `t = 0` is perfectly flat <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>, suggesting the car is not moving.
*   Paradoxically, if it doesn't start moving at time 0, when *does* it start moving? <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>

### Resolution
The question "Is the car moving at time `t = 0`?" makes no sense, as it references "change in a moment," which doesn't exist <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. The [[understanding_the_meaning_and_computation_of_derivatives | derivative]] does not measure instantaneous change <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

Instead, when the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of a distance function is 0, it means "the best constant approximation for the car's velocity around that point is 0 m per second" <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. The car *does* move over a small interval, e.g., between 0 and 0.1 seconds, traveling 0.001 m <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. This yields an average speed of 0.01 m/s <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>. The [[understanding_the_meaning_and_computation_of_derivatives | derivative]] being 0 means that for "smaller and smaller nudges in time, this ratio of m per second approaches 0" <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. This doesn't mean the car is static; approximating its movement with a constant velocity of 0 is "just an approximation" <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

Therefore, "instantaneous rate of change" should be understood as a "conceptual shorthand for the best constant approximation for rate of change" <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.