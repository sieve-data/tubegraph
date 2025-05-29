---
title: Eigenvectors in two and three dimensions
videoId: PFDu9oVAE-g
---

From: [[3blue1brown]] <br/> 

[[eigenvectors_and_eigenvalues | Eigenvectors and eigenvalues]] are a topic often found unintuitive by students, leading to unanswered questions about their purpose and meaning <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This difficulty often stems not from the inherent complexity of eigenthings, which are comparatively straightforward and well-explained in most books, but from a lack of solid visual understanding of preceding topics <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. A strong grasp of [[threedimensional_linear_transformations | matrices as linear transformations]], [[determinant_computation_for_2d_and_3d_transformations | determinants]], linear systems of equations, and [[concept_of_eigenbasis | change of basis]] is crucial <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Visualizing Eigenvectors in 2D

Consider a [[threedimensional_linear_transformations | linear transformation]] in two dimensions <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This transformation might move the [[unit_vectors_and_basis_vectors | basis vector]] i-hat to coordinates (3, 0) and j-hat to (1, 2), represented by a matrix with columns [3, 0] and [1, 2] <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

Most vectors are "knocked off their [[span_of_vectors_in_different_dimensions | span]]" (the line passing through its origin and its tip) during a transformation <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. It would seem coincidental for a vector to land on its original [[span_of_vectors_in_different_dimensions | span]] <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. However, some special vectors do remain on their own [[span_of_vectors_in_different_dimensions | span]] <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. For these vectors, the effect of the matrix is simply to stretch or squish them, like a scalar multiplication <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Examples of Eigenvectors in 2D

*   **i-hat**: In the given example, the [[unit_vectors_and_basis_vectors | basis vector]] i-hat is a special vector <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Its [[span_of_vectors_in_different_dimensions | span]] is the x-axis, and the transformation moves i-hat to 3 times itself, remaining on the x-axis <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Due to linearity, any other vector on the x-axis is also stretched by a factor of 3, staying on its [[span_of_vectors_in_different_dimensions | span]] <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **(-1, 1)**: Another vector that remains on its own [[span_of_vectors_in_different_dimensions | span]] for this transformation is (-1, 1) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. It gets stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Similarly, any vector on the diagonal line [[span_of_vectors_in_different_dimensions | spanned]] by (-1, 1) will also be stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

These special vectors are called the **[[eigenvectors_and_eigenvalues | eigenvectors]]** of the transformation <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Each [[eigenvectors_and_eigenvalues | eigenvector]] has an associated **[[eigenvectors_and_eigenvalues | eigenvalue]]**, which is the factor by which it's stretched or squished during the transformation <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Eigenvalues can be positive (stretching/squishing), or negative (flipping and squishing) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The crucial aspect is that the vector stays on its [[span_of_vectors_in_different_dimensions | span]] without getting rotated off <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Eigenvectors in 3D: The Axis of Rotation

For a [[threedimensional_linear_transformations | three-dimensional rotation]], finding an [[eigenvectors_and_eigenvalues | eigenvector]] (a vector that remains on its own [[span_of_vectors_in_different_dimensions | span]]) identifies the **axis of rotation** <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Thinking about a 3D rotation in terms of an axis and an angle is often much simpler than considering the full 3x3 matrix <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. For a pure rotation, the corresponding [[eigenvectors_and_eigenvalues | eigenvalue]] would be 1, as rotations do not stretch or squish vectors <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

Understanding a [[threedimensional_linear_transformations | linear transformation]] often benefits from finding its [[eigenvectors_and_eigenvalues | eigenvectors]] and [[eigenvectors_and_eigenvalues | eigenvalues]], as this provides a coordinate system-independent insight into what the transformation truly does <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

## Mathematical Definition and Computation

Symbolically, the idea of an [[eigenvectors_and_eigenvalues | eigenvector]] `v` for a transformation represented by matrix `A` and its corresponding [[eigenvectors_and_eigenvalues | eigenvalue]] `λ` is:

`Av = λv` <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>

This equation states that the matrix-vector product `A * v` yields the same result as simply scaling `v` by `λ` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. To solve for `v` and `λ`, the right-hand side `λv` can be rewritten as matrix-vector multiplication: `λIv`, where `I` is the identity matrix <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

This leads to:

`Av - λIv = 0` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>
`(A - λI)v = 0` <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>

We are looking for a non-zero [[eigenvectors_and_eigenvalues | eigenvector]] `v` <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. This is only possible if the [[threedimensional_linear_transformations | transformation]] associated with the matrix `(A - λI)` squishes space into a lower dimension <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This "squishification" corresponds to a zero [[determinant_computation_for_2d_and_3d_transformations | determinant]] for the matrix <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

So, to find the [[eigenvectors_and_eigenvalues | eigenvalues]] `λ`, we solve the **characteristic equation**:

`det(A - λI) = 0` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>

