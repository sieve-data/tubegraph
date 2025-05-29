---
title: Mathematical representation with 3x3 matrices
videoId: rHLEWRxRGiM
---

From: [[3blue1brown]] <br/> 

While much of the discussion about [[matrix_representation_of_linear_transformations | linear transformations]] and [[matrix_representation_of_transformations | matrices]] often focuses on two-dimensional cases for ease of visualization, the core concepts extend seamlessly to higher dimensions <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This includes representing three-dimensional [[matrix_representation_of_linear_transformations | linear transformations]] using 3x3 [[matrix_representation_of_transformations | matrices]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Visualizing 3D Linear Transformations
A [[matrix_representation_of_linear_transformations | linear transformation]] involving three-dimensional vectors as both inputs and outputs can be visualized as a manipulation of all points in three-dimensional space <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This transformation maintains a grid's parallel and evenly spaced lines, while keeping the origin fixed <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>, <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Each moving point in this visualization represents the tip of a vector, showing how input vectors are mapped to their corresponding output vectors <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## The Role of Basis Vectors in 3D
Just as in two dimensions, a [[matrix_representation_of_linear_transformations | linear transformation]] in three dimensions is fully defined by where its basis vectors land <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. The standard basis vectors for three dimensions are:
*   **i-hat**: The unit vector in the x-direction <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **j-hat**: The unit vector in the y-direction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **k-hat**: The unit vector in the z-direction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

Tracking only these three basis vectors is often clearer than visualizing the entire 3D grid <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. By observing their landing coordinates relative to the original axes, one can deduce the entire transformation <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Constructing a 3x3 Matrix
The coordinates where the three basis vectors (i-hat, j-hat, and k-hat) land after a transformation form the columns of a 3x3 [[matrix_representation_of_transformations | matrix]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This 3x3 [[matrix_representation_of_transformations | matrix]] comprehensively describes the transformation using only nine numbers <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

> [!EXAMPLE] Rotation Around the Y-axis
> Consider a [[matrix_representation_of_linear_transformations | transformation]] that rotates space 90 degrees around the y-axis <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
> *   i-hat moves to the coordinates (0, 0, -1) on the z-axis <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
> *   j-hat remains at (0, 1, 0) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
> *   k-hat moves to the coordinates (1, 0, 0) on the x-axis <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
>
> These three sets of coordinates form the columns of the [[matrix_representation_of_transformations | matrix]] representing this rotation <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>:
> ```
> ⎡ 0  0  1 ⎤
> ⎢ 0  1  0 ⎥
> ⎣ -1 0  0 ⎦
> ```

## Applying 3x3 Matrices to Vectors
To determine where a vector with coordinates (x, y, z) lands after a [[matrix_representation_of_linear_transformations | transformation]], the process is very similar to the two-dimensional case <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>, <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
The coordinates (x, y, z) represent instructions for scaling each basis vector (i-hat, j-hat, k-hat) so they add up to the original vector <a class="yt-timestamp" data="00:02:56">[00:02:56]</a>. This scaling and addition property holds both before and after the [[matrix_representation_of_linear_transformations | transformation]] <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

Therefore, to find the transformed vector, you multiply the vector's coordinates by the corresponding columns of the [[matrix_representation_of_transformations | matrix]] and then add the three resulting vectors <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This is standard [[matrix_representations_and_transformations | matrix]]-vector multiplication.

## Multiplying 3x3 Matrices
[[matrix_representations_and_transformations | Multiplying two matrices]] in three dimensions is conceptually identical to the two-dimensional process <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>, <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. When two 3x3 [[matrix_representation_of_transformations | matrices]] are multiplied, it represents the composition of two [[matrix_representation_of_linear_transformations | transformations]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. The transformation encoded by the right [[matrix_representation_of_transformations | matrix]] is applied first, followed by the transformation encoded by the left [[matrix_representation_of_transformations | matrix]] <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Applications
3D [[matrix_representation_of_transformations | matrix]] multiplication is crucial in fields such as [[embedding_matrices_and_vector_representations | computer graphics]] and robotics <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Complex operations like rotations in three dimensions, which can be difficult to describe directly, become more manageable when broken down into simpler, sequential rotations represented by [[matrix_representation_of_transformations | matrices]] <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.