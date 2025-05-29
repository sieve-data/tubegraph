---
title: Quaternion multiplication and fourdimensional geometry
videoId: d4EgbgTm0Bg
---

From: [[3blue1brown]] <br/> 

Quaternion multiplication can be understood as a specific representation of motion on a four-dimensional sphere, visualized within three-dimensional space <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Introduction to Quaternions

Quaternions are a fascinating and often underappreciated number system <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Just as complex numbers are a two-dimensional extension of real numbers, quaternions are a [[exploring_fourdimensional_geometry_and_its_implications | four-dimensional]] extension of complex numbers <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Beyond being a mathematical curiosity, they possess pragmatic utility for describing rotation in three dimensions and even for quantum mechanics <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Discovery and Early Reception

The discovery of quaternions by Irish mathematician William Rowan Hamilton is a famous story in mathematics <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Hamilton spent much of his life seeking a three-dimensional number system analogous to complex numbers <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. On October 16, 1843, while crossing Broom Bridge in Dublin, he had an insight: he needed to add two more imaginary dimensions (three imaginary dimensions in total) to the complex numbers, with the real numbers sitting perpendicularly in a kind of fourth dimension <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. He carved the crucial equation describing these three imaginary units into the bridge, which is commemorated with a plaque today <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

During Hamilton's time, the modern notion of vectors with dot and cross products was not standardized <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. After his discovery, Hamilton advocated for quaternions to be the primary language for describing three-dimensional space, even forming an official quaternion society <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. However, other mathematicians found the concept of quaternion multiplication confusing and unnecessary for describing three dimensions, leading to humorous historical debates where quaternions were "legitimately calling them evil" <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. It's even believed that the Mad Hatter scene in Lewis Carroll's *Alice in Wonderland* (Carroll being an Oxford mathematician) mocked quaternion multiplication through chaotic table placement and references to their non-commutative nature <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Modern Utility

About a century later, the computing industry spurred a resurgence of quaternions among programmers working with graphics, robotics, and anything involving orientation in 3D space <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This is because they offer an elegant, computationally efficient, and numerically stable way to describe and compute 3D rotations compared to other methods <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

The 20th century also saw quaternions gaining favor in quantum mechanics <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. The special actions quaternions describe in four dimensions are relevant to the mathematical description of two-state systems, such as electron spin or photon polarization <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Visualizing Quaternions and Higher Dimensions

Understanding quaternion multiplication geometrically requires visualizing their full [[exploring_fourdimensional_geometry_and_its_implications | four-dimensional]] nature <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This visualization can lead to a natural intuition for how to think about quaternion multiplication <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

The approach to visualizing quaternions involves a progression from simpler dimensions:
1.  Describing complex numbers to someone who only understands one dimension <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
2.  Describing 3D rotations to someone who only understands two dimensions <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
3.  Ultimately, representing what quaternions do in four dimensions within the constraints of our 3D space <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Linus the Linelander: From 1D to Complex Numbers

