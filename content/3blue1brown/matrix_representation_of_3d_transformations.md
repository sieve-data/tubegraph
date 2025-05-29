---
title: Matrix representation of 3D transformations
videoId: rHLEWRxRGiM
---

From: [[3blue1brown]] <br/> 

While many core ideas of [[linear_transformations | linear transformations]] are often introduced in two dimensions for ease of [[visualizing_linear_transformations_with_matrices | visualization]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, these concepts carry over seamlessly to [[higher_dimensions | higher dimensions]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. [[Threedimensional linear transformations | Three-dimensional linear transformations]] involve [[three-dimensional vectors | three-dimensional vectors]] as both inputs and outputs <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Visualizing 3D Transformations

A [[visualizing_transformations_in_three_dimensions | linear transformation]] in three dimensions can be visualized as "smooshing around" all points in three-dimensional space <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This transformation maintains certain properties:
*   Grid lines remain parallel and evenly spaced <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   The origin remains fixed in place <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

Each moving point in this visualization represents the tip of a vector, showing how input vectors move to their corresponding output vectors <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Describing 3D Transformations with Basis Vectors

Similar to two dimensions, a [[matrix_representation_of_transformations | linear transformation]] in three dimensions is completely described by where the basis vectors land after the transformation <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. In three dimensions, there are three standard basis vectors:
*   **i-hat**: The unit vector in the x-direction <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **j-hat**: The unit vector in the y-direction <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **k-hat**: The unit vector in the z-direction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

It can be easier to understand these [[matrix_representation_of_linear_transformations | transformations]] by focusing solely on the movement of these basis vectors, as a full 3D grid can be complex to visualize <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. By observing the coordinates where each of these three basis vectors lands, relative to the original axes <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>, one can completely describe the transformation.

## Constructing the 3x3 Matrix

The coordinates of the transformed basis vectors form the columns of a [[matrix_representation_of_transformations | 3x3 matrix]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This matrix, containing only nine numbers, fully describes the transformation <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Example: Rotation Around the Y-axis

Consider a transformation that rotates space 90 degrees around the y-axis <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:
*   i-hat moves to the coordinates (0, 0, -1) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   j-hat remains at (0, 1, 0) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   k-hat moves to the coordinates (1, 0, 0) <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

These three sets of coordinates become the columns of the [[matrix_representation_of_transformations | matrix]] describing this rotation transformation <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Applying Transformations to Vectors

To find where a vector with coordinates (x, y, z) lands after a transformation, the process is almost identical to two dimensions <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. The coordinates (x, y, z) indicate how to scale each basis vector so they add up to the original vector <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This scaling and adding process remains valid both before and after the transformation <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

Therefore, to find the transformed vector, you [[matrix_vector_multiplication_and_transformations | multiply those coordinates]] by the corresponding columns of the [[matrix_representation_of_transformations | matrix]], and then add the three results together <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Composing 3D Transformations with Matrix Multiplication

[[Matrix multiplication and transformations | Multiplying two matrices]] in 3D is similar to the 2D case <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. When two [[matrix_representation_of_transformations | 3x3 matrices]] are multiplied, it represents applying the transformation encoded by the right matrix first, followed by the transformation encoded by the left matrix <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Numerically, this process is also similar to the two-dimensional case <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, representing the idea of applying two successive transformations in space <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

## Importance in Fields like Computer Graphics and Robotics

[[Matrix multiplication and transformations | 3D matrix multiplication]] is crucial in fields such as [[computer_graphics_and_robotics | computer graphics and robotics]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This is because complex operations like rotations in three dimensions, which can be difficult to describe directly, become more manageable when broken down into compositions of simpler, easier-to-understand rotations using matrices <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.