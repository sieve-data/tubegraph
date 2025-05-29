---
title: Trigonometric identities and proofs
videoId: yBw67Fb31Cs
---

From: [[3blue1brown]] <br/> 

This article explores the foundational concepts of trigonometric functions, their definitions, and the discovery of non-trivial identities, aiming to connect them to complex numbers in future discussions <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Understanding Basic Trigonometric Functions

Initially, one might explore trigonometric functions like cosine using a graphing calculator like Desmos, without prior knowledge of their definitions <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. The graph of a cosine function resembles a [[understanding_basic_trigonometric_functions_and_waves | sinusoidal wave]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, displaying a cycling phenomenon relevant to wave dynamics <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Tweaking the input, such as multiplying `x` by a constant, "squishes" the graph, leading to a higher frequency <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

A particularly interesting observation arises when squaring the cosine function, i.e., `cos(x)^2` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. When `cos(x)` is squared, values like 1 squared remain 1, and negative 1 squared also become 1, ensuring the resulting graph stays positive <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Surprisingly, `f(x) = cos(x)^2` looks like another [[understanding_basic_trigonometric_functions_and_waves | cosine wave]], but oscillating more quickly <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This phenomenon suggests a connection between squaring the output and scaling the input <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

This observation leads to the discovery of a key [[trigonometry_and_complex_numbers_connection | trigonometric identity]]:
`cos(x)^2 = (1 + cos(2x))/2` <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>, <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
This identity shows that squaring the cosine function results in a scaled and shifted version of `cos(2x)`, implying a doubling of its frequency <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This non-obvious behavior hints at a deeper relationship between [[trigonometry_and_complex_numbers_connection | cosine]] and [[derivatives_of_trigonometric_and_exponential_functions | exponential functions]] <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

## Defining Sine and Cosine with Circles

While often taught with triangles, trigonometry is fundamentally about circles <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>, particularly the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]] (a circle with radius one) <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

*   **Sine (sin(θ))**: The `y`-coordinate (height) of a point as it moves around the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]], starting from the rightmost side <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. When starting at `x=0`, sine is 0, then increases as the point moves counter-clockwise <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
*   **Cosine (cos(θ))**: The `x`-coordinate (distance from the vertical line) of a point as it moves around the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]] <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. It starts at 1 when `x=0` and decreases as the point moves away from the starting point <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

The input `θ` (theta) represents the distance walked along the arc of the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]], measured in [[sine_and_cosine_on_the_unit_circle_and_angles | radians]] <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. For instance, walking `pi` units around the circle gets you halfway around <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

> For example, `cos(3)` and `sin(3)`: Since `pi` is approximately 3.14, walking 3 units around the unit circle places you slightly less than halfway around, near the left side <a class="yt-timestamp" data-t="00:19:13">[00:19:13]</a>.
> *   `cos(3)` (x-coordinate) will be very close to -1 <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
> *   `sin(3)` (y-coordinate) will be a small positive value <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.

## Right Triangle Definitions: SOH CAH TOA

In high school trigonometry, functions are often introduced using right triangles, summarized by the mnemonic "SOH CAH TOA" <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>. For a right triangle with angle `θ`:
*   **SOH**: `sin(θ) = Opposite / Hypotenuse` <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>
*   **CAH**: `cos(θ) = Adjacent / Hypotenuse` <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>
*   **TOA**: `tan(θ) = Opposite / Adjacent` <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>

> **Example Application**: For a 100-meter tall leaning tower that makes an 80-degree angle with the ground, when the sun is directly overhead, the shadow length (adjacent side) can be found using the cosine function <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.
> `cos(80°) = Shadow / 100` <a class="yt-timestamp" data-t="00:25:55">[00:25:55]</a>
> Thus, `Shadow = 100 * cos(80°)` <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>.

The connection between triangle-based definitions and the unit circle is established by scaling any right triangle so its hypotenuse is 1 <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>. In this scaled triangle, the adjacent side becomes `cos(θ)` and the opposite side becomes `sin(θ)` <a class="yt-timestamp" data-t="00:28:14">[00:28:14]</a>. The tip of such triangles traces out a unit circle, with coordinates `(cos(θ), sin(θ))` <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.
Mathematicians prefer [[sine_and_cosine_on_the_unit_circle_and_angles | radians]] over degrees for angles, as [[sine_and_cosine_on_the_unit_circle_and_angles | radians]] represent a natural unit (arc length on a unit circle) <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>. For example, 180 degrees is `pi` [[sine_and_cosine_on_the_unit_circle_and_angles | radians]] <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>, and 60 degrees is `pi/3` [[sine_and_cosine_on_the_unit_circle_and_angles | radians]] <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.

## Computing Trigonometric Values

Computing specific trigonometric values by hand can be challenging <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>. However, some values can be derived from geometric settings with sufficient symmetry.

