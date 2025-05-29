---
title: Approximating solutions using calculus
videoId: rfG8ce4nNh0
---

From: [[3blue1brown]] <br/> 
### Approximating Solutions Using Calculus: The Power of Integrals

The field of calculus often emphasizes the importance of intuition before diving into rigorous formulas. As mathematician Grothendieck noted, "Too often in math, we dive into showing that a certain fact is true with a long series of formulas before stepping back and making sure it feels reasonable, and preferably obvious, at least at an intuitive level." <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a> This principle is key to understanding integrals, which are presented as the inverse of [[introduction_to_derivatives_and_calculus_concepts | derivatives]]. <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>

#### The Problem: Finding Distance from Velocity

Consider a scenario where you are in a car, unable to see outside, with only the speedometer visible. <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a> The car starts, speeds up, and then slows to a stop over 8 seconds. <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a> The challenge is to determine the total distance traveled, or, more generally, to find a distance function `s(t)` that tells you how far you've traveled after time `t` (between 0 and 8 seconds), based solely on the speedometer readings. <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>

If you plot the velocity `v(t)` over time, you might find it can be modeled by a function like `v(t) = t * (8 - t)` in meters per second. <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a> In the [[introduction_to_derivatives_and_calculus_concepts | introduction to calculus series]], the opposite problem was explored: finding velocity from a known distance function `s(t)`. <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a> There, the [[calculating_derivatives_and_algebraic_simplification_in_calculus | derivative]] of a distance-time function yields a velocity-time function. <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a> Therefore, to find a distance-time function from a known velocity function, one must ask what function has `v(t)` as its derivative – this is known as finding the antiderivative. <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>

#### Connecting Distance to Area Under the Curve

While finding an antiderivative is the ultimate goal, the bulk of this problem's intuition comes from understanding its connection to the area bounded by the velocity graph. <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>

If the car moved at a constant velocity, calculating the distance would be straightforward: multiply velocity (meters per second) by time (seconds) to get meters traveled. <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a> This product can be visualized as the area of a rectangle on a velocity-time plot. <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a> On such a plot, where the horizontal axis is time (seconds) and the vertical axis is velocity (meters per second), the units of area naturally correspond to meters. <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>

The difficulty arises when velocity is not constant. <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a> To tackle this, the velocity function can be approximated as if it were constant over many small intervals. <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>

#### Approximation Using Rectangles (Riemann Sums)

This method involves chopping the time axis (e.g., from 0 to 8 seconds) into many small intervals, each with a tiny width, `dt` (e.g., 0.25 seconds). <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a> On each small interval, the car's velocity is approximated as a constant value (e.g., the velocity at the start of that interval). <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>, <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>

For a given interval, the approximated distance traveled is `v(t) * dt`, which is visualized as the area of a thin rectangle with height `v(t)` and width `dt`. <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a> The total approximated distance is the sum of the areas of all these rectangles. <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>

As `dt` becomes smaller and smaller:
*   The area of each individual rectangle decreases. <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>
*   The total number of rectangles increases, filling the space more accurately. <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>

This refinement leads to a more precise approximation of the actual distance traveled. <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>

#### The Integral: Limit of Approximations

The mathematical notation for this sum approaching a precise value is the integral, represented by a stretched 'S' symbol: `∫ v(t) dt`. <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a> The numbers at the bottom and top of the symbol (e.g., 0 and 8) indicate the range of time steps. <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a> This notation expresses the value that the sum approaches as `dt` approaches 0. <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>

This limiting value for the sum is precisely the area bounded by the velocity curve and the horizontal axis. <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a> This "area under the curve" provides the exact answer to the distance traveled. <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a> An integral "brings all of its values together, it integrates them." <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>

This insight demonstrates how a complex problem involving continuous change can be precisely solved by approximating it as a sum of many tiny parts. <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>

#### The Fundamental Theorem of Calculus

The true power of integrals becomes apparent when connecting them back to derivatives. <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a> If we consider the area under the velocity curve from time 0 to a variable `T` as a function, `s(T)`, this function represents the distance traveled after `T` seconds. <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>

What is the [[calculating_derivatives_and_algebraic_simplification_in_calculus | derivative]] of this distance function, `ds/dT`? <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a> A tiny change in distance `ds` over a tiny change in time `dt` is velocity, `v(t)`. <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a> Geometrically, a slight increase `dt` in the input `T` adds a thin sliver of area to `s(T)`. The area of this sliver, `ds`, is approximately `v(t) * dt` (height of the graph `v(t)` multiplied by its width `dt`). <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>, <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a> As `dt` approaches zero, this approximation becomes exact: `ds/dt = v(t)`. <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>

This leads to a general and profound conclusion: The derivative of any function representing the area under a graph is equal to the function for the graph itself. <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>

Therefore, to find the distance function `s(t)` when `v(t) = 8t - t^2`, we need to find its antiderivative:
*   The antiderivative of `8t` is `4t^2` (since the derivative of `4t^2` is `8t`). <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>, <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>
*   The antiderivative of `-t^2` is `-(1/3)t^3` (since the derivative of `(1/3)t^3` is `t^2`). <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>, <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>

So, `s(t) = 4t^2 - (1/3)t^3 + C`, where `C` is an arbitrary constant (since the derivative of a constant is zero). <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>, <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>

To determine the constant `C`, we use the bounds of the integral. The distance traveled from 0 seconds to 0 seconds must be zero. <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a> This means the integral, or the area function `s(T)`, must be zero when `T` equals the lower bound. <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a> To ensure this, you subtract the value of the antiderivative at the lower bound from its value at the upper bound. <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>

This core concept is the **Fundamental Theorem of Calculus**: To evaluate the integral of a function `f(x)` from `a` to `b`:
1.  Find an antiderivative, `F(x)`, such that `F'(x) = f(x)`. <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>
2.  The integral equals `F(b) - F(a)`. <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>

This theorem is "crazy" because it computes a sum over a continuum of inputs using only two specific inputs: the top and bottom bounds. <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>

For the car example, evaluating `s(t) = 4t^2 - (1/3)t^3` at `t=8` gives the total distance traveled: `85.33` meters. <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>

#### Signed Area and Negative Velocity

An important consideration is the concept of "negative area" in integrals. If the velocity function `v(t)` becomes negative (meaning the car goes backward), the contribution to the total distance is negative. <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a> In terms of the thin rectangles, if a rectangle goes below the horizontal axis, its area represents distance traveled backward and is counted as negative. <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>

Therefore, integrals measure the *signed area* between the graph and the horizontal axis, not just positive area. <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a> This allows them to accurately determine the net displacement or "distance between the car's start point and its end point." <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>

The understanding of integrals and "area under curves" is a very general problem-solving tool, applicable to many disparate problems in math and science that can be broken down and approximated as sums of small things. <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>, <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>

***

*The [[introduction_to_calculus_series | Introduction to Calculus Series]] was supported by The Art of Problem Solving. <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a> They offer resources for students to develop a love for creative math, from elementary school (Beast Academy) to higher-level topics and contest preparation. <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>