### Example: Finding Eigenvalues and Eigenvectors

Let's revisit the matrix from the beginning with columns [3, 0] and [1, 2] <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
To find its [[eigenvectors_and_eigenvalues | eigenvalues]], we subtract `λ` from the diagonal entries and compute the [[determinant_computation_for_2d_and_3d_transformations | determinant]]:

`det([[3-λ, 1], [0, 2-λ]]) = (3-λ)(2-λ) - (1)(0) = (3-λ)(2-λ)` <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>

Setting the [[determinant_computation_for_2d_and_3d_transformations | determinant]] to zero:
`(3-λ)(2-λ) = 0` <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>
The possible [[eigenvectors_and_eigenvalues | eigenvalues]] are `λ = 2` and `λ = 3` <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

To find the [[eigenvectors_and_eigenvalues | eigenvectors]] for `λ = 2`, plug `λ = 2` back into `(A - λI)v = 0`:

`([[3-2, 1], [0, 2-2]])v = 0`
`([[1, 1], [0, 0]])v = 0` <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>

Solving this system, you'll find that `v` must be a scalar multiple of (-1, 1) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. This confirms that vectors on the diagonal line [[span_of_vectors_in_different_dimensions | spanned]] by (-1, 1) are stretched by a factor of 2 <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

## Transformations Without Eigenvectors or With Special Eigenvectors

*   **Rotation by 90 degrees**: A 2D transformation doesn't have to have [[eigenvectors_and_eigenvalues | eigenvectors]] <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. For example, a 90-degree rotation rotates every vector off its own [[span_of_vectors_in_different_dimensions | span]] <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. Its matrix is [0, -1; 1, 0] <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. Computing `det(A - λI) = 0` yields `λ^2 + 1 = 0` <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. The only roots are imaginary numbers (i and -i), indicating no real [[eigenvectors_and_eigenvalues | eigenvectors]] <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **Shear**: A shear transformation fixes i-hat in place and moves j-hat one unit over, with a matrix of [1, 1; 0, 1] <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. All vectors on the x-axis are [[eigenvectors_and_eigenvalues | eigenvectors]] with [[eigenvectors_and_eigenvalues | eigenvalue]] 1, as they remain fixed <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. When computing `det(A - λI) = 0`, you get `(1-λ)^2 = 0`, meaning `λ = 1` is the only [[eigenvectors_and_eigenvalues | eigenvalue]] <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. This confirms that only eigenvectors with [[eigenvectors_and_eigenvalues | eigenvalue]] 1 exist <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Scaling Matrix**: A matrix that scales everything by 2 (e.g., [2, 0; 0, 2]) has only one [[eigenvectors_and_eigenvalues | eigenvalue]], `λ = 2` <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. However, every vector in the plane becomes an [[eigenvectors_and_eigenvalues | eigenvector]] for this [[eigenvectors_and_eigenvalues | eigenvalue]] <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.

## Eigenbasis

An **[[concept_of_eigenbasis | eigenbasis]]** occurs when the [[unit_vectors_and_basis_vectors | basis vectors]] themselves are [[eigenvectors_and_eigenvalues | eigenvectors]] <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. For example, if i-hat is scaled by -1 and j-hat by 2, the matrix's columns would be [-1, 0] and [0, 2] <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. The [[eigenvectors_and_eigenvalues | eigenvalues]] (-1 and 2) sit on the diagonal of the matrix, with all other entries being zero <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>. This is called a **diagonal matrix** <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

Diagonal matrices are simpler to work with <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. For instance, computing a high power of a diagonal matrix (e.g., 100 times) simply involves raising each diagonal [[eigenvectors_and_eigenvalues | eigenvalue]] to that power <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

If a [[threedimensional_linear_transformations | transformation]] has enough [[eigenvectors_and_eigenvalues | eigenvectors]] to [[span_of_vectors_in_different_dimensions | span]] the full space, you can perform a [[concept_of_eigenbasis | change of basis]] so that these [[eigenvectors_and_eigenvalues | eigenvectors]] become the new [[unit_vectors_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
The process involves:
1.  Creating a **change of basis matrix** by making the coordinates of the new [[eigenvectors_and_eigenvalues | eigenvector]] [[unit_vectors_and_basis_vectors | basis vectors]] its columns <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.
2.  "Sandwiching" the original transformation matrix between the change of basis matrix (on the right) and its inverse (on the left) <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
The resulting matrix in the new coordinate system will be diagonal, with the corresponding [[eigenvectors_and_eigenvalues | eigenvalues]] on the diagonal <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. This is incredibly useful for computations, such as computing matrix powers <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. Not all transformations, like a shear, have enough [[eigenvectors_and_eigenvalues | eigenvectors]] to [[span_of_vectors_in_different_dimensions | span]] the entire space, so an [[concept_of_eigenbasis | eigenbasis]] is not always possible <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.