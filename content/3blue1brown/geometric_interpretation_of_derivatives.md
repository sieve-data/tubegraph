---
title: Geometric interpretation of derivatives
videoId: S0_qX4VJhMQ
---

From: [[3blue1brown]] <br/> 

Understanding how to compute derivatives of functions is a crucial step after grasping their meaning as rates of change <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. While calculus students often spend time grappling with derivatives of abstract functions, this skill provides a language to describe real-world phenomena modeled by functions like polynomials, trigonometric functions, and exponentials <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

However, the process of computing derivatives can feel like rote memorization if one loses sight of the fundamental idea: that derivatives are about looking at tiny changes in one quantity and how they relate to resulting tiny changes in another <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Visualizing these rules intuitively and geometrically can help maintain this understanding <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Derivatives and Tiny Nudges
At the heart of [[understanding_the_meaning_and_computation_of_derivatives|derivatives]] are "tiny nudges" <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. When considering a function, the derivative asks what the corresponding change in the function's value (dF) is when the input (x) is increased by a tiny amount (dx), specifically the ratio dF/dx <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This ratio represents the rate at which the function changes per unit change in x <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### Geometric Interpretation of *x²*
One way to intuitively understand the derivative of *f(x) = x²* is to consider it geometrically <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Visualizing x²:** Imagine *x²* as the area of a square with side length *x* <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   **Applying a Nudge:** If *x* is increased by a tiny amount *dx*, the resulting change in the area of the square is *dF* <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   **New Area Components:** This tiny increase in area can be visualized as three new bits:
    *   Two thin rectangles, each with dimensions *x* by *dx*, contributing *2 * x * dx* to the area <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
    *   A minuscule square with dimensions *dx* by *dx*, contributing *dx²* to the area <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.
*   **Ignoring Negligible Terms:** Since *dx* represents a truly tiny amount, any term with *dx* raised to a power greater than 1 (like *dx²*) is considered negligibly tiny and can be ignored <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Result:** This leaves *dF ≈ 2x * dx*. Therefore, the derivative, *dF/dx*, is *2x* <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. For example, if *x = 3*, the rate of change in area per unit change in length is *2 * 3 = 6* <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

### Geometric Interpretation of *x³*
Similarly, the derivative of *f(x) = x³* can be understood geometrically <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Visualizing x³:** Think of *x³* as the volume of a cube with side length *x* <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Applying a Nudge:** When *x* is increased by a tiny *dx*, the resulting increase in volume (dF) is the new volume in a cube of side length *(x + dx)* that was not in the original cube <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **New Volume Components:** Almost all of this new volume comes from three square faces:
    *   Each face has an area of *x²* and a thickness of *dx*, contributing *x² * dx* to the volume <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
    *   In total, these three faces give *3x² * dx* of volume change <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Ignoring Negligible Terms:** Other slivers of volume along the edges or in the corner are proportional to *dx²* or *dx³* and can be safely ignored when *dx* approaches 0 <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Result:** This means the derivative of *x³*, *dF/dx*, is *3x²* <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. This also means the slope of the graph of *x³* at any point *x* is exactly *3x²* <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

## The Power Rule
The patterns observed for *x²* and *x³* lead to a general rule for [[power_rule_in_calculus_and_its_geometric_significance|derivatives of polynomial functions]]:
*   The derivative of *xⁿ* for any power *n* is *n * x^(n-1)* <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. This is known as the [[power_rule_in_calculus_and_its_geometric_significance|power rule]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

This rule can be understood by considering the expansion of *(x + dx)ⁿ* <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>:
*   The first term is *xⁿ* <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
*   The next terms involve choosing *dx* from one of the *n* parentheticals and *x* from the remaining *(n-1)* parentheticals. This results in *n* separate terms, each *x^(n-1) * dx* <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
*   All other terms in the expansion will be multiples of *dx²* or higher powers, which can be safely ignored <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   Thus, almost all of the increase in the output comes from *n* copies of *x^(n-1) * dx* <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

## Geometric Interpretation of Trigonometric Functions
The derivatives of trigonometric functions can also be understood geometrically using the unit circle.

### Derivative of Sine (sin(θ))
*   **Visualizing Sine:** On a unit circle (radius 1, centered at origin), for a given angle *θ*, *sin(θ)* represents the height of the point on the circle above the x-axis <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
*   **Applying a Nudge:** Consider a tiny nudge of *dθ* along the circumference of the unit circle <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. This tiny step changes the height by *d sin(θ)* <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Right Triangle Approximation:** Zooming in, the arc *dθ* looks like a straight line, forming the hypotenuse of a tiny right triangle. The vertical side of this triangle represents *d sin(θ)* <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
*   **Similar Triangles:** This tiny triangle is similar to a larger triangle formed by the angle *θ*, the radius of the unit circle (hypotenuse = 1), and the x-axis. The angle within the tiny triangle that corresponds to *θ* is found between the hypotenuse (*dθ*) and the horizontal leg <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Ratio of Sides:** The derivative of sine is the ratio *d sin(θ) / dθ* <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. In the tiny triangle, *d sin(θ)* is the side adjacent to the angle *θ*, and *dθ* is the hypotenuse. The ratio of the adjacent side to the hypotenuse is the definition of *cosine(θ)* <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
*   **Result:** Therefore, the derivative of *sin(θ)* is *cos(θ)* <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

By understanding these geometric interpretations, the rules for [[derivatives_of_simple_functions_and_their_intuition|derivatives of simple functions]] become more intuitive and less like a list of formulas to memorize <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.