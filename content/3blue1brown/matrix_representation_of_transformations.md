---
title: matrix representation of transformations
videoId: XkY2DOUCWMU
---

From: [[3blue1brown]] <br/> 

[[matrix_representations_of_linear_transformations | Linear transformations]] are functions that take vectors as inputs and produce vectors as outputs <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Visually, they "smoosh around space" in a way that keeps grid lines parallel and evenly spaced, and the origin remains fixed <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Key Principle: Basis Vectors
A [[matrix_representation_of_linear_transformations | linear transformation]] is entirely defined by where it maps the basis vectors of the space <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. In two dimensions, these are commonly `i-hat` and `j-hat` <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

This is because any other vector can be expressed as a [[linear_combination_of_basis_vectors | linear combination]] of these basis vectors <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, a vector with coordinates (x, y) is equivalent to `x * i-hat + y * j-hat` <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. After a [[matrix_representations_and_transformations | linear transformation]], the vector will land at `x` times the transformed `i-hat` plus `y` times the transformed `j-hat` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Constructing the Matrix
To represent a [[matrix_representation_of_linear_transformations | linear transformation]] with a [[mathematical_representation_with_3x3_matrices | matrix]], the coordinates where `i-hat` and `j-hat` land after the transformation are recorded as the columns of the matrix <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. [[matrix_vector_multiplication | Matrix-vector multiplication]] is then defined as the sum of the scaled versions of these columns, thereby computationally applying the transformation to a vector <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Composition of Transformations
Often, it is necessary to describe the effect of applying one [[matrix_representations_and_transformations | transformation]] and then another <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. For instance, rotating a plane 90 degrees counterclockwise and then applying a shear <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. The combined effect is a new [[matrix_representations_of_linear_transformations | linear transformation]] called the [[composition_of_transformations | composition of the two transformations]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Representing Compositions with Matrices
Like any [[threedimensional_linear_transformations | linear transformation]], a [[composition_of_transformations | composite transformation]] can be described by its own unique [[mathematical_representation_with_3x3_matrices | matrix]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This is done by tracking the ultimate landing spots of `i-hat` and `j-hat` after *both* transformations have been applied <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

For example, if `i-hat` ultimately lands at (1,1) and `j-hat` at (-1,0) after a rotation followed by a shear, the [[matrix_for_composite_transformation | composition matrix]] would have (1,1) as its first column and (-1,0) as its second column <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This new matrix encapsulates the overall effect as a single action <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Matrix Multiplication
The new matrix that represents the [[composition_of_transformations | composite transformation]] is called the product of the original two matrices <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
When applying two transformations sequentially to a vector:
1.  Multiply the vector by the [[matrix_representing_transformation | matrix representing]] the *first* transformation (on the right).
2.  Multiply the resulting vector by the [[matrix_representing_transformation | matrix representing]] the *second* transformation (on the left) <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
This sequence is equivalent to multiplying the original vector by the single [[matrix_for_composite_transformation | composition matrix]] <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

Geometrically, multiplying two matrices signifies applying one transformation and then another <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. It's important to note that the order of multiplication is read from right to left; the transformation represented by the matrix on the right is applied first <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This convention stems from [[function_notation | function notation]] <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

To computationally find the columns of a [[matrix_for_composite_transformation | composition matrix]]:
1.  **First column:** Take the first column of the right matrix (where `i-hat` initially lands), and then multiply it by the left matrix to find its final destination <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
2.  **Second column:** Similarly, take the second column of the right matrix (where `j-hat` initially lands), and multiply it by the left matrix to find its final destination <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### Properties of Matrix Multiplication
*   **Order Matters (Non-commutative):** The order in which matrices are multiplied is crucial, as changing the order typically results in a different [[matrix_for_composite_transformation | composite transformation]] <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Associativity:** [[matrix_multiplication_associativity | Matrix multiplication is associative]], meaning that for matrices A, B, and C, (A * B) * C = A * (B * C) <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This is intuitively true because applying transformations C, then B, then A in sequence is the same regardless of how the intermediate compositions are grouped <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

Thinking about [[matrix_multiplication_as_transformation_composition | matrix multiplication as applying one transformation after another]] provides a robust conceptual framework for understanding its properties <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

## Beyond Two Dimensions
These concepts of [[vector_representation_and_coordinate_systems | vector representation]], [[visualization_of_3d_vector_transformations | visualizing transformations with vectors]], and [[embedding_matrices_and_vector_representations | embedding matrices]] can be extended to three dimensions and beyond <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.