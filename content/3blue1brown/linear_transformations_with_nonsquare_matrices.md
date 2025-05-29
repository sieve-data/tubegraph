---
title: Linear transformations with nonsquare matrices
videoId: v8VSDg_WQlA
---

From: [[3blue1brown]] <br/> 

While [[linear_transformations | linear transformations]] are often discussed in the context of transforming vectors within the same dimension (e.g., 2D to 2D, or 3D to 3D) using square matrices <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, it is also perfectly reasonable to consider [[representing_transformations_between_dimensions_using_matrices | transformations between dimensions]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. These types of [[linear_transformations | linear transformations]] are represented by nonsquare matrices <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Characteristics of Linear Transformations
Regardless of the dimensions involved, a transformation is considered linear if two conditions are met:
*   Grid lines remain parallel and evenly spaced <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   The origin maps to the origin <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

It's important to note that the input and output spaces of transformations between dimensions are completely separate <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Encoding Transformations with Nonsquare Matrices
[[matrix_representation_of_linear_transformations | Encoding]] one of these transformations with a matrix follows the same principle as with square matrices <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. One identifies where each basis vector lands and writes the coordinates of these landing spots as the columns of the matrix <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### 3x2 Matrices: 2D to 3D Transformation
A 3x2 matrix represents a [[representing_transformations_between_dimensions_using_matrices | transformation]] that takes 2D vectors to [[threedimensional_linear_transformations | 3D vectors]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   The two columns indicate that the input space has two basis vectors (2D input) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   The three rows indicate that the landing spots for each basis vector are described with three separate coordinates (3D output) <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

For example, a transformation mapping the basis vector i-hat to (2, -1, -2) and j-hat to (0, 1, 1) would be represented by a 3x2 matrix <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>:
```
[ 2  0 ]
[-1  1 ]
[-2  1 ]
```
The column space of this 3x2 matrix, representing where all vectors land, is a 2D plane slicing through the origin of [[threedimensional_linear_transformations | 3D space]] <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This matrix is considered full rank because the number of dimensions in its column space (2D) is the same as the number of dimensions of the input space (2D) <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### 2x3 Matrices: 3D to 2D Transformation
A 2x3 matrix represents a [[representing_transformations_between_dimensions_using_matrices | transformation]] from [[threedimensional_linear_transformations | 3D space]] to a 2D plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   The three columns indicate that the starting space has three basis vectors (3D input) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   The two rows indicate that the landing spot for each of those three basis vectors is described with only two coordinates (2D output) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### 1x2 Matrices: 2D to 1D Transformation
A 1x2 matrix represents a [[representing_transformations_between_dimensions_using_matrices | transformation]] from two dimensions to one dimension <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. One-dimensional space is essentially the number line <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>, so this transformation takes 2D vectors and outputs numbers <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   The two columns represent where the basis vectors land <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   Each column has a single entry, representing the single number that the basis vector lands on <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

In this context, the visual understanding of linearity means that a line of evenly spaced dots in the input space would remain evenly spaced once mapped onto the number line <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This type of transformation has close ties to the [[linear_transformations_and_dot_products | dot product]] <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

Understanding [[matrix multiplication and transformations | matrix multiplication]] and linear systems of equations can be further explored in the context of [[representing_transformations_between_dimensions_using_matrices | transformations between different dimensions]] <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.