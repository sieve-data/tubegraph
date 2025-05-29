---
title: Matrix representation of linear transformations
videoId: v8VSDg_WQlA
---

From: [[3blue1brown]] <br/> 

[[introduction_to_linear_transformations | Linear transformations]], discussed previously, typically involve mapping vectors within the same dimension, such as 2D vectors to other 2D vectors using 2x2 matrices, or [[threedimensional_linear_transformations | 3D vectors]] to other 3D vectors using 3x3 matrices <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. However, [[matrix_representations_of_linear_transformations | non-square matrices]] also have significant geometric meaning <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Transformations Between Dimensions

It is entirely valid to consider [[linear_transformations_in_linear_algebra | linear transformations]] that map vectors between different dimensions <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For a transformation to be considered linear, grid lines must remain parallel and evenly spaced, and the origin must map to the origin <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

It's important to recognize that input vectors and output vectors exist in separate, unconnected spaces. For example, 2D vector inputs are fundamentally different from 3D vector outputs <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Encoding Transformations with Matrices

The process for encoding these transformations with a matrix is consistent with how square matrices are formed: you observe where each basis vector lands after the transformation and use their coordinates as the columns of the matrix <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Examples of Non-Square Matrices

#### From 2D to 3D (3x2 Matrix)

Consider a transformation that maps a 2D vector input space to a 3D vector output space <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
For instance, if the basis vector i-hat maps to (2, -1, -2) and j-hat maps to (0, 1, 1), the resulting matrix would be:
$\begin{pmatrix} 2 & 0 \\ -1 & 1 \\ -2 & 1 \end{pmatrix}$ <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

This matrix has three rows and two columns, making it a 3x2 matrix <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

*   The two columns signify that the input space has two basis vectors, indicating a 2D input <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   The three rows signify that the landing spots for each basis vector are described with three coordinates, indicating a 3D output <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

The column space of this matrix, which represents the space where all input vectors land, is a 2D plane intersecting the origin in 3D space <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This matrix is considered full rank because the number of dimensions in its column space (2D) is the same as the number of dimensions in the input space (2D) <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

#### From 3D to 2D (2x3 Matrix)

A 2x3 matrix has two rows and three columns <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

*   The three columns indicate a starting space with three basis vectors, meaning a 3D input <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   The two rows indicate that the landing spot for each of these three basis vectors is described with only two coordinates, meaning they land in 2D space <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

Thus, a 2x3 matrix represents a transformation from 3D space onto a 2D plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

#### From 2D to 1D (1x2 Matrix)

A transformation can also map 2D vectors to 1D vectors (numbers) <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. One-dimensional space is essentially the number line <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. For such a transformation, the visual intuition of linearity is that a line of evenly spaced dots in 2D would remain evenly spaced when mapped onto the number line <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

This transformation is encoded with a 1x2 matrix <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

*   The two columns represent where the 2D basis vectors land <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   Each column has a single entry, representing the single coordinate (number) each basis vector landed on <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

This type of transformation has significant ties to the dot product <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. Exploring the meanings of [[composition_of_linear_transformations | matrix multiplication]] and [[linear_transformations_in_linear_algebra | linear systems of equations]] in the context of transformations between different dimensions can be beneficial <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.