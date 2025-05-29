---
title: Understanding basic trigonometric functions and waves
videoId: yBw67Fb31Cs
---

From: [[3blue1brown]] <br/> 

Trigonometry, at its core, establishes a connection with [[trigonometry_and_complex_numbers_connection | complex numbers]], and a deep understanding of this relationship can strengthen one's grasp of both concepts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This article will explore the fundamentals of trigonometric functions, their meanings, and how they relate to wave dynamics.

## Exploring Trigonometric Functions with Graphs

One way to approach trigonometric functions, even without prior knowledge, is by [[graphing_trigonometric_functions_and_making_predictions | playing around with a graphing calculator]] like Desmos <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### The Cosine Function
The cosine function, for example, produces a sinusoidal wave <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This [[mathematical_functions_and_graphs | graph]] illustrates a cycling phenomenon, making it relevant for studying wave-type dynamics <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **Tweaking Input (Frequency)**: Modifying the input (e.g., `cos(Bx)`) squishes the graph, leading to a higher frequency as the constant `B` increases <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Tweaking Output (Amplitude)**: Modifying the output (e.g., `A * cos(x)`) stretches the graph in the Y direction <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### The Surprising Case of Cosine Squared
An interesting observation arises when squaring the cosine function: `cos(x)^2` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. While squaring typically affects the output (y-direction), `cos(x)^2` appears to be another sinusoidal wave, oscillating more quickly <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This can be observed by focusing on the region from 0 to 2π <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   `cos(0)` is 1, so `cos(0)^2` remains 1 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   `cos(π)` is -1, so `cos(π)^2` becomes 1 <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>, <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   `cos(2π)` is 1, so `cos(2π)^2` remains 1 <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>, <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
This means the squared function will always be positive and oscillate between 0 and 1 <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

Through graphical manipulation, it can be discovered that `cos(x)^2` is equivalent to `(1 + cos(2x)) / 2` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>, <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
To arrive at this identity graphically:
1.  Start with `cos(x)` <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
2.  Shift it up by 1: `cos(x) + 1` (making it entirely positive) <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
3.  Chop it in half: `(cos(x) + 1) / 2` (reducing its height) <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
4.  Squish it in the x-direction by scaling the input by 2: `(cos(2x) + 1) / 2` (changing its cycle from 2π to π) <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
The resulting graph perfectly overlays `cos(x)^2` <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This "half-angle identity" is not obvious but is a non-trivial fact about [[trigonometric_identities_and_proofs | trigonometric functions]] <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>, <a class="yt-timestamp" data-t="01:11:15">[01:11:15]</a>.

Interestingly, this behavior where squaring a function's output relates to scaling its input (i.e., `f(x)^2 = f(2x)`) is also seen in exponential functions like `f(x) = 2^x` <a class="yt-timestamp" data-t="01:11:05">[01:11:05]</a>, <a class="yt-timestamp" data-t="01:11:32">[01:11:32]</a>. This suggests a subtle connection between cosine and exponentials <a class="yt-timestamp" data-t="01:12:37">[01:12:37]</a>.

## Defining Sine and Cosine

### The Unit Circle Definition
The most fundamental way to think about trigonometry is through [[sine_and_cosine_on_the_unit_circle_and_angles | circles]], specifically the unit circle (a circle with a radius of one) <a class="yt-timestamp" data-t="01:13:22">[01:13:22]</a>.
*   **Sine (sin(θ))**: The y-coordinate (height) of a point on the unit circle after walking a distance `θ` (theta) around its circumference, starting from (1,0) <a class="yt-timestamp" data-t="01:13:54">[01:13:54]</a>.
*   **Cosine (cos(θ))**: The x-coordinate (distance to the vertical line) of the same point on the unit circle <a class="yt-timestamp" data-t="01:15:09">[01:15:09]</a>.

