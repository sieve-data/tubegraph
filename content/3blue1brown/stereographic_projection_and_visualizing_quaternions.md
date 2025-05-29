---
title: Stereographic projection and visualizing quaternions
videoId: d4EgbgTm0Bg
---

From: [[3blue1brown]] <br/> 

Quaternions are a [[mathematical_properties_and_noncommutative_nature_of_quaternions | fascinating and often underappreciated number system]] that extend complex numbers into four dimensions <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Initially viewed with skepticism in the 19th century, their utility for describing [[applications_of_quaternions_in_3d_rotations_and_quantum_mechanics | rotation in three dimensions]] and in [[applications_of_quaternions_in_3d_rotations_and_quantum_mechanics | quantum mechanics]] led to a resurgence of interest, particularly in the computing industry for graphics and robotics <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Visualizing these four-dimensional entities and their multiplication requires special techniques, such as stereographic projection <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Historical Context

The [[historical_discovery_and_significance_of_quaternions | discovery of quaternions]] by Irish mathematician William Rowan Hamilton in 1843 was a famous event in mathematics <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. After years of seeking a three-dimensional number system analogous to complex numbers, Hamilton realized that he needed to add *three* imaginary dimensions to the real numbers, totaling four dimensions <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. He famously carved the crucial equation describing these three imaginary units into Broom Bridge in Dublin <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

At the time, the modern notion of [[vector_representation_and_coordinate_systems | vectors]] with dot and cross products didn't exist in a standardized form <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Hamilton advocated for quaternions as the primary language to describe [[threedimensional_linear_transformations | three-dimensional space]] <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. However, the "confusing notion" of [[quaternion_multiplication_and_fourdimensional_geometry | quaternion multiplication]] led to resistance, with some mathematicians even calling them "evil" due to their non-commutative nature <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This non-commutative property is even believed to be referenced in the Mad Hatter scene from Alice in Wonderland <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Stereographic Projection as a Visualization Tool

To visualize [[quaternion_multiplication_and_fourdimensional_geometry | quaternion multiplication]] in its "full four-dimensional glory," stereographic projection is employed <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This method maps a circle onto a line, a sphere into a plane, or even a 4D hypersphere into 3D space <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### Analogy 1: Linus the Linelander (2D to 1D)

To understand visualizing quaternions, one can first imagine explaining complex numbers to "Linus the Linelander," a hypothetical being who only understands one-dimensional geometry and real numbers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

Complex numbers are a two-dimensional extension of real numbers, expressed as `a + bi`, where `i * i = -1` <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. While complex [[quaternion_multiplication_and_fourdimensional_geometry | multiplication]] can be defined algebraically, its geometric interpretation—as a rotation and stretching action on the plane—is crucial <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

Linus understands stretching (multiplication by real numbers), but rotation is intrinsically two-dimensional <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. However, since rotation involves only one degree of freedom (the angle), it can be associated with Linus's one-dimensional world using a stereographic projection <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>:

*   **Projection**: For every point on the unit circle (complex numbers a distance 1 from 0), a line is drawn from -1 through that point. Where it intersects a vertical line through the circle's center is where the point is projected <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
    *   The point 1 projects to the center of the line <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
    *   `i` and `-i` stay fixed <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
    *   The point -1 projects to "infinity" on the line <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Perception of Rotation**: When the unit circle is rotated, Linus sees a "strange morphing action" on his line <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. For example, multiplying by `i` (a 90-degree counterclockwise rotation) makes the point at `i` slide off to infinity, and the point at infinity return to `-i` <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. This "weird motion" allows Linus to grasp that `i^4 = 1` <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

### Analogy 2: Felix the Flatlander (3D to 2D)

Next, one considers "Felix the Flatlander," who understands two-dimensional geometry <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. The goal is to explain rotations of a sphere to Felix <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

Imagine extending complex numbers with a third axis, `j`, perpendicular to the complex plane, aligning the real number line along the z-direction and `i` and `j` axes in the x and y directions <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. While a useful multiplication for a 3D number system doesn't exist, this setup serves as an analogy <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

The unit sphere consists of all points a distance 1 from the origin <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. Stereographic projection maps this 2D surface to Felix's horizontal plane (defined by the `i` and `j` axes) <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>:

*   **Projection**: A line is drawn from -1 (south pole) through a point on the sphere to where it intersects the plane <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
    *   The point 1 (north pole) projects to the center of the plane <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
    *   The northern hemisphere maps inside the unit circle of the `i-j` plane <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
    *   Crucially, the unit circle passing through `i`, `j`, `-i`, `-j` stays fixed in place, unaltered by the projection <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. This circle is an "honest part" of the unit sphere Felix sees <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.
    *   The southern hemisphere maps outside this unit circle <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
    *   The point -1 again projects to "infinity" <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
