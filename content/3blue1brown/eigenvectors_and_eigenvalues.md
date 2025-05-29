---
title: Eigenvectors and eigenvalues
videoId: PFDu9oVAE-g
---

From: [[3blue1brown]] <br/> 

[[eigenvectors_in_two_and_three_dimensions | Eigenvectors and eigenvalues]] are topics that many students find unintuitive <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. A solid visual understanding of preceding topics, such as [[linear_transformations_in_linear_algebra | linear transformations]], [[determinant_properties_and_matrix_multiplication | determinants]], linear systems of equations, and [[concept_of_eigenbasis | change of basis]], is crucial for understanding eigenvectors and eigenvalues <a class="yt-timestamp" data-t="00:00:54">[00:01:02]</a>. Confusion often stems from a shaky foundation in these prerequisite areas rather than the concepts themselves <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## What are Eigenvectors and Eigenvalues?

Consider a [[linear_transformations_in_linear_algebra | linear transformation]] in two dimensions <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Most [[understanding_vectors | vectors]] will be "knocked off" their [[understanding_vectors | span]] (the line passing through their origin and tip) during a transformation <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. However, some special [[understanding_vectors | vectors]] remain on their own [[understanding_vectors | span]] <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This means the effect of the [[linear_transformations_in_linear_algebra | matrix]] on such a [[understanding_vectors | vector]] is simply to stretch or squish it, like a scalar <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

*   These special [[understanding_vectors | vectors]] are called **eigenvectors** <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   Each eigenvector has an associated **eigenvalue**, which is the factor by which it is stretched or squished during the transformation <a class="yt-timestamp" data-t="00:03:27">[00:03:31]</a>.

An eigenvalue can be positive, negative, or zero <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. For instance, an eigenvalue of negative one-half means the [[understanding_vectors | vector]] is flipped and squished by a factor of 0.5 <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The key characteristic is that the eigenvector stays on the line it spans without being rotated off it <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Examples

*   For a transformation represented by the [[matrixvector_multiplication | matrix]] with columns (3, 0) and (1, 2) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
    *   The [[unit_vectors_and_basis_vectors | basis vector]] *i-hat* (representing the x-axis) is an eigenvector <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. It moves to 3 times itself, remaining on the x-axis <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Its eigenvalue is 3 <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Due to linearity, any other [[understanding_vectors | vector]] on the x-axis is also stretched by a factor of 3 <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   The [[understanding_vectors | vector]] (-1, 1) is another eigenvector, getting stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Its eigenvalue is 2 <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Any [[understanding_vectors | vector]] on the diagonal line spanned by (-1, 1) also gets stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Significance

[[eigenvectors_in_two_and_three_dimensions | Eigenvectors]] and eigenvalues offer a way to understand [[linear_transformations_in_linear_algebra | linear transformations]] that is less dependent on the specific coordinate system <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

For example, in a [[basis_vectors_in_three_dimensions | three-dimensional rotation]], an eigenvector represents the axis of rotation <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Knowing the axis of rotation and the angle of rotation makes it much easier to conceptualize a 3D rotation than analyzing the full 3x3 [[matrixvector_multiplication | matrix]] <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. For a rotation, the corresponding eigenvalue would be 1, as rotations do not stretch or squish [[understanding_vectors | vectors]] <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Computing Eigenvectors and Eigenvalues

Symbolically, the idea of an eigenvector is represented as:
$A\mathbf{v} = \lambda\mathbf{v}$ <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>

Where:
*   $A$ is the [[linear_transformations_in_linear_algebra | matrix]] representing the transformation <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   $\mathbf{v}$ is the eigenvector <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   $\lambda$ (lambda) is the corresponding eigenvalue <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

This equation states that the [[matrixvector_multiplication | matrix-vector product]] $A\mathbf{v}$ yields the same result as simply scaling the eigenvector $\mathbf{v}$ by the value $\lambda$ <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

To solve for $\mathbf{v}$ and $\lambda$, the equation can be rewritten:
$A\mathbf{v} = \lambda I\mathbf{v}$ <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
$A\mathbf{v} - \lambda I\mathbf{v} = \mathbf{0}$ <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>
$(A - \lambda I)\mathbf{v} = \mathbf{0}$ <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>

Here, $I$ is the identity [[matrixvector_multiplication | matrix]], which scales any [[understanding_vectors | vector]] by a factor of $\lambda$ when multiplied by $\lambda$ <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

The goal is to find a non-zero eigenvector $\mathbf{v}$ <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. For the product of a [[linear_transformations_in_linear_algebra | matrix]] and a non-zero [[understanding_vectors | vector]] to be the zero [[understanding_vectors | vector]], the transformation associated with that [[linear_transformations_in_linear_algebra | matrix]] must squish space into a lower dimension <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This "squishification" corresponds to a zero [[determinant_computation_for_2d_and_3d_transformations | determinant]] for the [[linear_transformations_in_linear_algebra | matrix]] <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

