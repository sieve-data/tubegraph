---
title: Fundamental theorem of calculus
videoId: rfG8ce4nNh0
---

From: [[3blue1brown]] <br/> 

The [[fundamental_concepts_of_calculus | Fundamental Theorem of Calculus]] establishes a crucial relationship between derivatives and integrals, positing that they are inverse operations of each other <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This concept is often best understood by ensuring it "feels reasonable, and preferably obvious, at least at an intuitive level," a sentiment echoed by mathematician Grothendieck <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Connecting Integrals to Antiderivatives: The Car Example

To illustrate this inverse relationship, consider a scenario where you are in a car and can only see the speedometer, not outside the window <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The car speeds up and slows down over 8 seconds <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The goal is to determine the total distance traveled or, more generally, to find a distance function, `s(t)`, based solely on the speedometer readings <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

Let's assume the velocity of the car over time is modeled by the function `v(t) = t * (8 - t)` in meters per second <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. In a previous discussion (chapter 2 of the [[introduction_to_calculus_series | series, introducing derivatives]]), the problem was the opposite: starting with a distance function `s(t)` to find the velocity function <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. This involved taking the [[introduction_to_derivatives_and_calculus_concepts | derivative]] of the distance function to get the velocity function <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Therefore, in the current situation, finding the distance function from a known velocity function requires finding a function whose [[introduction_to_derivatives_and_calculus_concepts | derivative]] is `t * (8 - t)` <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This process is known as finding the antiderivative <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## The Role of Area Under the Curve

Before directly computing the antiderivative, it's crucial to understand how this question relates to finding the area bounded by the velocity graph <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This connection provides intuition for a wide class of problems known as integral problems <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### Constant Velocity Simplification

If the car moved at a constant velocity, the distance traveled would simply be the velocity multiplied by the time elapsed <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. On a velocity-time graph, this product can be visualized as the area of a rectangle <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. The units naturally align: meters per second (vertical axis) times seconds (horizontal axis) yields meters (area) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

### Approximating with Rectangles

Since velocity in our example is not constant, we approximate the velocity function by treating it as constant over many small time intervals <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

1.  **Divide the Time Axis**: Chop the time axis (from 0 to 8 seconds) into small intervals, each with a width `dt` (e.g., 0.25 seconds) <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
2.  **Approximate Velocity**: For each interval, approximate the car's velocity as constant, using the true velocity at the start of that interval (e.g., `v(1) = 7 m/s` for the interval from `t=1` to `t=1.25`) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
3.  **Calculate Interval Distance**: The approximate distance traveled in such an interval is `v(t) * dt` <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This is represented by the area of a thin rectangle <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
4.  **Sum the Distances**: Sum the areas of all these rectangles. As `dt` becomes smaller, the approximation becomes more precise <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

This sum is expressed using integral notation: `∫[from 0 to 8] v(t) dt` <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. The `dt` serves two roles: it's a factor in each quantity being added, and it indicates the spacing between sampled time steps <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. As `dt` approaches 0, this sum approaches the exact area bounded by the velocity curve and the horizontal axis <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This precise answer to the total distance traveled is what an integral represents <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## The Fundamental Theorem's Core Insight

The [[visualization_in_calculus | visualization]] of distance as the area under the velocity curve is a powerful, general problem-solving tool <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

Consider the area under the velocity curve from 0 up to a variable point, `T`. This area represents the distance traveled after `T` seconds, thus forming a distance function `s(T)` <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

Now, consider the [[introduction_to_derivatives_and_calculus_concepts | derivative]] of this distance function, `ds/dt`.
On one hand, a tiny change in distance (`ds`) over a tiny change in time (`dt`) *is* velocity <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
On the other hand, in terms of the graph, a slight nudge of `dt` to the input `T` increases the area by a small sliver <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. The height of this sliver is `v(t)` (the height of the graph at that point), and its width is `dt` <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. For small `dt`, this sliver is approximately a rectangle, so `ds ≈ v(t) * dt` <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. As `dt` approaches zero, this approximation becomes exact, leading to `ds/dt = v(t)` <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

This means the [[introduction_to_derivatives_and_calculus_concepts | derivative]] of any function representing the area under a graph is equal to the function for the graph itself <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This is the essence of the [[fundamental_concepts_of_calculus | Fundamental Theorem of Calculus]].

## Calculating Antiderivatives and Definite Integrals

Given our velocity function `v(t) = t * (8 - t) = 8t - t^2` <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>:

1.  **Find the Antiderivative**: We need a function `s(t)` whose [[introduction_to_derivatives_and_calculus_concepts | derivative]] is `8t - t^2` <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
    *   For `8t`: We know the [[power_rule_in_calculus_and_its_geometric_significance | derivative]] of `t^2` is `2t` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. Scaling by 4, the [[introduction_to_derivatives_and_calculus_concepts | derivative]] of `4t^2` is `8t` <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
    *   For `-t^2`: Using the [[power_rule_in_calculus_and_its_geometric_significance | power rule]], the [[introduction_to_derivatives_and_calculus_concepts | derivative]] of `t^3` is `3t^2` <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. Scaling by `1/3` gives `t^2`, so the [[introduction_to_derivatives_and_calculus_concepts | derivative]] of `-1/3 t^3` is `-t^2` <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
    *   Combining these using the [[understanding_the_sum_rule_for_derivatives | sum rule]], an antiderivative is `S(t) = 4t^2 - (1/3)t^3` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

    However, the [[introduction_to_derivatives_and_calculus_concepts | derivative]] of a constant is zero <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. This means `S(t) = 4t^2 - (1/3)t^3 + C` (where `C` is any constant) is also an antiderivative <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

2.  **Use the Bounds to Find the Specific Antiderivative**: The specific constant `C` is determined by the lower bound of the integral. For an integral from `a` to `b` of `f(x) dx`, the value is `F(b) - F(a)`, where `F(x)` is *any* antiderivative of `f(x)` <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. The constant `C` cancels out in this subtraction <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

    *   For our car example, integrating from `0` to `8` seconds:
        `∫[from 0 to 8] (8t - t^2) dt = S(8) - S(0)` <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
        `S(8) = 4(8)^2 - (1/3)(8)^3 = 4(64) - (1/3)(512) = 256 - 170.67 = 85.33` <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
        `S(0) = 4(0)^2 - (1/3)(0)^3 = 0` <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
        Total distance = `85.33 - 0 = 85.33` meters <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

    *   For an integral from `1` to `7`:
        `∫[from 1 to 7] (8t - t^2) dt = S(7) - S(1)` <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.
        `S(7) = 4(7)^2 - (1/3)(7)^3 = 4(49) - (1/3)(343) = 196 - 114.33 = 81.67`
        `S(1) = 4(1)^2 - (1/3)(1)^3 = 4 - 0.33 = 3.67`
        Distance traveled from 1 to 7 seconds = `81.67 - 3.67 = 78` meters <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.

This profound relationship—that an integral, which considers every input on a continuum, can be computed by only looking at two endpoints of an antiderivative—is the [[fundamental_concepts_of_calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

## Negative Area (Signed Area)

Integrals measure what is called "signed area." If the function's graph dips below the horizontal axis, the corresponding area is counted as negative <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>. For velocity, this means the car is moving backward, and the "distance traveled" in that direction would subtract from the total displacement <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. This is because a negative velocity multiplied by `dt` results in a negative change in distance (`ds`) <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.