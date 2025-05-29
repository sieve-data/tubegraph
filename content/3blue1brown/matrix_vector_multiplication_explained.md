---
title: Matrix vector multiplication explained
videoId: kYB8IZa5AuE
---

From: [[3blue1brown]] <br/> 

## Understanding Linear Transformations

A **transformation** is essentially a function that takes inputs and produces outputs [00:00:47]. In linear algebra, transformations typically take a vector as input and output another vector [00:00:56]. The term "transformation" is used to suggest a visual understanding of this input-output relationship: an input vector can be imagined as *moving* to its output vector [00:01:07]. To understand the transformation as a whole, one can visualize every point in space moving to a new point [00:01:48]. Using an infinite grid helps to visualize the overall "squishing and morphing" of space [00:02:02].

Linear algebra focuses on a special type of transformation known as a **linear transformation** [00:02:30]. Visually, a transformation is linear if it possesses two key properties:
1.  All lines remain straight lines (without getting curved) [00:02:43].
2.  The origin remains fixed in place [00:02:46].

For instance, a transformation that causes lines to curve [00:02:50] or moves the origin [00:02:56] is not linear. Linear transformations are characterized by keeping grid lines parallel and evenly spaced [00:03:16].

### Describing Linear Transformations Numerically

A two-dimensional linear transformation can be fully described by observing where the two basis vectors, `i-hat` and `j-hat`, land after the transformation [00:03:48]. If a vector `v` is expressed as a linear combination of `i-hat` and `j-hat` (e.g., `v = -1 * i-hat + 2 * j-hat`), then after a linear transformation, `v` will land at the same linear combination of where `i-hat` and `j-hat` landed [00:04:19]. This means that the destination of any vector `v` can be deduced solely from the landing points of `i-hat` and `j-hat` [00:04:35].

For example, if `i-hat` lands at coordinates (1, -2) and `j-hat` lands at (3, 0) [00:04:45], then a vector `v` with original coordinates (-1, 2) (i.e., `-1 * i-hat + 2 * j-hat`) will transform to `-1 * (1, -2) + 2 * (3, 0)`, which results in the vector (5, 2) [00:04:55].

In a general case, for a vector with coordinates `(x, y)`, it will transform to `x` times the vector where `i-hat` lands, plus `y` times the vector where `j-hat` lands [00:05:38].

### Matrices and [[matrixvector_multiplication|Matrix-Vector Multiplication]]

A two-dimensional linear transformation is completely described by just four numbers: the two coordinates for where `i-hat` lands and the two coordinates for where `j-hat` lands [00:06:04]. These four numbers are commonly packaged into a 2x2 grid called a **matrix** [00:06:18]. The columns of this matrix represent the transformed `i-hat` and `j-hat` vectors [00:06:23].

For a matrix with entries `A, B, C, D`:
<a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>
*   The first column `[A; C]` represents where the first basis vector (`i-hat`) lands [00:07:06].
*   The second column `[B; D]` represents where the second basis vector (`j-hat`) lands [00:07:09].

When you apply this transformation to a vector `[x; y]`, the resulting vector is calculated as:
`x * [A; C] + y * [B; D] = [Ax + By; Cx + Dy]` <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>

This calculation is precisely the definition of [[matrixvector_multiplication|matrixvector multiplication]] when the matrix is placed to the left of the vector [00:07:33]. This approach emphasizes understanding the columns as transformed basis vectors and the result as an appropriate [[vector_addition_and_scalar_multiplication | linear combination]] of those vectors, rather than rote memorization [00:07:48].

#### Examples of Transformations Represented by Matrices

*   **90-degree Counterclockwise Rotation:**
    *   `i-hat` lands on (0, 1) [00:08:04].
    *   `j-hat` lands on (-1, 0) [00:08:13].
    *   Matrix: `[[0, -1], [1, 0]]` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>

*   **Shear Transformation:**
    *   `i-hat` remains fixed, so its landing coordinates are (1, 0) [00:08:35].
    *   `j-hat` moves to (1, 1) [00:08:39].
    *   Matrix: `[[1, 1], [0, 1]]` <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>

### Visualizing a Matrix's Transformation

Given a matrix, one can deduce its transformation by imagining `i-hat` and `j-hat` moving to the coordinates specified by the matrix's columns, while the rest of space moves to keep gridlines parallel and evenly spaced [00:09:08].

If the vectors that `i-hat` and `j-hat` land on are [[linear_dependence|linearly dependent]] (meaning one is a scaled version of the other), the linear transformation will "squish" all of 2D space onto the line where those two vectors sit [00:09:21]. This line is also known as the one-dimensional span of those two [[linear_dependence|linearly dependent]] vectors [00:09:36].

## Key Takeaway

<div class="callout">
    <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a> Every time you encounter a matrix, you can interpret it as a specific transformation of space.
</div>

This understanding of matrices as [[matrix_representation_of_linear_transformations|representations of linear transformations]] is crucial for deeply understanding linear algebra [00:10:22]. Topics such as [[associative_property_of_matrix_multiplication | matrix multiplication]], determinants, change of basis, and eigenvalues become much clearer when viewed through the lens of transformations [00:10:27].