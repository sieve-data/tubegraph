---
title: Coordinate systems and basis vectors
videoId: P2LTAUO1TdA
---

From: [[3blue1brown]] <br/> 

In [[linear_algebra_foundations | linear algebra]], understanding [[coordinate_systems_in_linear_algebra | coordinate systems]] and [[basis_vectors | basis vectors]] is fundamental to [[understanding_vectors_in_linear_algebra | understanding vectors]] and transformations.

## Standard Coordinate System
A standard way to describe a vector in 2D space involves using coordinates, such as (3, 2) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This means moving three units to the right and two units up from the vector's tail to its tip <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

More formally, this description is rooted in the concept of [[representation_of_vectors_using_basis_vectors | representing vectors using basis vectors]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Each coordinate acts as a scalar, stretching or squishing vectors <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   The first coordinate scales `i-hat`, a vector of length 1 pointing to the right <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   The second coordinate scales `j-hat`, a vector of length 1 pointing straight up <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

The sum of these two scaled vectors describes the vector's coordinates <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. These two special vectors, `i-hat` and `j-hat`, encapsulate the implicit assumptions of our [[coordinate_systems_in_linear_algebra | coordinate system]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. They define:
*   Rightward motion for the first number <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   Upward motion for the second number <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   The unit of distance <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

Any method to translate between vectors and sets of numbers is called a [[coordinate_systems_in_linear_algebra | coordinate system]] <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, and `i-hat` and `j-hat` are the [[basis_vectors | basis vectors]] of the standard [[coordinate_systems_in_linear_algebra | coordinate system]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Alternate Basis Vectors
The concept extends to using a different set of [[basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. For example, a different set, `b1` and `b2`, might be used <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   `b1` might point up and to the right <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   `b2` might point left and up <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

The same vector that we describe with coordinates (3, 2) in our standard [[coordinate_systems_in_linear_algebra | system]] (using `i-hat` and `j-hat`) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, another person using `b1` and `b2` might describe with coordinates (5/3, 1/3) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This means the vector is formed by scaling `b1` by 5/3 and `b2` by 1/3, then adding them together <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

When using alternate [[basis_vectors | basis vectors]]:
*   The first coordinate scales `b1` <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   The second coordinate scales `b2` <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   The resulting vector is typically different from what would be implied by those coordinates in the standard system <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

In our standard [[coordinate_systems_in_linear_algebra | system]]:
*   `b1` could be described as (2, 1) <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   `b2` could be described as (-1, 1) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

However, from the perspective of the alternate system, `b1` and `b2` themselves have coordinates (1, 0) and (0, 1) respectively <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. These are the vectors that define the meaning of (1,0) and (0,1) in that particular system <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Essentially, different [[coordinate_systems_in_linear_algebra | systems]] are "speaking different languages" while looking at the same vectors in space <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Visualizing Different Coordinate Systems
The square grid typically used to animate 2D space is merely a construct to visualize *our* [[coordinate_systems_in_linear_algebra | coordinate system]] and depends on our choice of [[basis_vectors | basis]] <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Space itself has no intrinsic grid <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Someone using a different set of [[basis_vectors | basis vectors]] would draw their own grid, equally a made-up visual tool <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

The origin (0,0) is universally agreed upon, as it's the result of scaling any vector by zero <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. However, the direction of the axes and the spacing of the grid lines will differ based on the choice of [[basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Translating Between Coordinate Systems
A key question is how to translate between [[coordinate_systems_in_linear_algebra | coordinate systems]] <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, which is a core part of [[change_of_basis_and_its_implications | change of basis and its implications]].

### From an Alternate System to the Standard System
If a vector is described with coordinates (-1, 2) in an alternate system (e.g., Jennifer's) <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>, this means the vector is `(-1 * b1) + (2 * b2)` <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

To translate this into our standard [[coordinate_systems_in_linear_algebra | system]]:
1.  Represent `b1` and `b2` in our standard coordinates (e.g., `b1` = (2, 1) and `b2` = (-1, 1)) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
2.  Compute the linear combination: `(-1 * (2, 1)) + (2 * (-1, 1))` <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
3.  The result is (-4, 1) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

This process is [[matrix_vector_multiplication | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The matrix used for this translation, known as the **change of basis matrix**, has the alternate [[basis_vectors | basis vectors]] as its columns (expressed in our coordinates) <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   This matrix acts as a transformation that moves our standard [[basis_vectors | basis vectors]] (`i-hat` and `j-hat`) to the alternate [[basis_vectors | basis vectors]] (`b1` and `b2`) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   When this transformation is applied to a vector *represented in our system* (but incorrectly assumed to be in the alternate system), it yields the actual vector the alternate system refers to <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   Geometrically, this matrix transforms our standard grid into the alternate system's grid <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Numerically, it translates a vector described in the alternate system's language to our language <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

### From the Standard System to an Alternate System
To go the other way – translating a vector from our standard [[coordinate_systems_in_linear_algebra | system]] to an alternate one <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a> – we use the inverse of the change of basis matrix <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   The inverse of a transformation corresponds to playing the first one backward <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   For the example vector (3, 2) in our system, to find its coordinates in the alternate system, we multiply it by the inverse change of basis matrix <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   If the change of basis matrix has columns (2,1) and (-1,1), its inverse will have columns (1/3, -1/3) and (1/3, 2/3) <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   Multiplying this inverse by (3, 2) yields (5/3, 1/3) <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

In summary, the matrix whose columns represent the alternate [[basis_vectors | basis vectors]] in our coordinates translates vectors *from* the alternate system *to* our system <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. Its inverse matrix does the opposite <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Representing Transformations in Different Coordinate Systems
[[coordinate_systems_in_linear_algebra | Coordinate systems]] are also used to describe [[linear_transformation | linear transformations]] with matrices <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
When we represent a transformation (e.g., a 90-degree counterclockwise rotation) with a matrix, we follow where our standard [[basis_vectors | basis vectors]] (`i-hat` and `j-hat`) land <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. Their landing coordinates become the columns of our matrix <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. This representation is tied to our choice of [[basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

To find how an alternate system (e.g., Jennifer's) would describe the *same* 90-degree rotation:
1.  Start with any vector written in the alternate system's language <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
2.  Translate it into our language using the change of basis matrix (call it `A`), where its columns are the alternate [[basis_vectors | basis vectors]] in our language <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
3.  Apply the transformation matrix (`M`) that we use (multiplied on the left) to the vector now in our language <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
4.  Apply the inverse change of basis matrix (`A inverse`), multiplied on the left, to translate the transformed vector back into the alternate system's language <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

This composition of three matrices `A inverse * M * A` gives the transformation matrix as seen in the alternate system's language <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. This matrix takes a vector in the alternate system's language and outputs its transformed version in the same language <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

### Mathematical Empathy
The expression `A inverse * M * A` suggests a mathematical form of "empathy" <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   The middle matrix (`M`) represents a transformation as *you* see it <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   The outer two matrices (`A inverse` and `A`) represent the shift in perspective, the empathy <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   The full matrix product represents that same transformation but as *someone else* sees it <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

## Importance
Understanding [[coordinate_systems_in_linear_algebra | alternate coordinate systems]] is crucial for topics like eigenvectors and eigenvalues <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>, highlighting the [[importance_of_understanding_alternate_coordinate_systems | importance of understanding alternate coordinate systems]].