---
title: Visualizing transformations with vectors
videoId: kYB8IZa5AuE
---

From: [[3blue1brown]] <br/> 

A foundational concept in linear algebra is the idea of a linear transformation and its relationship to matrices <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Focusing on two-dimensional space, transformations provide a visual understanding of how matrix-vector multiplication operates without relying on memorization <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## What is a Transformation?

A "transformation" is essentially a sophisticated term for a function <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. It takes inputs and produces outputs <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. In linear algebra, transformations specifically involve taking an input vector and converting it into an output vector <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

The word "transformation" is used to suggest a specific way of visualizing this input-output relationship <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. To understand functions of vectors, one can imagine movement <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. If a transformation maps an input vector to an output vector, one visualizes the input vector *moving* to the output vector <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. To grasp the entire transformation, one can imagine every possible input vector moving to its corresponding output vector <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

Instead of visualizing vectors as arrows, it's often clearer to conceptualize each vector as a single point—the point where its tip sits <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This way, understanding a transformation means observing every point in space moving to another point <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. For [[visualization_of_3d_vector_transformations | transformations in two dimensions]], visualizing the movement of points on an infinite grid can provide a comprehensive understanding of the transformation's shape <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Keeping a copy of the original grid in the background helps track the relative positions of points <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This [[visual understanding of linear transformations | visual understanding of linear transformations]] creates the feeling of space itself squishing and morphing <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Linear Transformations

Arbitrary transformations can be complex, but linear algebra focuses on a special, more manageable type: linear transformations <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Visually, a transformation is linear if it possesses two key properties <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>:
1.  All lines must remain lines and not become curved <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
2.  The origin must remain fixed in place <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

For instance, a transformation that causes lines to curve is not linear <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Similarly, one that keeps lines straight but moves the origin is also not linear <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. A crucial [[visual intuition of linear transformations | visual intuition of linear transformations]] is that linear transformations keep grid lines parallel and evenly spaced <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Describing Linear Transformations Numerically

To numerically describe a linear transformation—for example, to program it—one needs a formula that takes vector coordinates as input and provides their transformed coordinates as output <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

It turns out that for a 2D linear transformation, you only need to know where the two standard basis vectors, i-hat and j-hat, land <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. The property that grid lines remain parallel and evenly spaced implies an important consequence: any vector, say `v`, which can be expressed as a linear combination of `i-hat` and `j-hat` (e.g., `v = -1 * i-hat + 2 * j-hat`), will land at the *same* linear combination of where `i-hat` and `j-hat` landed <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
This means that if you know where `i-hat` and `j-hat` transform, you can deduce where any other vector `v` must go <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

For a general vector `(x, y)`, if `i-hat` lands at `(a, c)` and `j-hat` lands at `(b, d)`, then the vector `(x, y)` will land at `x * (a, c) + y * (b, d) = (ax + by, cx + dy)` <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This implies that a two-dimensional linear transformation is completely defined by just four numbers: the coordinates of where `i-hat` and `j-hat` land <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

## Matrices as Transformations

These four coordinates are conventionally packaged into a 2x2 grid of numbers called a [[matrix_representation_of_linear_transformations | 2x2 matrix]] <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The columns of this matrix represent the transformed `i-hat` and `j-hat` vectors <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

To find where a linear transformation, described by a [[matrix_representation of transformations | 2x2 matrix]], takes a specific vector, you perform [[matrix_vector_multiplication | matrix-vector multiplication]] <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This multiplication involves multiplying the coordinates of the vector by the corresponding columns of the matrix and summing the results <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. This process directly corresponds to adding the scaled versions of the new basis vectors <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

For a matrix with entries:
```
[ A  B ]
[ C  D ]
```
and a vector `(x, y)`, the [[matrix representation of transformations | matrix-vector multiplication]] is defined as:
```
[ A  B ] * [ x ] = [ Ax + By ]
[ C  D ]   [ y ]   [ Cx + Dy ]
```
Remember, the first column `(A, C)` is where `i-hat` lands, and the second column `(B, D)` is where `j-hat` lands <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. The result is the new vector after the transformation <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### Examples of Matrices and their Transformations

*   **90-degree counterclockwise rotation**:
    *   `i-hat` lands on `(0, 1)`
    *   `j-hat` lands on `(-1, 0)`
    *   Matrix: `[[0, -1], [1, 0]]` <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>
*   **Shear**:
    *   `i-hat` remains fixed at `(1, 0)`
    *   `j-hat` moves to `(1, 1)`
    *   Matrix: `[[1, 1], [0, 1]]` <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>

If the vectors where `i-hat` and `j-hat` land are linearly dependent (one is a scaled version of the other), the linear transformation squishes all of 2D space onto a single line—the one-dimensional span of those two vectors <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## Importance of this Visual Interpretation

In summary, linear transformations are movements of space that keep grid lines parallel and evenly spaced, and fix the origin <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. These transformations are concisely described by the coordinates of where each basis vector lands <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. [[Matrix representations and transformations | Matrices]] provide a language to describe these transformations, with their columns indicating the destination of the basis vectors <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. [[Matrix representations of linear transformations | Matrix-vector multiplication]] is simply the computation of what a transformation does to a given vector <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

The key takeaway is that every time a matrix is encountered, it can be interpreted as a specific transformation of space <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. This deep understanding is crucial for grasping more advanced linear algebra concepts, such as [[matrix_multiplication | matrix multiplication]], determinants, change of basis, and eigenvalues <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.