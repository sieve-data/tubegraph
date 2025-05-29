---
title: Area under a curve in calculus
videoId: rfG8ce4nNh0
---

From: [[3blue1brown]] <br/> 

Often in mathematics, there's a tendency to jump into complex formulas before fully grasping the intuitive understanding of a concept <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Mathematical idol Grothendieck emphasized the importance of making concepts feel reasonable and obvious at an intuitive level <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. This article aims to illustrate that integrals are the inverse of derivatives, with a specific focus on [[visualization_in_calculus | visualizing]] the area under a curve <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Integrals as the Inverse of Derivatives

Consider a scenario where you are in a car, unable to see outside, with only a speedometer visible <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The car speeds up and slows down over 8 seconds <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The goal is to determine the total distance traveled during this time, or ideally, find a distance function `s(t)` that tells you how far the car has traveled after time `t` <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

If you plot the car's velocity over time, it might be modeled by the function `v(t) = t * (8 - t)` in meters per second <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. In a previous discussion (chapter 2), the opposite problem was addressed: knowing a distance function `s(t)` and deriving the velocity function from it using differentiation <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Therefore, finding a distance function from a known velocity function involves determining what function has `t * (8 - t)` as its derivative <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This process is known as finding the antiderivative <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Connecting to Area Under the Curve

The question of finding total distance traveled is deeply connected to finding the area bounded by the velocity graph and the horizontal axis <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This connection helps build [[intuition_behind_the_average_value_and_area_under_a_curve | intuition for integral problems]] in mathematics and science <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### Constant Velocity Scenario

If the car were moving at a constant velocity, calculating the distance would be straightforward: multiply velocity (meters per second) by time (seconds) <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This product can be visualized as the area of a rectangle on a velocity-time graph, where the horizontal axis represents seconds and the vertical axis represents meters per second <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. The units of this area naturally correspond to meters (distance) <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### Approximating with Changing Velocity

The challenge arises because velocity is constantly changing <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. To address this, the velocity function can be approximated as if it were constant over many small intervals <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This is a common technique in [[approximating_solutions_using_calculus | calculus]]: refining an approximation leads to a more precise result <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

For instance, divide the time axis (0 to 8 seconds) into small intervals of width `dt` (e.g., 0.25 seconds) <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. On each interval, approximate the car's velocity as constant, for convenience, using the velocity at the start of that interval <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. The distance traveled during this small interval `dt` is approximately `v(t) * dt`, which is visualized as the area of a thin rectangle <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

The sum of the areas of all these rectangles approximates the total distance <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. This sum is represented by the integral symbol (a stretched 'S' for sum), with limits indicating the time range (e.g., 0 to 8 seconds) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>:
$$ \int_0^8 v(t) \, dt $$
The `dt` signifies both a factor in each quantity being added and the spacing between sampled time steps <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. As `dt` approaches zero, the approximation becomes more accurate, and the sum approaches the exact area bounded by the curve and the horizontal axis <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This limiting value, the area under the curve, provides the precise answer to the total distance traveled <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This expression is called an integral, as it "integrates" or brings together all the values <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

## The Fundamental Theorem of Calculus

While finding the area under a curve might seem as difficult as the original problem, understanding how to interpret and compute this area is a general problem-solving tool applicable to many situations <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

Consider the integral of the velocity function between 0 and a variable upper bound `T` <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. This area represents the distance the car has traveled after `T` seconds, effectively defining the distance function `s(T)` <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

What is the derivative of this area function `s(T)`? A tiny change in distance `ds` over a tiny change in time `dt` is, by definition, velocity <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Graphically, a slight nudge of `dt` to the input `T` increases the area by a small sliver, `ds` <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. The height of this sliver is `v(T)`, and its width is `dt`, so `ds` is approximately `v(T) * dt` <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. As `dt` gets smaller, this approximation becomes exact, meaning the derivative `ds/dt` equals `v(t)` <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

This demonstrates a general principle: the derivative of any function representing the area under a graph is equal to the function of the graph itself <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

For `v(t) = t * (8 - t) = 8t - t^2` <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>, finding the antiderivative `s(t)` involves reversing the differentiation process:
*   Using the [[power_rule_in_calculus_and_its_geometric_significance | power rule]], the antiderivative of `8t` is `4t^2` (since the derivative of `4t^2` is `8t`) <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   Similarly, the antiderivative of `t^2` is `(1/3)t^3` (since the derivative of `(1/3)t^3` is `t^2`) <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
*   Thus, the antiderivative of `8t - t^2` is `4t^2 - (1/3)t^3` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

However, any constant `c` can be added to this function, and its derivative will still be `8t - t^2` (since the derivative of a constant is zero) <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. So, there are infinitely many antiderivatives of the form `4t^2 - (1/3)t^3 + c` <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

To find the specific distance function, we use the lower bound of the integral. The distance traveled between 0 seconds and 0 seconds must be zero <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. The [[fundamental_theorem_of_calculus | Fundamental Theorem of Calculus]] states that to evaluate a definite integral from `a` to `b` of a function `f(x)`, you find an antiderivative `F(x)` and compute `F(b) - F(a)` <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. This ensures that the integral from the lower bound to itself is zero <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

For our car example, `s(t) = 4t^2 - (1/3)t^3`. Since `s(0) = 0`, the constant `c` is 0 in this case <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. The total distance traveled over 8 seconds is `s(8) = 4(8)^2 - (1/3)(8)^3 = 85.33` meters <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. For an integral between two non-zero bounds, like 1 and 7, you would evaluate `F(7) - F(1)` <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

It's remarkable that to compute an integral, which considers every input on a continuum, you only need to evaluate the antiderivative at the two endpoints <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. The antiderivative implicitly accounts for all the information needed between those bounds <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

## Negative Area (Signed Area)

Integrals measure "signed area" <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. If the velocity function `v(t)` is negative at some point, it means the car is moving backward <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. In terms of the thin rectangles, if a rectangle extends below the horizontal axis, its area contributes negatively to the total sum, representing distance traveled in the reverse direction <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. This is crucial if the goal is to find the net displacement (distance between start and end points) <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

## Conclusion

The journey from approximating a continuously changing velocity with small, constant-velocity intervals to summing their areas, and then realizing this sum converges to the precise area under the curve, highlights the power of integrals <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. The key insight is that the derivative of this area function equals the original function, allowing the calculation of the integral by finding an antiderivative and evaluating it at the bounds <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. This concept of the integral as a sum of many small things, tied to the area under a curve, is a versatile problem-solving tool in various contexts <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.