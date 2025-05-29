---
title: Importance of understanding alternate coordinate systems
videoId: P2LTAUO1TdA
---

From: [[3blue1brown]] <br/> 

Understanding [[coordinate_systems_in_linear_algebra | coordinate systems]] and how to translate between them is fundamental in linear algebra, particularly when dealing with vectors and transformations <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

## What is a Coordinate System?

A [[coordinate_systems_and_basis_vectors | coordinate system]] is any method used to translate between vectors and sets of numbers (coordinates) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. These numbers (scalars) indicate how much to stretch or squish specific vectors, known as [[coordinate_systems_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The sum of these scaled basis vectors describes the target vector <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### The Standard Coordinate System
In 2D space, the standard way to describe a vector uses coordinates like (3,2), meaning three units to the right and two units up <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. In a [[linear_algebra_foundations | linear algebra]] context, this means:
*   The first coordinate scales `i-hat`, a vector of length 1 pointing to the right <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   The second coordinate scales `j-hat`, a vector of length 1 pointing straight up <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

These `i-hat` and `j-hat` vectors are the [[coordinate_systems_and_basis_vectors | basis vectors]] of the standard [[coordinate_systems_in_linear_algebra | coordinate system]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. They implicitly define aspects like direction (rightward/upward) and unit distance <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The grid typically used to visualize 2D space is a construct that depends on this choice of basis <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>; space itself has no intrinsic grid <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

### Alternate Coordinate Systems
The concept of a [[coordinate_systems_in_linear_algebra | coordinate system]] extends to using a different set of [[coordinate_systems_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. For example, a different individual, "Jennifer," might use basis vectors `b1` and `b2` <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   In the standard system, `b1` might be (2,1) and `b2` might be (-1,1) <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   From Jennifer's perspective, `b1` is (1,0) and `b2` is (0,1) in *her* system, as they define the meaning of her coordinates <a class="yt-timestamp" data-t="00:02:59">[00:03:06]</a>.

While everyone observes the same vectors in space, different [[coordinate_systems_in_linear_algebra | coordinate systems]] lead to different numerical descriptions <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Although the origin (0,0) is consistent across systems, the directions of axes and spacing of grid lines will vary based on the chosen [[coordinate_systems_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:03:53">[00:04:07]</a>.

## [[Change of basis and its implications | Translating Between Coordinate Systems]]

A key aspect of [[coordinate_systems_in_linear_algebra | coordinate systems]] is the ability to translate vector descriptions between them <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Translating Vectors
To translate a vector from an alternate system (e.g., Jennifer's) to the standard system (e.g., ours):
1.  Understand the vector's coordinates in the alternate system (e.g., Jennifer describes a vector as (-1,2)) <a class="yt-timestamp" data-t="00:04:18">[00:04:23]</a>.
2.  Recognize that these coordinates represent a linear combination of the alternate basis vectors (e.g., -1 times `b1` plus 2 times `b2`) <a class="yt-timestamp" data-t="00:04:29">[00:04:32]</a>.
3.  Express these alternate [[coordinate_systems_and_basis_vectors | basis vectors]] in terms of the standard system (e.g., `b1`=(2,1), `b2`=(-1,1) in our coordinates) <a class="yt-timestamp" data-t="00:04:39">[00:04:49]</a>.
4.  Compute the linear combination using the standard system's coordinates <a class="yt-timestamp" data-t="00:04:49">[00:04:53]</a>.
    *   This process is equivalent to [[linear_algebra_foundations | matrix-vector multiplication]], where the matrix columns are the alternate [[coordinate_systems_and_basis_vectors | basis vectors]] described in the standard system <a class="yt-timestamp" data-t="00:05:12">[00:05:21]</a>.
    *   This "change of basis matrix" (let's call it `A`) effectively transforms our "misconception" of the vector (if we used her coordinates in our system) into the actual vector she meant <a class="yt-timestamp" data-t="00:06:33">[00:06:37]</a>. So, `A * (her coordinates) = (our coordinates)` <a class="yt-timestamp" data-t="00:06:44">[00:06:47]</a>.

To translate a vector from the standard system to an alternate system:
*   Use the inverse of the change of basis matrix (`A⁻¹`) <a class="yt-timestamp" data-t="00:07:32">[00:07:36]</a>.
*   Applying `A⁻¹` to a vector described in the standard system yields its description in the alternate system <a class="yt-timestamp" data-t="00:08:11">[00:08:20]</a>.

### Translating Transformations
Just as vectors have different coordinate representations, linear transformations (represented by matrices) also have different forms depending on the [[coordinate_systems_in_linear_algebra | coordinate system]] they are described in <a class="yt-timestamp" data-t="00:08:50">[00:08:55]</a>.

To find the matrix representation of a transformation (M) in an alternate [[coordinate_systems_in_linear_algebra | coordinate system]] (represented by change of basis matrix A), the sequence of operations is:
1.  **Translate to our language:** Take a vector written in the alternate system's language and multiply it by the change of basis matrix `A` (whose columns are the alternate basis vectors in our language) <a class="yt-timestamp" data-t="00:10:23">[00:10:35]</a>. This converts the vector to our system.
2.  **Apply the transformation:** Multiply the result by our transformation matrix `M` <a class="yt-timestamp" data-t="00:10:43">[00:10:49]</a>. This applies the transformation in our system.
3.  **Translate back to their language:** Multiply the result by the inverse of the change of basis matrix `A⁻¹` <a class="yt-timestamp" data-t="00:10:53">[00:10:57]</a>. This converts the transformed vector back to the alternate system's language.

The composition of these three matrices, `A⁻¹ * M * A`, gives the transformation matrix as seen from the alternate [[coordinate_systems_in_linear_algebra | coordinate system]] <a class="yt-timestamp" data-t="00:11:04">[00:11:16]</a>. This new matrix takes a vector in the alternate system's coordinates and outputs the transformed vector in the same alternate system's coordinates <a class="yt-timestamp" data-t="00:11:19">[00:11:22]</a>.

The expression `A⁻¹ * M * A` signifies a "mathematical empathy" <a class="yt-timestamp" data-t="00:12:03">[00:12:07]</a>. The middle matrix `M` is the transformation as *we* see it, while the outer matrices `A⁻¹` and `A` represent the shift in perspective, making the full product represent the *same transformation as someone else sees it* <a class="yt-timestamp" data-t="00:12:07">[00:12:22]</a>.

## Why it Matters
Understanding [[change_of_basis_and_its_implications | alternate coordinate systems]] is crucial for various applications in [[linear_algebra_foundations | linear algebra]]. A significant example of its [[importance_of_geometric_understanding_in_linear_algebra | importance]] and application will be explored in the context of eigenvectors and eigenvalues <a class="yt-timestamp" data-t="00:12:22">[00:12:26]</a>.