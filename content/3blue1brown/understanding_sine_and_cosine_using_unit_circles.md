---
title: Understanding sine and cosine using unit circles
videoId: yBw67Fb31Cs
---

From: [[3blue1brown]] <br/> 

This lecture aims to establish a fundamental [[connection_between_trigonometry_and_complex_numbers | connection between trigonometry and complex numbers]], which is believed to strengthen the understanding of both subjects <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The initial approach involves revisiting the basics of trigonometric functions and exploring their properties through graphical experimentation before formal definitions <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Initial Graphical Explorations

Before formal definitions, one can observe properties of trigonometric functions by experimenting with a graphing calculator <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Cosine Function Behavior
The cosine function `cos(x)`, when graphed, displays a cycling phenomenon, making it relevant to studies of waves and wave-type dynamics <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   Tweaking the input `x` (e.g., `cos(2x)`) compresses the graph, leading to a higher frequency <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   Tweaking the output (e.g., `2cos(x)`) stretches the graph in the Y-direction <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Squaring the Cosine Function
When `cos(x)` is squared (i.e., `cos²(x)`), the resulting graph exhibits an interesting behavior <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. In the region from 0 to 2π, `cos(x)` goes from 1, dips to -1 at π, and returns to 1 at 2π <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Squaring these values means 1² remains 1, and (-1)² becomes 1, so the squared function will always be positive and oscillate between 0 and 1 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

Surprisingly, the graph of `cos²(x)` looks like another sinusoidal wave that oscillates more quickly <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This leads to the identity:
`cos²(x) = (1/2)cos(2x) + 1/2` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
This can also be written as: `cos²(x) = (1 + cos(2x))/2` <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
This discovered fact is non-trivial, as squaring the output (y-direction) results in a scaling of the input (x-direction) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This suggests a potential relationship between cosine and exponential functions, as squaring an exponential function (e.g., `(2^x)^2`) is equivalent to scaling its input (e.g., `2^(2x)`) <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

## Trigonometry and Circles: The Unit Circle Definition

"You think that it's about triangles, but really it's about circles" <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. This statement encapsulates a fundamental shift in understanding trigonometry from right triangles to [[eulers_formula_and_unit_circle | unit circles]] <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.

### Defining Sine and Cosine
Imagine a unit circle (radius of one) with a point starting at (1,0) on the rightmost side <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
*   **Sine (sin(θ))**: As the point walks around the circle at a constant rate, `sin(θ)` represents its **y-coordinate** (height) <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
    *   At the start (θ=0), the y-coordinate is 0, so `sin(0) = 0` <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Cosine (cos(θ))**: `cos(θ)` represents the point's **x-coordinate** (distance from the y-axis) <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
    *   At the start (θ=0), the x-coordinate is 1, so `cos(0) = 1` <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

The input `θ` (theta) is the distance walked around the unit circle, often thought of as an angle <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. For a unit circle, the input `θ` in radians is the literal arc length <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. For example, walking a distance of `pi` units gets you halfway around the circle, so `cos(pi) = -1` <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

### Radians vs. Degrees
*   **Radians**: The natural unit for angles in mathematics, representing the arc length around a unit circle <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>. For example, 180 degrees is equivalent to `pi` radians <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>. Mathematicians prefer radians because they are more natural and simplify calculations in calculus <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>.
*   **Degrees**: A human-assigned unit for angles, often preferred for intuition in geometry <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>.

## The Right Triangle Definition (SOH CAH TOA)

The classic way to remember [[introduction_to_trigonometric_functions | trigonometric functions]] is through the mnemonic SOH CAH TOA, which applies to right triangles <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>:
*   **SOH**: `Sine(θ) = Opposite / Hypotenuse` <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>
*   **CAH**: `Cosine(θ) = Adjacent / Hypotenuse` <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>
*   **TOA**: `Tangent(θ) = Opposite / Adjacent` <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>

This triangle-based definition can be connected to the unit circle by imagining all possible right triangles scaled such that their hypotenuse is 1 <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>. The end point of the hypotenuse then traces out a unit circle, with coordinates `(cos(θ), sin(θ))` <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.

### Computing Values Using Symmetry

While arbitrary values of sine and cosine are hard to compute by hand <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>, certain values can be derived from geometric settings with sufficient symmetry <a class="yt-timestamp" data-t="00:31:23">[00:31:23]</a>.

*   **Example: Equilateral Triangle (30-60-90)**
    *   Consider an equilateral triangle with side lengths of 1 <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>. Each angle is 60 degrees (π/3 radians) <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.
    *   Bisecting this triangle creates two 30-60-90 right triangles. The hypotenuse is 1, the side opposite the 30-degree (π/6) angle is 1/2, and the side adjacent to the 30-degree angle (opposite the 60-degree angle) can be found using the Pythagorean theorem <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>.
    *   `sin(pi/6)` (opposite/hypotenuse) = `(1/2) / 1 = 1/2` <a class="yt-timestamp" data-t="00:35:16">[00:35:16]</a>.
    *   `cos(pi/6)` (adjacent/hypotenuse) = `sqrt(1² - (1/2)²) / 1` (by Pythagorean theorem) = `sqrt(3/4) = sqrt(3)/2` <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.

