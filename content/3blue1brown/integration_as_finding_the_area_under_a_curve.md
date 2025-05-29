---
title: Integration as finding the area under a curve
videoId: rfG8ce4nNh0
---

From: [[3blue1brown]] <br/> 

In mathematics, **integrals** are closely related to [[integrals_and_derivatives | derivatives]], serving as their inverse <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The core intuition behind [[visualizing_integration_and_approximations | integrals]] can be built by understanding them as a method for finding the area bounded by a function's graph and the horizontal axis <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## The Car Velocity Problem

Imagine observing only a car's speedometer and wanting to determine the total distance traveled <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. The speedometer shows velocity, which changes over time, for example, accelerating and then slowing down to a stop over 8 seconds <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. If we plot this velocity (v) over time (t), we might get a curve described by a function like `v(t) = t * (8 - t)` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

This scenario is the inverse of finding velocity from a known distance function (s(t)) using [[integrals_and_derivatives | derivatives]] <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Since the derivative of a distance-time function yields a velocity-time function, finding a distance-time function from a velocity-time function involves determining what function has `v(t)` as its derivative <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This process is called finding the [[antiderivatives_and_their_role_in_integration | antiderivative]] <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Approximating Distance with Area

If the car's velocity were constant, calculating the distance would be simple: multiply velocity by time. This product can be visualized as the area of a rectangle on a velocity-time graph <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. On such a plot, where the x-axis is time (seconds) and the y-axis is velocity (meters per second), the units of area naturally correspond to meters <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

However, since velocity is constantly changing, a direct calculation is not possible <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. To solve this, we can approximate the velocity as constant over many small time intervals. For each interval, say of width `dt` (e.g., 0.25 seconds), we approximate the distance traveled by multiplying the velocity at the start of the interval (`v(t)`) by `dt` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This gives the area of a thin rectangle <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

The total approximate distance is the sum of the areas of all these thin rectangles <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. As `dt` becomes smaller and smaller, the approximation becomes more precise, and the sum of the rectangle areas approaches the true area under the velocity curve <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## The Integral Notation

This concept of summing infinitesimally thin rectangles is represented by the integral notation:
`∫₀⁸ v(t) dt` <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

*   The stretched 'S' symbol (∫) signifies a sum <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   The numbers at the top and bottom (0 and 8 in this case) indicate the range of time steps (from 0 to 8 seconds) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   `v(t) dt` represents the quantity being added at each time step: `velocity * tiny_change_in_time` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

Crucially, this notation expresses the limit of the sum as `dt` approaches zero <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This limit, the area bounded by the curve and the horizontal axis, provides the precise answer to the question of how far the car traveled <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

## The Fundamental Theorem of Calculus

While finding the area under a curve might seem as difficult as the original problem, it serves as a universal language for many problems that can be broken down into summing small quantities <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

Consider the area under the velocity curve as a function itself, where the upper bound is a variable `T`. This area function, `s(T)`, represents the distance traveled after `T` seconds <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. The [[relationship_between_integrals_and_derivatives | derivative]] of this distance function (`ds/dT`) is the velocity `v(T)` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This is because a tiny change in the upper bound `dt` adds a sliver of area approximately equal to `v(t) * dt` <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

This leads to a general and fundamental principle: the derivative of any function giving the area under a graph is equal to the function for the graph itself <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

To compute an integral, the first step is to find an [[antiderivatives_and_their_role_in_integration | antiderivative]] (e.g., `F(x)`) of the function inside the integral (`f(x)`) <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>. For example, if `v(t) = 8t - t^2`, its antiderivative is `4t^2 - (1/3)t^3` <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

However, any constant can be added to an antiderivative without changing its derivative (e.g., `4t^2 - (1/3)t^3 + C`) <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. To find the specific value of a definite integral (with upper and lower bounds), you evaluate the antiderivative at the top bound and subtract its value at the bottom bound <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. For instance, the total distance traveled from 0 to 8 seconds is `[4(8)^2 - (1/3)(8)^3] - [4(0)^2 - (1/3)(0)^3] = 85.33` meters <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This powerful relationship is known as the [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

## Signed Area

When a function's graph dips below the horizontal axis, the integral counts this area as negative <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>. For example, if velocity is negative, the car is moving backward, and the distance traveled in that direction is subtracted from the total displacement <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. Therefore, integrals are said to measure the **signed area** between the graph and the horizontal axis <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.

Understanding integrals as the area under a curve provides a powerful and general problem-solving tool applicable across various fields in math and science <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.