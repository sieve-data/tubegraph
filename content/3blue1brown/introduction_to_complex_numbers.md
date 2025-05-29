---
title: Introduction to complex numbers
videoId: 5PcpBw5Hbwo
---

From: [[3blue1brown]] <br/> 

[[complex_numbers_in_mathematics | Complex numbers]], a concept considered one of math's "absolute all-time favorite pieces" by some, are fundamental to [[applications_of_complex_numbers_in_engineering_and_mathematics | engineering]], [[complex_numbers_in_mathematics | mathematics]] itself, and quantum mechanics <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite their profound importance, they suffer from a "terrible, terrible name" <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The numbers themselves are called "complex numbers," and their foundational components are called "imaginary numbers" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## The Concept of "Real" Numbers

To understand complex numbers, it's helpful to first consider what we define as "real" in the realm of numbers <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. A poll posed the question of which values among 2, the square root of 2, the square root of negative 1, and infinity would be considered to "really exist" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. For many, if a numerical construct is helpful in the real world, it is considered "real" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

Poll results showed a significant number of participants considered the square root of negative one to be "real," while many were uncomfortable extending that reality to infinity <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

> [!tip] Renaming Complex Numbers
> The terms "complex numbers" and "imaginary numbers" are often seen as counter-intuitive and misrepresentative of their significant real-world applications <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Alternatives proposed include "sneaky numbers" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>, or names that connote spinning and rotation <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. [[conceptualizing_complex_numbers | Conceptualizing complex numbers]] in terms of rotation is one of their main uses <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

Historically, the term "imaginary" was coined by Rene Descartes as a derogatory remark, intending to mock the idea that such numbers could be taken as serious math <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. This convention, however, stuck, which is "genuinely absurd" given their utility <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

Engineers and serious mathematicians consider [[complex_numbers_in_mathematics | complex numbers]] as real a part of their work as real numbers <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

## Defining the Imaginary Unit `i`

The starting point for [[complex_numbers_in_mathematics | complex numbers]] is the assumption of a number, `i`, such that `i² = -1` <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This concept often elicits one of two reactions: either acceptance because it's defined that way, or skepticism, questioning whether one can simply define a solution to an otherwise unsolvable problem <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. Normally, squaring any real number, whether positive or negative, always results in a positive number <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## [[geometric_interpretation_of_complex_numbers | Geometric Interpretation of Complex Numbers]]

The peculiar nature of `i` is given a "home" through its [[geometric_interpretation_of_complex_numbers | geometric interpretation]] <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. Instead of living on the real number line, `i` resides in a different, perpendicular dimension <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. It is located one unit perpendicularly above the real number line, with negative `i` one unit below, and multiples like `2i` or `-2i` scaling along this axis <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

Essentially, this proposes that numbers are two-dimensional <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. A complex number combines a real part and an imaginary part, allowing for movement along both the horizontal (real) and vertical (imaginary) axes. For example, to visualize `-2 + 2i`, one moves two units to the left on the real axis and then two units up on the imaginary axis <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## Operations with Complex Numbers

### Addition

Adding [[complex_numbers_in_mathematics | complex numbers]] is straightforward, similar to adding vectors <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a> <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. For example, `(4) + (-2 + 2i)` would result in `2 + 2i` <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. The real parts are added together, and the imaginary parts are added together.

### Multiplication as Rotation

While addition is simple, the "interesting" part of [[complex_numbers_in_mathematics | complex numbers]] emerges with multiplication <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. Unlike vectors, which don't have a direct notion of multiplication in a 2D plane to yield another vector, [[complex_numbers_in_discrete_math | complex numbers]] behave much like real numbers, allowing rules from algebra to carry over <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.

The profound insight is that **multiplication by `i` corresponds to a 90-degree counter-clockwise rotation** in the complex plane <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a> <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>.

Consider the point (3, 2) on a coordinate grid, which can be represented as the complex number `3 + 2i` <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. Rotating this point 90 degrees counter-clockwise results in the point (-2, 3) <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.

Algebraically, multiplying `3 + 2i` by `i` yields:
`i * (3 + 2i) = 3i + 2i²` <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>
Since `i²` is defined as `-1` <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>:
`3i + 2(-1) = -2 + 3i` <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>

This algebraic result `(-2 + 3i)` perfectly matches the geometrically rotated point `(-2, 3)` <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. This connection between multiplication and rotation is not a coincidence <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>. When `i` is multiplied by `3 + 2i`:
1.  The original coordinates (3, 2) are swapped <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
2.  The new real part (which was the original imaginary part, 2) gets multiplied by -1 <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.

This indicates that multiplying by `i` indeed acts as a 90-degree rotation <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>. This property provides a computational mechanism for all types of rotations, not just 90 degrees <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. It allows for elegant descriptions of rotation, which are crucial in many fields <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

The distributive property of [[complex_numbers_in_mathematics | complex numbers]] multiplication helps to understand how a complex number `z` transforms any other complex number `c + di` <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>. If you know what `z` does to 1 and what `z` does to `i`, you can determine what `z` does to any other number by linearity <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>. Multiplication by a complex number applies a constrained rule to the entire plane, preserving parallelism and spacing <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>.

For instance, the product `(2 + i) * (2 - i)` can be worked out using the FOIL (First, Outer, Inner, Last) method:
`2*2 + 2*(-i) + i*2 + i*(-i)` <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>
`= 4 - 2i + 2i - i²`
`= 4 - (-1)`
`= 5`
This demonstrates how [[complex_numbers_in_mathematics | complex numbers]] can be used to simplify [[trigonometry_and_complex_numbers_connection | trigonometric identities]] <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This connection is further explored in topics like [[complex_numbers_and_imaginary_exponents | complex numbers and imaginary exponents]] and [[complex_numbers_and_transformations | complex numbers and transformations]].