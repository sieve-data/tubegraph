---
title: Inverse matrix and translating between coordinate systems
videoId: P2LTAUO1TdA
---

From: [[3blue1brown]] <br/> 

A coordinate system provides a method to translate between vectors and sets of numbers [00:01:17]. Our standard coordinate system utilizes basis vectors i-hat (unit vector to the right) and j-hat (unit vector straight up) [00:00:40]. These basis vectors implicitly define the assumptions of our system, such as the direction of motion for each coordinate and the unit of distance [00:00:55]. From a linear algebra perspective, each coordinate is a scalar that stretches or squishes these basis vectors, and their tip-to-tail sum describes the vector [00:00:27]. For example, a vector with coordinates 3,2 means moving three units right (3 * i-hat) and two units up (2 * j-hat) [00:00:18].

The visual grid commonly used to animate 2D space is merely a construct that depends on the chosen basis vectors, as space itself has no intrinsic grid [00:03:26]. While the origin (0,0) is universally agreed upon [00:03:53], the directions of axes and the spacing of grid lines will differ depending on the chosen basis vectors [00:04:03].

## Translating Between Coordinate Systems

Different coordinate systems arise from using a different set of basis vectors. For instance, a friend named Jennifer might use basis vectors b1 and b2 [00:01:35], which we might describe as b1 = (2,1) and b2 = (-1,1) in our standard system [00:02:44]. However, from Jennifer's perspective, these vectors are fundamental and are represented as (1,0) and (0,1) in her own system, defining the meaning of those coordinates for her [00:02:59].

A vector described as 3,2 in our system (using i-hat and j-hat) would be described as 5/3, 1/3 in Jennifer's system (using b1 and b2) [00:01:51]. This means that in her system, the vector is 5/3 times b1 plus 1/3 times b2 [00:02:06].

### Translating from Jennifer's Language to Ours

To translate a vector described in Jennifer's coordinate system (e.g., -1,2) into our system, we interpret her coordinates as scaling her basis vectors and then sum them up using our understanding of her basis vectors [00:04:29]:
(-1) * b1 + (2) * b2 = (-1) * (2,1) + (2) * (-1,1) = (-2,-1) + (-2,2) = (-4,1) [00:04:49].

This process is equivalent to [[Matrix representations and transformations | matrix-vector multiplication]] [00:05:18]. The matrix used for this translation is one whose columns are Jennifer's basis vectors, expressed in our coordinate system [00:05:21]. This matrix can be thought of as a [[Linear transformations in linear algebra | linear transformation]] that moves our basis vectors (i-hat, j-hat) to Jennifer's basis vectors (b1, b2) [00:05:39].

The full process involves taking our "misconception" of what Jennifer means (applying her coordinates in our system) and then applying this transformation to arrive at the actual vector she is referring to [00:06:33]. Numerically, this matrix translates a vector described in her language to our language [00:06:52].

### Translating from Our Language to Jennifer's

To translate a vector from our coordinate system to Jennifer's, one must use the [[inverse matrices | inverse]] of the change of basis matrix [00:07:32]. The [[inverse matrices | inverse]] of a transformation essentially "plays it backwards" [00:07:43]. For instance, if the change of basis matrix translating Jennifer's language to ours has columns (2,1) and (-1,1), its [[inverse matrices | inverse]] matrix will have columns (1/3, -1/3) and (1/3, 2/3) [00:07:58].

To find the coordinates of our vector (3,2) in Jennifer's system, we multiply this [[inverse matrices | inverse]] matrix by our vector (3,2):
```
[ 1/3  1/3 ]   [ 3 ]   [ (1/3)*3 + (1/3)*2 ]   [ 5/3 ]
[-1/3  2/3 ] * [ 2 ] = [(-1/3)*3 + (2/3)*2 ] = [ 1/3 ]
```
This calculation yields 5/3, 1/3, which are the coordinates of the vector in Jennifer's system [00:08:11].

In summary:
*   The [[Mathematical representation with 3x3 matrices | matrix]] with Jennifer's basis vectors (expressed in our coordinates) as its columns translates vectors from her language to ours [00:08:35].
*   Its [[inverse matrices | inverse]] matrix does the opposite, translating from our language to hers [00:08:46].

## Representing Transformations in Different Coordinate Systems

When we represent a [[Linear transformations in linear algebra | linear transformation]], such as a 90-degree counterclockwise rotation, with a [[matrix representation of transformations | matrix]], we observe where our basis vectors (i-hat and j-hat) land, and their landing coordinates become the columns of our [[matrix representation of transformations | matrix]] [00:09:12]. This [[matrix representation of transformations | representation]] is tied to our specific choice of basis vectors [00:09:36].

To find how Jennifer would describe this same 90-degree rotation, we cannot simply translate the columns of our rotation matrix into her language [00:09:59]. Jennifer's [[matrix representation of transformations | matrix]] must describe where *her* basis vectors land, and those landing spots must be described in *her* language [00:10:07].

The process for finding a [[matrix representation of linear transformations | transformation matrix in another basis]] (Jennifer's perspective) involves a sequence of three [[Matrix representations of linear transformations | matrix multiplications]] [00:11:04]:

1.  **Translate to our language:** Take a vector written in Jennifer's language and multiply it by the change of basis matrix (A), which has Jennifer's basis vectors as columns in our language. This yields the vector in our language [00:10:23].
2.  **Apply the transformation (in our language):** Multiply the result from step 1 by our [[matrix representation of linear transformations | transformation matrix]] (M) [00:10:43]. This gives the transformed vector, still in our language [00:10:49].
3.  **Translate back to Jennifer's language:** Multiply the result from step 2 by the [[inverse matrices | inverse]] of the change of basis matrix (A⁻¹) [00:10:53]. This gives the transformed vector in Jennifer's language [00:10:57].

This composition of three matrices: **A⁻¹ * M * A** results in the [[Linear transformations and change of basis | transformation matrix]] as seen in Jennifer's coordinate system [00:11:11]. This matrix takes a vector in her language and outputs its transformed version, also in her language [00:11:19].

The structure A⁻¹ * M * A often signifies "mathematical empathy" [00:12:03]. The middle matrix (M) represents a transformation from our perspective, while the outer two matrices (A⁻¹ and A) represent the shift in perspective. The entire product describes the *same transformation* but as seen by someone else (Jennifer) [00:12:07].

Understanding alternate coordinate systems is crucial, and the next video will explore eigenvectors and eigenvalues, providing a significant application for this concept [00:12:22].