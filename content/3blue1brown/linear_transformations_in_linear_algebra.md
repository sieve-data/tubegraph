---
title: Linear transformations in linear algebra
videoId: LyGKycYT2v0
---

From: [[3blue1brown]] <br/> 

Traditionally, dot products are introduced early in a linear algebra course, but a fuller understanding of their role emerges under the light of [[linear_transformations | linear transformations]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This article explores the connection between dot products and [[linear_transformations | linear transformations]], especially those that map higher dimensions to a single dimension (the number line).

## Dot Product: Numerical and Geometric Interpretations

Numerically, the dot product of two vectors of the same dimension (lists of numbers with the same lengths) involves pairing up corresponding coordinates, multiplying those pairs, and adding the results <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

*   For example, the vector `(1, 2)` dotted with `(3, 4)` is `(1 * 3) + (2 * 4)` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   The vector `(6, 2, 8, 3)` dotted with `(1, 8, 5, 3)` is `(6 * 1) + (2 * 8) + (8 * 5) + (3 * 3)` <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

Geometrically, the dot product between two vectors `v` and `w` can be visualized by projecting `w` onto the line passing through the origin and the tip of `v` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The dot product `v ⋅ w` is then the length of this projection multiplied by the length of `v` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

*   If the projection of `w` points in the opposite direction from `v`, the dot product is negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   When vectors generally point in the same direction, their dot product is positive <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   When they are perpendicular (the projection of one onto the other is the zero vector), their dot product is zero <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   If they point in generally opposite directions, their dot product is negative <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Symmetry of the Dot Product

Despite the asymmetric nature of the geometric interpretation (projecting `w` onto `v`), the order of vectors in a dot product does not matter: projecting `v` onto `w` and multiplying by the length of `w` yields the same result as projecting `w` onto `v` and multiplying by the length of `v` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

If `v` and `w` have the same length, projecting `w` onto `v` and multiplying by the length of `v` is a mirror image of projecting `v` onto `w` and multiplying by the length of `w` <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. If one vector, say `v`, is scaled by a constant (e.g., 2), the dot product `2v ⋅ w` will be exactly twice `v ⋅ w` <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This holds true whether you consider `w` projected onto `2v` (where `2v`'s length doubles) or `2v` projected onto `w` (where `2v`'s projection length doubles) <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## Linear Transformations to One Dimension

A deeper [[understanding_linear_algebra | understanding]] of the dot product comes from examining its relationship with [[linear_transformations | linear transformations]] from multiple dimensions to one dimension (the number line) <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

*   These are functions that take a 2D vector and output a single number <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   Unlike general functions, [[linear_transformations | linear transformations]] are restricted by specific properties <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   A key visual property of [[linear_transformations | linear transformations]] is that if you apply them to a line of evenly spaced dots, those dots will remain evenly spaced in the output space <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. If dots become unevenly spaced, the transformation is not linear <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

### Matrix Representation

Similar to [[matrix_representations_of_linear_transformations | transformations in higher dimensions]], a [[linear_transformations | linear transformation]] to the number line is completely determined by where it maps the basis vectors, i-hat and j-hat <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Since each basis vector lands on a single number, when these landing spots are recorded as columns of a matrix, each column contains only one number <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This results in a 1x2 matrix for a 2D input space <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

**Example:**
A linear transformation that maps i-hat to 1 and j-hat to -2 <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
To find where a vector `(4, 3)` lands:
1.  Break it down: `4 * i-hat + 3 * j-hat` <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
2.  Due to linearity, the transformed vector will be `4 * (where i-hat lands) + 3 * (where j-hat lands)` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  So, `4 * 1 + 3 * (-2) = 4 - 6 = -2` <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
This calculation is numerically identical to [[matrix_representations_of_linear_transformations | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

## Duality: Connecting Vectors and Transformations

The numerical operation of multiplying a 1x2 matrix by a vector strongly resembles taking a dot product of two vectors <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. This suggests a "nice association" between 1x2 matrices and 2D vectors, where one can be obtained by "tipping" the other on its side <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Geometrically, this hints at a deep connection between [[linear_transformations | linear transformations]] that map vectors to numbers and the vectors themselves <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

### The Projection Transformation Example

Consider a 2D projection transformation where 2D vectors are projected straight onto a diagonally placed copy of the number line <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. This function takes 2D vectors to numbers and is linear, as it preserves the even spacing of dots <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

To find the 1x2 matrix describing this projection, we determine where i-hat and j-hat land on this diagonal number line <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

*   Let `u-hat` be the 2D unit vector whose tip sits at the number 1 on this diagonal number line <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   Due to symmetry, projecting i-hat onto the line passing through `u-hat` is equivalent to projecting `u-hat` onto the x-axis <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Projecting `u-hat` onto the x-axis simply gives its x-coordinate <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   Therefore, the number where i-hat lands when projected onto the diagonal number line is the x-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   Similarly, the y-coordinate of `u-hat` gives the number where j-hat lands <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

Thus, the entries of the 1x2 matrix describing this projection transformation are the coordinates of `u-hat` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Applying this projection (which involves multiplying the matrix by a vector) is computationally identical to taking a dot product with `u-hat` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

This explains why dotting a vector with a unit vector (`u-hat`) can be interpreted as projecting the vector onto the span of that unit vector and taking the length <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

For non-unit vectors (e.g., `u-hat` scaled by 3), the numerical components of the associated matrix are also scaled <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. This means the transformation projects any vector onto the number line and then multiplies the result by the scaling factor <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. This demonstrates why the dot product with a non-unit vector involves first projecting onto that vector and then scaling the length of that projection by the length of the vector <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

### What is Duality?

The core lesson is that any [[linear_transformations | linear transformation]] whose output space is the number line will correspond to a unique vector `v` such that applying the transformation is the same as taking a dot product with `v` <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. This concept is known as duality in mathematics <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

> [!info] Duality
> Loosely speaking, duality refers to natural but surprising correspondences between two types of mathematical things <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. In linear algebra, the dual of a vector is the [[linear_transformations | linear transformation]] it encodes, and the dual of a [[linear_transformations | linear transformation]] from some space to one dimension is a specific vector in that space <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

The dot product is a useful geometric tool for projections and determining directional alignment <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. However, at a deeper level, dotting two vectors together is a way to translate one into the world of transformations <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Often, a vector can be more easily understood not just as an arrow, but as the physical embodiment of a [[linear_transformations | linear transformation]] <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. The vector can be seen as a conceptual shorthand for a transformation, simplifying how we think about moving space to the number line <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.