---
title: Change of basis and its implications
videoId: P2LTAUO1TdA
---

From: [[3blue1brown]] <br/> 

In [[linear_algebra_foundations | linear algebra]], understanding how vectors and transformations are described in different [[coordinate_systems_and_basis_vectors | coordinate systems]] is fundamental. This concept, known as change of basis, allows for flexible representation and analysis of mathematical objects.

## Standard Coordinate System

A vector in 2D space is typically described by its coordinates, such as (3, 2), meaning it moves three units to the right and two units up from its tail to its tip <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

More formally, these coordinates represent scalars that stretch or squish [[representation_of_vectors_using_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>:
*   The first coordinate scales `i-hat`, the vector of length 1 pointing right <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   The second coordinate scales `j-hat`, the vector of length 1 pointing straight up <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

The tip-to-tail sum of these two scaled vectors is what the coordinates describe <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. These special vectors, `i-hat` and `j-hat`, encapsulate the implicit assumptions of our standard coordinate system, defining direction and unit distance <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Coordinate Systems and Basis Vectors

Any method for translating between vectors and sets of numbers is called a [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The special vectors that define this translation (like `i-hat` and `j-hat`) are called the [[representation_of_vectors_using_basis_vectors | basis vectors]] of that system <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Alternate Coordinate Systems

It's possible to use a different set of [[representation_of_vectors_using_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. For example, consider "Jennifer's" coordinate system defined by [[representation_of_vectors_using_basis_vectors | basis vectors]] `b1` and `b2` <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
*   `b1` points up and to the right (e.g., our coordinates: (2, 1)) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a> <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   `b2` points left and up (e.g., our coordinates: (-1, 1)) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a> <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Vector Representation in Different Systems

A vector described as (3, 2) in our standard system (using `i-hat` and `j-hat`) would be described differently in Jennifer's system <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Jennifer would use coordinates like (5/3, 1/3) for the same vector <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This means the vector is obtained by scaling `b1` by 5/3 and `b2` by 1/3, then adding the results <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

From Jennifer's perspective, her basis vectors `b1` and `b2` have coordinates (1,0) and (0,1) respectively within her system, as they define the meaning of those coordinates for her <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. This highlights that different [[coordinate_systems_and_basis_vectors | coordinate systems]] are "speaking different languages" to describe the same vectors in space <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### The Nature of the Grid

The visual grid used to represent 2D space is merely a construct to visualize a [[coordinate_systems_and_basis_vectors | coordinate system]], and thus depends on the chosen basis <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Space itself has no intrinsic grid <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. While the origin (0,0) is universally agreed upon, the direction of axes and spacing of grid lines vary based on the choice of [[representation_of_vectors_using_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Translating Between Coordinate Systems

A natural question arises: how do we translate between [[coordinate_systems_and_basis_vectors | coordinate systems]] <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>?

### From Jennifer's System to Ours

If Jennifer describes a vector as (-1, 2) in her system, this means it is -1 times `b1` plus 2 times `b2` <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. Since we know `b1` is (2, 1) and `b2` is (-1, 1) in our system, we can compute:
`(-1) * (2, 1) + 2 * (-1, 1) = (-2, -1) + (-2, 2) = (-4, 1)` <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
So, the vector she calls (-1, 2) is (-4, 1) in our system <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

This process is [[concept_of_column_space_in_transformations | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. The matrix used for this translation has Jennifer's [[representation_of_vectors_using_basis_vectors | basis vectors]] (in our language) as its columns <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. This matrix can be seen as a [[meaningful_transformations_and_their_ties_to_the_dot_product | linear transformation]] that moves our standard [[representation_of_vectors_using_basis_vectors | basis vectors]] (`i-hat`, `j-hat`) to Jennifer's [[representation_of_vectors_using_basis_vectors | basis vectors]] (`b1`, `b2`) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. When we apply this matrix to a vector described with Jennifer's coordinates in our system, it transforms our "misconception" of what those coordinates mean into the actual vector she is referring to <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### From Our System to Jennifer's

To translate a vector from our system to Jennifer's, we use the inverse of the change of basis matrix <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. The inverse matrix "plays the first transformation backwards" <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. For example, to find the coordinates of (3, 2) in Jennifer's system:
1.  Construct the change of basis matrix (columns are Jennifer's basis vectors in our coordinates):
    ```
    [ 2  -1 ]
    [ 1   1 ]
    ```
2.  Compute its inverse. For this example, the inverse matrix has columns (1/3, -1/3) and (1/3, 2/3) <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
3.  Multiply this inverse matrix by our vector (3, 2):
    ```
    [ 1/3   1/3 ] [ 3 ]   [ (1/3)*3 + (1/3)*2 ]   [ 1 + 2/3 ]   [ 5/3 ]
    [ -1/3  2/3 ] [ 2 ] = [ (-1/3)*3 + (2/3)*2 ] = [ -1 + 4/3 ] = [ 1/3 ]
    ```
This yields (5/3, 1/3), which are the coordinates in Jennifer's system <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

In summary, the matrix with Jennifer's [[representation_of_vectors_using_basis_vectors | basis vectors]] as columns translates vectors *from her language into ours*, and its inverse matrix does the opposite <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

## Representing Linear Transformations in Different Bases

[[meaningful_transformations_and_their_ties_to_the_dot_product | Linear transformations]] are also described using matrices, which depend heavily on the chosen basis <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### Our Representation of a Rotation

For example, a 90-degree counterclockwise rotation is represented by a matrix whose columns show where `i-hat` and `j-hat` land after the transformation <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>:
*   `i-hat` lands at (0, 1) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   `j-hat` lands at (-1, 0) <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
So, our rotation matrix is:
```
[ 0  -1 ]
[ 1   0 ]
```

### Jennifer's Representation of a Rotation

Jennifer's matrix for this same 90-degree rotation must represent where *her* [[representation_of_vectors_using_basis_vectors | basis vectors]] land, and describe those landing spots in *her* language <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

To find the matrix for a transformation `M` in a different basis (like Jennifer's), given our change of basis matrix `A` (whose columns are Jennifer's basis vectors in our coordinates):
1.  **Translate to our language:** Apply the change of basis matrix `A` to the vector (written in Jennifer's language) <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
2.  **Apply the transformation:** Multiply by our transformation matrix `M` <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  **Translate back to Jennifer's language:** Apply the inverse change of basis matrix `A⁻¹` <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

This composition of three matrices `A⁻¹ M A` gives the transformation matrix in Jennifer's language <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. It takes a vector in her language and returns the transformed vector in her language <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

### The Formula A⁻¹MA

The expression `A⁻¹ M A` is a common mathematical pattern. The middle matrix `M` represents a transformation from our perspective, and the outer two matrices (`A⁻¹` and `A`) represent a shift in perspective, or "mathematical empathy" <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The full matrix product represents that same transformation, but as someone else (like Jennifer) sees it <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

## Importance of Understanding Alternate Coordinate Systems

Understanding how to change basis is crucial because some [[meaningful_transformations_and_their_ties_to_the_dot_product | linear transformations]] become much simpler when viewed from a specific [[coordinate_systems_and_basis_vectors | coordinate system]]. This leads directly into the concept of [[diagonalization and eigenbasis | eigenvectors and eigenvalues]], where finding a special basis (the eigenbasis) can simplify complex transformations to diagonal matrices <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.