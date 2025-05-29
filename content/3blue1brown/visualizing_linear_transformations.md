---
title: Visualizing linear transformations
videoId: PFDu9oVAE-g
---

From: [[3blue1brown]] <br/> 

Eigenvectors and eigenvalues are concepts that many students find unintuitive <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Understanding them visually requires a solid grasp of preceding topics, most importantly [[linear_transformations_and_matrices | matrices as linear transformations]] <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Familiarity with determinants, linear systems of equations, and change of basis is also crucial <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Confusion often stems from a shaky foundation in these prerequisite topics rather than the "eigenthings" themselves <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Special Vectors: Eigenvectors

Consider a [[linear_transformations | linear transformation]] in two dimensions, represented by a matrix with columns `3, 0` and `1, 2` <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a> <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a> <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. When a vector undergoes such a transformation, its "span" (the line passing through its origin and tip) typically changes <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a> <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

However, some special vectors remain on their own span after the transformation <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The effect of the matrix on these vectors is merely to stretch or squish them, as if by a scalar <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a> <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. These special vectors are called **eigenvectors** of the transformation <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a> <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

### Examples of Eigenvectors

*   For the example matrix `[[3, 1], [0, 2]]`, the basis vector i-hat (on the x-axis) is an eigenvector <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. It moves to `3` times itself, remaining on the x-axis <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a> <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. Due to the [[properties_of_linear_transformations | linearity]] of the transformation, any other vector on the x-axis will also be stretched by a factor of 3 and remain on its span <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a> <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a> <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   Another eigenvector for this transformation is `-1, 1` <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a> <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It gets stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Similarly, any vector on the diagonal line spanned by `-1, 1` will also be stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a> <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   For this specific transformation, these are the only lines of vectors that maintain their span; all other vectors are rotated off their line <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a> <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Eigenvalues

Each eigenvector has an associated **eigenvalue**, which is the factor by which it's stretched or squished during the transformation <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a> <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   Eigenvalues can be positive (stretching) or negative (flipping and squishing) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a> <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The key is that the vector remains on its span <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a> <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

## Why Eigenvectors are Useful

Eigenvectors and eigenvalues provide a powerful way to understand what a [[linear_transformations | linear transformation]] truly does, independent of the chosen coordinate system <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a> <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

For instance, when considering a [[threedimensional_linear_transformations | three-dimensional rotation]] <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a> <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>:
*   If you find an eigenvector, you have found the **axis of rotation** <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   Thinking about a 3D rotation in terms of an axis and an angle is much simpler than trying to understand the full 3x3 [[matrix_representation_of_linear_transformations | matrix representation]] of the transformation <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a> <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   For rotations, the corresponding eigenvalue must be `1`, as rotations do not stretch or squish vectors, preserving their length <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a> <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a> <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Computing Eigenvectors and Eigenvalues

Symbolically, the idea of an eigenvector `v` for a transformation represented by matrix `A` with corresponding eigenvalue `λ` is:
$Av = λv$ <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a> <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a> <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a> <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>

This equation states that the matrix-vector product `A * v` yields the same result as merely scaling the vector `v` by `λ` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a> <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

To solve for `v` and `λ`, the equation is rewritten:
1.  Rewrite the right side as matrix-vector multiplication by using an identity matrix `I`:
    $λv = λIv$ <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a> <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>
2.  Subtract `λIv` from both sides:
    $Av - λIv = 0$ <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>
3.  Factor out `v`:
    $(A - λI)v = 0$ <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a> <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>

For a non-zero eigenvector `v`, this equation implies that the transformation associated with the matrix `(A - λI)` must squish space into a lower dimension <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a> <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a> <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This "squishification" corresponds to the matrix `(A - λI)` having a zero determinant <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a> <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### Finding Eigenvalues
To find the eigenvalues `λ`:
1.  Compute the determinant of `(A - λI)` and set it to zero:
    $det(A - λI) = 0$ <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a> <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>

For the matrix `[[3, 1], [0, 2]]`:
*   `A - λI` becomes `[[3-λ, 1], [0, 2-λ]]` <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a> <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a> <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   The determinant is `(3 - λ)(2 - λ)` <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   Setting this to zero, `(3 - λ)(2 - λ) = 0`, gives the eigenvalues `λ = 2` and `λ = 3` <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a> <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

