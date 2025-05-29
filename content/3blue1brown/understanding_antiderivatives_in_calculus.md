---
title: Understanding antiderivatives in calculus
videoId: FnJqaIESC2s
---

From: [[3blue1brown]] <br/> 

## Introduction to Antiderivatives and Integration

Integration is commonly used to solve problems such as finding the average of a continuous variable <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This application offers a unique perspective on why [[antiderivatives_and_their_role_in_integration | integrals]] and [[understanding_what_a_derivative_is | derivatives]] are inverse operations of each other <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

Consider the graph of `sin(x)` between `0` and `π`, which represents half of its period <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A practical question is to find the average height of this graph over that interval <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This is relevant for analyzing cyclic phenomena modeled by sine waves, such as the average effectiveness of solar panels based on the duration of daylight hours <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## The Challenge of Averaging Continuous Variables

Averaging a continuous variable is complex because there are infinitely many values within an interval <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Unlike with a finite number of variables where you sum and divide by the count, you cannot simply add up infinitely many numbers and divide by infinity <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

This intuition, where one vaguely wants to add infinitely many values associated with a continuum, often points to the need for an [[antiderivatives_and_their_role_in_integration | integral]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Approximating with Finite Sums

A helpful first step is to approximate the situation with a finite sum <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. For instance, imagine sampling a finite number of evenly spaced points along the range of `sin(x)` <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. The average can then be found by summing the heights of `sin(x)` at these points and dividing by the number of sampled points <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

Presumably, the more points sampled, the closer the average of that sample should be to the actual average of the continuous variable <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This concept is closely related to taking an [[antiderivatives_and_their_role_in_integration | integral]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Connecting Finite Sums to Integrals

When considering an [[antiderivatives_and_their_role_in_integration | integral]], like `∫sin(x) dx` from `0` to `π`, a sample of inputs is also considered <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. However, instead of adding heights, you add `sin(x)` multiplied by `dx` (the spacing between samples), which represents little areas <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. The [[antiderivatives_and_their_role_in_integration | integral]] is the value that this sum approaches as `dx` approaches `0` <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

To reframe the average (sum of heights divided by number of points) in terms of `dx`:
The number of samples in an interval of length `L` (e.g., `π`) with spacing `dx` is approximately `L / dx` <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Substituting this into the average formula:

Average ≈ `(Σ sin(x)) / (L / dx)` <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>
Average ≈ `(Σ sin(x) * dx) / L` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>

As `dx` approaches `0` (for larger and larger samples), the sum `Σ sin(x) * dx` approaches the [[antiderivatives_and_their_role_in_integration | integral]] of `sin(x)` <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Thus, the average value of a function `f(x)` over an interval `[a, b]` is given by:

> **Average Value** = `(∫[a,b] f(x) dx) / (b - a)` <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>

This means the average height of a graph is the area under the graph divided by its width <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

## Calculating the Average Using Antiderivatives

To [[computing_derivatives_of_functions | compute]] an [[antiderivatives_and_their_role_in_integration | integral]], one must find an [[antiderivatives_and_their_role_in_integration | antiderivative]] of the function inside the integral <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. An [[antiderivatives_and_their_role_in_integration | antiderivative]] of `sin(x)` is a function whose [[understanding_what_a_derivative_is | derivative]] is `sin(x)` <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

Knowing that the [[understanding_what_a_derivative_is | derivative]] of `cos(x)` is `-sin(x)`, it follows that the [[antiderivatives_and_their_role_in_integration | antiderivative]] of `sin(x)` is `-cos(x)` <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

To evaluate the [[antiderivatives_and_their_role_in_integration | integral]] of `sin(x)` between `0` and `π`:
1.  Evaluate the [[antiderivatives_and_their_role_in_integration | antiderivative]] (`-cos(x)`) at the upper bound (`π`).
2.  Subtract its value at the lower bound (`0`) <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

So, `∫[0,π] sin(x) dx = -cos(π) - (-cos(0)) = -(-1) - (-1) = 1 + 1 = 2` <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
The area under the `sin(x)` graph from `0` to `π` is `2` <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

Therefore, the average height of `sin(x)` on `[0, π]` is `2 / π`, which is approximately `0.64` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

## The Inverse Relationship Between Integrals and Derivatives

The process of finding the average value (e.g., `2 / π`) involves looking at the change in the [[antiderivatives_and_their_role_in_integration | antiderivative]] (`-cos(x)`) over the input range, divided by the length of that range <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. This fraction, `(F(b) - F(a)) / (b - a)`, is precisely the [[geometric_interpretation_of_derivatives | rise over run slope]] between the two endpoints of the [[antiderivatives_and_their_role_in_integration | antiderivative]]'s graph <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

Since `sin(x)` is the [[understanding_what_a_derivative_is | derivative]] of `-cos(x)`, `sin(x)` represents the slope of the `-cos(x)` graph at every point <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. The average value of `sin(x)` can thus be seen as the average slope of all tangent lines to the `-cos(x)` graph between `0` and `π` <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

It makes sense that the average slope of a graph over a range should equal the total slope between its start and end points <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Generalizing the Concept

For any function `f(x)`, its average value on an interval `[a, b]` is:
`Average_f = (∫[a,b] f(x) dx) / (b - a)` <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>

This represents the signed area under the graph divided by its width <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
Evaluating the [[antiderivatives_and_their_role_in_integration | integral]] involves finding an [[antiderivatives_and_their_role_in_integration | antiderivative]] of `f(x)`, commonly denoted as `F(x)` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The [[antiderivatives_and_their_role_in_integration | integral]]'s value is the change in this [[antiderivatives_and_their_role_in_integration | antiderivative]]: `F(b) - F(a)` <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

Therefore, the solution to the average value problem is:
`Average_f = (F(b) - F(a)) / (b - a)` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>

This expression is the slope of the [[antiderivatives_and_their_role_in_integration | antiderivative]] graph `F(x)` between the two endpoints <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This makes sense because `f(x)` is, by definition, the [[understanding_what_a_derivative_is | derivative]] of `F(x)` <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

## Conclusion

One intuitive reason why [[antiderivatives_and_their_role_in_integration | antiderivatives]] are crucial for solving [[antiderivatives_and_their_role_in_integration | integrals]] is that reframing the problem of finding the average of a continuous value as finding the average slope of a series of tangent lines allows the answer to be determined simply by comparing endpoints, rather than summing all intermediate points <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

> [!NOTE] When to think of [[antiderivatives_and_their_role_in_integration | integrals]]:
> If you have an idea that you understand in a finite context (e.g., averaging numbers) that involves adding multiple values, and you wish to generalize it to an infinite, continuous range of values, try to phrase it in terms of an [[antiderivatives_and_their_role_in_integration | integral]] <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. This sensation is common, especially in probability <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.