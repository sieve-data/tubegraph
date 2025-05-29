---
title: Eigenvectors and eigenvalues
videoId: PFDu9oVAE-g
---

From: [[3blue1brown]] <br/> 

## Introduction to Eigen-concepts

[[Eigenvectors and eigenvalues]] are concepts in linear algebra that many find unintuitive, often leaving questions about their purpose and meaning unanswered <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. While not inherently complicated, understanding them requires a solid visual grasp of preceding topics <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Key foundational knowledge includes viewing [[matrices_and_their_properties | matrices]] as [[matrices_and_their_properties | linear transformations]], comfort with [[understanding_determinants_in_linear_algebra | determinants]], linear systems of equations, and [[representation_of_vectors_using_basis_vectors | change of basis]] <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Geometric Definition

Consider a [[matrices_and_their_properties | linear transformation]] in two dimensions <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. When a [[understanding_vectors_in_linear_algebra | vector]] undergoes this transformation, it usually gets "knocked off its span" (the line passing through its origin and tip) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

However, some special [[understanding_vectors_in_linear_algebra | vectors]] remain on their own span <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. For these [[understanding_vectors_in_linear_algebra | vectors]], the effect of the [[matrices_and_their_properties | matrix]] is simply to stretch or squish them, like a scalar multiplication <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

*   **Eigenvectors**: These special [[understanding_vectors_in_linear_algebra | vectors]] that remain on their own span after a transformation are called the eigenvectors of the transformation <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Eigenvalues**: Associated with each eigenvector is an eigenvalue, which is the factor by which the eigenvector is stretched or squished during the transformation <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Eigenvalues can be positive (stretching), negative (flipping and stretching/squishing), or fractional (squishing) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The crucial point is that the eigenvector stays on the line it spans without being rotated off <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Examples of Eigenvectors and Eigenvalues

*   For a [[matrices_and_their_properties | matrix]] where [[basis_vectors | i-hat]] moves to (3,0) and [[basis_vectors | j-hat]] to (1,2) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>:
    *   The [[basis_vectors | basis vector]] [[basis_vectors | i-hat]] (the x-axis) is an eigenvector because it moves to 3 times itself, remaining on the x-axis <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Its eigenvalue is 3 <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
    *   The [[understanding_vectors_in_linear_algebra | vector]] (-1,1) is also an eigenvector, getting stretched by a factor of 2 <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Its eigenvalue is 2 <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Application in 3D Rotations**: If you can find an eigenvector for a three-dimensional rotation, you have found the axis of rotation <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This simplifies understanding 3D rotations from a complex [[matrices_and_their_properties | matrix]] to an axis and an angle <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. For rotations, the eigenvalue would be 1, as lengths are preserved <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

Finding eigenvectors and eigenvalues often provides a deeper understanding of a [[matrices_and_their_properties | linear transformation]] that is less dependent on the specific coordinate system used <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Symbolic Representation and Computation

The idea of an eigenvector is expressed symbolically as:
$A\mathbf{v} = \lambda\mathbf{v}$ <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>

Where:
*   $A$ is the [[matrices_and_their_properties | matrix]] representing the transformation <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   $\mathbf{v}$ is the eigenvector <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   $\lambda$ (lambda) is a number, the corresponding eigenvalue <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

This equation states that applying the [[matrices_and_their_properties | matrix]] $A$ to [[understanding_vectors_in_linear_algebra | vector]] $\mathbf{v}$ yields the same result as simply scaling $\mathbf{v}$ by $\lambda$ <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

To find $\mathbf{v}$ and $\lambda$ that satisfy this expression, we manipulate the equation:

1.  Rewrite the right-hand side using a [[matrices_and_their_properties | matrix]] that scales any [[understanding_vectors_in_linear_algebra | vector]] by $\lambda$. This is the identity [[matrices_and_their_properties | matrix]] $I$ multiplied by $\lambda$, written as $\lambda I$ <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    $A\mathbf{v} = \lambda I\mathbf{v}$ <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>
2.  Subtract $\lambda I\mathbf{v}$ from both sides and factor out $\mathbf{v}$:
    $(A - \lambda I)\mathbf{v} = \mathbf{0}$ <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>

We are looking for a non-zero eigenvector $\mathbf{v}$ <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. For the product of a [[matrices_and_their_properties | matrix]] and a non-zero [[understanding_vectors_in_linear_algebra | vector]] to be the zero [[understanding_vectors_in_linear_algebra | vector]], the [[matrices_and_their_properties | transformation]] associated with that [[matrices_and_their_properties | matrix]] must squish space into a lower dimension <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This "squishification" corresponds to the [[understanding_determinants_in_linear_algebra | determinant]] of the [[matrices_and_their_properties | matrix]] being zero <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

Therefore, to find eigenvalues $\lambda$, we solve the characteristic equation:
$\text{det}(A - \lambda I) = 0$ <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>

