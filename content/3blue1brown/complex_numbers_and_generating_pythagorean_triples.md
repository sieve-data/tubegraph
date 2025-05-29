---
title: Complex numbers and generating Pythagorean triples
videoId: QJYmyhnaaek
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_pythagorean_triples | Pythagorean theorem]], stating that the sum of the squares of the two shorter sides on a right triangle always equals the square of its hypotenuse (a² + b² = c²), often brings to mind familiar examples like the 3-4-5 triangle or the 5-12-13 triangle <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It's easy to overlook that these examples, where the sum of two perfect squares results in another perfect square, even exist <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. In contrast, if the exponent were any whole number greater than two, there would be no integer solutions at all, a concept known as Fermat's Last Theorem <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

A triplet of whole numbers (a, b, c) satisfying a² + b² = c² is called a [[introduction_to_pythagorean_triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The pursuit of finding every possible example of these triples is an ancient mathematical problem, with evidence dating back to Babylonian clay tablets from 1800 BC, predating Pythagoras by over a millennium <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Proof of the Pythagorean Theorem

One visual proof of the [[introduction_to_pythagorean_triples | Pythagorean theorem]] involves starting with a square on each side of a right triangle <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
If you take the square on the hypotenuse (c²) and add four copies of the original triangle around it, you form a larger square with side lengths (a + b) <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
Alternatively, you can arrange the squares on the two shorter sides (a² and b²) together with four copies of the original triangle to form another large square also with side lengths (a + b) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
By comparing the "negative space" (the area of the large square minus the four triangles) in both arrangements, it becomes clear that a² + b² equals c² <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Reframing the Problem: Lattice Points

The question of finding [[introduction_to_pythagorean_triples | Pythagorean triples]] can be reframed as finding [[visualization_of_pythagorean_triples_using_lattice_points | lattice points]] (points with integer coordinates) on a plane that are a whole number distance away from the origin <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. For example, the point (3,4) is a distance of 5 from the origin, and (12,5) is a distance of 13 from the origin <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Most [[visualization_of_pythagorean_triples_using_lattice_points | lattice points]], like (2,1), have a distance from the origin that is the square root of a whole number (e.g., √5) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Generating Triples Using Complex Numbers

### Introduction to [[complex_numbers_in_mathematics | Complex Numbers]]
By thinking of the coordinate plane as the [[complex_numbers_in_mathematics | complex plane]], every point like (2,1) can be represented as a [[complex_numbers_in_mathematics | complex number]], such as 2 + i <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This allows for a method to generate points whose distance from the origin is guaranteed to be a whole number <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Squaring [[complex_numbers_in_mathematics | Complex Numbers]]
The key operation is to square a [[complex_numbers_in_mathematics | complex number]] <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
Algebraically, when a [[complex_numbers_in_mathematics | complex number]] (a + bi) is squared, the result (a² - b² + 2abi) will have integer components if the original number had integer components <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. For example, (2 + i)² = 3 + 4i <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

Geometrically, [[complex_numbers_multiplication_and_rotation | complex multiplication]] involves rotating and stretching <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. If a [[complex_numbers_in_mathematics | complex number]] z has a length (magnitude) `L` and an angle `θ` from the horizontal axis <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>:
*   Multiplying by z rotates by `θ` and stretches by `L` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   Therefore, squaring z (multiplying z by itself) doubles its angle (to 2`θ`) and squares its length (to L²) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

Since the initial length (distance from origin) of a [[visualization_of_pythagorean_triples_using_lattice_points | lattice point]] (u,v) is √(u² + v²), squaring the corresponding [[complex_numbers_in_mathematics | complex number]] (u + vi) guarantees that the resulting length will be a whole number (u² + v²) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Examples
*   Starting with 2 + i: The distance from the origin is √5 <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. Squaring it gives (2 + i)² = 3 + 4i. The new point (3,4) is a distance of 5 from the origin, corresponding to the 3-4-5 triple <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   Starting with 3 + 2i: The distance from the origin is √13 <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Squaring it gives (3 + 2i)² = 5 + 12i. The new point (5,12) is a distance of 13 from the origin, corresponding to the 5-12-13 triple <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   Starting with 4 + i: Squaring it gives (4 + i)² = 15 + 8i, which has a distance of 17 from the origin, forming the 8-15-17 triple <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### General Formula
For any initial [[lattice point]] (u,v) represented as the [[complex_numbers_in_mathematics | complex number]] u + vi, squaring it yields <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>:
(u + vi)² = (u² - v²) + (2uv)i <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
The resulting [[Pythagorean triple]] (a,b,c) is then (u² - v², 2uv, u² + v²) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This provides a general formula for generating [[introduction_to_pythagorean_triples | Pythagorean triples]] from any pair of integers (u,v) <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

## Visualizing the Transformation

Visualizing the transformation of the [[complex_numbers_in_mathematics | complex plane]] where every point z moves to z² is insightful <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   A point like 3 + 2i moves to 5 + 12i <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   Grid lines in the initial plane transform into parabolic arcs in the resulting plane <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   Every intersection point of these parabolic arcs is a transformed [[visualization_of_pythagorean_triples_using_lattice_points | lattice point]], thus corresponding to a [[introduction_to_pythagorean_triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. This visualization reveals an organized structure among triples, which often appear random <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Completeness of the Method

While this method generates many [[introduction_to_pythagorean_triples | Pythagorean triples]], it doesn't initially account for *every* possible triple <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. For example, 6 + 8i (corresponding to the 6-8-10 triple) is missed because there are no integers u and v such that (u + vi)² = 6 + 8i <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. Similarly, 9 + 12i is missed <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

However, any [[introduction_to_pythagorean_triples | Pythagorean triple]] missed by this method is simply a multiple of a triple that *is* generated <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. For instance, 6-8-10 is a multiple of 3-4-5, which *is* generated <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. Similarly, while 4 + 3i is missed, 8 + 6i (which is 3 + i squared) is hit, and 4 + 3i is simply one half of 8 + 6i <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

To account for these multiples, one can draw radial lines from the origin through each point generated by the squaring method, extending to infinity <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. Marking all [[visualization_of_pythagorean_triples_using_lattice_points | lattice points]] these lines intersect will account for all possible [[introduction_to_pythagorean_triples | Pythagorean triples]] <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

## Connection to [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | Rational Points on the Unit Circle]]

This method's completeness can be understood by its connection to [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | rational points on the unit circle]] <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
Dividing a² + b² = c² by c² gives (a/c)² + (b/c)² = 1 <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This means every [[introduction_to_pythagorean_triples | Pythagorean triple]] corresponds to a point (x,y) on the [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | unit circle]] (x² + y² = 1) where both x and y are [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | rational numbers]] <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. Conversely, any [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | rational point on the unit circle]] can be scaled up to yield a [[introduction_to_pythagorean_triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

When the points generated by squaring [[complex_numbers_in_mathematics | complex numbers]] (and their multiples along radial lines) are projected onto the [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | unit circle]], they should account for all [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | rational points]] <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

Consider any [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | rational point]] on the [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | unit circle]] <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. Drawing a line between this point and the point (-1,0) on the unit circle will result in a line with a [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | rational slope]] (since both rise and run are rational) <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
The method of squaring [[complex_numbers_in_mathematics | complex numbers]] works as follows <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>:
1.  Start with u + vi, which has an angle `θ` with the horizontal axis <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
2.  Squaring this number yields a point with an angle of 2`θ` <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
3.  Projecting this point onto the [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | unit circle]] gives a [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | rational point]] also at angle 2`θ` <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

A property of circle geometry states that the angle formed by two points on the circumference and the center (2`θ`) is twice the angle made by those same points and any other point on the circumference (e.g., -1), provided that other point is not between the original two <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This means the line connecting the [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | rational point]] on the circle to -1 will have an angle `θ` with the horizontal <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

The slope of the initial [[complex_numbers_in_mathematics | complex number]] u + vi from the origin is v/u <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. Since u and v can be any integers, this method generates every possible [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | rational slope]] <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. Therefore, the radial lines generated by this method must pass through every [[unit_circle_and_rational_points_in_relation_to_pythagorean_triples | rational point on the unit circle]], ensuring that every possible [[introduction_to_pythagorean_triples | Pythagorean triple]] is accounted for <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.