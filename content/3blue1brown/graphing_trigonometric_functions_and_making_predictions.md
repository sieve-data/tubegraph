---
title: Graphing trigonometric functions and making predictions
videoId: yBw67Fb31Cs
---

From: [[3blue1brown]] <br/> 

This lecture aims to connect [[trigonometry_and_complex_numbers_connection | trigonometry]] with complex numbers by first revisiting the fundamental concepts of trigonometric functions and their graphical representations <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The approach taken is to explore these functions as if encountering them for the first time, using a graphing calculator to reveal their properties and relationships <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Exploring Cosine through Graphing

Imagine discovering the cosine function for the first time using a graphing calculator like Desmos <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Plotting `cos(x)` immediately shows its relevance to waves and wave dynamics due to its cycling phenomenon <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
Playing with the graph reveals:
*   Tweaking the input `x` by multiplying it by a constant (e.g., `cos(2x)`) *squishes* the graph horizontally, leading to a higher frequency <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   Tweaking the output by multiplying it by a constant (e.g., `2*cos(x)`) *stretches* the graph vertically <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Predicting the Graph of `cos(x)^2`

A particularly interesting observation comes from considering the graph of `f(x) = cos(x)^2` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Focusing on the region from `0` to `2π`, the initial `cos(x)` graph hits `1` at `0`, `-1` at `π`, and `1` at `2π` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
When squaring `cos(x)`:
*   `1^2` remains `1` (at `0` and `2π`) <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   `(-1)^2` becomes `1` (at `π`) <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   All squared values will be positive or zero, causing the graph to stay above or on the x-axis <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

Surprisingly, the graph of `cos(x)^2` looks like another sinusoidal wave, specifically a scaled-down version of the cosine graph that oscillates more quickly <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This discovery, made simply by [[mathematical_functions_and_graphs | playing around with a graphing calculator]], is a non-trivial fact about [[understanding_basic_trigonometric_functions_and_waves | trigonometric functions]] <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Connecting to Exponents

This behavior of `cos(x)^2` (affecting the output `y` but resulting in an input scaling effect) hints at a deeper connection <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. A similar property is observed in exponential functions.
Consider a function `f(x)` where `f(2x) = f(x)^2` <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
The solution to this is `f(x) = 2^x` <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. When `2^x` is squared, it becomes `(2^x)^2 = 2^(2x)`, which is `2^(2x)`. This demonstrates how squaring an exponential function results in scaling its input <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. This parallel suggests a possible, non-obvious relationship between [[trigonometry_and_complex_numbers_connection | trigonometry]] and exponentials <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

### Deriving a Trigonometric Identity

By manipulating the original `cos(x)` graph to match `cos(x)^2`, one can discover a key identity <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>:
1.  **Shift up by 1**: To make `cos(x)` entirely positive like `cos(x)^2`, shift it up by `1`, resulting in `cos(x) + 1` <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
2.  **Halve the output**: The shifted graph is twice as high as `cos(x)^2`, so halve its output: `0.5 * (cos(x) + 1)` <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
3.  **Squish in x-direction**: The new graph still cycles every `2π`, but `cos(x)^2` cycles every `π`. To match this, scale the input by `2`, resulting in `0.5 * (cos(2x) + 1)` <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. This identity is:
    `cos(x)^2 = (1 + cos(2x)) / 2` <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

This identity, often called the half-angle identity (`cos(α/2)^2 = (1 + cos(α))/2`), is crucial and will be revisited in the context of [[trigonometry_and_complex_numbers_connection | complex numbers]] <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.

## Understanding Sine and Cosine

While trigonometric functions are often introduced via triangles, a deeper understanding comes from their connection to circles <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

### [[sine_and_cosine_on_the_unit_circle_and_angles | Unit Circle Definition]]

*   **Sine**: Imagine starting at `(1,0)` on a unit circle (radius 1). As you walk around the circle, `sin(theta)` is defined as your height (y-coordinate) as a function of the distance `theta` walked <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. `sin(x)` starts at `0` because the y-coordinate at `(1,0)` is `0` <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Cosine**: `cos(theta)` is defined as your x-coordinate (distance to the y-axis) as you walk around the unit circle <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. It starts at `1` <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
*   **Radians**: The input `theta` is typically measured in radians, representing the literal distance walked along the arc of the unit circle <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. For example, walking `π` units gets you halfway around the circle, leading to `cos(π) = -1` <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   **Prediction Example**: To predict `cos(3)` and `sin(3)`: `π` is approximately `3.14` <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>. Walking `3` units means you are just shy of halfway around the circle. At this point, the x-coordinate (`cos(3)`) will be negative and very close to `-1` (e.g., `-0.99`), while the y-coordinate (`sin(3)`) will be positive and relatively small (e.g., `0.14`) <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.

