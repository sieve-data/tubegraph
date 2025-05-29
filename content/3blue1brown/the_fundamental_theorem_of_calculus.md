---
title: The fundamental theorem of calculus
videoId: rfG8ce4nNh0
---

From: [[3blue1brown]] <br/> 
> [!quote] Grothendieck's Insight
> Too often in math, we dive into showing that a certain fact is true with a long series of formulas before stepping back and making sure it feels reasonable, and preferably obvious, at least at an intuitive level. <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>

This article explores [[introduction_to_calculus | integrals]] and their relationship with derivatives, building towards an [[intuition_behind_calculus_rules | intuitive understanding]] of the [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The core idea is to make it "almost obvious" that integrals are an inverse of derivatives <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Integrals as the Inverse of Derivatives

Consider a scenario where you are in a car, only able to see the speedometer, and you want to determine how far you've traveled over 8 seconds, given the velocity function v(t) = t * (8 - t) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This is the dual of a problem from Chapter 2 of this series, where a distance function s(t) was known, and the goal was to find the velocity <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. There, the derivative of a distance vs. time function yielded the velocity vs. time function <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

In the current situation, knowing only the velocity, finding a distance vs. time function means asking: What function has a derivative of t * (8 - t)? <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a> This process is known as finding the [[understanding_antiderivatives_in_calculus | antiderivative]] of a function <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Connecting to Area Under the Curve

To build intuition for [[introduction_to_calculus | integral]] problems, it's helpful to see how this question relates to finding the area bounded by the velocity graph <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Constant Velocity Approximation
If the car moved at a constant velocity, the distance traveled would simply be velocity multiplied by time <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This product can be visualized as the area of a rectangle on a velocity-time plot, where the horizontal axis represents time (seconds) and the vertical axis represents velocity (meters per second) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. The units of area (meters/second * seconds) naturally correspond to meters <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

However, car velocity is constantly changing <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. If velocity changed discontinuously at a few points, you could calculate distance on each constant-velocity interval and sum them up <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Approximating with Rectangles (Riemann Sums)
To handle continuously changing velocity, we approximate the velocity function as if it were constant over many small time intervals <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. As is common in [[introduction_to_calculus | calculus]], refining this approximation leads to a more precise result <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

1.  **Chop up the time axis**: Divide the total time (e.g., 0 to 8 seconds) into many small intervals, each with a width `dt` (e.g., 0.25 seconds) <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
2.  **Approximate velocity on each interval**: On each small interval, assume the car's velocity is constant, for instance, equal to the true velocity at the start of that interval <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
3.  **Calculate distance for each interval**: The approximated distance on each interval is `v(t) * dt`, which is visualized as the area of a thin rectangle <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
4.  **Sum the distances**: The total approximated distance is the sum of the areas of all these rectangles <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

This sum is denoted by a stretched 'S' symbol, known as an [[introduction_to_calculus | integral]] sign:
∫₀⁸ v(t) dt <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>

In this notation:
*   `dt` serves as both a factor in the quantity being added (`v(t) * dt`) and indicates the spacing between sampled time steps <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
*   The expression doesn't represent a specific sum for a particular `dt`, but rather what that sum approaches as `dt` approaches 0 <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

As `dt` approaches 0, the sum of these rectangle areas approaches the exact area bounded by the curve and the horizontal axis <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This limiting value, the area under the curve, provides the precise answer to the question of how far the car traveled <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This expression is called an [[introduction_to_calculus | integral]] of `v(t)` because it "integrates" or brings all its values together <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

While finding the area under a curve might seem equally hard, it is a common language for many diverse problems that can be broken down and approximated as sums of small things <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Understanding how to interpret and compute the area under a graph is a very general problem-solving tool <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

## The Fundamental Theorem of Calculus

Let's consider the right endpoint of the integral as a variable, say `T`. The [[introduction_to_calculus | integral]] of the velocity function between 0 and `T`, representing the area under the curve up to `T`, is a function of `T` <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. This function, `s(T)`, represents the distance the car has traveled after `T` seconds <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

Now, what is the derivative of this distance function, `s(T)`? A tiny change in distance (`ds`) over a tiny change in time (`dt`) is, by definition, velocity <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. In terms of the graph, a slight nudge of `dt` to the input `T` increases the area by a small sliver <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. The height of this sliver is `v(T)`, and its width is `dt` <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. For small `dt`, this sliver is approximately a rectangle, so `ds` ≈ `v(T) * dt` <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

As the approximation gets better for smaller `dt`, the derivative `ds/dt` at any point `T` equals `v(T)`, the value of the velocity function at that time <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. This is a general argument: the derivative of any function giving the area under a graph is equal to the function for the graph itself <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

Therefore, to find the distance function `s(T)` when `v(T)` = `T * (8 - T)`, we need to find a function whose derivative is `T * (8 - T)` <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
Expanding `T * (8 - T)` gives `8T - T²` <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   To get `8T`, we need `4T²` (since the derivative of `4T²` is `8T`) <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   To get `-T²`, we need `-(1/3)T³` (since the derivative of `T³` is `3T²`, so `-(1/3)T³` yields `-T²` using the [[product_rule_in_calculus | power rule]]) <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

So, the [[understanding_antiderivatives_in_calculus | antiderivative]] of `8T - T²` is `4T² - (1/3)T³` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

### The Constant of Integration
A key aspect of [[understanding_antiderivatives_in_calculus | antiderivatives]] is that you can add any constant `C` to the function, and its derivative will still be the same (e.g., `8T - T²`) because the derivative of a constant is zero <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. This means there are infinitely many possible [[understanding_antiderivatives_in_calculus | antiderivative]] functions, all of the form `4T² - (1/3)T³ + C` <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

However, for a definite [[introduction_to_calculus | integral]] (with specific upper and lower bounds), the constant `C` is resolved by the lower bound of the integral <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. The [[introduction_to_calculus | integral]] from a lower bound to itself must be zero (e.g., distance traveled between 0 seconds and 0 seconds is zero) <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

The [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] states that to evaluate the [[introduction_to_calculus | integral]] of a function `f(x)` from `a` to `b`:
1.  Find an [[understanding_antiderivatives_in_calculus | antiderivative]], let's call it `F(x)`, such that `F'(x) = f(x)` <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
2.  The [[introduction_to_calculus | integral]] equals `F(b) - F(a)` <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

This means the constant `C` always cancels out: `(F(b) + C) - (F(a) + C) = F(b) - F(a)` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

For our car example, the total distance traveled during the full 8 seconds is `s(8) - s(0)`:
(4 * 8² - (1/3) * 8³) - (4 * 0² - (1/3) * 0³) = 85.33 meters <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

It's "crazy" that the [[introduction_to_calculus | integral]], which considers every single input on a continuum, can be computed by looking only at the two bounds (top and bottom) with an [[understanding_antiderivatives_in_calculus | antiderivative]] <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. The [[understanding_antiderivatives_in_calculus | antiderivative]] implicitly accounts for all the necessary information <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

### Signed Area
The concept of area under the curve extends to "negative area." If the velocity function `v(t)` is negative at some point (meaning the car is going backward), the product `v(t) * dt` will be negative <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. In terms of rectangles, if a rectangle goes below the horizontal axis, its area represents distance traveled backward <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. This negative contribution is subtracted from the total. Therefore, [[introduction_to_calculus | integrals]] measure the *signed area* between the graph and the horizontal axis <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

## Recap
*   To find distance from velocity, you need to solve the inverse problem of differentiation, which is finding an [[understanding_antiderivatives_in_calculus | antiderivative]] <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
*   Approximating velocity with constant segments allows you to sum up distances as areas of rectangles <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.
*   As the approximation gets finer (dt approaches 0), this sum approaches the true area under the velocity curve, which represents the precise distance traveled <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   This area, viewed as a function of its variable upper bound, has a derivative equal to the original function (e.g., the derivative of the distance function is the velocity function) <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   This means finding the area function is equivalent to finding an [[understanding_antiderivatives_in_calculus | antiderivative]] of the original function <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
*   The [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] connects definite integrals to [[understanding_antiderivatives_in_calculus | antiderivatives]], allowing calculation by evaluating the [[understanding_antiderivatives_in_calculus | antiderivative]] at the upper and lower bounds and subtracting <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   [[introduction_to_calculus | Integrals]] measure signed area, meaning area below the x-axis is counted as negative <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.