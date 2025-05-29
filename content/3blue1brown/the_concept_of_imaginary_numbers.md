---
title: The concept of imaginary numbers
videoId: 5PcpBw5Hbwo
---

From: [[3blue1brown]] <br/> 

[[Complex numbers in mathematics | Complex numbers]], specifically their [[introduction_to_complex_numbers | imaginary]] components, are described as incredibly fundamental to engineering, mathematics, and quantum mechanics, despite having what is considered a "terrible, terrible name" <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The term "imaginary numbers" is particularly criticized, with even Rene Descartes coining the term as a derogatory one, meant to imply they were not serious mathematics <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. However, anyone in engineering or serious math recognizes [[applications_of_complex_numbers_in_engineering_and_mathematics | complex numbers]] as just as real a part of their work as real numbers <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

## Defining Imaginary Numbers

The starting point for [[conceptualizing_complex_numbers | complex numbers]] is the assumption of a number `i` such that `i^2 = -1` <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This concept often elicits skepticism, as traditionally, squaring any real number (positive or negative) always yields a positive result <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. The question arises: "Hang on a second, you can do that?" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Yet, the usefulness of `i` in the real world is seen as a justification for its "reality" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### A New Dimension for Numbers

To give `i` a "home," the number system is extended to be two-dimensional <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Instead of just the real number line, `i` is said to live in a different, perpendicular dimension <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. It's positioned one unit perpendicularly above the real number line, with `-i` residing below it <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This extension, while initially requiring a "lot on faith" from students <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>, becomes foundational.

## Operations with Complex Numbers

### Addition

Adding [[complex numbers and imaginary exponents | complex numbers]] is straightforward, much like adding vectors <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. If you have a complex number like `a + bi` (where `a` is the real part and `b` is the imaginary part), addition involves simply adding the real parts together and the imaginary parts together separately <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. For example, `(4) + (-2 + 2i)` would result in `2 + 2i` <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. This suggests that there is nothing particularly "complicated" about complex number addition <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.

### Multiplication and Rotation

Where [[complex numbers and transformations | complex numbers]] become particularly interesting is in their multiplication <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. Unlike vectors in a 2D plane which lack a direct notion of multiplication that yields another 2D vector, [[complex numbers in discrete math | complex numbers]] behave much like real numbers, allowing standard algebraic rules to carry over <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.

A key insight is that **multiplication by `i` corresponds to a 90-degree rotation** <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>.

*   **Algebraic Process**: When multiplying a complex number `(a + bi)` by `i`, the distributive property applies. For example, `i * (3 + 2i)`:
    *   `i * 3 = 3i`
    *   `i * 2i = 2 * i^2`
    *   Since `i^2 = -1`, `2 * i^2 = -2`
    *   Thus, `i * (3 + 2i) = -2 + 3i` <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.
*   **Geometric Interpretation**: If you start with a point (or vector) `(3, 2)` representing `3 + 2i` on the [[Geometric interpretation of complex numbers | complex plane]], and then rotate it 90 degrees counterclockwise, the new coordinates are `(-2, 3)` <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. This precisely matches the algebraic result `(-2 + 3i)` <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>. This consistency provides significant reassurance that the operation of multiplying by `i` behaves as expected <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.

The ability to perform 90-degree rotations through multiplication by `i` hints at a broader utility: [[complex numbers and transformations | complex numbers]] provide a computational mechanism for all other types of rotations, not just 90-degree ones <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.

When multiplying a complex number `z` by any other complex number `(c + di)`, the distributive property `z * (c + di) = c*z + d*(z*i)` holds <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. This means that the multiplication of [[complex numbers and imaginary exponents | complex numbers]] applies a very constrained rule to the entire plane, maintaining parallelism and even spacing, effectively performing a rotation and scaling transformation on all points <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>.

The elegance of [[complex numbers and transformations | complex numbers]] is further highlighted by their ability to simplify complex trigonometric identities. Identities that are difficult to remember become "much less error-prone" and "just fall right out" when approached with complex numbers <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. This makes them a useful tool for understanding other pieces of mathematics <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.