---
title: Intuition behind the average value and area under a curve
videoId: FnJqaIESC2s
---

From: [[3blue1brown]] <br/> 

Integration is commonly used to solve problems involving the average of a continuous variable <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Understanding this application can provide a fresh [[mathematical_intuition_versus_analysis | perspective]] on why integrals and [[Derivatives of simple functions and their intuition | derivatives]] are inverse operations of each other <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Finding the Average of a Continuous Variable

Consider the graph of sin(x) between 0 and pi, which represents half of its period <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A natural question to ask is: what is the average height of this graph over that interval? <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>

This is a practical question, as many cyclic phenomena, such as the number of daylight hours over a year, can be modeled using sine waves <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a> <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. For instance, determining the average effectiveness of solar panels during summer versus winter months would require finding the average value of a sine function over a specific period <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a> <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. While real-world examples might involve additional constants, the fundamental approach remains the same <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a> <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a> <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### The Challenge of Averaging Continuous Variables

Calculating the average of a continuous variable presents a unique challenge <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a> <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Unlike discrete variables, where you sum a finite number of values and divide by their count, there are infinitely many values of sin(x) between 0 and pi <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a> <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It's not possible to simply add them all up and divide by infinity <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

> [!NOTE] When to use an integral
> A common sensation in mathematics is the desire to "add together infinitely many values associated with a continuum" where a simple summation doesn't make sense <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a> <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a> <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. In almost all such cases, the solution involves using an integral <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Approximating the Average with Finite Sums

A good first step to understand how integrals apply is to approximate the situation with a finite sum <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a> <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

Imagine sampling a finite number of evenly spaced points along the range [0, pi] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. For this finite sample, the average can be found by summing the heights of sin(x) at each point and dividing by the number of sampled points <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a> <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. The more points sampled, the closer this finite average will be to the true average of the continuous variable <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a> <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a> <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a> <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

This concept feels related to taking an integral of sin(x) between 0 and pi <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a> <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. For an integral, you also consider a sample of inputs, but instead of adding heights, you add `sin(x) * dx`, where `dx` is the spacing between samples <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a> <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a> <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. This means you are adding up small areas, not just heights <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a> <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. The integral is the limit of this sum as `dx` approaches zero <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a> <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a> <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Reframing the Average in Terms of `dx`

To connect the average to the integral, reframe the expression for the average (sum of heights / number of sampled points) in terms of `dx` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a> <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a> <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

If the interval length is `pi` and the spacing between samples is `dx`, the number of samples is approximately `pi / dx` <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a> <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a> <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a> <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a> <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a> <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a> <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Substituting this into the average formula:

Average ≈ (Sum of `sin(x)`) / (`pi / dx`) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a> <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>

Rearranging, this becomes:

Average ≈ (Sum of `sin(x) * dx`) / `pi` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a> <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a> <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a> <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>

As the number of samples increases (i.e., `dx` approaches 0), the sum of `sin(x) * dx` approaches the integral of sin(x) between 0 and pi <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a> <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a> <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

Therefore, the average height of the graph is given by the [[area_under_a_curve_in_calculus | integral]] of sin(x) between 0 and pi, divided by the length of the interval, pi <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a> <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a> <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. This intuitively makes sense: [[area_under_a_curve_in_calculus | area]] divided by width yields an average height <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a> <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a> <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

## Solving the Example: Average Height of sin(x)

To compute the integral of sin(x), an antiderivative is needed – a function whose derivative is sin(x) <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a> <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Since the derivative of cos(x) is -sin(x), the antiderivative of sin(x) is -cos(x) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a> <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a> <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a> <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

To evaluate the integral between 0 and pi, evaluate the antiderivative at the upper bound and subtract its value at the lower bound <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a> <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a> <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
<a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>
Integral = `-cos(pi) - (-cos(0))`
Integral = `-(-1) - (-1)`
Integral = `1 + 1 = 2` <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>

The [[area_under_a_curve_in_calculus | area under]] the sine graph from 0 to pi is exactly 2 <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a> <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a> <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

Therefore, the average height is the integral divided by the width of the region:
Average Height = `2 / pi` ≈ `0.64` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a> <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a> <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

## Integrals as the Average Slope

Finding the average value (2/pi) involved examining the change in the antiderivative (-cos(x)) over the input range, divided by the length of that range <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a> <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a> <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a> <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a> <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. This fraction can be interpreted as the "rise over run" slope between the antiderivative graph's points at 0 and pi <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a> <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

Since sin(x) is, by definition, the derivative of its antiderivative (-cos(x)), it represents the slope of -cos(x) at every point <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a> <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a> <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. Therefore, the average value of sin(x) can be seen as the average slope of all tangent lines to the -cos(x) graph between 0 and pi <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a> <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

It makes intuitive sense that the average slope of a graph over a certain range should equal the total slope (change in y / change in x) between the start and end points <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a> <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a> <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a> <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

### General Formula for Average Value

For any function f(x), its average value over an interval [a, b] is given by the integral of f(x) over that interval, divided by the width of the interval (b - a) <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a> <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a> <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a> <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. This represents the signed [[area_under_a_curve_in_calculus | area under]] the graph divided by its width <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a> <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a> <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

```
Average Value of f(x) = (∫[a,b] f(x) dx) / (b - a)
```

This formula connects to the finite average notion by recognizing that:
- A sample of points spaced by `dx` means the number of samples is approximately `(b - a) / dx` <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a> <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a> <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
- Summing `f(x)` at each sample and dividing by the number of samples is equivalent to summing `f(x) * dx` and dividing by the total interval width `(b - a)` <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a> <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a> <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
- The integral is the limit as `dx` approaches 0, representing an increasingly accurate approximation of the true average <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a> <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a> <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

To evaluate any integral, an antiderivative of f(x), denoted F(x), is found <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a> <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. The integral's value is the change in this antiderivative between `a` and `b`, i.e., `F(b) - F(a)` <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a> <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

Thus, the average value is the change in the antiderivative's height (`F(b) - F(a)`) divided by the change in the x-value (`b - a`) <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a> <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. This is precisely the slope of the antiderivative graph between the two endpoints <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a> <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. This relationship makes sense because `f(x)` is the derivative of `F(x)`, giving the slope of the tangent line to `F(x)` at each point <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a> <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a> <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

## Conclusion

Understanding the [[Calculating the average value of a continuous function | average value of a continuous function]] provides a powerful [[visual_intuition_in_calculus | visual intuition]] into the inverse relationship between integrals and derivatives <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a> <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. By reframing the problem as finding the average slope of many tangent lines, the solution can be seen by simply comparing the endpoints of the antiderivative, rather than needing to sum infinitely many points <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a> <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a> <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

This concept highlights a key "sensation" in calculus: if an idea is understood in a finite context involving summing multiple values (like finding an average) and needs to be generalized to an infinite, continuous range of values, try phrasing it in terms of an integral <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a> <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a> <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a> <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a> <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a> <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a> <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. This approach is frequently used, especially in probability, for [[approximating_solutions_using_calculus | approximating solutions]] and solving [[application_of_integrals_in_real_world_problems | real-world problems]] <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a> <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.