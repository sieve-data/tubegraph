---
title: linear transformations
videoId: XkY2DOUCWMU
---

From: [[3blue1brown]] <br/> 

## Introduction to Linear Transformations
[[Introduction to linear transformations | Linear transformations]] are functions that take vectors as inputs and produce vectors as outputs <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Visually, they can be understood as "smooshing" space such that grid lines remain parallel and evenly spaced, and the origin stays fixed <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

A key property of a [[linear_transformations_in_linear_algebra | linear transformation]] is that it is completely determined by where it moves the basis vectors of the space <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. In two dimensions, these are i-hat and j-hat <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Any other vector (x, y) can be expressed as a linear combination of these basis vectors (x times i-hat plus y times j-hat) <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. After a [[linear_transformations_and_linearity | linear transformation]], the transformed vector will be x times the transformed i-hat plus y times the transformed j-hat <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Matrix Representation
[[Matrix representations of linear transformations | Linear transformations are represented by matrices]] where the coordinates of where i-hat and j-hat land become the columns of the matrix <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Applying a [[linear_transformations_in_linear_algebra | linear transformation]] to a vector computationally means multiplying the matrix by that vector <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Composition of Linear Transformations
Often, it's necessary to describe the effect of applying one [[linear_transformations_in_linear_algebra | transformation]] and then another <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. For example, rotating a plane 90 degrees counterclockwise and then applying a shear <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. The overall effect of these successive actions is another distinct [[linear_transformations_in_linear_algebra | linear transformation]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This new [[linear_transformations_in_linear_algebra | linear transformation]] is called the [[composition of linear transformations | composition of the two separate transformations]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

Like any [[linear_transformations_in_linear_algebra | linear transformation]], the composite transformation can be described by its own matrix <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This is done by tracking the ultimate landing spots of i-hat and j-hat after both transformations <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. For instance, if i-hat ultimately lands at (1,1) and j-hat at (-1,0), the composite matrix would have columns `[1,1]` and `[-1,0]` respectively <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This new matrix captures the overall effect as a single action <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## Matrix Multiplication
The new matrix representing the [[composition of linear transformations | composition]] is the product of the original two matrices <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
To compute the product of two matrices, say M2 * M1 (meaning M1 is applied first, then M2):
1.  **Find where i-hat lands after M1**: This is given by the first column of M1 <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
2.  **Apply M2 to this transformed i-hat**: Multiply the M2 matrix by the vector that represents the transformed i-hat <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This result becomes the first column of the composite matrix <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
3.  **Repeat for j-hat**: Find where j-hat lands after M1 (second column of M1) <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
4.  **Apply M2 to this transformed j-hat**: Multiply the M2 matrix by this vector <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This result becomes the second column of the composite matrix <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

In general, the first column of the composite matrix (representing the [[composition of linear transformations | composition]] of A and B as AB) is the left matrix (A) multiplied by the first column of the right matrix (B) <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. Similarly, the second column is the left matrix (A) multiplied by the second column of the right matrix (B) <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### Order of Operations
When multiplying matrices to represent [[composition of linear transformations | composed transformations]], the order is read from right to left <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. The transformation represented by the matrix on the right is applied first, followed by the transformation represented by the matrix on the left <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This convention stems from function notation <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Properties of Matrix Multiplication
Understanding matrix multiplication geometrically, as applying one [[linear_transformations_in_linear_algebra | transformation]] after another, helps to comprehend its properties <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Non-Commutativity
The order of matrix multiplication generally matters <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. Applying a shear then a 90-degree rotation yields a different overall effect than applying a 90-degree rotation then a shear <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

### Associativity
Matrix multiplication is associative, meaning that for three matrices A, B, and C, (AB)C = A(BC) <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This property is trivial when viewed geometrically: it simply means applying C, then B, then A, which is the same regardless of how the operations are grouped <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

Playing around with imagining different [[applications_and_examples_of_linear_transformations | transformations]] and their compositions, then numerically working out the matrix products, can help solidify this understanding <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. The concepts can be extended beyond two dimensions to [[threedimensional_linear_transformations | three-dimensional linear transformations]] <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.