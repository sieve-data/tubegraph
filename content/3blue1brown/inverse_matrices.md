---
title: inverse matrices
videoId: uQhTuRlWMxw
---

From: [[3blue1brown]] <br/> 

This article explores the concept of [[inverse_matrix_and_translating_between_coordinate_systems | inverse matrices]] and related concepts, primarily through the visual lens of [[linear_transformations | linear transformations]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The focus is on intuition rather than computational methods <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Linear Algebra and Systems of Equations

[[linear_transformations | Linear algebra]] is broadly applicable because it allows for the solution of certain systems of equations <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. A system of equations involves a list of unknown variables and equations relating them <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

A special form of these systems is when, within each equation, variables are only scaled by constants and then added together, without exponents, fancy functions, or multiplication of variables <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Such systems are organized by placing all variables on the left and constants on the right, vertically aligning common variables (using zero coefficients if necessary) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This is known as a **linear system of equations** <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Geometric Interpretation of Solving Ax = V

A linear system of equations can be packaged into a single vector equation: `Ax = V` <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Here:
*   `A` is a constant [[matrix_representations_and_transformations | matrix]] containing all the constant coefficients <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   `X` is a vector containing all the variables <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   `V` is a constant vector on the right-hand side <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

This [[matrixvector_multiplication | matrix-vector multiplication]] perspective offers a geometric interpretation: the [[matrix_representation_of_transformations | matrix A]] corresponds to a [[linear_transformations | linear transformation]] <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Solving `Ax = V` means finding a vector `X` that, after applying the transformation `A`, lands on vector `V` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This allows for a visual understanding of complex multivariable interactions as morphing space <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

For a system with two equations and two unknowns, `A` is a 2x2 [[matrix_representations_of_linear_transformations | matrix]], and `V` and `X` are two-dimensional vectors <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. The nature of the solutions depends on whether the transformation `A` squishes space into a lower dimension (e.g., a line or point) or preserves its full dimensionality <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This distinction is captured by the determinant of `A` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## The Inverse Matrix (Determinant Non-Zero)

If the determinant of `A` is non-zero, space is not squished into a zero-area region <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. In this case, there will always be *one and only one* vector `X` that lands on `V` <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. This vector `X` can be found by "playing the transformation in reverse" <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

This reverse transformation corresponds to a separate [[linear_transformations | linear transformation]] called the **inverse of A**, denoted `A⁻¹` <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   If `A` is a 90-degree counterclockwise rotation, `A⁻¹` is a 90-degree clockwise rotation <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   If `A` is a rightward shear pushing j-hat one unit right, `A⁻¹` is a leftward shear pushing j-hat one unit left <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

The defining property of `A⁻¹` is that if you apply `A` and then `A⁻¹`, you end up back where you started <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Algebraically, this means that `A⁻¹ * A` equals the [[matrix_representations_and_transformations | matrix]] corresponding to "doing nothing" <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### The Identity Transformation

The transformation that "does nothing" is called the **identity transformation** <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. It leaves basis vectors (like i-hat and j-hat) unmoved <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. For a 2D space, its columns are `(1,0)` and `(0,1)` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

Therefore, the core property of the [[inverse_matrix_and_translating_between_coordinate_systems | inverse matrix]] `A⁻¹` is that `A⁻¹ * A = I`, where `I` is the identity matrix <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### Solving Ax = V with the Inverse Matrix

Once `A⁻¹` is found (typically via computer) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, the equation `Ax = V` can be solved by multiplying `A⁻¹` by `V`: `X = A⁻¹V` <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. Geometrically, this means playing the transformation in reverse and following `V` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

This case (non-zero determinant) is the most common for a randomly chosen [[matrix_representations_of_linear_transformations | matrix]] and implies a single, unique solution when the number of equations equals the number of unknowns <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This principle extends to higher dimensions as long as the transformation `A` does not squish space into a lower dimension <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

## When There is No Inverse (Determinant is Zero)

When the determinant of `A` is zero, the transformation squishes space into a smaller dimension, and there is no [[inverse_matrix_and_translating_between_coordinate_systems | inverse matrix]] <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. It's impossible to "unsquish" a line back into a plane using a function, as functions must map a single input to a single output <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

For three equations and three unknowns, there is no inverse if the transformation squishes 3D space onto a plane, line, or point <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. These all correspond to a determinant of zero because any region is squished into something with zero volume <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

Even without an inverse, a solution might still exist if the target vector `V` happens to lie within the squished space <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

### Column Space and Rank

To describe the degree of squishing, specific language beyond "zero determinant" is used <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   If the output of a transformation is a line (one-dimensional), the transformation has a **rank of one** <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   If all vectors land on a two-dimensional plane, the transformation has a **rank of two** <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Rank** is defined as the number of dimensions in the output of a transformation <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

For 2x2 matrices, rank two is the maximum, meaning basis vectors span the full two dimensions and the determinant is non-zero <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. For 3x3 matrices, rank two indicates collapse, but less so than rank one <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. If a 3D transformation has a non-zero determinant and fills all 3D space, it has a rank of three <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

The set of all possible outputs for a [[matrix_representations_of_linear_transformations | matrix]] (line, plane, 3D space, etc.) is called the **column space** of the matrix <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. This is because the columns of the [[matrix_representation_of_transformations | matrix]] show where the basis vectors land, and the span of these transformed basis vectors gives all possible outputs <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. More precisely, rank is the number of dimensions in the column space <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. A matrix is **full rank** if its rank equals the number of its columns <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

The zero vector is always in the column space because [[linear_transformations | linear transformations]] keep the origin fixed <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

### Null Space (Kernel)

For a full rank transformation, only the zero vector itself lands at the origin <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. However, for matrices that are not full rank and squish space to a smaller dimension, many vectors can land on zero <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   If a 2D transformation squishes space onto a line, another line of vectors in a different direction gets squished onto the origin <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   If a 3D transformation squishes space onto a plane, a full line of vectors lands on the origin <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   If a 3D transformation squishes space onto a line, a whole plane of vectors lands on the origin <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

This set of vectors that lands on the origin is called the **null space** or **kernel** of the [[matrix_representations_of_linear_transformations | matrix]] <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. It's the space of all vectors that become "null" by landing on the zero vector <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. When `V` is the zero vector, the null space provides all possible solutions to the equation `Ax = 0` <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## Conclusion

Understanding linear systems of equations geometrically involves associating each system with a [[linear_transformations | linear transformation]] <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. When this transformation has an [[inverse_matrix_and_translating_between_coordinate_systems | inverse matrix]], it can be used to solve the system <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. Otherwise, the concepts of **column space** help determine if a solution exists, and **null space** helps understand the set of all possible solutions <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.