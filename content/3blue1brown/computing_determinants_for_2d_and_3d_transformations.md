---
title: Computing determinants for 2D and 3D transformations
videoId: Ip3X9LOh2dk
---

From: [[3blue1brown]] <br/> 

Determinants are a crucial concept in [[linear_transformations_and_matrices | linear transformations and matrices]] that measure how much a transformation stretches or squishes space <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. More precisely, it quantifies the factor by which the area (in 2D) or volume (in 3D) of a given region increases or decreases <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Determinants in Two Dimensions

The determinant of a [[two_dimensional_grid_transformations | two-dimensional grid transformation]] indicates how much it scales the area of any region <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

### Visualizing Area Scaling

Consider a unit square (1x1 area) formed by the basis vectors i-hat and j-hat <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Scaling Example**: A matrix with columns (3, 0) and (0, 2) scales i-hat by 3 and j-hat by 2 <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. The unit square transforms into a 2x3 rectangle <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Since the area goes from 1 to 6, the determinant is 6 <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Shear Example**: A shear transformation with columns (1, 0) and (1, 1) keeps i-hat in place and moves j-hat to (1, 1) <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The unit square becomes a parallelogram, but its area remains 1 (base 1, height 1) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. Thus, the determinant is 1 <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

The scaling factor of the unit square's area applies to *any* region in space <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. This is because grid lines remain parallel and evenly spaced, meaning all squares in the grid are affected uniformly <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Any shape can be approximated by grid squares, so if tiny squares scale by a certain amount, the whole shape scales by that same amount <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This special scaling factor is the determinant <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

### Values of the Determinant

*   **Positive Determinant**: Means areas are scaled up (e.g., determinant 3 scales area by a factor of 3) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Fractional Determinant**: Means areas are squished down (e.g., determinant ½ squishes areas by a factor of ½) <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Zero Determinant**: Means the [[linear_transformations_and_matrices | transformation]] squishes all of space onto a line or a single point, resulting in zero area for any region <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This implies the columns of the matrix are linearly dependent <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   **Negative Determinant**: Means space is "flipped over" or its orientation is inverted <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This can be observed if, after the transformation, j-hat ends up to the right of i-hat (whereas initially it was to the left) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. The absolute value of the determinant still gives the area scaling factor <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### Computing the 2x2 Determinant

For a 2x2 matrix with entries:
$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$
The determinant is calculated as `ad - bc` <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

**Intuition for the 2x2 Formula:**
*   If `b` and `c` are both 0, `a` stretches i-hat in the x-direction and `d` stretches j-hat in the y-direction <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. The area of the transformed unit square is `a * d` <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   Even if only one of `b` or `c` is 0, the transformed shape is a parallelogram with base `a` and height `d`, so the area is still `a * d` <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   The `b * c` term roughly accounts for how much the parallelogram is stretched or squished diagonally when both `b` and `c` are non-zero <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

## Determinants in Three Dimensions

In three dimensions, the determinant tells you how much a transformation scales volumes <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### Visualizing Volume Scaling

Instead of a unit square, focus on the 1x1x1 unit cube defined by the basis vectors i-hat, j-hat, and k-hat <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. After a [[threedimensional_linear_transformations | transformation]], this cube might warp into a "parallelepiped" <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. Since the initial volume is 1, the determinant is simply the volume of this transformed parallelepiped <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### Values of the 3D Determinant

*   **Zero Determinant**: Means all of space is squished onto something with zero volume, like a flat plane, a line, or a single point <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This again signifies that the columns of the matrix are linearly dependent <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   **Negative Determinant**: Implies that the orientation of space has been flipped <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. This can be understood using the right-hand rule: if the transformed basis vectors (i-hat, j-hat, k-hat) can only align with your left hand's thumb, forefinger, and middle finger (instead of the right hand), the determinant is negative <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

### Computing the 3D Determinant

While there is a formula for 3D determinants, understanding its representation is more important than the computation itself <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. For those who need to compute it, practice is key <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

## Properties of Determinants

If you multiply two matrices together, the determinant of the resulting matrix is the product of the determinants of the original two matrices <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This makes sense because performing two transformations in sequence means their individual area/volume scaling factors multiply to give the total scaling factor.