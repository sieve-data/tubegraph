---
title: Velocity and distance relationship
videoId: rfG8ce4nNh0
---

From: [[3blue1brown]] <br/> 

Integrals are considered the inverse of [[derivative_and_velocity_relationship | derivatives]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This concept can be intuitively understood through the relationship between velocity and distance in motion.

## The Problem: Determining Distance from Velocity

Imagine being in a car where the only view is the speedometer, showing instantaneous velocity <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The car speeds up and slows down over 8 seconds <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The challenge is to determine the total distance traveled or to find a distance function, `s(t)`, that describes the distance traveled after a given time `t` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

If the velocity of the car over time (in meters per second) is modeled by the function `v(t) = t * (8 - t)` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, the question becomes: what function `s(t)` has `v(t)` as its derivative? This is known as finding the antiderivative <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Visualizing Distance as Area Under the Curve

### Constant Velocity Scenario
If the car moved at a constant velocity, the distance traveled would simply be the velocity multiplied by the time elapsed <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. On a [[graphical_representation_of_motion_distance_and_velocity | velocity-time plot]], this product can be visualized as the area of a rectangle <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Given that the horizontal axis represents time (seconds) and the vertical axis represents velocity (meters per second), the units of the area (seconds * meters/second) naturally correspond to meters, representing distance <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

### Approximating Changing Velocity
Since real-world velocity changes constantly, the challenge is greater <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. To address this, the velocity function can be approximated as if it were constant over many small time intervals <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

For each small interval, with a width `dt` (e.g., 0.25 seconds), the distance traveled can be approximated by multiplying the velocity at the start of that interval by `dt` <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This approximate distance corresponds to the area of a thin rectangle on the velocity-time graph <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Summing the areas of all these thin rectangles provides an approximation of the total distance traveled <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

## The Integral: Summing Infinitesimal Areas

The sum of these rectangular areas can be represented using the integral symbol (a stretched 'S' for sum) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. For example, the integral from 0 to 8 seconds of `v(t) * dt` denotes the sum of `v(t) * dt` for time steps between 0 and 8 seconds <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

As the width `dt` of these intervals approaches zero, the approximation becomes increasingly precise <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. The limiting value of this sum precisely equals the area bounded by the velocity curve and the horizontal axis <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This area, therefore, represents the precise distance traveled by the car <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

This expression is called an **integral** because it brings together, or integrates, all the infinitesimal contributions `v(t) * dt` across the range <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

## The Fundamental Theorem of Calculus

Thinking of the area under the velocity curve from time `0` to a variable `T` as a function `s(T)` (representing distance traveled after `T` seconds) <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>:

*   A tiny change in distance `ds` over a tiny change in time `dt` is velocity <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   Geometrically, a slight increase `dt` in the input `T` adds a sliver of area `ds` under the curve <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. The height of this sliver is `v(T)` and its width is `dt` <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   Thus, `ds` is approximately `v(T) * dt` <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   As `dt` approaches zero, the [[derivative_and_velocity_relationship | derivative]] of the area function, `ds/dt`, equals `v(T)` <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

This leads to a general principle: the derivative of any function giving the area under a graph is equal to the function for the graph itself <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

### Finding the Antiderivative
Given `v(t) = t * (8 - t) = 8t - t^2` <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>, we need a function `s(t)` whose derivative is `8t - t^2`.
*   The antiderivative of `8t` is `4t^2` (since the derivative of `4t^2` is `8t`) <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   The antiderivative of `-t^2` is `-(1/3)t^3` (since the derivative of `-(1/3)t^3` is `-t^2`) <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
*   Therefore, a possible antiderivative is `s(t) = 4t^2 - (1/3)t^3` <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### The Constant of Integration
Any constant `C` added to this antiderivative will still have a derivative of `8t - t^2` because the derivative of a constant is zero <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. So, there are infinitely many antiderivatives of the form `4t^2 - (1/3)t^3 + C` <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

### Definite Integrals and Evaluating the Constant
To find the precise distance traveled, the lower bound of the integral is used <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. The distance traveled from `0` seconds to `0` seconds must be zero <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

The **Fundamental Theorem of Calculus** states that to evaluate an integral of a function `f(x)` from `a` to `b` (denoted as `∫_a^b f(x) dx`), one finds an antiderivative `F(x)` of `f(x)` and then computes `F(b) - F(a)` <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. The constant `C` cancels out in this subtraction, ensuring a unique answer for the definite integral <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

For the car example, the total distance traveled during the full 8 seconds is `(4 * 8^2 - (1/3) * 8^3) - (4 * 0^2 - (1/3) * 0^3) = 85.33` meters <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

## Negative Area and Signed Area

If the velocity function goes negative (e.g., the car moves backward) <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>, the corresponding area below the horizontal axis is counted as negative <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. This means integrals measure "signed area" rather than just positive geometric area <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. This signed area represents the net change in position from the starting point <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.