The input `θ` is often considered an angle, but in the context of a unit circle, it can also represent the literal distance walked along the circumference <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>.
*   Walking a distance of π (pi) units gets you halfway around the circle, leading to an x-coordinate of -1 (`cos(π) = -1`) <a class="yt-timestamp" data-t="01:16:02">[01:16:02]</a>.
*   Walking a distance of π/2 units (90 degrees) leads to an x-coordinate of 0 (`cos(π/2) = 0`) <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>.

**Radians vs. Degrees**: Mathematicians prefer to think in terms of radians, which are a natural unit based on the distance walked around a unit circle, rather than arbitrary degrees <a class="yt-timestamp" data-t="02:37:13">[02:37:13]</a>. For example, 180 degrees is equivalent to π radians <a class="yt-timestamp" data-t="02:59:32">[02:59:32]</a>.

### The Right Triangle Definition (SOH CAH TOA)
In a typical high school setting, trigonometry is often introduced through right triangles <a class="yt-timestamp" data-t="02:25:25">[02:25:25]</a>. The mnemonic SOH CAH TOA defines the relationships:
*   **SOH**: **S**ine = **O**pposite / **H**ypotenuse <a class="yt-timestamp" data-t="02:11:42">[02:11:42]</a>, <a class="yt-timestamp" data-t="02:31:36">[02:31:36]</a>.
*   **CAH**: **C**osine = **A**djacent / **H**ypotenuse <a class="yt-timestamp" data-t="02:14:48">[02:14:48]</a>, <a class="yt-timestamp" data-t="02:19:04">[02:19:04]</a>.
*   **TOA**: **T**angent = **O**pposite / **A**djacent <a class="yt-timestamp" data-t="02:18:23">[02:18:23]</a>, <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

This triangle-based definition can be connected to the unit circle by scaling any right triangle so its hypotenuse is 1 <a class="yt-timestamp" data-t="02:44:02">[02:44:02]</a>. In such a triangle, the opposite side length becomes `sin(θ)` and the adjacent side length becomes `cos(θ)`, effectively mapping to the y and x coordinates on the unit circle respectively <a class="yt-timestamp" data-t="02:48:08">[02:48:08]</a>.

**Geometric Interpretation of Tangent**: On the unit circle, if you draw a line tangent to the circle at (1,0) and extend the radius corresponding to angle `θ`, the length of the segment from (1,0) to where it intersects the tangent line is `tan(θ)` <a class="yt-timestamp" data-t="00:57:37">[00:57:37]</a>. As `θ` approaches π/2 (90 degrees), the tangent value blows up to infinity because the adjacent side approaches zero <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>.

## Computing Trigonometric Values

Calculating exact trigonometric values by hand is generally difficult without specific geometric settings or advanced techniques <a class="yt-timestamp" data-t="03:08:42">[03:08:42]</a>.

### Key Values from Symmetry
Some values can be derived using geometric symmetry, such as from an equilateral triangle:
*   Consider an equilateral triangle with side lengths of 1 <a class="yt-timestamp" data-t="03:19:54">[03:19:54]</a>. Each angle is 60 degrees (π/3 radians) <a class="yt-timestamp" data-t="03:20:59">[03:20:59]</a>.
*   Bisecting one of its angles creates a 30-60-90 right triangle <a class="yt-timestamp" data-t="03:28:44">[03:28:44]</a>.
*   The hypotenuse remains 1, the side opposite the 30-degree angle (π/6 radians) becomes 1/2 <a class="yt-timestamp" data-t="03:52:05">[03:52:05]</a>.
    *   Therefore, `sin(π/6) = Opposite/Hypotenuse = (1/2)/1 = 1/2` <a class="yt-timestamp" data-t="03:55:04">[03:55:04]</a>.
