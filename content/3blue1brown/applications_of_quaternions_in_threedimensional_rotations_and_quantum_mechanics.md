---
title: Applications of quaternions in threedimensional rotations and quantum mechanics
videoId: d4EgbgTm0Bg
---

From: [[3blue1brown]] <br/> 

Quaternions are a fascinating and often underappreciated number system in mathematics <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Just as [[complex_numbers_as_a_foundation_for_understanding_quaternions | complex numbers]] are a two-dimensional extension of real numbers, quaternions are a four-dimensional extension of [[complex_numbers_as_a_foundation_for_understanding_quaternions | complex numbers]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Beyond their abstract mathematical nature, quaternions possess a pragmatic utility for describing [[threedimensional_linear_transformations | rotation in three dimensions]] and are even relevant to [[quantum_mechanics_basics_for_beginners | quantum mechanics]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Historical Context and Initial Resistance

The [[history_and_discovery_of_quaternions_by_william_rowan_hamilton | discovery of quaternions]] is a famous story in mathematics <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The Irish mathematician William Rowan Hamilton spent years attempting to find a three-dimensional number system analogous to [[complex_numbers_as_a_foundation_for_understanding_quaternions | complex numbers]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. On October 16, 1843, while crossing the Broom Bridge in Dublin, Hamilton had a flash of insight: he needed to add not one, but two more imaginary dimensions to the [[complex_numbers_as_a_foundation_for_understanding_quaternions | complex numbers]], resulting in three imaginary dimensions and a real number, all perpendicular to each other in a kind of fourth dimension <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. He carved the crucial equation describing these three imaginary units into the bridge, where a plaque now stands in his honor <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

In Hamilton's era, the modern notion of vectors with dot and cross products was not standardized <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. After his discovery, Hamilton strongly advocated for quaternions to be the primary language for describing [[threedimensional_linear_transformations | three-dimensional space]], even establishing an official quaternion society <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. However, other mathematicians opposed this, finding the [[quaternion_multiplication_and_fourdimensional_geometry | confusing notion of quaternion multiplication]] unnecessary for describing three dimensions <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This led to "old-timey trash talk," with some legitimately calling them "evil" <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. It is even believed that the Mad Hatter scene in Lewis Carroll's "Alice in Wonderland" (Carroll was an Oxford mathematician) mocked quaternion multiplication through its chaotic table placement and references to their non-commutative nature <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Describing [[threedimensional_linear_transformations | Three-Dimensional Rotations]]

Despite initial resistance, the computing industry spurred a resurgence of quaternions among programmers working with graphics, robotics, and anything involving orientation in [[threedimensional_linear_transformations | 3D space]] <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Efficiency and Error Avoidance

Quaternions provide an elegant way to describe and compute [[threedimensional_linear_transformations | 3D rotations]] <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. They are computationally more efficient than other methods and help avoid numerical errors that can arise in alternative approaches <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Geometric Intuition

A quaternion's magnitude (its distance from zero) is found by taking the square root of the sum of the squares of its four components <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>. When one quaternion `q1` is multiplied by another `q2`, the effect is to scale `q2` by the magnitude of `q1`, followed by a specific type of rotation in four dimensions <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. These special 4D rotations correspond to the hypersphere of quaternions, which are a distance of 1 from the origin <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. Unit quaternions (those with a magnitude of 1) are precisely those whose multiplication action is a pure rotation <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.

### Quaternion Multiplication

[[quaternion_multiplication_and_fourdimensional_geometry | Quaternion multiplication]] is not commutative, meaning the order of multiplication matters (e.g., `i` times `j` is `k`, but `j` times `i` is `-k`) <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>. This non-commutative property is common in groups of actions on space, such as rotations of a Rubik's Cube <a class="yt-timestamp" data-t="00:29:09">[00:29:09]</a>.

While a single quaternion product doesn't directly correspond to a [[threedimensional_linear_transformations | 3D rotation]] in an obvious way (as it would morph the ijk unit sphere out of place), the description of [[threedimensional_linear_transformations | 3D rotation]] using quaternions involves a process called "conjugation" <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a>.

## Relevance in [[quantum_mechanics_basics_for_beginners | Quantum Mechanics]]

The 20th century saw quaternions gain appreciation from a new field: [[quantum_mechanics_basics_for_begginers | quantum mechanics]] <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. The specific actions quaternions describe in four dimensions are highly relevant to how two-state systems, such as the spin of an electron or the [[polarization_and_superposition_in_quantum_mechanics | polarization of a photon]], are mathematically described <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Visualizing Quaternions (Supporting Understanding)

To build intuition for [[quaternion_multiplication_and_fourdimensional_geometry | quaternion multiplication]], a visualization approach uses stereographic projection <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This method maps a higher-dimensional sphere onto a lower-dimensional space <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### Stereographic Projection

*   **Circle to Line (for Linus the Linelander)**: Analogous to explaining [[complex_numbers_as_a_foundation_for_understanding_quaternions | complex numbers]] to a creature understanding only one dimension, a circle can be projected onto a line <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Sphere to Plane (for Felix the Flatlander)**: Similar to explaining [[threedimensional_linear_transformations | 3D rotations]] to a two-dimensional creature, a sphere can be projected onto a plane <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **4D Hypersphere to 3D Space (for us)**: Quaternions, which live in four-dimensional space, can be visualized by stereographically projecting their unit hypersphere into our familiar 3D space <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.
    *   The number 1 projects to the center of our space <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
    *   A whole sphere (passing through i, j, and k) on the unit hypersphere remains fixed in place under this projection, representing all unit quaternions with a real part of zero (Hamilton's "unit vectors") <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>. This sphere appears as a unit sphere in our 3D space <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.
    *   The number negative 1 projects to "the point at infinity" <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
    *   Any plane seen in the projection represents a sphere on the hypersphere that passes through the number negative 1 <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.

### Quaternion Multiplication Visualization

The action of multiplying a unit quaternion by any other quaternion from the left can be conceptualized as two distinct 2D rotations happening perpendicularly and in sync in four dimensions <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

For example, when multiplying by `i`:
*   The circle passing through 1 and `i` (seen as a line in projection) rotates 90 degrees <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.
*   The circle perpendicular to it, passing through `j` and `k`, rotates 90 degrees according to a right-hand rule (thumb pointing from 1 to `i`, fingers curling in the direction of rotation) <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.

Similarly, for multiplication by `j`:
*   The circle through 1 and `j` rotates 90 degrees <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.
*   The perpendicular circle (through `i` and `k`) rotates 90 degrees according to the right-hand rule (thumb pointing from 1 to `j`) <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>.

This dual rotation describes the rigid motion of the hypersphere <a class="yt-timestamp" data-t="00:25:45">[00:25:45]</a>. While this discussion primarily focuses on left multiplication, right multiplication exists and follows a similar logic but uses a left-hand rule <a class="yt-timestamp" data-t="00:29:44">[00:29:44]</a>. Understanding both left and right multiplication is crucial for comprehending how unit quaternions describe [[threedimensional_linear_transformations | rotation in three dimensions]] through a process called conjugation <a class="yt-timestamp" data-t="00:30:24">[00:30:24]</a>.