### Right Triangle Definition (SOH CAH TOA)

The classic way to remember [[trigonometric_identities_and_proofs | trigonometric identities]] for a right triangle is SOH CAH TOA <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>:
*   **SOH**: `Sine(theta) = Opposite / Hypotenuse` <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>
*   **CAH**: `Cosine(theta) = Adjacent / Hypotenuse` <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>
*   **TOA**: `Tangent(theta) = Opposite / Adjacent` <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>

**Example: Leaning Tower Problem**
A 100-meter tower leans, making an 80-degree angle with the ground. When the sun is directly overhead, its shadow forms a right triangle <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>. The tower itself is the hypotenuse (100m). The shadow is the side adjacent to the 80-degree angle <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>.
Using CAH: `cos(80°) = Shadow / 100` <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>.
Thus, `Shadow = 100 * cos(80°)` <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>.

### Connecting Triangles and the Unit Circle

The triangle definition relates to the unit circle by rescaling any right triangle so its hypotenuse is 1 <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>.
*   If hypotenuse = 1, then the opposite side becomes `sin(theta)` and the adjacent side becomes `cos(theta)` <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.
*   All possible right triangles with a hypotenuse of 1 can be traced by points on a unit circle, where each point's coordinates are `(cos(theta), sin(theta))` for the corresponding angle `theta` <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.
*   Mathematicians prefer radians as a natural unit for angles <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>: `180 degrees = π radians`, `60 degrees = π/3 radians`, `30 degrees = π/6 radians` <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>.

## Computing Specific Values

Calculating exact trigonometric values can be challenging without advanced methods. Some values can be derived using geometric symmetry, like from an equilateral triangle <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>.

### Example: Sine and Cosine of `π/6` (30 degrees)

Consider an equilateral triangle with side lengths of 1 <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>. Bisecting one of its angles (60 degrees, or `π/3` radians) creates a 30-60-90 right triangle <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.
The angle corresponding to 30 degrees is `π/6` radians <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>.
*   **`sin(π/6)`**: For the 30-degree angle, the opposite side is half the original equilateral triangle's side (1/2), and the hypotenuse is 1 <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>.
    `sin(π/6) = (1/2) / 1 = 1/2` <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   **`cos(π/6)`**: The adjacent side can be found using the Pythagorean theorem: `adjacent^2 + (1/2)^2 = 1^2` <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.
    `adjacent^2 + 1/4 = 1`
    `adjacent^2 = 3/4`
    `adjacent = sqrt(3)/2` <a class="yt-timestamp" data-t="00:38:12">[00:38:12]</a>.
    So, `cos(π/6) = (sqrt(3)/2) / 1 = sqrt(3)/2` <a class="yt-timestamp" data-t="00:38:34">[00:38:34]</a>.

### The Pythagorean Identity

From the unit circle or a right triangle with hypotenuse 1, if the legs are `cos(theta)` and `sin(theta)`, then the Pythagorean theorem states:
`cos(x)^2 + sin(x)^2 = 1^2 = 1` <a class="yt-timestamp" data-t="00:39:24">[00:39:24]</a>.
*Note on Notation*: In [[trigonometric_identities_and_proofs | trigonometry]], `cos^2(x)` (or `sin^2(x)`) is a shorthand for `(cos(x))^2` <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. This differs from `f^2(x)` in other [[understanding_function_behavior_beyond_graphs | mathematical functions]], which typically means `f(f(x))` <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>.

### Computing `cos(-2π/3)`

Using the unit circle, `(-2π/3)` means walking `2π/3` units clockwise from `(1,0)` <a class="yt-timestamp" data-t="00:45:41">[00:45:41]</a>.
*   This is equivalent to `-120` degrees <a class="yt-timestamp" data-t="00:46:17">[00:46:17]</a>.
*   The x-coordinate will be negative <a class="yt-timestamp" data-t="00:45:47">[00:45:47]</a>.
*   The reference angle in the third quadrant (relative to the negative x-axis) is `π/3` or 60 degrees.
*   For a 60-degree angle in a unit hypotenuse triangle, the adjacent side is `1/2`. Since it's in the negative x-direction, `cos(-2π/3) = -1/2` <a class="yt-timestamp" data-t="00:46:33">[00:46:33]</a>.

