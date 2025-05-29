---
title: Complex numbers multiplication and rotation
videoId: 5PcpBw5Hbwo
---

From: [[3blue1brown]] <br/> 

[[introduction_to_complex_numbers | Complex numbers]] are a fundamental concept in engineering, mathematics, and quantum mechanics, despite being given a "terrible, terrible name" <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. The components that give rise to [[introduction_to_complex_numbers | complex numbers]] are called [[introduction_to_complex_numbers | imaginary numbers]], a term René Descartes coined derogatorily to imply they were not serious math <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## The Nature of Complex and Imaginary Numbers

At the core of [[introduction_to_complex_numbers | complex numbers]] is the definition of a number `i` such that `i² = -1` <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. This concept often leads to questions about their "reality," as numbers squared typically result in positive values <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a> <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. However, for mathematicians and engineers, [[introduction_to_complex_numbers | complex numbers]] are as "real a part of their work and their life as real numbers are" <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a> <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. They are considered "real" when they are helpful in the real world as a numerical construct <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Geometric Representation

[[introduction_to_complex_numbers | Complex numbers]] are represented as two-dimensional numbers <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a> <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. Unlike real numbers which lie on a single line, `i` exists in a "different dimension," perpendicularly above the real number line <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a> <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a> <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a> <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This allows for numbers to be scaled in both real and [[introduction_to_complex_numbers | imaginary]] directions, like `2i` or `-2i` <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a> <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

## Operations with Complex Numbers

### Addition

Adding [[introduction_to_complex_numbers | complex numbers]] is "pretty straightforward" and similar to adding [[Vector addition and scalar multiplication | vectors]] <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a> <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a> <a class="yt-timestamp" data-t="00:17:21">[00:17:28]</a>. For example, the sum of `(X + Y*i)` and `(A + B*i)` is `(X+A + (Y+B)i)`.

### Multiplication and Rotation

Where [[introduction_to_complex_numbers | complex numbers]] become "interesting" is in their multiplication <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. Unlike [[Vector addition and scalar multiplication | vectors]] in a 2D plane, where there isn't a direct notion of multiplying two [[Vector addition and scalar multiplication | vectors]] to get another [[Vector addition and scalar multiplication | vector]] <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a> <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>, [[introduction_to_complex_numbers | complex numbers]] behave much like real numbers, allowing rules from algebra to carry over <a class="yt-timestamp" data-t="00:18:58">[00:19:03]</a>.

Multiplying a [[introduction_to_complex_numbers | complex number]] by `i` corresponds to a 90-degree counterclockwise rotation <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a> <a class="yt-timestamp" data-t="00:02:31">[00:02:39]</a>.
Consider a point `(3, 2)` on a coordinate grid, which can be represented as `3 + 2i` <a class="yt-timestamp" data-t="00:19:18">[00:19:21]</a>. If we rotate this point 90 degrees counterclockwise, it moves to `(-2, 3)` <a class="yt-timestamp" data-t="00:19:35">[00:19:59]</a> <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. Algebraically, multiplying `(3 + 2i)` by `i` gives:

*   `i * (3 + 2i)` <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a> <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>
*   `= 3i + 2i²` <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>
*   Since `i² = -1`, this becomes `3i + 2(-1)` <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>
*   `= -2 + 3i` <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>

This algebraic result `(-2 + 3i)` corresponds precisely to the geometric 90-degree rotation from `(3, 2)` to `(-2, 3)` <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a> <a class="yt-timestamp" data-t="00:21:12">[00:21:16]</a>. The coordinates are swapped, and the new "real" part is multiplied by negative one <a class="yt-timestamp" data-t="00:21:21">[00:21:44]</a>. This indicates that "multiplying by `i` has this action of rotating things by 90 degrees" <a class="yt-timestamp" data-t="00:21:51">[00:21:53]</a>.

More generally, multiplication by any [[introduction_to_complex_numbers | complex number]] `z` applies a transformation (both scaling and rotation) to the entire [[introduction_to_complex_numbers | complex plane]] <a class="yt-timestamp" data-t="00:22:15">[00:22:29]</a>. This operation preserves parallelism and perpendicularity, and applies a "very constrained rule to the whole plane" <a class="yt-timestamp" data-t="00:26:08">[00:26:11]</a>. The distributive property allows understanding how multiplication by a complex number `z = a + bi` affects any other complex number `c + di`:

*   `z * (c + di) = z * c + z * di` <a class="yt-timestamp" data-t="00:25:05">[00:25:21]</a>

By understanding where `z` lands (scaling `1` by `z`) and where `z * i` lands (scaling `i` by `z`, which is a 90-degree rotation of `z`), the location of `z * (c + di)` can be determined through [[Vector addition and scalar multiplication | vector addition]] of `c * z` and `d * (z * i)` <a class="yt-timestamp" data-t="00:25:23">[00:25:33]</a> <a class="yt-timestamp" data-t="00:26:20">[00:26:26]</a>. This demonstrates how [[introduction_to_complex_numbers | complex numbers]] provide an elegant way to describe rotations <a class="yt-timestamp" data-t="00:02:37">[00:02:39]</a> and makes other pieces of math, like trigonometric identities, "much less error-prone" and more understandable <a class="yt-timestamp" data-t="00:06:59">[00:07:23]</a>.