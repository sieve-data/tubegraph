---
title: rank of a matrix
videoId: uQhTuRlWMxw
---

From: [[3blue1brown]] <br/> 

The concept of matrix rank is central to [[understanding_fullrank_matrices | understanding fullrank matrices]] and linear algebra, particularly when analyzing [[matrix_representation_of_transformations | linear transformations]] and systems of equations. This discussion focuses on the intuition behind these concepts rather than computational methods <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Linear Systems of Equations

Linear algebra provides a powerful framework for solving certain systems of equations <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. A linear system is characterized by equations where variables are only scaled by constants and then added together (no exponents, fancy functions, or variable multiplication) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. These systems can be organized with variables on the left, constants on the right, and common variables vertically aligned, using zero coefficients where necessary <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Such a system can be elegantly packaged into a single [[matrixvector_multiplication | matrix-vector multiplication]] equation <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>:

$A\mathbf{x} = \mathbf{v}$

Here:
*   $A$ is the matrix containing all constant coefficients <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   $\mathbf{x}$ is the vector holding all the variables <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   $\mathbf{v}$ is a different constant vector <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Geometric Interpretation of $A\mathbf{x} = \mathbf{v}$

The matrix $A$ corresponds to some [[matrix_representation_of_transformations | linear transformation]] <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Therefore, solving $A\mathbf{x} = \mathbf{v}$ means finding a vector $\mathbf{x}$ which, after applying the transformation associated with $A$, lands on the vector $\mathbf{v}$ <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This provides a geometric interpretation: you are looking for a vector that, when the space is squished and morphed by $A$, maps to $\mathbf{v}$ <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## [[inverse_matrices | Inverse Matrices]] ($A^{-1}$)

The approach to solving $A\mathbf{x} = \mathbf{v}$ depends on whether the transformation associated with $A$ squishes space into a lower dimension (e.g., a line or a point) or leaves it spanning its original full dimensions <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This corresponds to whether the determinant of $A$ is zero or non-zero <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Non-Zero Determinant Case

When the determinant of $A$ is non-zero, space is not squished into a zero-area/volume region <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. In this case, there will always be one and only one vector $\mathbf{x}$ that lands on $\mathbf{v}$ <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. This solution can be found by playing the transformation in reverse <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

This reverse transformation is called the **inverse of $A$**, denoted $A^{-1}$ <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. For example:
*   If $A$ is a counterclockwise rotation by 90 degrees, $A^{-1}$ is a clockwise rotation by 90 degrees <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   If $A$ is a rightward shear, $A^{-1}$ is a leftward shear <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

The defining property of $A^{-1}$ is that if you apply $A$ and then $A^{-1}$, you end up back where you started <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Algebraically, this is expressed through [[associative_property_of_matrix_multiplication | matrix multiplication]]: $A^{-1}A = I$, where $I$ is the identity matrix (the matrix corresponding to the "do nothing" transformation) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

To solve $A\mathbf{x} = \mathbf{v}$, you multiply both sides by $A^{-1}$: $\mathbf{x} = A^{-1}\mathbf{v}$ <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. Geometrically, this means playing the transformation in reverse and following $\mathbf{v}$ <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### Zero Determinant Case (No Inverse)

When the determinant is zero, the transformation squishes space into a smaller dimension <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. In this scenario, there is no inverse transformation, because it's impossible for a function to "unsquish" a line back into a plane (a function must have a single output for each input) <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. For example, a 3D transformation squishing space onto a plane, line, or point would have a determinant of zero <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

However, a solution might still exist even when there is no inverse <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. This happens if the vector $\mathbf{v}$ is lucky enough to lie within the "squished" space (e.g., on the line or plane that space collapses onto) <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## Column Space

To describe the output of a transformation more precisely than "squished space," we use the term **column space** <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. The column space of a matrix is the set of all possible outputs of the transformation associated with that matrix <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. It is the span of the columns of the matrix, as the columns indicate where the basis vectors land, and the span of these transformed basis vectors gives all possible outputs <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

The zero vector is always included in the column space because [[Matrix representations of linear transformations | linear transformations]] must keep the origin fixed <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

## Rank of a Matrix

The **rank** of a matrix is defined as the number of dimensions in its column space <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

*   If the output of a transformation is a line (one-dimensional), the transformation has a rank of one <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   If all vectors land on a two-dimensional plane, the transformation has a rank of two <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   For a 3D transformation, if its output fills all of 3D space, it has a rank of three <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

When the rank is as high as it can be (i.e., it equals the number of columns), the matrix is called **full rank** <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. For a square matrix, being full rank implies a non-zero determinant.

## Null Space (Kernel)

For a full rank transformation, the only vector that lands at the origin is the zero vector itself <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. However, for matrices that are not full rank and squish space to a smaller dimension, many vectors can land on zero <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

The **null space**, or **kernel**, of a matrix is the set of all vectors that land on the origin (the zero vector) after the transformation <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. In terms of linear systems, if $\mathbf{v}$ is the zero vector, the null space provides all possible solutions to the equation $A\mathbf{x} = \mathbf{0}$ <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

For example:
*   If a 2D transformation squishes space onto a line, there is a separate line of vectors that get squished onto the origin <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   If a 3D transformation squishes space onto a plane, there is a line of vectors that land on the origin <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   If a 3D transformation squishes all of space onto a line, then a whole plane of vectors lands on the origin <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

## Conclusion

Understanding [[Matrix representation of linear transformations | linear transformations]] provides a geometric perspective on solving linear systems of equations <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. When a transformation has an inverse, it can be used to solve the system directly <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. When an inverse does not exist, the concepts of **column space** and **null space** become crucial for determining if a solution even exists and for understanding the nature of all possible solutions <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. The **rank of a matrix** quantifies the dimensionality of the transformation's output, giving insight into how much space is squished.