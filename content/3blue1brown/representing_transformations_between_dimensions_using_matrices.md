---
title: Representing transformations between dimensions using matrices
videoId: v8VSDg_WQlA
---

From: [[3blue1brown]] <br/> 

While [[linear_transformations_and_matrices | linear transformations]] are often discussed in the context of mapping vectors within the same dimension (e.g., 2D to 2D using [[matrix_representation_of_transformations | 2x2 matrices]] or 3D to 3D using [[matrix_representation_of_transformations | 3x3 matrices]]), it is also possible to represent transformations that map vectors from one dimension to another using non-square matrices <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These matrices provide a geometric interpretation of how vectors transform between different dimensional spaces <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Characteristics of Linear Transformations Between Dimensions

A transformation between dimensions remains linear if two key conditions are met <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>:
*   Gridlines remain parallel and evenly spaced <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   The origin maps to the origin <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

It's important to recognize that input vectors from one dimension are distinct from output vectors in another dimension, residing in completely separate spaces <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Encoding Transformations with Non-Square Matrices

[[matrix_representation_of_linear_transformations | Encoding these transformations with a matrix]] follows the same principle as with square matrices <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>:
1.  Identify where each basis vector lands after the transformation <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
2.  Use the coordinates of these landing spots as the columns of the matrix <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Mapping 2D to 3D (3x2 Matrix)

Consider a transformation that takes 2D vectors to 3D vectors <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The input space is 2D, and the output space is 3D <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

*   **Example**: If the basis vector i-hat (from the 2D input space) lands at coordinates (2, -1, -2) in 3D space, and j-hat lands at (0, 1, 1) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Matrix Structure**: The [[matrix representation of linear transformations | matrix encoding]] this transformation will have three rows (for the 3D output coordinates) and two columns (for the two 2D basis vectors) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This is known as a 3x2 matrix <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

```
[[ 2, 0 ],
 [ -1, 1 ],
 [ -2, 1 ]]
```

*   **Geometric Interpretation**: A 3x2 matrix maps two dimensions to three dimensions <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   The two columns indicate an input space with two basis vectors <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
    *   The three rows indicate that the landing spot for each basis vector requires three coordinates <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Column Space**: The column space of such a matrix (where all vectors land) is a 2D plane passing through the origin within 3D space <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. If the number of dimensions in the column space is equal to the number of dimensions of the input space, the matrix is considered full rank <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Mapping 3D to 2D (2x3 Matrix)

A 2x3 matrix (two rows, three columns) represents a transformation from 3D space to a 2D plane <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

*   **Geometric Interpretation**:
    *   The three columns indicate a starting space with three basis vectors (3D input) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
    *   The two rows indicate that the landing spot for each of those three basis vectors is described with only two coordinates (2D output) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Mapping 2D to 1D (1x2 Matrix)

A transformation from two dimensions to one dimension takes 2D vectors and outputs single numbers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. One-dimensional space is essentially the number line <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

*   **Linearity in 1D**: For [[two_dimensional_grid_transformations | gridlines]] or evenly spaced dots, linearity means they remain evenly spaced after being mapped onto the number line <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Matrix Structure**: Such a transformation is encoded with a 1x2 matrix <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
    *   The two columns represent where the 2D basis vectors land <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
    *   Each column has a single entry, representing the number that basis vector landed on <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

This type of transformation is closely related to the dot product <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

Understanding [[matrix_vector_multiplication_and_transformations | matrix multiplication]] and linear systems of equations in the context of transformations between different dimensions can provide further insights <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.