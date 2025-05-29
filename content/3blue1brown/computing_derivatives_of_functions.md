---
title: Computing derivatives of functions
videoId: S0_qX4VJhMQ
---

From: [[3blue1brown]] <br/> 

Computing derivatives is the next step after understanding what a derivative means and its connection to rates of change <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. The goal is to find a formula for a function's derivative when given its explicit formula <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This skill is crucial because many real-world phenomena analyzed with calculus are modeled by pure functions like polynomials, trigonometric functions, and exponentials <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Developing fluency with these abstract functions provides a language to discuss rates of change in concrete situations <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

However, it is easy for this process to become rote memorization of rules, leading to a loss of sight that derivatives are fundamentally about observing tiny changes in quantities and their relationship to resulting tiny changes in other quantities <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The aim is to understand these rules intuitively and [[geometric_interpretation_of_derivatives | geometrically]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>, always remembering that tiny "nudges" are at the core of derivatives <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Computing the Derivative of `x²`

Consider the function `f(x) = x²` <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. To find its derivative, `dF/dx`, one asks: if `x` is increased by a tiny amount `dx`, what is the corresponding change in `f(x)`, denoted `dF`, and what is the rate `dF/dx` <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>?

### Visualizing with Graphs
Initially, `dF/dx` can be conceptualized as the slope of the tangent line to the graph of `x²` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This slope generally increases as `x` increases, being zero at `x=0` and becoming steeper as `x` moves away from zero <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. However, relying solely on [[visualizing_derivatives_using_graphs | graphs]] is not ideal for deriving precise derivative formulas <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

### Geometric Approach
A more direct approach is to [[geometric_interpretation_of_derivatives | visualize]] `x²` as the area of a square with side length `x` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
If `x` is increased by a tiny nudge `dx`, the resulting change in the area of the square (`dF`) is visible as new bits of area <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This new area consists of:
*   Two thin rectangles, each with dimensions `x` by `dx`, totaling `2 * x * dx` in area <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   A minuscule square with dimensions `dx` by `dx`, resulting in `dx²` area <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

When considering tiny changes, any term including `dx` raised to a power greater than 1 (`dx²`, `dx³`, etc.) is considered negligibly tiny and can be ignored <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This is because such terms will not "survive" the process of letting `dx` approach zero when divided by `dx` <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

Therefore, the change in area `dF` is approximately `2x * dx` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
Dividing `dF` by `dx` yields the derivative of `x²`, which is `2x` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. This `2x` represents the rate of change of the area per unit change in `x` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Computing the Derivative of `x³`

For `f(x) = x³`, a similar [[geometric_interpretation_of_derivatives | geometric view]] can be taken <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Visualize `x³` as the volume of a cube with side length `x` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

If `x` is increased by a tiny nudge `dx`, the resulting increase in volume (dF) is primarily comprised of three square faces, each with dimensions `x` by `x` by `dx` <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>, <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. Each thin square has a volume of `x² * dx` <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. In total, this accounts for `3x² * dx` of the volume change <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. Other slivers of volume (along edges or in corners) are proportional to `dx²` or `dx³` and can be safely ignored as they are negligible <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

Thus, the derivative of `x³` – the rate at which `x³` changes per unit change of `x` – is `3x²` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. This means the slope of the graph of `x³` at any point `x` is exactly `3x²` <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. While [[visualizing_derivatives_using_graphs | graphical intuition]] helps understand the general shape of the slope, it does not provide the precise quantity `3x²` <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

## The [[power_rule_for_derivatives | Power Rule]]

The patterns observed for `x²` and `x³` extend to other polynomial terms <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   The derivative of `x⁴` is `4x³` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   The derivative of `x⁵` is `5x⁴` <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

Abstractly, the derivative of `xⁿ` for any power `n` is `n * x^(n-1)` <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. This is known as the [[power_rule_for_derivatives | power rule]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

The underlying reason for this rule is seen when nudging `x` to `x + dx` and expanding `(x + dx)ⁿ` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
The first term in the expansion is `xⁿ`, analogous to the original square's area or cube's volume <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. The next significant terms arise from choosing `n-1` `x` terms and a single `dx` from the `n` parenthetical terms <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Since there are `n` ways to choose that single `dx`, this results in `n` terms, each `x^(n-1) * dx` <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. All other terms in the expansion will be multiples of `dx²` or higher powers, which are negligible <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

Therefore, the increase in the output is negligibly approximated by `n` copies of `x^(n-1) * dx` <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This explains why the derivative of `xⁿ` is `n * x^(n-1)` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

## Derivative of `1/x` (Challenge)

Consider `f(x) = 1/x` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, which can be written as `x⁻¹` <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. Applying the [[power_rule_for_derivatives | power rule]] symbolically would yield `-1 * x⁻²` <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

Geometrically, `1/x` can be visualized as the height of a rectangle with a constant area of 1 and a width of `x` <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. If the width `x` is increased by a tiny `dx`, the height must decrease by `d(1/x)` to maintain the constant area <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. The `d(1/x)` term is negative as the height is decreasing <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

## Derivatives of Trigonometric Functions: Sine

Let's find the derivative of the sine function, `f(theta) = sin(theta)` <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

### Unit Circle Visualization
Using the unit circle, `sin(theta)` represents the height of a point after traversing an arc length `theta` (or an angle of `theta` radians) from the rightmost point <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. As `theta` increases, the height (sine value) oscillates between -1 and 1 <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

### [[visualizing_derivatives_using_graphs | Graph-based Intuition]]
The graph of `sin(theta)` is a wave pattern <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. By observing the slope of this graph:
*   At `theta = 0`, the slope is positive and increasing <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   As `sin(theta)` approaches its peak, the slope decreases to 0 <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
*   The slope becomes negative as `sin(theta)` decreases, then returns to 0 as it levels out again <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
This suggests the derivative graph might be `cosine(theta)` <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

### Precise Geometric Reasoning
To understand *why* the derivative is precisely `cosine(theta)`, one must look at the unit circle itself <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
Consider a tiny nudge `d(theta)` along the circumference of the unit circle <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. This causes a tiny change in height, `d(sin(theta))` <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. Zooming in, the arc `d(theta)` can be approximated as the hypotenuse of a tiny right triangle <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. The vertical side of this triangle represents `d(sin(theta))` <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

This tiny triangle is similar to a larger triangle formed by the radius (hypotenuse of length 1), the x-axis, and the vertical line representing `sin(theta)` <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. The angle at the origin in the tiny triangle is `theta` radians <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. The ratio of the change in height (`d(sin(theta))`) to the change in input (`d(theta)`) corresponds to the ratio of the side adjacent to angle `theta` to the hypotenuse in the tiny triangle <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>, <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. This ratio, adjacent over hypotenuse, is the definition of `cosine(theta)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. Therefore, the derivative of `sin(theta)` is `cosine(theta)` <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

## Conclusion

Understanding [[calculating_derivatives_and_their_applications | derivatives]] through geometric interpretations and the concept of "tiny nudges" helps to demystify the rules and provide a more intuitive grasp beyond mere symbolic manipulation <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. This foundational understanding is crucial for moving on to [[understanding_derivatives_of_combined_functions | derivatives of combined functions]] like sums, products, or function compositions <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.