> For an equilateral triangle with side length 1, splitting it in half forms a 30-60-90 right triangle with hypotenuse 1, an opposite side of 1/2 (to the 30-degree angle), and an adjacent side of `sqrt(3)/2` (derived via the [[proof_and_demonstration_of_the_pythagorean_theorem | Pythagorean theorem]]) <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>.
> *   `sin(pi/6)` (or 30 degrees) = Opposite/Hypotenuse = (1/2) / 1 = 1/2 <a class="yt-timestamp" data-t="00:35:16">[00:35:16]</a>.
> *   `cos(pi/6)` (or 30 degrees) = Adjacent/Hypotenuse = `(sqrt(3)/2)` / 1 = `sqrt(3)/2` <a class="yt-timestamp" data-t="00:37:23">[00:37:23]</a>, <a class="yt-timestamp" data-t="00:38:46">[00:38:46]</a>.

### The Pythagorean Identity

A fundamental identity is `cos(x)^2 + sin(x)^2 = 1` <a class="yt-timestamp" data-t="00:39:31">[00:39:31]</a>. This identity directly stems from the [[proof_and_demonstration_of_the_pythagorean_theorem | Pythagorean theorem]] applied to the unit circle: `x^2 + y^2 = r^2`, where `x = cos(theta)`, `y = sin(theta)`, and `r = 1` <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>.
Note the unconventional notation in trigonometry where `cos^2(x)` means `(cos(x))^2` <a class="yt-timestamp" data-t="00:40:11">[00:40:11]</a>.

### Half-Angle Identity

The previously discovered identity, `cos^2(x) = (1 + cos(2x))/2`, is known as a [[trigonometry_and_complex_numbers_connection | half-angle identity]] <a class="yt-timestamp" data-t="01:11:59">[01:11:59]</a>. It allows for the computation of values that are otherwise tricky, like `cos(pi/12)` (15 degrees) <a class="yt-timestamp" data-t="00:48:43">[00:48:43]</a>.
To find `cos(pi/12)`:
`cos^2(pi/12) = (1 + cos(2 * pi/12))/2` <a class="yt-timestamp" data-t="00:53:20">[00:53:20]</a>
`cos^2(pi/12) = (1 + cos(pi/6))/2` <a class="yt-timestamp" data-t="00:53:34">[00:53:34]</a>
Since `cos(pi/6) = sqrt(3)/2`, then `cos^2(pi/12) = (1 + sqrt(3)/2)/2` <a class="yt-timestamp" data-t="00:54:13">[00:54:13]</a>.
Therefore, `cos(pi/12) = sqrt((1 + sqrt(3)/2)/2)` <a class="yt-timestamp" data-t="00:54:23">[00:54:23]</a>.

## Visualizing Tangent and a Sneaky Proof

The tangent function, `tan(theta)`, can also be visualized on the [[sine_and_cosine_on_the_unit_circle_and_angles | unit circle]] <a class="yt-timestamp" data-t="00:56:44">[00:56:44]</a>. If a perpendicular line is drawn from `(1,0)` (the rightmost point of the unit circle) upwards, and a line from the origin at angle `theta` extends to intersect it, the length of the segment on the perpendicular line, from the x-axis to the intersection, represents `tan(theta)` <a class="yt-timestamp" data-t="00:58:15">[00:58:15]</a>, <a class="yt-timestamp" data-t="00:58:49">[00:58:49]</a>. This line is tangent to the circle, which is where the term "tangent" comes from <a class="yt-timestamp" data-t="00:58:33">[00:58:33]</a>. As `theta` approaches `pi/2` (90 degrees), `tan(theta)` approaches infinity <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>.

Perhaps the most exciting application is a "sneaky" [[proof_and_demonstration_of_the_pythagorean_theorem | proof of the Pythagorean theorem]] using trigonometric concepts <a class="yt-timestamp" data-t="01:05:40">[01:05:40]</a>.
Consider a right triangle within the unit circle, with hypotenuse 1, vertical side `sin(theta)`, and horizontal side `cos(theta)` <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>.
Draw a perpendicular line from the top vertex down to the hypotenuse. This creates two smaller right triangles similar to the original.
1.  The projection of the horizontal side (`cos(theta)`) onto the hypotenuse will have a length of `cos(theta) * cos(theta) = cos^2(theta)` <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>, <a class="yt-timestamp" data-t="01:07:33">[01:07:33]</a>.
2.  Similarly, the projection of the vertical side (`sin(theta)`) onto the hypotenuse will have a length of `sin(theta) * sin(theta) = sin^2(theta)` <a class="yt-timestamp" data-t="01:09:11">[01:09:11]</a>, <a class="yt-timestamp" data-t="01:09:32">[01:09:32]</a>.

Since these two projected lengths compose the entire hypotenuse, and the hypotenuse has a length of 1, it visually demonstrates that `cos^2(theta) + sin^2(theta) = 1` <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>. This visualization provides insight into how [[proof_and_demonstration_of_the_pythagorean_theorem | the Pythagorean theorem]] is inherent in the definitions of sine and cosine on the unit circle <a class="yt-timestamp" data-t="01:09:36">[01:09:36]</a>. This is one form of a [[visual_proofs_and_triangle_isosceles | visual proof]].

The connection between these trigonometric identities and [[trigonometry_and_complex_numbers_connection | complex numbers]] will be explored further, particularly how doubling an angle relates to squaring a quantity, which is not a coincidence <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>.