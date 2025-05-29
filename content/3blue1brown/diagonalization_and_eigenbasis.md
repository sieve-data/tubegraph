---
title: Diagonalization and eigenbasis
videoId: PFDu9oVAE-g
---

From: [[3blue1brown]] <br/> 

[[eigenvectors_and_eigenvalues | Eigenvectors and eigenvalues]] is a topic that many students find unintuitive, often leaving questions about its purpose unanswered in a sea of computations <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. A solid visual understanding of preceding topics is crucial for making sense of it <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Key foundational concepts include thinking about matrices as linear transformations, comfort with [[understanding_determinants_in_linear_algebra | determinants]], linear systems of equations, and [[change_of_basis_and_its_implications | change of basis]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Confusion often stems from a [[linear_algebra_foundations | shaky foundation]] in these areas rather than the eigen-concepts themselves <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Understanding Eigenvectors and Eigenvalues

Consider a linear transformation in two dimensions <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Most vectors are "knocked off" their span (the line passing through their origin and tip) during a transformation <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. However, some special vectors remain on their own span <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The effect of the matrix on such a vector is simply to stretch or squish it, like a scalar multiplication <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

These special vectors are called **eigenvectors** of the transformation <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Each eigenvector has an associated **eigenvalue**, which is the factor by which it's stretched or squished <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. An eigenvalue can be negative, meaning the vector is flipped and squished <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The crucial point is that it stays on the line it spans without getting rotated off <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

For example:
*   In a 2D transformation represented by a matrix with columns `(3,0)` and `(1,2)`:
    *   The [[Basis vectors in threedimensional space | basis vector]] i-hat (representing the x-axis) is an eigenvector with an eigenvalue of 3, as it moves to 3 times itself <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Any other vector on the x-axis is also stretched by a factor of 3 <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
    *   The vector `(-1,1)` is another eigenvector, stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Any vector on the diagonal line spanned by `(-1,1)` also gets stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

In a 3D rotation, finding an eigenvector reveals the axis of rotation, which simplifies understanding the transformation compared to a full 3x3 matrix <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. For a rotation, the corresponding eigenvalue would be 1, as rotations do not stretch or squish vectors <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

Finding eigenvectors and eigenvalues often provides a better understanding of a linear transformation, less dependent on the particular [[coordinate systems in linear algebra | coordinate system]] <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Computing Eigenvalues and Eigenvectors

Symbolically, the idea of an eigenvector `v` for a matrix `A` with a corresponding eigenvalue `λ` is represented as:
`A v = λ v` <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>

To solve this, the right-hand side `λv` can be rewritten as matrix-vector multiplication `(λI)v`, where `I` is the identity matrix <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. This leads to:
`A v - λ I v = 0`
`(A - λI) v = 0` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>

For a non-zero eigenvector `v` to satisfy this equation, the transformation associated with the matrix `(A - λI)` must squish space into a lower dimension <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. This "squishification" corresponds to a zero [[understanding_determinants_in_linear_algebra | determinant]] for the matrix `(A - λI)` <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

The process involves:
1.  Subtracting `λ` from each diagonal entry of matrix `A` to form `(A - λI)` <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
2.  Setting the [[computing_determinants_for_2D_and_3D_transformations | determinant]] of `(A - λI)` to zero: `det(A - λI) = 0` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
3.  Solving this characteristic polynomial for `λ` to find the eigenvalues <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
4.  For each eigenvalue `λ`, plug it back into `(A - λI)v = 0` and solve for `v` to find the corresponding eigenvectors <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

**Example**: For a 90-degree rotation, the matrix has columns `(0,1)` and `(-1,0)` <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. Computing `det(A - λI) = 0` yields `λ² + 1 = 0` <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. The roots are imaginary numbers (`i` and `-i`), indicating no real number solutions, and thus no eigenvectors <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. Geometrically, this makes sense as every vector is rotated off its span <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

Some transformations, like a shear, might have only one eigenvalue but a line full of eigenvectors <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. Conversely, a transformation that scales everything (e.g., by 2) has only one eigenvalue (2), but *every* vector in the plane is an eigenvector <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

## Diagonalization and Eigenbasis

A **diagonal matrix** is one with zeros everywhere except along its diagonal <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. If the [[Coordinate systems and basis vectors | basis vectors]] themselves happen to be eigenvectors, their eigenvalues will sit on the diagonal of the matrix representing the transformation <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. This means all basis vectors are eigenvectors, with the diagonal entries being their eigenvalues <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

Diagonal matrices are particularly useful because they simplify computations, especially for calculating high powers of a matrix <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. Applying a diagonal matrix multiple times simply means scaling each basis vector by the corresponding eigenvalue raised to that power <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

An **eigenbasis** is a set of basis vectors that are also eigenvectors for a transformation <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. While it's rare for standard basis vectors to be eigenvectors, if a transformation has enough eigenvectors to span the entire space, you can perform a [[change_of_basis_and_its_implications | change of basis]] <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

To represent a transformation `A` in a new [[coordinate systems in linear algebra | coordinate system]] defined by eigenvectors `v1, v2,...vn` (which form the columns of a [[change_of_basis_and_its_implications | change of basis]] matrix `P`):
`A' = P⁻¹ A P` <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>

The resulting matrix `A'` will be diagonal, with the corresponding eigenvalues along its diagonal <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. This process is called **diagonalization**. This new matrix represents the transformation from the perspective of the eigenbasis, where the basis vectors simply get scaled <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

Diagonalization is immensely helpful for complex matrix operations, such as computing the 100th power of a matrix <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>. Instead of directly computing `A^100`, one can:
1.  Change to an eigenbasis (using `P`).
2.  Compute the power in that simpler, diagonal system (`(A')^100`).
3.  Convert back to the standard system (using `P⁻¹`).

Not all transformations can be diagonalized; for instance, a shear transformation does not have enough eigenvectors to span the full space <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. However, when an eigenbasis can be found, it significantly simplifies matrix operations <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.