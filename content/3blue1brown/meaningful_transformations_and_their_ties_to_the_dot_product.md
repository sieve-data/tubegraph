---
title: Meaningful transformations and their ties to the dot product
videoId: v8VSDg_WQlA
---

From: [[3blue1brown]] <br/> 

While [[linear_transformations | linear transformations]] are often illustrated as mapping vectors within the same dimension (e.g., 2D to 2D, or 3D to 3D), represented by square matrices <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>, it is also possible to discuss transformations that map vectors from one dimension to another <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. These transformations are represented by non-square matrices <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Characteristics of Linear Transformations Between Dimensions
For a transformation between dimensions to be considered linear, it must adhere to the same principles as other [[linear_transformations | linear transformations]]:
*   Grid lines in the input space remain parallel and evenly spaced in the output space <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   The origin of the input space maps to the origin of the output space <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

It is important to note that the input and output spaces are distinct and unconnected <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Matrix Representation of Cross-Dimensional Transformations
Encoding these transformations into a [[matrix_representation_of_transformations | matrix]] follows the same process as with square matrices <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>:
1.  Observe where each basis vector of the input space lands in the output space <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
2.  Write the coordinates of these landing spots as the columns of the matrix <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Examples of Non-Square Matrices
*   **3x2 Matrix (Mapping 2D to 3D):**
    *   A 3x2 matrix represents a transformation that takes 2D vectors and maps them to 3D vectors <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   The two columns indicate that the input space has two basis vectors (2D) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
    *   The three rows indicate that the landing spot for each basis vector is described with three coordinates (3D) <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   For example, if i-hat lands at (2, -1, -2) and j-hat lands at (0, 1, 1), the matrix would be:
        ```
        [ 2  0 ]
        [-1  1 ]
        [-2  1 ]
        ``` <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
    *   The column space of this matrix is a 2D plane passing through the origin of 3D space <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This matrix is considered full rank because the number of dimensions in the column space (2D) is the same as the number of dimensions in the input space (2D) <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

*   **2x3 Matrix (Mapping 3D to 2D):**
    *   A 2x3 matrix (two rows, three columns) signifies a transformation from 3D space to a 2D plane <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   The three columns indicate a starting space with three basis vectors (3D) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
    *   The two rows indicate that the landing spot for each of these basis vectors is described with only two coordinates (2D) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

*   **1x2 Matrix (Mapping 2D to 1D):**
    *   A 1x2 matrix represents a transformation from 2D space to a 1D space, which is essentially the number line <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This means 2D vectors are input, and numbers (scalars) are output <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   The two columns indicate the basis vectors of the 2D input space <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   The single entry in each column signifies that each basis vector lands on a single number on the number line <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
    *   For this type of transformation, linearity means that a line of evenly spaced dots in the input space would remain evenly spaced when mapped onto the number line <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Ties to the [[dot_product | Dot Product]]
The transformation from two dimensions to one dimension, represented by a 1x2 matrix, is a particularly significant type of transformation <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This specific kind of [[linear_transformations_and_dot_products | transformation has close ties to the dot product]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.