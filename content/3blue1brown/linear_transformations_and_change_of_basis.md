---
title: Linear transformations and change of basis
videoId: P2LTAUO1TdA
---

From: [[3blue1brown]] <br/> 

## Understanding Coordinate Systems and Basis Vectors

In two-dimensional space, a vector can be described using coordinates <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. For instance, coordinates (3, 2) for a vector mean moving three units to the right and two units up from its tail to its tip <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

From a [[linear_transformations_in_linear_algebra | linear algebra]] perspective, these coordinates are scalars that stretch or squish vectors <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The first coordinate scales the `i-hat` vector (length 1, pointing right) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, and the second coordinate scales the `j-hat` vector (length 1, pointing straight up) <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The tip-to-tail sum of these two scaled vectors is what the coordinates describe <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

These two special vectors, `i-hat` and `j-hat`, encapsulate the implicit assumptions of our standard coordinate system, including the meaning of rightward/upward motion and unit distance <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Any method for translating between vectors and sets of numbers is called a coordinate system <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, and `i-hat` and `j-hat` are the [[unit_vectors_and_basis_vectors | basis vectors]] of our standard system <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Introducing Different Basis Vectors

The [[change_of_basis_concept | change of basis concept]] involves using a different set of [[coordinate_systems_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. For example, consider a friend, Jennifer, who uses basis vectors `b1` and `b2` <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   Her `b1` might point up and to the right <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   Her `b2` might point left and up <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

A vector that we describe as (3, 2) using `i-hat` and `j-hat` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, Jennifer might describe as (5/3, 1/3) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This means she scales `b1` by 5/3, `b2` by 1/3, and adds them to reach the same vector <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

From our perspective (our coordinate system):
*   Jennifer's `b1` has coordinates (2, 1) <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   Jennifer's `b2` has coordinates (-1, 1) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

However, from Jennifer's perspective, these vectors are (1, 0) and (0, 1) respectively, as they define the meaning of those coordinates in her system <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. This highlights that different coordinate systems are like different "languages" to describe the same vectors in space <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. While the origin (0,0) is universally agreed upon <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>, the direction of axes and spacing of grid lines will differ based on the choice of [[unit_vectors_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Translating Between Coordinate Systems

### From Jennifer's Language to Our Language

To translate a vector described in Jennifer's coordinates (e.g., (-1, 2)) into our standard coordinates:
1.  Understand what Jennifer's coordinates mean: the vector is -1 times `b1` plus 2 times `b2` <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
2.  Substitute the coordinates of `b1` and `b2` as known in our system: `b1`=(2,1) and `b2`=(-1,1) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
3.  Perform the calculation: -1 * (2,1) + 2 * (-1,1) = (-2,-1) + (-2,2) = (-4,1) <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
    *   So, Jennifer's vector (-1,2) is (-4,1) in our system <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

This process is essentially [[linear_transformations | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. A "change of basis" matrix, where the columns are Jennifer's [[unit_vectors_and_basis_vectors | basis vectors]] (e.g., `b1` and `b2`) expressed in our coordinate system, can be used. Multiplying this matrix by a vector in Jennifer's coordinates translates it to our coordinates <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

> "A matrix whose columns represent Jennifer's basis vectors can be thought of as a transformation that moves our basis vectors, i-hat and j-hat... to Jennifer's basis vectors..." <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>
> This matrix effectively transforms our "misconception" of what Jennifer means (applying her coordinates to *our* basis) into the actual vector she's referring to <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Geometrically, this matrix transforms our grid into Jennifer's grid <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### From Our Language to Jennifer's Language

To go the other way (e.g., our (3,2) to Jennifer's (5/3, 1/3)), you use the **inverse** of the change of basis matrix <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. The inverse matrix "plays the first one backwards" <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

For Jennifer's basis vectors (2,1) and (-1,1), the change of basis matrix is:
```
[ 2  -1 ]
[ 1   1 ]
```
Its inverse is:
```
[ 1/3   1/3  ]
[ -1/3  2/3 ]
```
Multiplying this inverse matrix by our vector (3,2) yields (5/3, 1/3) <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

In summary:
*   **Matrix with Jennifer's basis as columns**: Translates vectors *from* her language *into* our language <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Inverse of that matrix**: Translates vectors *from* our language *into* her language <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Representing Linear Transformations in Different Coordinate Systems

When we represent a [[linear_transformations | linear transformation]] (like a 90-degree counterclockwise rotation) with a matrix, we observe where `i-hat` and `j-hat` land and record their landing spots in *our* coordinate system to form the matrix columns <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. This representation is heavily tied to our choice of [[unit_vectors_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

To find how Jennifer would describe the same [[linear_transformations | 90-degree rotation]] of space, a simple translation of our matrix columns is incorrect <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. Jennifer's matrix needs to represent where *her* [[unit_vectors_and_basis_vectors | basis vectors]] land, described in *her* language <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

The process involves a [[composition_of_linear_transformations | composition of three linear transformations]]:
1.  **Translate to our language**: Take a vector written in Jennifer's language and multiply it by the change of basis matrix (call it `A`, with Jennifer's basis vectors as columns) to get the vector in our language <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
2.  **Apply the transformation**: Multiply the result by our transformation matrix (call it `M`) to see where the vector lands, still in our language <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  **Translate back to Jennifer's language**: Multiply the result by the inverse change of basis matrix (`A⁻¹`) to get the transformed vector described in Jennifer's language <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

The overall transformation matrix in Jennifer's language is the product of these three matrices: **`A⁻¹MA`** <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. This composite matrix takes a vector in her language and returns its transformed version in her language <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

```
A⁻¹  *  M  *  A
```
```
(to Jennifer's (our transformation (to our language)
language)     in our language)
```

! note
Whenever you see an expression like `A⁻¹MA`, it represents a "mathematical empathy" <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The middle matrix (`M`) is how *you* see a transformation, and the outer two matrices (`A⁻¹` and `A`) represent a shift in perspective. The full matrix product (`A⁻¹MA`) is that same transformation as *someone else* sees it <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

The importance of alternate [[coordinate_systems_and_basis_vectors | coordinate systems]] will become clearer when discussing eigenvectors and eigenvalues <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.