Thus, to find eigenvalues, one must solve the characteristic equation:
$\det(A - \lambda I) = 0$ <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>

### Examples of Computation

*   **Original Example**: For the [[matrixvector_multiplication | matrix]] with columns (3, 0) and (1, 2) <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>:
    *   Subtract $\lambda$ from the diagonal entries and compute the [[determinant_computation_for_2d_and_3d_transformations | determinant]]: $(3 - \lambda)(2 - \lambda) = 0$ <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
    *   The eigenvalues are $\lambda = 2$ and $\lambda = 3$ <a class="yt-timestamp" data-t="00:09:50">[00:10:02]</a>.
    *   To find eigenvectors for $\lambda = 2$, plug it back into $(A - 2I)\mathbf{v} = \mathbf{0}$ and solve the [[linear_transformations_in_linear_algebra | linear system]] <a class="yt-timestamp" data-t="00:10:09">[00:10:14]</a>. The solutions are all [[understanding_vectors | vectors]] on the diagonal line spanned by (-1, 1) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

*   **Rotation by 90 degrees**:
    *   Its [[matrixvector_multiplication | matrix]] has columns (0, 1) and (-1, 0) <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
    *   The characteristic equation is $\det(A - \lambda I) = \lambda^2 + 1 = 0$ <a class="yt-timestamp" data-t="00:11:11">[00:11:18]</a>.
    *   The only roots are imaginary numbers ($i$ and $-i$) <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. The absence of real solutions indicates no real eigenvectors, which makes sense as a 90-degree rotation moves every [[understanding_vectors | vector]] off its own [[understanding_vectors | span]] <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

*   **Shear Transformation**:
    *   Its [[matrixvector_multiplication | matrix]] has columns (1, 0) and (1, 1) <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
    *   All [[understanding_vectors | vectors]] on the x-axis are eigenvectors with an eigenvalue of 1 (they remain fixed) <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
    *   The characteristic equation is $\det(A - \lambda I) = (1 - \lambda)^2 = 0$ <a class="yt-timestamp" data-t="00:11:58">[00:12:03]</a>.
    *   The only root is $\lambda = 1$ <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>, confirming that all eigenvectors for this transformation have an eigenvalue of 1 <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
    *   A shear transformation does not have enough eigenvectors to span the full space <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

*   **Scaling Matrix**:
    *   A [[matrixvector_multiplication | matrix]] that scales everything by 2 has only one eigenvalue, $\lambda = 2$ <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.
    *   However, every [[understanding_vectors | vector]] in the plane is an eigenvector with that eigenvalue <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.

## Eigenbasis

A **diagonal [[matrixvector_multiplication | matrix]]** is one where all entries other than the diagonal are zeros <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. In a diagonal [[matrixvector_multiplication | matrix]], all [[unit_vectors_and_basis_vectors | basis vectors]] are eigenvectors, and their eigenvalues are the diagonal entries <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

Diagonal matrices are advantageous because they simplify operations like computing matrix powers <a class="yt-timestamp" data-t="00:13:57">[00:14:01]</a>. Applying a diagonal [[matrixvector_multiplication | matrix]] multiple times (e.g., 100 times) simply scales each [[unit_vectors_and_basis_vectors | basis vector]] by the 100th power of its corresponding eigenvalue <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

An **eigenbasis** is a set of [[unit_vectors_and_basis_vectors | basis vectors]] that are also eigenvectors <a class="yt-timestamp" data-t="00:15:55">[00:15:59]</a>. If a transformation has enough eigenvectors to span the full space, one can perform a [[concept_of_eigenbasis | change of basis]] to use these eigenvectors as the new [[unit_vectors_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:14:42">[00:14:49]</a>.

To express a [[linear_transformations_in_linear_algebra | transformation]] in a different coordinate system (one formed by eigenvectors) <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>:
1.  Form a **change of basis matrix** ($P$) using the coordinates of the eigenvectors as its columns <a class="yt-timestamp" data-t="00:15:08">[00:15:14]</a>.
2.  "Sandwich" the original transformation [[matrixvector_multiplication | matrix]] ($A$) between the inverse of the change of basis matrix ($P^{-1}$) and the change of basis matrix ($P$) <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>: $P^{-1}AP$.

The resulting [[matrixvector_multiplication | matrix]] will be diagonal, with the corresponding eigenvalues on its diagonal <a class="yt-timestamp" data-t="00:15:37">[00:15:41]</a>. This makes complex [[matrixvector_multiplication | matrix]] operations, like computing high powers of a [[matrixvector_multiplication | matrix]], much simpler by converting to an eigenbasis, performing the operation, and then converting back <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.