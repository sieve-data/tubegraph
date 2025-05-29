---
title: Visualization of 3D vector transformations
videoId: rHLEWRxRGiM
---

From: [[3blue1brown]] <br/> 

While two-dimensional vectors are often used for visual simplicity <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, the core concepts of linear transformations extend seamlessly to higher dimensions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This article focuses on [[threedimensional_linear_transformations | three-dimensional linear transformations]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Visualizing 3D Transformations

A [[threedimensional_linear_transformations | linear transformation]] involving three-dimensional vectors as both inputs and outputs can be visualized as "smooshing around" all points in three-dimensional space <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This transformation maintains grid lines parallel and evenly spaced and fixes the origin in place <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Every moving point represents the tip of a vector, illustrating how input vectors map to their corresponding outputs <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

For [[visualizing_transformations_with_vectors | visualizing transformations with vectors]], especially in 3D, it can be clearer to follow only the basis vectors, as the full 3D grid can become complex <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. By keeping a copy of the original axes in the background, one can observe the coordinates where each of the three basis vectors land <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Basis Vectors in 3D

Similar to two dimensions, a [[threedimensional_linear_transformations | 3D linear transformation]] is entirely defined by where its basis vectors move <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. In three dimensions, there are three standard basis vectors:
*   **i-hat**: The unit vector in the x-direction <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **j-hat**: The unit vector in the y-direction <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **k-hat**: The unit vector in the z-direction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Matrix Representation of 3D Transformations

The coordinates of where these three basis vectors land after a transformation are recorded as the columns of a 3x3 matrix <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This [[matrix_representations_of_linear_transformations | matrix representation of linear transformations]] fully describes the transformation using only nine numbers <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Example: 90-degree Rotation Around Y-axis

Consider a transformation that rotates space 90 degrees around the y-axis <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **i-hat** moves to coordinates (0, 0, -1) on the z-axis <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **j-hat** remains at (0, 1, 0) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **k-hat** moves to (1, 0, 0) on the x-axis <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

These three sets of coordinates form the columns of the matrix that describes this rotation <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Applying Transformations to Vectors

To determine where a vector with coordinates (x, y, z) lands after a [[threedimensional_linear_transformations | transformation]], the process is almost identical to two dimensions <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Each coordinate instructs how to scale each basis vector so they sum to the original vector <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This scaling and adding process remains consistent both before and after the transformation <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

Therefore, to find where a vector lands, its coordinates are multiplied by the corresponding columns of the [[matrix_representation_of_transformations | matrix representation of transformations]], and the three results are added together <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Matrix Multiplication in 3D

Multiplying two 3x3 [[matrix_representations_and_transformations | matrices representations and transformations]] is similar to the 2D case <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. It should be imagined as applying the transformation encoded by the right matrix first, followed by the transformation encoded by the left matrix <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

[[Matrix representation of linear transformations | 3D matrix multiplication]] is crucial in fields like computer graphics and robotics <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Complex 3D rotations, which can be difficult to describe directly, become more manageable when broken down into compositions of simpler rotations using matrix multiplication <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Numerically, this matrix multiplication is very similar to the two-dimensional case <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

The next topic to be explored is the determinant <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.