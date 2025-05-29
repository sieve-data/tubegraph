---
title: Introduction to cross products
videoId: eu6i7WJeinw
---

From: [[3blue1brown]] <br/> 

The cross product is a fundamental operation in linear algebra, often introduced alongside the [[geometric_interpretation_of_dot_products | dot product]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While the [[geometric_interpretation_of_dot_products | dot product]] relates to projections and how vectors stretch, the cross product is deeply connected to areas and volumes and how orientation changes under [[introduction_to_linear_transformations | linear transformations]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## [[cross_product_in_two_dimensions | Cross Product in Two Dimensions]]

In two dimensions, the cross product of two vectors, `v` and `w`, is a scalar value <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Geometric Interpretation

The cross product `v × w` represents the area of the parallelogram spanned by `v` and `w` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This parallelogram is formed by taking a copy of `v` and moving its tail to the tip of `w`, and a copy of `w` and moving its tail to the tip of `v` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

However, it's not just the area; orientation must also be considered <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>:
*   If `v` is on the right of `w`, `v × w` is positive and equal to the parallelogram's area <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   If `v` is on the left of `w`, `v × w` is negative, specifically the negative area of the parallelogram <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

This implies that the order of the vectors matters: `w × v` will be the negative of `v × w` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>, <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The orientation is defined by the order of the basis vectors, such as `i-hat × j-hat` being positive <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

For example, if the parallelogram's area is 7 and `v` is on the left of `w`, then `v × w = -7` <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Computation: [[using_determinants_in_cross_products | Using Determinants]]

The [[cross_product_in_two_dimensions | 2D cross product]] `v × w` can be computed using the determinant <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
If `v` has coordinates `(v_x, v_y)` and `w` has coordinates `(w_x, w_y)`, you form a matrix where `v`'s coordinates are the first column and `w`'s coordinates are the second column <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. The determinant of this matrix is the cross product <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

```
| v_x  w_x |
| v_y  w_y |
```
The determinant measures how areas change due to a [[introduction_to_linear_transformations | linear transformation]] <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. When basis vectors `i-hat` and `j-hat` are transformed to `v` and `w`, the unit square they define transforms into the parallelogram spanned by `v` and `w` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The determinant thus gives the area of this parallelogram <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. A negative determinant indicates that orientation was flipped, aligning with `v` being on the left of `w` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

**Example**: If `v = (-3, 1)` and `w = (2, 1)` <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>:
Determinant = `(-3 * 1) - (2 * 1) = -3 - 2 = -5` <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
This means the parallelogram's area is 5, and the negative sign indicates `v` is to the left of `w` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Intuitive Properties

*   When two vectors are perpendicular, their cross product is larger than if they were pointing in similar directions, as the parallelogram's area is maximized when sides are perpendicular <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   Scaling one of the vectors scales the parallelogram's area by the same factor <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. For example, `(3v) × w = 3 * (v × w)` <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

## 3D Cross Product

The "true" cross product combines two 3D vectors to produce a new 3D vector <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

### Geometric Interpretation

Similar to 2D, the parallelogram defined by the two vectors still plays a big role <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Magnitude**: The length of the resulting vector is the area of the parallelogram spanned by the two input vectors <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Direction**: The direction of the resulting vector is perpendicular to the plane containing the parallelogram <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>, <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### [[right_hand_rule_for_cross_products | Right Hand Rule]]

To determine the specific direction (which of the two perpendicular directions), the [[right_hand_rule_for_cross_products | right hand rule]] is used <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>:
1.  Point your right hand's forefinger in the direction of the first vector (`v`) <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
2.  Extend your middle finger in the direction of the second vector (`w`) <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
3.  Your thumb will then point in the direction of the cross product (`v × w`) <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

**Example**: If `v` is length 2 in the positive z-direction and `w` is length 2 in the positive y-direction <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>:
*   The parallelogram is a square with area 4 <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   Using the [[right_hand_rule_for_cross_products | right hand rule]], `v × w` points in the negative x-direction <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   Thus, `v × w = -4 * i-hat` <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### [[3d_cross_product_computations | 3D Cross Product Computations]]

For general computations, a formula can be memorized, but it's more common to use a process involving a 3D determinant <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
This involves writing a 3D matrix where:
*   The first column contains the basis vectors `i-hat`, `j-hat`, and `k-hat` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   The second and third columns contain the coordinates of `v` and `w` respectively <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

Then, you compute the determinant of this matrix, treating `i-hat`, `j-hat`, and `k-hat` as if they were numbers <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. The result will be a linear combination of these basis vectors, which defines the cross product vector <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

```
| i-hat  v_x  w_x |
| j-hat  v_y  w_y |
| k-hat  v_z  w_z |
```

Although this process might seem like a notational trick <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>, the determinant's continued importance is not coincidental <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. The reason for this connection lies in the concept of duality, which provides a deeper understanding of how this computation relates to the underlying geometry <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>, <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.