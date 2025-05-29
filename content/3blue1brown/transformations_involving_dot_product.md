---
title: Transformations involving dot product
videoId: v8VSDg_WQlA
---

From: [[3blue1brown]] <br/> 

While [[linear_transformations_in_linear_algebra | linear transformations]] are often discussed in the context of mapping vectors within the same dimension (e.g., 2D to 2D using 2x2 matrices, or 3D to 3D using 3x3 matrices) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, it is also possible to consider [[transformations_between_different_dimensions | transformations between different dimensions]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. These transformations are represented by non-square matrices <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>, and their geometric meaning can be understood by examining how basis vectors are mapped <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Geometric Interpretation of Non-Square Matrices

A fundamental property of linear transformations, regardless of dimension change, is that gridlines remain parallel and evenly spaced, and the origin maps to the origin <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Transformations from 2D to 3D

A transformation that takes 2D vectors to 3D vectors is perfectly reasonable <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The input space is 2D, while the output is a 3D space <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. It is important to emphasize that 2D input vectors and 3D output vectors reside in completely separate, unconnected spaces <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

To encode such a transformation with a matrix, one observes where each basis vector lands and uses their coordinates as the columns of the matrix <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

For example, if the i-hat basis vector lands at (2, -1, -2) and the j-hat basis vector lands at (0, 1, 1) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>, the resulting matrix will have three rows and two columns, making it a 3x2 matrix <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

A 3x2 matrix geometrically interprets as mapping two dimensions to three dimensions <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   The two columns indicate that the input space has two basis vectors <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   The three rows indicate that the landing spots for each basis vector are described with three coordinates <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

The column space of such a matrix, which represents where all vectors land, would be a 2D plane slicing through the origin of 3D space <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. If the number of dimensions in this column space matches the number of dimensions of the input space, the matrix is considered full rank <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Transformations from 3D to 2D

A 2x3 matrix, with two rows and three columns, means:
*   The three columns indicate a starting space with three basis vectors (3D) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   The two rows indicate that the landing spot for each of these three basis vectors is described with only two coordinates (2D) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

Thus, a 2x3 matrix represents a transformation from 3D space onto the 2D plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Transformations from 2D to 1D and the Dot Product

It is also possible to have a transformation from two dimensions to one dimension <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. One-dimensional space is simply the number line <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Such a transformation takes 2D vectors as input and outputs single numbers <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

In this context, the visual understanding of linearity means that a line of evenly spaced dots in the input space would remain evenly spaced once mapped onto the number line <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

These transformations are encoded with a 1x2 matrix <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   The two columns represent where the basis vectors land <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   Each column has just a single entry, representing the number that the basis vector landed on <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

This type of transformation, where 2D vectors are mapped to numbers, has close ties to the [[geometric_interpretation_of_dot_products | dot product]] <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This relationship highlights how the dot product can be viewed as a specific type of [[transformations_between_different_dimensions | linear transformation]] that reduces dimensionality to one.

Further exploration of matrix multiplication and linear systems of equations within the context of [[transformations_between_different_dimensions | transformations between different dimensions]] can provide deeper insights <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.