---
title: Visualizing Pythagorean triples using complex numbers
videoId: QJYmyhnaaek
---

From: [[3blue1brown]] <br/> 

The [[Pythagorean theorem and triples | Pythagorean theorem]], stating that the sum of the squares of the two shorter sides of a right triangle equals the square of its hypotenuse ($a^2 + b^2 = c^2$), often brings to mind familiar examples like the 3-4-5 or 5-12-13 triangles <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It's easy to overlook the significance of these "Pythagorean triples" – sets of three whole numbers (a, b, c) where this relationship holds <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. In contrast, if the exponent were any whole number greater than 2, there would be no integer solutions at all, as stated by Fermat's Last Theorem <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

This article explores a method to find and [[visualizing_mathematical_concepts | visualize]] every possible [[Pythagorean theorem and triples | Pythagorean triple]] using complex numbers <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. The problem of finding these triples is ancient, with Babylonian clay tablets from 1800 BC listing them, predating Pythagoras by over a millennium <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Reframing the Problem

Finding [[Pythagorean theorem and triples | Pythagorean triples]] (a, b, c) is equivalent to identifying [[complex_numbers_and_2d_plane_transformations | lattice points]] (points with integer coordinates) on a plane that are a whole number distance away from the origin <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. For example, the point (3,4) is 5 units from the origin, and (12,5) is 13 units away <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. While most lattice points (like 2,1) result in a distance that is the square root of a whole number (e.g., √5 for (2,1)), the goal is to find those where the distance is a whole number itself <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## The Power of Complex Numbers

A powerful approach involves thinking of the plane as the [[geometric_representation_of_complex_numbers | complex plane]], where each lattice point (x,y) corresponds to a complex number x + yi <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Squaring Complex Numbers
By simply squaring a complex number with integer coordinates, we can guarantee that the resulting number's distance from the origin will be a whole number <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

*   **Algebraic Perspective**: When squaring a complex number like `(a + bi)^2`, the result's real and imaginary parts (`a^2 - b^2` and `2ab`) are guaranteed to be integers if `a` and `b` are integers <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. For example, `(2 + i)^2` expands to `3 + 4i` <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Geometric Perspective**: Complex number multiplication involves multiplying their lengths from the origin and adding their angles with the horizontal axis <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. When a complex number is multiplied by itself (squared), its angle from the horizontal axis is doubled, and its length is squared <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. If the original length is the square root of a whole number (as is the case for any lattice point), then squaring that length results in a whole number <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. For `2 + i`, its initial length is √5. Squaring it results in a complex number `3 + 4i` with a length of 5 <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

This method reliably generates [[Pythagorean theorem and triples | Pythagorean triples]]:
*   Starting with `3 + 2i` (distance √13), squaring it yields `5 + 12i` (distance 13), corresponding to the 5-12-13 triple <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   Starting with `4 + i` (distance √17), squaring it yields `15 + 8i` (distance 17), corresponding to the 8-15-17 triple <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

The general formula for generating a triple from any integers `u` and `v` is:
If `z = u + vi`, then `z^2 = (u^2 - v^2) + (2uv)i` <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. The resulting [[Pythagorean theorem and triples | Pythagorean triple]] is `(u^2 - v^2, 2uv, u^2 + v^2)` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Visualizing the Transformation
[[complex_numbers_and_2d_plane_transformations | Visualizing the transformation]] `z → z^2` for every point on the complex plane shows that grid lines are transformed into parabolic arcs <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>, <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. Every intersection point of these transformed arcs corresponds to a lattice point whose distance from the origin is a whole number, thus representing a [[Pythagorean theorem and triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. This visualization beautifully organizes triples that might otherwise appear random <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Accounting for All Pythagorean Triples

While squaring complex numbers generates many triples, it doesn't directly hit *every* possible one <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. For instance, `6 + 8i` (from the 6-8-10 triple) is missed <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. However, missed triples like 6-8-10 are simply multiples of those generated by the method (e.g., 6-8-10 is a multiple of 3-4-5) <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

To account for all triples, one can take each point generated by squaring complex numbers and draw a radial line from the origin through that point out to infinity <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. All lattice points hit by these lines represent multiples of the generated triples, thus encompassing every possible [[Pythagorean theorem and triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

### Proof of Completeness via Rational Points on the Unit Circle
The problem of finding [[Pythagorean theorem and triples | Pythagorean triples]] can be rephrased as finding rational points on the unit circle ($x^2 + y^2 = 1$) <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. Dividing $a^2 + b^2 = c^2$ by $c^2$ yields $(a/c)^2 + (b/c)^2 = 1$, where $a/c$ and $b/c$ are rational coordinates on the unit circle <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. Conversely, any rational point on the unit circle can be scaled to yield integer coordinates with an integer distance from the origin, thus forming a [[Pythagorean theorem and triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

When the points generated by squaring complex numbers are projected onto the unit circle along their radial lines, they produce many rational points on the circle <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. To prove this method is complete, we must show it hits every rational point on the unit circle <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

Consider any rational point on the unit circle and draw a line between it and the point (-1,0) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The slope of this line will always be a rational number <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

Our method starts with an initial complex number `u + vi` with integer coordinates, making an angle `theta` with the horizontal axis <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. Squaring this number results in a complex number whose angle is `2*theta` <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. When projected onto the unit circle, this point also has an angle of `2*theta` <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

A key piece of circle geometry states that the angle from the center of a circle to two points on its circumference is twice the angle made by those same two points and any other point on the circumference <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. Applied here, the line between (-1,0) and the rational point on the circle (at angle `2*theta`) must make an angle `theta` with the horizontal <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

Crucially, the slope of the line between the origin and our initial complex number `u + vi` is `v/u` <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. Since `u` and `v` can be any integers, the ratio `v/u` can represent *every possible rational slope* <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. Therefore, the radial lines generated by our method, based on all possible choices of `u` and `v`, must pass through every rational point on the unit circle <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. This confirms that the method effectively accounts for every possible [[Pythagorean theorem and triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.