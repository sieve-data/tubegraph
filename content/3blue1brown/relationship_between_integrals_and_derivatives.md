---
title: Relationship between integrals and derivatives
videoId: FnJqaIESC2s
---

From: [[3blue1brown]] <br/> 

[[integration_and_antiderivatives | Integration]] is a common mathematical tool used to find the average of a continuous variable <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This application provides an insightful perspective on why [[derivatives_and_integrals | integrals and derivatives are inverses]] of each other <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Finding the Average of a Continuous Function

Consider the graph of sin(x) between 0 and π, which represents half of its period <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A practical question could be, "What is the average height of this graph on that interval?" <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This is relevant for modeling cyclic phenomena, such as the average effectiveness of solar panels based on the number of daylight hours over a year <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

The challenge with finding the average of a continuous variable lies in the infinite number of values within a given range. Unlike a finite set of numbers, where you sum them and divide by their count, you cannot sum infinitely many values and divide by infinity <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

When faced with the desire to "add together infinitely many values associated with a continuum," the key is almost always to use an [[antiderivatives_and_solving_integrals | integral]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### Approximating the Average with Finite Sums

A helpful first step is to approximate the continuous situation with a finite sum <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Imagine sampling a finite number of points evenly spaced along the range from 0 to π <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. The average of this finite sample can be found by summing the heights (sin(x) at each point) and dividing by the number of sampled points <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. As more points are sampled, this approximation should get closer to the true average of the continuous variable <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

This concept is related to [[integration_and_antiderivatives | taking an integral]], where you also consider a sample of inputs on a continuum <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Instead of just adding heights, an integral adds "little areas," specifically sin(x) times `dx`, where `dx` is the spacing between samples <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. The [[integration_and_antiderivatives | integral]] is the value that this sum approaches as `dx` approaches 0 <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Deriving the Average Value Formula

To formally connect the finite average to the integral, reframe the expression for the average (sum of heights / number of sampled points) in terms of `dx`, the spacing between samples <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

If the interval length is π and the spacing is `dx`, the number of samples is approximately π / `dx` <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Substituting this into the average formula:

Average ≈ (Sum of sin(x) values) / (π / `dx`) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>

Rearranging, this becomes:

Average ≈ (Sum of (sin(x) * `dx`)) / π <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>

As the number of samples increases (i.e., `dx` approaches 0), the sum in the numerator approaches the [[integration_and_antiderivatives | integral]] of sin(x) between 0 and π <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

Therefore, the average height of a graph over an interval is:

`Average Height = (Integral of f(x) over the interval) / (Width of the interval)` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>

This means the average height is the area under the graph divided by its width <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

### Solving the Example: Average of sin(x)

To compute the [[integration_and_antiderivatives | integral]], an [[antiderivatives_and_solving_integrals | antiderivative]] of the function (sin(x)) is needed <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. The [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of cos(x) is -sin(x), so the [[antiderivatives_and_solving_integrals | antiderivative]] of sin(x) is -cos(x) <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

To evaluate the integral of sin(x) between 0 and π:
1.  Evaluate the [[antiderivatives_and_solving_integrals | antiderivative]] at the upper bound (π): -cos(π) = 1 <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
2.  Evaluate the [[antiderivatives_and_solving_integrals | antiderivative]] at the lower bound (0): -cos(0) = -1 <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
3.  Subtract the lower bound value from the upper bound value: 1 - (-1) = 2 <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

This means the area under the sine graph from 0 to π is 2 <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

The average height of sin(x) on the interval [0, π] is then:
`Average Height = Area / Width = 2 / π` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>

Which is approximately 0.64 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

## Integrals and Derivatives as Inverses

This problem illustrates an important aspect of the [[derivatives_and_integrals | relationship between integrals and derivatives]]. The process of finding the average value (2/π) involved:
1.  Looking at the change in the [[antiderivatives_and_solving_integrals | antiderivative]] (-cos(x)) over the input range [0, π] <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
2.  Dividing by the length of that range (π) <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

This fraction, `(Change in Antiderivative) / (Change in x)`, is precisely the rise-over-run slope between the starting and ending points of the [[antiderivatives_and_solving_integrals | antiderivative]] graph <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

Since sin(x) is the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of -cos(x), sin(x) gives the slope of the -cos(x) graph at every point <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Therefore, the average value of sin(x) can be thought of as the average slope over all tangent lines of the -cos(x) graph between 0 and π <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. It makes intuitive sense that the average slope of a graph over a range should equal the total slope (rise over run) between its start and end points <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Generalization

For any function `f(x)`, its average value on an interval `[a, b]` is given by:

`Average Value = (Integral of f(x) from a to b) / (b - a)` <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>

This is the signed area under the graph divided by its width <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

The connection to finite averages is maintained:
*   A finite sample's average is `(Sum of f(x) values) / (Number of samples)` <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   Number of samples ≈ `(b - a) / dx` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   Substituting yields `(Sum of (f(x) * dx)) / (b - a)` <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   As `dx` approaches 0, the sum becomes the [[integration_and_antiderivatives | integral]] <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

Evaluating the [[integration_and_antiderivatives | integral]] requires finding an [[antiderivatives_and_solving_integrals | antiderivative]] of `f(x)`, often denoted as `F(x)` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The integral's value is `F(b) - F(a)`, which represents the change in height of the [[antiderivatives_and_solving_integrals | antiderivative]] graph between the bounds <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

Thus, the average value is:

`Average Value = (F(b) - F(a)) / (b - a)` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>

This is the slope of the [[antiderivatives_and_solving_integrals | antiderivative]] graph between the two endpoints <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. Since `f(x)` is the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of `F(x)` by definition, `f(x)` gives the slope of the tangent line to `F(x)` at each point <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. This perspective highlights why [[antiderivatives_and_solving_integrals | antiderivatives]] are crucial for solving [[integration_and_antiderivatives | integrals]]: reframing the question of finding an average as finding the average slope allows the answer to be found by comparing only the endpoints of the [[antiderivatives_and_solving_integrals | antiderivative]] graph <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

## When to Think of Integrals

Two key "sensations" should bring [[integration_and_antiderivatives | integrals]] to mind:
1.  If a problem can be approximated by breaking it into small pieces and summing them up <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
2.  If an idea understood in a finite context (like averaging numbers) needs to be generalized to an infinite, continuous range of values <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. In such cases, phrasing the problem in terms of an [[integration_and_antiderivatives | integral]] is often the solution <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. This is particularly common in probability <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.