---
title: Calculating the average value of a continuous function
videoId: FnJqaIESC2s
---

From: [[3blue1brown]] <br/> 

Finding the average of a continuous variable is a common type of problem where [[evaluating_integrals_and_the_role_of_the_convergence_point | integration]] becomes useful <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This concept not only provides a useful tool in its own right <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, but also offers a unique perspective on why [[calculating_derivatives_and_algebraic_simplification_in_calculus | integrals and derivatives]] are inverse operations <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## The Challenge of Averaging Continuous Variables

When calculating averages, it's typical to consider a finite number of variables that can be summed and then divided by their count <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. However, with a continuous function like `sin(x)` between 0 and pi, there are infinitely many values <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It's not possible to simply add up all these numbers and divide by infinity <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

This challenge often arises in mathematics when one wants to sum infinitely many values associated with a continuum <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. In such cases, the key is almost always to use an [[evaluating_integrals_and_the_role_of_the_convergence_point | integral]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### Approximating with Finite Sums

A good initial approach to understanding how [[evaluating_integrals_and_the_role_of_the_convergence_point | integrals]] apply is to approximate the continuous situation with a finite sum <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

1.  **Sample Points**: Imagine sampling a finite number of points evenly spaced along the continuous range <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  **Calculate Finite Average**: For this finite sample, the average can be found by adding up all the function heights (e.g., `sin(x)`) at each sampled point and dividing by the total number of points <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
3.  **Improve Approximation**: As more points are sampled (adding more heights), the average of the sample should increasingly approximate the actual average of the continuous variable <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Connecting to Integrals

The concept of sampling and summing for an average shares similarities with [[evaluating_integrals_and_the_role_of_the_convergence_point | integral]] calculation <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. An [[evaluating_integrals_and_the_role_of_the_convergence_point | integral]] also considers a sample of inputs on a continuum. Instead of just adding heights and dividing by the count, an [[evaluating_integrals_and_the_role_of_the_convergence_point | integral]] sums `sin(x) * dx`, where `dx` is the spacing between samples, effectively adding little areas <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. The [[evaluating_integrals_and_the_role_of_the_convergence_point | integral]] is the limit of this sum as `dx` approaches 0 <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

To bridge the gap, the expression for the average (sum of heights / number of sampled points) can be reframed in terms of `dx` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

If the interval length is `L` (e.g., pi) and the spacing between samples is `dx`, the number of samples is approximately `L / dx` <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a> <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

When this is substituted into the average formula, and rearranged, the numerator transforms into a sum where terms look like `sin(x) * dx` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a> <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This numerator exactly resembles an [[evaluating_integrals_and_the_role_of_the_convergence_point | integral]] expression <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

For larger samples, the average approaches the [[evaluating_integrals_and_the_role_of_the_convergence_point | integral]] of the function over the interval, divided by the length of that interval <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>:

Average Height = `(Integral of f(x) from a to b) / (b - a)` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>

This can be understood as the [[area_under_a_curve_in_calculus | area under the graph]] divided by its width <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. Conceptually, area divided by width yields an average height, which is reasonable <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

## Example: Average Height of sin(x) on [0, π]

Consider finding the average height of the graph of `sin(x)` between 0 and pi <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a> <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

1.  **Find the Antiderivative**: To compute the [[evaluating_integrals_and_the_role_of_the_convergence_point | integral]], an antiderivative of `sin(x)` is needed <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
    *   The [[taking_derivatives_of_complex_combinations_of_functions | derivative]] of `cos(x)` is `-sin(x)` <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
    *   Therefore, the antiderivative of `sin(x)` is `-cos(x)` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

2.  **Evaluate the Integral**: Evaluate the antiderivative at the upper bound (`pi`) and subtract its value at the lower bound (`0`) <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
    *   `[-cos(pi)] - [-cos(0)] = [-(-1)] - [-(1)] = 1 - (-1) = 2` <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
    *   The [[area_under_a_curve_in_calculus | area under the sine graph]] from 0 to pi is exactly 2 <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

3.  **Calculate the Average Height**: Divide the [[area_under_a_curve_in_calculus | integral]] value by the width of the interval (pi - 0 = pi) <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
    *   Average Height = `2 / pi` ≈ `0.64` <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

## Integrals and Derivatives: An Inverse Relationship

Calculating the average value of a function offers insight into why [[calculating_derivatives_and_algebraic_simplification_in_calculus | integrals and derivatives]] are inverse operations <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

The average value (e.g., `2/pi`) is obtained by looking at the change in the antiderivative (`-cos(x)`) over the input range, divided by the length of that range <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. This fraction represents the "rise over run" slope between the antiderivative's values at the interval's start and end points <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Average Slope

The function `sin(x)` is, by definition, the [[taking_derivatives_of_complex_combinations_of_functions | derivative]] of its antiderivative (`-cos(x)`), representing the slope of the antiderivative graph at every point <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
Thus, the average value of `sin(x)` can be interpreted as the average slope over all tangent lines of `-cos(x)` between 0 and pi <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

> [!NOTE] Average Slope of a Function
> It makes intuitive sense that the average slope of a graph over a specific range should equal the total slope between its start and end points <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This highlights the inverse relationship between the function and its antiderivative.

### Generalizing the Concept

For any function `f(x)`, its average value on an interval `[a, b]` is given by:

`Average Value = (Integral of f(x) from a to b) / (b - a)` <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

This is the [[area_under_a_curve_in_calculus | signed area under the graph]] divided by its width <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

As `dx` approaches 0, the sum of `f(x) * dx` approximates the [[evaluating_integrals_and_the_role_of_the_convergence_point | integral]], and the division by the interval width (`b-a`) yields the true average <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

Let `F(x)` be an antiderivative of `f(x)` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The [[evaluating_integrals_and_the_role_of_the_convergence_point | integral]] from `a` to `b` is `F(b) - F(a)` <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
So, the average value becomes:

`Average Value = (F(b) - F(a)) / (b - a)` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

This expression is precisely the slope of the antiderivative graph `F(x)` between the two endpoints `a` and `b` <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. Since `f(x)` is the [[taking_derivatives_of_complex_combinations_of_functions | derivative]] of `F(x)`, `f(x)` represents the slope of the tangent line to `F(x)` at each point <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

> [!SUMMARY] Why Antiderivatives Solve Integrals
> One powerful [[intuition_behind_the_average_value_and_area_under_a_curve | intuition]] is that reframing the problem of finding the average of a continuous value as finding the average slope of tangent lines allows the answer to be found by comparing endpoints, rather than summing all intermediate points <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

### When to Think of Integrals

Integrals should come to mind in two primary scenarios:
1.  When a problem can be [[approximating_solutions_using_calculus | approximated]] by breaking it into many small parts and summing them <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
2.  When generalizing an idea from a finite context (like averaging numbers) to an infinite, continuous range of values <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. In such cases, phrasing the problem in terms of an [[evaluating_integrals_and_the_role_of_the_convergence_point | integral]] is often the solution <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. This applies frequently in fields like probability <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.