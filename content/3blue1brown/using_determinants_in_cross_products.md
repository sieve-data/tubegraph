---
title: Using determinants in cross products
videoId: eu6i7WJeinw
---

From: [[3blue1brown]] <br/> 

This article explores the concept of the [[introduction_to_cross_products | cross product]], detailing its standard introduction and computation, particularly emphasizing the role of determinants. It differentiates between the [[cross_product_in_two_dimensions | cross product in two dimensions]] and the true 3D cross product, setting the stage for a deeper understanding through linear transformations <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Cross Product in Two Dimensions

When considering two vectors, `v` and `w`, in two dimensions, their cross product relates to the parallelogram they span <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This parallelogram is formed by taking a copy of `v` and moving its tail to the tip of `w`, and a copy of `w` to the tip of `v` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

The cross product of `v` and `w` (written as `v x w`) is defined as the area of this parallelogram, with an important consideration for orientation <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

*   If `v` is to the right of `w`, `v x w` is positive and equals the parallelogram's area <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   If `v` is to the left of `w`, `v x w` is negative, equaling the negative area of the parallelogram <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

This definition implies that the order of vectors in a cross product matters; swapping `v` and `w` will negate the result (`w x v` = -(`v x w`)) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The orientation is fundamentally defined by the order of basis vectors, such as `i-hat x j-hat` yielding a positive result <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Computing the 2D Cross Product with Determinants

The [[determinant_computation_for_2d_and_3d_transformations | determinant]] is crucial for computing the 2D cross product <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. To find `v x w`:
1.  Create a matrix where the coordinates of `v` form the first column and the coordinates of `w` form the second column <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
2.  Compute the [[determinant_properties_and_matrix_multiplication | determinant]] of this matrix <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

```
Example: v = [-3, 1], w = [2, 1]
Matrix:
|-3  2|
| 1  1|

Determinant: (-3 * 1) - (2 * 1) = -3 - 2 = -5
```
Thus, `v x w = -5` <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. The area of the parallelogram is 5, and since `v` is to the left of `w`, the result is negative <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

#### Why the Determinant Works

The reason the [[determinant_computation_for_2d_and_3d_transformations | determinant]] yields this value is rooted in linear transformations <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. A matrix with `v` and `w` as columns represents a linear transformation that maps the basis vectors `i-hat` and `j-hat` to `v` and `w`, respectively <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

The [[determinant_properties_and_matrix_multiplication | determinant]] measures how areas change under a transformation <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Specifically, it reveals how the unit square (defined by `i-hat` and `j-hat` with an area of 1) transforms into the parallelogram defined by `v` and `w` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The determinant's sign also indicates if orientation was flipped during the transformation, resulting in a negative value when `v` is to the left of `w` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

#### Properties of the 2D Cross Product
*   When vectors are perpendicular or nearly perpendicular, their cross product (and thus the parallelogram's area) tends to be larger <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   Scaling one of the vectors scales the cross product by the same factor. For example, `3v x w` will be 3 times the value of `v x w` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## The True Cross Product in Three Dimensions

While the 2D operation is mathematically valid, the "true" [[introduction_to_cross_products | cross product]] combines two 3D vectors to produce a new 3D vector <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

This resulting 3D vector has:
*   **Length (Magnitude)**: The area of the parallelogram defined by the two original vectors <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Direction**: Perpendicular to the parallelogram <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. The specific direction is determined by the [[right_hand_rule_for_cross_products | right hand rule]] <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>:
    1.  Point your right forefinger in the direction of the first vector (`v`).
    2.  Point your middle finger in the direction of the second vector (`w`).
    3.  Your thumb will then point in the direction of `v x w` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

```
Example: v = [0, 0, 2] (2 units in z-direction), w = [0, 2, 0] (2 units in y-direction)
*   Parallelogram is a square with area 4 <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   Using the right-hand rule, the cross product points in the negative x-direction <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   Result: `-4 * i-hat` (or `[-4, 0, 0]`) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
```

### Computing the 3D Cross Product with Determinants

For [[3d_cross_product_computations | 3D cross product computations]], a specific determinant process is often used <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
1.  Construct a 3D matrix.
2.  The second and third columns contain the coordinates of `v` and `w` respectively <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
3.  The first column contains the basis vectors `i-hat`, `j-hat`, and `k-hat` <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
4.  Compute the [[determinant_properties_and_matrix_multiplication | determinant]] of this matrix, treating the basis vectors as if they were numbers <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

While this method appears to be a "notational trick" where basis vectors are temporarily treated as numbers <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>, the computation yields a linear combination of these basis vectors <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This resulting vector is perpendicular to `v` and `w`, its magnitude equals the parallelogram's area, and its direction adheres to the [[right_hand_rule_for_cross_products | right hand rule]] <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

The use of the [[determinant_computation_for_2d_and_3d_transformations | determinant]] in this context is not a coincidence <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. A deeper understanding of this process, involving the concept of duality, exists but is often explored in more advanced discussions on linear algebra <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. For general understanding, the key is knowing the geometric representation of the cross product vector <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.