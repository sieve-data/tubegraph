---
title: Sine and cosine on the unit circle and angles
videoId: yBw67Fb31Cs
---

From: [[3blue1brown]] <br/> 
The primary objective of this lecture is to establish a connection between [[Trigonometry and complex numbers connection | trigonometry and complex numbers]], which strengthens the understanding of both concepts <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article will begin by revisiting the fundamental aspects of [[Understanding basic trigonometric functions and waves | trigonometric functions]] and their meanings <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Exploring [[Understanding basic trigonometric functions and waves | Cosine Waves]] with a Graphing Calculator

Even without prior knowledge of trigonometry, exploring a graphing calculator can lead to non-trivial insights <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. For instance, inputting the cosine function `cos(x)` reveals a sinusoidal wave that appears relevant to wave dynamics and cyclical phenomena <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

Tweaking the input `x` by multiplying it by a constant (e.g., `cos(2x)`) "squishes" the wave, increasing its frequency <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Stretching the wave in the Y direction involves modifying the output (e.g., `2*cos(x)`) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Discovery of a [[Trigonometric identities and proofs | Cosine Squared Identity]]

An interesting observation arises when squaring the cosine function, `cos(x)^2` <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. When graphed from 0 to 2π, `cos(x)^2` stays positive, reaching 1 at 0, π, and 2π <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Surprisingly, its graph looks like another cosine wave, but scaled down and oscillating more quickly <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

By manipulating a standard cosine wave, it can be observed that `cos(x)^2` is equivalent to `0.5 * cos(2x) + 0.5` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This identity, `cos^2(x) = (1 + cos(2x)) / 2`, is a significant and non-obvious fact about [[Trigonometric identities and proofs | trigonometric functions]] <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Connection to Exponentials

The behavior of `cos(x)^2` (squaring the output leading to a scaling of the input) is similar to that of exponential functions <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. For example, `(2^x)^2` is equivalent to `2^(2x)` <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. This similarity suggests a hidden relationship between cosine and exponentials, which is a key concept connecting [[Trigonometry and complex numbers connection | trigonometry and complex numbers]] <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

## [[unit circle and complex plane | Sine and Cosine Defined by Circles]]

A fundamental insight into trigonometry is that it is fundamentally about circles, not just triangles <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

### Unit Circle Definition
Imagine a point starting at (1,0) on a [[unit circle and complex plane | unit circle]] (radius of one) <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. As this point moves around the circle at a constant rate, its height (y-coordinate) defines the sine function `sin(θ)` <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. Its x-coordinate defines the cosine function `cos(θ)` <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

The input `θ` (theta) represents the distance walked around the circle, also known as radians <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. For example, walking a distance of π units gets you halfway around the circle, leading to `cos(π) = -1` <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. Similarly, `cos(π/2) = 0` as it corresponds to a 90-degree turn <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

Estimating values like `cos(3)` and `sin(3)` without a calculator involves understanding that `π` (approximately 3.14) means halfway around the circle <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. So, 3 radians is slightly less than halfway, placing the point in the second quadrant. This means `cos(3)` would be close to -1 (around -0.99), and `sin(3)` would be positive but small (around 0.14) <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.

### Radians vs. Degrees
While degrees are intuitive for angles in triangles, mathematicians prefer radians for their natural unit <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>. Radians measure the arc length on a unit circle, meaning 180 degrees equals π radians <a class="yt-timestamp" data-t="00:29:23">[00:29:23]</a>. Thinking in radians is more natural for calculus and advanced mathematical contexts <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>.

## [[Trigonometric identities and proofs | Sine and Cosine Defined by Right Triangles]] (SOH CAH TOA)

The classic way trigonometry is taught involves right triangles, using the mnemonic SOH CAH TOA <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>:
*   **SOH**: `sin(θ) = Opposite / Hypotenuse` <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>
*   **CAH**: `cos(θ) = Adjacent / Hypotenuse` <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>
*   **TOA**: `tan(θ) = Opposite / Adjacent` <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>

**Example: Leaning Tower of Pisa**
A 100-meter tower leaning to make an 80-degree angle with the ground, with the sun directly overhead, casts a shadow <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. This forms a right triangle where the tower is the hypotenuse (100m), the shadow is the adjacent side to the 80-degree angle <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>. Using CAH, the shadow length `s` is `s = 100 * cos(80°)` <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>.

### Connecting Triangles to the [[unit circle and complex plane | Unit Circle]]
The triangle definitions are consistent with the [[unit circle and complex plane | unit circle]] <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>. If any right triangle is scaled so its hypotenuse is 1, its opposite side becomes `sin(θ)` and its adjacent side becomes `cos(θ)` <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>. All such scaled triangles trace out a [[unit circle and complex plane | unit circle]] where the point (x,y) is (`cos(θ)`, `sin(θ)`) <a class="yt-timestamp" data-t="00:28:24">[00:28:24]</a>.

## Computing Specific [[Trigonometric identities and proofs | Trigonometric Values]]

Calculating exact [[Trigonometric identities and proofs | trigonometric values]] by hand is generally difficult without specific geometric symmetries <a class="yt-timestamp" data-t="00:30:48">[00:30:48]</a>.