*   Using the Pythagorean theorem (`a^2 + b^2 = c^2`), the adjacent side to the 30-degree angle can be found: `(1/2)^2 + Adjacent^2 = 1^2` <a class="yt-timestamp" data-t="03:58:01">[03:58:01]</a>.
    *   `Adjacent^2 = 1 - 1/4 = 3/4` <a class="yt-timestamp" data-t="03:59:12">[03:59:12]</a>.
    *   `Adjacent = sqrt(3)/2` <a class="yt-timestamp" data-t="04:00:23">[04:00:23]</a>.
    *   Therefore, `cos(π/6) = Adjacent/Hypotenuse = (sqrt(3)/2)/1 = sqrt(3)/2` <a class="yt-timestamp" data-t="03:47:04">[03:47:04]</a>.

### The Pythagorean Identity
A crucial [[trigonometric_identities_and_proofs | trigonometric identity]] derived directly from the Pythagorean theorem on a unit circle is:
`cos(x)^2 + sin(x)^2 = 1` <a class="yt-timestamp" data-t="03:59:01">[03:59:01]</a>.
This identity implies that if one knows the value of sine, they can determine cosine, and vice-versa <a class="yt-timestamp" data-t="03:59:52">[03:59:52]</a>.

A common notation for `(cos(x))^2` is `cos^2(x)` and for `(sin(x))^2` is `sin^2(x)`, despite this convention being unusual in other areas of mathematics where `f^2(x)` often means applying the function twice (e.g., `f(f(x))`) <a class="yt-timestamp" data-t="04:00:04">[04:00:04]</a>.

### Applying Identities: Cosine of π/12
The identity `cos^2(x) = (1 + cos(2x)) / 2` (also known as the half-angle identity for cosine, or `cos(α/2) = sqrt((1 + cos(α))/2)` <a class="yt-timestamp" data-t="01:11:37">[01:11:37]</a>) can be used to compute values like `cos(π/12)` (15 degrees) <a class="yt-timestamp" data-t="04:47:57">[04:47:57]</a>:
1.  Let `x = π/12`. Then `2x = π/6` <a class="yt-timestamp" data-t="05:31:07">[05:31:07]</a>.
2.  `cos^2(π/12) = (1 + cos(π/6)) / 2` <a class="yt-timestamp" data-t="05:33:43">[05:33:43]</a>.
3.  Substitute `cos(π/6) = sqrt(3)/2`: `cos^2(π/12) = (1 + sqrt(3)/2) / 2` <a class="yt-timestamp" data-t="05:41:07">[05:41:07]</a>.
4.  Solve for `cos(π/12)`: `cos(π/12) = sqrt((1 + sqrt(3)/2) / 2)` <a class="yt-timestamp" data-t="05:46:17">[05:46:17]</a>.
This demonstrates how [[trigonometric_identities_and_proofs | identities]] extend the ability to make concrete computations, even for angles not easily derived from basic symmetric triangles <a class="yt-timestamp" data-t="05:57:08">[05:57:08]</a>.

## Visualizing Cosine Squared

The geometric interpretation of `cos^2(θ)` and `sin^2(θ)` can be found on the unit circle <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.
If a right triangle within the unit circle has a hypotenuse of 1, and its legs are `cos(θ)` and `sin(θ)`:
1.  Draw a perpendicular line from the right-angle vertex down to the hypotenuse <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.
2.  This projection divides the hypotenuse into two segments <a class="yt-timestamp" data-t="01:10:35">[01:10:35]</a>.
3.  The segment adjacent to the angle `θ` (at the origin) is `cos^2(θ)` <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>, <a class="yt-timestamp" data-t="01:07:24">[01:07:24]</a>.
4.  The other segment is `sin^2(θ)` <a class="yt-timestamp" data-t="01:09:32">[01:09:32]</a>.
Since these two segments make up the entire hypotenuse (which is 1), this visualization provides an intuitive proof of the Pythagorean identity `cos^2(θ) + sin^2(θ) = 1` <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.

The insights gained from [[graphing_trigonometric_functions_and_making_predictions | playing with graphs]] and understanding these fundamental definitions lay the groundwork for deeper connections, particularly with [[trigonometry_and_complex_numbers_connection | complex numbers]] <a class="yt-timestamp" data-t="01:11:05">[01:11:05]</a>.