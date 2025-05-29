---
title: Calculating derivatives and algebraic simplification in calculus
videoId: 9vKqVkMQHKk
---

From: [[3blue1brown]] <br/> 

## Understanding the Derivative: Beyond "Instantaneous Change"

The primary goal of understanding [[understanding_the_meaning_and_computation_of_derivatives | derivatives]] is to explain what a [[understanding_the_meaning_and_computation_of_derivatives | derivative]] is <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This concept, however, carries subtleties and potential for paradoxes if not approached carefully <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. A common description of the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] is that it measures an "[[understanding_the_meaning_and_computation_of_derivatives | instantaneous rate of change]]" <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, this phrase is considered an oxymoron because change inherently occurs between separate points in time; at a single instant, there is no room for change <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Appreciating this apparent contradiction highlights the cleverness of the founders of [[introduction_to_derivatives_and_calculus_concepts | calculus]] in capturing this idea with a sensible mathematical concept: the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Visualizing Motion and Velocity

To illustrate, consider a car that starts at point A, speeds up, and then slows to a stop at point B, 100 meters away, over 10 seconds <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This motion can be graphed with the vertical axis representing distance traveled and the horizontal axis representing time <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The height of the graph `s(t)` (distance function) at any time `t` indicates the total distance traveled <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

*   **Shallow Slope**: Initially, the curve is shallow, indicating the car is slow to start, and the distance traveled doesn't change much <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Steeper Slope**: As the car speeds up, the distance traveled per second increases, corresponding to a steeper slope in the graph <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Shallowing Out**: Towards the end, as the car slows down, the curve shallows out again <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

If we were to plot the car's velocity (in meters per second) as a function of time, it would appear as a "bump" <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. These two curves (distance vs. time and velocity vs. time) are related, and the goal is to understand the specifics of this relationship <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### The Paradox of Velocity

Intuitively, we understand velocity at a given moment as what a car's speedometer shows <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It seems logical that velocity is higher when the distance function is steeper, meaning more distance covered per unit time <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. However, "velocity at a single moment" poses a conceptual problem <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. To compute velocity, one needs two separate points in time to compare the change in distance over the change in time <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This raises the question: how can a velocity function take a single value of `t` (a single snapshot) as input <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>? This apparent paradox was a central challenge for the founders of [[introduction_to_derivatives_and_calculus_concepts | calculus]] <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Approaching the Derivative: `ds/dt`

A car's speedometer effectively bypasses this paradox by measuring distance traveled over a *very small amount of time*, not at a single instant <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. For example, it might calculate speed between 3 seconds and 3.01 seconds <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

Let:
*   `dt` = a tiny change in time (e.g., 0.01 seconds) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>
*   `ds` = the resulting tiny change in distance <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>

The velocity at a point in time can then be approximated as `ds` divided by `dt` <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Graphically, `dt` is a small step to the right on the time axis, and `ds` is the resulting change in the height of the distance graph <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This ratio `ds/dt` can be seen as the "rise over run" slope between two very close points on the graph <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This `ds/dt` expression can be considered a function of `t`, providing velocity at any given time <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

When computing a velocity function, a computer might calculate `(s(t + dt) - s(t)) / dt` for a small `dt` (e.g., 0.01) across many `t` values <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## The Definition of the Derivative

While `ds/dt` for a concrete `dt` is an approximation, the true "pure math" [[understanding_the_meaning_and_computation_of_derivatives | derivative]] is defined as whatever that ratio *approaches* as `dt` approaches 0 <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

Visually, as `dt` approaches 0, the two points on the graph used to calculate the slope get closer and closer, and the slope of the line passing through them approaches the slope of a line that is *tangent* to the graph at the single point `t` <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Thus, the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] is equal to the slope of a line tangent to the graph at a single point <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

