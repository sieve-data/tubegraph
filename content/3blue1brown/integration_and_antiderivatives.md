---
title: Integration and antiderivatives
videoId: rfG8ce4nNh0
---

From: [[3blue1brown]] <br/> 

Mathematics often prioritizes proving a fact with formulas over building an intuitive understanding <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This article aims to make it intuitively obvious that [[Derivatives and integrals | integrals]] are the inverse operation of [[Derivatives and integrals | derivatives]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## The Car Example: Velocity to Distance

Imagine sitting in a car where you can only see the speedometer, not outside <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The car speeds up and slows down over 8 seconds <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The challenge is to figure out the total distance traveled or a distance function `s(t)` based solely on the speedometer readings <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

Let's say the velocity `v(t)` is modeled by the function `t * (8 - t)` in meters per second <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. In a previous discussion, the opposite problem was addressed: knowing a distance function `s(t)` and figuring out the velocity function from it <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. That problem showed how the [[Derivatives and integrals | derivative]] of a distance-time function yields a velocity-time function <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

Now, with only velocity known, finding the distance function `s(t)` means asking: what function has `t * (8 - t)` as its [[Derivatives and integrals | derivative]]? <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a> This process is known as finding the [[Antiderivatives and solving integrals | antiderivative]] of a function <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Connecting Distance to Area Under the Curve

While finding an [[Antiderivatives and solving integrals | antiderivative]] directly solves the problem, there's a powerful intuitive connection to the area bounded by the velocity graph <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This intuition is key for understanding [[Derivatives and integrals | integral]] problems in various fields <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### Constant Velocity Scenario

If the car moved at a constant velocity, calculating distance would be simple: multiply velocity (meters/second) by time (seconds) <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This product (distance) can be visualized as the area of a rectangle on a velocity-time graph <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. On such a plot, the units of area (meters/second * seconds) naturally correspond to meters <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

### Approximating with Rectangles

The difficulty arises because velocity is constantly changing <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. To tackle this, the velocity function can be approximated as if it were constant over many small time intervals <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

1.  **Divide the Time Axis**: Chop the time axis (e.g., from 0 to 8 seconds) into many small intervals, each with a width `dt` (e.g., 0.25 seconds) <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
2.  **Constant Velocity Approximation**: For each interval, approximate the car's velocity as constant. A convenient choice is the true velocity at the start of that interval (the height of the graph above the left side) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
3.  **Calculate Interval Distance**: The distance traveled in each small interval is approximately `v(t) * dt` <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This can be visualized as the area of a thin rectangle <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
4.  **Summation**: Sum the areas of all these rectangles <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### The Integral: A Limit of Sums

The expression for this sum is written using a stretched 'S' symbol, representing an [[Derivatives and integrals | integral]] <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>:
$$ \int_0^8 v(t) dt $$
This notation implies two things <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>:
*   `dt` is a factor in each quantity being added <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   `dt` also indicates the spacing between sampled time steps <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

As `dt` becomes smaller and smaller, the number of rectangles increases, and the approximation becomes more precise <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. The [[Derivatives and integrals | integral]] expresses the value that this sum approaches as `dt` approaches zero <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This limiting value is precisely the area bounded by the curve and the horizontal axis <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>, which gives the exact distance traveled <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

The concept of "area under a graph" is a general problem-solving tool, common in many scientific and mathematical problems that involve summing a large number of small things <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

## The Fundamental Theorem of Calculus

The [[Relationship between integrals and derivatives | relationship between integrals and derivatives]] is profound. Consider the area under the velocity curve from 0 to a variable `T` as a function `s(T)` <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. This `s(T)` represents the distance traveled after `T` seconds <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

What is the [[Derivatives and integrals | derivative]] of this distance function `s(T)`? <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a> A tiny change in distance `ds` over a tiny change in time `dt` is, by definition, velocity <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

Visually, a slight nudge `dt` to the input `T` adds a thin sliver of area `ds` <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. The height of this sliver is `v(T)` (the height of the graph at that point) and its width is `dt` <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. For small `dt`, `ds` is approximately `v(T) * dt` <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. Therefore, the [[Derivatives and integrals | derivative]] of the area function, `ds/dt`, equals `v(T)`, the value of the velocity function at that time <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

This leads to a general argument: the [[Derivatives and integrals | derivative]] of any function that gives the area under a graph is equal to the function of the graph itself <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This is the essence of the [[Relationship between integrals and derivatives | Fundamental Theorem of Calculus]].

### Finding the Antiderivative

To find `s(t)` for `v(t) = t * (8 - t)` (or `8t - t^2`), we need to find its [[Antiderivatives and solving integrals | antiderivative]] <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   For `8t`: The [[Derivatives and integrals | derivative]] of `t^2` is `2t` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. Scaling it up, the [[Derivatives and integrals | derivative]] of `4t^2` is `8t` <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   For `-t^2`: The [[Derivatives and integrals | derivative]] of `t^3` is `3t^2` <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. Scaling it down, the [[Derivatives and integrals | derivative]] of `(1/3)t^3` is `t^2` <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. Therefore, the [[Derivatives and integrals | derivative]] of `-(1/3)t^3` is `-t^2` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

So, an [[Antiderivatives and solving integrals | antiderivative]] of `8t - t^2` is `4t^2 - (1/3)t^3` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

### The Constant of Integration and Definite Integrals

A crucial point is that adding any constant `C` to an [[Antiderivatives and solving integrals | antiderivative]] does not change its [[Derivatives and integrals | derivative]] (since the [[Derivatives and integrals | derivative]] of a constant is zero) <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. Thus, there are infinitely many possible [[Antiderivatives and solving integrals | antiderivative]] functions, all of the form `4t^2 - (1/3)t^3 + C` <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

To find the specific distance traveled between two points, like `0` and `8` seconds, we use the bounds of the [[Derivatives and integrals | integral]] <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. The [[Derivatives and integrals | integral]] from a lower bound (`a`) to an upper bound (`b`) of a function `f(x)` is evaluated by finding an [[Antiderivatives and solving integrals | antiderivative]] `F(x)` and computing `F(b) - F(a)` <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>. This is the **Fundamental Theorem of Calculus** <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

For the car example, evaluating `s(t) = 4t^2 - (1/3)t^3` at `t = 8` gives the total distance traveled: `85.33` meters <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. If integrating between `t=1` and `t=7`, you would calculate `s(7) - s(1)` <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>. The constant `C` cancels out in this subtraction, confirming that any [[Antiderivatives and solving integrals | antiderivative]] can be used <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

The remarkable aspect of the Fundamental Theorem of Calculus is that to compute an [[Derivatives and integrals | integral]] (which accounts for every input on a continuum), one only needs to evaluate the [[Antiderivatives and solving integrals | antiderivative]] at two inputs: the top and bottom bounds <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

## Negative Area (Signed Area)

What if the velocity function is negative, meaning the car moves backwards? <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a> A tiny change in distance `ds` is still `v(t) * dt`, but `v(t)` would be negative, resulting in a negative `ds` <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

On the graph, if a rectangle goes below the horizontal axis, its "area" represents distance traveled backward <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. This backward distance is subtracted from the total <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. Therefore, [[Derivatives and integrals | integrals]] measure the **signed area** between the graph and the horizontal axis <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

## Recap

*   To find total distance from varying velocity, approximate the journey as constant velocity on many small intervals <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
*   The sum of distances (velocity * time) on these intervals corresponds to the sum of areas of thin rectangles <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
*   As the interval width approaches zero, this sum approaches the exact area under the velocity curve, which is the precise total distance traveled <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.
*   Thinking of this area as a function of its right endpoint, its [[Derivatives and integrals | derivative]] is the original function (the height of the graph) <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   Thus, to find the area function, one needs to find an [[Antiderivatives and solving integrals | antiderivative]] of the original function <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
*   The constant of integration in [[Antiderivatives and solving integrals | antiderivatives]] is handled by subtracting the value of the [[Antiderivatives and solving integrals | antiderivative]] at the lower bound from its value at the upper bound <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   When a function's graph dips below the horizontal axis, the area is counted as negative, representing "signed area" <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>.

This understanding of [[Derivatives and integrals | integrals]] and [[Antiderivatives and solving integrals | antiderivatives]] forms the [[Relationship between integrals and derivatives | fundamental theorem of calculus]], a powerful tool for solving a wide range of problems.