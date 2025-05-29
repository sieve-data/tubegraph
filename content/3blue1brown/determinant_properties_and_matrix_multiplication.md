---
title: Determinant properties and matrix multiplication
videoId: Ip3X9LOh2dk
---

From: [[3blue1brown]] <br/> 

A **determinant** is a special scaling factor that measures how much a [[linear_transformations | linear transformation]] stretches or squishes space <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. More specifically, it measures the factor by which the area (in 2D) or volume (in 3D) of a given region increases or decreases <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Understanding what the determinant represents is more important than knowing its computation <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Determinants in Two Dimensions

In two dimensions, the determinant tells you how much a transformation scales areas <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. This can be understood by observing what happens to a 1x1 unit square defined by the standard basis vectors i-hat and j-hat <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

*   **Scaling Example**: A matrix with columns `[3, 0]` and `[0, 2]` scales i-hat by 3 and j-hat by 2 <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. The unit square transforms into a 2x3 rectangle <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Since its area changes from 1 to 6, the determinant is 6 <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Shear Example**: A shear transformation with matrix columns `[1, 0]` and `[1, 1]` keeps i-hat in place and moves j-hat to `[1, 1]` <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The unit square becomes a parallelogram, but its area remains 1 <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Thus, its determinant is 1 <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

The scaling factor applied to the unit square's area applies equally to any other region in space <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This is because grid lines remain parallel and evenly spaced, and any shape can be approximated by grid squares <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Determinant Values

*   **Positive Determinant**: Indicates that areas are scaled up or down, but the orientation of space is preserved <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. For example, a determinant of 3 means areas increase by a factor of 3 <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, and a determinant of ½ means areas are squished by a factor of ½ <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Zero Determinant**: Occurs if the transformation squishes all of space onto a line or a single point <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, meaning the area of any region becomes zero <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This is a crucial concept, as a zero determinant indicates that the transformation reduces the dimension of the space <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Negative Determinant**: Indicates that the orientation of space has been inverted <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This can be visualized as j-hat moving from being to the left of i-hat to being to its right <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. The absolute value of the determinant still gives the area scaling factor <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. For instance, a determinant of -3 means space is flipped over and areas are scaled by a factor of 3 <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. This negative value feels natural as the determinant passes through zero when orientation flips <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Calculating a 2x2 Determinant

For a 2x2 matrix with entries:
```
[ a b ]
[ c d ]
```
The formula for its determinant is `ad - bc` <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. The `ad` term represents the area of the rectangle formed if `b` and `c` were zero <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. The `bc` term accounts for the stretching or squishing in diagonal directions <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
For more on calculating determinants, see [[determinant_computation_for_2d_and_3d_transformations | Determinant Computation for 2D and 3D Transformations]].

## Determinants in Three Dimensions

In three dimensions, the determinant represents how much a transformation scales volumes <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This is typically observed by focusing on a 1x1x1 unit cube aligned with the basis vectors i-hat, j-hat, and k-hat <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. After transformation, this cube may warp into a "parallelepiped" <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. The determinant is simply the volume of this transformed parallelepiped <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### Determinant Values in 3D

*   **Zero Determinant**: Means all of space is squished onto something with zero volume, such as a flat plane, a line, or a single point <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This implies that the columns of the matrix are [[linear_dependence | linearly dependent]] <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   **Negative Determinant**: Signifies that the orientation of space has been flipped <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. This can be understood using the right-hand rule: if, after transformation, the orientation of i-hat, j-hat, and k-hat only aligns with the left hand, then the determinant is negative <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

## Determinants and Matrix Multiplication

A key property of determinants is how they behave under matrix multiplication:
The determinant of the product of two matrices is equal to the product of their individual determinants <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
That is, for matrices A and B: `det(AB) = det(A) * det(B)` <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

> [!NOTE] Thinking Question
> If `det(A)` represents the scaling factor of transformation A, and `det(B)` represents the scaling factor of transformation B, why would `det(AB)` (which represents the combined transformation) be the product of their individual scaling factors? Consider what happens to areas/volumes when two transformations are applied sequentially.