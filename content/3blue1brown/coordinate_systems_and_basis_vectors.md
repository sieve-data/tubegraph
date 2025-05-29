---
title: Coordinate systems and basis vectors
videoId: P2LTAUO1TdA
---

From: [[3blue1brown]] <br/> 

When discussing a [[understanding_vectors | vector]] in 2D space, a standard method for describing it uses coordinates <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. For example, a vector with coordinates (3, 2) indicates a movement of three units to the right and two units up from its tail to its tip <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## [[Vector representation and coordinate systems | Standard Vector Representation]]

In linear algebra, coordinates are understood as scalars that stretch or squish vectors <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The first coordinate scales `i-hat`, a [[unit_vectors_and_basis_vectors | vector]] of length 1 pointing to the right <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, while the second coordinate scales `j-hat`, a [[unit_vectors_and_basis_vectors | vector]] of length 1 pointing straight up <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The tip-to-tail sum of these two scaled vectors is what the coordinates describe <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

These two special vectors, `i-hat` and `j-hat`, encapsulate the implicit assumptions of a coordinate system <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This includes the understanding that the first number indicates rightward motion, the second upward motion, and the exact unit of distance <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Any method to translate between vectors and sets of numbers is called a [[Vector representation and coordinate systems | coordinate system]] <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. `i-hat` and `j-hat` are known as the [[unit_vectors_and_basis_vectors | basis vectors]] of the standard coordinate system <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## [[Change of basis concept | Alternative Basis Vectors]]

