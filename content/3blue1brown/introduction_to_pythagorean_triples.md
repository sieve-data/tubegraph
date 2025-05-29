---
title: Introduction to Pythagorean triples
videoId: QJYmyhnaaek
---

From: [[3blue1brown]] <br/> 

When first introduced to the [[Proof and demonstration of the Pythagorean theorem | Pythagorean theorem]], which states that the sum of the squares of the two shorter sides of a right triangle always equals the square of its hypotenuse <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>, common examples like the 3-4-5 triangle or the 5-12-13 triangle are often encountered <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. It is noteworthy that examples exist where the sum of two perfect squares results in a perfect square <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. In contrast, if the exponent were changed to any whole number greater than 2, there would be no integer solutions, a concept known as Fermat's Last Theorem <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

Any triplet of whole numbers (a, b, c) that satisfies the equation a² + b² = c² is known as a [[Pythagorean triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The objective is to find every possible example of these triples and visualize how they fit together <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Historical Context

The concept of [[Pythagorean triples]] is ancient, with Babylonian clay tablets from 1800 BC (more than a millennium before Pythagoras) listing such triples <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Proof of the Pythagorean Theorem

A favorite [[Proof and demonstration of the Pythagorean theorem | proof]] of the [[Proof and demonstration of the Pythagorean theorem | Pythagorean theorem]] involves a visual demonstration <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>:
1.  Draw a square on each side of a right triangle <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  Take the square built on the hypotenuse (c-square) and add four copies of the original triangle around it to form a larger square with side lengths (a + b) <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
3.  Alternatively, arrange the squares built on the two shorter sides (a-square and b-square) together with four copies of the original triangle to also form a large square with side lengths (a + b) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
4.  The negative space within each of these larger squares (the area of the big square minus four times the area of the triangle) is clearly a² + b² from one arrangement, and c² from the other, thus proving a² + b² = c² <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Reframing the Problem: Lattice Points

The problem of finding [[Pythagorean triples]] can be reframed as finding points on a plane with integer coordinates ([[Visualization of Pythagorean triples using lattice points | lattice points]]) that are a whole number distance away from the origin <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   For example, the point (3,4) is 5 units away from the origin <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   The point (12,5) is 13 units away <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

Most points, like (2,1), are not a whole number distance from the origin; their distance is the square root of a whole number (e.g., √(2² + 1²) = √5) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Generating Triples Using Complex Numbers

A powerful method for generating [[Pythagorean triples]] involves [[Complex numbers and generating Pythagorean triples | complex numbers]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### The Squaring Method
Consider the plane as a complex plane, where each [[Visualization of Pythagorean triples using lattice points | lattice point]] (x,y) corresponds to a [[Complex numbers and generating Pythagorean triples | complex number]] x + yi <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
Squaring such a [[Complex numbers and generating Pythagorean triples | complex number]] (x + yi)² produces a new point whose distance from the origin is guaranteed to be a whole number <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

#### Algebraic and Geometric Interpretation
*   **Algebraically:** When a [[Complex numbers and generating Pythagorean triples | complex number]] (u + vi) is squared, the result is (u² - v²) + (2uv)i <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. Since u and v are integers, both the real (u² - v²) and imaginary (2uv) components of the result are guaranteed to be integers <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Geometrically:** Multiplying a [[Complex numbers and generating Pythagorean triples | complex number]] by itself doubles its angle from the horizontal axis and squares its length (magnitude) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. If the initial length was the square root of some whole number (e.g., √(u² + v²)), squaring it guarantees the resulting length will be a whole number (u² + v²) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

#### Examples
*   Starting with 2 + i (distance √5), squaring it yields (2² - 1²) + (2 * 2 * 1)i = 3 + 4i <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. The distance of 3 + 4i from the origin is 5, forming the 3-4-5 triple <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   Starting with 3 + 2i (distance √13), squaring it yields (3² - 2²) + (2 * 3 * 2)i = 5 + 12i <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. The distance of 5 + 12i from the origin is 13, forming the 5-12-13 triple <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   Starting with 4 + i, squaring it yields 15 + 8i, which has a distance of 17 from the origin, forming the 8-15-17 triple <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

#### General Formula
If the initial integer coordinates are u and v (representing u + vi), then the resulting [[Pythagorean triples | Pythagorean triple]] (a, b, c) is given by:
*   a = u² - v² <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>
*   b = 2uv <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>
*   c = u² + v² (the distance from the origin) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>

This formula serves as a "machine" that takes any pair of integers (u, v) and produces a [[Pythagorean triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

#### Visualization
When every point *z* on the complex plane is mapped to *z²*, the grid lines transform into parabolic arcs <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. The intersections of these parabolic arcs correspond to [[Visualization of Pythagorean triples using lattice points | lattice points]] that are the result of squaring initial [[Visualization of Pythagorean triples using lattice points | lattice points]] <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. A triangle formed by such a point and the origin will have whole number side lengths <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. This visualization shows a remarkable organization among [[Pythagorean triples]], which might otherwise appear random <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Accounting for All Pythagorean Triples

The squaring method alone does not directly produce *every* [[Pythagorean triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. For instance, the point 6 + 8i (corresponding to the 6-8-10 triple) is never directly obtained by squaring integers u and v <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. Similarly, 9 + 12i is missed <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

However, these "missed" triples are simply multiples of triples that *are* hit by the method <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. For example, 6-8-10 is a multiple of 3-4-5, which is generated by (2+i)² <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. The method also misses 4+3i (as the imaginary component is odd), but it hits 8+6i (from 3+i²), of which 4+3i is half <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

To account for all possible [[Pythagorean triples]], one can take each point generated by the squaring method and draw a radial line from the origin through it <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. All [[Visualization of Pythagorean triples using lattice points | lattice points]] along this line represent multiples of the original triple, ensuring every possible [[Pythagorean triples | Pythagorean triple]] is covered <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

## Connection to the Unit Circle and Rational Points

The problem of finding [[Pythagorean triples]] is equivalent to finding [[Unit circle and rational points in relation to Pythagorean triples | rational points on the unit circle]] <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
If a² + b² = c², dividing by c² gives (a/c)² + (b/c)² = 1 <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This means (a/c, b/c) is a point on the unit circle (x² + y² = 1) where both coordinates are rational numbers <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. Conversely, any [[Unit circle and rational points in relation to Pythagorean triples | rational point on the unit circle]] can be scaled up to produce a [[Pythagorean triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

Projecting all the generated points (and their multiples) onto the [[Unit circle and rational points in relation to Pythagorean triples | unit circle]] results in a set of [[Unit circle and rational points in relation to Pythagorean triples | rational points]] on that circle <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. If all infinitely many radial lines corresponding to every squared [[Visualization of Pythagorean triples using lattice points | lattice point]] were drawn, they would fill every pixel of the screen <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

### Proof of Completeness
To prove that this method accounts for every possible [[Pythagorean triples | Pythagorean triple]], consider any [[Unit circle and rational points in relation to Pythagorean triples | rational point]] (x, y) on the [[Unit circle and rational points in relation to Pythagorean triples | unit circle]] <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
1.  Draw a line between this rational point and the point (-1, 0) on the unit circle <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
2.  The slope of this line (rise over run) will be a rational number <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
3.  Recall that our method starts with an integer point u + vi, which makes an angle `theta` with the horizontal axis <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
4.  Squaring this number yields a point with an angle of `2 * theta` <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
5.  When this point is projected onto the [[Unit circle and rational points in relation to Pythagorean triples | unit circle]], the corresponding [[Unit circle and rational points in relation to Pythagorean triples | rational point]] also has an angle of `2 * theta` <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
6.  A geometric property of circles states that the angle subtended by two points at the center (e.g., `2 * theta`) is twice the angle subtended by those same points at any other point on the circumference (e.g., at -1) <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
7.  Therefore, the line drawn from (-1, 0) to the [[Unit circle and rational points in relation to Pythagorean triples | rational point]] on the circle makes an angle of `theta` with the horizontal <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
8.  The slope of this line is `v/u`, which is the slope of the initial line from the origin to u + vi <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
9.  Since u and v can be any integers, their ratio `v/u` can represent any possible rational slope <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
10. Thus, our method of squaring [[Complex numbers and generating Pythagorean triples | complex numbers]] and drawing radial lines accounts for every possible rational slope, which in turn means it hits every possible [[Unit circle and rational points in relation to Pythagorean triples | rational point on the unit circle]] <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

This demonstrates that the method hits every possible [[Pythagorean triples | Pythagorean triple]] <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

---
The concepts discussed here are closely related to topics such as [[Prime numbers and their regularities | prime number regularities]] and their connection to pi <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.