This concept of letting `dt` approach 0 provides a "sneaky backdoor" to reasonably discuss the rate of change at a single point in time without implying actual "change in an instant" <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. It's healthiest to think of this slope not as an [[understanding_the_meaning_and_computation_of_derivatives | instantaneous rate of change]], but as the *best constant approximation* for a rate of change around a point <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

In [[introduction_to_derivatives_and_calculus_concepts | calculus]], notation like `ds/dt` is used to announce the intention that one will eventually see what happens as `dt` approaches 0 <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## Algebraic Calculation and Simplification

Calculating what the ratio `ds/dt` approaches as `dt` approaches 0 often simplifies the computation.

Consider a distance vs. time function `s(t) = t^3` <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. To compute the velocity `ds/dt` at `t = 2`:

1.  **Form the ratio:**
    `ds/dt = (s(2 + dt) - s(2)) / dt` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>

2.  **Substitute the function:**
    `ds/dt = ((2 + dt)^3 - 2^3) / dt` <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>

3.  **Expand the numerator:**
    `(2 + dt)^3 = 2^3 + 3 * 2^2 * dt + 3 * 2 * dt^2 + dt^3` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>
    So, the numerator becomes: `(2^3 + 3 * 2^2 * dt + 3 * 2 * dt^2 + dt^3) - 2^3` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>

4.  **Simplify algebraically:**
    The `2^3` terms cancel out <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
    `= (3 * 2^2 * dt + 3 * 2 * dt^2 + dt^3) / dt` <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>

    Since every remaining term in the numerator has a `dt`, and there's a `dt` in the denominator, many terms can be canceled <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
    `= 3 * 2^2 + 3 * 2 * dt + dt^2` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>

5.  **Consider `dt` approaching 0:**
    As `dt` approaches 0, the terms `3 * 2 * dt` and `dt^2` also approach 0 <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
    This leaves: `3 * 2^2 = 12` <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

This means the slope of the line tangent to the graph of `s(t) = t^3` at `t = 2` is exactly 12 <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. More generally, the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of `t^3` as a function of `t` is `3t^2` <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

This algebraic simplification, achieved by letting `dt` approach 0, demonstrates why [[introduction_to_derivatives_and_calculus_concepts | calculus]] becomes useful: it allows us to ignore much of the "mess" of a specific `dt` and simplify the problem <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. Students often learn [[derivatives_of_simple_functions_and_their_intuition | derivative formulas]] like `3t^2` directly, without re-deriving them each time <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

## Readdressing the Paradox

Consider the `t^3` distance function and the car's motion at `t = 0` <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.
*   The [[understanding_the_meaning_and_computation_of_derivatives | derivative]] `3t^2` at `t = 0` works out to `0` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. This suggests the car's "[[understanding_the_meaning_and_computation_of_derivatives | instantaneous velocity]]" is 0, implying it's not moving <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.
*   However, if it doesn't start moving at `t = 0`, when does it start moving <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>?

This is a [[understanding_the_meaning_and_computation_of_derivatives | paradox]] because the question itself, referencing "change in a moment," is nonsensical <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. The [[understanding_the_meaning_and_computation_of_derivatives | derivative]] does not measure true "change in an instant" <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. Instead, a [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of 0 means that the *best constant approximation* for the car's velocity *around* that point is 0 m/s <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

For instance, between `t = 0` and `t = 0.1` seconds, the car *does* move (0.001 m), resulting in an average speed of 0.01 m/s <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>. What the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] being 0 at that point signifies is that for smaller and smaller nudges in time, this average speed ratio *approaches* 0 <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. This doesn't mean the car is static; approximating its movement with a constant velocity of 0 is merely an [[approximating_solutions_using_calculus | approximation]] <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

Therefore, when the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] is referred to as an "[[understanding_the_meaning_and_computation_of_derivatives | instantaneous rate of change]]", it should be understood as a conceptual shorthand for the "best constant [[approximating_solutions_using_calculus | approximation]] for rate of change" <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.