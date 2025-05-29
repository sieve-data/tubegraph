---
title: Matrix vector multiplication
videoId: kYB8IZa5AuE
---

From: [[3blue1brown]] <br/> 

One foundational concept that illuminates linear algebra is the idea of a linear transformation and its relationship to matrices <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Focusing on two dimensions, this concept directly links to [[matrix_vector_multiplication_and_transformations | matrix vector multiplication]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Thinking about [[matrix_vector_multiplication_and_transformations | matrix vector multiplication]] in terms of transformations offers an intuitive understanding rather than rote memorization <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Understanding Transformations

A "transformation" is essentially a sophisticated term for a function <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. It processes inputs and generates a corresponding output for each <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. In linear algebra, transformations often take an input vector and produce another vector as output <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. The term "transformation" is used to suggest a visual way of understanding this input-output relationship, particularly through the concept of movement <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

When a transformation converts an input vector into an output vector, it can be visualized as the input vector "moving" to the position of the output vector <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. To grasp a transformation's overall effect, one might imagine every possible input vector moving to its new location <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

Instead of envisioning each vector as an arrow, a useful technique is to represent each vector as a single point, specifically where its tip rests <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This allows for visualizing a transformation as every point in space moving to a new point <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. For two-dimensional transformations, observing the movement of all points on an infinite grid, often with a copy of the original grid in the background, helps to understand the transformation's shape <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This visualization evokes the feeling of space itself being squished and morphed <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Linear Transformations

Linear algebra specifically deals with a simpler type of transformation called [[matrix_representation_of_linear_transformations | linear transformations]] <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

Visually, a transformation is considered linear if it satisfies two conditions <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>:
1.  All lines must remain straight lines, without curving <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
2.  The origin (0,0) must remain fixed in place <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

Examples of non-linear transformations include those that:
*   Cause lines to become curvy <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   Keep lines straight but move the origin <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   Appear to keep horizontal/vertical lines straight but curve diagonal lines <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

In general, [[matrix_representation_of_linear_transformations | linear transformations]] preserve the parallelism and even spacing of grid lines <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Simple examples include rotations about the origin <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

## Describing Linear Transformations with Matrices

To describe [[matrix_representation_of_linear_transformations | linear transformations]] numerically, for instance, in programming animations, you only need to record the final positions of the two basis vectors, i-hat and j-hat <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. All other vectors' movements can be derived from these two <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

Consider a vector `v` with coordinates (-1, 2), which can be written as -1 times i-hat plus 2 times j-hat <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Due to the properties of [[matrix_representation_of_linear_transformations | linear transformations]] (grid lines remaining parallel and evenly spaced), the transformed `v` will be -1 times the vector where i-hat landed, plus 2 times the vector where j-hat landed <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This means a vector's final position is the same linear combination of the transformed basis vectors as its original components were of the initial basis vectors <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

For example, if i-hat lands at (1, -2) and j-hat lands at (3, 0) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>:
A vector `v` = -1 * i-hat + 2 * j-hat <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
transforms to:
-1 * (1, -2) + 2 * (3, 0) = (-1, 2) + (6, 0) = (5, 2) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>

This principle allows us to deduce where any vector lands knowing only the landing spots of i-hat and j-hat, without needing to visualize the entire transformation <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

For a general vector (x, y), it will land at:
x * (where i-hat lands) + y * (where j-hat lands) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
If i-hat lands at (1, -2) and j-hat lands at (3, 0):
x * (1, -2) + y * (3, 0) = (x, -2x) + (3y, 0) = (x + 3y, -2x) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Matrices as Transformation Descriptors

A two-dimensional [[matrix_representation_of_linear_transformations | linear transformation]] is entirely defined by four numbers: the two coordinates where i-hat lands, and the two coordinates where j-hat lands <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. These coordinates are typically arranged into a 2x2 grid of numbers called a matrix <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. The columns of this matrix represent the landing spots of the i-hat and j-hat basis vectors <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

To find where a [[matrix_representation_of_linear_transformations | linear transformation]] (represented by a matrix) takes a specific vector, you multiply the vector's coordinates by the corresponding columns of the matrix and sum the results <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. This directly corresponds to adding the scaled versions of the new basis vectors <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

For a matrix with entries:
A B
C D

The first column (A, C) represents where i-hat lands, and the second column (B, D) represents where j-hat lands <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
When this matrix is applied to a vector (x, y), the result is:
x * (A, C) + y * (B, D) = (Ax + By, Cx + Dy) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
This is the definition of [[matrix_vector_multiplication_and_transformations | matrix vector multiplication]], where the matrix is placed to the left of the vector, acting like a function <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

> [!NOTE] Intuitive Understanding
> It's more intuitive to conceptualize matrix columns as the transformed basis vectors and the product as the appropriate [[vector_addition_and_scalar_multiplication | linear combination]] of those vectors <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## Examples of Matrix Vector Multiplication (Linear Transformations)

### Rotation
If all of space is rotated 90 degrees counterclockwise <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>:
*   i-hat lands on (0, 1) <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   j-hat lands on (-1, 0) <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
The corresponding matrix has columns (0, 1) and (-1, 0) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. To rotate any vector 90 degrees, you multiply its coordinates by this matrix <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

### Shear
In a shear transformation <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>:
*   i-hat remains fixed, so the first column of the matrix is (1, 0) <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   j-hat moves to (1, 1), which forms the second column of the matrix <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
Applying a shear to a vector involves [[matrix_vector_multiplication_and_transformations | multiplying this matrix]] by that vector <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Deducing Transformation from a Matrix
Given a matrix, for example, with columns (1, 2) and (3, 1), you can deduce its transformation by:
1.  Moving i-hat to (1, 2) <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
2.  Moving j-hat to (3, 1) <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
3.  Ensuring the rest of space moves in a way that keeps grid lines parallel and evenly spaced <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

If the vectors that i-hat and j-hat land on are [[understanding_vectors_in_linear_algebra | linearly dependent]] (one is a scaled version of the other), the [[matrix_representation_of_linear_transformations | linear transformation]] will squish all of 2D space onto the one-dimensional line spanned by those two vectors <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

## Conclusion

[[matrix_representation_of_linear_transformations | Linear transformations]] move space while keeping grid lines parallel and evenly spaced, and the origin fixed <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. These transformations can be described simply by the coordinates of where each basis vector lands <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. Matrices provide a language for describing these transformations, where their columns represent the transformed basis vectors <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. [[matrix_vector_multiplication_and_transformations | Matrix-vector multiplication]] is the computational method to determine how a transformation affects a given vector <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

A crucial takeaway is that every matrix can be interpreted as a specific transformation of space <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This fundamental understanding is key to grasping advanced topics in linear algebra, such as [[matrix_multiplication_and_transformations | matrix multiplication]], determinants, change of basis, and eigenvalues <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.