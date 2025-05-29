---
title: Transformations between different dimensions
videoId: v8VSDg_WQlA
---

From: [[3blue1brown]] <br/> 

While discussions of [[Linear transformations in linear algebra | linear transformations]] often focus on transformations within the same dimension (e.g., 2D to 2D or 3D to 3D) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, it is also perfectly reasonable to consider transformations that map vectors from one dimension to another <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, such as taking 2D vectors to 3D vectors <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Linearity Criteria

Similar to same-dimension transformations, what makes a transformation between different dimensions linear is that gridlines remain parallel and evenly spaced, and the origin maps to the origin <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For transformations that result in significant "squishification" (e.g., 2D to 1D), the visual understanding of linearity is that a line of evenly spaced dots would remain evenly spaced once mapped onto the number line <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

It is important to emphasize that input vectors from one dimension are fundamentally different from output vectors in another, existing in completely separate, unconnected spaces <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Matrix Representation of Transformations

Encoding these transformations with a matrix follows the same principle as [[Matrix representations and transformations | matrix representations and transformations]] within the same dimension <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. One examines where each basis vector lands and writes the coordinates of these landing spots as the columns of a matrix <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This often results in non-square matrices <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

### Mapping 2D to 3D (3x2 Matrix)

A transformation that takes 2D vectors to 3D vectors is encoded by a 3x2 matrix <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Columns:** The two columns indicate that the input space has two basis vectors (i.e., it's a 2D input space) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Rows:** The three rows indicate that the landing spots for each of those basis vectors are described with three separate coordinates (i.e., they land in 3D space) <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

For example, if the 2D basis vector **î** lands at (2, -1, -2) and **ĵ** lands at (0, 1, 1), the matrix would be:
$$
\begin{pmatrix} 2 & 0 \\ -1 & 1 \\ -2 & 1 \end{pmatrix}
$$
<a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>

The column space of this 3x2 matrix, which represents where all vectors land, is a 2D plane slicing through the origin of 3D space <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This matrix is considered full rank because the number of dimensions in its column space (2D) is the same as the number of dimensions of the input space (2D) <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Mapping 3D to 2D (2x3 Matrix)

A transformation from 3D space onto the 2D plane is encoded by a 2x3 matrix <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **Columns:** The three columns indicate that the starting space has three basis vectors (i.e., it's a 3D input space) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Rows:** The two rows indicate that the landing spot for each of those three basis vectors is described with only two coordinates (i.e., they land in 2D space) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Mapping 2D to 1D (1x2 Matrix)

A transformation from two dimensions to one dimension (the number line) takes in 2D vectors and outputs numbers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This is encoded by a 1x2 matrix <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Columns:** The two columns represent where the 2D basis vectors land <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Rows:** Each column has just a single entry, representing the single number that each basis vector landed on in the 1D output space <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

This type of transformation has close ties to the dot product <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

## Broader Implications

Understanding these non-square matrices allows for the contemplation of concepts like matrix multiplication and linear systems of equations in the context of transformations between different dimensions <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.