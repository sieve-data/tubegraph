---
title: Trigonometry in relation to angles and triangles
videoId: yBw67Fb31Cs
---

From: [[3blue1brown]] <br/> 

[[Trigonometry and complex numbers | Trigonometry]] is fundamentally about understanding the relationship between angles and the sides of triangles, particularly right triangles <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>. While often introduced through triangles, a deeper understanding reveals its core connection to circles <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

## Introduction to Trigonometric Functions

Trigonometric functions, such as cosine and sine, describe cycling phenomena and are relevant in fields like physics for studying waves <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. By manipulating their inputs and outputs on a graphing calculator, one can observe how these functions behave <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. For instance, putting a larger constant in front of `x` in `cosine(x)` squishes the graph, increasing its frequency <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

A surprising discovery from graphing `cosine(x)` is that squaring `cosine(x)` (i.e., `cos²(x)`) results in a graph that looks like a scaled-down, faster-oscillating cosine wave <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This non-obvious behavior suggests a deeper mathematical relationship, particularly a connection to exponential functions <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. For example, `(2^x)²` is equivalent to `2^(2x)`, showing a similar property where squaring a function is like scaling its input <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

## Understanding Sine and Cosine Using Unit Circles

A powerful way to understand sine and cosine is through the [[understanding_sine_and_cosine_using_unit_circles | unit circle]] <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. Imagine starting at the rightmost side of a circle with a radius of one <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. As you walk around the circle at a constant rate:
*   **Sine (sin θ)**: The sine of an angle (or distance walked) represents your height, or y-coordinate, on the unit circle <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   **Cosine (cos θ)**: The cosine of an angle represents your x-coordinate, or distance from the vertical line <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

Since a full walk around the unit circle is `2π` units (where `π` units gets you halfway around), trigonometric functions naturally cycle <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. For instance, `cosine(3)` is approximately -0.99 and `sine(3)` is approximately 0.14, because walking 3 units around the circle places you just shy of halfway around (`π ≈ 3.14`) <a class="yt-timestamp" data-t="00:18:33">[00:18:33]</a>.

### Radians vs. Degrees

In mathematics, angles are often expressed in [[geometry_and_circles | radians]], which represent the literal distance walked along the circumference of a unit circle <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. This is considered a more "natural unit" than degrees, as it directly relates to arc length <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>. For example, 180 degrees is equivalent to `π` radians <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>. When dealing with calculus involving trigonometric functions, radians are almost always preferred <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>.

## Trigonometric Functions in Right Triangles (SOH CAH TOA)

The classic way to remember trigonometric definitions for a right triangle is "SOH CAH TOA" <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>:
*   **SOH**: **S**ine = **O**pposite / **H**ypotenuse <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>
*   **CAH**: **C**osine = **A**djacent / **H**ypotenuse <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>
*   **TOA**: **T**angent = **O**pposite / **A**djacent <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>

For example, if a 100-meter leaning tower makes an 80-degree angle with the ground, the length of its shadow when the sun is directly overhead (forming a right triangle) would be `100 * cosine(80 degrees)` <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>.

This triangle-based definition connects to the unit circle by scaling any right triangle so its hypotenuse is 1 <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>. In such a [[geometry_and_circles | triangle]], the opposite side becomes `sin θ` and the adjacent side becomes `cos θ`, representing the y and x coordinates on a unit circle, respectively <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>.

## Computing Specific Values and Identities

Computing exact values for sine and cosine can be challenging <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>. However, some values can be derived using geometric symmetries. For example, by bisecting an equilateral triangle (with side lengths of 1), a 30-60-90 right triangle is formed <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>.
*   The sine of `π/6` (30 degrees) is 1/2 <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>.
*   The cosine of `π/6` (30 degrees) is `√3 / 2` <a class="yt-timestamp" data-t="00:37:23">[00:37:23]</a>. This is found using the [[Pythagorean theorem and triples | Pythagorean theorem]]: `(1/2)² + (adjacent)² = 1²`, leading to `adjacent = √(3/4) = √3 / 2` <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>.

