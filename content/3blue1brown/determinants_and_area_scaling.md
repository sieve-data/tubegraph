---
title: Determinants and area scaling
videoId: Ip3X9LOh2dk
---

From: [[3blue1brown]] <br/> 

Linear transformations can stretch or squish space <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. A useful aspect of understanding these transformations is to measure precisely how much they stretch or squish things <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. More specifically, the goal is to measure the factor by which the area of a given region increases or decreases <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This special scaling factor is called the determinant of the transformation <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Determinants in 2D

The determinant quantifies how a linear transformation scales areas <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Unit Square Transformation
Consider a 1x1 square whose bottom sits on the i-hat basis vector and whose left side sits on the j-hat basis vector <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. After a transformation, this unit square will change shape and area <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

*   **Example 1: Scaling**
    For a matrix with columns `[3, 0]` and `[0, 2]`, i-hat is scaled by a factor of 3 and j-hat by a factor of 2 <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The initial 1x1 square transforms into a 2x3 rectangle <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Since the area started at 1 and ended at 6, the linear transformation scaled its area by a factor of 6 <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The determinant here is 6.

*   **Example 2: Shear**
    For a shear transformation with a matrix of columns `[1, 0]` and `[1, 1]`, i-hat stays in place, and j-hat moves to `[1, 1]` <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The unit square becomes a parallelogram, but its area remains 1, as its base and height each have length 1 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This transformation leaves areas unchanged, meaning its determinant is 1 <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### Generalization of Area Scaling
The way the area of the single unit square changes dictates how the area of *any* region in space changes <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This is because:
1.  What happens to one grid square applies to all other grid squares, regardless of size, due to grid lines remaining parallel and evenly spaced <a class="yt="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
2.  Any shape can be approximated by grid squares <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
Therefore, if the tiny grid squares' areas are scaled by a single amount, the entire blob's area will also be scaled by that same amount <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Determinant Values
*   A determinant of 3 means the transformation increases a region's area by a factor of 3 <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   A determinant of ½ means it squishes down all areas by a factor of ½ <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   A determinant of 0 means the transformation squishes all of space onto a line or even a single point, causing the area of any region to become zero <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Checking if a matrix's determinant is zero indicates if the transformation associated with that matrix squishes everything into a smaller dimension <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## [[Determinants and orientation flipping | Negative Determinants]] and Orientation

The full concept of the determinant allows for negative values, which relate to the idea of orientation <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   A transformation can flip space over, like turning a sheet of paper to its other side <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Such transformations are said to invert the orientation of space <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   In 2D, if j-hat (initially to the left of i-hat) ends up to the right of i-hat after a transformation, the orientation has been inverted <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   When the orientation of space is inverted, the determinant will be negative <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   The absolute value of the determinant still indicates the factor by which areas have been scaled <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   For example, a transformation with a determinant of -3 means space is flipped over, and areas are scaled by a factor of 3 <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   The progression from positive to negative determinants can be visualized: as i-hat approaches j-hat, areas squish, and the determinant approaches 0 <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. When they align, the determinant is 0 <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. If i-hat continues past j-hat, it feels natural for the determinant to continue decreasing into negative numbers <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Determinants in 3D

In three dimensions, the determinant tells how much a transformation scales volumes <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### Unit Cube Transformation
Similar to 2D, the determinant is easiest to understand by focusing on a specific 1x1x1 cube whose edges rest on the basis vectors i-hat, j-hat, and k-hat <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
*   After a transformation, this cube might warp into a shape called a "parallelipiped" <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   Since the cube starts with a volume of 1, the determinant is simply the volume of the parallelipiped that the cube transforms into <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   A determinant of 0 in 3D means that all of space is squished onto something with 0 volume, such as a flat plane, a line, or a single point <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. This implies that the columns of the matrix are linearly dependent <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Orientation in 3D
For 3D orientation, the right-hand rule applies <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>:
*   Point your right hand's forefinger in the direction of i-hat, middle finger in j-hat, and your thumb will point in the direction of k-hat <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   If you can still use your right hand to match the transformed basis vectors, the orientation has not changed, and the determinant is positive <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   If only your left hand can match the transformed basis vectors, orientation has been flipped, and the determinant is negative <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## [[Determinant computation for 2D and 3D transformations | Computing the Determinant]]

For a 2x2 matrix with entries `a, b, c, d`, the formula for the determinant is `ad - bc` <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   If `b` and `c` are both 0, `a` scales i-hat in the x-direction, and `d` scales j-hat in the y-direction <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. In this case, `a` multiplied by `d` (`ad`) gives the area of the resulting rectangle <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   If only one of `b` or `c` is 0, the transformed shape is a parallelogram with base `a` and height `d`, so the area is still `ad` <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   If both `b` and `c` are non-zero, the `bc` term accounts for how the parallelogram is stretched or squished diagonally <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

While computation can be practiced, understanding what the determinant represents is more important than the calculation itself <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

## [[Determinant properties and matrix multiplication | Determinants and Matrix Multiplication]]

A notable property is that if two matrices are multiplied together, the determinant of the resulting matrix is the same as the product of the determinants of the original two matrices <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. This makes intuitive sense because applying two transformations sequentially means their individual area scaling factors multiply to give the total area scaling.