---
title: Cross product in two dimensions
videoId: eu6i7WJeinw
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_cross_products | cross product]], like the dot product, can be understood both through its standard introduction and a deeper view related to [[transformations_between_different_dimensions | linear transformations]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This article focuses on the [[introduction_to_cross_products | cross product]] as it applies in two dimensions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Geometric Interpretation

When considering two vectors, `v` and `w`, in two dimensions, they naturally [[span_of_vectors_in_different_dimensions | span]] a parallelogram <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This parallelogram is formed by taking a copy of `v` and moving its tail to the tip of `w`, and a copy of `w` to the tip of `v`, enclosing a specific four-sided figure <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

The [[introduction_to_cross_products | cross product]] of `v` and `w` (written as `v` × `w`) is related to the area of this parallelogram <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. However, it also incorporates the concept of orientation <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>:
*   If `v` is to the right of `w`, `v` × `w` is positive and equals the parallelogram's area <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   If `v` is to the left of `w`, `v` × `w` is negative and equals the negative of the parallelogram's area <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Order Matters
This definition implies that the order of the vectors in a [[introduction_to_cross_products | cross product]] is crucial <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Swapping the order, such as calculating `w` × `v` instead of `v` × `w`, will result in the negative of the original [[introduction_to_cross_products | cross product]] value <a class="yt_timestamp" data-t="00:01:31">[00:01:31]</a>. The orientation is fundamentally defined by the order of your basis vectors (e.g., `i-hat` before `j-hat` yields a positive result for `i-hat` × `j-hat`) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

For example, if `v` is to the left of `w` and the parallelogram's area is 7, then `v` × `w` would be -7 <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Computation Using Determinants

To compute the 2D [[introduction_to_cross_products | cross product]] without knowing the area beforehand, [[using_determinants_in_cross_products | determinants]] are used <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
For `v` × `w`:
1.  Form a 2x2 matrix where the coordinates of `v` make up the first column.
2.  The coordinates of `w` make up the second column.
3.  Compute the determinant of this matrix <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Connection to Linear Transformations
This method works because a matrix with `v` and `w` as its columns represents a [[transformations_between_different_dimensions | linear transformation]] that maps the standard basis vectors (`i-hat` and `j-hat`) to `v` and `w`, respectively <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The [[using_determinants_in_cross_products | determinant]] of a matrix measures how areas change under the corresponding [[transformations_between_different_dimensions | transformation]] <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

The "unit square" formed by `i-hat` and `j-hat` (which has an area of 1) is transformed into the parallelogram defined by `v` and `w` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Therefore, the [[using_determinants_in_cross_products | determinant]] directly gives the area of this parallelogram <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Furthermore, if the transformation flips the orientation (i.e., if `v` is to the left of `w`), the [[using_determinants_in_cross_products | determinant]] will be negative, accurately reflecting the sign convention of the [[introduction_to_cross_products | cross product]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

**Example**:
If `v` = (-3, 1) and `w` = (2, 1) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, the matrix is:
```
[-3  2]
[ 1  1]
```
The [[using_determinants_in_cross_products | determinant]] is (-3 * 1) - (2 * 1) = -3 - 2 = -5 <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. This means the parallelogram has an area of 5, and `v` is to the left of `w` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Intuitive Properties

Playing with this concept can build intuition <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>:
*   When two vectors are perpendicular (or close to it), their [[introduction_to_cross_products | cross product]] tends to be larger <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. This is because the area of the parallelogram is maximized when the vectors are orthogonal <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   Scaling one of the vectors scales the area of the parallelogram proportionally <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. For example, `(3v)` × `w` will be three times `v` × `w` <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

## Distinction from the True Cross Product

It is important to note that while the 2D operation described above is a valid mathematical concept, it is technically not the "true" [[introduction_to_cross_products | cross product]] in the standard definition <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The standard [[introduction_to_cross_products | cross product]] takes two 3D vectors and produces a new 3D vector <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

In 3D, the length of the resulting vector is still the area of the parallelogram formed by the two input vectors <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The direction of this 3D vector is perpendicular to the parallelogram, determined by the [[right_hand_rule_for_cross_products | right-hand rule]] <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. [[3d_cross_product_computations | Computing the 3D cross product]] also involves [[using_determinants_in_cross_products | determinants]], specifically a 3D determinant where the first column consists of basis vectors `i-hat`, `j-hat`, and `k-hat` <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. While this 3D computation can seem like a "notational trick," there's a deeper reason for it related to the concept of duality <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.