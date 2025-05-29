---
title: Change of basis concept
videoId: P2LTAUO1TdA
---

From: [[3blue1brown]] <br/> 

A [[coordinate_systems_and_basis_vectors | coordinate system]] provides a standard way to describe a vector in 2D space using coordinates, such as (3, 2) for a vector that moves three units to the right and two units up from its tail to its tip <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Standard Basis Vectors

In [[linear_transformations_and_change_of_basis | linear algebra]], coordinates are thought of as scalars that stretch or squish vectors <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The first coordinate scales the [[unit_vectors_and_basis_vectors | unit vector]] i-hat (length 1, pointing right) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, while the second coordinate scales the [[unit_vectors_and_basis_vectors | unit vector]] j-hat (length 1, pointing straight up) <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The tip-to-tail sum of these two scaled vectors is what the coordinates describe <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

These two special vectors, i-hat and j-hat, encapsulate the implicit assumptions of our [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. They define directions (rightward, upward) and unit distances <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Any method for translating between vectors and sets of numbers is called a [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, and i-hat and j-hat are the [[coordinate_systems_and_basis_vectors | basis vectors]] of the standard [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Using Different Basis Vectors

It is possible to use a different set of [[coordinate_systems_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. For example, if a friend, Jennifer, uses [[coordinate_systems_and_basis_vectors | basis vectors]] b1 and b2 <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
*   b1 points up and to the right (described as (2,1) in our standard system) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a> <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   b2 points left and up (described as (-1,1) in our standard system) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a> <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

A vector described as (3,2) in our standard [[coordinate_systems_and_basis_vectors | coordinate system]] would be described by Jennifer as (5/3, 1/3) <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This means the vector is 5/3 times b1 plus 1/3 times b2 <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. From Jennifer's perspective, her [[coordinate_systems_and_basis_vectors | basis vectors]] b1 and b2 have coordinates (1,0) and (0,1) respectively within her system, as they define the meaning of these coordinates for her <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

Although different [[coordinate_systems_and_basis_vectors | coordinate systems]] use different descriptions, everyone agrees on the origin (0,0) <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. However, the direction of axes and spacing of grid lines will differ based on the choice of [[coordinate_systems_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Translating Between Coordinate Systems

### From Another System to Ours

To translate a vector described in Jennifer's [[coordinate_systems_and_basis_vectors | coordinate system]] (e.g., (-1,2)) into our [[coordinate_systems_and_basis_vectors | coordinate system]], we interpret her coordinates as scaling her [[coordinate_systems_and_basis_vectors | basis vectors]] (b1 and b2) and summing them <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>:
*   Jennifer's vector = -1 * b1 + 2 * b2 <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>
*   Since b1 = (2,1) and b2 = (-1,1) in our system, the computation is:
    *   -1 * (2,1) + 2 * (-1,1) = (-2,-1) + (-2,2) = (-4,1) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>
*   Thus, the vector she describes as (-1,2) is (-4,1) in our [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

This process is [[linear_transformations_and_change_of_basis | matrix-vector multiplication]], where the matrix columns represent Jennifer's [[coordinate_systems_and_basis_vectors | basis vectors]] in our language <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This "change of basis" matrix can be seen as a [[linear_transformations_and_change_of_basis | transformation]] that moves our standard [[coordinate_systems_and_basis_vectors | basis vectors]] (i-hat, j-hat) to Jennifer's [[coordinate_systems_and_basis_vectors | basis vectors]] (b1, b2) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### From Our System to Another System

To translate a vector from our [[coordinate_systems_and_basis_vectors | coordinate system]] (e.g., (3,2)) into Jennifer's system, we take the inverse of the "change of basis" matrix (the one whose columns are Jennifer's [[coordinate_systems_and_basis_vectors | basis vectors]] in our language) <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. The inverse matrix performs the opposite [[linear_transformations_and_change_of_basis | transformation]] <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

For Jennifer's [[coordinate_systems_and_basis_vectors | basis vectors]] b1=(2,1) and b2=(-1,1), the change of basis matrix is:
```
[ 2  -1 ]
[ 1   1 ]
```
Its inverse is:
```
[ 1/3   1/3 ]
[-1/3   2/3 ]
```
Multiplying this inverse matrix by our vector (3,2) gives:
```
[ 1/3   1/3 ] [ 3 ]   [ (1/3)*3 + (1/3)*2  ]   [ 5/3 ]
[-1/3   2/3 ] [ 2 ] = [ (-1/3)*3 + (2/3)*2 ] = [ 1/3 ]
```
So, the vector (3,2) in our system is (5/3, 1/3) in Jennifer's system <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

## Representing Transformations in Different Bases

A [[linear_transformations_and_change_of_basis | linear transformation]], such as a 90-degree counterclockwise rotation, is typically represented by a matrix whose columns show where our standard [[coordinate_systems_and_basis_vectors | basis vectors]] (i-hat and j-hat) land, described in our [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. For a 90-degree rotation, i-hat lands at (0,1) and j-hat lands at (-1,0), forming the matrix:
```
[ 0  -1 ]
[ 1   0 ]
```
This representation is dependent on the chosen [[coordinate_systems_and_basis_vectors | basis]] <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

To find the matrix representation of this same 90-degree rotation in Jennifer's [[coordinate_systems_and_basis_vectors | coordinate system]], a three-step process is used <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>:
1.  **Translate to our language:** Take a vector in Jennifer's language and multiply it by the "change of basis" matrix (P), whose columns are Jennifer's [[coordinate_systems_and_basis_vectors | basis vectors]] in our language <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This gives the vector in our language.
2.  **Apply the transformation:** Multiply the result by our transformation matrix (A), representing the 90-degree rotation <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. This gives the transformed vector in our language.
3.  **Translate back to Jennifer's language:** Multiply the result by the inverse of the change of basis matrix (P⁻¹) <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. This gives the transformed vector in Jennifer's language.

This composition of three matrices, P⁻¹AP, yields the transformation matrix in Jennifer's [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

The expression `A⁻¹MA` (or P⁻¹AP in the example above) represents a mathematical "empathy" <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The middle matrix (M or A) is the transformation as one person sees it, and the outer two matrices (A⁻¹ and A, or P⁻¹ and P) represent the shift in perspective to see that same [[linear_transformations_and_change_of_basis | transformation]] from someone else's point of view <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

Understanding alternate [[coordinate_systems_and_basis_vectors | coordinate systems]] is crucial for concepts like [[concept_of_eigenbasis | eigenvectors and eigenvalues]] <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.