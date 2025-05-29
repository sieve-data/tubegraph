---
title: Applications and examples of linear transformations
videoId: kYB8IZa5AuE
---

From: [[3blue1brown]] <br/> 

[[linear transformations | Linear transformations]] are a foundational concept in linear algebra, often considered the single most important topic for understanding others within the field <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. They provide a visual and intuitive way to understand how matrices operate <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## What is a Transformation?
A transformation is fundamentally a sophisticated term for a function <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. It takes inputs and produces an output for each <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. In the context of linear algebra, transformations typically take a vector as input and output another vector <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

The word "transformation" is used to suggest a visual way of understanding this input-output relationship <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. By imagining an input vector "moving" to its output vector, one can conceptualize the transformation as a whole by visualizing all possible input vectors moving to their corresponding outputs <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Instead of thinking of vectors as arrows, it's often clearer to visualize them as single points—the tip of the arrow <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This allows for the visualization of every point in space moving to another point <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

For [[visual understanding of linear transformations | two-dimensional linear transformations]], visualizing the movement of an infinite grid of points helps grasp the overall shape of the transformation <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Keeping a copy of the original grid in the background can help track relative movements <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This visualization gives the impression of space itself being "squished and morphed" <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Properties of Linear Transformations
[[linear transformations | Linear transformations]] are a specific type of transformation <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Visually, a transformation is linear if it satisfies two conditions <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>:
1.  All lines must remain lines; they do not get curved <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
2.  The origin `(0,0)` must remain fixed in place <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

Examples of non-linear transformations include those where lines become curvy <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>, or where the origin moves <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. A key characteristic of [[linear transformations | linear transformations]] is that they keep grid lines parallel and evenly spaced <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Describing Linear Transformations Numerically with Matrices
A [[linear transformations | two-dimensional linear transformation]] is entirely defined by where its two basis vectors, `i-hat` and `j-hat`, land <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This is because any vector `v` can be expressed as a linear combination of `i-hat` and `j-hat` (e.g., `v = x * i-hat + y * j-hat`) <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Due to the properties of [[linear transformations | linear transformations]] (keeping grid lines parallel and evenly spaced), the transformed vector `v'` will be the same linear combination of the transformed `i-hat` and `j-hat` vectors <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

[!NOTE]
If `v = x * i-hat + y * j-hat`, and `T` is a linear transformation, then `T(v) = x * T(i-hat) + y * T(j-hat)` <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

This means that if you know where `i-hat` and `j-hat` land, you can deduce where any vector `v` will land under that transformation <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

### Matrices as Representations of Linear Transformations
The coordinates of where `i-hat` and `j-hat` land can be packaged into a 2x2 grid of numbers called a 2x2 matrix <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   The first column of the matrix represents the coordinates where `i-hat` lands <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   The second column of the matrix represents the coordinates where `j-hat` lands <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

Given a matrix `M = [[A, B], [C, D]]` representing a linear transformation, and a vector `v = [x, y]`, the transformed vector `v'` is calculated by matrix-vector multiplication <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>:
`M * v = x * [A, C] + y * [B, D] = [Ax + By, Cx + Dy]` <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
This multiplication is the mathematical way of computing the scaled sum of the transformed basis vectors <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

## Examples of Linear Transformations

### 1. Rotation
A rotation of all space 90 degrees counterclockwise around the origin <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>:
*   `i-hat` lands on `(0, 1)` <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   `j-hat` lands on `(-1, 0)` <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
The matrix for this transformation is `[[0, -1], [1, 0]]` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

### 2. Shear
A shear transformation <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>:
*   `i-hat` remains fixed at `(1, 0)` <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   `j-hat` moves to `(1, 1)` <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
The matrix for this transformation is `[[1, 1], [0, 1]]` <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### 3. Transformation from a Given Matrix
Given a matrix `M = [[1, 3], [2, 1]]` <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>:
*   `i-hat` lands on `(1, 2)` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   `j-hat` lands on `(3, 1)` <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
The transformation moves `i-hat` to `(1, 2)` and `j-hat` to `(3, 1)`, while keeping grid lines parallel and evenly spaced <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

### Special Case: Linearly Dependent Basis Vectors
If the vectors where `i-hat` and `j-hat` land are linearly dependent (meaning one is a scaled version of the other) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>, the linear transformation will squish all of 2D space onto a single line <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This line is the one-dimensional span of those two linearly dependent vectors <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

## Conclusion
[[linear transformations | Linear transformations]] are defined as transformations of space that keep grid lines parallel and evenly spaced, and the origin fixed <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. They can be fully described by the coordinates of where the basis vectors `i-hat` and `j-hat` land <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Matrices provide a language to describe these transformations, where the columns represent the transformed basis vectors <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. [[linear transformations | Matrix-vector multiplication]] is simply the computation of what a transformation does to a given vector <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

Every time a matrix is encountered, it can be interpreted as a specific transformation of space <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. This understanding is crucial for deeply comprehending many advanced topics in linear algebra, including [[composition of linear transformations | matrix multiplication]], determinants, change of basis, and eigenvalues <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.