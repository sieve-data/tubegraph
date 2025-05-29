---
title: Matrix multiplication and transformations
videoId: O85OWBJ2ayo
---

From: [[3blue1brown]] <br/> 

When thinking about matrices, it is helpful to consider them as [[linear_transformations_and_matrices | transformations]] <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. This perspective offers a clear view of what matrices actually do to vectors in space.

## Matrices as Transformations
A core idea in understanding [[matrix_representation_of_transformations | matrix representation of transformations]] is how a matrix acts on basis vectors <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
When you [[matrix_vector_multiplication | multiply a matrix]] by the vector `[1, 0]`, it effectively "pulls out" the first column of that matrix <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Similarly, [[matrix_vector_multiplication | multiplying by `[0, 1]` pulls out the second column]] <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

This means that you can discern a matrix's transformational action by simply looking at its columns <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. The columns tell you where the standard basis vectors (like `[1, 0]` and `[0, 1]`) are mapped to after the transformation <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

The way a matrix transforms *any other vector* is a result of scaling and adding these basis vector transformations according to the vector's coordinates <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This forms the basis for [[visualizing_linear_transformations_with_matrices | visualizing linear transformations with matrices]].

## Examples of Matrix Transformations
### Rotation Matrix
Consider a matrix like `[0, -1; 1, 0]`. From its columns, it's evident that it transforms the first basis vector `[1, 0]` to `[0, 1]` and the second basis vector `[0, 1]` to `[-1, 0]` <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This specific matrix is recognized as a 90-degree rotation matrix <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

A more general rotation matrix, capable of rotating by `t` radians, appears as:
```
[cos(t), -sin(t);
 sin(t),  cos(t)]
```
Again, reading its columns reveals that it maps the first basis vector to `[cos(t), sin(t)]` and the second to `[-sin(t), cos(t)]`, which aligns with a rotation by `t` radians <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

### Applying Transformations
[[Matrix multiplication as applying transformations | Multiplying this rotation matrix]] by an initial state vector (e.g., `[x0, y0]`) allows you to predict where that state will end up after `t` units of time <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. The resulting matrix, often derived from operations like matrix exponentiation, describes the transition from an initial state to a final state <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.

Another example illustrates a transformation that involves squishing along one diagonal and stretching along another <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>. This indicates that matrices can represent complex deformations of space, not just simple rotations or reflections.

In essence, [[matrix_vector_multiplication_and_transformations | matrix-vector multiplication]] serves as the mechanism by which these geometric transformations are applied to vectors <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. The matrix, in turn, provides a compact [[matrix_representation_of_linear_transformations | representation of the linear transformation]] itself <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.