---
title: Symmetry in dot products
videoId: LyGKycYT2v0
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_dot_products | dot product]] is a fundamental concept in linear algebra, often introduced early in a course <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While its numerical calculation involves pairing coordinates, multiplying them, and summing the results <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, its [[geometric_interpretation_of_dot_products | geometric interpretation]] reveals interesting properties, particularly concerning symmetry.

## Apparent Asymmetry and Underlying Symmetry

The standard [[geometric_interpretation_of_dot_products | geometric interpretation of the dot product]] between two vectors, `v` and `w`, involves projecting `w` onto the line containing `v`. The dot product `v ⋅ w` is then calculated by multiplying the length of this projection by the length of `v` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This interpretation appears "weirdly asymmetric" because it treats the two vectors differently <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

However, a surprising property of the dot product is that order does not matter: `v ⋅ w` is equal to `w ⋅ v` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This means projecting `v` onto `w` and multiplying the length of the projected `v` by the length of `w` yields the same result <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

The intuition for this symmetry is clearer when considering two vectors `v` and `w` of the same length. In this case, projecting `w` onto `v` (and scaling by `|v|`) is a complete mirror image of projecting `v` onto `w` (and scaling by `|w|`), demonstrating why the results are identical <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Effects of Scaling

Even when the vectors do not have equal lengths, such as when one vector `v` is scaled by a constant (e.g., `2v`), the dot product maintains its commutative property despite the "symmetry being broken" in the visual interpretation <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

Consider `(2v) ⋅ w`:
*   If `w` is projected onto `v`, scaling `v` by 2 doubles the length of the vector `v` but does not change the length of the projection of `w` onto `v`. Thus, the dot product `(2v) ⋅ w` is twice `v ⋅ w` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   If `v` is projected onto `w`, scaling `v` by 2 doubles the length of the projection of `v` onto `w`, while the length of `w` remains constant. This also results in the dot product `(2v) ⋅ w` being twice `v ⋅ w` <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

The effect of scaling on the value of the dot product is consistent across both interpretations, even though the geometric symmetry is altered <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Symmetry in Projection Transformations

The connection between the numerical and geometric definitions of the dot product can be understood through the concept of duality, specifically by examining [[linear_transformations_and_dot_products | linear transformations]] from multiple dimensions to a one-dimensional number line <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

When defining a linear transformation by projecting 2D vectors onto a diagonal copy of the number line, anchored at the origin and passing through a unit vector `u-hat` <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>, we can use symmetry to determine the components of its corresponding 1x2 matrix.

To find where the basis vector `i-hat` lands after projection onto the line containing `u-hat`:
*   Since both `i-hat` and `u-hat` are unit vectors, projecting `i-hat` onto the line through `u-hat` is symmetric to projecting `u-hat` onto the x-axis <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Projecting `u-hat` onto the x-axis simply means taking its x-coordinate <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   Therefore, the number where `i-hat` lands on the diagonal number line is the x-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

The same reasoning applies to `j-hat`, which lands on the y-coordinate of `u-hat` when projected onto the diagonal number line <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. This means the entries of the 1x2 matrix describing this projection transformation are precisely the coordinates of `u-hat` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

The numerical operation of applying this linear transformation to any vector is computationally identical to taking the dot product with `u-hat` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This reveals why the dot product with a unit vector can be interpreted as projecting a vector onto its span and taking the length <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.