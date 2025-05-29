---
title: Understanding determinants in linear algebra
videoId: Ip3X9LOh2dk
---

From: [[3blue1brown]] <br/> 

The determinant of a [[Matrix representation of linear transformations | linear transformation]] is a crucial value that quantifies how much the transformation stretches or squishes space <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Specifically, it measures the factor by which the area of a given region (in 2D) or volume (in 3D) increases or decreases <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Geometric Intuition of Determinants

The determinant is defined by observing what happens to a specific unit region in space:
*   In 2D, this is the 1x1 square whose bottom edge sits on the i-hat basis vector and whose left side sits on the j-hat basis vector <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   In 3D, this is the 1x1x1 cube whose edges rest on the basis vectors i-hat, j-hat, and k-hat <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

The area or volume of this unit region after the transformation directly corresponds to the absolute value of the determinant <a class="yt-timestamp" data-t="01:01:08">[01:01:08]</a>, <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. Whatever happens to this single unit square or cube applies to any other region in space, as grid lines remain parallel and evenly spaced, scaling all areas/volumes by the same factor <a class="yt-timestamp" data-t="01:01:46">[01:01:46]</a>.

### 2D Determinants: Area Scaling

For a 2D transformation, the determinant is the factor by which areas are scaled <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.
*   **Scaling Example**: A matrix with columns (3, 0) and (0, 2) scales i-hat by 3 and j-hat by 2 <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The unit square transforms into a 2x3 rectangle <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Since its initial area was 1 and final area is 6, the determinant is 6 <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **Shear Example**: A shear transformation with matrix columns (1, 0) and (1, 1) keeps i-hat in place and moves j-hat to (1, 1) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The unit square turns into a parallelogram, but its area remains 1 <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Thus, its determinant is 1 <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

#### Determinant of Zero in 2D

A determinant of 0 indicates that the transformation squishes all of space onto a line or even a single point <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. In this case, the area of any region becomes zero <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. This concept is particularly important as it relates to [[applications_of_determinants_to_linear_systems_of_equations | linear systems of equations]] <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.

#### Negative Determinants in 2D: Orientation

While the absolute value of the determinant represents scaling, a negative determinant signifies that the transformation has inverted the orientation of space <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This can be visualized as "flipping space over" like a sheet of paper <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

One way to observe orientation in 2D is by looking at the relative positions of i-hat and j-hat <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. If j-hat starts to the left of i-hat, and after transformation, it ends up to the right of i-hat, the orientation has been inverted <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This happens as the determinant crosses zero when the basis [[understanding_vectors_in_linear_algebra | vectors]] become collinear <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### 3D Determinants: Volume Scaling

In three dimensions, the determinant tells you how much volumes are scaled <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. The unit cube defined by i-hat, j-hat, and k-hat transforms into a shape called a "parallelipiped" <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. The volume of this parallelipiped is the determinant <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

#### Determinant of Zero in 3D

A determinant of 0 in 3D means that all of space is squished onto something with zero volume, such as a flat plane, a line, or a single point <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. This implies that the columns of the matrix are [[linear_algebra_foundations | linearly dependent]] <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

#### Negative Determinants in 3D: Orientation

Orientation in 3D can be described using the right-hand rule <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>:
1.  Point your forefinger in the direction of i-hat.
2.  Stick out your middle finger in the direction of j-hat.
3.  Your thumb should point in the direction of k-hat <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

If you can still align your fingers this way after the transformation, the determinant is positive <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. If you can only do this with your left hand, the orientation has been flipped, and the determinant is negative <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## Computing Determinants

While understanding what the determinant represents is more important, formulas exist for [[computing_determinants_for_2d_and_3d_transformations | computing determinants]] <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>, <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.

### 2x2 Matrix Determinant

For a 2x2 matrix with entries:
```
[ a  b ]
[ c  d ]
```
The determinant is calculated as `ad - bc` <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

The `ad` term intuitively relates to the area scaling when off-diagonal terms are zero, as it represents the stretching along the x and y axes <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. The `bc` term accounts for the diagonal stretching or squishing that occurs when `b` and `c` are non-zero <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

### 3x3 Matrix Determinant

There is also a formula for 3x3 matrices, but the focus remains on the conceptual understanding rather than rote computation <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

## Further Considerations

An interesting property of determinants is that if you multiply two matrices together, the determinant of the resulting matrix is the product of the determinants of the original two matrices <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. This makes intuitive sense because if one transformation scales space by a factor of `det(A)` and another by `det(B)`, applying both transformations sequentially would scale space by `det(A) * det(B)`.

The concept of determinants is fundamental to understanding [[applications_of_determinants_to_linear_systems_of_equations | linear systems of equations]] and other areas of [[linear_algebra_foundations | linear algebra]] <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.