### Finding Eigenvectors
Once an eigenvalue `λ` is found, plug it back into `(A - λI)v = 0` and solve for `v` <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a> <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a> <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   For `λ = 2` in the example matrix `[[3, 1], [0, 2]]`:
    *   `(A - 2I)v = 0` becomes `[[1, 1], [0, 0]]v = 0` <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
    *   Solving this linear system shows that solutions are all vectors on the diagonal line spanned by `-1, 1` <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a> <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. This confirms that these vectors are stretched by a factor of 2 by the original matrix `A` <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a> <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

## Transformations Without Eigenvectors

Not all 2D [[linear_transformations | transformations]] have eigenvectors <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   A 90-degree rotation, for example, rotates every vector off its own span <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a> <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
*   When computing eigenvalues for a 90-degree rotation matrix `[[0, -1], [1, 0]]` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a> <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a> <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>, the determinant `det([[ -λ, -1], [1, -λ]]) = λ² + 1` <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a> <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. The roots of this polynomial are imaginary numbers (`i` and `-i`), indicating no real number solutions and thus no eigenvectors <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a> <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

## Transformations with Limited Eigenvectors

Some transformations might only have a limited set of eigenvectors.
*   A shear transformation (matrix `[[1, 1], [0, 1]]`), fixes i-hat in place and moves j-hat 1 unit over <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a> <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a> <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   All vectors on the x-axis are eigenvectors with eigenvalue `1` (they remain fixed) <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a> <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   When computing the determinant of `(A - λI)`, the result is `(1 - λ)²` <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a> <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The only root is `λ = 1` <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. This aligns with the geometric observation that all eigenvectors have an eigenvalue of `1` <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

## Transformations Where All Vectors are Eigenvectors

It's also possible to have just one eigenvalue but with more than a line full of eigenvectors <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a> <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   A matrix that scales everything by 2 <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.
*   The only eigenvalue is `2`, but every vector in the plane is an eigenvector with that eigenvalue <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a> <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

## Eigenbasis

An **eigenbasis** is a special set of basis vectors that are also eigenvectors of a transformation <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a> <a class="yt="yt-timestamp" data-t="00:13:06">[00:13:06]</a> <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a> <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.
*   If basis vectors happen to be eigenvectors (e.g., i-hat scaled by -1 and j-hat scaled by 2), the [[matrix_representation_of_transformations | matrix representation]] of the transformation becomes a **diagonal matrix** <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a> <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
*   In a diagonal matrix, the eigenvalues sit on the diagonal, and all other entries are zero <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a> <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a> <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a> <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. This means all basis vectors are eigenvectors, with their corresponding eigenvalues on the diagonal <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a> <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a> <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a> <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

### Advantages of Diagonal Matrices
Diagonal matrices are much easier to work with <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a> <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   Computing a matrix multiplied by itself many times (e.g., `A^100`) becomes straightforward <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. If a matrix simply scales each basis vector by its eigenvalue, applying it 100 times just scales each basis vector by the 100th power of its eigenvalue <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a> <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a> <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. This is a "nightmare" for non-diagonal matrices <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.

### Changing to an Eigenbasis
If a transformation has enough eigenvectors to span the full space, you can change your coordinate system so that these eigenvectors become your new basis vectors <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a> <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a> <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a> <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a> <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

The process of [[composition_of_linear_transformations | change of basis]] involves:
1.  Creating a **change of basis matrix** (P) whose columns are the coordinates of the new basis vectors (eigenvectors) <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a> <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a> <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a> <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
2.  "Sandwiching" the original transformation matrix `A` with the change of basis matrix and its inverse: `P⁻¹AP` <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a> <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a> <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
3.  The result `P⁻¹AP` will be a diagonal matrix, representing the same transformation from the perspective of the new eigenbasis <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a> <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a> <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. The diagonal entries will be the corresponding eigenvalues <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a> <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

This transformation to an eigenbasis allows for easier matrix operations, such as computing high powers of a matrix <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a> <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a> <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. However, not all transformations, like a shear, have enough eigenvectors to span the full space and form an eigenbasis <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a> <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a> <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.