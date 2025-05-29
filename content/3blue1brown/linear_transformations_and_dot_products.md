---
title: Linear transformations and dot products
videoId: LyGKycYT2v0
---

From: [[3blue1brown]] <br/> 

Traditionally, the [[introduction_to_dot_products | dot product]] is introduced early in a linear algebra course, often at the very beginning <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While a basic understanding of vectors is sufficient for this initial introduction, a deeper comprehension of the dot product's role in mathematics is best achieved through the lens of [[linear_transformations | linear transformations]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Standard Definition of the Dot Product

Numerically, for two vectors of the same dimension (lists of numbers with the same lengths), their dot product is calculated by pairing up corresponding coordinates, multiplying those pairs together, and then adding the results <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Examples
*   The dot product of vector [1, 2] and vector [3, 4] is (1 × 3) + (2 × 4) = 3 + 8 = 11 <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   The dot product of vector [6, 2, 8, 3] and vector [1, 8, 5, 3] is (6 × 1) + (2 × 8) + (8 × 5) + (3 × 3) = 6 + 16 + 40 + 9 = 71 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Geometric Interpretation of Dot Products

The computation of the dot product has a clear [[geometric_interpretation_of_dot_products | geometric interpretation]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. To understand the dot product between two vectors, `v` and `w`, one can imagine projecting `w` onto the line that passes through the origin and the tip of `v` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. The dot product `v · w` is found by multiplying the length of this projection by the length of `v` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. If the projection of `w` points in the opposite direction from `v`, the dot product will be negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Directional Interpretation
*   When two vectors generally point in the same direction, their dot product is positive <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   When they are perpendicular (meaning the projection of one onto the other is the zero vector), their dot product is zero <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   If they point in generally opposite directions, their dot product is negative <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Symmetry in Dot Products
This geometric interpretation appears asymmetric, treating the two vectors differently <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. However, the order of the vectors in a dot product does not matter: projecting `v` onto `w` and multiplying the length of the projected `v` by the length of `w` yields the same result as projecting `w` onto `v` <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This property is a form of [[symmetry_in_dot_products | symmetry in dot products]].

The intuition behind why order doesn't matter can be understood by considering two scenarios:
1.  **Equal Lengths:** If `v` and `w` have the same length, projecting `w` onto `v` (and multiplying by the length of `v`) is a mirror image of projecting `v` onto `w` (and multiplying by the length of `w`), resulting in the same value <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
2.  **Unequal Lengths (Scaling):** If one vector, say `v`, is scaled by a constant (e.g., `2v`), the symmetry is broken <a class="yt-timestamp" data-t="00:03:00">[00:02:57]</a>.
    *   If `w` is projected onto `2v`, the length of `w`'s projection doesn't change, but the length of the vector being projected onto (which is `2v`) is doubled, thus doubling the dot product `2v · w` compared to `v · w` <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   If `2v` is projected onto `w`, the length of the projection of `2v` is doubled, while the length of `w` remains constant. This also doubles the dot product <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    Even when symmetry is broken by scaling, the effect on the dot product's value is consistent across both interpretations <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Duality: Connecting Dot Products and Linear Transformations

A key question arises: why does the numerical process of multiplying paired coordinates and adding them relate to geometric projection? <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a> The answer lies in a deeper concept known as duality <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Linear Transformations to One Dimension
To understand this connection, it's necessary to consider [[linear_transformations | linear transformations]] that map multiple dimensions to one dimension, specifically the number line <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. These are functions that take a 2D vector as input and output a single number <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

Similar to higher-dimensional transformations, a visual property defines these [[linear_transformations | linear transformations]]: if a line of evenly spaced dots is transformed, a [[linear_transformations | linear transformation]] will keep those dots evenly spaced on the number line <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. If dots become unevenly spaced, the transformation is not linear <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

Such a [[linear_transformations | linear transformation]] is fully determined by where it maps the basis vectors, `i-hat` and `j-hat` <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Since the output space is the number line, `i-hat` and `j-hat` each land on a single number <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. When recording their landing spots as columns of a matrix, each column contains just one number, forming a 1x2 matrix <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

For example, if a [[linear_transformations | linear transformation]] maps `i-hat` to 1 and `j-hat` to -2 <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>, a vector like [4, 3] can be broken down as `4 * i-hat + 3 * j-hat` <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. Due to linearity, after transformation, the vector will land on `4 * (where i-hat lands) + 3 * (where j-hat lands)`, which is `4 * 1 + 3 * (-2) = 4 - 6 = -2` <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Numerically, this calculation is equivalent to [[matrix_multiplication_and_transformations | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

This operation of multiplying a 1x2 matrix by a vector closely resembles taking the dot product of two vectors <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. This suggests a direct association between 1x2 matrices and 2D vectors: one can "tip" the numerical representation of a vector on its side to get its associated matrix, or vice versa <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. This numerical similarity hints at a profound geometric connection between [[linear_transformations | linear transformations]] that map vectors to numbers and vectors themselves <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

### Projection as a Linear Transformation
Consider placing a copy of the number line diagonally in 2D space, with its zero point at the origin <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. Let `u-hat` be the 2D unit vector whose tip sits at the number 1 on this diagonal number line <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

By projecting 2D vectors straight onto this diagonal number line, a function is defined that maps 2D vectors to numbers <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. This function is indeed a [[linear_transformations | linear transformation]], as it preserves the even spacing of dots on a line <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. Although the number line is embedded in 2D space, the function's outputs are numbers, not 2D vectors <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

Since this projection is a [[linear_transformations | linear transformation]] from 2D vectors to numbers, it must be described by some 1x2 matrix <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. To find this matrix, one needs to determine where `i-hat` and `j-hat` land after projection <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

Through an elegant piece of [[symmetry_in_dot_products | symmetry]], because `i-hat` and `u-hat` are both unit vectors, projecting `i-hat` onto the line through `u-hat` is symmetric to projecting `u-hat` onto the x-axis <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. Projecting `u-hat` onto the x-axis simply means taking its x-coordinate <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Therefore, by symmetry, the number where `i-hat` lands when projected onto the diagonal number line is the x-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. Identical reasoning applies to `j-hat`: its landing spot is the y-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

This means the entries of the 1x2 matrix describing the projection transformation are precisely the coordinates of `u-hat` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Consequently, applying this projection transformation to any vector, which involves multiplying the matrix by the vector, is computationally identical to taking a dot product with `u-hat` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This explains why taking the dot product with a unit vector can be interpreted as projecting a vector onto the span of that unit vector and measuring its length <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

For non-unit vectors, if `u-hat` is scaled by a factor (e.g., 3), its components are also multiplied by 3 <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. The associated matrix will then map `i-hat` and `j-hat` to three times their original values <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. This means the new matrix can be interpreted as projecting any vector onto the number line copy and then multiplying the result by 3 <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. This is why the dot product with a non-unit vector involves first projecting onto that vector and then scaling the length of that projection by the length of the non-unit vector <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

In essence, any [[linear_transformations | linear transformation]] whose output space is the number line, regardless of how it's defined, has a unique vector `v` corresponding to it <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. Applying the transformation is equivalent to taking a dot product with that vector <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

## The Concept of Duality

This phenomenon is an example of duality, a concept that appears in many forms throughout mathematics and refers to surprising correspondences between two types of mathematical things <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. In the context of [[linear_transformations | linear transformations]] and dot products:
*   The dual of a vector is the [[linear_transformations | linear transformation]] it encodes <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   The dual of a [[linear_transformations | linear transformation]] from some space to one dimension is a specific vector in that space <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

## Conclusion

On the surface, the dot product is a valuable geometric tool for understanding projections and determining if vectors generally point in similar directions <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. However, at a deeper level, dotting two vectors together serves to translate one of them into the realm of transformations <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This is significant because, in mathematics, vectors can sometimes be more easily understood not merely as arrows in space but as the physical embodiment of a [[linear_transformations | linear transformation]] <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. A vector can be seen as conceptual shorthand for a specific transformation, simplifying the thought process from complex space manipulations to more intuitive arrows <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. This duality is a recurring theme in linear algebra.