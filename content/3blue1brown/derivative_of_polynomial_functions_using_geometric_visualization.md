---
title: Derivative of polynomial functions using geometric visualization
videoId: S0_qX4VJhMQ
---

From: [[3blue1brown]] <br/> 

Learning to compute derivatives for functions with explicit formulas is a crucial step in calculus <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This skill is important because many real-world phenomena are modeled using polynomial, trigonometric, and exponential functions <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Fluency with the rates of change for these pure abstract functions provides a language to discuss changes in concrete situations <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

It is easy for this process to feel like mere memorization of rules, potentially leading to a loss of sight that [[derivatives_and_integrals | derivatives]] are fundamentally about tiny changes in quantities <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This article aims to show how to think about some of these rules intuitively and [[geometric_interpretation_of_derivatives | geometrically]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Derivative of f(x) = x²

To find the derivative of a simple function like `f(x) = x²`, we ask: if `x` changes by a tiny `dx`, what is the corresponding change in the function's value, `dF`? <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a> Specifically, we want `dF` divided by `dx`, which represents the rate of change of the function per unit change in `x` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

While `dF/dx` can be thought of as the slope of a tangent line to the graph of `x²` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>, observing the graph isn't the best way to understand the precise formula for a derivative <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

Instead, we can visualize `x²` as the area of a square with side length `x` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. If `x` is increased by a tiny nudge `dx`, the resulting change in the square's area (`dF`) is visible <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

The new area consists of three parts <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>:
*   Two thin rectangles, each with dimensions `x` by `dx`, contributing `2 * x * dx` to the new area <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   One minuscule square with dimensions `dx` by `dx`, contributing `dx²` to the new area <a class="yt="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

When dealing with tiny changes, any term that includes `dx` raised to a power greater than 1 (like `dx²`) can be considered negligibly tiny <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

This leaves us with `dF = 2x * dx` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Therefore, the derivative of `x²` is `dF/dx = 2x` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. This means that if `x` was 3, the rate of change in area per unit change in length would be `2 * 3 = 6` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

## Derivative of f(x) = x³

Similarly, for `f(x) = x³`, we can visualize it as the volume of a cube with side length `x` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. When `x` is increased by a tiny nudge `dx`, the resulting increase in volume (dF) can be seen <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

Almost all of this new volume comes from three square faces <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. Each of these thin squares has a volume of `x² * dx` (area of the face times the thickness `dx`) <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. So, in total, this accounts for `3x² * dx` of volume change <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

Other slivers of volume (along the edges and in the corner) are proportional to `dx²` or `dx³`, which can be safely ignored because they are negligible when `dx` approaches 0 <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

Thus, the derivative of `x³` (the rate at which `x³` changes per unit change of `x`) is `3x²` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. This means the slope of the graph of `x³` at any point `x` is `3x²` <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

## The Power Rule

The patterns observed for `x²` and `x³` generalize to what is known as the [[power_rule_in_calculus_and_its_geometric_significance | power rule]] <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>:
$$
\frac{d}{dx}(x^n) = nx^{n-1}
$$
This means that the derivative of `x⁴` is `4x³`, and the derivative of `x⁵` is `5x⁴`, and so on <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

Intuitively, when you nudge `x` slightly to `x + dx`, the output `(x + dx)^n` involves multiplying `n` separate `(x + dx)` terms <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
The full expansion is complicated, but the most significant terms for the derivative are those that involve `dx` to the first power <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
The initial term in the expansion is `xⁿ` <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. The next terms in the expansion arise from choosing mostly `x`'s with a single `dx` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Since there are `n` different parentheticals from which you could choose that single `dx`, this results in `n` separate terms, each of which is `x^(n-1) * dx` <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
All other terms in the expansion will be multiples of `dx²` or higher powers of `dx`, which are negligible <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
Therefore, almost all the increase in the output `dF` comes from `n` copies of `x^(n-1) * dx` <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This is precisely why the derivative of `xⁿ` is `nx^(n-1)` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

Although this rule often becomes a symbolic "exponent hopping down" in practice, understanding the underlying geometric reasoning reinforces the concept of [[derivatives_of_simple_functions_and_their_intuition | derivatives]] as tiny nudges <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

## Challenge: Derivative of f(x) = 1/x

Consider the function `f(x) = 1/x`, which can also be written as `x⁻¹` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. While the [[power_rule_in_calculus_and_its_geometric_significance | power rule]] could be applied directly (the derivative would be `(-1) * x⁻²`), let's think about this geometrically <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

Visualize `1/x` as the height of a rectangle with a constant area of 1 and a width of `x` <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. If `x` increases by a tiny `dx`, how must the height (`1/x`) change to keep the area constant at 1? <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>
This involves the height decreasing (a negative `d(1/x)`) to compensate for the area gained by the increase in width <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

> [!challenge] Pause and Ponder
> Work out the expression for `d(1/x)` divided by `dx` based on this geometric reasoning, and compare it to the result from applying the power rule symbolically <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

> [!challenge] Another Challenge
> Try to reason through what the derivative of the square root of `x` should be using a similar approach <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

Further topics include [[derivative_of_trigonometric_functions_with_unit_circle_analysis | derivatives of trigonometric functions]] and [[derivatives_of_exponential_functions | exponential functions]], which also benefit from [[visualization_in_calculus | visualization]] <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. The next video will discuss [[taking_derivatives_of_complex_combinations_of_functions | taking derivatives of complex combinations of functions]] such as sums, products, and function compositions <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.