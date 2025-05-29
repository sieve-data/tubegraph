---
title: Concept of eigenbasis
videoId: PFDu9oVAE-g
---

From: [[3blue1brown]] <br/> 

The concept of an eigenbasis is closely related to [[eigenvectors_and_eigenvalues | eigenvectors and eigenvalues]] and provides a powerful way to simplify the representation and analysis of [[linear_transformations_and_change_of_basis | linear transformations]]. It builds upon the idea of [[change_of_basis_concept | changing the coordinate system]] to better understand a transformation <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## What is an Eigenbasis?

An eigenbasis is a set of [[unit_vectors_and_basis_vectors | basis vectors]] for a transformation that are also [[eigenvectors_in_two_and_three_dimensions | eigenvectors]] <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a> <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. If a transformation's [[unit_vectors_and_basis_vectors | basis vectors]] happen to be [[eigenvectors_in_two_and_three_dimensions | eigenvectors]], the matrix representing that transformation will be a diagonal matrix <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

### Diagonal Matrices
A diagonal matrix is one where all entries are zero except for those on the main diagonal <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. When a transformation is represented by a diagonal matrix, it means that its [[unit_vectors_and_basis_vectors | basis vectors]] are [[eigenvectors_in_two_and_three_dimensions | eigenvectors]], and the diagonal entries are their corresponding [[eigenvectors_and_eigenvalues | eigenvalues]] <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a> <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. For example, if the i-hat [[unit_vectors_and_basis_vectors | basis vector]] is scaled by -1 and the j-hat [[unit_vectors_and_basis_vectors | basis vector]] by 2, the resulting matrix will have -1 and 2 on its diagonal, with zeros elsewhere <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a> <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

## Utility of an Eigenbasis

Working with diagonal matrices is often much simpler than working with non-diagonal matrices <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

### Computing Matrix Powers
One significant advantage of diagonal matrices is the ease with which one can compute their powers (e.g., `A` multiplied by itself 100 times) <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. If a matrix is diagonal, applying it multiple times simply corresponds to scaling each [[unit_vectors_and_basis_vectors | basis vector]] by the corresponding eigenvalue raised to the power of the number of applications <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a> <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. This is a "nightmare" for non-diagonal matrices <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.

### Changing to an Eigenbasis
While [[unit_vectors_and_basis_vectors | basis vectors]] rarely happen to be [[eigenvectors_in_two_and_three_dimensions | eigenvectors]] in the standard [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>, if a transformation has enough [[eigenvectors_in_two_and_three_dimensions | eigenvectors]] to span the entire space, you can perform a [[change_of_basis_concept | change of basis]] <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

To do this:
1.  Choose a set of [[eigenvectors_in_two_and_three_dimensions | eigenvectors]] that can serve as the new [[unit_vectors_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a> <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
2.  Form a [[change_of_basis_concept | change of basis]] matrix by using the coordinates of these [[eigenvectors_in_two_and_three_dimensions | eigenvectors]] as its columns <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a> <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a> <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
3.  "Sandwich" the original transformation matrix (`A`) between the [[change_of_basis_concept | change of basis]] matrix (`P`) and its inverse (`P⁻¹`), forming the expression `P⁻¹AP` <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a> <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.

The resulting matrix (`P⁻¹AP`) will represent the same [[linear_transformations_and_change_of_basis | transformation]], but from the perspective of the new [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a> <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. Crucially, this new matrix is guaranteed to be diagonal, with the corresponding [[eigenvectors_and_eigenvalues | eigenvalues]] down its diagonal <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a> <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

This approach simplifies computations significantly. For instance, to compute the 100th power of a matrix, one can convert to an eigenbasis, compute the power in that simpler system (where it's just powers of the diagonal entries), and then convert back to the standard system <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a> <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

## Limitations

Not all [[linear_transformations_and_change_of_basis | transformations]] can be represented with an eigenbasis <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. For example, a shear transformation does not have enough [[eigenvectors_in_two_and_three_dimensions | eigenvectors]] to span the entire space, meaning an eigenbasis cannot be formed for it <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a> <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>. However, when an eigenbasis *can* be found, it makes matrix operations much more manageable <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.