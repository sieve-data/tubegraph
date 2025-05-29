---
title: Concept of column space in transformations
videoId: v8VSDg_WQlA
---

From: [[3blue1brown]] <br/> 

The concept of the column space of a matrix is illuminated by understanding how matrices represent [[linear_transformations | linear transformations]], particularly those that transform vectors between different dimensions <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## [[linear_transformations | Linear Transformations]] Between Dimensions

While [[visualizing_linear_transformations_with_matrices | linear transformations]] are often discussed in the context of 2D to 2D or 3D to 3D mappings <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, it is also perfectly reasonable to consider transformations that map vectors from one dimension to another <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For example, a transformation might take 2D vectors to 3D vectors <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

The defining characteristics of a [[linear_transformations | linear transformation]] remain consistent:
*   Gridlines in the input space remain parallel and evenly spaced in the output space <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   The origin of the input space maps to the origin of the output space <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

It is crucial to recognize that input vectors and output vectors exist in completely separate, unconnected spaces when dimensions differ (e.g., 2D inputs vs. 3D outputs) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## [[matrix_representation_of_transformations | Matrix Representation of Transformations]] Between Dimensions

Encoding these [[representing_transformations_between_dimensions_using_matrices | transformations between dimensions using matrices]] follows the same principles as with square matrices <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>:
1.  Identify where each basis vector of the input space lands after the transformation <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
2.  The coordinates of these landing spots become the columns of the matrix <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Interpreting Non-Square Matrices

Non-square matrices arise when the input and output dimensions are different:

*   **3x2 Matrix (3 rows, 2 columns):**
    *   This matrix encodes a transformation from two dimensions to three dimensions <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>, <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.
    *   The **two columns** indicate that the input space has two basis vectors (i.e., it's a 2D input space) <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.
    *   The **three rows** indicate that the landing spot for each basis vector is described with three coordinates (i.e., the output is in 3D space) <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
    *   *Example:* If i-hat maps to (2, -1, -2) and j-hat maps to (0, 1, 1), the matrix would be:
        ```
        [ 2  0 ]
        [-1  1 ]
        [-2  1 ]
        ```
        <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>

*   **2x3 Matrix (2 rows, 3 columns):**
    *   This matrix indicates a transformation from three dimensions to two dimensions <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>, <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
    *   The **three columns** mean the input space has three basis vectors (3D input) <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.
    *   The **two rows** mean the landing spot for each basis vector is described with two coordinates (2D output) <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

*   **1x2 Matrix (1 row, 2 columns):**
    *   This matrix represents a transformation from two dimensions to one dimension (the number line) <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>, <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.
    *   The **two columns** signify two basis vectors in the input <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.
    *   The **single row** means each basis vector lands on a single number <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.

## The Column Space

The "column space" of a matrix is the set of all possible output vectors of the [[matrix_representation_of_linear_transformations | linear transformation]] it represents <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. It is the geometric "place where all the vectors land" <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

For the 3x2 matrix example given above:
*   The column space is a 2D plane that slices through the origin of 3D space <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. This is because all 2D input vectors are transformed into vectors that lie on this specific 2D plane within the larger 3D output space.
*   A matrix is considered "full rank" if the number of dimensions in its column space is equal to the number of dimensions in the input space <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. The 3x2 matrix example is full rank because its column space (a 2D plane) has the same dimensionality as the input space (2D).

This concept has close ties to the dot product, which will be explored further <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.