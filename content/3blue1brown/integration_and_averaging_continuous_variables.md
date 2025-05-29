---
title: Integration and averaging continuous variables
videoId: FnJqaIESC2s
---

From: [[3blue1brown]] <br/> 

One common application of integration is in finding the average of a continuous variable <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This concept not only has practical uses but also offers a unique perspective on why [[integrals_and_derivatives | integrals and derivatives]] are inverses of each other <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## The Challenge of Averaging a Continuous Variable

Consider the graph of `sin(x)` between 0 and π <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A natural question is to determine the average height of this graph over that interval <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This is relevant because cyclic phenomena, such as the hours of sunlight per day, are often modeled using sine waves <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. For instance, calculating the average effectiveness of solar panels would require answering such a question <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

Averaging a continuous variable presents a unique challenge <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Typically, to find an average, one sums a finite number of values and divides by the count of those values <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. However, there are infinitely many values of `sin(x)` between 0 and π, making it impossible to sum them and divide by infinity <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

When there's a vague sense of wanting to sum infinitely many values associated with a continuum, the solution almost always involves an integral <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Approximating with Finite Sums

A helpful first step is to approximate the continuous situation with a finite sum <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This involves sampling a finite number of points evenly spaced along the range <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. The average can then be found by summing the heights of `sin(x)` at each sampled point and dividing by the total number of points <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. The more points sampled, the closer this approximation should be to the true average of the continuous variable <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. This process inherently relates to the [[concept_of_sample_approximation_in_integration | concept of sample approximation in integration]] and [[visualizing_integration_and_approximations | visualizing integration and approximations]]

While taking an integral of `sin(x)` between 0 and π also involves sampling inputs <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>, instead of just adding heights, the integral adds `sin(x)` times `dx` (the spacing between samples), representing little areas rather than heights <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. The integral is the limit of this sum as `dx` approaches 0 <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

To bridge the gap, the expression for the average (sum of heights / number of points) can be reframed in terms of `dx` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. If the interval length is π and the spacing is `dx`, the number of samples is approximately `π / dx` <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

Substituting this into the average formula:
$$ \text{Average} = \frac{\sum \sin(x)}{\text{Number of Samples}} = \frac{\sum \sin(x)}{\pi / dx} $$
Rearranging the terms:
$$ \text{Average} = \frac{1}{\pi} \sum \sin(x) \, dx $$
The numerator, `$\sum \sin(x) \, dx$`, closely resembles an integral expression <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. As `dx` approaches 0, the sum approaches the integral <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

Therefore, the average height of the graph approaches the integral of `sin(x)` between 0 and π, divided by the length of the interval, π <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
In essence, the average height is the area under the graph divided by its width <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. This aligns with [[integration_as_finding_the_area_under_a_curve | integration as finding the area under a curve]].

## Example: Average Height of `sin(x)`

To compute the integral `$\int_0^\pi \sin(x) \, dx$`, an antiderivative of `sin(x)` is needed <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. The derivative of `cos(x)` is `-sin(x)`, so the antiderivative of `sin(x)` is `-cos(x)` <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

Evaluating the definite integral:
$$ \int_0^\pi \sin(x) \, dx = [-\cos(x)]_0^\pi = (-\cos(\pi)) - (-\cos(0)) $$
$$ = (-(-1)) - (-(1)) = 1 - (-1) = 2 $$
The area under the `sin(x)` graph between 0 and π is exactly 2 <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

The average height is this area divided by the width of the interval (π):
$$ \text{Average Height} = \frac{2}{\pi} \approx 0.64 $$

## Integration and Derivative Relationship from Averaging

This problem also illuminates why [[integrals_and_derivatives | integrals and derivatives]] are inverses <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The average value, `$\frac{2}{\pi}$`, came from the change in the antiderivative (`-cos(x)`) over the input range (`$\pi - 0$`), divided by the length of that range <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. This can be seen as the rise-over-run slope between the points of the antiderivative graph at `x=0` and `x=π` <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

Since `sin(x)` is, by definition, the derivative of `-cos(x)`, it represents the slope of the antiderivative graph at every point <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Therefore, the average value of `sin(x)` can be interpreted as the average slope over all tangent lines between 0 and π <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. It makes intuitive sense that the average slope of a graph over a range equals the total slope between its start and end points <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## General Formula for Average Value of a Function

For any function `f(x)`, its average value over an interval `[a, b]` is given by:
$$ \text{Average Value} = \frac{1}{b-a} \int_a^b f(x) \, dx $$
This represents the signed area under the graph divided by its width <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

The connection to a finite average lies in approximating the integral <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. If samples are spaced by `dx`, the number of samples is approximately `$(b-a)/dx$` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Summing `f(x)` values and dividing by the number of samples is equivalent to summing `f(x) * dx` and dividing by the interval width `(b-a)` <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. The integral is the limit as `dx` approaches 0, corresponding to increasingly accurate approximations with more points <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

To evaluate the integral, an antiderivative `F(x)` of `f(x)` is found <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The integral value is `F(b) - F(a)`, which is the change in height of `F(x)` between `a` and `b` <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
Thus, the average value is `$\frac{F(b) - F(a)}{b-a}$`, which is the slope of the antiderivative graph between its two endpoints <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. This makes sense because `f(x)` is the derivative of `F(x)`, representing the slope of the tangent line to `F(x)` at every point <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

This perspective reveals that reframing the question of finding a continuous average as finding the average slope of tangent lines allows the answer to be determined by just comparing endpoints, rather than tallying all points in between <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

## When to Think of Integrals

Beyond approximating a problem by breaking it up into many small things and adding them <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>, a second key sensation that should bring integrals to mind is when you want to generalize an idea understood in a finite context (e.g., averaging numbers) to an infinite, continuous range of values <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. This feeling often arises, especially in [[integrals_and_probability_distributions | probability]], and is a useful concept to remember <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.