Imagine Linus, whose mind grasps only one-dimensional geometry (lines) and the algebra of real numbers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. To describe complex numbers to Linus:
*   **Algebraic Definition**: Complex numbers are expressed as a real number plus another real number times `i`, where `i * i = -1` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. Multiplication uses the distributive property (FOIL) and this rule for `i` <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Geometric Interpretation**: For those who understand two dimensions, multiplying two complex numbers `z * w` can be seen as `z` acting as a function on `w`, rotating and stretching it <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. This action transforms the entire complex plane, fixing zero and dragging one to `z` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Stereographic Projection for Rotation**: While Linus understands stretching (multiplication by real numbers), rotation is difficult to communicate <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Since rotation involves one degree of freedom (the angle), it's possible to associate all rotations to a one-dimensional continuum <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. Stereographic projection maps a circle onto a line <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>:
    *   For every point on the unit circle, a line from -1 through that point intersects a vertical line (Linus's world) to project the point <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
    *   The point 1 projects to the center of the line <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
    *   `i` and `-i` stay fixed <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
    *   The point -1 projects to "the point at infinity" <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Visualizing Complex Multiplication on the Line**: When `i` multiplies a complex number `w`, it rotates it by 90 degrees counterclockwise <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. On Linus's projected line, this results in a "strange morphing action" <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>:
    *   `1` moves to `i` <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
    *   `i` slides off to infinity (`i * i = -1`) <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
    *   The point at infinity (`-1`) comes back to `-i` (`i * -1 = -i`) <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   `-i` slides up to `1` (`i * -i = 1`) <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### Felix the Flatlander: From 2D to 3D Rotations

Next, consider Felix, who understands two-dimensional geometry <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. To explain rotations of a sphere to Felix, we extend the complex numbers with a third axis, `j`, perpendicular to the complex plane <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. In this setup, the `i` and `j` axes align with the x and y directions, and the real number line aligns with the z-direction <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. While it's not possible to define a useful notion of multiplication for a 3D number system <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>, we can still describe 3D rotations in this coordinate system.

*   **The Unit Sphere**: The unit sphere comprises all numbers a distance of 1 from the origin, where the sum of the squares of their coordinates is 1 <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   **Stereographic Projection for 3D Rotations**: Analogous to the previous step, stereographic projection associates almost every point on the unit sphere with a unique point on the horizontal plane defined by the `i` and `j` axes <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
    *   A line from -1 (south pole) through a point on the sphere intersects the plane to project the point <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
    *   The point 1 (north pole) projects to the center of the plane <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
    *   Points on the northern hemisphere map inside the unit circle of the `i-j` plane <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
    *   The unit circle passing through `i, j, -i, -j` remains fixed in place under projection <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.
    *   Points on the southern hemisphere project outside the unit circle, with -1 projecting to "a point at infinity" <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   **Visualizing 3D Rotations on the Plane**: As the sphere rotates, lines of latitude and longitude project into circles and lines in Felix's space <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
    *   A 90-degree rotation about the `j`-axis moves `1` to `i`, `i` to `-1`, etc. <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. Felix sees an extension of Linus's rotation <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.
    *   This action rotates Felix's unit circle (initially the `i,j` unit circle) into a vertical line, and the red vertical line (1,j unit circle) into the unit circle <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
    *   A rotation about the real axis appears as a simple rotation of the entire projection about the origin for Felix <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.

## Quaternion Structure and Multiplication

Quaternions extend real numbers with three separate imaginary dimensions, represented by the units `i`, `j`, and `k` <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. These three imaginary dimensions are perpendicular to the real number line and to each other <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. Each quaternion is written using four real numbers and exists in [[exploring_fourdimensional_geometry and its implications | four-dimensional]] space <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. They can be thought of as having a real (scalar) part and a 3D imaginary part <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. Hamilton coined the term "vector" for quaternions with no real part and only `i, j, k` components <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.

*   **Algebraic Definition**: Quaternion multiplication can be defined by rules for how `i`, `j`, and `k` multiply together, with everything distributing nicely <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. This is how computers perform quaternion multiplication, valued for its compactness compared to [[matrix_multiplication_and_transformations | matrix multiplication]] <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. An elegant form of this rule uses the dot product and cross product, with quaternion multiplication subsuming both notions in three dimensions <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.
*   **Geometric Interpretation in 4D**: Just as complex multiplication involves scaling and rotation, a deeper understanding of quaternion multiplication comes from its [[exploring_fourdimensional_geometry and its implications | four-dimensional geometry]] <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.
    *   The magnitude of a quaternion is the square root of the sum of the squares of its components <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>.
    *   Multiplying one quaternion `q1` by `q2` scales `q2` by the magnitude of `q1`, followed by a special type of rotation in four dimensions <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.
    *   These special 4D rotations correspond to the hypersphere of quaternions (distance 1 from the origin) <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   **Stereographic Projection of the 4D Hypersphere**: The hypersphere is stereographically projected into 3D space <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.
    *   Projection is from the number -1 on the real number line, which is perpendicular to our 3D space and beyond perception <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
    *   The number 1 projects to the center of our 3D space <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
    *   A whole sphere passing through `i, j, k` on the unit hypersphere stays fixed in place under projection <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>. This "unit sphere" in our 3D space is the unaltered part of the hypersphere, analogous to a 3D sphere's equator, and represents unit quaternions with a zero real part (unit vectors) <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.
    *   Unit quaternions with positive real parts (0-1) project inside this unit sphere <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>.
    *   Unit quaternions with negative real parts project outside the unit sphere <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>.
    *   Negative 1 projects to the "point at infinity" <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
    *   A line through the origin passing through `i` and `-i` represents a circle on the hypersphere <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. Any plane seen in the projection represents a sphere on the hypersphere that passes through -1 <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.
*   **4D Rotations as Double Rotations**: The action of multiplying a unit quaternion by any other quaternion from the left can be thought of as two separate 2D rotations occurring perpendicularly and in sync in four dimensions <a class="yt-timestamp" data-t="00:23:19">[00:23:19]</a>.
    *   **Example: Multiplication by `i`**:
        *   The circle through `1` and `i` (seen as a line) rotates 90 degrees: `1` goes to `i`, `i` to `-1` (infinity), `-1` to `-i`, and `-i` to `1` <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>.
        *   The circle perpendicular to this one, passing through `j` and `k`, also rotates 90 degrees according to a "right-hand rule": Point your thumb from `1` to `i`, and curl your fingers. The `j-k` circle rotates in the direction of the curl <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. So, `j` goes to `k`, `k` to `-j`, `-j` to `-k`, and `-k` to `j` <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.
*   **Non-Commutative Nature**: The order of quaternion multiplication matters; it is not commutative <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>. For example, `i * j = k`, but `j * i = -k` <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>. This property is common in groups of actions on space, similar to how the order of rotations matters on a Rubik's cube <a class="yt-timestamp" data-t="00:29:09">[00:29:09]</a>.
*   **Left vs. Right Multiplication**: Quaternions can act by left multiplication (e.g., `i * j` where `i` acts on `j`) or right multiplication (e.g., `j * i` where `i` acts on `j` from the right) <a class="yt-timestamp" data-t="00:29:31">[00:29:31]</a>. While the result `i * j = k` is the same, the underlying "hand rule" differs: left multiplication uses the right-hand rule, while right multiplication uses the left-hand rule <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>.

### Quaternions and 3D Rotation
The direct action of a single quaternion product does not leave the unit sphere (representing vectors) in place; it morphs it <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a>. The way unit quaternions describe 3D rotation involves a process called "conjugation," which is a more complex operation <a class="yt-timestamp" data-t="00:30:49">[00:30:49]</a>.