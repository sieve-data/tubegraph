---
title: Matrix dimensions and their geometric interpretations
videoId: v8VSDg_WQlA
---

From: [[3blue1brown]] <br/> 

Linear transformations are not limited to mapping vectors within the same dimension. It's perfectly reasonable to conceptualize transformations that alter the number of dimensions of a vector, such as mapping 2D vectors to 3D vectors <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Characteristics of Linear Transformations
Regardless of the dimensions involved, a transformation is considered linear if two conditions are met:
*   Gridlines in the input space remain parallel and evenly spaced in the output space <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   The origin of the input space maps to the origin of the output space <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

It's important to note that the input and output spaces are "completely separate, unconnected" entities, emphasizing that 2D vector inputs are distinct from 3D vector outputs <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## [[Matrix representation of transformations | Matrix Representation of Transformations]] Between Dimensions
[[Matrix representation of linear transformations | Encoding linear transformations]] between different dimensions with a matrix follows the same principles as within the same dimension <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. To construct the matrix, you observe where each basis vector (e.g., i-hat and j-hat in 2D) lands in the output space, and these landing coordinates become the columns of the matrix <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Example: 2D to 3D Transformation (3x2 Matrix)
Consider a transformation that maps 2D vectors to 3D vectors.
*   If the i-hat basis vector lands at coordinates (2, -1, -2) <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   And the j-hat basis vector lands at coordinates (0, 1, 1) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

This transformation is encoded by a matrix with three rows and two columns, known as a 3x2 matrix <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

The geometric interpretation of a 3x2 matrix is a mapping from two dimensions to three dimensions <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>:
*   The **two columns** indicate that the input space has two basis vectors, implying a 2D input <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   The **three rows** indicate that the landing coordinates for each basis vector are described with three separate coordinates, implying a 3D output <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

The column space of such a matrix, which represents the entire set of possible output vectors, is a 2D plane slicing through the origin of 3D space <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This matrix is "full rank" because the number of dimensions in its column space (2D) matches the number of dimensions in the input space (2D) <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Other Non-Square Matrix Interpretations
*   **2x3 Matrix (3D to 2D)**: A matrix with two rows and three columns indicates a transformation from 3D space onto the 2D plane <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. The three columns signify a starting space with three basis vectors (3D input) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>, while the two rows mean each basis vector's landing spot is described with only two coordinates (2D output) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **1x2 Matrix (2D to 1D)**: A transformation from two dimensions to one dimension <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. One-dimensional space is essentially the number line, so this transformation takes 2D vectors and outputs single numbers <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. A 1x2 matrix has two columns, each with a single entry, representing where the basis vectors land on the number line <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This type of transformation has close ties to the dot product <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

These examples illustrate how the dimensions of a matrix directly convey the geometric nature of the linear transformation it represents, specifically concerning the change in dimensionality between the input and output spaces.