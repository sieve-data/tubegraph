---
title: Finding integer solutions with lattice points
videoId: QJYmyhnaaek
---

From: [[3blue1brown]] <br/> 

The exploration of integer solutions, particularly those related to the Pythagorean theorem, involves a fascinating interplay between geometry and number theory. A core concept is the **Pythagorean triple**, defined as a triplet of whole numbers `a, b, c` where `a² + b² = c²` <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Common examples include the 3-4-5 triangle and the 5-12-13 triangle <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. It's notable that such integer solutions exist, especially when compared to Fermat's Last Theorem, which states that for any whole number exponent greater than 2, there are no integer solutions for `aⁿ + bⁿ = cⁿ` <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

The quest to find every possible Pythagorean triple is an ancient mathematical problem, with evidence dating back to Babylonian clay tablets from 1800 BC that list these triples <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Reframing the Problem: Lattice Points

The problem of finding Pythagorean triples can be reframed geometrically: which points on the plane with integer coordinates (known as **lattice points**) are a whole number distance away from the origin? <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a> For instance, the point (3,4) is a distance of 5 from the origin, and (12,5) is a distance of 13 <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This means finding Pythagorean triples is entirely equivalent to locating lattice points that are a whole number distance from the origin <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. While most lattice points, like (2,1), do not have a whole number distance from the origin, their distance is at least the square root of a whole number (e.g., √5 for (2,1)) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Generating Triples Using Complex Numbers

A powerful method for generating Pythagorean triples involves viewing lattice points as [[Complex numbers and Gaussian integers | complex numbers]] <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. If a lattice point (a,b) is represented as a complex number `a + bi`, squaring this complex number `(a + bi)²` can yield a new point whose distance from the origin is guaranteed to be a whole number <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

Algebraically, squaring a complex number `u + vi` results in `(u² - v²) + (2uv)i` <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. Since `u` and `v` are integers, both the real part (`u² - v²`) and the imaginary part (`2uv`) of the result are guaranteed to be integers <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. The magnitude (distance from the origin) of this new complex number is `u² + v²` <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This gives a general formula for Pythagorean triples: `(u² - v², 2uv, u² + v²)`.

Geometrically, complex multiplication involves rotating and stretching <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. If `u + vi` has a length `L` and makes an angle `θ` with the horizontal axis, squaring it doubles the angle to `2θ` and squares its length to `L²` <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Since the initial length `L` is the square root of a whole number (e.g., `√(u² + v²)`, which is `√5` for `2+i`), the resulting length `L²` is guaranteed to be a whole number (e.g., 5) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Examples:
*   Starting with `2 + i`: `(2 + i)² = 3 + 4i`. This corresponds to the 3-4-5 triangle, with a distance of 5 from the origin <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   Starting with `3 + 2i`: `(3 + 2i)² = 5 + 12i`. This yields the 5-12-13 triangle, with a distance of 13 from the origin <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   Starting with `4 + i`: `(4 + i)² = 15 + 8i`. This generates the 8-15-17 triangle, with a distance of 17 from the origin <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

Some choices of `u` and `v` might lead to trivial triples (e.g., if `u=v` or one is zero), such as `2 + 2i` squared yielding `8i`, which corresponds to the 0-8-8 triple <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. However, for the most part, this method effectively generates non-trivial Pythagorean triples <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

### Visualization with `z²` Mapping

Visualizing the transformation `z → z²` reveals how these triples are organized. When every point on the complex plane, including grid lines, is mapped by `z²`, the grid lines transform into parabolic arcs <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. The intersections of these arcs represent where lattice points land, and thus correspond to Pythagorean triples <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This visualization demonstrates an underlying pattern and organization among seemingly random triples <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## Accounting for All Pythagorean Triples

While the squaring method generates many triples, it doesn't account for all of them directly. For example, the triple 6-8-10 (corresponding to 6 + 8i) is missed by this method <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. However, 6-8-10 is simply a multiple of the 3-4-5 triple, which *is* generated (from `2+i` squared) <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. Similarly, 4 + 3i (corresponding to 4-3-5) is missed, but 8 + 6i (corresponding to 8-6-10) is hit (from `3+i` squared), and 4 + 3i is half of 8 + 6i <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

To account for all triples, one must consider every point generated by the squaring method and then draw a line from the origin through that point, extending to infinity <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. All other lattice points hit by these radial lines represent multiples of the original generated triples <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. This combined approach covers every possible Pythagorean triple <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

## Connection to Rational Points on the Unit Circle

The problem of finding Pythagorean triples is closely related to [[Generating and understanding rational points on the unit circle | finding rational points on the unit circle]] (`x² + y² = 1`) <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. If `a² + b² = c²`, dividing by `c²` yields `(a/c)² + (b/c)² = 1`, where `a/c` and `b/c` are rational numbers <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. Conversely, any rational point `(x,y)` on the unit circle can be scaled by a common denominator to yield an integer point whose distance from the origin is also an integer <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

Projecting all the generated (and scaled) lattice points onto the unit circle (by moving them along their radial lines) should cover every rational point on that circle <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. The completeness of this method can be proven by considering the slopes of lines drawn from a rational point on the unit circle to the point (-1,0) <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

Let `u + vi` be the initial complex number with integer coordinates, making an angle `θ` with the horizontal <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. Squaring it produces a complex number at angle `2θ` <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. When this point is projected onto the unit circle, it remains at angle `2θ` <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. A geometric property of circles states that the angle formed by two points on the circumference and the center (`2θ`) is twice the angle formed by those same points and any other point on the circumference (like -1,0), which would be `θ` <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This means the line connecting the rational point on the circle to (-1,0) has a slope equal to the slope of the original line from the origin to `u + vi`, which is `v/u` <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. Since `u` and `v` can be any integers, `v/u` can represent every possible rational slope <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. Therefore, the method effectively hits every rational point on the unit circle, proving that it accounts for every possible Pythagorean triple <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

***

> [!info] Further Connections
> The concepts discussed here are highly related to topics in the [[distribution_of_lattice_points_and_prime_factorization | distribution of lattice points and prime factorization]] <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.