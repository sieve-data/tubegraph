---
title: Matrix representation of transformations
videoId: kYB8IZa5AuE
---

From: [[3blue1brown]] <br/> 
The concept of a [[linear_transformations_and_matrices | linear transformation]] and its relationship to [[linear_transformations_and_matrices | matrices]] is fundamental to understanding linear algebra deeply <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This article focuses on how [[visualizing_linear_transformations | these transformations]] appear in two dimensions and their connection to [[matrix_vector_multiplication_and_transformations | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## What is a Transformation?
A "transformation" is essentially another term for a function <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. In the context of linear algebra, it refers to something that takes an input vector and produces an output vector <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. The term "transformation" is used to suggest a way of visualizing this input-output relationship through movement <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

To understand a transformation, one can imagine an input vector moving to its output vector <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. To visualize the entire transformation, every possible input vector is imagined moving to its corresponding output vector <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Instead of thinking of vectors as arrows, it's helpful to conceptualize them as single points—the tip of the vector <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This allows for the visualization of every point in space moving to another point <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. For two-dimensional transformations, using an infinite grid of points helps in grasping the overall shape of the transformation <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Keeping a copy of the original grid in the background can assist in tracking relative movement <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Linear Transformations
Linear algebra focuses on a specific type of transformation called a [[visualizing_linear_transformations | linear transformation]] <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Visually, a transformation is linear if it satisfies two properties <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>:
*   All lines remain lines (without curving) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   The origin remains fixed in place <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

[[visualizing_linear_transformations | Linear transformations]] maintain grid lines as parallel and evenly spaced <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## Representing Linear Transformations with Matrices
To describe [[linear_transformations_and_matrices | linear transformations]] numerically, especially for programming animations, one needs a formula to determine where a vector lands <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. It's only necessary to record where the two basis vectors (i-hat and j-hat) land <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

For any vector `v` with coordinates `x` and `y`, meaning `v = x * i-hat + y * j-hat` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, a linear transformation will transform `v` to `x` times where i-hat landed plus `y` times where j-hat landed <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. This means a vector's final position is the same linear combination of the transformed basis vectors as it was of the original basis vectors <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

A two-dimensional [[matrix_representation_of_linear_transformations | linear transformation]] is fully described by four numbers: the two coordinates for where i-hat lands and the two coordinates for where j-hat lands <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. These coordinates are typically packaged into a 2x2 matrix <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. The columns of this matrix represent the two special vectors where i-hat and j-hat land <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### [[matrix_vector_multiplication_and_transformations | Matrix-Vector Multiplication]]
If given a 2x2 matrix `M` that describes a [[matrix_representation_of_linear_transformations | linear transformation]] and a specific vector `v`, to find where `v` lands after the transformation, one multiplies the coordinates of `v` by the corresponding columns of `M` and then adds the results <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. This process is known as [[matrix_vector_multiplication_and_transformations | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

For a matrix with entries:
`[ A B ]`
`[ C D ]`

And a vector `[x y]`:
The transformed vector is `x` times `[A C]` plus `y` times `[B D]` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>, resulting in `[Ax + By, Cx + Dy]` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This [[matrix_vector_multiplication_and_transformations | multiplication]] method computes the appropriate linear combination of the transformed basis vectors <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

### Examples of [[matrix_representation_of_linear_transformations | Matrix Representation of Transformations]]
*   **90-degree counterclockwise rotation**:
    *   i-hat lands at (0, 1) <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
    *   j-hat lands at (-1, 0) <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
    *   Matrix:
        `[ 0 -1 ]`
        `[ 1  0 ]` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>
*   **Shear**:
    *   i-hat remains fixed at (1, 0) <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
    *   j-hat moves to (1, 1) <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
    *   Matrix:
        `[ 1 1 ]`
        `[ 0 1 ]` <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>

### Properties of Transformed Space
If the vectors where i-hat and j-hat land are linearly dependent (one is a scaled version of the other), the [[matrix_representation_of_linear_transformations | linear transformation]] will squash all of 2D space onto the line where those two vectors reside <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This is also known as the one-dimensional span of those linearly dependent vectors <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

## Conclusion
[[linear_transformations_and_matrices | Linear transformations]] provide a method for moving space such that grid lines stay parallel and evenly spaced, and the origin remains fixed <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. These transformations can be described using a small set of numbers: the coordinates of where each basis vector lands <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. [[linear_transformations_and_matrices | Matrices]] serve as a language to represent these transformations, with their columns indicating the transformed basis vectors <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. [[matrix_vector_multiplication_and_transformations | Matrix-vector multiplication]] is the computational process of determining how a transformation affects a given vector <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

Every time a matrix is encountered, it can be interpreted as a specific transformation of space <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This understanding is key to deeply comprehending linear algebra concepts such as [[matrix_multiplication_and_transformations | matrix multiplication]], determinants, change of basis, and eigenvalues <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.