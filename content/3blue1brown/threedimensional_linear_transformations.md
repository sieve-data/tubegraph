---
title: Threedimensional linear transformations
videoId: rHLEWRxRGiM
---

From: [[3blue1brown]] <br/> 

This article explores [[linear_transformations_in_linear_algebra | linear transformations]] in three dimensions, expanding upon concepts typically introduced in two dimensions <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. While most core ideas in [[visual_understanding_of_linear_transformations | two dimensions]] translate seamlessly to higher dimensions <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>, it is beneficial to understand their application beyond flatland <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Visualization

A [[linear_transformations | linear transformation]] with three-dimensional vectors as inputs and outputs can be visualized as "smooshing around" all points in three-dimensional space <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This transformation maintains grid lines parallel and evenly spaced, while fixing the origin in place <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Each moving point represents the tip of a vector, showing how input vectors are mapped to their corresponding outputs <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Basis Vectors and Matrix Representation

Just as in two dimensions, a [[introduction_to_linear_transformations | linear transformation]] is entirely defined by where its basis vectors land <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. In three dimensions, there are three standard basis vectors:
*   **i-hat**: The unit vector in the x-direction <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>
*   **j-hat**: The unit vector in the y-direction <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>
*   **k-hat**: The unit vector in the z-direction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

To describe a transformation, the coordinates of where these three basis vectors land are recorded as the columns of a 3x3 matrix <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This 3x3 [[matrix_representation_of_linear_transformations | matrix representation]] completely describes the transformation using only nine numbers <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Thinking about the transformation by only following these basis vectors can be easier than visualizing the entire 3D grid <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Example: 90-degree rotation around the y-axis

Consider a transformation that rotates space 90 degrees around the y-axis <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:
*   **i-hat** moves to the coordinates (0, 0, -1) on the z-axis <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **j-hat** remains at (0, 1, 0) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **k-hat** moves to the x-axis at (1, 0, 0) <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

These three sets of coordinates form the columns of the matrix describing this rotation <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>:

```
⎡ 0  0  1 ⎤
⎢ 0  1  0 ⎥
⎣-1  0  0 ⎦
```

## Applying a Transformation to a Vector

To determine where a vector with coordinates (x, y, z) lands after a transformation, the process is similar to two dimensions <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. The coordinates (x, y, z) instruct how to scale each basis vector so they add up to the original vector <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This scaling and adding process works both before and after the transformation <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
Therefore, to find the transformed vector, you multiply the vector's coordinates by the corresponding columns of the [[matrix_representations_of_linear_transformations | transformation matrix]], and then sum the three resulting vectors <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Matrix Multiplication and Composition

Multiplying two 3x3 matrices is analogous to the 2D case <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. It represents applying the transformation encoded by the right matrix first, followed by the transformation encoded by the left matrix <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

[[composition_of_linear_transformations | 3D matrix multiplication]] is crucial in fields such as computer graphics and robotics <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Complex rotations in three dimensions, which can be challenging to describe directly, become more manageable when broken down into the [[composition of linear transformations | composition]] of simpler, easier-to-understand rotations <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The numerical process for 3D matrix multiplication is very similar to its two-dimensional counterpart <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.