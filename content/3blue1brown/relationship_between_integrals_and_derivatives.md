---
title: Relationship between integrals and derivatives
videoId: FnJqaIESC2s
---

From: [[3blue1brown]] <br/> 

## Finding the Average of a Continuous Variable

One common application of [[integrals_and_derivatives | integration]] is finding the average of a continuous variable <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This concept not only has practical uses but also provides a unique perspective on why [[integrals_and_derivatives | integrals and derivatives]] are inverse operations <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

Consider the graph of `sin(x)` between 0 and pi, which represents half of its period <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A practical question might be: What is the average height of this graph over that interval? <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a> This is relevant for modeling cyclic phenomena, such as the average effectiveness of solar panels during different seasons, as the hours of daylight follow a sine wave pattern <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### The Challenge of Averaging Continuous Values

Calculating the average of a continuous variable presents a challenge because there are infinitely many values within a given range <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. Unlike finite sets where values can be added up and divided by the count, one cannot simply add up infinitely many values and divide by infinity <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. This situation often indicates that an [[integrals_and_derivatives | integral]] is needed <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.

## Approximating with Finite Sums

To approach this, one can approximate the continuous average by sampling a finite number of points evenly spaced along the range <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. The average of this finite sample can be found by adding up the heights of `sin(x)` at each sampled point and dividing by the number of points <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. As more points are sampled, the approximation gets closer to the actual average of the continuous variable <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.

This process is closely related to taking an [[integrals_and_derivatives | integral]] <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. In an [[integrals_and_derivatives | integral]], instead of just adding heights, one adds `sin(x)` multiplied by `dx`, where `dx` is the spacing between samples, effectively adding up small areas <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. The [[integrals_and_derivatives | integral]] itself is the limit of this sum as `dx` approaches zero <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.

To connect the finite average to the [[integrals_and_derivatives | integral]], the expression for the average (sum of heights divided by the number of points) can be reframed in terms of `dx` <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. If the spacing between points is `dx` and the interval length is `pi`, the number of samples is approximately `pi / dx` <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.

Substituting this into the average formula:
Average `≈ (Σ heights) / (pi / dx)` <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>
Rearranging: Average `≈ (Σ heights * dx) / pi` <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>

As the sample size increases (i.e., `dx` approaches 0), the sum `Σ heights * dx` approaches the [[integrals_and_derivatives | integral]] of `sin(x)` between 0 and pi <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.

Therefore, the average height of the graph is given by the [[integrals_and_ их role in integration | integral]] of the function over the interval, divided by the length of that interval <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>:

Average Value = `(∫ f(x) dx) / (b - a)` <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>

This can be intuitively understood as the area under the graph divided by its width <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.

### Solving the Example: Average Height of sin(x)

To compute the [[integrals_and_derivatives | integral]], one needs to find an [[antiderivatives_and_their_role_in_integration | antiderivative]] of `sin(x)` <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. Since the [[computing_derivatives_of_functions | derivative]] of `cos(x)` is `-sin(x)`, the [[antiderivatives_and_their_role_in_integration | antiderivative]] of `sin(x)` is `-cos(x)` <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.

To evaluate the [[integrals_and_derivatives | integral]] of `sin(x)` between 0 and pi, evaluate the [[antiderivatives_and_their_role_in_integration | antiderivative]] at the upper bound (pi) and subtract its value at the lower bound (0) <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>:

`[-cos(pi)] - [-cos(0)] = [1] - [-1] = 2` <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>

So, the area under the `sin(x)` graph from 0 to pi is 2 <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.

The average height is this [[integrals_and_derivatives | integral]] value divided by the width of the region (`pi`):
Average Height = `2 / pi ≈ 0.64` <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.

## The Inverse Relationship: Integrals and Derivatives

This method for finding the average value provides an alternative perspective on why [[integrals_and_derivatives | integrals and derivatives]] are inverses <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>. The average value is the change in the [[antiderivatives_and_their_role_in_integration | antiderivative]] (e.g., `-cos(x)`) over the input range, divided by the length of that range <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>.

This can be expressed as:
Average Value = `(F(b) - F(a)) / (b - a)` <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>, where `F(x)` is the [[antiderivatives_and_their_role_in_integration | antiderivative]] of `f(x)`.

This formula represents the "rise over run" slope of the [[antiderivatives_and_their_role_in_integration | antiderivative]] graph between the two endpoints (`a` and `b`) <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.

Since `f(x)` (the original function, like `sin(x)`) is, by [[derivative_definitions_and_their_relation_to_limits | definition]], the [[calculating_derivatives_and_their_applications | derivative]] of `F(x)` (the [[antiderivatives_and_their_role_in_integration | antiderivative]]), `f(x)` gives the [[geometric_interpretation_of_derivatives | slope]] of `F(x)` at every point <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. Therefore, the average value of `f(x)` can be interpreted as the average [[geometric_interpretation_of_derivatives | slope]] over all tangent lines of `F(x)` between 0 and pi <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a>.

It makes sense that the average [[geometric_interpretation_of_derivatives | slope]] of a graph over a certain range should equal the total [[geometric_interpretation_of_derivatives | slope]] between the start and end points <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>. This highlights how the area under one graph (calculated by an [[integrals_and_derivatives | integral]]) is directly related to the [[geometric_interpretation_of_derivatives | slope]] of another graph (its [[antiderivatives_and_their_role_in_integration | antiderivative]]), illustrating the fundamental inverse relationship between [[integrals_and_derivatives | integration]] and [[calculating_derivatives_and_their_applications | differentiation]] <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.

### Key Takeaway

A valuable intuition for when to use [[integrals_and_derivatives | integrals]] arises in two scenarios:
1.  When a problem can be approximated by breaking it into smaller parts and summing many small things <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.
2.  When generalizing an idea understood in a finite context (like averaging multiple values) to an infinite, continuous range of values <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>. This feeling comes up frequently, particularly in [[integrals_and_probability_distributions | probability]] <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>.