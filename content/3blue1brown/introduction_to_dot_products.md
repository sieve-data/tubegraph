---
title: Introduction to dot products
videoId: LyGKycYT2v0
---

From: [[3blue1brown]] <br/> 

Traditionally, [[Introduction to dot products | dot products]] are introduced early in a linear algebra course, often at the start <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This article will cover the standard introduction and then delve into a deeper understanding of their role, particularly in relation to linear transformations.

## Numerical Calculation of Dot Products

Numerically, for two [[understanding_vectors_in_linear_algebra | vectors]] of the same dimension (lists of numbers with the same length), their [[Introduction to dot products | dot product]] is found by:
1.  Pairing up all corresponding coordinates <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
2.  Multiplying those pairs together <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
3.  Adding the results <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### Examples:
*   The [[understanding_vectors_in_linear_algebra | vector]] `[1, 2]` dotted with `[3, 4]` equals `(1 * 3) + (2 * 4) = 3 + 8 = 11` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   The [[understanding_vectors_in_linear_algebra | vector]] `[6, 2, 8, 3]` dotted with `[1, 8, 5, 3]` equals `(6 * 1) + (2 * 8) + (8 * 5) + (3 * 3) = 6 + 16 + 40 + 9 = 71` <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Geometric Interpretation of Dot Products

