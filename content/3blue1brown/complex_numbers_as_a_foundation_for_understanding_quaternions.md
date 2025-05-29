---
title: Complex numbers as a foundation for understanding quaternions
videoId: d4EgbgTm0Bg
---

From: [[3blue1brown]] <br/> 

Quaternions are an often underappreciated number system that extends [[complex_numbers_introduction | complex numbers]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Just as [[complex_numbers_introduction | complex numbers]] are a two-dimensional extension of real numbers, quaternions are a four-dimensional extension of [[complex_numbers_introduction | complex numbers]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. While not just mathematical constructs, they possess pragmatic utility for describing [[applications_of_quaternions_in_threedimensional_rotations_and_quantum_mechanics | rotation in three dimensions]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a> and even for [[applications_of_quaternions_in_threedimensional_rotations_and_quantum_mechanics | quantum mechanics]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Historical Context and Development

The [[history_and_discovery_of_quaternions_by_william_rowan_hamilton | Irish mathematician William Rowan Hamilton]] spent a significant portion of his life attempting to discover a three-dimensional number system analogous to the [[complex_numbers_introduction | complex numbers]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. His breakthrough occurred on October 16, 1843, when he realized that the solution wasn't to add a single dimension to [[complex_numbers_introduction | complex numbers]], but rather to add two more imaginary dimensions, totaling three imaginary dimensions, with real numbers existing perpendicular to that in a fourth dimension <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. He famously carved the crucial equation describing these three imaginary units into the Broom Bridge in Dublin <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

At the time, the modern notion of [[linear_algebra_foundations | vectors]] with dot and cross products was not standardized <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Hamilton strongly advocated for quaternions as the primary language for describing three-dimensional space <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. However, the perceived confusion of quaternion multiplication led to resistance from other mathematicians <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

Decades later, the computing industry spurred a resurgence of quaternions, particularly among programmers involved in graphics, robotics, and 3D orientation <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This is due to their elegant and computationally efficient way to describe 3D rotations, which also avoids many numerical errors common in other methods <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. The 20th century also saw quaternions gaining relevance in [[applications_of_quaternions_in_threedimensional_rotations_and_quantum_mechanics | quantum mechanics]], as their description of actions in four dimensions is pertinent to two-state systems like electron spin or photon polarization <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Analogous Visualization: From 1D to 4D

To understand quaternions geometrically, an analogy is drawn by first explaining [[complex_numbers_introduction | complex numbers]] to a hypothetical being ("Linus the Linelander") who only understands one dimension <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This process then scales up to understanding 3D rotations and, finally, quaternions in four dimensions.

### Describing Complex Numbers to a 1D Being

Linus the Linelander's mind is limited to one-dimensional geometry and the algebra of real numbers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. While [[complex_numbers_introduction | complex numbers]] can be defined purely algebraically (e.g., `a + bi` where `i * i = -1`) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>, a deeper [[geometric_representation_of_complex_numbers | understanding comes from their geometry]] <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

For those who understand two dimensions, [[uses_of_complex_numbers_in_mathematics_and_engineering | multiplying two complex numbers]], `z` and `w`, can be visualized as `z` acting as a function that rotates and stretches `w` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. This concept of the left number transforming space is key to understanding quaternion multiplication <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

The challenge for Linus is understanding rotation, an intrinsically two-dimensional idea <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. However, since rotation involves only one degree of freedom (the angle), it's possible to associate all rotations to Linus's one-dimensional world using a [[geometric_representation_of_complex_numbers | stereographic projection]] <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. This projection maps the unit circle of the complex plane onto a line <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

When the unit circle of [[complex_numbers_introduction | complex numbers]] is rotated (e.g., by multiplying by `i`), Linus observes a strange morphing action on his line <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. This motion, though unusual, conveys the core idea that multiplying by `i` four times returns to the starting point (`i^4 = 1`) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Extending to a Hypothetical 3D System

The next step in the analogy introduces "Felix the Flatlander," who understands two-dimensional geometry <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. To explain 3D rotations, a conceptual 3D number system is proposed, extending the complex plane with a third axis `j` <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. However, it's not possible to define a useful notion of multiplication for such a 3D system <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

Despite this, the unit sphere in this 3D space (all numbers a distance of 1 from the origin) can be projected onto Felix's 2D plane using [[geometric_representation_of_complex_numbers | stereographic projection]] <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. The point at 1 (north pole) maps to the center, the northern hemisphere maps inside the unit circle, and the unit circle itself (passing through `i`, `j`, `-i`, `-j`) remains fixed <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. The southern hemisphere maps outside the unit circle, with -1 mapping to a point at infinity <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

When the sphere rotates, Felix observes warping and transformation of projected circles and lines <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. For example, a 90-degree rotation about the j-axis transforms the unit circle into a vertical line <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. From a 3D perspective, this is rigid motion; the warping is an artifact of the projection <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

## Quaternions: A Four-Dimensional System

Quaternions include real numbers and three distinct imaginary dimensions, represented by units `i`, `j`, and `k` <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. These three imaginary dimensions are mutually perpendicular to each other and to the real number line <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. A quaternion is written with four real numbers and resides in four-dimensional space <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>, often divided into a real/scalar part and a 3D imaginary part <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. Hamilton coined the term "vector" for quaternions with no real part (only `i`, `j`, `k` components) <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.

### Quaternion Multiplication and Geometry

Quaternion multiplication can be defined algebraically by rules for how `i`, `j`, and `k` multiply together (e.g., `i*j = k`, `j*i = -k`) <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. This algebraic definition is compact and computationally efficient for programming applications <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. The rules also elegantly incorporate the [[linear_algebra_foundations | dot product and cross product]] <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.

However, a deeper understanding comes from the four-dimensional [[geometric_representation_of_complex_numbers | geometry of quaternion multiplication]] <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. Similar to [[complex_numbers_and_2d_plane_transformations | complex numbers]], multiplying one quaternion (`q1`) by another (`q2`) scales `q2` by `q1`'s magnitude, followed by a special type of rotation in four dimensions <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. These 4D rotations correspond to the hypersphere of quaternions (distance 1 from the origin) <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

Analogous to the previous projections, the unit hypersphere is stereographically projected into our 3D space <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. The point at 1 projects to the center of our space <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>. A unit sphere passing through `i`, `j`, and `k` on the unit hypersphere remains fixed under projection, representing the unaltered part of the hypersphere—all unit quaternions with a real part of zero <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

### Visualizing 4D Quaternion Actions

The action of multiplying a unit quaternion `q` by any other quaternion from the left can be visualized as two separate 2D rotations, happening perpendicularly and in sync, a phenomenon possible only in four dimensions <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.

For example, multiplication by `i`:
*   The circle through 1 and `i` (seen as a line) rotates 90 degrees: 1 goes to `i`, `i` goes to -1 (at infinity), -1 goes to `-i`, and `-i` goes to 1 <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.
*   The circle perpendicular to this one, passing through `j` and `k`, also rotates 90 degrees according to a right-hand rule: pointing the thumb from 1 to `i` causes the fingers to curl in the direction of the `j-k` circle's rotation <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. Thus, `j` goes to `k`, `k` to `-j`, `-j` to `-k`, and `-k` to `j` <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.

This concept of perpendicular, synchronous rotations provides an intuition for quaternion multiplication. The entire 4D transformation is locked in by understanding what a quaternion does to these key circles <a class="yt-timestamp" data-t="00:25:45">[00:25:45]</a>.

### Non-Commutativity

A crucial property of quaternion multiplication is that it is not commutative; the order of multiplication matters <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>. For example, `i * j = k`, but `j * i = -k` <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>. This behavior is analogous to how rotations in 3D space are not commutative (e.g., rotating about the z-axis then x-axis yields a different result than x-axis then z-axis) <a class="yt-timestamp" data-t="00:29:12">[00:29:12]</a>.

### Left vs. Right Multiplication

Quaternions can act by either left or right multiplication <a class="yt-timestamp" data-t="00:29:31">[00:29:31]</a>. When thinking of `i * j`, `i` acts as a function on `j` (left multiplication), and the right-hand rule applies to the perpendicular circle <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>. For right multiplication (e.g., `j` acting on `i`), a similar rule applies, but using the left hand <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>. This distinction is vital for understanding how unit quaternions describe [[applications_of_quaternions_in_threedimensional_rotations_and_quantum_mechanics | 3D rotation]] through a process called conjugation <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>.