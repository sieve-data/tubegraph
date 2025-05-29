---
title: Basis vectors in three dimensions
videoId: rHLEWRxRGiM
---

From: [[3blue1brown]] <br/> 

Linear transformations in higher dimensions, such as three dimensions, build seamlessly on the core ideas established in two dimensions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. While the series primarily focuses on two dimensions for easier visualization <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, understanding these concepts in three dimensions is crucial for broader applications <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Visualizing 3D Linear Transformations

A linear transformation involving three-dimensional vectors as both inputs and outputs can be visualized as "smooshing around" all points in three-dimensional space <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This transformation maintains certain properties:
*   Grid lines remain parallel <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   Grid lines remain evenly spaced <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   The origin stays fixed in place <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

Each point in space that moves during the transformation acts as a proxy for a [[understanding_vectors | vector]] whose tip is at that point, illustrating the transformation of input vectors to their corresponding outputs <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Role of Basis Vectors in 3D

Just as in two dimensions, any linear transformation in three dimensions is completely described by knowing where its [[coordinate_systems_and_basis_vectors | basis vectors]] land after the transformation <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. For three dimensions, there are three standard [[unit_vectors_and_basis_vectors | basis vectors]] typically used:
*   **i-hat**: The [[unit_vectors_and_basis_vectors | unit vector]] in the x-direction <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **j-hat**: The [[unit_vectors_and_basis_vectors | unit vector]] in the y-direction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **k-hat**: The [[unit_vectors_and_basis_vectors | unit vector]] in the z-direction <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

It is often easier to understand these transformations by focusing solely on where these three [[unit_vectors_and_basis_vectors | basis vectors]] move, as visualizing the entire 3D grid can become complex <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. By observing the coordinates where each of these [[unit_vectors_and_basis_vectors | basis vectors]] lands against a backdrop of the original axes, one can deduce the transformation <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## Matrices for 3D Transformations

The coordinates of the transformed [[unit_vectors_and_basis_vectors | basis vectors]] form the columns of a 3x3 matrix <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This matrix, composed of nine numbers, fully describes the linear transformation <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

> [!example] Rotation Around the Y-axis
> Consider a transformation that rotates space 90 degrees around the y-axis <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:
> *   **i-hat** (original: (1,0,0)) moves to (0,0,-1) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
> *   **j-hat** (original: (0,1,0)) remains at (0,1,0) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
> *   **k-hat** (original: (0,0,1)) moves to (1,0,0) <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
>
> These three sets of coordinates then become the columns of the 3x3 matrix representing this rotation transformation <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>:
>
> $$\begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ -1 & 0 & 0 \end{bmatrix}$$

## Applying Transformations to Vectors

To determine where a [[understanding_vectors | vector]] with coordinates (x,y,z) lands after a 3D linear transformation, the process is nearly identical to the two-dimensional case <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. The coordinates (x,y,z) instruct how to scale each [[unit_vectors_and_basis_vectors | basis vector]] so that they sum to form the original vector <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Crucially, this scaling and adding property holds true both before and after the transformation <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

Therefore, to find the transformed vector, you multiply the vector's coordinates by the corresponding columns of the transformation matrix and then add the three resulting vectors <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Matrix Multiplication in 3D

Multiplying two 3x3 matrices together is also similar to the two-dimensional process <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. It represents the composition of two successive linear transformations: first applying the transformation encoded by the right matrix, then applying the transformation encoded by the left matrix <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

This concept of 3D matrix multiplication is particularly important in fields like computer graphics and robotics. It allows complex transformations, such as rotations in three dimensions, to be broken down into simpler, easier-to-manage component rotations <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Numerically, the calculation of 3D matrix multiplication mirrors its two-dimensional counterpart <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.