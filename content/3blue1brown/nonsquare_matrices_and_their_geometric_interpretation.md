---
title: Nonsquare matrices and their geometric interpretation
videoId: v8VSDg_WQlA
---

From: [[3blue1brown]] <br/> 

[[Matrix representation of linear transformations | Linear transformations]] have typically been discussed in the context of transforming 2D vectors to other 2D vectors, represented by 2x2 matrices, or 3D vectors to other 3D vectors, represented by [[mathematical_representation_with_3x3_matrices | 3x3 matrices]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. However, it is also possible to talk about transformations between different dimensions, which are represented by nonsquare matrices <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Transformations Between Dimensions

A [[Matrix representation of linear transformations | linear transformation]] maintains that gridlines remain parallel and evenly spaced, and that the origin maps to the origin <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Encoding these transformations with a matrix follows the same principle as with square matrices: observe where each basis vector lands, and write the coordinates of these landing spots as the columns of the matrix <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### From 2D to 3D (3x2 Matrix)

It is perfectly reasonable to describe a transformation that takes 2D vectors to 3D vectors <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. In such a scenario, the input space (2D) is distinct and unconnected from the output space (3D) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

For example, a transformation might map the 2D basis vector i-hat to the 3D coordinates (2, -1, -2) and j-hat to (0, 1, 1) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This results in a matrix with three rows and two columns, known as a 3x2 matrix <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

*   The two columns indicate that the input space has two basis vectors (i.e., 2D input) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   The three rows indicate that the landing spots for each basis vector are described with three coordinates (i.e., 3D output) <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

The column space of this 3x2 matrix, which is the space where all transformed vectors land, forms a 2D plane slicing through the origin of 3D space <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. If the number of dimensions in this column space matches the number of dimensions in the input space, the matrix is considered full rank <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### From 3D to 2D (2x3 Matrix)

A 2x3 matrix (two rows and three columns) has a different geometric interpretation <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

*   The three columns signify that the transformation starts in a space with three basis vectors (i.e., 3D input) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   The two rows indicate that the landing spot for each of these three basis vectors is described with only two coordinates (i.e., 2D output) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

Thus, a 2x3 matrix represents a transformation from 3D space onto the 2D plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### From 2D to 1D (1x2 Matrix)

A transformation can also map two dimensions to one dimension <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. One-dimensional space is simply the number line <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This means 2D vectors are taken as input and numbers are output <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

Due to the significant "squishification," the visual understanding of linearity changes slightly; if a line of evenly spaced dots is input, it remains evenly spaced when mapped onto the number line <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

This type of transformation is encoded by a 1x2 matrix, where each of the two columns has only a single entry <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

*   The two columns represent where the basis vectors land <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   Each column requires just one number, representing the point where that basis vector landed on the number line <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

This particular type of transformation is closely related to the [[geometric_interpretation_of_dot_products | dot product]] <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

Understanding these [[Matrix representation of linear transformations | matrix representations of linear transformations]] across different dimensions can provide valuable insight into [[geometric_interpretation_of_linear_systems | linear systems]] of equations and matrix multiplication <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.