The numerical calculation has a significant [[geometric_interpretation_of_dot_products | geometric interpretation]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. To understand the [[Introduction to dot products | dot product]] between two [[understanding_vectors_in_linear_algebra | vectors]], `v` and `w`:
1.  Imagine projecting [[understanding_vectors_in_linear_algebra | vector]] `w` onto the line that passes through the origin and the tip of [[understanding_vectors_in_linear_algebra | vector]] `v` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  Multiply the length of this projection by the length of `v` to get the [[Introduction to dot products | dot product]] `v ⋅ w` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Sign of the Dot Product:
*   If the projection of `w` is pointing in the opposite direction from `v`, the [[Introduction to dot products | dot product]] will be negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   When two [[understanding_vectors_in_linear_algebra | vectors]] generally point in the same direction, their [[Introduction to dot products | dot product]] is positive <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   When [[understanding_vectors_in_linear_algebra | vectors]] are perpendicular (meaning the projection of one onto the other is the zero [[understanding_vectors_in_linear_algebra | vector]]), their [[Introduction to dot products | dot product]] is zero <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   If they point in generally opposite directions, their [[Introduction to dot products | dot product]] is negative <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Symmetry in Dot Products

Despite the seemingly asymmetric nature of the projection process (projecting `w` onto `v`), the order of [[understanding_vectors_in_linear_algebra | vectors]] in a [[Introduction to dot products | dot product]] does not matter <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Projecting `v` onto `w` and multiplying its length by `w`'s length yields the same result as projecting `w` onto `v` <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

This [[symmetry_in_dot_products | symmetry]] can be intuited:
*   If `v` and `w` have the same length, projecting `w` onto `v` (then multiplying by `v`'s length) is a mirror image of projecting `v` onto `w` (then multiplying by `w`'s length) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   If one [[understanding_vectors_in_linear_algebra | vector]] (e.g., `v`) is scaled by a constant (e.g., 2), breaking the [[symmetry_in_dot_products | symmetry]], the effect on the [[Introduction to dot products | dot product]] remains consistent. Scaling `v` by 2 doubles the [[Introduction to dot products | dot product]] `2v ⋅ w`. This is because scaling `v` by 2 doubles the length of `v` (when `w` is projected onto `v`), or doubles the length of the projection of `v` (when `v` is projected onto `w`), while the other component (projection length or `w`'s length) remains constant <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. The overall effect on the dot product value is the same under both interpretations <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Dot Products and Linear Transformations

A deeper understanding of the [[meaningful_transformations_and_their_ties_to_the_dot_product | significance of the dot product]] involves its connection to [[linear_transofrmations_and_dot_products | linear transformations]] from multiple dimensions to a single dimension (the number line) <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Linear Transformations to the Number Line
These are functions that take a 2D [[understanding_vectors_in_linear_algebra | vector]] and output a single number <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. A visual property of [[linear_transofrmations_and_dot_products | linear transformations]] is that a line of evenly spaced dots will remain evenly spaced after the transformation onto the number line <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

Similar to higher-dimensional transformations, these are entirely determined by where they map the basis [[understanding_vectors_in_linear_algebra | vectors]] (i-hat and j-hat) <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. Since the output is a single number, when these landing spots are recorded as columns of a matrix, each column consists of a single number, forming a 1x2 matrix (for a 2D input) <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

For example, a [[linear_transofrmations_and_dot_products | linear transformation]] mapping i-hat to 1 and j-hat to -2, when applied to a [[understanding_vectors_in_linear_algebra | vector]] `[4, 3]`, results in `(4 * 1) + (3 * -2) = -2` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. This calculation is numerically identical to matrix-vector multiplication <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

### The Duality: Vector-Transformation Correspondence
The numerical resemblance between multiplying a 1x2 matrix by a [[understanding_vectors_in_linear_algebra | vector]] and taking a [[Introduction to dot products | dot product]] suggests a connection between 1x2 matrices (representing [[linear_transofrmations_and_dot_products | linear transformations]] to numbers) and 2D [[understanding_vectors_in_linear_algebra | vectors]] (by "tipping" the matrix on its side) <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. This implies a deeper link between [[linear_transofrmations_and_dot_products | linear transformations]] that map [[understanding_vectors_in_linear_algebra | vectors]] to numbers and the [[understanding_vectors_in_linear_algebra | vectors]] themselves <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

Consider a diagonal copy of the number line in 2D space, with 0 at the origin <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. If 2D [[understanding_vectors_in_linear_algebra | vectors]] are projected onto this number line, this defines a [[linear_transofrmations_and_dot_products | linear transformation]] from 2D [[understanding_vectors_in_linear_algebra | vectors]] to numbers <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

Let `u-hat` be the 2D unit [[understanding_vectors_in_linear_algebra | vector]] whose tip sits at the number 1 on this diagonal number line <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. To find the 1x2 matrix describing this projection [[linear_transofrmations_and_dot_products | transformation]], we need to see where i-hat and j-hat land on this number line <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

*   By [[symmetry_in_dot_products | symmetry]], projecting i-hat onto the line passing through `u-hat` is equivalent to projecting `u-hat` onto the x-axis <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Projecting `u-hat` onto the x-axis simply means taking its x-coordinate <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Thus, i-hat lands on the x-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   Similarly, j-hat lands on the y-coordinate of `u-hat` <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

This means the entries of the 1x2 matrix describing the projection [[linear_transofrmations_and_dot_products | transformation]] are the coordinates of `u-hat` <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Applying this projection [[linear_transofrmations_and_dot_products | transformation]] (multiplying the matrix by a [[understanding_vectors_in_linear_algebra | vector]]) is computationally identical to taking a [[Introduction to dot products | dot product]] with `u-hat` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This explains why taking the [[Introduction to dot products | dot product]] with a unit [[understanding_vectors_in_linear_algebra | vector]] can be interpreted as projecting a [[understanding_vectors_in_linear_algebra | vector]] onto its span and taking the length <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

For non-unit [[understanding_vectors_in_linear_algebra | vectors]] (e.g., `3u-hat`), scaling the [[understanding_vectors_in_linear_algebra | vector]] numerically scales its components and thus scales the elements of the associated matrix <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. This means the corresponding [[linear_transofrmations_and_dot_products | transformation]] involves projecting the [[understanding_vectors_in_linear_algebra | vector]] onto the number line and then multiplying the result by 3 <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. This is why the [[Introduction to dot products | dot product]] with a non-unit [[understanding_vectors_in_linear_algebra | vector]] can be interpreted as first projecting onto that [[understanding_vectors_in_linear_algebra | vector]], then scaling the length of that projection by the length of the [[understanding_vectors_in_linear_algebra | vector]] <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

### Duality
The central idea here is "duality" <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Duality refers to surprising correspondences between two types of mathematical objects <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. In this context, any [[linear_transofrmations_and_dot_products | linear transformation]] whose output is the number line (1D space) corresponds to a unique [[understanding_vectors_in_linear_algebra | vector]] `v` such that applying the transformation is equivalent to taking a [[Introduction to dot products | dot product]] with `v` <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

The dual of a [[understanding_vectors_in_linear_algebra | vector]] is the [[linear_transofrmations_and_dot_products | linear transformation]] it encodes, and the dual of a [[linear_transofrmations_and_dot_products | linear transformation]] from some space to one dimension is a certain [[understanding_vectors_in_linear_algebra | vector]] in that space <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

## Conclusion
On the surface, the [[Introduction to dot products | dot product]] is a useful [[geometric_interpretation_of_dot_products | geometric tool]] for understanding projections and determining if [[understanding_vectors_in_linear_algebra | vectors]] point in similar directions <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. However, at a deeper level, dotting two [[understanding_vectors_in_linear_algebra | vectors]] together serves as a way to translate one of them into the realm of [[linear_transofrmations_and_dot_products | transformations]] <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Often, a [[understanding_vectors_in_linear_algebra | vector]] can be understood not merely as an arrow in space, but as the physical embodiment of a [[linear_transofrmations_and_dot_products | linear transformation]] to the number line <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

This concept of duality will be further explored in the context of the [[introduction_to_cross_products | cross product]] <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.