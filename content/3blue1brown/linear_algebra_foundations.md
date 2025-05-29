---
title: Linear algebra foundations
videoId: PFDu9oVAE-g
---

From: [[3blue1brown]] <br/> 

Eigenvectors and eigenvalues are topics that many students find particularly unintuitive <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Common questions like "why are we doing this and what does this actually mean" are often left unanswered in computational contexts <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. While the concepts themselves are comparatively straightforward and generally well-explained in textbooks <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, understanding them requires a solid visual foundation in preceding linear algebra topics <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Prerequisites for Understanding
A strong grasp of certain foundational concepts is essential for understanding eigenvectors and eigenvalues:
*   Thinking about [[Linear transformations and matrices | matrices as linear transformations]] is most important <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Comfort with [[Understanding determinants in linear algebra | determinants]], linear systems of equations, and [[Matrix representation of linear transformations | change of basis]] is also necessary <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   Confusion about these concepts often stems from a shaky foundation in these prerequisite topics <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Geometric Intuition
Consider a [[Linear transformations and matrices | linear transformation]] in two dimensions <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   Most [[understanding_vectors_in_linear_algebra | vectors]] are "knocked off their span" (the line passing through their origin and tip) during a transformation <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   However, some special [[understanding_vectors_in_linear_algebra | vectors]] *do* remain on their own span <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   For these special [[understanding_vectors_in_linear_algebra | vectors]], the effect of the matrix is simply to stretch or squish them, akin to scalar multiplication <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

For example, with a transformation represented by the matrix with columns (3, 0) and (1, 2) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
*   The basis vector i-hat (on the x-axis) is such a special vector, moving to 3 times itself <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Due to linearity, any other vector on the x-axis is also stretched by a factor of 3 and remains on its span <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   Another special vector is (-1, 1), which gets stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Linearity implies any vector on the diagonal line spanned by (-1, 1) is also stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   For this transformation, these are the only vectors with this property; all others are rotated off their span <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

These special [[understanding_vectors_in_linear_algebra | vectors]] are called the **eigenvectors** of the transformation <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Each eigenvector has an associated **eigenvalue**, which is the factor by which it's stretched or squished <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Eigenvalues can be positive (stretching/squishing) or negative (flipping and squishing) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>, but the key is that the eigenvector stays on its own span <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Applications
Understanding eigenvectors and eigenvalues can simplify thinking about transformations:
*   For a three-dimensional rotation, finding an eigenvector reveals the axis of rotation <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. It is easier to describe a 3D rotation by its axis and angle than by a 3x3 matrix <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. For a pure rotation, the eigenvalue associated with the axis of rotation would be 1, as rotations do not stretch or squish <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   While a [[Linear transformations and matrices | linear transformation]] can be understood by its matrix columns (landing spots for basis vectors), finding eigenvectors and eigenvalues often provides a deeper understanding, less dependent on a particular [[coordinate systems in linear algebra | coordinate system]] <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Computational Approach
Symbolically, the idea of an eigenvector is represented by the equation:
`Av = λv` <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>
Where:
*   `A` is the matrix representing the transformation <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   `v` is the eigenvector <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   `λ` (lambda) is the eigenvalue, a number representing the scaling factor <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
This equation means that applying the matrix `A` to vector `v` (`Av`) yields the same result as simply scaling `v` by `λ` (`λv`) <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

To find `v` and `λ`, the equation is rearranged:
1.  Rewrite `λv` as a matrix-vector multiplication: `λI v`, where `I` is the identity matrix <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
2.  Subtract `λIv` from both sides: `Av - λIv = 0` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
3.  Factor out `v`: `(A - λI)v = 0` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
We are looking for non-zero eigenvectors `v` <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. A non-zero vector `v` is sent to the zero vector by a matrix `(A - λI)` only if the transformation associated with `(A - λI)` squishes space into a lower dimension <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This "squishification" corresponds to the [[Understanding determinants in linear algebra | determinant]] of the matrix being zero <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

Therefore, to find eigenvalues `λ`:
1.  Form the matrix `(A - λI)` by subtracting `λ` from each diagonal entry of `A` <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
2.  Set the [[Understanding determinants in linear algebra | determinant]] of `(A - λI)` equal to zero: `det(A - λI) = 0` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
3.  Solve the resulting polynomial equation for `λ`. The solutions are the eigenvalues <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
Once eigenvalues are found, substitute each `λ` back into `(A - λI)v = 0` and solve for `v` to find the corresponding eigenvectors <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### Cases without Eigenvectors
*   A [[Linear transformations and matrices | 2D transformation]] does not necessarily have eigenvectors <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   For example, a 90-degree rotation has no real eigenvectors because it rotates every vector off its own span <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. When computing eigenvalues for such a rotation (matrix columns 0, 1 and -1, 0), the polynomial `λ² + 1 = 0` is obtained, which only has imaginary roots (`i` and `-i`), indicating no real eigenvectors <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

### Cases with Specific Eigenvectors
*   **Shear transformation**: A shear (matrix columns 1, 0 and 1, 1) fixes i-hat in place <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. All vectors on the x-axis are eigenvectors with an eigenvalue of 1 (remaining fixed) <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. These are the only eigenvectors <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. Computing `det(A - λI) = 0` for a shear yields `(1 - λ)² = 0`, with only one root, `λ = 1` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Scaling matrix**: A matrix that scales everything by a factor (e.g., by 2, represented by a diagonal matrix with 2s on the diagonal) has only one eigenvalue (e.g., 2), but *every* vector in the plane is an eigenvector with that eigenvalue <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

### Eigenbasis
If a transformation has enough eigenvectors to span the full space, an **eigenbasis** can be formed <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   When basis vectors are eigenvectors (e.g., i-hat scaled by -1 and j-hat scaled by 2), their eigenvalues sit on the diagonal of the transformation matrix, with all other entries being zero <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. This is called a **diagonal matrix** <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
*   Diagonal matrices are much easier to work with; for instance, computing `A^100` for a diagonal matrix simply involves raising each diagonal eigenvalue to the 100th power <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   If a transformation has an eigenbasis (a set of basis vectors that are also eigenvectors), you can change the [[coordinate systems in linear algebra | coordinate system]] so that these eigenvectors become the new basis vectors <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
*   To express a transformation `A` in a new basis (whose vectors form the columns of a [[Matrix representation of linear transformations | change of basis]] matrix `P`), the new matrix is `P⁻¹AP` <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. When using an eigenbasis, this new matrix `P⁻¹AP` will be diagonal, with the corresponding eigenvalues on its diagonal <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
*   This process simplifies matrix operations like computing high powers of a matrix; it's easier to convert to an eigenbasis, compute the power in that system (which is diagonal), and then convert back <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
*   Not all transformations have an eigenbasis (e.g., a shear does not have enough eigenvectors to span the full space) <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

***

The next video in the series will cover abstract vector spaces <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.