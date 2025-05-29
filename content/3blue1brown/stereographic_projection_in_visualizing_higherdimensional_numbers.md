---
title: Stereographic projection in visualizing higherdimensional numbers
videoId: d4EgbgTm0Bg
---

From: [[3blue1brown]] <br/> 

Stereographic projection is a specialized method used to map objects from higher dimensions onto lower-dimensional spaces, allowing for the [[visualizing_mathematical_concepts | visualization of mathematical concepts]] that would otherwise be difficult or impossible to perceive directly <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. This technique helps in understanding transformations and rotations in spaces beyond our ordinary experience, such as those related to complex numbers and quaternions <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.

## Complex Numbers: Projecting a Circle onto a Line

To understand [[geometric_representation_of_complex_numbers | the geometry of complex numbers]] and their multiplication, one can imagine explaining them to a hypothetical "Linus the Linelander," a being whose mind can only grasp one-dimensional geometry and the algebra of real numbers <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.

While complex numbers can be defined algebraically (e.g., *a + bi* where *i*² = -1), their spatial intuition is crucial <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>. From a two-dimensional perspective, multiplying two complex numbers, *z* times *w*, can be seen as *z* acting as a function that rotates and stretches *w* <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>. The difficult concept for Linus to grasp is rotation, as it is intrinsically two-dimensional <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>.

However, rotation involves only one degree of freedom (an angle), meaning it should be possible to associate the set of all rotations to a one-dimensional continuum <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>. This is where stereographic projection comes in <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>.

### The Projection
A circle (representing the unit complex numbers) can be mapped onto a line <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>:
1.  For every point on the unit circle, draw a line from the point at -1 (the "south pole") through that point <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>.
2.  The intersection of this line with a vertical line through the circle's center is where the point gets projected <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>.
3.  The point at 1 projects to the center of the line <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.
4.  Points *i* and -*i* remain fixed in place on the projection line <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.
5.  Points on the arc between 1 and *i* project to an interval between where 1 and *i* landed <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.
6.  Points approaching -1 project farther and farther away on the line, with -1 itself mapping to a "point at infinity" <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

Linus only sees the projection of the unit circle, which represents complex numbers whose multiplication results in pure rotation <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>. When a two-dimensional rotation (e.g., by 90 degrees counterclockwise via multiplication by *i*) is applied to the circle, Linus observes a "strange morphing action" on his line <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. For example:
*   1 moves to *i* <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.
*   *i* moves to -1 (slides off to infinity) <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>.
*   -1 moves to -*i* (comes back from infinity) <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>.
*   -*i* moves to 1 <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>.
Despite its appearance, this motion communicates the idea that multiplying by *i* four times returns to the start (*i*⁴ = 1) <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>.

## 3D Numbers: Projecting a Sphere onto a Plane

The analogy extends to explaining 3D rotations to "Felix the Flatlander," who understands only two-dimensional geometry <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. Imagine extending complex numbers (with real and *i* axes) with a third imaginary axis, *j*, perpendicular to the complex plane <a class="yt-timestamp" data-t="11:21:00">[11:21:00]</a>. For better analogy with quaternions, the *i* and *j* axes are aligned with the x and y directions, and the real number line along the z-direction <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.

It is not possible to define a useful multiplication for a 3D number system that satisfies standard algebraic properties <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>. However, 3D rotations can still be described in this coordinate system <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>. The unit sphere (all numbers a distance 1 from the origin) is projected onto a 2D horizontal plane (the *i*-*j* plane) using stereographic projection <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.

### The Projection
1.  Lines are drawn from -1 (south pole on the real axis) through each point on the sphere to intersect the *i*-*j* plane <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.
2.  The point 1 (north pole) projects to the center of the plane <a class="yt-timestamp" data-t="13:12:00">[13:12:00]</a>.
3.  The northern hemisphere points map inside the *i*-*j* unit circle <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>.
4.  The unit circle passing through *i*, *j*, -*i*, -*j* stays fixed in place on the projection, forming an "honest part" of the sphere unaltered by projection <a class="yt-timestamp" data-t="13:19:00">[13:19:00]</a>.
5.  Southern hemisphere points project outside this unit circle, with -1 mapping to a "point at infinity" <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.

