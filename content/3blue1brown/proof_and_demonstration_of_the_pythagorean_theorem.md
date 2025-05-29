---
title: Proof and demonstration of the Pythagorean theorem
videoId: QJYmyhnaaek
---

From: [[3blue1brown]] <br/> 

The [[Pythagorean Theorem]] states that the sum of the squares of the two shorter sides on a right triangle always equals the square of its hypotenuse <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Common examples of this include the 3-4-5 triangle and the 5-12-13 triangle <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. It's easy to overlook the fact that examples where the sum of two perfect squares results in a perfect square even exist <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. In contrast, if the exponent were any whole number greater than 2, there would be no integer solutions, a principle known as Fermat's Last Theorem <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

A special name for any triplet of whole numbers (a, b, c) where a² + b² = c² is a [[introduction_to_pythagorean_triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The question of finding all such triples is ancient, with Babylonian clay tablets from 1800 BC (more than a millennium before Pythagoras) already listing these triples <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## A Visual Proof of the Pythagorean Theorem

One favorite [[visual_proofs_and_triangle_isosceles | visual proof]] of the [[Pythagorean Theorem]] begins by drawing a square on each side of a right triangle <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

1.  Take the square on the hypotenuse (the 'c' square) and arrange four copies of the original triangle around it <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This forms a larger square with side lengths of (a + b) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
2.  Alternatively, arrange the squares on the two shorter sides (the 'a' square and 'b' square) together with four copies of the original triangle <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This also forms a large square with side lengths of (a + b) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

By comparing the "negative space" within each of these larger (a+b) squares, the proof becomes clear <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. The area of the big square minus four times the area of the triangle is, from one perspective, clearly a² + b², and from another, it is c² <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Therefore, a² + b² = c² <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Finding All Pythagorean Triples Using Complex Numbers

The problem of finding [[introduction_to_pythagorean_triples | Pythagorean triples]] is equivalent to finding lattice points (points with integer coordinates) on a plane that are a whole number distance away from the origin <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. For example, the point (3,4) is a distance 5 from the origin, and (12,5) is a distance 13 <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### The Role of Complex Numbers

Consider the complex plane, where each point (x,y) is represented as a complex number x + yi <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. The distance of a complex number from the origin is its magnitude, |x + yi| = sqrt(x² + y²) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

Squaring a complex number with integer coordinates, such as (u + vi), guarantees that the resulting complex number will also have integer coordinates <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. More importantly, squaring a complex number doubles its angle from the horizontal axis and squares its length (magnitude) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. If the initial length is the square root of a whole number (e.g., sqrt(5) for 2+i), the resulting length after squaring is guaranteed to be a whole number (e.g., 5) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

This method can generate [[introduction_to_pythagorean_triples | Pythagorean triples]]:
*   Squaring (2 + i) algebraically yields 3 + 4i, corresponding to the 3-4-5 triangle (magnitude 5) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   Squaring (3 + 2i) yields 5 + 12i, corresponding to the 5-12-13 triangle (magnitude 13) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   Squaring (4 + i) yields 15 + 8i, corresponding to the 15-8-17 triple (magnitude 17) <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

Some "boring" triples can result if the initial coordinates are the same (e.g., (2+2i)² = 8i, yielding a 0-8-8 triple) or if one is zero <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### General Formula for Pythagorean Triples

For an initial point (u + vi), squaring it yields:
*   Real part: u² - v²
*   Imaginary part: 2uv
*   Resulting magnitude (hypotenuse): u² + v²

Thus, any [[introduction_to_pythagorean_triples | Pythagorean triple]] (a, b, c) can be generated by a = u² - v², b = 2uv, and c = u² + v² for integers u and v <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

### Visualizing the Generation

When every point `z` on the complex plane is mapped to `z²`, the grid lines transform into parabolic arcs <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. The intersections of these arcs represent where lattice points landed, corresponding to [[introduction_to_pythagorean_triples | Pythagorean triples]] <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This visualization organizes seemingly random triples into a clear pattern <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Proof of Completeness: Accounting for All Pythagorean Triples

While squaring complex numbers generates many triples, it doesn't immediately account for all of them, such as 6-8-10, which is a multiple of 3-4-5 <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. The method misses multiples of triples it hits <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>, as well as triples where the imaginary component is odd (e.g., 4+3i is missed, but 8+6i is hit) <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

To account for all triples, radial lines are drawn from the origin through each generated point, extending to infinity <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. All lattice points hit by these lines represent every possible [[introduction_to_pythagorean_triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Connecting to Rational Points on the Unit Circle

The expression a² + b² = c² can be transformed by dividing by c² into (a/c)² + (b/c)² = 1 <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This represents a point (x, y) on the unit circle (x² + y² = 1) where x and y are rational numbers, known as a rational point of the unit circle <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. Conversely, any rational point on the unit circle can be scaled up by a common denominator to yield a [[introduction_to_pythagorean_triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:10:56">[00:11:00]</a>.

Projecting all the generated points (and their multiples along radial lines) onto the unit circle results in a collection of rational points on that circle <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. The proof of completeness relies on showing that *every* rational point on the unit circle is hit by this method <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

### The Slope Argument

Take any rational point on the unit circle and draw a line between it and the point (-1, 0) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The slope of this line will always be a rational number, as both the rise and run are rational <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

If an initial complex number (u + vi) makes an angle θ with the horizontal axis, squaring it results in a point that makes an angle 2θ <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. When this point is projected onto the unit circle, the rational point also has an angle of 2θ from the horizontal <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. A geometric property of circles states that the angle at the center (2θ) is twice the angle made by the same points and any other point on the circumference (θ), provided that other point isn't between the original two points <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This means the line connecting the rational point on the circle to (-1, 0) makes an angle θ with the horizontal <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

Crucially, this line has the same slope as the line between the origin and the initial complex number (u + vi) <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. The slope of (u + vi) from the origin is v/u <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. Since u and v can be any integers, *every possible rational slope* can be generated this way <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

Therefore, the radial lines from this method, determined by all possible choices of integers u and v, must pass through every rational point on the unit circle <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. This comprehensive approach ensures that every possible [[introduction_to_pythagorean_triples | Pythagorean triple]] is accounted for <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.