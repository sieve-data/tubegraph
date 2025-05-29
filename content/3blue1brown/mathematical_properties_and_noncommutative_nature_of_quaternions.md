---
title: Mathematical properties and noncommutative nature of quaternions
videoId: d4EgbgTm0Bg
---

From: [[3blue1brown]] <br/> 

Quaternions are a unique and often undervalued number system in mathematics <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Just as [[complex_numbers_in_mathematics | complex numbers]] extend real numbers into two dimensions, quaternions extend [[complex_numbers_in_mathematics | complex numbers]] into four dimensions <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Definition and Structure

A quaternion can be understood as a four-dimensional extension of [[complex_numbers_in_mathematics | complex numbers]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. They include real numbers along with three distinct imaginary dimensions, represented by the units `i`, `j`, and `k` <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. These three imaginary dimensions are mutually perpendicular and also perpendicular to the real number line <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. Thus, each quaternion is expressed using four real numbers, residing in four-dimensional space <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. This structure is often viewed as having a real or scalar part and a 3D imaginary part <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. William Rowan Hamilton coined the term "vector" for quaternions that possessed no real part, only `i`, `j`, and `k` components <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.

The magnitude of a quaternion, representing its distance from zero, is calculated as the square root of the sum of the squares of its components <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>.

## Quaternion Multiplication

[[quaternion_multiplication_and_fourdimensional_geometry | Quaternion multiplication]] can be defined algebraically by establishing the rules for how `i`, `j`, and `k` multiply together, allowing for the distributive property <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. This approach is similar to how [[complex_numbers_in_mathematics | complex multiplication]] is defined, where `i` times `i` equals negative one <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. This algebraic definition is particularly useful for computational purposes, offering a relatively compact operation compared to, for example, matrix multiplication, making quaternions valuable in graphics programming and other fields <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. [[quaternion_multiplication_and_fourdimensional_geometry | Quaternion multiplication]] can also be elegantly expressed using the dot product and cross product, essentially encompassing both notions in three dimensions <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.

### Geometric Interpretation

From a geometric perspective, multiplying one quaternion (q1) by another (q2) results in scaling q2 by the magnitude of q1, followed by a specific type of rotation in four dimensions <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. These special 4D rotations are central to understanding quaternions and correspond to the hypersphere of quaternions that are a distance of 1 from the origin <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. The multiplying action of quaternions on this hypersphere results in a pure rotation <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>.

The action of multiplying by a unit quaternion from the left can be visualized as two distinct 2D rotations occurring perpendicularly and in sync with each other within four dimensions <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>. For example, left multiplication by `i`:
*   The circle passing through 1 and `i` (which is projected as a line) rotates 90 degrees, moving 1 to `i`, `i` to -1 (off to infinity), -1 back to -`i`, and -`i` to 1 <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.
*   Concurrently, the circle perpendicular to the 1-`i` circle (e.g., the `j-k` circle) rotates 90 degrees according to a right-hand rule, where the thumb points from 1 to `i`, and the fingers curl in the direction of rotation <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>, <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>. This means `j` goes to `k`, `k` goes to -`j`, -`j` goes to -`k`, and -`k` goes to `j` <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.

Similarly, for right multiplication, the rule is very similar, but a left-hand rule is applied to the perpendicular circle <a class="yt-timestamp" data-t="00:29:44">[00:29:44]</a>.

To understand the full transformation, knowing what a quaternion does to the numbers 1, `i`, `j`, and `k` is sufficient, as multiplication distributes nicely <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>. These units form a basis for the 4-dimensional space <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.

## Non-Commutativity

A significant property of [[quaternion_multiplication_and_fourdimensional_geometry | quaternion multiplication]] is that the order of multiplication matters; it is not commutative <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>. For example, `i` times `j` equals `k`, where `i` acts on `j` to rotate it to `k` <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>. However, if `j` acts on `i` (`j` times `i`), it rotates `i` to negative `k` <a class="yt-timestamp" data-t="00:28:55">[00:28:55]</a>. This lack of commutativity is a more common property in groups of actions on spaces than many realize, similar to how the order of rotations on a Rubik's Cube or a physical object affects the final state <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.

Historically, this "confusing notion of [[quaternion_multiplication_and_fourdimensional_geometry | quaternion multiplication]]" contributed to initial resistance against their adoption, with some mathematicians even legitimately calling them "evil" <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Visualization

To visualize quaternions and their actions in four dimensions, [[stereographic_projection_and_visualizing_quaternions | stereographic projection]] is employed <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This technique maps a 4D hypersphere into 3D space, similar to how a circle can be mapped onto a line or a sphere onto a plane <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>, <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. This projection helps in understanding the complex [[quaternion_multiplication_and_fourdimensional_geometry | quaternion multiplication]] <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

While a single quaternion product doesn't directly correspond to a 3D rotation, a process called "conjugation" involving quaternions is used to describe [[applications_of_quaternions_in_3d_rotations_and_quantum_mechanics | 3D rotations]] <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>, <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>.