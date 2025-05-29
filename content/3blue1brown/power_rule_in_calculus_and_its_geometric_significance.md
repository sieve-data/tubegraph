---
title: Power rule in calculus and its geometric significance
videoId: S0_qX4VJhMQ
---

From: [[3blue1brown]] <br/> 

Computing derivatives of functions with explicit formulas is a fundamental step in calculus, especially for understanding real-world phenomena often modeled by polynomials, trigonometric functions, and exponentials <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. While the process can sometimes feel like rote memorization <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, it's crucial to remember that derivatives are fundamentally about analyzing how tiny changes in one quantity relate to resulting tiny changes in another <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This article, part of an [[introduction_to_calculus_series | Introduction to Calculus series]], aims to explore some key derivative rules intuitively and [[geometric_interpretation_of_derivatives | geometrically]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Deriving the Power Rule Geometrically

The [[Power rule in calculus and its geometric significance | Power Rule]] is a cornerstone for finding derivatives of polynomial terms. We can understand this rule deeply through [[geometric_interpretation_of_derivatives | geometric visualization]].

### Derivative of x²

Consider the function `f(x) = x²` <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. If we want to find its derivative, `dF/dx`, we are looking for the rate at which the function changes per unit change in `x` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. While `dF/dx` can be visualized as the slope of the tangent line to the graph of `x²` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>, a more precise understanding comes from a direct look at what `x²` represents: the area of a square with side length `x` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

If we increase `x` by a tiny nudge, `dx`, the resulting change in the area of that square (`dF`) can be seen by observing the new bits of area added <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>:
*   Two thin rectangles, each with side lengths `x` and `dx`. Their combined area is `2 * x * dx` <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   A minuscule square with area `dx²` <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

> [!NOTE] Negligible Terms
> When `dx` is a truly tiny amount, any term containing `dx` raised to a power greater than 1 (like `dx²` or `dx³`) becomes negligibly small and can be ignored <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. For example, if `dx = 0.01`, then `dx² = 0.0001`, which is much smaller <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

Ignoring the `dx²` term, the total change in area `dF` is approximately `2x * dx` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Therefore, the derivative `dF/dx` is `2x` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. This means for `x=3`, the rate of change is `6` <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, and for `x=5`, it is `10` <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### Derivative of x³

Similarly, consider `f(x) = x³` <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. We can visualize this as the volume of a cube with side length `x` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. When `x` is increased by a tiny `dx`, the resulting increase in volume comes almost entirely from three square faces <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

Each of these thin squares has a volume of `x² * dx` (area of the face times the thickness `dx`) <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. In total, this contributes `3x² * dx` to the volume change <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. Other slivers of volume (along the edges or in the corner) are proportional to `dx²` or `dx³`, which can be ignored because they are negligible when `dx` approaches zero <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

Thus, the derivative of `x³` is `3x²` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. This precisely explains why the slope of the graph of `x³` at any point `x` is `3x²` <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### The General Power Rule (xⁿ)

The patterns observed for `x²` and `x³` generalize into the [[Power rule in calculus and its geometric significance | Power Rule]] <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>:
*   The derivative of `x⁴` is `4x³` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   The derivative of `x⁵` is `5x⁴` <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

Abstractly, the derivative of `xⁿ` for any power `n` is `n * x^(n-1)` <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. This is often thought of symbolically as the exponent "hopping down" in front, leaving behind one less than itself <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

The geometric intuition behind this general rule involves considering the expansion of `(x + dx)ⁿ` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>:
*   The first term is `xⁿ`, analogous to the original square's area or cube's volume <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
*   The terms contributing to the significant change are those where a single `dx` is chosen from the `n` parenthetical `(x + dx)` terms, while the rest are `x` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   Since there are `n` ways to choose that single `dx`, this gives `n` separate terms, each being `x^(n-1) * dx` <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   This sum, `n * x^(n-1) * dx`, accounts for the majority of the increase in the output <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   All other terms in the expansion will be proportional to `dx²` or higher powers of `dx`, making them negligible <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

This explains why the derivative of `xⁿ` is `n * x^(n-1)` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Remembering these geometric underpinnings reinforces that calculus rules are logical, not just formulas to memorize <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

### Challenge: Derivative of 1/x

Consider the function `f(x) = 1/x`, which can also be written as `x⁻¹` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. While the [[Power rule in calculus and its geometric significance | Power Rule]] can be blindly applied (`-1 * x⁻²`) <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>, let's explore its [[geometric_interpretation_of_derivatives | geometric interpretation]].

Imagine a rectangle with an area of 1, a width of `x`, and thus a height of `1/x` <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. This visual represents the relationship between `x` and `1/x` <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

> [!TIP] Pause and Ponder
> If you nudge `x` by a tiny `dx`, how must the height of this rectangle change (let's call it `d(1/x)`, which will be negative as the height decreases) so that the total area of the puddle remains constant at 1? <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a> Use this visual to work out the expression for `d(1/x) / dx` and compare it to the result from the [[Power rule in calculus and its geometric significance | Power Rule]] <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

### Beyond the Power Rule: Derivative of Sine

Even for non-polynomial functions, [[visualization_in_calculus | visualization]] provides intuition. For `f(theta) = sin(theta)`, using the unit circle:
*   `sin(theta)` represents the height of a point on the unit circle after traversing an arc length `theta` <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
*   When `theta` is nudged by `d(theta)` along the circumference <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>, the change in height `d(sin(theta))` can be viewed as one side of a tiny right triangle <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   This tiny triangle is similar to a larger triangle within the unit circle, whose hypotenuse is the radius (length 1) and whose angle is `theta` <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   The ratio `d(sin(theta)) / d(theta)` (tiny change in height divided by tiny change in input) corresponds to the ratio of the adjacent side to the hypotenuse in this tiny triangle <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   By the definition of cosine, this ratio is `cos(theta)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

Thus, the derivative of `sin(theta)` is `cos(theta)` <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. This geometric reasoning provides a precise explanation beyond merely observing the graph's slope <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.

Understanding derivatives through "tiny nudges" and their [[geometric_interpretation_of_derivatives | geometric interpretation]] is invaluable, even when applying symbolic rules <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. The next video in this series will explore how to combine simple functions using rules like the Product Rule and Chain Rule, also through a geometric lens <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.