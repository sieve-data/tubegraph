---
title: Matrix representations and transformations
videoId: PFDu9oVAE-g
---

From: [[3blue1brown]] <br/> 

[[linear_transformations | Linear transformations]] can be understood by considering how they affect space and, in particular, how they act on specific vectors within that space <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This perspective is crucial for grasping concepts like eigenvectors and eigenvalues <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Matrices as Linear Transformations
Matrices provide a [[matrix_representation_of_transformations | representation]] of [[linear_transformations | linear transformations]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. For a [[matrix_representation_of_transformations | matrix representation of a transformation]], its columns show where the basis vectors land after the transformation <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. For example, a transformation that moves the basis vector i-hat to (3, 0) and j-hat to (1, 2) is represented by a matrix with columns (3, 0) and (1, 2) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Eigenvectors and Eigenvalues
While most vectors are "knocked off" their original span (the line passing through their origin and tip) during a [[linear_transformations | linear transformation]], some special vectors remain on their span <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. The effect of the [[matrix_representation_of_transformations | matrix representation of the transformation]] on such vectors is merely to stretch or squish them, as if by a scalar factor <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

These special vectors are called **eigenvectors** of the transformation <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Each eigenvector has an associated **eigenvalue**, which is the factor by which it is stretched or squished <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. An eigenvalue can be positive (stretching), negative (flipping and stretching/squishing), or even zero (collapsing onto the origin) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The key property is that the vector stays on its span <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Examples of Eigenvectors and Eigenvalues
*   **Example 1 (2D Transformation)**: For a transformation where i-hat moves to (3,0) and j-hat to (1,2) (matrix columns are 3,0 and 1,2):
    *   The basis vector i-hat is an eigenvector <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Its span is the x-axis, and it moves to 3 times itself, remaining on the x-axis <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. The eigenvalue is 3 <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
    *   The vector (-1, 1) is also an eigenvector for this transformation <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. It gets stretched by a factor of 2, so its eigenvalue is 2 <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Example 2 ([[Threedimensional_linear_transformations | 3D Rotation]])**: For a [[Threedimensional_linear_transformations | three-dimensional rotation]], an eigenvector represents the axis of rotation <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Since rotations don't stretch or squish, the corresponding eigenvalue is 1 <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Example 3 (Rotation by 90 degrees)**: A 90-degree rotation has no real eigenvectors because every vector is rotated off its span <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. When calculating its eigenvalues, the solutions are imaginary numbers (i and -i), indicating no real eigenvectors <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **Example 4 (Shear Transformation)**: A shear transformation fixes the x-axis in place (eigenvalue 1) <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. These are the only eigenvectors for a shear, and the only eigenvalue is 1 <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Example 5 (Scaling Matrix)**: A matrix that scales everything by a factor (e.g., 2) has only one eigenvalue (e.g., 2), but *every* vector in the plane is an eigenvector with that eigenvalue <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

### Significance of Eigenvectors and Eigenvalues
Understanding a [[linear_transformations | linear transformation]] by finding its eigenvectors and eigenvalues can be more insightful and less dependent on the specific coordinate system than merely reading off the columns of its [[matrix_representation_of_transformations | matrix representation of a transformation]] <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Computing Eigenvectors and Eigenvalues
Symbolically, the idea of an eigenvector `v` and its eigenvalue `λ` for a transformation represented by matrix `A` is expressed as:
`A * v = λ * v` <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>

To find `v` and `λ` that satisfy this:
1.  Rewrite the right side using a matrix that scales any vector by `λ`. This is `λ` times the identity matrix (`λI`) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    `A * v = (λI) * v` <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>
2.  Rearrange the equation:
    `(A - λI) * v = 0` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>
3.  For a non-zero eigenvector `v` to satisfy this, the matrix `(A - λI)` must "squish" space into a lower dimension <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This condition corresponds to the determinant of `(A - λI)` being zero <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
    `det(A - λI) = 0` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>

Solving `det(A - λI) = 0` for `λ` yields the possible eigenvalues. Once an eigenvalue is found, it can be plugged back into `(A - λI) * v = 0` to solve for the corresponding eigenvectors `v` <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

## Eigenbasis and Diagonal Matrices
A matrix where all entries are zero except for the diagonal is called a **diagonal matrix** <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. In a diagonal matrix, the basis vectors themselves are eigenvectors, and their corresponding eigenvalues are the entries on the diagonal <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

Diagonal matrices are computationally convenient. For instance, computing a high power of a diagonal matrix (e.g., `A^100`) simply involves raising each diagonal entry (eigenvalue) to that power <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

### Changing to an Eigenbasis
If a transformation has enough eigenvectors to span the full space (i.e., you can choose a set of eigenvectors that form a basis), you can change your coordinate system to this **eigenbasis** <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a> <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

To do this, use a **change of basis matrix** (whose columns are the coordinates of the new basis vectors, which are your eigenvectors) <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. By "sandwiching" the original transformation matrix `A` between the inverse of the change of basis matrix `P⁻¹` and the change of basis matrix `P` (`P⁻¹AP`), the resulting matrix will be a diagonal matrix representing the same transformation from the perspective of the eigenbasis <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. The diagonal entries of this new matrix will be the eigenvalues <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

This transformation to an eigenbasis simplifies complex matrix operations, such as computing high powers of a matrix <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. However, not all transformations have enough eigenvectors to form an eigenbasis (e.g., a shear transformation) <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.