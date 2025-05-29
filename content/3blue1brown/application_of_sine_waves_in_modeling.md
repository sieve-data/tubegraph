---
title: Application of sine waves in modeling
videoId: FnJqaIESC2s
---

From: [[3blue1brown]] <br/> 

[[fourier_series_and_sine_waves | Sine waves]] are commonly used to model various cyclic phenomena in the world <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. For instance, the number of hours the sun is visible per day over the course of a year follows a [[fourier_series_and_sine_waves | sine wave]] pattern <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Finding the Average of a Continuous Variable
To predict the average effectiveness of solar panels in different seasons, one might need to find the average value of a [[fourier_series_and_sine_waves | sine function]] over a specific period <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This involves finding the average height of a graph, such as `sin(x)` between 0 and pi, which represents half of its period <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

The challenge in finding the average of a continuous variable, like the height of a [[fourier_series_and_sine_waves | sine wave]], is that there are infinitely many values <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Unlike with a finite number of variables where values are summed and divided by the count, this approach is not feasible for a continuum <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Approximating the Average with Integrals
When encountering a situation that feels like summing infinitely many values associated with a continuum, the key is almost always to use an integral <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

A good first step to understanding how integrals apply is to approximate the situation with a finite sum <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. If one samples a finite number of points evenly spaced along a range, their average can be found by summing their heights and dividing by the number of sampled points <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. As more points are sampled, this approximation approaches the true average of the continuous variable <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

The process for taking an integral of `sin(x)` between 0 and pi involves summing `sin(x)` times `dx`, where `dx` is the spacing between samples, effectively adding up little areas <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. The integral itself is the limit of this sum as `dx` approaches 0 <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

To reframe the average of heights in terms of `dx`:
1.  The sum of heights is `Σ sin(x)`.
2.  The number of samples is approximately `(length of interval) / dx` (e.g., `π / dx` for the range 0 to pi) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
3.  The average becomes `(Σ sin(x)) / (π / dx)`.
4.  Rearranging, this is `(Σ sin(x) * dx) / π` <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

As the sample size increases (i.e., `dx` approaches 0), the sum `Σ sin(x) * dx` approaches the integral of `sin(x)` between 0 and pi <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Therefore, the average height of the graph is the integral (area under the graph) divided by the length of the interval (its width) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This concept aligns intuitively, as "area divided by width gives you an average height" <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

### Example: Average Height of `sin(x)` from 0 to π
To compute the integral of `sin(x)`, one must find its antiderivative, a function whose [[applications_of_derivatives_in_realworld_phenomena | derivative]] is `sin(x)` <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   The [[applications_of_derivatives_in_realworld_phenomena | derivative]] of `cos(x)` is `-sin(x)` <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
*   Thus, the antiderivative of `sin(x)` is `-cos(x)` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

To evaluate the definite integral from 0 to π:
1.  Evaluate the antiderivative at the upper bound (`-cos(π)`).
2.  Subtract its value at the lower bound (`-cos(0)`) <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
    *   `-cos(π) = -(-1) = 1`
    *   `-cos(0) = -(1) = -1`
    *   `1 - (-1) = 2` <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>

The area under the `sin(x)` graph between 0 and π is exactly 2 <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
Therefore, the average height of `sin(x)` on this interval is `(Integral of sin(x) from 0 to π) / π = 2 / π` (approximately 0.64) <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

## Integrals and Derivatives as Inverses
This problem offers a perspective on why integrals and [[applications_of_derivatives_in_realworld_phenomena | derivatives]] are inverses <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The average value (2/π) is found by looking at the change in the antiderivative (`-cos(x)`) over the input range, divided by the length of that range <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. This fraction represents the "rise over run" slope between the antiderivative's value at 0 and its value at π <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

Since `sin(x)` is, by definition, the [[applications_of_derivatives_in_realworld_phenomena | derivative]] of `-cos(x)` (giving the slope of `-cos(x)` at every point) <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>, the average value of `sin(x)` can also be viewed as the average slope of all tangent lines to `-cos(x)` between 0 and π <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. It makes sense that the average slope of a graph over a range equals the total slope between its start and end points <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### Generalization
For any function `f(x)`, its average value on an interval `[a, b]` is given by:
`Average Value = (Integral of f(x) from a to b) / (b - a)` <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
This can be thought of as the signed area under the graph divided by its width <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
If `F(x)` is the antiderivative of `f(x)`, then the integral is `F(b) - F(a)` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
Thus, the average value is `(F(b) - F(a)) / (b - a)` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. This is the slope of the antiderivative graph between its two endpoints <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

This perspective highlights that finding the average of a continuous value by comparing endpoints (the total change in the antiderivative) is equivalent to finding the average slope of all tangent lines (the function itself) over that range <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

### When to Consider Integrals
Integrals come to mind not only when approximating a problem by summing many small things <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>, but also when generalizing an idea from a finite context (like averaging numbers) to an infinite, continuous range of values <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. This generalization frequently arises in areas like probability <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.