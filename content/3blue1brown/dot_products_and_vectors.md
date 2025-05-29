---
title: Dot products and vectors
videoId: LyGKycYT2v0
---

From: [[3blue1brown]] <br/> 

Dot products are a fundamental concept in linear algebra, often introduced early in a course <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While a basic [[understanding_vectors | understanding of vectors]] is sufficient for an initial grasp, a deeper understanding of dot products emerges when viewed through the lens of [[visualizing_transformations_with_vectors | linear transformations]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Numerical Definition
Numerically, the dot product of two vectors of the same dimension (lists of numbers with the same length) is calculated by:
1.  Pairing up all corresponding coordinates <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
2.  Multiplying those pairs together <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
3.  Adding the results <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

**Examples:**
*   The dot product of vector (1, 2) and (3, 4) is (1 * 3) + (2 * 4) = 3 + 8 = 11 <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   The dot product of vector (6, 2, 8, 3) and (1, 8, 5, 3) is (6 * 1) + (2 * 8) + (8 * 5) + (3 * 3) = 6 + 16 + 40 + 9 = 71 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Geometric Interpretation
The numerical calculation of the dot product has a distinct [[geometric_interpretation_of_dot_products | geometric interpretation]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

To understand the dot product between two vectors, `v` and `w`:
1.  Imagine projecting `w` onto the line that passes through the origin and the tip of `v` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  Multiply the length of this projection by the length of `v` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This product is `v` dot `w` <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Directional Significance
The sign of the dot product indicates the general direction of the vectors:
*   If the projection of `w` is pointing in the opposite direction from `v`, the dot product is negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   When two vectors generally point in the same direction, their dot product is positive <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   When two vectors are perpendicular, meaning the projection of one onto the other is the zero vector, their dot product is zero <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   If they point in generally the opposite direction, their dot product is negative <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Order Invariance
Despite this seemingly asymmetric [[geometric_interpretation_of_dot_products | geometric interpretation]], the order of vectors in a dot product does not matter <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Projecting `v` onto `w` and multiplying by the length of `w` yields the same result as projecting `w` onto `v` and multiplying by the length of `v` <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

This symmetry can be intuited:
*   If `v` and `w` have the same length, the processes of projecting `w` onto `v` and `v` onto `w` are mirror images, resulting in the same dot product <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   If one vector, say `v`, is scaled by a constant (e.g., 2v), the dot product `2v` dot `w` will be twice `v` dot `w` <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This holds true regardless of which vector is considered for projection:
    *   Projecting `w` onto `2v`: The length of `w`'s projection doesn't change, but the length of the vector `2v` is doubled <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   Projecting `2v` onto `w`: The length of `2v`'s projection is scaled by 2, while the length of `w` remains constant <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    In both cases, the overall dot product is doubled <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Duality: Connecting Numerical Computation and Geometric Projection
A deeper understanding of why the numerical dot product calculation relates to geometric projection involves the concept of [[transformations_involving_dot_product | linear transformations]] from multiple dimensions to a single dimension (the number line) <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Linear Transformations to the Number Line
These are functions that take a 2D vector as input and output a single number <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Like other [[visualizing_transformations_with_vectors | linear transformations]], they maintain even spacing of dots on a line when mapped to the output space (the number line) <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

A linear transformation is completely determined by where it takes the [[unit_vectors_and_basis_vectors | basis vectors]] `i-hat` and `j-hat` <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Since the output space is a single number, the landing spots of `i-hat` and `j-hat` are recorded as single numbers, forming the columns of a 1x2 matrix <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

**Example:**
If a [[transformations_involving_dot_product | linear transformation]] maps `i-hat` to 1 and `j-hat` to -2 <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>, then for a vector (4, 3):
*   It's expressed as 4 times `i-hat` plus 3 times `j-hat` <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   After transformation, it lands at (4 * 1) + (3 * -2) = 4 - 6 = -2 <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
This calculation is identical to matrix-vector multiplication <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

### The Connection: Duality
The numerical operation of multiplying a 1x2 matrix by a vector strongly resembles taking the dot product <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. This suggests an association between 1x2 matrices and 2D [[vector_representation_and_coordinate_systems | vectors]] by simply "tipping" one on its side to get the other <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This seemingly simple numerical correspondence hints at a profound [[geometric_interpretation_of_dot_products | geometric connection]]:

Consider a linear transformation defined by projecting 2D vectors onto a diagonal copy of the number line embedded in 2D space, with 0 at the origin <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. Let `u-hat` be the [[unit_vectors_and_basis_vectors | unit vector]] in 2D space whose tip is at the number 1 on this diagonal number line <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This projection defines a [[transformations_involving_dot_product | linear transformation]] from 2D vectors to numbers <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

To find the 1x2 matrix describing this projection:
*   Projecting `i-hat` onto the line passing through `u-hat` is symmetric to projecting `u-hat` onto the x-axis <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Projecting `u-hat` onto the x-axis simply means taking its x-coordinate <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   Therefore, the number where `i-hat` lands when projected onto the diagonal number line is the x-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   Similarly, the number where `j-hat` lands is the y-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

Thus, the entries of the 1x2 matrix describing this projection transformation are the coordinates of `u-hat` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Calculating this projection transformation for any vector involves multiplying that matrix by the vector, which is computationally identical to taking a dot product with `u-hat` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This explains why dotting with a [[unit_vectors_and_basis_vectors | unit vector]] can be interpreted as projecting a vector onto that unit vector's span and taking the length <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

For non-unit vectors, if `u-hat` is scaled by a factor (e.g., 3), its components are also scaled by 3 <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. The associated matrix will take `i-hat` and `j-hat` to three times their previous values <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. This means the new matrix projects any vector onto the number line and then multiplies the result by 3 <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. This explains why the dot product with a non-unit vector is interpreted as first projecting onto that vector, then scaling the length of that projection by the length of the vector <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

This revelation highlights a concept called **duality** <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Duality describes a natural, often surprising, correspondence between two types of mathematical objects <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. In this case, the dual of a vector is the [[transformations_involving_dot_product | linear transformation]] it encodes, and the dual of a [[transformations_involving_dot_product | linear transformation]] from a space to one dimension is a specific vector in that space <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

## Conclusion
On the surface, the dot product is a valuable [[geometric_interpretation_of_dot_products | geometric tool]] for understanding projections and determining if vectors point in similar directions <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. More profoundly, dotting two vectors together serves as a method to translate one of them into the realm of [[visualizing_transformations_with_vectors | transformations]] <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This signifies that a [[definition_and_nature_of_vectors | vector]] can sometimes be best understood not just as an arrow, but as the physical embodiment of a linear transformation <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. Vectors, in this sense, act as a conceptual shorthand for certain transformations <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.