### Using Equilateral Triangles
Consider an equilateral triangle with side lengths of 1 <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>. Dividing it in half creates two 30-60-90 right triangles <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>.
*   For `sin(π/6)` (which is 30 degrees): The opposite side is 0.5 (half of the base) and the hypotenuse is 1 <a class="yt-timestamp" data-t="00:35:16">[00:35:16]</a>. Thus, `sin(π/6) = 0.5 / 1 = 0.5` <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   For `cos(π/6)`: Using the Pythagorean theorem, `adjacent^2 + opposite^2 = hypotenuse^2` <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>. `adjacent^2 + (0.5)^2 = 1^2`, leading to `adjacent = sqrt(1 - 0.25) = sqrt(0.75) = sqrt(3)/2` <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>. So, `cos(π/6) = sqrt(3)/2` <a class="yt-timestamp" data-t="00:38:34">[00:38:34]</a>.

### The Pythagorean Identity
From the unit circle or a right triangle with hypotenuse 1, the Pythagorean theorem implies the fundamental [[Trigonometric identities and proofs | identity]]: `cos^2(x) + sin^2(x) = 1` <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.
*   **Note on Notation**: `cos^2(x)` is a common convention for `(cos(x))^2`, despite being potentially confusing as `f^2(x)` typically means function composition `f(f(x))` <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.

### Using the Unit Circle for Negative Angles
For `cos(-2π/3)`:
*   A negative angle means moving clockwise around the [[unit circle and complex plane | unit circle]] <a class="yt-timestamp" data-t="00:42:42">[00:42:42]</a>.
*   -2π/3 radians is equivalent to -120 degrees <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a>.
*   This places the point in the third quadrant, where the x-coordinate (cosine) is negative <a class="yt-timestamp" data-t="00:45:47">[00:45:47]</a>.
*   The reference angle to the x-axis is 60 degrees (or π/3 radians), leading to a 30-60-90 triangle <a class="yt-timestamp" data-t="00:46:26">[00:46:26]</a>.
*   The adjacent side (x-coordinate) for a 60-degree angle (with hypotenuse 1) is 0.5 <a class="yt-timestamp" data-t="00:46:39">[00:46:39]</a>.
*   Therefore, `cos(-2π/3) = -0.5` <a class="yt-timestamp" data-t="00:47:08">[00:47:08]</a>.

### Using the Half-Angle Identity
The previously discovered identity `cos^2(x) = (1 + cos(2x)) / 2` can be used to compute values like `cos(π/12)` (15 degrees) <a class="yt-timestamp" data-t="00:48:24">[00:48:24]</a>.
Let `x = π/12`. Then `2x = π/6`.
`cos^2(π/12) = (1 + cos(π/6)) / 2` <a class="yt-timestamp" data-t="00:53:12">[00:53:12]</a>
Since `cos(π/6) = sqrt(3)/2`,
`cos^2(π/12) = (1 + sqrt(3)/2) / 2` <a class="yt-timestamp" data-t="00:54:13">[00:54:13]</a>
`cos(π/12) = sqrt((1 + sqrt(3)/2) / 2)` <a class="yt-timestamp" data-t="00:54:19">[00:54:19]</a>. This is known as the half-angle identity <a class="yt-timestamp" data-t="01:11:59">[01:11:59]</a>.

## Visualizing [[Graphing trigonometric functions and making predictions | Tangent]] and the Pythagorean Theorem

### Geometric Interpretation of [[Graphing trigonometric functions and making predictions | Tangent]]
On the [[unit circle and complex plane | unit circle]], draw a line tangent to the circle at (1,0) <a class="yt-timestamp" data-t="00:58:22">[00:58:22]</a>. Extend the hypotenuse of the triangle (the radius) until it intersects this tangent line <a class="yt-timestamp" data-t="00:58:25">[00:58:25]</a>. The length of this tangent segment, from (1,0) to the intersection point, represents `tan(θ)` <a class="yt-timestamp" data-t="00:58:45">[00:58:45]</a>. As θ approaches π/2 (90 degrees), this length grows infinitely large, explaining why the tangent graph has vertical asymptotes at multiples of π/2 <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>.

### Geometric Proof of the Pythagorean Identity
Consider the triangle inside the [[unit circle and complex plane | unit circle]] with hypotenuse 1, adjacent side `cos(θ)`, and opposite side `sin(θ)` <a class="yt-timestamp" data-t="01:05:24">[01:05:24]</a>.
1.  Draw a perpendicular line from the point (`cos(θ)`, `sin(θ)`) on the circle to the hypotenuse (which is the radius) <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>. This divides the main right triangle into two smaller similar right triangles.
2.  Using the definition of cosine on the smaller triangle formed by the adjacent side: The length of the segment on the hypotenuse (adjacent to `θ` in the smaller triangle) is `cos(θ) * cos(θ) = cos^2(θ)` <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>.
3.  Similarly, using the definition of sine on the other smaller triangle (where the original `sin(θ)` is now a hypotenuse): The length of the other segment on the original hypotenuse is `sin(θ) * sin(θ) = sin^2(θ)` <a class="yt-timestamp" data-t="01:08:55">[01:08:55]</a>.

Since these two segments make up the entire hypotenuse of the original triangle, which has a length of 1, it visually demonstrates that `cos^2(θ) + sin^2(θ) = 1` <a class="yt-timestamp" data-t="01:09:36">[01:09:36]</a>. This constitutes a visual proof of the Pythagorean theorem using trigonometric definitions <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.

This visual interpretation of `cos^2(θ)` (as a segment length) and `sin^2(θ)` (as another segment length) will provide further intuition for the half-angle identity `cos^2(x) = (1 + cos(2x)) / 2` in future discussions <a class="yt-timestamp" data-t="01:11:06">[01:11:06]</a>. The relationship between squaring cosine and scaling its input is a hint at the deeper connection between [[Trigonometry and complex numbers connection | trigonometry and complex numbers]] <a class="yt-timestamp" data-t="01:12:07">[01:12:07]</a>.