## Pythagorean Identity: `cos²(x) + sin²(x) = 1`

This fundamental identity directly stems from the Pythagorean theorem applied to a right triangle in the unit circle <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>. If the hypotenuse is 1, and the legs are `cos(x)` and `sin(x)`, then `cos²(x) + sin²(x) = 1² = 1` <a class="yt-timestamp" data-t="00:39:16">[00:39:16]</a>.

### Visual Proof of Pythagorean Identity
This identity can be visually demonstrated on the unit circle without relying on prior knowledge of the Pythagorean theorem for its definition <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>.
1.  Draw a right triangle with hypotenuse 1, where the legs are `cos(θ)` (horizontal) and `sin(θ)` (vertical) <a class="yt-timestamp" data-t="01:06:02">[01:06:02]</a>.
2.  Drop a perpendicular from the vertex where the sine and cosine legs meet to the hypotenuse <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>. This divides the original triangle into two smaller right triangles that are similar to the original.
3.  Consider the angle `θ` at the origin. The segment of the hypotenuse adjacent to this angle is the "shadow" cast by the cosine leg onto the hypotenuse. By definition of cosine, `cos(θ) = (adjacent shadow) / cos(θ)`, which means the shadow length is `cos²(θ)` <a class="yt-timestamp" data-t="01:06:18">[01:06:18]</a>.
4.  The remaining segment of the hypotenuse is the "shadow" cast by the sine leg. Its length can be found using `sin(θ) = (opposite shadow) / sin(θ)`, meaning this shadow length is `sin²(θ)` <a class="yt-timestamp" data-t="01:09:02">[01:09:02]</a>.
5.  Since these two segments make up the entire hypotenuse of length 1, it visually proves that `cos²(θ) + sin²(θ) = 1` <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.

> [!NOTE] Notation: `cos²(x)` is a common trigonometric convention for `(cos(x))²`, unlike most other functions `f²(x)` which usually imply `f(f(x))` or a second derivative <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.

## Visualizing Tangent on the Unit Circle
While `tan(θ) = Opposite / Adjacent` <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>, its geometric interpretation on the unit circle is distinct.
*   Draw a vertical line tangent to the unit circle at the point (1,0) <a class="yt-timestamp" data-t="00:58:30">[00:58:30]</a>.
*   Extend the hypotenuse of the triangle (the radius of the unit circle) until it intersects this tangent line <a class="yt-timestamp" data-t="00:58:25">[00:58:25]</a>.
*   The length of the segment on the tangent line from the x-axis to the intersection point is `tan(θ)` <a class="yt-timestamp" data-t="00:58:49">[00:58:49]</a>. This is because in the large right triangle formed, the adjacent side is the radius (length 1), making the opposite side directly equal to `tan(θ)` <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.

The graph of `tan(θ)` starts at 0, increases as `θ` approaches π/2, and "blows up to infinity" at π/2, where it is undefined (analogous to dividing by zero) <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>.

## The Half-Angle Identity and Complex Numbers
The identity `cos²(x) = (1 + cos(2x))/2` (also known as the half-angle identity when rearranged as `cos(α/2) = sqrt((1 + cos(α))/2)`) <a class="yt-timestamp" data-t="01:11:30">[01:11:30]</a> allows for the computation of values like `cos(pi/12)` (15 degrees) <a class="yt-timestamp" data-t="00:48:43">[00:48:43]</a>.

For example, to find `cos(pi/12)`:
1.  Use the identity: `cos²(pi/12) = (1 + cos(2 * pi/12)) / 2 = (1 + cos(pi/6)) / 2` <a class="yt-timestamp" data-t="00:53:12">[00:53:12]</a>.
2.  Substitute `cos(pi/6) = sqrt(3)/2` <a class="yt-timestamp" data-t="00:54:07">[00:54:07]</a>.
3.  `cos²(pi/12) = (1 + sqrt(3)/2) / 2` <a class="yt-timestamp" data-t="00:54:13">[00:54:13]</a>.
4.  `cos(pi/12) = sqrt((1 + sqrt(3)/2) / 2)` <a class="yt-timestamp" data-t="00:54:19">[00:54:19]</a>.
This demonstrates how complex values for simple angles can be derived from these identities <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>.

The non-obvious nature of this identity and the observation that squaring cosine relates to scaling its input (doubling the angle) strongly suggests a deeper connection. This connection is found through [[trigonometry_and_complex_numbers | complex numbers]], where doubling an angle corresponds to multiplying by a complex number twice <a class="yt-timestamp" data-t="00:56:15">[00:56:15]</a>. This relationship will be further explored in subsequent discussions <a class="yt-timestamp" data-t="00:56:23">[00:56:23]</a>.