### Example of Computation

For the [[matrices_and_their_properties | matrix]] $A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$ <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>:

1.  Form $A - \lambda I$:
    $A - \lambda I = \begin{pmatrix} 3 - \lambda & 1 \\ 0 & 2 - \lambda \end{pmatrix}$ <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>
2.  Compute the [[understanding_determinants_in_linear_algebra | determinant]] and set it to zero:
    $\text{det}(A - \lambda I) = (3 - \lambda)(2 - \lambda) - (1)(0) = (3 - \lambda)(2 - \lambda) = 0$ <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>
3.  Solve for $\lambda$:
    This yields $\lambda = 2$ and $\lambda = 3$ as the only possible eigenvalues <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
4.  To find eigenvectors for a specific eigenvalue (e.g., $\lambda = 2$):
    Plug $\lambda = 2$ back into $(A - \lambda I)\mathbf{v} = \mathbf{0}$:
    $\begin{pmatrix} 3 - 2 & 1 \\ 0 & 2 - 2 \end{pmatrix}\mathbf{v} = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}\mathbf{v} = \mathbf{0}$ <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>
    Solving this linear system shows that solutions are all [[understanding_vectors_in_linear_algebra | vectors]] on the diagonal line spanned by (-1,1) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. This confirms that these are the eigenvectors associated with eigenvalue 2 <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

## Cases Without Eigenvectors

Not all [[matrices_and_their_properties | transformations]] have eigenvectors.

*   **Rotation**: A 90-degree rotation, for example, rotates every [[understanding_vectors_in_linear_algebra | vector]] off its own span <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. When computing eigenvalues for such a rotation [[matrices_and_their_properties | matrix]] (columns (0,1) and (-1,0)), the characteristic equation results in $\lambda^2 + 1 = 0$ <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. The roots are imaginary numbers ($i$ and $-i$), indicating no real number solutions and thus no real eigenvectors <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **Shear**: A shear [[matrices_and_their_properties | transformation]] (e.g., [[matrices_and_their_properties | matrix]] with columns (1,0) and (1,1)) has all [[understanding_vectors_in_linear_algebra | vectors]] on the x-axis as eigenvectors with an eigenvalue of 1 (they remain fixed) <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. However, these are the *only* eigenvectors <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. The characteristic equation yields $(1-\lambda)^2=0$, meaning $\lambda=1$ is the only eigenvalue <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   **Scaling**: A [[matrices_and_their_properties | matrix]] that scales everything by a factor (e.g., by 2) has only one eigenvalue (2), but *every* [[understanding_vectors_in_linear_algebra | vector]] in the plane is an eigenvector with that eigenvalue <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

## Eigenbasis

An [[diagonalization_and_eigenbasis | eigenbasis]] is a set of [[basis_vectors | basis vectors]] that are also eigenvectors of a [[matrices_and_their_properties | transformation]] <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

*   **Diagonal Matrices**: If [[basis_vectors | basis vectors]] happen to be eigenvectors, the [[matrices_and_their_properties | matrix]] representing the transformation will have its eigenvalues on the diagonal and zeros everywhere else <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. Such a [[matrices_and_their_properties | matrix]] is called a [[diagonalization_and_eigenbasis | diagonal matrix]] <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
*   **Benefits of Diagonal Matrices**: [[diagonalization_and_eigenbasis | Diagonal matrices]] are much easier to work with <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. For example, computing the 100th power of a [[diagonalization_and_eigenbasis | diagonal matrix]] simply involves raising each diagonal entry (eigenvalue) to the 100th power <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. This is significantly simpler than computing powers of non-diagonal [[matrices_and_their_properties | matrices]] <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Changing to an Eigenbasis**: If a [[matrices_and_their_properties | transformation]] has enough eigenvectors to span the full space, you can change your coordinate system so that these eigenvectors become your new [[basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
    *   This is done by using a "change of basis [[matrices_and_their_properties | matrix]]" (whose columns are the new [[basis_vectors | basis vectors]]) and its inverse <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.
    *   Sandwiching the original transformation [[matrices_and_their_properties | matrix]] between the change of basis [[matrices_and_their_properties | matrix]] and its inverse results in a [[diagonalization_and_eigenbasis | diagonal matrix]] in the new coordinate system, with eigenvalues down the diagonal <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
    *   This process, known as [[diagonalization_and_eigenbasis | diagonalization]], allows for easier computation of [[matrices_and_their_properties | matrix]] powers by performing the operation in the [[diagonalization_and_eigenbasis | eigenbasis]] and then converting back <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

Not all [[matrices_and_their_properties | transformations]] can be [[diagonalization_and_eigenbasis | diagonalized]]. For instance, a shear [[matrices_and_their_properties | transformation]] does not have enough eigenvectors to span the entire space <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

## Next Topic

The concept of [[abstract_vector_spaces | abstract vector spaces]] builds upon these foundational ideas <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.