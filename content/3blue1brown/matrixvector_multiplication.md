---
title: Matrixvector multiplication
videoId: P2LTAUO1TdA
---

From: [[3blue1brown]] <br/> 

## Understanding Coordinate Systems and Basis Vectors

A vector in 2D space can be described using coordinates, for example, a vector with coordinates 3,2 means moving three units to the right and two units up from its tail to its tip <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. In linear algebra, these numbers are thought of as scalars that stretch or squish vectors <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

This description is tied to a standard coordinate system defined by special vectors called basis vectors <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:
*   **i-hat**: The vector with length 1 pointing to the right, scaled by the first coordinate <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **j-hat**: The vector with length 1 pointing straight up, scaled by the second coordinate <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

The tip-to-tail sum of these two scaled vectors is what the coordinates describe <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. These basis vectors encapsulate assumptions about the coordinate system, such as which direction is rightward or upward, and how far a unit of distance is <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Alternative Coordinate Systems

Different sets of basis vectors define different coordinate systems <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. For example, a friend named Jennifer might use basis vectors b1 and b2 <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>:
*   b1: Points up and slightly to the right (described as 2,1 in our standard system) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a> <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   b2: Points left and up (described as -1,1 in our standard system) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a> <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

From Jennifer's perspective, these vectors have coordinates 1,0 and 0,1, respectively, defining the meaning of those coordinates in her system <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. While we observe the same vectors in space, Jennifer uses different numbers to describe them <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. The origin (0,0) is consistent across all systems, but the direction of axes and spacing of grid lines will differ based on the chosen basis vectors <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Translating Between Coordinate Systems

A natural question arises: how do we translate vector descriptions between different coordinate systems <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>?

### From Jennifer's System to Ours

If Jennifer describes a vector with coordinates -1,2, this means the vector is -1 times b1 plus 2 times b2 <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. To translate this into our system:
1.  Represent Jennifer's basis vectors (b1 and b2) in our coordinates: b1 = (2,1) and b2 = (-1,1) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
2.  Perform the [[vector_addition_and_scalar_multiplication | scalar multiplication and vector addition]] using our coordinates:
    (-1) * (2,1) + (2) * (-1,1) = (-2,-1) + (-2,2) = (-4,1) <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
So, the vector Jennifer describes as -1,2 is described as -4,1 in our system <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

This process is precisely [[matrixvector_multiplication | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. The matrix used for this translation, known as the **change of basis matrix**, has Jennifer's basis vectors as its columns (in our language) <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>:

$$
\begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix}
\begin{pmatrix} -1 \\ 2 \end{pmatrix}
= \begin{pmatrix} (-1 \times 2) + (2 \times -1) \\ (-1 \times 1) + (2 \times 1) \end{pmatrix}
= \begin{pmatrix} -4 \\ 1 \end{pmatrix}
$$

### Interpreting Matrix-Vector Multiplication as a Linear Transformation

Understanding [[matrixvector_multiplication | matrix-vector multiplication]] as applying a [[matrix_representations_and_transformations | linear transformation]] provides intuition <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. A matrix whose columns represent Jennifer's basis vectors can be viewed as a [[matrix_representations_of_linear_transformations | transformation]] that moves our basis vectors (i-hat and j-hat) to Jennifer's basis vectors (b1 and b2) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

When this transformation is applied to a vector represented in our system (e.g., -1 times i-hat plus 2 times j-hat), a key property of linear transformations ensures the resulting vector will be the same linear combination of the *new* basis vectors (the landing spots of i-hat and j-hat) <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. In essence, this matrix transforms our "misconception" of what Jennifer means (if we use her coordinates in our system) into the actual vector she is referring to <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

> [!NOTE] Interpretation
> Geometrically, this matrix transforms our grid into Jennifer's grid. Numerically, it translates a vector described in Jennifer's language to our language <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### From Our System to Jennifer's

To go the other way – translating a vector from our system (e.g., 3,2) into Jennifer's coordinates (5/3, 1/3) <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a> – we use the inverse of the change of basis matrix <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

The inverse of a transformation effectively "plays it backwards" <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. For the example where Jennifer's basis matrix is $\begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix}$, its inverse is $\begin{pmatrix} 1/3 & 1/3 \\ -1/3 & 2/3 \end{pmatrix}$ <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

To find the coordinates of vector (3,2) in Jennifer's system, we multiply it by this inverse matrix <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>:

$$
\begin{pmatrix} 1/3 & 1/3 \\ -1/3 & 2/3 \end{pmatrix}
\begin{pmatrix} 3 \\ 2 \end{pmatrix}
= \begin{pmatrix} (1/3 \times 3) + (1/3 \times 2) \\ (-1/3 \times 3) + (2/3 \times 2) \end{pmatrix}
= \begin{pmatrix} 1 + 2/3 \\ -1 + 4/3 \end{pmatrix}
= \begin{pmatrix} 5/3 \\ 1/3 \end{pmatrix}
$$

So, the vector (3,2) in our system is (5/3, 1/3) in Jennifer's system <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

> [!SUMMARY] Translation Summary
> *   The matrix whose columns represent Jennifer's basis vectors (in our coordinates) translates vectors from her language into our language <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
> *   Its inverse matrix does the opposite, translating from our language to hers <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Translating Linear Transformations Between Coordinate Systems

Matrices are also used to represent [[matrix_representations_and_transformations | linear transformations]] <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. Our matrix for a 90-degree counterclockwise rotation, for instance, has columns (0,1) and (-1,0), representing where i-hat and j-hat land <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This representation is specific to our choice of basis vectors <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

To find how Jennifer would describe this same 90-degree rotation, we need a matrix that operates on vectors in *her* language and outputs transformed vectors *in her language* <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

This is achieved by a composition of three transformations, often seen as an expression like $A^{-1}MA$:
1.  **Translate to our language (A):** Take any vector written in Jennifer's language and multiply it by her change of basis matrix (A). This converts the vector into our coordinate system <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
2.  **Apply the transformation (M):** Apply our standard transformation matrix (M, e.g., the 90-degree rotation matrix) to the vector now expressed in our language <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. The result is the transformed vector, still in our language <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
3.  **Translate back to Jennifer's language (A<sup>-1</sup>):** Apply the inverse of the change of basis matrix ($A^{-1}$) to get the final transformed vector back in Jennifer's language <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

This composition of three matrices ($A^{-1}MA$) results in the [[associative_property_of_matrix_multiplication | transformation matrix]] as seen in Jennifer's coordinate system <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. When Jennifer uses this matrix with a vector from her system, it returns the transformed version of that vector, also expressed in her system <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

> [!NOTE] Mathematical Empathy
> The expression $A^{-1}MA$ suggests a "mathematical empathy" <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. The middle matrix (M) represents a transformation as *we* see it, while the outer matrices ($A^{-1}$ and A) represent a shift in perspective. The full matrix product represents that same transformation, but as *someone else* sees it <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.