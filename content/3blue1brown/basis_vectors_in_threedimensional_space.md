---
title: Basis vectors in threedimensional space
videoId: rHLEWRxRGiM
---

From: [[3blue1brown]] <br/> 

In linear algebra, the concept of [[basis_vectors | basis vectors]] extends naturally from two dimensions to three dimensions, providing a fundamental way to understand and describe [[threedimensional_linear_transformations | three-dimensional linear transformations]] <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. While core ideas often begin with [[vectors_in_two_and_three_dimensions | two-dimensional vectors]] for visualization purposes, they carry over seamlessly to higher dimensions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Visualizing 3D Linear Transformations

A [[threedimensional_linear_transformations | linear transformation]] involving [[vectors_in_two_and_three_dimensions | three-dimensional vectors]] as both inputs and outputs can be visualized by imagining the entire [[vectors_in_two_and_three_dimensions | three-dimensional space]] being "smooshed around" <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This transformation must maintain parallelism and even spacing of the grid lines, and crucially, it must keep the origin fixed in place <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Each point moving in this space represents the tip of a vector, and the transformation maps input vectors to their corresponding output vectors <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Standard Basis Vectors in 3D

Similar to two dimensions, a [[threedimensional_linear_transformations | linear transformation]] in three dimensions is entirely defined by where its [[basis_vectors | basis vectors]] land <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. In three dimensions, there are three standard [[basis_vectors | basis vectors]]:
*   **i-hat**: The unit vector in the x-direction <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **j-hat**: The unit vector in the y-direction <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **k-hat**: The unit vector in the z-direction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

Focusing on the transformation of these three [[basis_vectors | basis vectors]] is often simpler than visualizing the entire 3D grid <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. By observing where each of these [[basis_vectors | basis vectors]] lands in relation to the original axes, their new coordinates can be recorded <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Describing 3D Transformations with Matrices

The coordinates of where the three transformed [[basis_vectors | basis vectors]] land become the columns of a 3x3 matrix <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This 3x3 matrix completely describes the [[threedimensional_linear_transformations | transformation]] using only nine numbers <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

For example, a transformation that rotates space 90 degrees around the y-axis would result in the following:
*   i-hat moves to the coordinates (0, 0, -1) on the z-axis <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   j-hat remains at its original coordinates (0, 1, 0) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   k-hat moves to the coordinates (1, 0, 0) on the x-axis <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

These three sets of coordinates form the columns of the matrix describing this rotation transformation <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>:

```
⎡ 0  0  1 ⎤
⎢ 0  1  0 ⎥
⎣ -1 0  0 ⎦
```

## Transforming a General Vector

To determine where a [[vectors_in_two_and_three_dimensions | general vector]] with coordinates (x, y, z) lands after a [[threedimensional_linear_transformations | transformation]], the reasoning is similar to the [[representation_of_vectors_using_basis_vectors | two-dimensional case]] <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. Each coordinate (x, y, z) indicates how much to scale each of the [[basis_vectors | basis vectors]] (i-hat, j-hat, k-hat) so that they sum up to form the original vector <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Crucially, this scaling and adding process remains valid both before and after the [[threedimensional_linear_transformations | transformation]] <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Therefore, to find the transformed vector's position, you multiply the original coordinates by the corresponding columns of the transformation matrix and then add the three resulting vectors together <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Matrix Multiplication in 3D

The multiplication of two 3x3 matrices in three dimensions is analogous to the 2D case <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. When two such matrices are multiplied, it represents the composition of two successive transformations <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>: first applying the transformation encoded by the rightmost matrix, and then applying the transformation encoded by the leftmost matrix <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. This process is particularly important in fields like computer graphics and robotics, where complex 3D rotations can be broken down into simpler, sequential transformations <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.