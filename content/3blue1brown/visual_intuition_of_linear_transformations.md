---
title: Visual intuition of linear transformations
videoId: Ip3X9LOh2dk
---

From: [[3blue1brown]] <br/> 
This article assumes a prior [[visual_understanding_of_linear_transformations | visual understanding of linear transformations]] and their [[matrix_representation of linear transformations | matrix representation]], as discussed in previous content <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Measuring Space Transformation

[[Linear transformations in linear algebra | Linear transformations]] can either stretch space out or squish it in <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. A key aspect of [[visual_understanding_of_linear_transformations | understanding these transformations]] is to measure precisely how much they stretch or squish <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. More specifically, it's useful to measure the factor by which the area of a given region increases or decreases <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

Consider the following examples:

*   **Scaling Transformation**: For a matrix with columns `(3, 0)` and `(0, 2)` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, it scales the basis vector `i-hat` by a factor of 3 and `j-hat` by a factor of 2 <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. If we focus on the 1x1 unit square defined by `i-hat` and `j-hat`, this transformation turns it into a 2x3 rectangle <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Since the area started at 1 and ended at 6, the linear transformation scaled its area by a factor of 6 <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **Shear Transformation**: A shear matrix with columns `(1, 0)` and `(1, 1)` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a> means `i-hat` stays in place and `j-hat` moves to `(1, 1)` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The unit square gets slanted into a parallelogram, but its area remains 1, as its base and height each have a length of 1 <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This transformation leaves areas unchanged for the unit square <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

The change in the area of the unit square is significant because if you know how much the area of this one unit square changes, it reveals how the area of *any* possible region in space changes <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This is because all grid squares scale identically, as grid lines remain parallel and evenly spaced <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Any shape, even a non-grid square, can be approximated by grid squares <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, meaning the area of any region scales by the same amount <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## The Determinant

This special scaling factor, which dictates how much a [[linear_transformations_in_linear_algebra | linear transformation]] changes any area, is called the **determinant** of that transformation <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. Understanding what the determinant represents is much more important than simply knowing how to compute it <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

*   A determinant of 3 means the transformation increases area by a factor of 3 <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   A determinant of ½ means areas are squished down by a factor of ½ <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   A determinant of 0 for a 2D transformation signifies that all of space is squished onto a line or even a single point, causing any region's area to become zero <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This implies that checking if a matrix's determinant is zero indicates whether its associated transformation squishes everything into a smaller dimension <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Negative Determinants and Orientation

The concept of the determinant also allows for negative values, which relate to the idea of **orientation** <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Some transformations can give the sensation of "flipping space over," inverting its orientation <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

One way to visualize this is by observing `i-hat` and `j-hat` <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Initially, `j-hat` is typically to the left of `i-hat` <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. If, after a transformation, `j-hat` is now to the right of `i-hat`, the orientation of space has been inverted <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. Whenever orientation is inverted, the determinant will be negative <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The absolute value of the determinant still provides the factor by which areas have been scaled <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

For example, a matrix with columns `(1, 1)` and `(2, -1)` has a determinant of -3 <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. This means space is flipped over, and areas are scaled by a factor of 3 <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. The negative sign naturally arises as `i-hat` slowly crosses the line defined by `j-hat`, causing the determinant to pass through zero and become negative <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

## Determinants in Three Dimensions

For [[threedimensional_linear_transformations | three dimensions]], the determinant still indicates how much a transformation scales things, but this time, it refers to how much **volumes** are scaled <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

To visualize this, focus on the 1x1x1 unit cube whose edges align with the basis vectors `i-hat`, `j-hat`, and `k-hat` <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. After the transformation, this cube might warp into a "parallelipiped" (a slanted cube) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. Since the cube starts with a volume of 1, the determinant is simply the volume of this resulting parallelipiped <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

A determinant of 0 in 3D means all of space is squished onto something with zero volume, like a flat plane, a line, or a single point <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. This condition also indicates that the columns of the matrix are linearly dependent <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### 3D Orientation

For negative determinants in 3D, orientation can be described using the **right-hand rule** <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>:
1.  Point your forefinger in the direction of `i-hat` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
2.  Stick out your middle finger in the direction of `j-hat` <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
3.  Your thumb will point in the direction of `k-hat` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

If you can still perform this with your *right* hand after the transformation, the orientation has not changed, and the determinant is positive <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. If it only makes sense to do this with your *left* hand, orientation has been flipped, and the determinant is negative <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## Computing the Determinant

For a 2x2 matrix with entries:
`a b`
`c d`

The formula for its determinant is `(a * d) - (b * c)` <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

This formula can be intuitively understood:
*   If `b` and `c` are both 0, `a` scales `i-hat` in the x-direction and `d` scales `j-hat` in the y-direction <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. In this case, `(a * d)` gives the area of the resulting rectangle, similar to the `(3,0; 0,2)` example <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   Even if only one of `b` or `c` is 0, you would still have a parallelogram with base `a` and height `d`, so the area would still be `(a * d)` <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   When both `b` and `c` are non-zero, the `(b * c)` term accounts for how much the parallelogram is stretched or squished in the diagonal direction <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

While computing determinants by hand requires practice <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>, the [[importance_of_visual_intuition_for_learning_linear_algebra | visual understanding of what the determinant represents]] is central to the essence of linear algebra <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### Determinants and [[composition_of_linear_transformations | Matrix Multiplication]]

A useful property to consider is that when two matrices are multiplied, the determinant of the resulting matrix is the same as the product of the determinants of the original two matrices <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. This makes intuitive sense because applying one transformation then another means their individual area/volume scaling factors simply multiply together.