---
title: Geometric interpretation of derivatives
videoId: S0_qX4VJhMQ
---

From: [[3blue1brown]] <br/> 

Understanding how to [[computing_derivatives_of_functions | compute derivatives]] is a fundamental step after grasping [[understanding_what_a_derivative_is | what a derivative is]] and its connection to rates of change <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. While much of calculus involves grappling with derivatives of abstract functions, this skill is crucial because many real-world phenomena are modeled using pure functions like polynomials, trigonometric functions, and exponentials <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Developing fluency with these abstract functions provides a language to discuss rates of change in concrete situations <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

However, it's easy for this process to feel like mere memorization of rules <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. It's important to remember that derivatives are fundamentally about looking at tiny changes in one quantity and how they relate to resulting tiny changes in another quantity <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. This article aims to show how to think about these rules intuitively and geometrically, always keeping in mind that tiny nudges are at the heart of derivatives <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Calculating Derivatives: The Core Idea

The core question when [[calculating_derivatives_and_their_applications | calculating derivatives]] is: if you look at a value `x` and compare it to a value slightly bigger (`dx` bigger), what's the corresponding change in the function's value (`dF`) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>? Specifically, what is `dF` divided by `dx`, representing the rate at which the function changes per unit change in `x` <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>?

Initially, this ratio `dF/dx` can be conceptualized as the slope of a tangent line to the graph of the function <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. For instance, with `f(x) = x²`, the slope generally increases as `x` increases: it's zero at `x=0`, steeper at `x=1`, and steeper still at `x=2` <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. However, [[visualizing_derivatives_using_graphs | looking at graphs]] isn't always the best way to understand the precise formula for a derivative <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. For that, a more literal look at what the function represents is beneficial <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### The Derivative of x²

Consider `f(x) = x²` geometrically as the area of a square with side length `x` <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
If `x` is increased by a tiny nudge `dx`, the resulting change in the area of that square is `dF` <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This increase in area consists of three new bits:
*   Two thin rectangles, each with side lengths `x` and `dx`, contributing `2 * x * dx` to the new area <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   A minuscule square with area `dx²` <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

When dealing with tiny amounts, a crucial rule of thumb is to ignore anything that includes `dx` raised to a power greater than 1, as a tiny change squared is a negligibly tiny change <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
Thus, `dF` is approximately `2x * dx`.
Dividing `dF` by `dx` gives the derivative of `x²`, which is `2x` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This means if you start at `x=3`, the rate of change in area per unit change in length is `2 * 3 = 6` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### The Derivative of x³

For `f(x) = x³`, visualize it as the volume of a cube with side length `x` <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
When `x` is increased by a tiny `dx`, the resulting increase in volume (`dF`) is primarily contributed by three square faces <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
Each of these thin squares has a volume of `x² * dx` (area of the face times the thickness `dx`) <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
In total, this accounts for `3x² * dx` of volume change <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
Other slivers of volume along the edges and in the corner are proportional to `dx²` or `dx³`, and can be safely ignored because they will vanish when divided by `dx` and `dx` approaches 0 <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
Therefore, the derivative of `x³` is `3x²` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
This means the slope of the graph of `x³` at every point `x` is `3x²` <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### The Power Rule

These examples illustrate a recognizable pattern for polynomial terms, known as the **power rule**:
The derivative of `x` to the power of `n` (`x^n`) for any power `n` is `n * x^(n-1)` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
Symbolically, the exponent "hops down in front, leaving behind one less than itself" <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

Geometrically, when `x` is nudged to `x + dx`, expanding `(x + dx)^n` involves multiplying `n` separate `(x + dx)` terms <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. The expansion starts with `x^n` <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. The next terms result from choosing mostly `x`'s with a single `dx` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Since there are `n` different parentheticals from which to choose that single `dx`, this gives `n` separate terms, each `x^(n-1) * dx` <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. All other terms will be multiples of `dx²` or higher powers, which are negligible <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. Thus, the increase in the output is primarily from `n` copies of `x^(n-1) * dx` <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

### The Derivative of 1/x

The function `f(x) = 1/x` can be written as `x^(-1)`, allowing the application of the power rule: `(-1) * x^(-1-1) = -1 * x^(-2)` or `-1/x²` <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
Geometrically, `1/x` can be visualized as the height of a rectangle with area 1 and width `x` <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
If the width `x` is nudged by `dx`, the height must change (decrease) by `d(1/x)` to maintain an area of 1 <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. The increase in width `dx` adds new area, so the puddle must decrease in height to cancel out this area gain <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. `d(1/x)` would be a negative amount <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

:::info Challenge
Pause and ponder how to derive the derivative of `1/x` using this geometric reasoning and compare it to the power rule result <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. Also, try to reason through the derivative of the square root of `x` <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
:::

### The Derivative of sin(x)

For trigonometric functions, specifically `sin(x)`, knowledge of the unit circle is helpful <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. On a unit circle (radius 1, centered at origin), for a given `theta`, `sin(theta)` is the height of the point above the x-axis after traversing an arc length `theta` <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

[[visualizing_derivatives_using_graphs | Visualizing derivatives using graphs]] of `sin(theta)` reveals a wave pattern, and by observing the slope:
*   At `theta = 0`, the slope is positive <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   As `theta` approaches its peak, the slope goes to 0 <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   The slope becomes negative while `sin(theta)` decreases, returning to 0 as the graph levels out <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
This shape suggests the derivative graph should be `cos(theta)` <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

For a more precise understanding, consider the unit circle itself <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. Imagine a tiny nudge `d theta` along the circumference <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. The question is how much this tiny step changes `sin(theta)` (the height above the x-axis), represented as `d sin(theta)` <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
Zoomed in, the circle appears as a straight line. A small right triangle can be formed where:
*   The hypotenuse is `d theta` (the nudge along the circumference) <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
*   The vertical side (opposite the angle `theta`) is `d sin(theta)` (the change in height) <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
This tiny triangle is similar to the larger triangle formed by the radius (hypotenuse of length 1), the x-coordinate, and the y-coordinate (sin(theta)) <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. The angle at the center of the tiny triangle is `theta` <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

The derivative of sine is the ratio `d sin(theta) / d theta` <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. From the diagram, this ratio represents the length of the side adjacent to the angle `theta` divided by the hypotenuse <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. By definition, this is exactly `cos(theta)` <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
This geometric perspective provides a precise understanding beyond mere graphical intuition <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

:::info Challenge
Using a similar line of reasoning, determine what the derivative of `cos(theta)` should be <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
:::

These geometric interpretations help to make the rules of derivatives intuitively reasonable and memorable, connecting them back to the fundamental concept of "tiny nudges" rather than treating them as abstract formulas <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
The next step is to explore how to take derivatives of functions that combine these simple functions, through sums, products, or function compositions <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.