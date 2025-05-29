---
title: Imaginary numbers and their reality
videoId: 5PcpBw5Hbwo
---

From: [[3blue1brown]] <br/> 

[[complex_numbers_introduction | Complex numbers]], and specifically their imaginary components, are described as one of the most fundamental pieces of math, crucial to engineering, mathematics, and quantum mechanics <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Despite their widespread application, they are burdened with what is considered a "terrible, terrible name" <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, particularly "imaginary numbers" <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## The Question of Existence

The perception of what constitutes "real" numbers is subjective <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. A poll asking participants which values they consider to "really exist" included 2, square root of 2, square root of negative 1, and infinity <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Results showed a split, with many rejecting infinity as real but being comfortable with the square root of negative 1 <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

The speaker's personal view is that any numerical construct that is "helpful in the real world" should be considered real <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. The goal is to demonstrate the usefulness of imaginary and complex numbers to imbue them with more "reality" <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### The Misleading Name
The term "imaginary" was coined by Rene Descartes as a derogatory term, meant to mock the idea that such a number could exist or be taken seriously in mathematics <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. The continued use of this name is considered "genuinely absurd" <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a> given their utility.

If renamed, the speaker suggests a name connoting "spinning and rotation" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, while a friend proposed "sneaky numbers" <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. The current names fail to convey their "numerous applications in the real world" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Defining and Locating Imaginary Numbers

The starting point for [[complex_numbers_introduction | complex numbers]] involves assuming the existence of a number 'i' such that `i² = -1` <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This definition can seem strange or counterintuitive to students, who might question the ability to simply define a solution for a previously unsolvable problem <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### A New Dimension
Unlike real numbers, which exist on a one-dimensional number line, 'i' is given a "home" in a "different dimension" <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. This dimension is perpendicular to the real number line <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, essentially proposing that numbers become two-dimensional <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. 'i' is located one unit perpendicularly above the real number line, with '-i' below it, and multiples like '2i' scaled accordingly <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This [[geometric_representation_of_complex_numbers | geometric representation of complex numbers]] is key to understanding their behavior.

> "Essentially it's proposing that numbers be two-dimensional and that i has a very specific home, one unit perpendicular, uh, perpendicularly above the real number line." <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>

## Operations with Complex Numbers

### Addition
Adding [[complex_numbers_introduction | complex numbers]] is straightforward, similar to adding vectors <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. If you have a complex number like `3 + 2i` (represented as a point `(3,2)`) and add another, say `(-1 + i)` (represented as `(-1,1)`), the result `(2 + 3i)` is found by adding the real parts and the imaginary parts separately: `(3 + (-1)) + (2 + 1)i = 2 + 3i` <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

### Multiplication as Rotation
Where [[complex_numbers_introduction | complex numbers]] become particularly interesting is in their multiplication <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. Unlike vectors in a 2D plane, complex numbers have a natural multiplication rule <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

Multiplying a complex number by 'i' performs a 90-degree counterclockwise rotation on the complex plane <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.
For example, if you take the complex number `3 + 2i` (represented as the point `(3,2)`) and multiply it by `i`:
`i * (3 + 2i) = 3i + 2i²` <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>
Since `i² = -1`, this becomes `3i + 2(-1) = -2 + 3i` <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>.
Geometrically, the point `(3,2)` is rotated 90 degrees counterclockwise to `(-2,3)` <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. This action involves swapping the coordinates and multiplying the first one by negative one <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

This [[connection_between_numerical_and_geometric_understandings | connection between numerical and geometric understandings]] shows that multiplying by 'i' has the action of rotating things by 90 degrees <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>. This characteristic provides a "computational mechanism for all of the other types of rotations that you might want to do that might not necessarily be 90 degrees" <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>.

## Utility and Applications

Complex numbers simplify concepts that are otherwise difficult to remember or derive in other areas of mathematics. For example, trigonometric identities, such as the cosine of the sum of two angles (`cos(A+B)`), which are "pretty hard to remember" <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a> <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a> and involve "long thing[s] in terms of cosines and sines of the original two angles" <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>, become much less error-prone and "just falls right out" <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a> when approached with [[complex_numbers_introduction | complex numbers]].

> "Even if you don't necessarily believe in the reality of the square root of negative one, you at the very least have to admit that it's interesting that it can make other pieces of math useful, that other pieces of math a little bit more understandable too." <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>

Engineers and mathematicians consider complex numbers "as real a part of their work and their life as real numbers are" <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a> <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. They behave much like real numbers, allowing rules from algebra to carry over <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>, unlike some other extended number systems (e.g., in vector algebra, there's no general notion of multiplying two 2D vectors to get another 2D vector) <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>.