---
title: Generating and understanding rational points on the unit circle
videoId: QJYmyhnaaek
---

From: [[3blue1brown]] <br/> 

The exploration of [[visualizing_pythagorean_triples_using_complex_numbers | Pythagorean triples]] provides a fascinating path to understanding rational points on the unit circle. These two concepts are deeply interconnected, with methods for finding one set naturally leading to the other.

## Pythagorean Triples

A Pythagorean triple is a set of three whole numbers, `a`, `b`, and `c`, such that `a^2 + b^2 = c^2` <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Common examples include the 3-4-5 triangle and the 5-12-13 triangle <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. It's noteworthy that such integer solutions only exist for squares; if the exponent is changed to any whole number greater than 2, there are no integer solutions, as stated by Fermat's Last Theorem <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

The search for [[visualizing_pythagorean_triples_using_complex_numbers | Pythagorean triples]] is an ancient problem, with Babylonian clay tablets from 1800 BC already listing these triples <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Visual Proof of the Pythagorean Theorem
A visual proof of the Pythagorean theorem involves arranging squares and triangles <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>:
1.  Start by drawing a square on each side of a right triangle <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
2.  Take the square built on the hypotenuse (`c^2`) and add four copies of the original triangle around it to form a larger square with side lengths `a + b` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
3.  Alternatively, arrange the squares built on the two shorter sides (`a^2` and `b^2`) along with four copies of the original triangle to also form a large square with side lengths `a + b` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
4.  By comparing the "negative space" (the area of the large square minus four times the area of the triangle) in both arrangements, it becomes clear that `a^2 + b^2 = c^2` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Reframing the Problem: Lattice Points and Distance
The question of finding [[visualizing_pythagorean_triples_using_complex_numbers | Pythagorean triples]] is equivalent to finding lattice points (points with integer coordinates) on a plane that are a whole number distance away from the origin <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. For example, the point (3,4) is 5 units away from the origin, and (12,5) is 13 units away <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Most lattice points, like (2,1), are not a whole number distance away (e.g., √5) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Generating Triples Using Complex Numbers
A surprising and effective way to generate [[visualizing_pythagorean_triples_using_complex_numbers | Pythagorean triples]] involves using the [[complex_numbers_introduction | complex plane]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### The Squaring Method
1.  **Represent Lattice Points as Complex Numbers**: Think of each lattice point (u,v) as a [[geometric_representation_of_complex_numbers | complex number]] `u + vi` <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
2.  **Square the Complex Number**: Squaring a complex number `u + vi` (where u and v are integers) guarantees that each component of the result will also be an integer <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
    *   Algebraically, `(u + vi)^2 = (u^2 - v^2) + (2uv)i` <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. The real part is `u^2 - v^2` and the imaginary part is `2uv` <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
    *   Geometrically, squaring a complex number doubles its angle from the horizontal axis and squares its length (or magnitude) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Since the initial length was the square root of some whole number (e.g., √(u^2 + v^2)), squaring it results in a whole number (u^2 + v^2) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
3.  **Forming the Triple**: The resulting complex number `(u^2 - v^2) + (2uv)i` has integer coordinates and an integer magnitude `u^2 + v^2` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This directly forms a Pythagorean triple: `(u^2 - v^2)^2 + (2uv)^2 = (u^2 + v^2)^2` <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

For example:
*   Starting with `2 + i` (distance √5) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, its square is `(2^2 - 1^2) + (2*2*1)i = 3 + 4i` <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. The magnitude is 5, giving the 3-4-5 triple <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   Starting with `3 + 2i` (distance √13) <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>, its square is `(3^2 - 2^2) + (2*3*2)i = 5 + 12i` <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. The magnitude is 13, giving the 5-12-13 triple <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   Starting with `4 + i` <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>, its square is `15 + 8i`, with a distance of 17, giving the 15-8-17 triple <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

However, some "boring" triples can be generated, such as when starting coordinates are the same (e.g., `2 + 2i` squared gives `8i`, corresponding to `0^2 + 8^2 = 8^2`) or one coordinate is zero <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Visualizing the Transformation
By observing how every point `z` on the complex plane moves to `z^2` <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>, the grid lines transform into parabolic arcs <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. The intersections of these arcs represent where lattice points land after squaring, thus corresponding to [[visualizing_pythagorean_triples_using_complex_numbers | Pythagorean triples]] <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. The resulting triples appear in an organized pattern, not random <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Accounting for All Pythagorean Triples
The direct squaring method doesn't generate *every* [[visualizing_pythagorean_triples_using_complex_numbers | Pythagorean triple]] <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. For example, `6 + 8i` (from the 6-8-10 triple) is missed <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>, as is `9 + 12i` <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. These "missed" triples are simply multiples of triples that *are* hit (e.g., 6-8-10 is a multiple of 3-4-5, which comes from `2+i` squared) <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. Also, points with an odd imaginary component (like `4+3i`) are never directly hit <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>, but `8+6i` (from `3+i` squared) is, and `4+3i` is `1/2` times that point <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

To account for all triples, one can take each point generated by the squaring method and draw a line from the origin through it to infinity <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. All lattice points on this line represent multiples of the original triple, thereby covering every possible [[visualizing_pythagorean_triples_using_complex_numbers | Pythagorean triple]] <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

## Connection to Rational Points on the Unit Circle
The problem of finding [[visualizing_pythagorean_triples_using_complex_numbers | Pythagorean triples]] is equivalent to finding points on the unit circle (`x^2 + y^2 = 1`) that have [[rational_and_irrational_numbers_in_music | rational]] coordinates <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

### Equivalence
If `a^2 + b^2 = c^2`, dividing by `c^2` gives `(a/c)^2 + (b/c)^2 = 1` <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. Here, `x = a/c` and `y = b/c` are [[rational_and_irrational_numbers_in_music | rational numbers]] and lie on the unit circle. Conversely, if `(x,y)` is a [[rational_and_irrational_numbers_in_music | rational point]] on the unit circle, multiplying by a common denominator will result in integer coordinates whose distance from the origin is also an integer, thus forming a [[visualizing_pythagorean_triples_using_complex_numbers | Pythagorean triple]] <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

### Proof of Completeness
Projecting all the points generated by the squaring method (and their multiples along radial lines) onto the unit circle yields a collection of [[rational_and_irrational_numbers_in_music | rational points]] on that circle <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. To prove this method accounts for *every* rational point on the unit circle (and thus every [[visualizing_pythagorean_triples_using_complex_numbers | Pythagorean triple]]):

1.  **Rational Point to Rational Slope**: Take any [[rational_and_irrational_numbers_in_music | rational point]] `(x,y)` on the unit circle and draw a line between it and the point `(-1,0)` <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The slope of this line will be a [[rational_and_irrational_numbers_in_music | rational number]] because both the rise (`y - 0`) and the run (`x - (-1)`) are [[rational_and_irrational_numbers_in_music | rational]] <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
2.  **Connecting Slopes**:
    *   Our initial complex number `u + vi` forms a line from the origin with a slope of `v/u` <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
    *   Let the angle of `u + vi` be `theta` <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. Squaring `u + vi` results in a complex number whose angle is `2 * theta` <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
    *   When this squared point is projected onto the unit circle, it creates a [[rational_and_irrational_numbers_in_music | rational point]] at angle `2 * theta` <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
    *   According to circle geometry, the angle formed by two points on the circumference and the center of the circle (`2 * theta`) is exactly twice the angle formed by those same two points and any other point on the circumference (`theta`) <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
    *   Applying this, the line connecting the rational point on the unit circle (at angle `2 * theta`) and `(-1,0)` must make an angle `theta` with the horizontal <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
    *   Therefore, this line has the *same slope* as the line from the origin to our initial complex number `u + vi` <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
3.  **Conclusion**: Since `u` and `v` can be any integers <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>, the slope `v/u` can represent *every possible [[rational_and_irrational_numbers_in_music | rational number]]* <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. This means that every [[rational_and_irrational_numbers_in_music | rational point]] on the unit circle is accounted for, and consequently, every possible [[visualizing_pythagorean_triples_using_complex_numbers | Pythagorean triple]] is generated by this method <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.