---
title: Geometric interpretation of complex numbers
videoId: 5PcpBw5Hbwo
---

From: [[3blue1brown]] <br/> 

[[introduction_to_complex_numbers | Complex numbers]] are a fundamental concept in [[applications_of_complex_numbers_in_engineering_and_mathematics | engineering]], [[complex_numbers_in_mathematics | mathematics]], and quantum mechanics, despite having a "terrible, terrible name" <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The numbers that introduce them are called [[conceptualizing_complex_numbers | imaginary numbers]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## The "Unreal" Start

Historically, the term "imaginary" was coined by Rene Descartes as a derogatory term, meant to mock the idea that such numbers could exist or be considered serious mathematics <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. However, for those in [[applications_of_complex_numbers_in_engineering_and_mathematics | engineering]] or serious [[complex_numbers_in_mathematics | math]], [[introduction_to_complex_numbers | complex numbers]] are as "real a part of their work and their life as real numbers are" <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. While the concept of a number whose square is negative may seem strange <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>, their utility in the real world is a key indicator of their "reality" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

Instead of the initial name, one suggestion for [[introduction_to_complex_numbers | complex numbers]] is "sneaky numbers" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>, but a more fitting name would connote "spinning and rotation" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>, reflecting their elegant use in describing rotation <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## A New Dimension for Numbers

The starting point for [[introduction_to_complex_numbers | complex numbers]] is the definition of a number `i`:

> Assume that there's some number `i` so that `i` squared is equal to negative 1. <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>

This concept often leads to questions about how such a definition is possible <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. On the standard real number line, squaring any number (positive or negative) always results in a positive number <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

To give `i` a "home," the number system is extended beyond a single line. Instead of just the real number line, `i` is proposed to "live in a different dimension" <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, specifically "perpendicularly" to the real number line <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

This proposal suggests that numbers are "two-dimensional" <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. The number `i` is located one unit perpendicularly above the real number line <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This provides a geometric context for `i` and allows for numbers like `2i`, `negative i`, or `negative 2i` by scaling along this new axis <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

## Operations: Addition

Adding [[introduction_to_complex_numbers | complex numbers]] is relatively straightforward, similar to adding vectors <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. For example, if you have a number like `negative 2 + 2i`, it means moving two units in the real direction and then two units in the perpendicular, or imaginary, direction <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. Addition in this two-dimensional system involves adding the real parts together and the imaginary parts together, resulting in a sum like `2 + 3i` for `(4 - i) + (-2 + 4i)` <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

## Operations: Multiplication and Rotation

Where [[introduction_to_complex_numbers | complex numbers]] become particularly interesting geometrically is in their multiplication <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. Unlike vectors in a 2D plane, [[introduction_to_complex_numbers | complex numbers]] *do* have a natural multiplication rule <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>.

### Multiplying by *i*

Consider the multiplication of a [[introduction_to_complex_numbers | complex number]] like `3 + 2i` by `i` <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
Algebraically:
`i * (3 + 2i) = 3i + 2i²` <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>
Since `i²` is defined as `negative 1` <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>, the expression becomes:
`3i + 2(-1) = -2 + 3i` <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>

Geometrically, if you take the point `(3, 2)` (representing `3 + 2i`) and rotate it 90 degrees counterclockwise around the origin, the new coordinates are `(-2, 3)` (representing `-2 + 3i`) <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. This corresponds to swapping the coordinates and then multiplying the first coordinate by negative one <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

This demonstrates that "multiplying by `i` has this action of rotating things by 90 degrees" <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>. This geometric interpretation is a key reason why [[introduction_to_complex_numbers | complex numbers]] are so useful <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### General Complex Multiplication

This rotational property extends beyond just multiplying by `i`. Multiplying any [[introduction_to_complex_numbers | complex number]] `z` by another complex number `c + di` involves the distributive property <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>. The operation `z * (c + di)` can be expressed as `c * z + d * (z * i)` <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.

This means that multiplying by a [[introduction_to_complex_numbers | complex number]] `z` effectively rotates and scales every other [[introduction_to_complex_numbers | complex number]] in the plane <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. This operation preserves parallelism and perpendicularity of lines, applying a consistent transformation across the entire plane <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. This elegant behavior is what makes [[introduction_to_complex_numbers | complex numbers]] invaluable for describing rotations and transformations in various [[applications_of_complex_numbers_in_engineering_and_mathematics | engineering]] and [[complex_numbers_in_mathematics | mathematical]] contexts.