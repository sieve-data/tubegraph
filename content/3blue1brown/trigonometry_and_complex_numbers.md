---
title: Trigonometry and complex numbers
videoId: 5PcpBw5Hbwo
---

From: [[3blue1brown]] <br/> 

## Introduction to Complex Numbers
[[Complex numbers introduction | Complex numbers]], which the speaker considers a fundamental piece of mathematics for engineering, mathematics, and quantum mechanics, are unfortunately given a "terrible, terrible name" <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The components that lead to complex numbers are called "imaginary numbers" <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The speaker aims to demonstrate the usefulness of imaginary and complex numbers to imbue them with more "reality" <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## The "Reality" of Numbers
A poll was conducted asking the audience which numbers they considered to "really exist" among values like 2, the square root of 2, the square root of negative 1, and infinity <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The speaker's personal view is that any numerical construct helpful in the real world should be considered "real" <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

Poll results showed a significant portion of the audience was comfortable with the square root of negative 1, but many rejected infinity as being "real" <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. Historically, René Descartes coined the term "imaginary" for these numbers derisively, implying they were not serious mathematics, yet the term stuck <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Defining Imaginary Numbers and Their Geometric Home
The starting point for [[complex_numbers_introduction | complex numbers]] is to assume the existence of a number `i` such that `i² = -1` <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This concept initially seems strange, as squaring any real number (positive or negative) results in a positive number <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

To give `i` a "home", [[complex_numbers_and_2d_plane_transformations | complex numbers]] are proposed to be two-dimensional <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Instead of just the real number line, `i` lives in a "different dimension," perpendicularly to the real axis <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. This extends the number system into a plane, where `i` is one unit perpendicularly above the real number line <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. This [[geometric_representation_of_complex_numbers | geometric representation of complex numbers]] is similar to vectors, where numbers can be scaled (e.g., negative 2i) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

## Operations with Complex Numbers

### Addition
Addition of complex numbers is straightforward, similar to adding vectors <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. For example, adding two complex numbers involves summing their real parts and their imaginary parts separately <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. If 4 (real) and 2i (imaginary) are added to -2 (real) and i (imaginary), the sum is 2 + 3i <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

### Multiplication and Rotation
Where things become interesting is in the multiplication of complex numbers <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. Unlike vectors in a 2D plane, complex numbers have a well-defined multiplication operation <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>.

Multiplying by `i` has the action of rotating things by 90 degrees <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>. For a point (3, 2) (representing 3 + 2i), a 90-degree counterclockwise rotation results in (-2, 3) (representing -2 + 3i) <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.
Mechanistically, when multiplying `i` by `3 + 2i`:
`i * (3 + 2i) = 3i + 2i²` <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>
Since `i² = -1`, the expression becomes:
`3i + 2(-1) = -2 + 3i` <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>
This algebraic result corresponds precisely to a 90-degree rotation of the point (3, 2) <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>. The coordinates are swapped (3, 2) to (2, 3), and the first coordinate is multiplied by -1 <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

This ability of complex numbers to encode rotations provides a computational mechanism for various types of rotations, not just 90 degrees <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. This property is crucial for understanding how [[complex_numbers_and_2d_plane_transformations | complex numbers transform a 2D plane]], keeping lines parallel, evenly spaced, and perpendicular <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>.

## Connection to Trigonometry
The lesson will eventually build towards understanding two identities from [[introduction_to_trigonometric_functions | trigonometry]] using [[complex_numbers_introduction | complex numbers]] <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. While trigonometric identities like the cosine of the sum of two angles are "hard to remember" and seem unrelated to the square root of negative one <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, [[complex_numbers_introduction | complex numbers]] can simplify them <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. This demonstrates how [[connection_between_trigonometry_and_complex_numbers | complex numbers]] can make other pieces of math more understandable and useful <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.