---
title: Trigonometry and complex numbers connection
videoId: yBw67Fb31Cs
---

From: [[3blue1brown]] <br/> 
The connection between [[trigonometric_identities_and_proofs | trigonometry]] and [[introduction_to_complex_numbers | complex numbers]] is fundamental to understanding both concepts more deeply <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Exploring Trigonometric Functions

Initial exploration of trigonometric functions can begin with a graphing calculator like Desmos, even without prior knowledge of their formal definitions <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. For instance, graphing `cos(x)` reveals its sinusoidal, cycling nature, suggesting its relevance to waves and cyclical phenomena <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Manipulating the input `x` (e.g., `cos(ax)`) squishes the graph, increasing its frequency, while manipulating the output (e.g., `b*cos(x)`) stretches it vertically <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### The Half-Angle Identity
A peculiar observation arises when considering the graph of `cos(x)^2` (or `cos²(x)`) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Despite squaring affecting the y-direction, `cos²(x)` remarkably resembles a scaled-down cosine wave that oscillates more quickly <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Through graphical manipulation, this behavior can be expressed as the identity:
`cos²(x) = (1 + cos(2x))/2` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>, <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
This identity, known as the half-angle identity (when rearranged as `cos(α/2) = √(1 + cos(α))/2`), is not obvious and hints at deeper relationships within [[complex_numbers_in_mathematics | mathematics]] <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>, <a class="yt-timestamp" data-t="01:11:53">[01:11:53]</a>.

### Connection to Exponentials
The observation that squaring `cos(x)` leads to a scaled input (`cos(2x)`) is similar to the behavior of exponential functions <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. For example, `(2^x)^2 = 2^(2x)`, where squaring the function is equivalent to scaling its input <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. This parallel suggests a possible connection between [[conceptualizing_complex_numbers | trigonometric functions]] and [[complex_numbers_and_imaginary_exponents | exponents]], a relationship that becomes clear with [[complex_numbers_and_imaginary_exponents | imaginary exponents]] <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

## Conceptualizing Sine and Cosine

### Unit Circle Definition
While often introduced with triangles, [[trigonometric_identities_and_proofs | trigonometry]] is fundamentally about circles <a class="yt-timestamp" data-t="01:13:11">[01:13:11]</a>. In the [[geometric_interpretation_of_complex_numbers | unit circle]], with a radius of one, the input to sine and cosine is a measure of the distance walked around the circle (or the angle in radians) <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>, <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   **Sine (sin θ):** Represents the y-coordinate (height) of a point on the unit circle after walking a distance θ from the rightmost side <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   **Cosine (cos θ):** Represents the x-coordinate (distance to the y-axis) of that same point <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
For example, walking `π` units (half the circumference) brings the point to (-1, 0), so `cos(π) = -1` and `sin(π) = 0` <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

### Right Triangle Definition (SOH CAH TOA)
The traditional definition uses right triangles <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>:
*   **SOH:** Sine = Opposite / Hypotenuse <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>
*   **CAH:** Cosine = Adjacent / Hypotenuse <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>
*   **TOA:** Tangent = Opposite / Adjacent <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>
This definition is useful for solving problems involving side lengths and angles in triangles, such as calculating the shadow cast by a leaning tower <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.

### Degrees vs. Radians
While degrees are intuitive for angles in triangles, mathematicians prefer radians, as they are a "natural unit" directly related to the arc length of a unit circle <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>, <a class="yt-timestamp" data-t="00:29:23">[00:29:23]</a>. For example, 180 degrees is equivalent to `π` radians <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>.

## Calculating Trigonometric Values
Direct computation of sine and cosine values can be complex without advanced techniques <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>. However, some values can be derived using geometric symmetries:
*   **Equilateral Triangle:** By bisecting an equilateral triangle with side length 1, a 30-60-90 right triangle is formed <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>. This allows for the calculation of `sin(π/6)` (30 degrees) as 1/2 <a class="yt-timestamp" data-t="00:35:16">[00:35:16]</a> and `cos(π/6)` as `√(3)/2` using the Pythagorean theorem <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.
*   **Negative Angles:** The unit circle definition naturally handles negative angles, representing movement in the clockwise direction <a class="yt-timestamp" data-t="00:42:42">[00:42:42]</a>. For example, `cos(-2π/3)` is -1/2, as `2π/3` radians corresponds to 120 degrees <a class="yt-timestamp" data-t="00:46:17">[00:46:17]</a>.

### Using Identities for Computation
The half-angle identity `cos²(x) = (1 + cos(2x))/2` can be used to compute values that are otherwise difficult, such as `cos(π/12)` (15 degrees) <a class="yt-timestamp" data-t="00:48:43">[00:48:43]</a>. By setting `x = π/12`, the identity relates `cos(π/12)` to `cos(π/6)`, a known value:
`cos²(π/12) = (1 + cos(2 * π/12))/2 = (1 + cos(π/6))/2` <a class="yt-timestamp" data-t="00:53:12">[00:53:12]</a>.
Since `cos(π/6) = √(3)/2`, then `cos²(π/12) = (1 + √(3)/2)/2` <a class="yt-timestamp" data-t="00:54:07">[00:54:07]</a>.
Therefore, `cos(π/12) = √((1 + √(3)/2)/2)` <a class="yt-timestamp" data-t="00:54:19">[00:54:19]</a>. This complex result highlights the power of trigonometric identities.

## Geometric Interpretations on the Unit Circle
### Tangent
On the unit circle, the tangent of an angle `θ` (tan θ) can be visualized as the length of a line segment tangent to the circle at (1,0) that extends vertically to intersect the radial line for angle `θ` <a class="yt-timestamp" data-t="00:57:19">[00:57:19]</a>. This directly represents `opposite/adjacent` where the adjacent side is 1 <a class="yt-timestamp" data-t="00:58:11">[00:58:11]</a>. As `θ` approaches `π/2` (90 degrees), the tangent line becomes vertical, and its length approaches infinity, corresponding to `tan(π/2)` being undefined <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>.

### Visualizing Cosine Squared and Sine Squared
Consider a right triangle inscribed in a unit circle with hypotenuse 1, an angle `θ`, adjacent side `cos θ`, and opposite side `sin θ` <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>. If a perpendicular line is dropped from the vertex of angle `θ` to the hypotenuse, it divides the hypotenuse into two segments <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.
*   One segment, adjacent to `cos θ` in the smaller right triangle formed, has length `cos²(θ)` <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>.
*   The other segment, adjacent to `sin θ` in the other smaller right triangle, has length `sin²(θ)` <a class="yt-timestamp" data-t="01:09:11">[01:09:11]</a>.

Since these two segments make up the entire hypotenuse (which has length 1), this visually demonstrates the [[trigonometric_identities_and_proofs | Pythagorean identity]]:
`cos²(θ) + sin²(θ) = 1` <a class="yt-timestamp" data-t="00:39:24">[00:39:24]</a>.

This visual representation of `cos²(θ)` and `sin²(θ)` within the unit circle diagram is distinct from simply literally squaring the lengths of `cos θ` and `sin θ` <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. It provides a geometric understanding of these squared terms and their relationship, setting the stage for understanding their connection to [[complex_numbers_and_transformations | complex numbers]] in the context of [[applications_of_complex_numbers_in_engineering_and_mathematics | advanced mathematics]] and [[complex_numbers_and_fourier_transform | Fourier Transform]] <a class="yt-timestamp" data-t="01:11:15">[01:11:15]</a>.