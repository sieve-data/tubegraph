---
title: Antiderivatives and their role in integration
videoId: rfG8ce4nNh0
---

From: [[3blue1brown]] <br/> 
> [!quote] "Too often in math, we dive into showing that a certain fact is true with a long series of formulas before stepping back and making sure it feels reasonable, and preferably obvious, at least at an intuitive level." <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
> — Grothendieck <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>

[[integrals_and_derivatives | Integrals]] are presented as the inverse of [[understanding_derivatives_of_combined_functions | derivatives]], with the goal of making this [[relationship_between_integrals_and_derivatives | relationship]] intuitively obvious <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This concept involves finding an [[understanding_antiderivatives_in_calculus | antiderivative]] of a function <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## The Car Example: Distance from Velocity

Consider a scenario where you are in a car, unable to see outside, with only the speedometer visible <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The car speeds up and then slows down over 8 seconds <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The challenge is to determine the total distance traveled based solely on the speedometer readings <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, or more broadly, to find a distance function `s(t)` for any time `t` between 0 and 8 seconds <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

If you plot the car's velocity over time, it might be modeled by the function `v(t) = t * (8 - t)` in meters per second <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### The Inverse Problem
In earlier discussions, the opposite situation was explored: knowing a distance function `s(t)` and deriving the velocity function from it using [[calculating_derivatives_and_their_applications | derivatives]] <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. The derivative of a distance vs. time function yields a velocity vs. time function <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Therefore, finding a distance vs. time function when only velocity is known means asking what function has `t * (8 - t)` as its derivative <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This process is called finding the [[understanding_antiderivatives_in_calculus | antiderivative]] <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Connecting to Area Under the Curve
The question of finding total distance is deeply related to finding the area bounded by the velocity graph <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This connection provides intuition for a class of problems known as [[integrals_and_derivatives | integral problems]] <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

*   **Constant Velocity:** If velocity were constant, distance would simply be velocity multiplied by time <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This product can be visualized as the area of a rectangle on a velocity-time plot, where the horizontal axis has units of seconds and the vertical axis has units of meters per second, making the area units correspond to meters <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Approximating with Rectangles:** Since real-world velocity is constantly changing, approximation is necessary <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The velocity function can be approximated as if it were constant over many small time intervals, each with a width `dt` (e.g., 0.25 seconds) <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
    *   For each interval, the distance traveled is `v(t) * dt`, which is the area of a thin rectangle <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. The chosen constant velocity for the interval (e.g., at the start of the interval) doesn't matter for the limit, only that the approximation improves as `dt` shrinks <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
    *   The sum of these rectangle areas approximates the total distance <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **The Integral Symbol:** The sum of these areas is represented by the [[integrals_and_derivatives | integral]] symbol (a stretched 'S' for sum) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. For the car example, it's expressed as `∫[0 to 8] v(t) dt` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   Implicit in this notation is that `dt` represents both a factor in the quantity being summed and the spacing between sampled time steps <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
    *   This expression represents the limit of the sum as `dt` approaches 0 <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. This limit precisely equals the area bounded by the curve and the horizontal axis <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>, giving the exact distance traveled <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## The Fundamental Theorem of Calculus

The profound connection arises when considering the area under the curve as a function itself.

### Area as a Function
If we define the area under the velocity curve from 0 to a variable upper bound `T` as a function `s(T)`, this function represents the distance traveled after `T` seconds <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

*   **Derivative of the Area Function:** The derivative of this area function `s(T)` with respect to `T` is precisely the velocity `v(T)` at that point <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
    *   A tiny change `dT` in the input causes the area `s` to increase by a small amount `dS` <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
    *   This `dS` is approximately the area of a thin sliver (rectangle) with height `v(T)` and width `dT` <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
    *   Thus, `dS/dT` (the derivative) equals `v(T)` <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   **Generalization:** This generalizes to any function: the derivative of any function giving the area under a graph is equal to the function for the graph itself <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

### Finding the Antiderivative
Since the derivative of the distance function `s(t)` is `v(t) = t * (8 - t) = 8t - t^2` <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>, we need to find a function whose derivative is `8t - t^2`.

*   **Term by Term:**
    *   For `8t`: The derivative of `t^2` is `2t`, so scaling by 4, the derivative of `4t^2` is `8t` <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
    *   For `-t^2`: The derivative of `t^3` is `3t^2`. Scaling by `1/3` gives `t^2` (from `(1/3)t^3`), so the derivative of `-(1/3)t^3` is `-t^2` <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **General Antiderivative:** Thus, an antiderivative of `8t - t^2` is `4t^2 - (1/3)t^3` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. However, since the derivative of a constant is zero, any constant `C` can be added to this function without changing its derivative <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. So, the general [[understanding_antiderivatives_in_calculus | antiderivative]] is `4t^2 - (1/3)t^3 + C` <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

### Definite Integrals and Evaluation
The specific constant `C` is determined by the lower bound of the integral <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
The distance traveled by the car between time `0` and `0` is zero <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

The **Fundamental Theorem of Calculus** states that to evaluate the integral of a function `f(x)` from `a` to `b`:
1.  Find an [[understanding_antiderivatives_in_calculus | antiderivative]], `F(x)`, of `f(x)` <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.
2.  The integral equals `F(b) - F(a)` <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

This means that `C` effectively cancels out, as `(F(b) + C) - (F(a) + C) = F(b) - F(a)` <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. For the car example, the total distance traveled during 8 seconds is `(4 * 8^2 - (1/3) * 8^3) - (4 * 0^2 - (1/3) * 0^3)` which is `85.33` meters <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

> [!tip] The "crazy" aspect of the Fundamental Theorem of Calculus is that an integral, which considers every input on a continuum, can be computed by looking at only two inputs: the top and bottom bounds of the integral <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. The [[understanding_antiderivatives_in_calculus | antiderivative]] implicitly accounts for all the necessary information <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

## Recap of Antiderivatives and Integration
*   To find how far a car travels from its speedometer, given constantly changing velocity <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
*   Approximate velocity as constant over small intervals, sum distances, and refine approximations <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.
*   Better approximations correspond to the aggregate area of rectangles approaching the true area under the velocity curve <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   The area under the curve is the precise distance traveled <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.
*   If that area is considered a function with a variable endpoint, its derivative equals the height of the original graph (the velocity function) at every point <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   Therefore, to find the area function, one asks what function has `v(t)` as its derivative – this is finding the [[understanding_antiderivatives_in_calculus | antiderivative]] <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
*   There are infinitely many [[understanding_antiderivatives_in_calculus | antiderivatives]] (differing by a constant), but the definite integral uses the difference between the antiderivative at the top and bottom bounds, effectively canceling out any constant <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.

## Negative Area (Signed Area)
If the velocity function becomes negative, it means the car is moving backwards <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. In terms of integrals:
*   A negative velocity over a small time interval results in a negative change in distance `dS` <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.
*   This corresponds to a thin rectangle whose area is below the horizontal axis <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
*   This "negative area" is subtracted from the total, representing distance traveled backwards <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   [[integrals_and_derivatives | Integrals]] measure the **signed area** between the graph and the horizontal axis <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

## Broader Context
Understanding how to interpret and compute the area under a graph is a very general problem-solving tool, applicable to many disparate problems approximated as sums of small things <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. More contexts and intuitions for the fundamental theorem of calculus will be explored further <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.

This video was supported by The Art of Problem Solving, which offers resources like Beast Academy for elementary school children and courses for higher-level topics and contest preparation <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.