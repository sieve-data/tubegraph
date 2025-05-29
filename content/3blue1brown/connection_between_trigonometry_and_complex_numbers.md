---
title: Connection between trigonometry and complex numbers
videoId: yBw67Fb31Cs
---

From: [[3blue1brown]] <br/> 

The primary goal of this lecture series is to demonstrate a fundamental connection between [[trigonometry_and_complex_numbers | trigonometry and complex numbers]], which can strengthen understanding of both concepts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Exploring Trigonometric Functions through Graphs

An initial exploration of trigonometric functions can be done by simply playing around with a graphing calculator, even without prior knowledge of their formal definitions <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### The Cosine Function

When graphing the cosine function (e.g., `cos(x)`), it immediately becomes apparent that it produces a sinusoidal wave, relevant to phenomena like waves and cycling dynamics <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Manipulating the input `x` by multiplying it by a constant "squishes" the graph, increasing its frequency <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Similarly, modifying the output can stretch the graph in the y-direction <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### The Behavior of `cos(x)^2`

An interesting observation arises when graphing `cos(x)^2` (also commonly written as `cos^2(x)`). While squaring typically affects the y-direction, `cos^2(x)` surprisingly resembles another cosine wave, but oscillating more quickly and entirely positive <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>, <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This non-trivial fact can be discovered through graphical experimentation <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

Through graphical manipulation, it can be derived that `cos^2(x)` is equivalent to `(1 + cos(2x))/2` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This identity is found by:
1.  Shifting the `cos(x)` graph up by 1 unit to make it entirely positive <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
2.  Dividing the result by 2 to match the amplitude <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
3.  Multiplying the input `x` by 2 (e.g., `cos(2x)`) to "squish" the graph and double its frequency <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

This observation hints at a deeper, non-obvious relationship <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### Connecting to Exponentials

