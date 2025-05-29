---
title: Matrix vector multiplication and transformations
videoId: P2LTAUO1TdA
---

From: [[3blue1brown]] <br/> 

## Understanding Coordinate Systems and Basis Vectors

A vector in 2D space is typically described using coordinates, such as (3, 2), which indicates a movement of three units to the right and two units up from the tail to the tip <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. In linear algebra, these coordinates are viewed as scalars that stretch or squish basis vectors <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

The standard way to describe coordinates involves:
*   **i-hat**: A vector of length 1 pointing to the right <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **j-hat**: A vector of length 1 pointing straight up <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

The first coordinate scales i-hat, and the second scales j-hat. The tip-to-tail sum of these scaled vectors describes the original vector <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. These two special vectors, i-hat and j-hat, are known as the **basis vectors** of the standard coordinate system <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. They encapsulate all implicit assumptions of the coordinate system, including direction and unit distance <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Any method of translating between vectors and sets of numbers is called a coordinate system <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Alternate Coordinate Systems (Change of Basis)

It is possible to use a different set of basis vectors <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. For example, if a friend, Jennifer, uses basis vectors b1 and b2 (where b1 points up and to the right, and b2 points left and up) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
A vector that is (3, 2) in the standard system (using i-hat and j-hat) would be described as (5/3, 1/3) in Jennifer's system <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This means the vector is formed by scaling b1 by 5/3, scaling b2 by 1/3, and then adding them together <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

From our perspective (standard system), Jennifer's basis vectors are described as:
*   b1: (2, 1) <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
*   b2: (-1, 1) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>

However, from Jennifer's perspective, within her own system, these vectors are (1, 0) and (0, 1) respectively, as they define the meaning of those coordinates in her world <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. While everyone observes the same vectors in space, different coordinate systems use different numbers and words to describe them <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

Visualizations of coordinate systems, like a square grid, are constructs tied to the chosen basis <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Space itself has no intrinsic grid <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. The origin (0,0) remains consistent across systems, as it represents scaling any vector by zero <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. However, the directions of axes and grid line spacing will differ based on the choice of basis vectors <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

## Translating Between Coordinate Systems

### From Another System to Ours

To translate a vector described in Jennifer's system (e.g., (-1, 2)) to our standard system, we use the definition of her coordinates: the vector is -1 times b1 plus 2 times b2 <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
Since we know b1=(2,1) and b2=(-1,1) in our system, we can calculate:
(-1) * (2, 1) + (2) * (-1, 1) = (-2, -1) + (-2, 2) = (-4, 1) <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

This process of scaling each of Jennifer's basis vectors by the corresponding coordinates and adding them is equivalent to [[matrix_vector_multiplication|matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. The matrix used for this translation has Jennifer's basis vectors (in our language) as its columns <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

This matrix can be understood as a [[matrix_multiplication_and_transformations|linear transformation]] that maps our standard basis vectors (i-hat and j-hat) to Jennifer's basis vectors (b1 and b2) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. If we take a vector in our system (e.g., (-1, 2) meant as -1 * i-hat + 2 * j-hat) and apply this transformation, the result is the same linear combination but of the *new* basis vectors (-1 * where i-hat lands + 2 * where j-hat lands) <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Thus, this matrix transforms our 'misconception' of what Jennifer means (interpreting her coordinates in our system) into the actual vector she is referring to <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Numerically, it translates a vector from her language to ours <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### From Our System to Another

To translate a vector from our system (e.g., (3, 2)) to Jennifer's system, we use the inverse of the change of basis matrix <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. The inverse of a transformation corresponds to playing the first one backward <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

For Jennifer's basis vectors (b1=(2,1), b2=(-1,1)), the inverse change of basis matrix has columns (1/3, -1/3) and (1/3, 2/3) <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Multiplying this inverse matrix by the vector (3, 2) yields (5/3, 1/3) <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

In summary:
*   The matrix whose columns are Jennifer's basis vectors (in our coordinates) translates vectors from her language to ours <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   Its inverse matrix does the opposite, translating from our language to hers <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Representing Transformations in Different Coordinate Systems

When [[matrix_representation_of_linear_transformations|representing linear transformations with matrices]], the representation is heavily tied to the chosen basis vectors <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. For example, a 90-degree counterclockwise rotation in our system is represented by a matrix whose columns are where i-hat (0,1) and j-hat (-1,0) land after the rotation <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

To find how Jennifer would describe this same 90-degree rotation of space, her matrix needs to represent where *her* basis vectors land, described in *her* language <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

The process to find a transformation matrix in a different coordinate system involves a composition of three transformations:
1.  **Translate to our language:** Start with a vector written in Jennifer's language. Multiply it by the change of basis matrix (let's call it 'A', with Jennifer's basis vectors as columns) to express it in our language <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
2.  **Apply the transformation:** Multiply the result by the transformation matrix ('M', the rotation matrix in our language) to apply the rotation <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
3.  **Translate back to Jennifer's language:** Multiply the result by the inverse of the change of basis matrix ('A inverse') to express the transformed vector back in Jennifer's language <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

This sequence of operations forms a single matrix product: **A inverse * M * A** <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. This composite matrix takes a vector in Jennifer's language and returns its transformed version in her language <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

This mathematical expression (A inverse * M * A) suggests a concept of "mathematical empathy" <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The middle matrix (M) represents the transformation as seen from our perspective, while the outer two matrices (A inverse and A) represent the shift in perspective, or empathy <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. The entire matrix product represents the same transformation, but as someone else sees it <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.