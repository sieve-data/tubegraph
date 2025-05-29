---
title: Representation of vectors using basis vectors
videoId: P2LTAUO1TdA
---

From: [[3blue1brown]] <br/> 

In linear algebra, vectors are often described using [[coordinate_systems_and_basis_vectors | coordinates]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. For a vector in 2D space, coordinates like (3, 2) mean moving three units to the right and two units up from the tail to the tip <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Standard Coordinate System and Basis Vectors

From a linear algebra perspective, each coordinate is a scalar that stretches or squishes vectors <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
In a standard 2D system:
*   The first coordinate scales `i-hat`, a vector of length 1 pointing to the right <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   The second coordinate scales `j-hat`, a vector of length 1 pointing straight up <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

The tip-to-tail sum of these two scaled vectors is what the coordinates describe <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. These two special vectors, `i-hat` and `j-hat`, encapsulate all the implicit assumptions of a [[coordinate_systems_and_basis_vectors | coordinate system]], including the direction of motion for each coordinate and the unit of distance <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

Any method for translating between vectors and sets of numbers is called a [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The vectors `i-hat` and `j-hat` are known as the [[basis_vectors | basis vectors]] of the standard [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Alternate Coordinate Systems

It's possible to use a [[change_of_basis_and_its_implications | different set of basis vectors]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. For example, if a friend, Jennifer, uses [[basis_vectors | basis vectors]] `b1` and `b2` <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
*   `b1` points up and slightly right <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   `b2` points left and up <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

A vector that we describe with coordinates (3, 2) in our standard system (using `i-hat` and `j-hat`) <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a> would be described by Jennifer with coordinates (5/3, 1/3) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This means the vector is formed by scaling `b1` by 5/3 and `b2` by 1/3, then adding them together <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

From Jennifer's perspective, her [[basis_vectors | basis vectors]] `b1` and `b2` have [[coordinate_systems_and_basis_vectors | coordinates]] (1, 0) and (0, 1) respectively in her system <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. These vectors define the meaning of (1, 0) and (0, 1) in her world <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Essentially, different choices of [[basis_vectors | basis vectors]] lead to different "languages" for describing the same vectors in space <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

The grid typically used to visualize 2D space is a construct tied to the choice of [[basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Space itself does not have an intrinsic grid <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. While the origin (0,0) is universally agreed upon <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>, the direction of axes and spacing of grid lines will vary depending on the chosen [[basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Translating Between Coordinate Systems

### From Jennifer's Language to Ours
To translate a vector described in Jennifer's [[coordinate_systems_and_basis_vectors | coordinate system]] (e.g., (-1, 2)) into our system:
1.  Recognize that Jennifer's coordinates mean (-1) * `b1` + (2) * `b2` <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
2.  Substitute our description of `b1` (2, 1) and `b2` (-1, 1) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
3.  Compute the linear combination: (-1) * (2, 1) + (2) * (-1, 1) = (-2, -1) + (-2, 2) = (-4, 1) <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
This process is equivalent to matrix-vector multiplication <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The matrix used for this translation has Jennifer's [[basis_vectors | basis vectors]] (in our [[coordinate_systems_and_basis_vectors | coordinates]]) as its columns <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

The matrix whose columns represent Jennifer's [[basis_vectors | basis vectors]] (in our language) can be thought of as a transformation that moves our [[basis_vectors | basis vectors]] (`i-hat` and `j-hat`) to Jennifer's [[basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Applying this matrix to a vector expressed in "our misconception" of Jennifer's coordinates (i.e., using her coordinates with our [[basis_vectors | basis vectors]]) transforms it into the actual vector she's referring to <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### From Our Language to Jennifer's
To translate a vector from our [[coordinate_systems_and_basis_vectors | coordinate system]] (e.g., (3, 2)) into Jennifer's system:
1.  Start with the "change of basis" matrix that translates Jennifer's language into ours <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
2.  Take its inverse <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. The inverse of a transformation plays it backwards <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
3.  Multiply this inverse matrix by the vector's [[coordinate_systems_and_basis_vectors | coordinates]] in our system <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

For instance, the inverse of the matrix with Jennifer's [[basis_vectors | basis vectors]] as columns (2,1 and -1,1) is a matrix with columns (1/3, -1/3) and (1/3, 2/3) <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Multiplying this by (3, 2) yields (5/3, 1/3) <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

In summary, the matrix whose columns represent Jennifer's [[basis_vectors | basis vectors]] in our [[coordinate_systems_and_basis_vectors | coordinates]] translates vectors from her language to ours <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. Its inverse matrix performs the opposite translation <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Representing Linear Transformations in Different Bases

When a linear transformation (e.g., a 90-degree counterclockwise rotation) is represented by a matrix, this representation is heavily dependent on the chosen [[basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. The matrix columns are derived from where the [[basis_vectors | basis vectors]] (`i-hat`, `j-hat`) land, recorded in the system's own [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

To find how Jennifer would describe this same 90-degree rotation <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>:
1.  Start with a vector written in Jennifer's language <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
2.  Translate it into our language using the "change of basis" matrix (let's call it `A`) <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
3.  Apply our transformation matrix (let's call it `M`) to the vector in our language <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
4.  Apply the inverse change of basis matrix ( `A_inverse`) to translate the transformed vector back into Jennifer's language <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

This composition of three matrices — `A_inverse * M * A` — gives the transformation matrix in Jennifer's language <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. This matrix takes a vector in her language and outputs its transformed version, also in her language <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

> [!NOTE] Mathematical Empathy
> An expression like `A_inverse * M * A` suggests "mathematical empathy" <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The middle matrix (`M`) represents a transformation as one sees it, while the outer two matrices (`A_inverse` and `A`) represent a shift in perspective <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. The full matrix product then represents the same transformation but as someone else sees it <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

Understanding [[change_of_basis_and_its_implications | alternate coordinate systems]] is crucial, especially for concepts like [[eigenvectors_and_eigenvalues | eigenvectors and eigenvalues]] <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.