---
title: Concept of sample approximation in integration
videoId: FnJqaIESC2s
---

From: [[3blue1brown]] <br/> 

Integration is commonly used to find the average of a continuous variable <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This application provides an alternative perspective on why [[relationship_between_integrals_and_derivatives | integrals and derivatives]] are inverse operations <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## The Challenge of Averaging Continuous Variables

When considering the average of a continuous variable, such as the average height of the `sin(x)` graph between 0 and pi, a unique challenge arises <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Unlike discrete variables where a finite number of values can be added and divided by their count, continuous variables involve infinitely many values <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It's not possible to simply sum these infinite values and divide by infinity <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

This "sensation" of wanting to add together infinitely many values associated with a continuum frequently occurs in mathematics <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. In such cases, the solution almost always involves using an integral <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Approximating with Finite Samples

To approach this problem, a good first step is to [[approximations and limits in geometry | approximate]] the situation with a finite sum <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This involves sampling a finite number of evenly spaced points along the continuous range <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. For this finite sample, the average can be found by summing the heights (`sin(x)`) at each point and dividing by the number of sampled points <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

The premise is that as more points are sampled (increasing the sum of heights), the average of that sample should progressively get closer to the true average of the continuous variable <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Connecting to Integrals

This concept is inherently related to taking an integral <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. An integral also considers a sample of inputs on a continuum, but instead of adding just the height, it adds the height multiplied by `dx` (the spacing between samples), effectively summing little areas <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Technically, an integral is the limit of this sum as `dx` approaches zero <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

To transform the finite average sum into an integral, the expression for the average (sum of heights divided by number of sampled points) is reframed in terms of `dx` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
If the spacing between points is `dx`, and the interval length is `L` (e.g., pi for `sin(x)` from 0 to pi), then the number of samples (`n`) is approximately `L / dx` <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

Substituting `n = L / dx` into the average formula:
$$ \text{Average} \approx \frac{\sum \text{heights}}{n} = \frac{\sum \text{heights}}{L / \text{dx}} = \frac{1}{L} \sum (\text{heights} \cdot \text{dx}) $$

As `dx` approaches 0 (i.e., for larger and larger samples), the sum of `heights * dx` terms becomes an integral expression <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This means the average approaches the integral of the function over the interval, divided by the length of that interval <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

For example, the average height of `sin(x)` between 0 and pi is its integral between 0 and pi, divided by pi <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. This can be intuitively understood as area divided by width yields average height <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. The integral of `sin(x)` from 0 to pi is 2 <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>, so the average height is `2/pi`, approximately 0.64 <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

## General Formula for Average Value

For any function `f(x)`, its average value on an interval between `a` and `b` is given by:
$$ \text{Average Value} = \frac{1}{b-a} \int_{a}^{b} f(x) \, dx $$
This represents the signed area under the graph divided by its width <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

## Intuition and Relation to Derivatives

This concept offers an alternate perspective on why [[integrals and derivatives | integrals and derivatives]] are inverse operations <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Computing the average value involves finding the change in the antiderivative of the function over the input range, divided by the length of that range <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. This fraction (`rise over run`) represents the slope between the points of the antiderivative graph at the interval's bounds <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

Since the original function `f(x)` is the derivative of its antiderivative `F(x)`, `f(x)` gives the slope of the tangent line to `F(x)` at every point <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Therefore, the average value of `f(x)` can be seen as the average slope over all tangent lines within the interval <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. It logically follows that the average slope of a graph over a range should equal the total slope between its start and end points <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

In summary, when calculating the average of a continuous value, reframing it as finding the average slope of many tangent lines allows the answer to be determined by comparing endpoints of the antiderivative, rather than summing all intermediate points <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

## When to Think of Integrals

Integrals should come to mind in two main scenarios:
1.  When a problem can be [[visualizing_integration_and_approximations | approximated]] by breaking it up and adding a large number of small things <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
2.  When generalizing an idea understood in a finite context (like taking an average of numbers) to an infinite, continuous range of values <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. This sensation is particularly common in [[integrals and probability distributions | probability]] <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.