### The Pythagorean Identity

A fundamental trigonometric identity, directly derived from the [[Pythagorean theorem and triples | Pythagorean theorem]] on a unit circle, is `cos²(x) + sin²(x) = 1` <a class="yt-timestamp" data-t="00:39:31">[00:39:31]</a>. This means if you know one function, you can find the other <a class="yt-timestamp" data-t="00:39:40">[00:39:40]</a>.
*   **Note on Notation**: In [[Trigonometry and complex numbers | trigonometry]], `cos²(x)` is a shorthand for `(cos(x))²`, which differs from how squaring a function `f(x)` is usually written in other areas of mathematics (`f²(x)` often means `f(f(x))`) <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a>.

### Half-Angle Identity

The relationship discovered by graphing `cosine(x)` squared, `cos²(x) = (1 + cos(2x)) / 2`, is a version of the half-angle identity <a class="yt-timestamp" data-t="00:48:24">[00:48:24]</a>. This identity allows for the computation of values that are otherwise difficult to determine, such as `cosine(π/12)` (15 degrees) <a class="yt-timestamp" data-t="00:48:43">[00:48:43]</a>.
By plugging `x = π/12` into the identity:
`cos²(π/12) = (1 + cos(2 * π/12)) / 2`
`cos²(π/12) = (1 + cos(π/6)) / 2`
Since `cos(π/6) = √3 / 2`:
`cos²(π/12) = (1 + √3 / 2) / 2`
`cos(π/12) = √((1 + √3 / 2) / 2)` <a class="yt-timestamp" data-t="00:54:19">[00:54:19]</a>

This identity highlights the [[connection_between_trigonometry_and_complex_numbers | connection between trigonometry and complex numbers]], where doubling the angle corresponds to a squaring operation <a class="yt-timestamp" data-t="00:56:15">[00:56:15]</a>.

## Geometric Interpretation of Tangent

The tangent function (`tan θ`) can also be visualized on the unit circle <a class="yt-timestamp" data-t="00:56:44">[00:56:44]</a>. If a line tangent to the unit circle is drawn at the point (1,0) and extended upwards or downwards to intersect the terminal side of the angle `θ` (extended if necessary), the length of this tangent segment is `tan θ` <a class="yt-timestamp" data-t="00:58:11">[00:58:11]</a>. This is because a right triangle can be formed where the adjacent side is 1 (the radius) and the opposite side is `tan θ` <a class="yt-timestamp" data-t="00:58:15">[00:58:15]</a>.
*   As `θ` approaches `π/2` (90 degrees), `tan θ` approaches infinity, as the vertical line from the origin becomes parallel to the tangent line at (1,0) <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>.

## Geometric Interpretation of `cos²(θ)` and `sin²(θ)`

Within the unit circle triangle (where the hypotenuse is 1, and legs are `cos θ` and `sin θ`), a powerful visual proof of the [[Pythagorean theorem and triples | Pythagorean identity]] exists <a class="yt-timestamp" data-t="01:05:24">[01:05:24]</a>. By drawing a perpendicular line from the vertex of the right angle to the hypotenuse, two smaller right triangles are formed that are similar to the original <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.
*   The length of the segment on the hypotenuse adjacent to `cos θ` is `cos²(θ)` <a class="yt-timestamp" data-t="01:07:12">[01:07:12]</a>.
*   The length of the segment on the hypotenuse adjacent to `sin θ` is `sin²(θ)` <a class="yt-timestamp" data-t="01:09:32">[01:09:32]</a>.
Since these two segments make up the entire hypotenuse, and the hypotenuse's length is 1, it visually demonstrates that `cos²(θ) + sin²(θ) = 1` <a class="yt-timestamp" data-t="01:09:44">[01:09:44]</a>. This geometric interpretation provides a deep insight into the [[Pythagorean theorem and triples | Pythagorean theorem]] itself <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.