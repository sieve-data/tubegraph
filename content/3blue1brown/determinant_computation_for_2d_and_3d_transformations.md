---
title: Determinant computation for 2D and 3D transformations
videoId: Ip3X9LOh2dk
---

From: [[3blue1brown]] <br/> 

The determinant of a [[linear_transformations_in_linear_algebra | linear transformation]] is a special scaling factor that measures how much the transformation stretches or squishes space <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. More specifically, it quantifies the factor by which the area of a given region (in 2D) or the volume (in 3D) increases or decreases <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Determinants in Two Dimensions

In two dimensions, the determinant measures how much a [[linear_transformations_in_linear_algebra | linear transformation]] changes any area <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This scaling factor can be understood by observing what happens to a 1x1 unit square <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Visualizing Area Scaling
Consider a matrix with columns `[3, 0]` and `[0, 2]` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This transformation scales the basis vector i-hat by a factor of 3 and j-hat by a factor of 2 <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. A 1x1 unit square, whose bottom sits on i-hat and left side on j-hat, transforms into a 2x3 rectangle <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Since the initial area was 1 and the final area is 6, the area has been scaled by a factor of 6 <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The determinant of this transformation is 6.

In contrast, a shear transformation with matrix columns `[1, 0]` and `[1, 1]` leaves i-hat in place and moves j-hat to `[1, 1]` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The unit square gets slanted into a parallelogram, but its area remains 1, as its base and height continue to be 1 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This means the determinant for this shear transformation is 1, indicating areas remain unchanged <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

The scaling factor derived from the unit square applies to any region in space <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This is because all grid squares scale by the same amount due to parallel and evenly spaced grid lines, and any shape can be approximated by grid squares <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Determinant of Zero
A determinant of 0 for a 2D transformation signifies that the transformation squishes all of space onto a line or even a single point <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. In such cases, the area of any region becomes zero <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Checking if a matrix's determinant is zero provides a way to determine if its associated transformation reduces dimensionality <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Negative Determinants and Orientation
The full concept of the determinant allows for negative values, which signifies an inversion of space's orientation <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This can be visualized as "flipping space over" like turning a sheet of paper <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Another way to perceive this is by observing i-hat and j-hat: if j-hat moves from being to the left of i-hat to the right of i-hat after transformation, orientation has been inverted <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

When orientation is inverted, the determinant is negative <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. The absolute value of the determinant still provides the factor by which areas have been scaled <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. For example, a matrix with columns `[1, 1]` and `[2, -1]` has a determinant of -3, meaning space is flipped over and areas are scaled by a factor of 3 <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. The progression of i-hat approaching j-hat, causing the determinant to approach zero and then become negative as i-hat "crosses over," makes negative values feel natural <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Computing the 2D Determinant
For a 2x2 matrix with entries `[a, b; c, d]`, the formula for the determinant is `ad - bc` <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   If `b` and `c` are both 0, `a` indicates i-hat's stretch in the x-direction, and `d` indicates j-hat's stretch in the y-direction. In this case, `ad` represents the area of the transformed rectangle, similar to the `[3, 0; 0, 2]` example <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   If only one of `b` or `c` is 0, the transformed shape is a parallelogram with base `a` and height `d`, so the area is still `ad` <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   The `bc` term accounts for how much the parallelogram is stretched or squished in the diagonal direction when both `b` and `c` are non-zero <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

While computation by hand requires practice, understanding what the determinant represents is more crucial <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

## Determinants in Three Dimensions

In three dimensions, the determinant tells you how much a [[linear_transformations_in_linear_algebra | linear transformation]] scales volumes <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This is understood by observing the transformation of a 1x1x1 unit cube, whose edges rest on the basis vectors i-hat, j-hat, and k-hat <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. After transformation, this cube becomes a "parallelepiped" <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. Since the initial volume is 1, the determinant is simply the volume of this resulting parallelepiped <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

### Determinant of Zero in 3D
A determinant of 0 in 3D implies that all of space is squished onto something with zero volume, such as a flat plane, a line, or a single point <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. This condition also indicates that the columns of the matrix are [[linear_transformations_in_linear_algebra | linearly dependent]] <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Negative Determinants in 3D
For three dimensions, orientation is described using the right-hand rule <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. If, after the transformation, the right-hand rule (forefinger for i-hat, middle finger for j-hat, thumb for k-hat) can still be applied, the orientation has not changed, and the determinant is positive <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. If only the left hand can be used to align with the transformed basis vectors, the orientation has been flipped, and the determinant is negative <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

### Computing the 3D Determinant
There is a formula for computing 3D determinants, but the emphasis remains on understanding its conceptual meaning over manual computation <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

## Properties of Determinants
A notable property of determinants is that if two matrices are multiplied together, the determinant of the resulting matrix is equal to the product of the determinants of the original two matrices <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. This is a key [[determinant_properties_and_matrix_multiplication | determinant property related to matrix multiplication]].

Determinants are fundamental to understanding [[linear_transformations_in_linear_algebra | linear transformations]] and will be related to [[linear_transformations_in_linear_algebra | linear systems of equations]] in future discussions <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.