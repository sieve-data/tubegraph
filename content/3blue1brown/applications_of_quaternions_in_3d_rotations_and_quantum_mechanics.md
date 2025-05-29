---
title: Applications of quaternions in 3D rotations and quantum mechanics
videoId: d4EgbgTm0Bg
---

From: [[3blue1brown]] <br/> 

Quaternions are a fascinating number system that extends complex numbers into four dimensions <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Beyond their mathematical properties, they possess significant practical utility, particularly for describing rotation in three dimensions and in quantum mechanics <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Historical Context and Initial Resistance
The [[historical_discovery_and_significance_of_quaternions | story of their discovery]] is famous in mathematics <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Irish mathematician William Rowan Hamilton sought a three-dimensional number system analogous to complex numbers for much of his life <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. On October 16, 1843, he realized that instead of adding one dimension to complex numbers, he needed to add two more imaginary dimensions, totaling three imaginary dimensions plus a real number sitting perpendicularly in a fourth dimension <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. He carved the crucial equation describing these three imaginary units into Broom Bridge in Dublin <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

In Hamilton's era, the modern notion of vectors with dot and cross products was not standardized <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. After his discovery, Hamilton advocated for quaternions as the primary language for describing three-dimensional space, even forming an official society <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. However, this was met with resistance from mathematicians who found the notion of [[quaternion_multiplication_and_fourdimensional_geometry | quaternion multiplication]] confusing and unnecessary for describing three dimensions <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. It's even believed that the Mad Hatter scene in "Alice in Wonderland" (authored by an Oxford mathematician) mocked quaternion multiplication and its [[mathematical_properties_and_noncommutative_nature_of_quaternions | non-commutative nature]] <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Applications in 3D Rotations
Approximately a century after their discovery, the computing industry led to a resurgence of quaternions, particularly among programmers working with graphics, robotics, and anything involving orientation in 3D space <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
The reasons for this utility include:
*   **Elegant Description and Computation**: Quaternions offer an elegant method to describe and compute 3D rotations <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   **Computational Efficiency**: Their operations are computationally more efficient than other methods <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Avoidance of Numerical Errors**: They help avoid many numerical errors that can arise in other rotational methods <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

While this video primarily lays the groundwork for understanding, the specific mechanism by which quaternions describe 3D rotations involves a process called conjugation, which is explored in a subsequent video <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>.

## Applications in Quantum Mechanics
The 20th century also saw quaternions gaining favor in quantum mechanics <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. The special actions that quaternions describe in four dimensions are relevant to the mathematical description of two-state systems, such as the spin of an electron or the [[polarization_and_superposition_in_quantum_mechanics | polarization]] of a photon <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Visualizing Quaternions and Their Actions
Understanding [[quaternion_multiplication_and_fourdimensional_geometry | quaternion multiplication]] and its geometric implications in four dimensions is key to grasping its applications <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. A useful method to [[stereographic_projection_and_visualizing_quaternions | visualize quaternions]] in their full four-dimensional glory involves stereographic projection <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

By analogy, this process is similar to explaining complex numbers (two-dimensional) to a one-dimensional being (Linus the Linelander) or explaining 3D rotations to a two-dimensional being (Felix the Flatlander) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This projection maps a 4D hypersphere into 3D space <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.

Multiplying one quaternion by another, for example, `q1` by `q2`, involves scaling `q2` by the magnitude of `q1` followed by a unique type of rotation in four dimensions <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. These 4D rotations correspond to the hypersphere of quaternions at a distance of 1 from the origin <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

A key aspect of [[quaternion_multiplication_and_fourdimensional_geometry | quaternion multiplication]] is its non-commutative nature <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>. For instance, `i` times `j` equals `k`, but `j` times `i` equals negative `k` <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>. This means the order of multiplication matters, similar to how the order of rotations on a Rubik's cube affects the final state <a class="yt-timestamp" data-t="00:29:12">[00:29:12]</a>.

When a unit quaternion acts by left multiplication, it involves two separate 2D rotations occurring perpendicularly and in sync in four dimensions <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>. For example, multiplying by `i` rotates the 1-`i` circle (seen as a line) by 90 degrees, and simultaneously rotates the perpendicular `j`-`k` circle by the same amount following a right-hand rule <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. Similarly, right multiplication follows a left-hand rule for the perpendicular circle <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>. Understanding this left-hand rule for right multiplication is crucial for understanding how unit quaternions describe 3D rotation <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>.