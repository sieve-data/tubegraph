---
title: Threedimensional linear transformations
videoId: rHLEWRxRGiM
---

From: [[3blue1brown]] <br/> 

[[linear_transformations | Linear transformations]] can operate in more than two dimensions, extending the core ideas from 2D seamlessly to higher dimensions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This concept involves transforming three-dimensional vectors into other three-dimensional vectors <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## [[visualizing_transformations_in_three_dimensions | Visualizing Transformations in Three Dimensions]]

A [[visualizing_transformations_in_three_dimensions | three-dimensional linear transformation]] can be [[visualizing_transformations_in_three_dimensions | visualized]] by manipulating all points in three-dimensional space, represented by a grid <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. During this process, the grid lines remain parallel and evenly spaced, and the origin stays fixed <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Points moving in space are proxies for vectors whose tips are at those points, illustrating how input vectors map to their corresponding outputs <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

It can be simpler to [[visualizing_transformations_in_three_dimensions | visualize]] these transformations by focusing solely on the movements of the basis vectors, as a full 3D grid can appear cluttered <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. By keeping a copy of the original axes in the background, one can track the coordinates of where each of the three basis vectors lands <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## [[matrix_representation_of_3d_transformations | Matrix Representation of 3D Transformations]]

Just as with two dimensions, a [[linear_transformations | linear transformation]] is entirely defined by where its basis vectors land <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. In three dimensions, there are three standard basis vectors:
*   **i-hat**: The unit vector in the x-direction <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **j-hat**: The unit vector in the y-direction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **k-hat**: The unit vector in the z-direction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

The coordinates of these three transformed basis vectors are recorded as the columns of a 3x3 matrix <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This 3x3 matrix, containing only nine numbers, completely describes the transformation <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Example: Rotation Around the Y-axis
Consider a transformation that rotates space 90 degrees around the y-axis <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:
*   i-hat moves to coordinates (0, 0, -1) on the z-axis <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   j-hat remains at (0, 1, 0) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   k-hat moves to (1, 0, 0) on the x-axis <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

These three sets of coordinates form the columns of the matrix that describes this rotation <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Applying Transformations to Vectors

To determine where a vector with coordinates (x, y, z) lands after a transformation, the process is nearly identical to the two-dimensional case <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. Each coordinate represents instructions on how to scale each basis vector so they add up to the original vector <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This scaling and adding process works both before and after the transformation <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

Therefore, to find the transformed vector's location, you multiply the vector's coordinates by the corresponding columns of the transformation matrix, and then sum the three resulting vectors <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## [[composition_of_linear_transformations | Composition of Three-Dimensional Linear Transformations]]

Multiplying two 3x3 matrices is similar to the 2D case <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. When multiplying two 3x3 matrices, imagine first applying the transformation encoded by the rightmost matrix, followed by the transformation encoded by the leftmost matrix <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The numerical process of matrix multiplication in 3D is also very similar to the two-dimensional case <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Importance

[[matrix_representation_of_3d_transformations | 3D matrix multiplication]] is crucial in fields like computer graphics and robotics <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Complex transformations, such as rotations in three dimensions, can be challenging to describe directly. However, they become easier to understand by breaking them down into the [[composition_of_linear_transformations | composition]] of simpler, individual rotations <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.