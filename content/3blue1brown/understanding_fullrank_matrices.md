---
title: Understanding fullrank matrices
videoId: v8VSDg_WQlA
---

From: [[3blue1brown]] <br/> 

When discussing [[Linear transformations in linear algebra | linear transformations]], it's common to consider transformations between spaces of the same dimension, such as 2D to 2D or 3D to 3D, represented by square matrices (e.g., 2x2 or 3x3 matrices) <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. However, [[Matrix representations of linear transformations | transformations]] can also occur between spaces of different dimensions, which are represented by non-square matrices <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.

## Non-Square Matrix Representations

A transformation is considered linear if grid lines remain parallel and evenly spaced, and the origin maps to the origin <a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a>. Encoding these transformations with a matrix involves looking at where each basis vector lands and writing its coordinates as the columns of the matrix <a class="yt-timestamp" data-t="01:21:21">[01:21:21]</a>.

### 3x2 Matrices: 2D to 3D Transformations

A 3x2 matrix (three rows, two columns) geometrically interprets as mapping two dimensions to three dimensions <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>.
*   The two columns indicate that the input space has two basis vectors, originating from a 2D space <a class="yt-timestamp" data-t="02:25:25">[02:25:25]</a>.
*   The three rows indicate that the landing spots for each of these basis vectors are described with three separate coordinates, placing them in 3D space <a class="yt-timestamp" data-t="02:29:29">[02:29:29]</a>.

For example, a transformation might take the 2D basis vector i-hat to coordinates (2, -1, -2) and j-hat to (0, 1, 1) <a class="yt-timestamp" data-t="01:33:33">[01:33:33]</a>. The *output* of this transformation results in 3D vectors from 2D vector inputs, which are considered "completely separate, unconnected space[s]" <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>.

The [[rank of a matrix | column space]] of such a 3x2 matrix — the space where all the vectors land — would be a 2D plane slicing through the origin of 3D space <a class="yt-timestamp" data-t="01:57:57">[01:57:57]</a>.

### 2x3 Matrices: 3D to 2D Transformations

Conversely, a 2x3 matrix (two rows, three columns) represents a transformation from three dimensions to two dimensions <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>.
*   The three columns indicate a starting space with three basis vectors (3D input) <a class="yt-timestamp" data-t="02:43:43">[02:43:43]</a>.
*   The two rows indicate that the landing spot for each of those three basis vectors is described with only two coordinates (2D output) <a class="yt-timestamp" data-t="02:50:50">[02:50:50]</a>.

This type of transformation maps 3D space onto a 2D plane <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### 1x2 Matrices: 2D to 1D Transformations

A 1x2 matrix (one row, two columns) represents a transformation from two dimensions to one dimension <a class="yt-timestamp" data-t="03:13:13">[03:13:13]</a>. One-dimensional space is effectively a number line <a class="yt-timestamp" data-t="03:17:17">[03:17:17]</a>, meaning this transformation takes 2D vectors and outputs single numbers <a class="yt-timestamp" data-t="03:20:20">[03:20:20]</a>.
*   The two columns signify where the two basis vectors land <a class="yt-timestamp" data-t="03:50:50">[03:50:50]</a>.
*   Each column has a single entry, representing the number on the number line where the basis vector landed <a class="yt-timestamp" data-t="03:53:53">[03:53:53]</a>.
For linearity in this context, a line of evenly spaced dots in the input space would remain evenly spaced when mapped onto the number line <a class="yt-timestamp" data-t="03:33:33">[03:33:33]</a>.

## Understanding Full Rank

For a matrix representing a transformation, it is considered **full rank** if the number of dimensions in its [[rank of a matrix | column space]] is the same as the number of dimensions of the input space <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>.

For instance, the 3x2 matrix example, which maps 2D input vectors to a 2D plane within 3D space, is full rank because the column space (a 2D plane) has the same number of dimensions (two) as the input space (2D) <a class="yt-timestamp" data-t="01:57:57">[01:57:57]</a>.