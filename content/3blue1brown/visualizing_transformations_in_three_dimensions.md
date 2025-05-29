---
title: Visualizing transformations in three dimensions
videoId: rHLEWRxRGiM
---

From: [[3blue1brown]] <br/> 

This article explores [[visualizing_mathematical_concepts | visualizing]] [[threedimensional_linear_transformations | linear transformations]] in [[threedimensional_linear_transformations | three dimensions]], building upon concepts previously discussed for [[two_dimensional_grid_transformations | two dimensions]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. While most discussions in this series focus on [[two_dimensional_grid_transformations | two dimensions]] for ease of [[visualizing_mathematical_concepts | visualization]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, the core ideas extend seamlessly to higher dimensions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Visualizing 3D Transformations

A [[threedimensional_linear_transformations | linear transformation]] involving [[threedimensional_linear_transformations | three-dimensional vectors]] as both inputs and outputs can be [[visualizing_mathematical_concepts | visualized]] by manipulating points in [[threedimensional_linear_transformations | three-dimensional space]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This manipulation, represented by a grid, maintains parallelism and even spacing of the grid lines, and keeps the origin fixed <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Every moving point represents a vector whose tip is at that point, illustrating how input vectors transform into their corresponding outputs <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Role of Basis Vectors

Similar to [[two_dimensional_grid_transformations | two dimensions]], a [[threedimensional_linear_transformations | 3D linear transformation]] is entirely defined by where the basis vectors land <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. In [[threedimensional_linear_transformations | three dimensions]], there are three standard basis vectors:
*   **i-hat**: The unit vector in the x-direction <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **j-hat**: The unit vector in the y-direction <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **k-hat**: The unit vector in the z-direction <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

Focusing on the transformation of these basis vectors simplifies [[visualizing_mathematical_concepts | visualizing]] the overall transformation, as a full [[threedimensional_linear_transformations | 3D]] grid can become complex <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. By observing the coordinates where each of these three basis vectors lands relative to the original axes, one can understand the transformation <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Matrix Representation of 3D Transformations

The coordinates of these three transformed basis vectors form the columns of a [[matrix_representation_of_3d_transformations | 3x3 matrix]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This [[matrix_representation_of_3d_transformations | matrix]] comprehensively describes the transformation using just nine numbers <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Example: Rotation Around the Y-axis
Consider a transformation that rotates space 90 degrees around the y-axis <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>:
*   i-hat moves to the coordinates (0, 0, -1) on the z-axis <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   j-hat remains at (0, 1, 0) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   k-hat moves to (1, 0, 0) on the x-axis <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

These three sets of coordinates become the columns of the [[matrix_representation_of_3d_transformations | matrix]] representing this rotation <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>:

```
[[0, 0, 1],
 [0, 1, 0],
 [-1, 0, 0]]
```

## Applying Transformations to Vectors

To determine where a vector with coordinates (x, y, z) lands after a transformation, the process is nearly identical to the [[two_dimensional_grid_transformations | two-dimensional]] case <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. Each coordinate instructs how to scale the corresponding basis vector so they sum up to the original vector <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This scaling and adding process remains consistent before and after the transformation <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Therefore, to find the transformed vector, multiply the input coordinates by the corresponding columns of the [[matrix_representation_of_3d_transformations | matrix]] and sum the three resulting vectors <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Matrix Multiplication for Successive Transformations

[[matrix_representation_of_transformations | Multiplying]] two [[matrix_representation_of_3d_transformations | 3x3 matrices]] represents applying two successive transformations <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. The transformation encoded by the right [[matrix_representation_of_3d_transformations | matrix]] is applied first, followed by the transformation encoded by the left [[matrix_representation_of_3d_transformations | matrix]] <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. Numerically, [[matrix_representation_of_transformations | 3D matrix multiplication]] is similar to its [[two_dimensional_grid_transformations | two-dimensional]] counterpart <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Applications
[[matrix_representation_of_transformations | 3D matrix multiplication]] is crucial in fields like [[applications_of_3d_transformations_in_computer_graphics_and_robotics | computer graphics and robotics]] <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. [[threedimensional_linear_transformations | Rotations in three dimensions]], which can be complex to describe, become easier to understand when broken down into compositions of simpler rotations <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.