---
title: Properties of linear transformations
videoId: kYB8IZa5AuE
---

From: [[3blue1brown]] <br/> 

The concept of a [[linear_transformations | linear transformation]] is fundamental in linear algebra, often clarifying many other topics <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

## What is a Transformation?
A "transformation" is essentially a function that takes inputs and produces outputs <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. In linear algebra, this typically involves taking a vector as input and outputting another vector <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>. The term "transformation" is used to suggest a way of [[visualizing_linear_transformations | visualizing]] this input-output relationship, by imagining the input vector "moving over" to the output vector <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. To understand the transformation as a whole, one can imagine every point in space moving to some other point <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

## Visual Properties of Linear Transformations
While arbitrary transformations can be complex, [[linear_transformations | linear transformations]] are a special, simpler type of transformation <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. Visually, a transformation is considered [[linear_transformations | linear]] if it satisfies two key properties:
1.  **Lines Remain Lines**: All lines in the space must remain straight lines; they cannot become curved <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.
2.  **Origin Remains Fixed**: The origin (0,0) must stay in its original position <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

In general, [[linear_transformations | linear transformations]] are characterized by keeping grid lines parallel and evenly spaced <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.

### Examples of Non-Linear Transformations
*   A transformation that causes lines to curve <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   A transformation that shifts the origin <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   A transformation that keeps horizontal/vertical lines straight but curves diagonal lines, demonstrating that not all lines remain straight <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

## Numerical Description of Linear Transformations
A two-dimensional [[linear_transformations | linear transformation]] can be completely described by just four numbers <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>. These numbers are the coordinates of where the two standard basis vectors, i-hat and j-hat, land after the transformation <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

The property that grid lines remain parallel and evenly spaced has a significant consequence: any vector, which starts as a linear combination of the basis vectors, will end up as the *same* linear combination of where those basis vectors landed <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.

For a vector **v** represented by `x * i-hat + y * j-hat`:
*   If i-hat lands at `(a, c)` and j-hat lands at `(b, d)` <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.
*   Then **v** will land at `x * (a, c) + y * (b, d)` <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.
*   This sum results in the vector `(ax + by, cx + dy)` <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

## Relationship with Matrices
These four coordinates that describe a [[linear_transformations | linear transformation]] are typically packaged into a 2x2 grid of numbers called a [[matrix_representation_of_linear_transformations | matrix]] <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>.
*   The first column of the [[matrix_representation_of_linear_transformations | matrix]] represents where i-hat lands <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.
*   The second column of the [[matrix_representation_of_linear_transformations | matrix]] represents where j-hat lands <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.

### Matrix-Vector Multiplication
When a [[matrix_representation_of_linear_transformations | matrix]] `[[A, B], [C, D]]` is multiplied by a vector `[x, y]`, the result is the transformed vector `[Ax + By, Cx + Dy]` <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>. This operation of [[visualizing_linear_transformations_with_matrices | matrix-vector multiplication]] is a direct computation of where the [[linear_transformations | linear transformation]] takes a given vector <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>. It reflects the idea of taking a linear combination of the transformed basis vectors <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.

> [!INFO] Interpreting a Matrix
> Every time you encounter a [[matrix_representation_of_linear_transformations | matrix]], you can interpret it as a specific [[linear_transformations | transformation]] of space <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>.

### Examples
*   **Rotation**: A 90-degree counter-clockwise rotation transforms i-hat to `(0, 1)` and j-hat to `(-1, 0)`. The corresponding [[matrix_representation_of_linear_transformations | matrix]] is `[[0, -1], [1, 0]]` <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.
*   **Shear**: In a shear transformation, i-hat remains fixed at `(1, 0)`, and j-hat moves to `(1, 1)`. The [[matrix_representation_of_linear_transformations | matrix]] is `[[1, 1], [0, 1]]` <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.

### Special Case: Linearly Dependent Basis Vectors
If the vectors that i-hat and j-hat land on are [[linear_transformations_and_matrices | linearly dependent]] (meaning one is a scaled version of the other), the [[linear_transformations | linear transformation]] will squish all of 2D space onto a single line, which is the one-dimensional span of those two vectors <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.

Understanding [[linear_transformations | linear transformations]] and their [[matrix_representation_of_linear_transformations | matrix representation]] is crucial for grasping other topics in linear algebra, such as [[composition_of_linear_transformations | matrix multiplication]], determinants, change of basis, and eigenvalues <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.