---
title: Visualizing linear transformations with matrices
videoId: Ip3X9LOh2dk
---

From: [[3blue1brown]] <br/> 
The concept of a determinant is crucial for [[visualizing_linear_transformations | visualizing linear transformations]] and understanding how they are [[matrix_representation_of_linear_transformations | represented with matrices]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. It measures how much a [[linear_transformations | linear transformation]] stretches or squishes space <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. More precisely, it quantifies the factor by which the area of a given region increases or decreases <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

### Determinant in Two Dimensions

To understand the determinant, focus on how a 1x1 unit square (defined by the basis vectors i-hat and j-hat) transforms <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

*   **Scaling Example**: For a [[matrix_representation_of_transformations | matrix]] with columns (3, 0) and (0, 2), i-hat is scaled by 3 and j-hat by 2 <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. The unit square transforms into a 2x3 rectangle <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Since the area changed from 1 to 6, the determinant is 6 <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Shear Example**: A shear [[matrix_representation_of_transformations | matrix]] with columns (1, 0) and (1, 1) keeps i-hat in place and moves j-hat to (1, 1) <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The unit square becomes a parallelogram, but its area remains 1 <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. In this case, the determinant is 1 <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

The change in area of this single unit square reveals how the area of *any* region in space changes <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This is because all grid squares transform identically (due to grid lines remaining parallel and evenly spaced), and any shape can be approximated by grid squares <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. The "special scaling factor" by which a [[linear_transformations | linear transformation]] changes any area is called the **determinant** of that transformation <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

#### Values of the Determinant
*   A determinant of 3 means areas are increased by a factor of 3 <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   A determinant of ½ means areas are squished down by a factor of ½ <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   A determinant of **0** indicates that the transformation squishes all of space onto a line or even a single point, causing any region's area to become zero <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This means the [[linear_transformations | transformation]] maps everything into a smaller dimension <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Negative Determinants**: The determinant can be negative <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. A negative determinant signifies an **inversion of orientation** in space <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a> <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
    *   In 2D, if j-hat moves from being to the left of i-hat to the right of i-hat after transformation, orientation has been inverted <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   The *absolute value* of a negative determinant still gives the area scaling factor <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. For example, a determinant of -3 means space is flipped over and areas are scaled by 3 <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    *   This feels natural when considering a continuous series of transformations: as i-hat aligns with j-hat, the determinant approaches 0; if i-hat continues past j-hat, the determinant naturally becomes negative <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### Determinant in Three Dimensions

For [[threedimensional_linear_transformations | three-dimensional linear transformations]], the determinant tells you how much **volumes** get scaled <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

*   Focus on the 1x1x1 unit cube defined by i-hat, j-hat, and k-hat <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   After transformation, this cube warps into a shape called a **parallelepiped** <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   The determinant is simply the volume of this transformed parallelepiped <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   A determinant of **0** means all of space is squished onto something with zero volume, such as a flat plane, a line, or a single point <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This implies that the columns of the [[matrix_representation_of_3d_transformations | matrix]] are linearly dependent <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   **Negative Determinants in 3D**: Orientation is described by the **right-hand rule** <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. If, after the transformation, you can only align your fingers (forefinger i-hat, middle finger j-hat, thumb k-hat) using your *left* hand instead of your right, then orientation has been flipped, and the determinant is negative <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

### Computing the Determinant

For a 2x2 [[matrix_representation_of_transformations | matrix]] with entries `a, b, c, d`, the formula for the determinant is `ad - bc` <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   If `b` and `c` are both 0, then `a` scales i-hat in the x-direction and `d` scales j-hat in the y-direction, making `a * d` the area of the transformed rectangle <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   Even if only one of `b` or `c` is 0, the area of the parallelogram formed would still be `a * d` <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   When both `b` and `c` are non-zero, the `b * c` term accounts for the additional stretching or squishing in the diagonal direction <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

While computation of determinants (especially for 3D matrices) can be practiced, understanding what the determinant represents visually is more important than the calculation itself <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

### Determinants and Matrix Multiplication

A key property of determinants is that if you multiply two matrices together, the determinant of the resulting [[matrix_representation_of_transformations | matrix]] is the same as the product of the determinants of the original two matrices <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This makes intuitive sense because applying two [[linear_transformations | linear transformations]] sequentially means their individual scaling factors (determinants) multiply to give the total scaling factor.

The concept of determinants is fundamental and will be related to [[linear_transformations | linear systems of equations]] in future discussions <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.