*   **Perception of Rotation**: When the sphere rotates, Felix sees circles and lines morphing in his space <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. For example, a 90-degree rotation about the `j`-axis (bringing 1 to `i`, `i` to -1, etc.) makes Felix's unit circle transform into a vertical line, and the red vertical line transforms into the unit circle <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. From our 3D perspective, this is rigid motion, but to Felix, it appears as "stretching or morphing" <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

## Visualizing Quaternions in 3D Space (4D to 3D)

Quaternions include real numbers and three imaginary dimensions, represented by the units `i`, `j`, and `k` <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. Each is perpendicular to the real number line and to each other <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. A quaternion can be written with four real numbers, often broken into a scalar (real) part and a 3D imaginary part <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. Hamilton coined the term "vector" for quaternions with no real part <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.

[[quaternion_multiplication_and_fourdimensional_geometry | Quaternion multiplication]] involves scaling and a "very special type of rotation in four dimensions" <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. This 4D rotation corresponds to the "hypersphere of quaternions" (all quaternions a distance 1 from the origin) <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

Stereographic projection of this 4D hypersphere into our 3D space works analogously to the previous examples <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>:

*   **Projection**: Projecting from the number -1 (which sits on the real number line perpendicular to our 3D space) <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
    *   The number 1 projects into the center of our 3D space <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
    *   A whole sphere passing through `i`, `j`, and `k` on the unit hypersphere stays fixed in place under the projection <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>. This "unit sphere" in our 3D space represents the "only unaltered part" of the hypersphere and corresponds to unit quaternions with a zero real part (unit [[vector_representation_and_coordinate_systems | vectors]]) <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.
    *   Unit quaternions with positive real parts project inside this unit sphere <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.
    *   Unit quaternions with negative real parts project outside this unit sphere <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>.
    *   The number -1 sits at the "point at infinity" <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
*   **Interpretation**: Although points appear closer or farther from the origin in our 3D projection, they all represent unit quaternions and thus have the same magnitude (distance from 0 in 4D) <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>. Lines in the 3D projection represent circles on the hypersphere, and planes represent spheres on the hypersphere that pass through -1 <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.

### Visualizing Quaternion Multiplication

The action of multiplying by a unit quaternion from the left can be thought of as "two separate 2D rotations, happening perpendicular to and in sync with each other in a way that could only ever be possible in four dimensions" <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.

*   **Example: Multiplication by `i`**:
    *   The circle passing through 1 and `i` (which we see as a line) rotates 90 degrees: 1 goes to `i`, `i` goes to -1 (off to infinity), -1 returns to `-i`, and `-i` goes to 1 <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.
    *   The circle perpendicular to that one, passing through `j` and `k`, also rotates 90 degrees according to a **right-hand rule**: If the thumb points from 1 to `i`, the curled fingers indicate the direction of rotation for the `j-k` circle <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. So, `j` goes to `k`, `k` to `-j`, `-j` to `-k`, and `-k` to `j` <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.
    *   This action of repeatedly multiplying by `i` on the projected `ijk` sphere causes it to rotate into a plane, then back to its original position (reversed orientation), then a plane again, and finally back to its starting point after four iterations (`i^4 = 1`) <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.

*   **General Left Multiplication**: For any unit quaternion `q`, draw the unit circle passing through 1, `q`, and -1 (seen as a line) <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>. Then draw the circle perpendicular to it on the unit sphere. Rotate the first circle so 1 moves to `q`, and rotate the perpendicular circle by the same amount using the right-hand rule <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>.

### Non-Commutativity

A crucial property of quaternion multiplication is that it is [[mathematical_properties_and_noncommutative_nature_of_quaternions | non-commutative]]; the order of multiplication matters <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>. For example:
*   `i * j = k` (i acts on j, rotating it to k) <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>.
*   `j * i = -k` (j acts on i, rotating it to -k) <a class="yt-timestamp" data-t="00:28:55">[00:28:55]</a>.
This is similar to how the order of rotations matters when solving a Rubik's cube <a class="yt-timestamp" data-t="00:29:12">[00:29:12]</a>.

### Right Multiplication

Quaternions can also act by multiplying from the right <a class="yt-timestamp" data-t="00:29:44">[00:29:44]</a>. The rule for multiplication is similar, but instead of applying the right-hand rule to the perpendicular circle, a **left-hand rule** is used <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>. For example, `i * j = k` can be seen with the right hand curling `j` to `k` as the thumb points from 1 to `i`, or with the left hand curling `i` to `k` as its thumb points from 1 to `j` <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.

This visual understanding of quaternion multiplication lays the groundwork for how unit quaternions describe [[visualization_of_3d_vector_transformations | 3D rotations]] through a process called conjugation <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>.