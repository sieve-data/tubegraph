---
title: Visual understanding of linear transformations
videoId: PFDu9oVAE-g
---

From: [[3blue1brown]] <br/> 
This article provides a visual understanding of linear transformations, particularly focusing on eigenvectors and eigenvalues, which are often considered unintuitive topics <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. A solid [[visual_intuition_of_linear_transformations | visual understanding]] of preceding topics, especially how to think about [[matrix_representation_of_linear_transformations | matrices as linear transformations]], is crucial for grasping these concepts <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Familiarity with determinants, linear systems of equations, and change of basis is also beneficial <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Special Vectors: Eigenvectors and Eigenvalues

When considering a [[linear_transformations_in_linear_algebra | linear transformation]] in two dimensions <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>, most vectors are "knocked off" their span (the line passing through their origin and tip) during the transformation <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. However, some special vectors remain on their own span <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The effect of the transformation on these vectors is simply to stretch or squish them, as if by a scalar <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

These special vectors are called **eigenvectors** <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Each eigenvector is associated with an **eigenvalue**, which is the factor by which it is stretched or squished <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

For example, in a transformation represented by a matrix with columns (3, 0) and (1, 2) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
*   The basis vector i-hat (on the x-axis) is an eigenvector <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Its span is the x-axis, and it moves to 3 times itself, remaining on the x-axis <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Any vector on the x-axis is also stretched by a factor of 3 <a class="yt="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This means 3 is an eigenvalue <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   The vector (-1, 1) is another eigenvector, getting stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Any vector on the diagonal line spanned by (-1, 1) is also stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This means 2 is an eigenvalue <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

Eigenvalues can be positive (stretching), negative (flipping and squishing, e.g., an eigenvalue of -1/2 would flip and squish by half) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The key property is that the eigenvector stays on its own span without getting rotated off it <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Applications of Eigenvectors and Eigenvalues

Understanding eigenvectors and eigenvalues offers a powerful way to interpret [[applications_and_examples_of_linear_transformations | linear transformations]]:
*   **Three-dimensional Rotations**: For a [[threedimensional_linear_transformations | three-dimensional rotation]], an eigenvector represents the axis of rotation <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This simplifies understanding the rotation to an axis and an angle, rather than a complex 3x3 matrix <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. In this case, the eigenvalue would be 1, as rotations don't stretch or squish <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Coordinate System Independence**: While the columns of a matrix show where basis vectors land <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>, eigenvectors and eigenvalues reveal the core action of a [[linear_transformations_in_linear_algebra | linear transformation]] in a way that is less dependent on the specific coordinate system <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Finding Eigenvectors and Eigenvalues

Symbolically, an eigenvector `v` of a transformation represented by matrix `A` satisfies `A * v = lambda * v`, where `lambda` is the eigenvalue <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This means the matrix-vector product `A * v` yields the same result as scaling `v` by `lambda` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

To find `v` and `lambda`, the equation is rewritten as `(A - lambda * I) * v = 0`, where `I` is the identity matrix <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. For a non-zero eigenvector `v`, the matrix `(A - lambda * I)` must squish space into a lower dimension, implying its determinant is zero <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

To find eigenvalues `lambda`:
1.  Subtract `lambda` from each diagonal entry of the matrix `A` <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
2.  Compute the determinant of the resulting matrix `(A - lambda * I)` <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
3.  Set the determinant equal to zero and solve for `lambda`. This polynomial's roots are the possible eigenvalues <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

To find eigenvectors `v` for a specific eigenvalue `lambda`:
1.  Plug the eigenvalue `lambda` back into the matrix `(A - lambda * I)` <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
2.  Solve for the non-zero vectors `v` that this matrix sends to zero (`(A - lambda * I) * v = 0`) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

#### Transformations Without Eigenvectors or With Limited Eigenvectors

*   **Rotation by 90 degrees**: This [[visualizing_transformations_with_vectors | transformation]] rotates every vector off its own span, so it has no real eigenvectors <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. When calculating its eigenvalues, the resulting polynomial (e.g., `lambda^2 + 1`) has only imaginary roots, indicating no real eigenvectors <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Shear**: A shear transformation (e.g., matrix columns (1,0) and (1,1)) fixes vectors on the x-axis in place, making them eigenvectors with eigenvalue 1 <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. In this case, these are the only eigenvectors, even though there's an entire line of them <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Scaling**: A matrix that scales everything by a factor (e.g., 2) has only one eigenvalue (e.g., 2), but every vector in the plane is an eigenvector with that eigenvalue <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

### The Eigenbasis

If a set of basis vectors also happen to be eigenvectors, the matrix representing the transformation in that basis will be a **diagonal matrix** <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. This means all entries are zero except for those on the diagonal, which are the eigenvalues corresponding to the basis vectors <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

Diagonal matrices are much easier to work with. For instance, computing a high power of a diagonal matrix (e.g., 100th power) simply involves raising each diagonal entry (eigenvalue) to that power <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

If a [[linear_transformations_in_linear_algebra | transformation]] has enough eigenvectors to span the full space, you can change your coordinate system to use these eigenvectors as new basis vectors <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. This is done using a change of basis matrix, where the eigenvectors form its columns <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. By "sandwiching" the original [[matrix_representations_of_linear_transformations | transformation matrix]] between the change of basis matrix and its inverse, the result is a diagonal matrix in the new coordinate system <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. A set of basis vectors that are also eigenvectors is called an **eigenbasis** <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. This transformation to an eigenbasis simplifies complex matrix operations like computing high powers of a matrix <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. However, not all transformations (like a shear) have enough eigenvectors to form an eigenbasis <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.