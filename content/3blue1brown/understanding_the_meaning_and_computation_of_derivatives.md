---
title: Understanding the meaning and computation of derivatives
videoId: S0_qX4VJhMQ
---

From: [[3blue1brown]] <br/> 

After understanding what a derivative means and its connection to rates of change, the next step in calculus is to learn how to compute them for functions with explicit formulas <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Why Compute Derivatives?

A significant portion of a calculus student's time is dedicated to grappling with derivatives of abstract functions, rather than solely focusing on concrete rate-of-change problems <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This is because many real-world phenomena are modeled using fundamental pure functions like polynomials, trigonometric functions, and exponentials <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Developing fluency in computing rates of change for these abstract functions provides a language to discuss changes in concrete situations that calculus is used to model <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

It is crucial to remember that derivatives are fundamentally about observing tiny changes in one quantity and how they relate to a resulting tiny change in another <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This concept of "tiny nudges" is at the heart of derivatives and should not be lost when learning computational rules <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## [[derivatives_of_simple_functions_and_their_intuition | Derivatives of Simple Functions: Geometric Intuition]]

To intuitively and [[geometric_interpretation_of_derivatives | geometrically understand]] derivative rules, consider the fundamental meaning of a derivative: the ratio of the corresponding change in the function's value (dF) to a tiny change in its input (dx) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This ratio, dF/dx, represents the rate at which the function changes per unit change in its input <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### The Power Rule

The power rule is a common pattern for polynomial terms <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>: the derivative of x to the power of n (`x^n`) is `n * x^(n-1)` <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. This rule often feels like a symbolic manipulation (exponent hops down, leaving one less than itself) <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>, but it has a strong geometric foundation.

#### Example: `f(x) = x^2`

The derivative of `f(x) = x^2` can be visualized using a square with side length `x` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. If `x` is increased by a tiny amount `dx`, the resulting change in the area of the square (dF) consists of three new parts <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>:
*   Two thin rectangles, each with dimensions `x` by `dx`, totaling `2 * x * dx` in area <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   One minuscule square with dimensions `dx` by `dx`, totaling `dx^2` in area <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

Since `dx` is infinitesimally tiny, `dx^2` is negligibly tiny and can be ignored (a tiny change squared is a negligible change) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Therefore, the change in area `dF` is approximately `2x * dx` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Dividing by `dx` gives the derivative: `dF/dx = 2x` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

#### Example: `f(x) = x^3`

Similarly, the derivative of `f(x) = x^3` can be visualized as the volume of a cube with side length `x` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. When `x` is increased by a tiny `dx`, the resulting increase in volume (dF) is primarily from three square faces <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Each of these thin squares has a volume of `x^2 * dx` <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. Thus, the total volume change is approximately `3x^2 * dx` <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. Other slivers of volume along edges and in the corner are proportional to `dx^2` or `dx^3` and can be ignored <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Dividing by `dx`, the derivative of `x^3` is `3x^2` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. This aligns with what was previously covered algebraically in [[calculating_derivatives_and_algebraic_simplification_in_calculus | calculating derivatives]] <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

#### Generalizing `x^n`

When the input `x` is nudged to `x + dx`, calculating `(x + dx)^n` involves multiplying `n` terms of `(x + dx)` <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. The expansion yields `x^n` as the first term, analogous to the original area or volume <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. The next significant terms come from choosing mostly `x`'s with a single `dx` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Since there are `n` places to choose that single `dx`, this results in `n` terms, each with `x^(n-1) * dx` <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. All other terms in the expansion will be multiples of `dx^2` or higher powers of `dx`, which can be ignored because they are negligible <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. Therefore, the increase in output is approximately `n * x^(n-1) * dx`, meaning the derivative of `x^n` is `n * x^(n-1)` <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

> [!challenge] Challenge 1: `f(x) = 1/x`
> The function `f(x) = 1/x` can be written as `x^-1` <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. You can try to apply the power rule symbolically, where the exponent `-1` hops down and leaves `-2` as the new exponent <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
>
> Alternatively, visualize `1/x` as the height of a rectangle with area 1 and width `x` <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. If `x` is nudged by `dx`, how must the height `1/x` change (d(1/x)) to keep the area constant at 1 <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>? The increase in width `dx` adds new area, so the height must decrease <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. Reason out the expression for `d(1/x) / dx` geometrically and compare it to the result from the power rule <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

> [!challenge] Challenge 2: `f(x) = sqrt(x)`
> Try to reason through the derivative of the square root of `x` (`x^(1/2)`) using a similar geometric approach <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

## [[derivatives_of_simple_functions_and_their_intuition | Derivatives of Trigonometric Functions]]

### Example: `f(x) = sin(x)`

For `f(x) = sin(x)`, assuming familiarity with the unit circle, `sin(theta)` represents the height of a point after traversing an arc length `theta` on a unit circle <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

#### Graphical Intuition
Looking at the graph of `sin(theta)`:
*   The slope at `theta = 0` is positive <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   As `theta` approaches its peak, the slope goes to 0 <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   The slope becomes negative while `sin(theta)` is decreasing <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
*   The slope returns to 0 as the graph levels out <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
This pattern suggests that the derivative of `sin(theta)` is `cos(theta)` <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

#### Geometric Intuition (Unit Circle)
For a more precise understanding, consider a tiny nudge `d(theta)` along the circumference of the unit circle <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. This tiny step changes the height, `d(sin(theta))` <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

Zooming in, the circle segment appears as a straight line. This creates a tiny right triangle where:
*   The hypotenuse is `d(theta)` (the tiny arc length) <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
*   The vertical side is `d(sin(theta))` (the change in height) <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
This tiny triangle is similar to the larger triangle formed by the angle `theta`, with a hypotenuse of 1 (the radius of the unit circle) <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. The angle in the tiny triangle corresponding to `theta` is also `theta` <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

The derivative `d(sin(theta))/d(theta)` is the ratio of the side adjacent to `theta` (which is `d(sin(theta))`) divided by the hypotenuse (`d(theta)`) in the tiny triangle <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. From trigonometry, "adjacent divided by hypotenuse" is the definition of `cos(theta)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. Thus, the derivative of `sin(theta)` is precisely `cos(theta)` <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

> [!challenge] Challenge 3: `f(x) = cos(x)`
> Apply a similar line of reasoning using the unit circle to find the derivative of `cos(theta)` <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

## Next Steps

The next stage of learning about derivatives involves understanding how to take derivatives of functions that combine these simple functions, such as sums, products, or function compositions <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. This includes topics like [[understanding_the_sum_rule_for_derivatives | the Sum Rule]] and [[understanding_the_chain_rule_for_function_composition_in_derivatives | the Chain Rule]] <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. The goal remains to understand each rule [[geometric_interpretation_of_derivatives | geometrically]] and intuitively <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.