When Felix observes a sphere rotating, he sees lines of latitude and longitude project into various circles and lines on his plane <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>. A rotation about the *j*-axis (e.g., 1 to *i*, *i* to -1, etc.) results in the *i*-*j* unit circle transforming into a vertical line, and the vertical line transforming into the unit circle <a class="yt-timestamp" data-t="15:58:00">[15:58:00]</a>. Similarly, rotation about the *i*-axis transforms the unit circle into a horizontal line <a class="yt-timestamp" data-t="16:42:00">[16:42:00]</a>. A rotation about the real axis appears as a simple rotation of Felix's entire projection around the origin <a class="yt-timestamp" data-t="17:09:00">[17:09:00]</a>. All observed stretching and morphing are artifacts of the projection, as the motion in 3D is rigid <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a>.

## Quaternions: Projecting a 4D Hypersphere into 3D Space

Quaternions are a four-dimensional extension of complex numbers, comprising a real number and three separate imaginary dimensions, represented by the units *i*, *j*, and *k* <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. Each of these imaginary dimensions is perpendicular to the real number line and to each other <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. They have practical utility for describing rotation in three dimensions and are relevant to quantum mechanics <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>, <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

Historically, William Rowan Hamilton sought a 3D number system but realized he needed two more imaginary dimensions (three imaginary and one real) to define a useful multiplication <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. Quaternion multiplication is non-commutative (order matters), a property that differentiates it from real or complex number multiplication <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.

### The 4D to 3D Projection
Just as the magnitude of a complex number is its distance from zero, the same operation gives the magnitude of a quaternion <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. Multiplying one quaternion (*q*₁) by another (*q*₂) scales *q*₂ by the magnitude of *q*₁ followed by a "very special type of rotation in four dimensions" <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.

These 4D rotations correspond to the [[highdimensional_spheres | hypersphere]] of quaternions a distance of 1 from the origin <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. To visualize this, a 4D hypersphere is stereographically projected into 3D space <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
1.  The projection is made from the number -1, which lies on the real number line perpendicular to the 3D space of observation <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
2.  The number 1 projects into the center of the 3D space <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.
3.  A unit sphere passing through *i*, *j*, and *k* (representing unit quaternions with a real part of zero, or "unit vectors" as Hamilton called them) remains fixed in place under this projection <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. This acts like the "equator" of the 4D hypersphere <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.
4.  Unit quaternions with positive real parts project inside this 3D unit sphere <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
5.  Unit quaternions with negative real parts project outside this 3D unit sphere <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.
6.  The number -1 projects to the "point at infinity" <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

### Understanding Quaternion Multiplication (4D Rotation)
The action of left-multiplying a unit quaternion by any other quaternion can be conceptualized as two separate 2D rotations <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>:
1.  **Primary Rotation**: A unit circle (e.g., the circle passing through 1 and *i*) is rotated so that 1 moves to the position of the multiplying quaternion <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. This appears as a morphing motion on the projected line, analogous to Linus's experience <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
2.  **Perpendicular Rotation**: A circle perpendicular to the first (e.g., the circle passing through *j* and *k*) also rotates by the same amount <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. This rotation follows a "right-hand rule": if the thumb points from 1 to the multiplying quaternion, the fingers curl in the direction of the perpendicular circle's rotation <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

This "double rotation" is the heart of what quaternions do in 4D space <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. For example, left-multiplying by *i*:
*   The 1-*i* circle rotates 90 degrees <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   The *j*-*k* circle (perpendicular to 1-*i*) rotates 90 degrees according to the right-hand rule, meaning *j* goes to *k*, *k* to -*j*, etc. <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.

### Non-Commutativity and Left/Right Multiplication
The order of quaternion multiplication matters: *i* times *j* equals *k*, but *j* times *i* equals -*k* <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. This non-commutative property is common in groups of actions on space, such as [[highdimensional_geometry_and_cube_coloring | rotations of a Rubik's cube]] <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

While left multiplication uses the right-hand rule, right multiplication of quaternions involves a similar process but uses a left-hand rule for the perpendicular circle's rotation <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.

Despite the complexities of these 4D actions, this [[higher_dimensions_and_their_relevance | visualization]] helps explain how quaternions precisely describe [[visualizing_transformations_in_three_dimensions | 3D rotations]] through a process called conjugation, which will involve both left and right multiplication <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. The visual understanding of these 4D transformations provides a pleasing intuition for otherwise opaque formulas <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.