---
title: Two dimensional grid transformations
videoId: kYB8IZa5AuE
---

From: [[3blue1brown]] <br/> 

## Introduction to Transformations
A "transformation" is a term often used interchangeably with "function" in linear algebra. It describes something that takes inputs and produces an output for each one <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Specifically, in the context of linear algebra, transformations typically take an input vector and produce another vector as an output <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

The word "transformation" is used to suggest a visual way to understand this input-output relationship <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. If a transformation maps an input vector to an output vector, one can imagine the input vector "moving over" to the output vector <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. To grasp the transformation as a whole, one might imagine every possible input vector moving to its corresponding output vector <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

Instead of visualizing each vector as an arrow, a helpful trick is to conceptualize each vector as a single point—the point where its tip sits <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This allows for visualizing a transformation as every point in space moving to some other point <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. For two-dimensional transformations, it's illustrative to apply this concept to all points on an infinite grid <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Keeping a copy of the original grid in the background can help track relative movement <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This visualization evokes the feeling of space itself squishing and morphing <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Linear Transformations
While arbitrary transformations can be complex, [[linear_transformations_and_matrices | linear algebra]] focuses on a special type called [[linear_transformations_and_matrices | linear transformations]], which are easier to understand <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Visually, a transformation is considered linear if it satisfies two conditions <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>:
1.  All lines must remain straight lines without getting curved <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. For example, a transformation that curves lines is not linear <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  The origin (0,0) must remain fixed in place <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. A transformation that moves the origin is not linear, even if it keeps lines straight <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Generally, [[visualizing_linear_transformations | linear transformations]] maintain grid lines parallel and evenly spaced <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Describing Linear Transformations with Matrices
To describe [[visualizing_linear_transformations_with_matrices | linear transformations]] numerically, for instance, in programming, one needs a formula that takes vector coordinates and provides the coordinates of where that vector lands <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

Crucially, you only need to record where the two basis vectors, i-hat (unit vector in the x-direction) and j-hat (unit vector in the y-direction), land <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Everything else follows from this. If a vector `v` starts as a linear combination of i-hat and j-hat (e.g., `v = x * i-hat + y * j-hat`), then after a linear transformation, `v` will land at the same linear combination of where i-hat and j-hat landed <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This property stems from grid lines remaining parallel and evenly spaced <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

For example, if i-hat lands on coordinates (1, -2) and j-hat lands on (3, 0) <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>, a vector `v` with coordinates (-1, 2) (i.e., -1 * i-hat + 2 * j-hat) will land at:
(-1) * (1, -2) + (2) * (3, 0) = (-1, 2) + (6, 0) = (5, 2) <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

This provides a method to determine where any vector `(x, y)` lands, given only where i-hat and j-hat land <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>:
`(x, y)` lands at `x * (where i-hat lands) + y * (where j-hat lands)` <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
Using the example above, `(x, y)` lands at `x * (1, -2) + y * (3, 0) = (1x + 3y, -2x + 0y)` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

A two-dimensional [[linear_transformations_and_matrices | linear transformation]] is entirely defined by four numbers: the two coordinates for where i-hat lands and the two coordinates for where j-hat lands <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

### Matrices as a Language for Transformations
These four coordinates are typically packaged into a 2x2 grid of numbers called a **2x2 matrix** <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The columns of the matrix represent the transformed i-hat and j-hat vectors <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

For a 2x2 matrix describing a linear transformation and a specific vector, determining where the transformation takes the vector involves [[matrix_multiplication_and_transformations | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This is done by taking the coordinates of the vector, multiplying them by the corresponding columns of the matrix, and then adding the results <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. This process corresponds to adding the scaled versions of the new basis vectors <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

Given a matrix:
```
[ A  B ]
[ C  D ]
```
where the first column `[A, C]` represents where the first basis vector (i-hat) lands, and the second column `[B, D]` represents where the second basis vector (j-hat) lands <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. When applied to a vector `[x, y]`, the result is:
`x * [A, C] + y * [B, D] = [Ax + By, Cx + Dy]` <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
This is the definition of [[matrix_multiplication_and_transformations | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

The intuitive understanding is to view the matrix columns as the transformed basis vectors, and the result of the multiplication as the appropriate linear combination of those transformed vectors <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### Examples of Linear Transformations and their Matrices
*   **90-degree Counterclockwise Rotation**:
    *   i-hat lands on (0, 1) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
    *   j-hat lands on (-1, 0) <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
    *   Matrix:
        ```
        [ 0  -1 ]
        [ 1   0 ]
        ```
    To find what happens to any vector after this rotation, one multiplies its coordinates by this matrix <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Shear**:
    *   i-hat remains fixed, so it lands on (1, 0) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
    *   j-hat moves to (1, 1) <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
    *   Matrix:
        ```
        [ 1  1 ]
        [ 0  1 ]
        ```
    Applying this shear to a vector involves [[matrix_multiplication_and_transformations | multiplying this matrix]] by that vector <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

### Interpreting a Matrix Visually
To understand what a transformation described by a matrix looks like (e.g., matrix with columns (1, 2) and (3, 1)), one can visualize moving i-hat to (1, 2) and j-hat to (3, 1), while ensuring all other space moves in a way that keeps gridlines parallel and evenly spaced <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

If the vectors where i-hat and j-hat land are [[computing_determinants_for_2D_and_3D_transformations | linearly dependent]] (one is a scaled version of the other), the linear transformation will squish all of 2D space onto the line where those two vectors reside <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. This line is also known as the one-dimensional span of those two [[computing_determinants_for_2D_and_3D_transformations | linearly dependent]] vectors <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

## Conclusion
[[visualizing_linear_transformations | Linear transformations]] are a way to move space such that gridlines remain parallel and evenly spaced, and the origin stays fixed <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. These transformations can be described by a few numbers—specifically, the coordinates of where each basis vector lands <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. [[linear_transformations_and_matrices | Matrices]] provide a language for describing these transformations, with their columns representing the transformed basis vectors <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. [[matrix_multiplication_and_transformations | Matrix-vector multiplication]] is the computational method to determine how a transformation affects a given vector <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

A fundamental insight in [[linear_transformations_and_matrices | linear algebra]] is that every matrix can be interpreted as a specific transformation of space <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. Grasping this concept provides a deep understanding of many advanced topics, including [[matrix_multiplication_and_transformations | matrix multiplication]], [[computing_determinants_for_2D_and_3D_transformations | determinants]], change of basis, and eigenvalues <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.