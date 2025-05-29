---
title: Applications of 3D transformations in computer graphics and robotics
videoId: rHLEWRxRGiM
---

From: [[3blue1brown]] <br/> 

While much of the foundational understanding of [[Linear transformations and matrices | linear transformations]] is often explored in two dimensions for clarity <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>, the core ideas extend seamlessly to higher dimensions <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This generalization is particularly crucial for fields like [[Applications of vectors in data analysis and computer graphics | computer graphics]] and robotics, where operations in three-dimensional space are fundamental.

## Visualizing 3D Transformations
A [[visualizing_transformations_in_three_dimensions | linear transformation]] involving three-dimensional vectors as both inputs and outputs can be visualized as a "smooshing around" of all points in [[Threedimensional linear transformations | three-dimensional space]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This transformation maintains parallel and evenly spaced grid lines and keeps the origin fixed <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Each moving point represents the tip of a vector, showing how input vectors are mapped to their corresponding outputs <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Matrix Representation of 3D Transformations
Just as with [[Two dimensional grid transformations | two-dimensional transformations]], a three-dimensional linear transformation is completely defined by where its basis vectors land <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. In three dimensions, there are three standard basis vectors:
*   i-hat (unit vector in the x direction) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>
*   j-hat (unit vector in the y direction) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>
*   k-hat (unit vector in the z direction) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>

The coordinates where these three basis vectors land become the columns of a 3x3 matrix <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This [[matrix_representation_of_3d_transformations | matrix representation]] uses only nine numbers to fully describe the transformation <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. For example, a rotation of space by 90 degrees around the y-axis would transform i-hat to (0,0,-1), j-hat to (0,1,0), and k-hat to (1,0,0) <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. These new coordinates form the columns of the transformation matrix <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## Applying and Composing 3D Transformations
To find where a vector (x,y,z) lands after a transformation, one can think of its coordinates as instructions to scale each basis vector and add them together <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. This scaling and adding process remains consistent before and after the transformation <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Numerically, this means multiplying the vector's coordinates by the corresponding columns of the transformation matrix and then adding the three resulting vectors <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Matrix Multiplication for Composition
Multiplying two 3x3 matrices together corresponds to applying two successive transformations in space <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. The transformation encoded by the right matrix is applied first, followed by the transformation encoded by the left matrix <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## Importance in Computer Graphics and Robotics
[[Matrix representation of 3D transformations | 3D matrix multiplication]] is highly significant in fields such as [[Applications of vectors in data analysis and computer graphics | computer graphics]] and robotics <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Complex operations like [[Applications of quaternions in threedimensional rotations and quantum mechanics | rotations in three dimensions]] can be challenging to describe directly <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. However, they become more manageable when broken down into a composition of simpler, more intuitive rotations <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. This compositional approach, facilitated by matrix multiplication, simplifies the computational and conceptual handling of intricate 3D movements and transformations.