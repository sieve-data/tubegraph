---
title: 3D cross product computations
videoId: eu6i7WJeinw
---

From: [[3blue1brown]] <br/> 

This article explores the concept of the [[introduction_to_cross_products | cross product]], detailing both its standard geometric interpretation and the computational methods, particularly in three dimensions <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Cross Product in Two Dimensions (Context)

While the "true" [[introduction_to_cross_products | cross product]] operates in 3D space, it's often introduced by first considering two-dimensional vectors <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Geometric Interpretation (2D)

Given two vectors, `v` and `w`, their [[cross_product_in_two_dimensions | cross product]] is defined by the area of the parallelogram they span <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Magnitude**: The area of the parallelogram formed by `v` and `w` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   **Orientation**: The sign of the [[cross_product_in_two_dimensions | cross product]] depends on the relative orientation of the vectors <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   If `v` is to the right of `w`, `v` cross `w` is positive and equal to the parallelogram's area <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   If `v` is to the left of `w`, `v` cross `w` is negative, equal to the negative area <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Order Matters**: Swapping the order of `v` and `w` reverses the sign of the [[cross_product_in_two_dimensions | cross product]] (e.g., `w` cross `v` is the negative of `v` cross `w`) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The order of basis vectors (i-hat cross j-hat being positive) defines this orientation <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Computation (2D)

To compute the [[cross_product_in_two_dimensions | cross product]] of `v` and `w` in 2D, one constructs a matrix where the columns are the coordinates of `v` and `w`, respectively, and then computes the [[determinant_computation_for_2d_and_3d_transformations | determinant]] of this matrix <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

```
If v = [v₁, v₂] and w = [w₁, w₂]
v x w = det(
    [v₁  w₁]
    [v₂  w₂]
) = v₁w₂ - v₂w₁
```
This works because the [[determinant_computation_for_2d_and_3d_transformations | determinant]] measures how areas change due to a linear transformation, and the parallelogram formed by `v` and `w` can be seen as the transformed unit square <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. A negative [[determinant_computation_for_2d_and_3d_transformations | determinant]] indicates an orientation flip <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## The True Cross Product in Three Dimensions

The [[introduction_to_cross_products | true cross product]] combines two 3D vectors to produce a new 3D vector <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### Geometric Interpretation (3D)

*   **Magnitude**: The length of the resulting vector is the area of the parallelogram defined by the two vectors being crossed <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Direction**: The direction of the new vector is perpendicular to the parallelogram <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. To resolve the ambiguity of "which way" (two possible perpendicular directions), the [[right_hand_rule_for_cross_products | right hand rule]] is applied <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
    *   Point your right hand's forefinger in the direction of the first vector (`v`).
    *   Stick out your middle finger in the direction of the second vector (`w`).
    *   Your thumb then points in the direction of the [[introduction_to_cross_products | cross product]] (`v` cross `w`) <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

For example, if `v` is a vector with length 2 pointing in the z-direction, and `w` is a vector with length 2 pointing in the y-direction, their cross product is a vector with length 4 (the area of the 2x2 square they form). Using the [[right_hand_rule_for_cross_products | right hand rule]], the cross product points in the negative x-direction, resulting in negative 4 times i-hat <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### Computation (3D)

A common and easier way to compute the [[introduction_to_cross_products | 3D cross product]] involves a process using the 3D [[determinant_computation_for_2d_and_3d_transformations | determinant]] <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

To find `v` cross `w`:
1.  Construct a 3x3 matrix.
2.  The first column contains the basis vectors: i-hat, j-hat, and k-hat <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
3.  The second column contains the coordinates of `v` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
4.  The third column contains the coordinates of `w` <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
5.  Compute the [[determinant_computation_for_2d_and_3d_transformations | determinant]] of this matrix <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

This computation works by treating the basis vectors as if they were numbers during the [[determinant_computation_for_2d_and_3d_transformations | determinant]] calculation, which results in a linear combination of those basis vectors. The resulting vector is the unique vector perpendicular to `v` and `w`, whose magnitude is the area of their parallelogram, and whose direction obeys the [[right_hand_rule_for_cross_products | right hand rule]] <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

While often presented as a "notational trick," the importance of the [[determinant_computation_for_2d_and_3d_transformations | determinant]] and the placement of basis vectors is not coincidental <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. A deeper understanding of this connection involves the concept of duality, which is explored in a separate video <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.