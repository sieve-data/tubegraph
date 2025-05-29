---
title: geometric interpretation of linear systems
videoId: uQhTuRlWMxw
---

From: [[3blue1brown]] <br/> 

The bulk of understanding matrix and vector operations can be approached through the [[linear_transformations_in_linear_algebra | visual lens of linear transformations]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This perspective is particularly useful for understanding concepts such as inverse matrices, column space, rank, and null space <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. While computational methods like Gaussian elimination and row echelon form are important, the primary value of this approach lies in building intuition <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Usefulness of Linear Algebra

Linear algebra is broadly applicable and required in nearly any technical discipline because it allows for the solution of certain systems of equations <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. It is also useful in describing the manipulation of space, which is applied in fields like computer graphics and robotics <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Linear Systems of Equations

A system of equations involves a list of unknown variables and a list of equations relating them <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. If these equations take a specific form where each variable is only scaled by a constant and these scaled variables are only added together (without exponents, fancy functions, or variable multiplication), they form a "linear system of equations" <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

Such systems are typically organized with all variables on the left side and constants on the right, vertically aligning common variables (inserting zero coefficients if needed) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This arrangement closely resembles matrix-vector multiplication <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

The entire system can be packaged into a single vector equation:
`A` **x** = **v** <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>
where:
*   `A` is a matrix containing all constant coefficients <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **x** is a bold-faced vector containing all variables <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **v** is a constant vector on the right-hand side <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Geometric Interpretation of `A`x = **v**

This algebraic representation sheds light on a powerful [[geometric_versus_numeric_understanding_in_linear_algebra | geometric interpretation]] <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. The matrix `A` corresponds to a [[linear_transformations_in_linear_algebra | linear transformation]] <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Therefore, solving `A`**x** = **v** means finding a vector **x** that, after the transformation `A` is applied, lands on the vector **v** <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This allows for thinking about complicated systems of intermingling variables as the squishing and morphing of space <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### Case 1: Non-Zero Determinant (Inverse Transformation Exists)

For systems where the number of equations equals the number of unknowns (e.g., a 2x2 matrix `A` with two-dimensional vectors **v** and **x**) <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, the approach depends on whether the transformation `A` squishes space into a lower dimension (like a line or a point) or if it retains the full dimensions <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

The most common scenario is when the determinant of `A` is non-zero, meaning space does not get squished <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. In this case, there will always be **one and only one** vector that lands on **v** <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. This solution can be found by "playing the transformation in reverse" <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

*   **Inverse Matrix (`A`⁻¹)**: The transformation that reverses `A` is called the inverse of `A`, denoted `A`⁻¹ <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. For example, if `A` is a 90-degree counterclockwise rotation, `A`⁻¹ is a 90-degree clockwise rotation <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. The core property of `A`⁻¹ is that applying `A` and then `A`⁻¹ results in the "identity transformation" (doing nothing), represented by the identity matrix (I) <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Algebraically, `A`⁻¹ `A` = I <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

To solve `A`**x** = **v** in this case, one multiplies the inverse matrix by **v**: **x** = `A`⁻¹**v** <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. Geometrically, this means following **v** as the transformation is played in reverse <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. This scenario signifies a unique solution when the number of equations equals the number of unknowns <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### Case 2: Zero Determinant (No Inverse)

When the determinant of `A` is zero, the transformation `A` squishes space into a smaller dimension (e.g., a plane to a line, or 3D space to a plane) <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. In such cases, there is no inverse transformation <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, because it's impossible to "unsquish" a lower-dimensional space back into a higher dimension with a function <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

However, a solution might still exist if the vector **v** happens to lie within the reduced dimension that `A` squishes space into <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

*   **Column Space**: The set of all possible outputs for a matrix (the line, plane, or 3D space that space is squished into) is called the **column space** of the matrix <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. This name comes from the fact that the columns of the matrix show where the basis vectors land, and the span of these transformed basis vectors gives all possible outputs <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Rank**: The **rank** of a transformation is defined as the number of dimensions in its output, or more precisely, the number of dimensions in the column space <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
    *   If a 2D transformation squishes space onto a line, its rank is one <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   If a 2D transformation's output fills all two dimensions, its rank is two <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
    *   A matrix is considered **full rank** if its rank equals the number of its columns <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### Null Space (Kernel)

The zero vector is always included in the column space because linear transformations fix the origin <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   For a full-rank transformation, only the zero vector itself maps to the origin <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   However, for matrices that are not full rank (i.e., they squish space to a smaller dimension), a whole set of vectors can land on the origin <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
    *   If a 2D transformation maps space to a line, a separate line of vectors maps to the origin <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
    *   If a 3D transformation maps space to a plane, a line of vectors maps to the origin <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
    *   If a 3D transformation maps space to a line, a whole plane of vectors maps to the origin <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

This set of vectors that lands on the origin is called the **null space** or **kernel** of the matrix <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. It represents all vectors that become "null" (land on the zero vector) <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. In the context of a linear system, if **v** is the zero vector, the null space provides all possible solutions to the equation <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

### Conclusion

Understanding linear systems geometrically involves associating each system with a [[linear_transformations_in_linear_algebra | linear transformation]] <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. If this transformation has an inverse, it can be used to solve the system <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. If not, the concepts of [[column_space | column space]] help determine if a solution exists, and the [[null_space | null space]] helps understand the nature of all possible solutions <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

> [!NOTE] Limitations
> This overview focuses on the geometric intuition rather than computational methods (e.g., Gaussian elimination) or the detailed analysis of [[nonsquare_matrices_and_their_geometric_interpretation | non-square matrices]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a> <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.