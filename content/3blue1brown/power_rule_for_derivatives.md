---
title: Power rule for derivatives
videoId: S0_qX4VJhMQ
---

From: [[3blue1brown]] <br/> 

## Computing Derivatives: An Overview
Once the meaning of a derivative and its connection to rates of change are understood, the next step is to learn how to [[computing_derivatives_of_functions | compute these derivatives]] for functions with explicit formulas <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This skill is crucial because many real-world phenomena analyzed with calculus are modeled using polynomials, trigonometric functions, and exponentials <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Developing fluency in finding rates of change for these abstract functions provides a common language to discuss changes in concrete situations <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

It's important to remember that derivatives fundamentally involve looking at tiny changes in one quantity and how they relate to resulting tiny changes in another quantity <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This concept of "tiny nudges" is at the heart of understanding derivatives intuitively and geometrically <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Deriving the Power Rule Geometrically
The power rule is a method for [[computing_derivatives_of_functions | computing derivatives]] of functions where the variable is raised to a power. It can be understood through geometric visualization.

### Derivative of f(x) = x²
To find the derivative of `f(x) = x²`, consider a square with side length `x` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. If `x` is increased by a tiny nudge, `dx`, the resulting change in the area of the square (`dF`) is sought <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

This change in area consists of three new bits <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>:
*   Two thin rectangles, each with dimensions `x` by `dx`, contributing `2 * x * dx` to the new area <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   A minuscule square with area `dx²` <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

When dealing with "truly tiny amounts" for `dx`, any term involving `dx` raised to a power greater than 1 (like `dx²`) can be safely ignored because it becomes negligibly tiny <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

Therefore, the change in area (`dF`) is approximately `2x * dx` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. The derivative, `dF/dx`, is then `2x` <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This represents the rate of change of the area per unit change in `x` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Derivative of f(x) = x³
Similarly, for `f(x) = x³`, this can be visualized as the volume of a cube with side length `x` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. When `x` is increased by `dx`, the resulting increase in volume (the yellow region in the visualization) is `dF` <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

This new volume is predominantly comprised of three square faces, each with dimensions `x` by `x` by `dx` <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. Each of these thin squares contributes `x² * dx` to the volume change, totaling `3x² * dx` <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. Other slivers of volume along edges (`dx²` terms) or in the corner (`dx³` terms) are proportional to higher powers of `dx` and can be ignored as `dx` approaches zero <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

Thus, the derivative of `x³`, `dF/dx`, is `3x²` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. This corresponds to the slope of the graph of `x³` at any point `x` <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### The General Power Rule
The derivations for `x²` and `x³` reveal a pattern known as the **power rule**: the derivative of `xⁿ` for any power `n` is `n * x^(n-1)` <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

This rule can be understood by considering `(x + dx)ⁿ` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. When `x` is nudged by `dx`, `(x + dx)ⁿ` involves multiplying `n` terms of `(x + dx)` <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   The first term in the expansion is `xⁿ` <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
*   The next set of terms comes from choosing `dx` from one parenthesis and `x` from the remaining `n-1` parentheses <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Since there are `n` ways to choose which parenthesis contributes `dx`, this results in `n` terms, each of which is `x^(n-1) * dx` <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. In total, this contributes `n * x^(n-1) * dx` to the change <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   All other terms in the expansion will include `dx²` or higher powers of `dx`, making them negligible when `dx` is tiny <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

Therefore, the increase in the output is negligibly `n * x^(n-1) * dx`, meaning the derivative of `xⁿ` is `n * x^(n-1)` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Application and Challenges
While the power rule is often applied symbolically (the exponent "hops down in front" and is "reduced by one" <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>), understanding its geometric foundation reinforces the underlying principles of derivatives as "tiny nudges" <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

#### Challenge: Derivative of f(x) = 1/x (or x⁻¹)
One can apply the power rule directly to `f(x) = 1/x` by rewriting it as `x⁻¹` <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. The video poses a challenge to reason about this geometrically:
*   Visualize `1/x` as the height of a rectangle with an area of 1 and a width of `x` <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   Consider how the height must change (`d(1/x)`) if the width increases by a tiny `dx`, while maintaining a constant area of 1 <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
*   The video encourages comparing the geometrically derived `d(1/x)/dx` to the result obtained by applying the power rule symbolically <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

#### Challenge: Derivative of f(x) = √x
Another challenge presented is to reason through what the derivative of the square root of `x` should be <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

## Other Types of Derivatives Explained Intuitively
The video briefly touches upon finding derivatives of other functions through intuitive geometric understanding, such as trigonometric functions.

### Derivative of f(x) = sin(θ)
The derivative of sine can be understood by looking at the unit circle <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
*   `sin(θ)` represents the height of a point on the unit circle after traversing an arc length `θ` <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
*   If `θ` is nudged by a tiny `dθ` along the circumference, the change in height is `d(sin(θ))` <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   Zooming in, the arc `dθ` can be seen as the hypotenuse of a tiny right triangle, where the vertical side is `d(sin(θ))` <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
*   This tiny triangle is similar to a larger triangle formed by the radius and `θ` within the unit circle <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   By properties of similar triangles, the ratio `d(sin(θ))/dθ` (adjacent side divided by hypotenuse in the tiny triangle, which is `d(sin(θ))` divided by `dθ`) corresponds to `cos(θ)` (adjacent side of `θ` in unit circle triangle divided by hypotenuse of 1) <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   Therefore, the derivative of `sin(θ)` is `cos(θ)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

#### Challenge: Derivative of f(x) = cos(θ)
A challenge is posed to apply a similar line of reasoning to find the derivative of `cos(θ)` <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

## Moving Forward
Subsequent topics in calculus build upon these fundamental derivative rules, including how to take derivatives of functions that combine simple functions through sums, products, or function compositions, like the [[sum_rule_for_derivatives | sum rule]], [[product_rule_in_calculus | product rule]], and [[chain_rule_in_differentiation | chain rule]] <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. The goal remains to understand each rule geometrically and intuitively for better memorability and understanding <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.