The behavior of `cos^2(x)` (scaling the input `x`) is similar to that of exponential functions. For example, the function `f(x) = 2^x` satisfies the property `f(2x) = f(x)^2` <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. This means `(2^x)^2` is equivalent to `2^(2x)` <a class="yt-timestamp" data-t="00:12:13">[00:12:13]`. This peculiar property of exponents, where squaring the function is like scaling its input, suggests that [[trigonometry_and_complex_numbers | cosine might be somehow related to exponentials]] <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>. This connection is further explored in later lectures <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

## Fundamentals of Trigonometry

While often taught in relation to triangles, [[trigonometry_in_relation_to_angles_and_triangles | trigonometry is fundamentally about circles]] <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

### Unit Circle Definition of Sine and Cosine

*   **Sine (sin):** The sine of an angle (or arc distance) `theta` is defined as the y-coordinate of a point on a unit circle (a circle with radius 1) when starting from the rightmost side (0 radians) and walking around counter-clockwise <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. So, `sin(0)` is 0 <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
*   **Cosine (cos):** The cosine of an angle `theta` is defined as the x-coordinate of that same point on the unit circle <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. Thus, `cos(0)` is 1 <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

The input for these functions, when defined by the unit circle, can be thought of as the literal distance walked around the circle, measured in radians <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. For example, walking `pi` units (approximately 3.14) around the circle gets you halfway, leading to `cos(pi) = -1` <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>, <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.

### Right Triangle Definitions (SOH CAH TOA)

[[Trigonometry in relation to angles and triangles | Trigonometric functions are also defined using right triangles]]:
*   **SOH**: **S**ine = **O**pposite / **H**ypotenuse <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>
*   **CAH**: **C**osine = **A**djacent / **H**ypotenuse <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>
*   **TOA**: **T**angent = **O**pposite / **A**djacent <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>

These definitions are consistent with the unit circle definition because any right triangle can be scaled to have a hypotenuse of 1, placing its vertices on the unit circle <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>. In such a scaled triangle with hypotenuse 1:
*   The opposite side length becomes `sin(theta)` <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.
*   The adjacent side length becomes `cos(theta)` <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>.
*   The coordinates of the point on the unit circle are `(cos(theta), sin(theta))` <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.

### Degrees vs. Radians

While degrees are intuitive for humans (e.g., 90 degrees), mathematicians often prefer radians <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>. Radians provide a more natural unit because they relate directly to the arc length on a unit circle:
*   180 degrees = `pi` radians (halfway around a unit circle) <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>.
*   60 degrees = `pi/3` radians <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>.
*   30 degrees = `pi/6` radians <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>.
In calculus and advanced mathematics, it is typically easier to use radians <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.

## Computing Trigonometric Values

Calculating precise trigonometric values by hand is generally difficult <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>. However, some values can be derived using geometric symmetry, particularly from equilateral triangles or special right triangles (e.g., 30-60-90 or 45-45-90) <a class="yt-timestamp" data-t="00:31:23">[00:31:23]</a>.

For example, for an angle of `pi/6` (30 degrees) in a right triangle with hypotenuse 1:
*   `sin(pi/6)` = 1/2 <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>
*   `cos(pi/6)` = `sqrt(3)/2` <a class="yt-timestamp" data-t="00:37:23">[00:37:23]</a> (derived using the Pythagorean theorem) <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>

Values for angles outside the 0 to 90 degree (0 to `pi/2` radian) range can be found using the unit circle. For example, `cos(-2pi/3)` is -1/2 <a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a>.

The identity `cos^2(x) = (1 + cos(2x))/2` (known as the half-angle identity for cosine) can be used to compute more complex values, such as `cos(pi/12)` (15 degrees) <a class="yt-timestamp" data-t="00:48:24">[00:48:24]</a>. Plugging in `x = pi/12` gives:
`cos^2(pi/12) = (1 + cos(2 * pi/12))/2`
`cos^2(pi/12) = (1 + cos(pi/6))/2`
Since `cos(pi/6) = sqrt(3)/2`:
`cos^2(pi/12) = (1 + sqrt(3)/2)/2`
`cos(pi/12) = sqrt((1 + sqrt(3)/2)/2)` <a class="yt-timestamp" data-t="00:53:12">[00:53:12]</a>.

This demonstrates how identities, even if not immediately obvious from definition, can be practical for calculation <a class="yt-timestamp" data-t="00:54:29">[00:54:29]</a>.

## Important Trigonometric Identities and Conventions

### Pythagorean Identity: `cos^2(x) + sin^2(x) = 1`

This fundamental identity states that the square of the cosine of an angle plus the square of the sine of the same angle is always equal to 1 <a class="yt-timestamp" data-t="00:39:24">[00:39:24]</a>. This is a direct consequence of the Pythagorean theorem applied to a right triangle with hypotenuse 1, where the legs are `cos(theta)` and `sin(theta)` <a class="yt-timestamp" data-t="00:39:49">[00:39:49]</a>.

A peculiar notational convention in [[trigonometry_and_complex_numbers | trigonometry]] is writing `(cos(x))^2` as `cos^2(x)` <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a>. This differs from general mathematical notation where `f^2(x)` usually denotes function composition (`f(f(x))`) or sometimes the second derivative, rather than `(f(x))^2` <a class="yt-timestamp" data-t="00:40:34">[00:40:34]</a>.

### Geometric Interpretation of Tangent (`tan(theta)`)

On a unit circle, `tan(theta)` can be visually represented as the length of a vertical line segment that is tangent to the circle at the point `(1,0)` and extends to intersect the extended radial line corresponding to `theta` <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. This is where the term "tangent" originates <a class="yt-timestamp" data-t="00:58:37">[00:58:37]</a>. As `theta` approaches `pi/2` (90 degrees), the tangent line becomes vertical and parallel to the radial line, causing `tan(theta)` to approach infinity (or be undefined) <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>.

### Geometric Interpretation of `cos^2(theta)` and `sin^2(theta)`

Within a unit triangle (hypotenuse = 1) in the unit circle, `cos(theta)` is the length of the adjacent side and `sin(theta)` is the length of the opposite side <a class="yt-timestamp" data-t="01:06:02">[01:06:02]</a>. If a perpendicular line is drawn from the right angle vertex to the hypotenuse:
*   The segment of the hypotenuse adjacent to the angle `theta` represents `cos^2(theta)` <a class="yt-timestamp" data-t="01:07:18">[01:07:18]</a>, <a class="yt-timestamp" data-t="01:10:35">[01:10:35]</a>.
*   The other segment of the hypotenuse represents `sin^2(theta)` <a class="yt-timestamp" data-t="01:09:32">[01:09:32]</a>.
This provides a visual proof of the Pythagorean identity (`cos^2(theta) + sin^2(theta) = 1`), as the sum of these two segments equals the total hypotenuse length of 1 <a class="yt-timestamp" data-t="01:09:37">[01:09:37]</a>.

The non-trivial identity `cos^2(x) = (1 + cos(2x))/2` (or the half-angle identity `cos(alpha/2) = sqrt((1 + cos(alpha))/2)`) will be further explored in future lectures to show how [[trigonometry_and_complex_numbers | complex numbers]] provide an intuitive understanding of its derivation <a class="yt-timestamp" data-t="01:11:10">[01:11:10]</a>. The fact that squaring `cos(x)` results in a function related to `cos(2x)` is not a coincidence, but a "shadow" of the relationship between [[trigonometry_and_complex_numbers | trigonometric functions and complex numbers]] <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>.