### Computing `cos(π/12)` (15 degrees) using the Identity

The identity `cos^2(x) = (1 + cos(2x)) / 2` is useful for finding values of half-angles <a class="yt-timestamp" data-t="00:48:24">[00:48:24]</a>.
To find `cos(π/12)`:
Let `x = π/12`. Then `2x = π/6`.
`cos^2(π/12) = (1 + cos(π/6)) / 2` <a class="yt-timestamp" data-t="00:53:20">[00:53:20]</a>.
We know `cos(π/6) = sqrt(3)/2` <a class="yt-timestamp" data-t="00:53:43">[00:53:43]</a>.
`cos^2(π/12) = (1 + sqrt(3)/2) / 2` <a class="yt-timestamp" data-t="00:54:13">[00:54:13]</a>.
`cos(π/12) = sqrt((1 + sqrt(3)/2) / 2)` <a class="yt-timestamp" data-t="00:54:23">[00:54:23]</a>.
This value is approximately `0.965`, which makes sense for a small angle close to 1 <a class="yt-timestamp" data-t="00:55:38">[00:55:38]</a>.

## Geometric Interpretation of Tangent and Cosine Squared

### Where is `tan(theta)` on the Unit Circle?

To geometrically interpret `tan(theta)` as a single length on the unit circle:
1.  Draw a unit circle.
2.  Draw the angle `theta` from the origin.
3.  Draw a vertical line (a [[tangent_lines_and_slopes | tangent line]]) at `x=1` (the rightmost point of the circle). This line is perpendicular to the x-axis, thus it is "tangent" to the circle <a class="yt-timestamp" data-t="00:58:11">[00:58:11]</a>.
4.  Extend the line from the origin through the point `(cos(theta), sin(theta))` on the circle until it intersects the vertical line `x=1`.
5.  This forms a new right triangle where the adjacent side to `theta` is 1 (along the x-axis), and the opposite side is the length of the vertical segment from `(1,0)` up to the intersection point <a class="yt-timestamp" data-t="00:58:15">[00:58:15]</a>.
6.  By SOH CAH TOA, `tan(theta) = Opposite / Adjacent = Opposite / 1 = Opposite`. Therefore, this vertical length **is** `tan(theta)` <a class="yt-timestamp" data-t="00:58:49">[00:58:49]</a>.

From this visualization, it's clear that `tan(theta)` starts at `0` (for `theta=0`) and "blows up to infinity" as `theta` approaches `π/2` (90 degrees), where the extending line becomes parallel to the vertical tangent line and never intersects <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>.

### Where are `cos^2(theta)` and `sin^2(theta)` on the Unit Circle?

Consider the standard right triangle within the unit circle, with hypotenuse 1, base `cos(theta)`, and height `sin(theta)` <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>.
1.  Drop a perpendicular line from the point on the unit circle to the hypotenuse of this triangle (which is the x-axis in the standard representation).
2.  This divides the original hypotenuse (which has length 1) into two segments <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.
3.  By using the definition of cosine on the *smaller* right triangle created:
    *   The lower segment of the hypotenuse is the adjacent side to `theta` in the original triangle, and its own hypotenuse is `cos(theta)` <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>.
    *   `cos(theta) = (lower segment) / cos(theta)`. Therefore, the lower segment's length is `cos^2(theta)` <a class="yt-timestamp" data-t="01:07:18">[01:07:18]</a>.
4.  Similarly, the upper segment of the original hypotenuse can be shown to be `sin^2(theta)` by considering the other angle in the original triangle (`90 - theta`), or by considering the upper smaller triangle <a class="yt-timestamp" data-t="01:07:51">[01:07:51]</a>.

This geometric interpretation visually demonstrates the Pythagorean identity `cos^2(theta) + sin^2(theta) = 1` by showing how these two lengths (the projections of the legs onto the hypotenuse) sum up to the total length of the hypotenuse (which is 1) <a class="yt-timestamp" data-t="01:09:36">[01:09:36]</a>. This is a "sneaky" visual proof of the Pythagorean theorem using trigonometry <a class="yt-timestamp" data-t="01:05:40">[01:05:40]</a>.