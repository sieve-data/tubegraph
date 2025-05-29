---
title: Pythagorean theorem and triples
videoId: QJYmyhnaaek
---

From: [[3blue1brown]] <br/> 

The [[Pythagorean theorem and triples | Pythagorean theorem]] states that for a right triangle, the sum of the squares of the two shorter sides always equals the square of its hypotenuse <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Common examples of integer side lengths satisfying this theorem include the 3-4-5 triangle and the 5-12-13 triangle <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. It's notable that the sum of two perfect squares can result in another perfect square <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. In contrast, if the exponent were any whole number greater than 2, there would be no integer solutions, a concept known as Fermat's Last Theorem <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

A triplet of whole numbers (a, b, c) where a² + b² = c² is called a Pythagorean triple <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Historical Context

The question of finding [[Pythagorean theorem and triples | Pythagorean triples]] is ancient, with Babylonian clay tablets from 1800 BC listing these triples, over a millennium before Pythagoras himself <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Proof of the Pythagorean Theorem

One visual [[proofs of sphere surface area and triangle properties | proof]] of the [[Pythagorean theorem and triples | Pythagorean theorem]] involves squares drawn on each side of a right triangle <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
1.  Start with the square on the hypotenuse (c-square) and add four copies of the original triangle around it to form a larger square with side lengths (a + b) <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  Alternatively, arrange the squares on the two shorter sides (a-square and b-square) together with four copies of the original triangle to also form a large square with side lengths (a + b) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  The "negative space" in both diagrams (the area of the big square minus four times the area of the triangle) must be equal <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. From one perspective, this area is a² + b² <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>, and from the other, it is c² <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, thus proving a² + b² = c² <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Reframing the Problem: Lattice Points

Finding [[Pythagorean theorem and triples | Pythagorean triples]] is equivalent to finding lattice points (points with integer coordinates) on a plane that are a whole number distance away from the origin <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   For example, the point (3,4) is a distance of 5 from the origin <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   The point (12,5) is a distance of 13 from the origin <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   For most lattice points, like (2,1), the distance from the origin is not a whole number (e.g., √5 for (2,1)) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Generating Triples Using Complex Numbers

A surprising method for generating [[Pythagorean theorem and triples | Pythagorean triples]] involves [[Trigonometry and complex numbers | complex numbers]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
Think of the plane as the complex plane, where each point (a,b) corresponds to a complex number a + bi <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### The Squaring Method
Squaring a complex number of the form u + vi, where u and v are integers, guarantees that its components are integers and its magnitude is a whole number <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

Algebraically, when you square u + vi:
(u + vi)² = u² + 2uvi + (vi)² = u² + 2uvi - v² = (u² - v²) + (2uv)i <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
The resulting real part is (u² - v²), and the imaginary part is (2uv) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The distance from the origin (magnitude) of this new number is (u² + v²) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This directly gives a [[Pythagorean theorem and triples | Pythagorean triple]]: (u² - v²)² + (2uv)² = (u² + v²)² <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

Geometrically, [[Trigonometry in relation to angles and triangles | complex multiplication]] involves rotation and stretching <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. If a complex number z has a length (magnitude) L and an angle θ with the horizontal axis <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>, then z² will have a length of L² and an angle of 2θ <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
Since the initial length L is the square root of a whole number (e.g., √(u² + v²)), squaring it results in a whole number (u² + v²) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Examples:
*   Start with 2 + i: (2 + i)² = 3 + 4i <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. The original number's magnitude is √5, and the squared number's magnitude is 5. This gives the 3-4-5 triangle <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   Start with 3 + 2i: (3 + 2i)² = 5 + 12i <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. The original magnitude is √13, and the squared magnitude is 13. This gives the 5-12-13 triangle <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   Start with 4 + i: (4 + i)² = 15 + 8i <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. This has a distance of 17 from the origin, forming the 15-8-17 triple <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### "Boring" Triples
If the coordinates of the starting complex number (u,v) are the same (e.g., u=v) or one is zero, the resulting triple might include a zero <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. For example, (2 + 2i)² = 8i, which corresponds to the 0-8-8 triple <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

## Visualizing Pythagorean Triples

A powerful way to visualize this process is by mapping every point z on the complex plane to z² <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
When the grid lines of the complex plane are transformed by the z² function, they turn into parabolic arcs <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Every intersection point of these transformed arcs represents a lattice point that is a whole number distance from the origin, thus corresponding to a [[Pythagorean theorem and triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This visualization organizes what often seems like random triples into a clear pattern on nicely spaced curves <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Completeness of the Method

While the squaring method generates many [[Pythagorean theorem and triples | Pythagorean triples]], it does not generate *every* possible triple directly <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   For example, 6-8-10 is a valid triple (6² + 8² = 36 + 64 = 100 = 10²), but there are no integers u and v such that (u + vi)² = 6 + 8i <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   Similarly, 4-3i is missed, as its imaginary component is odd <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. However, 8+6i (which is (3+i)²) is hit, and 4+3i is simply half of 8+6i <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

Any [[Pythagorean theorem and triples | Pythagorean triple]] missed by this method is simply a multiple of a triple that *is* generated <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. By drawing radial lines from the origin through all points generated by the squaring method (and thus through their multiples), every possible [[Pythagorean theorem and triples | Pythagorean triple]] can be accounted for <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

### Connection to Rational Points on the Unit Circle
This problem can be reframed as finding points on a unit circle (x² + y² = 1) that have rational coordinates <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
If a² + b² = c², dividing by c² gives (a/c)² + (b/c)² = 1 <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This means (a/c, b/c) is a rational point on the unit circle. Conversely, any rational point (x,y) on the unit circle, when multiplied by a common denominator, yields integer coordinates whose distance from the origin is also an integer <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

When all points generated by the squaring method (and their multiples) are projected onto the unit circle along their radial lines, they cover all rational points on that circle <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

To demonstrate that this method accounts for *every* rational point on the unit circle:
1.  Take any rational point on the unit circle <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
2.  Draw a line between this point and the point (-1,0) <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
3.  The slope of this line (rise over run) will be a rational number, as both rise and run are rational <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
4.  Consider the initial complex number u + vi used in the squaring method. It makes an angle θ with the horizontal <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
5.  Squaring this number yields a point whose angle is 2θ <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. This 2θ is the angle made by the rational point (from the unit circle) and the origin <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
6.  By [[Geometry and circles | circle geometry]], the angle made by the line connecting (-1,0) to the rational point on the circle is half of the central angle, meaning it is θ <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
7.  Therefore, the slope of this line from (-1,0) to the rational point is the same as the slope of the line from the origin to our initial complex number u + vi <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
8.  The slope of u + vi is v/u <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. Since u and v can be any integers, we can account for every possible rational slope <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
9.  This implies that the radial lines from our method pass through every rational point on the unit circle <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>, ensuring that every possible [[Pythagorean theorem and triples | Pythagorean triple]] is accounted for <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.