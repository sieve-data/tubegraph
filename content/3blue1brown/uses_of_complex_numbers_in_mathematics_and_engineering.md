---
title: Uses of complex numbers in mathematics and engineering
videoId: 5PcpBw5Hbwo
---

From: [[3blue1brown]] <br/> 

[[complex_numbers_introduction | Complex numbers]] are considered one of the most fundamental pieces of mathematics, with significant applications in engineering, mathematics itself, and quantum mechanics <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Despite their importance, they are often burdened with confusing terminology; the numbers themselves are called "complex," and their foundational components are termed "imaginary numbers" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. This naming convention is considered "genuinely absurd" by some, with the term "imaginary" originally coined by Rene Descartes as a derogatory label to imply they were not serious math <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

If renamed to be more intuitive and convey their real-world applications, suggestions include "sneaky numbers" or names that connote "spinning and rotation" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## The "Reality" of Numbers

The concept of what numbers "really exist" is subjective <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. When polled, some people consider numbers like 2, the square root of 2, and the square root of negative 1 as "real," but reject infinity <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. Others might reject the square root of negative 1 <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. For many mathematicians and engineers, if a numerical construct is helpful in the real world, it is considered "real" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Engineers and serious mathematicians widely accept [[complex_numbers_introduction | complex numbers]] as a "real" part of their work and life <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>, <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

## [[geometric_representation_of_complex_numbers | Geometric Representation]] and Operations

The starting point for understanding [[complex_numbers_introduction | complex numbers]] involves assuming the existence of a number `i` such that `i² = -1` <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This is initially counter-intuitive because any "real" number, when squared, results in a positive number <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

To give `i` a "home," the number system is extended to be two-dimensional <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>, <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. Instead of just the real number line, `i` lives perpendicularly to it, with `i` one unit "above" zero and `-i` one unit "below" zero <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. This allows for scaling, such as `-2i` <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

### Addition of [[complex_numbers_introduction | Complex Numbers]]

Adding two-dimensional numbers like this is straightforward, operating similarly to vectors <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. For example, adding `4 - 2i` and `-2 + 5i` results in `2 + 3i` <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. This process is generally not considered the "most interesting" part of [[complex_numbers_introduction | complex numbers]] <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.

### Multiplication of [[complex_numbers_introduction | Complex Numbers]]

Multiplication is where [[complex_numbers_introduction | complex numbers]] become particularly interesting, unlike vectors in a 2D plane where there isn't a direct notion of multiplying two vectors to get another vector <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. [[complex_numbers_introduction | Complex numbers]] behave much like real numbers, allowing rules from algebra to carry over <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.

A key property of multiplication by `i` is its effect on [[geometric_representation_of_complex_numbers | geometric representation]]:
*   Multiplying by `i` rotates a complex number by 90 degrees counterclockwise <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>, <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.
*   Geometrically, a 90-degree rotation of a point `(x, y)` results in `(-y, x)` <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.
*   Algebraically, if a complex number is `3 + 2i`, multiplying by `i` gives `i(3 + 2i) = 3i + 2i² = 3i + 2(-1) = -2 + 3i` <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>. This matches the geometric rotation <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

This indicates that `i`'s defining feature of squaring to negative one directly links to its role in rotation <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

### General Multiplication Properties

Three crucial facts influence [[complex_numbers_introduction | complex number]] multiplication and its rotational effects <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>:
1.  Multiplying any complex number `z` by `1` leaves it unchanged: `z * 1 = z` <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>.
2.  Multiplying any complex number `z` by `i` rotates it 90 degrees: `z * i` results in a 90-degree counterclockwise rotation of `z` <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>.
3.  The distributive property holds for [[complex_numbers_introduction | complex numbers]] <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>. For example, `z * (c + di) = c*z + d*(zi)` <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. This property, combined with the first two, implies that multiplying by any complex number `z` corresponds to a geometric transformation of the entire complex plane <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>. This transformation scales and rotates the plane in a way that keeps lines parallel, evenly spaced, and perpendicular <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>.

This computational mechanism for rotation extends beyond 90-degree turns, allowing for the calculation of all other types of rotations <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.

## Applications

[[complex_numbers_introduction | Complex numbers]] offer very elegant descriptions of how to rotate objects <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>, making them incredibly useful in various fields.

### [[trigonometry_and_complex_numbers | Trigonometry]]

One significant application of [[complex_numbers_introduction | complex numbers]] is in simplifying and understanding [[trigonometry_and_complex_numbers | trigonometric]] identities <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Complex numbers can make complicated identities, like the addition formulas for cosine, much less error-prone and reveal a "very beautiful meaning," where the identities "fall right out" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. Even if one doesn't believe in the "reality" of the square root of negative one, its ability to make other pieces of math more understandable is compelling <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Broader Fields

Beyond rotation and [[trigonometry_and_complex_numbers | trigonometry]], [[complex_numbers_introduction | complex numbers]] are fundamental to:
*   Engineering <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>
*   Mathematics itself <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>
*   Quantum Mechanics <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>