It is possible to use a different set of [[unit_vectors_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. For instance, another individual might use basis vectors `b1` and `b2` <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. If `b1` points slightly up and to the right, and `b2` points left and up <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, a [[understanding_vectors | vector]] described as (3, 2) in the standard system (using `i-hat` and `j-hat`) might be described as (5/3, 1/3) using `b1` and `b2` <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This means that to reach that [[understanding_vectors | vector]] using `b1` and `b2`, `b1` is scaled by 5/3 and `b2` by 1/3, then added together <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

In this alternative system, the first coordinate scales `b1`, and the second scales `b2`, with the results summed <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This will typically result in a different [[understanding_vectors | vector]] than what one would expect from the same coordinates in the standard system <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

From the standard system's perspective:
*   `b1` might have coordinates (2, 1) <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   `b2` might have coordinates (-1, 1) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

However, from the perspective of the alternative system, `b1` has coordinates (1, 0) and `b2` has coordinates (0, 1) within their own system <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. These vectors define the meaning of (1, 0) and (0, 1) in that system <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Essentially, different [[Vector representation and coordinate systems | coordinate systems]] are "speaking different languages" while observing the same vectors in space <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

A grid, often used to visualize 2D space, is a construct tied to the choice of [[unit_vectors_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Space itself has no intrinsic grid <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. While the origin (0,0) remains consistent across all systems (as it's any [[understanding_vectors | vector]] scaled by 0) <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>, the directions of axes and spacing of grid lines will differ based on the chosen [[unit_vectors_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## [[Change of basis concept | Translating Between Coordinate Systems]]

A key question is how to translate [[vector_coordinates_and_scalar_implications | vector coordinates]] between [[Vector representation and coordinate systems | coordinate systems]] <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### From Alternate to Standard System

If a [[understanding_vectors | vector]] is described with coordinates (-1, 2) in an alternative system, this means it is -1 times `b1` plus 2 times `b2` <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. Using the standard system's description of `b1` as (2, 1) and `b2` as (-1, 1) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>, the calculation `(-1 * (2,1)) + (2 * (-1,1))` results in the vector (-4, 1) in the standard system <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

This process of scaling each of the alternate [[unit_vectors_and_basis_vectors | basis vectors]] by the corresponding coordinates and adding them is equivalent to [[linear_transformations_and_change_of_basis | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. The matrix involved has the alternate [[unit_vectors_and_basis_vectors | basis vectors]] (expressed in the standard system's coordinates) as its columns <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

This "change of basis matrix" can be understood as a [[linear_transformations_and_change_of_basis | linear transformation]] that moves the standard basis vectors (`i-hat`, `j-hat`) to the alternate basis vectors (`b1`, `b2`) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. When this matrix is applied to a [[understanding_vectors | vector]] (e.g., (-1, 2)) conceived in the standard system, it transforms this "misconception" (what the coordinates would mean in the standard system) into the actual [[understanding_vectors | vector]] being referred to by the alternative system <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### From Standard to Alternate System

To translate a [[understanding_vectors | vector]] from the standard system to an alternate system (e.g., how the vector (3, 2) in the standard system becomes (5/3, 1/3) in the alternative system) <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, the [[inverse_matrix_and_translating_between_coordinate_systems | inverse of the change of basis matrix]] is used <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. The inverse matrix is a transformation that corresponds to "playing the first one backwards" <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

For the example using `b1`=(2,1) and `b2`=(-1,1), the change of basis matrix would be:
```
[ 2 -1 ]
[ 1  1 ]
```
Its inverse matrix for this case is:
```
[ 1/3  1/3 ]
[-1/3  2/3 ]
```
Multiplying this inverse matrix by the vector (3, 2) results in (5/3, 1/3) <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

Therefore:
*   The matrix whose columns represent the alternate [[unit_vectors_and_basis_vectors | basis vectors]] (in standard coordinates) translates vectors *from* the alternate language *to* the standard language <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   The [[inverse_matrix_and_translating_between_coordinate_systems | inverse matrix]] does the opposite <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## [[Linear transformations and change of basis | Representing Transformations in Different Coordinate Systems]]

Matrices are also used to represent [[linear_transformations_and_change_of_basis | linear transformations]] <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. For instance, a 90-degree counterclockwise rotation can be represented by tracking where `i-hat` and `j-hat` land <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. If `i-hat` lands at (0, 1) and `j-hat` lands at (-1, 0), these coordinates become the columns of the transformation matrix in the standard system <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This representation is tied to the choice of [[unit_vectors_and_basis_vectors | basis vectors]] and the coordinate system used to record their landing spots <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

To describe the *same* 90-degree rotation in an alternative system, one cannot simply translate the columns of the standard rotation matrix <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. The matrix for the alternative system needs to represent where *its* [[unit_vectors_and_basis_vectors | basis vectors]] land, and describe those landing spots in *its own language* <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

The process for finding this matrix involves a composition of three transformations:
1.  **Translate to standard language**: Take a [[understanding_vectors | vector]] from the alternative system and use the change of basis matrix (whose columns are the alternative [[unit_vectors_and_basis_vectors | basis vectors]] in standard coordinates) to translate it into the standard system <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
2.  **Apply transformation in standard language**: Apply the desired [[linear_transformations_and_change_of_basis | transformation matrix]] (expressed in the standard system) <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  **Translate back to alternative language**: Apply the [[inverse_matrix_and_translating_between_coordinate_systems | inverse change of basis matrix]] to get the transformed [[understanding_vectors | vector]] back into the alternative system's language <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

This composition of three matrices `(Inverse Change of Basis) * (Transformation in Standard System) * (Change of Basis)` yields the [[linear_transformations_and_change_of_basis | transformation matrix]] in the alternative system's language <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

For the specific example where alternative basis vectors `b1`=(2,1) and `b2`=(-1,1) in the standard system, and the transformation is a 90-degree rotation, the resulting matrix in the alternative system would have columns (1/3, 5/3) and (-2/3, -1/3) <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

### The `A⁻¹MA` Expression

In general, an expression like `A⁻¹MA` represents a mathematical "empathy" <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The middle matrix `M` is a [[linear_transformations_and_change_of_basis | transformation]] as seen from one perspective <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. The outer two matrices (`A⁻¹` and `A`) represent a shift in perspective <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. The full matrix product represents that same [[linear_transformations_and_change_of_basis | transformation]] but as someone else sees it <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

Understanding alternate [[Vector representation and coordinate systems | coordinate systems]] is crucial for topics like [[eigenvectors_in_two_and_three_dimensions | eigenvectors and eigenvalues]] <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.