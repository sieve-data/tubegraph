---
title: Geometric interpretation of dot products
videoId: LyGKycYT2v0
---

From: [[3blue1brown]] <br/> 

## Introduction to Dot Products
Traditionally, [[introduction_to_dot_products | dot products]] are introduced early in a linear algebra course, often at the start <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While a basic understanding of vectors is sufficient for their introduction, a fuller understanding of their role in mathematics is found under the light of [[linear_transformations_and_dot_products | linear transformations]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

Numerically, the dot product of two vectors of the same dimension involves pairing up all corresponding coordinates, multiplying those pairs together, and adding the results <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   For example, the dot product of vector (1, 2) and (3, 4) is (1 * 3) + (2 * 4) <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   For vectors (6, 2, 8, 3) and (1, 8, 5, 3), the dot product is (6 * 1) + (2 * 8) + (8 * 5) + (3 * 3) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Geometric Interpretation
The numerical computation of the dot product has a distinct [[geometric_representation_of_cross_products | geometric interpretation]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. To conceptualize the dot product between two vectors, `v` and `w`:
1.  Imagine projecting `w` onto the line that passes through the origin and the tip of `v` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  Multiply the length of this projection by the length of `v` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This product is `v` dot `w` <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Directional Significance
The sign of the dot product indicates the general direction of the vectors relative to each other:
*   If the projection of `w` points in the opposite direction from `v`, the dot product will be negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   When two vectors generally point in the same direction, their dot product is positive <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   When they are perpendicular, meaning the projection of one onto the other is the zero vector, their dot product is zero <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   If they point in generally opposite directions, their dot product is negative <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

## Symmetry in Dot Products
The geometric interpretation, which initially appears asymmetric, treats the two vectors differently <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. However, the order of vectors in a dot product does not matter; projecting `v` onto `w` and multiplying its length by `w`'s length yields the same result <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This property is known as [[symmetry_in_dot_products | symmetry in dot products]].

### Intuition for Symmetry
If vectors `v` and `w` have the same length, projecting `w` onto `v` (then multiplying by `v`'s length) is a complete mirror image of projecting `v` onto `w` (then multiplying by `w`'s length) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

When one vector is scaled (e.g., `v` by 2), the symmetry is broken <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   If `w` is projected onto `2v`, the projection length of `w` doesn't change, but the length of `2v` is doubled, making `(2v)` dot `w` twice `v` dot `w` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   If `2v` is projected onto `w`, the length of the projection of `2v` is scaled by 2, while the length of `w` remains constant. The overall effect is still to double the dot product <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
Even with broken symmetry, the effect of scaling on the dot product value is consistent across both interpretations <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Duality and Linear Transformations
A deeper understanding of why the numerical dot product relates to projection involves the concept of duality <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This requires exploring [[linear_transformations_and_dot_products | linear transformations]] that map multiple dimensions to a single dimension (the number line) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

### Linear Transformations to the Number Line
*   These are functions that take a 2D vector and output a single number <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   A key visual property of these linear transformations is that a line of evenly spaced dots remains evenly spaced when mapped to the number line <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   Such a transformation is completely determined by where it maps the basis vectors, `i-hat` and `j-hat` <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Since they land on a number, their landing spots form the columns of a 1x2 matrix <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   Applying this transformation to a vector (e.g., 4, 3) means multiplying its components by where `i-hat` and `j-hat` land (e.g., 4 * 1 + 3 * -2 = -2) <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This numerical process is [[linear_transformations_and_dot_products | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

### The Connection to Dot Products
The numerical operation of multiplying a 1x2 matrix by a vector is similar to taking the dot product of two vectors <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. This suggests an association between 1x2 matrices and 2D vectors, where one can be tipped on its side to become the other <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

Consider placing a copy of the number line diagonally in 2D space, with 0 at the origin <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. Let `u-hat` be the 2D unit vector whose tip sits at the number 1 on this diagonal number line <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

*   Projecting 2D vectors straight onto this diagonal number line defines a linear transformation from 2D vectors to numbers <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   To find the 1x2 matrix describing this projection transformation, one must determine where `i-hat` and `j-hat` land <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
*   Due to symmetry, projecting `i-hat` onto the line through `u-hat` is equivalent to projecting `u-hat` onto the x-axis, which is simply `u-hat`'s x-coordinate <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Similarly, projecting `j-hat` onto the number line gives `u-hat`'s y-coordinate <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

Therefore, the entries of the 1x2 matrix describing the projection transformation are the coordinates of `u-hat` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Computing this transformation for arbitrary vectors by matrix multiplication is computationally identical to taking a dot product with `u-hat` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This explains why dotting with a unit vector is interpreted as projecting onto its span and taking the length <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

For non-unit vectors, scaling `u-hat` by a factor (e.g., 3) results in a matrix that scales the output of the projection by that same factor <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. This means the dot product with a non-unit vector is interpreted as first projecting onto that vector, then scaling the length of that projection by the length of the vector <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

### The Essence of Duality
Any linear transformation whose output space is the number line can be uniquely associated with some vector `v` such that applying the transformation is equivalent to taking a dot product with that vector <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. This "natural but surprising correspondence" between two types of mathematical things is known as [[meaningful_transformations_and_their_ties_to_the_dot_product | duality]] <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

In this linear algebra context:
*   The dual of a vector is the linear transformation it encodes <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   The dual of a linear transformation from a space to one dimension is a certain vector in that space <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

While the dot product is a useful geometric tool for understanding projections and directional alignment <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>, at a deeper level, it translates one vector into the world of transformations <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Vectors can be understood not just as arrows in space, but as the physical embodiment of a linear transformation <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.