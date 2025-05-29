---
title: Visualizing integration and approximations
videoId: rfG8ce4nNh0
---

From: [[3blue1brown]] <br/> 

## Introduction to Integrals and Derivatives
Mathematics often benefits from intuition before formal proof <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Integrals, a fundamental concept in calculus, can be intuitively understood as the inverse of [[integrals_and_derivatives | derivatives]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This relationship can be effectively [[visualizing_mathematical_concepts | visualized]] through practical examples <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## The Car Analogy: From Velocity to Distance
Imagine being in a car with only a speedometer visible <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The car speeds up and slows down over 8 seconds <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The challenge is to determine the total distance traveled or find a distance function `s(t)` based solely on the velocity readings <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

If the velocity `v(t)` is modeled by `t * (8 - t)` meters per second <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, the problem becomes: what function `s(t)` has `v(t)` as its [[visualizing_derivatives using graphs | derivative]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>? This is known as finding the antiderivative <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Connecting to Area Under the Curve
The problem of finding distance from a velocity graph is deeply related to finding the area bounded by the velocity graph and the horizontal axis <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

#### Constant Velocity: The Simple Case
If the car moved at a constant velocity, distance would simply be velocity multiplied by time <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. This product can be [[integration_as_finding_the_area_under_a_curve | visualized as the area]] of a rectangle on a velocity-time plot, where the horizontal axis is time (seconds) and the vertical axis is velocity (meters per second), resulting in area units of meters <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

#### Approximating Changing Velocity
Since velocity is constantly changing <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, the problem is more complex. However, it can be approximated by treating the velocity as constant over many small time intervals <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

The strategy involves:
1.  **Chopping the time axis**: Divide the total time (e.g., 0 to 8 seconds) into many small intervals, each with a tiny width `dt` (e.g., 0.25 seconds) <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
2.  **Approximating velocity**: For each interval, approximate the car's velocity as constant, often by using the true velocity at the start of the interval (the height of the graph above the left side) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
3.  **Calculating distance for each interval**: Multiply the approximated constant velocity `v(t)` by the time interval `dt` to get the distance traveled in that small interval <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This distance is visualized as the area of a thin rectangle <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
4.  **Summing the distances**: Add up the distances from all these small intervals <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Refining the Approximation: The Integral
This process represents a [[concept_of_sample_approximation_in_integration | sample approximation]] <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. As `dt` gets smaller and smaller, two things happen:
*   The area of each individual rectangle decreases <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   The total number of rectangles whose areas are being summed increases <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

The sum of these increasingly numerous, thinner rectangles approaches the precise answer to the original question <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This limiting value is exactly the [[integration_as_finding_the_area_under_a_curve | area bounded by the curve and the horizontal axis]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Integral Notation
This limiting sum is expressed using integral notation:
∫_0^8 `v(t) dt` <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>

Here, the stretched 'S' symbol indicates a sum <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>, with the lower bound (0) and upper bound (8) indicating the range over which the sum is taken <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. `dt` signifies both a factor in the quantity being added and the spacing between sampled time steps <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This expression is not just any particular sum, but what the sum approaches as `dt` approaches 0 <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. This value is called an integral <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

## The General Power of Integrals
While reframing finding distance as finding area might seem to just replace one hard problem with another <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>, the concept of [[integration_as_finding_the_area_under_a_curve | finding the area under a function's graph]] is a common language for many diverse problems in mathematics and science <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. It applies to any problem that can be broken down and approximated as the sum of a large number of small things <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

## The Fundamental Theorem of Calculus: Connecting Integrals and Derivatives
Consider the integral of a velocity function from 0 to a variable upper bound, `T` <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. This integral represents the distance `s(T)` traveled after `T` seconds <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

What is the derivative of this area function `s(T)`? A tiny change in distance `ds` over a tiny change in time `dt` is, by definition, velocity <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. In terms of the graph, a slight nudge of `dt` to the input causes the area to increase by a small sliver, `ds` <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. The height of this sliver is `v(t)` and its width is `dt`, so `ds ≈ v(t) * dt` <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. As `dt` approaches 0, this approximation becomes exact, meaning `ds/dt = v(t)` <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

This implies a fundamental insight: the [[visualizing_derivatives beyond graphs | derivative]] of any function representing the area under a graph is equal to the function for the graph itself <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. This is the essence of the [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>, which establishes that [[integrals and derivatives | integrals are the inverse of derivatives]].

## Evaluating Integrals with Antiderivatives
To find the distance function `s(t)` for `v(t) = 8t - t^2` <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>, one needs to find a function whose derivative is `8t - t^2`. This process is called finding the antiderivative.
*   The antiderivative of `8t` is `4t^2` <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   The antiderivative of `-t^2` is `-1/3 t^3` <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
So, a general antiderivative is `s(t) = 4t^2 - 1/3 t^3 + C`, where `C` is any constant <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. The derivative of a constant is zero, so `C` does not affect the slope of the function <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

To find the specific distance traveled over an interval (a definite integral), the constant `C` is determined by the integral's lower bound <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. The integral from a lower bound to itself must be zero <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

According to the [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>:
> To evaluate an integral of a function `f(x)` from `a` to `b`, find an antiderivative `F(x)` of `f(x)`. The integral is then `F(b) - F(a)` <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

For example, the total distance traveled during the full 8 seconds (from 0 to 8) for `v(t) = 8t - t^2` is calculated by evaluating the antiderivative `4t^2 - 1/3 t^3` at `t=8` and subtracting its value at `t=0` <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. Since `4(0)^2 - 1/3 (0)^3 = 0`, the total distance is `4(8)^2 - 1/3 (8)^3 = 85.33` meters <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

### The Mystery of the Fundamental Theorem
The "crazy" aspect of the [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] is that an integral, which takes into account every single input on a continuum (the sum of infinite tiny things), can be computed by looking only at two specific inputs: the top and bottom bounds <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. Finding the antiderivative implicitly accounts for all the information needed <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

## Negative Area (Signed Area)
When a velocity function is negative (meaning the car goes backward), the tiny change in distance `ds` is negative <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. In terms of thin rectangles, if a rectangle goes below the horizontal axis, its area represents distance traveled backward and is counted as negative <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. Therefore, integrals are said to measure the "signed area" between the graph and the horizontal axis <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

<hr/>

> [!quote] Grothendieck's Insight
> "Too often in math, we dive into showing that a certain fact is true with a long series of formulas before stepping back and making sure it feels reasonable, and preferably obvious, at least at an intuitive level." <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
> — Grothendieck

This perspective guides the approach to [[visualizing mathematical concepts | visualizing mathematical concepts]] like [[application_of_limits_in_integral_calculus | integral calculus]] through intuitive approximations and graphical representations.