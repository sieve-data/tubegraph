---
title: 3D cross product and the right hand rule
videoId: eu6i7WJeinw
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_cross_products|cross product]] is a mathematical operation that combines two vectors. While it has a standard introduction, a deeper understanding can be gained by relating it to linear transformations <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Two-Dimensional Cross Product (A Precursor)

In two dimensions, given two vectors `v` and `w`, their [[cross_product_and_parallelogram_area|cross product]] is defined by the area of the parallelogram they span <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
To form this parallelogram, one can take a copy of `v` and move its tail to the tip of `w`, and similarly, a copy of `w` to the tip of `v` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Orientation

The [[cross_product_and_parallelogram_area|cross product]] also considers orientation <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>:
*   If `v` is on the right of `w`, `v` cross `w` is positive and equals the parallelogram's area <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   If `v` is on the left of `w`, the cross product is negative (the negative area) <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
This implies that the order of vectors matters: `w` cross `v` is the negative of `v` cross `w` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The order of basis vectors (i-hat cross j-hat being positive) defines orientation <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. For example, if `v` is on the left of `w` and the parallelogram area is 7, `v` cross `w` is -7 <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Computation using Determinants

The 2D [[determinants_and_2d_cross_product|cross product]] `v` cross `w` can be computed by writing the coordinates of `v` as the first column and `w` as the second column of a matrix, then computing its [[computing_determinants_for_2d_and_3d_transformations|determinant]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

This works because a matrix with `v` and `w` as columns represents a linear transformation that moves the basis vectors i-hat and j-hat to `v` and `w` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The [[computing_determinants_for_2d_and_3d_transformations|determinant]] measures how areas change under a transformation, specifically transforming the unit square (area one) spanned by i-hat and j-hat into the parallelogram spanned by `v` and `w` <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. A negative [[computing_determinants_for_2d_and_3d_transformations|determinant]] indicates an orientation flip <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

For instance, if `v` = (-3, 1) and `w` = (2, 1), the [[computing_determinants_for_2d_and_3d_transformations|determinant]] is (-3 * 1) - (2 * 1) = -5 <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This means the parallelogram area is 5, and the negative sign reflects `v` being to the left of `w` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Intuitive Properties
*   When vectors are perpendicular, their [[cross_product_and_parallelogram_area|cross product]] is larger, as the parallelogram area is maximized <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   Scaling one vector by a factor scales the parallelogram area by the same factor. So, `3v` cross `w` is 3 times `v` cross `w` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## The True 3D Cross Product

The "true" [[introduction_to_cross_products|cross product]] combines two 3D vectors to produce a new 3D vector <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Magnitude**: The length of this new vector is the area of the parallelogram defined by the two original vectors <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Direction**: The direction of the new vector is perpendicular to the plane of the parallelogram <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### The Right Hand Rule

To determine which of the two possible perpendicular directions is correct, the [[geometric_representation_of_cross_products|right hand rule]] is used <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>:
1.  Point the forefinger of your right hand in the direction of the first vector (`v`).
2.  Stick out your middle finger in the direction of the second vector (`w`).
3.  Your thumb will then point in the direction of the [[geometric_representation_of_cross_products|cross product]] (`v` cross `w`) <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

For example, if `v` is a vector of length 2 pointing in the z-direction (straight up) and `w` is a vector of length 2 pointing in the y-direction, they form a square of area 4 <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Using the [[geometric_representation_of_cross_products|right hand rule]], their [[introduction_to_cross_products|cross product]] points in the negative x-direction. Thus, the cross product is -4 times i-hat <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Computation using 3D Determinants

For general computations, a common method involves a "notational trick" with the 3D [[computing_determinants_for_2d_and_3d_transformations|determinant]] <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>:
1.  Create a 3D matrix.
2.  The second and third columns contain the coordinates of `v` and `w` respectively <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
3.  The first column contains the basis vectors i-hat, j-hat, and k-hat <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
4.  Compute the [[computing_determinants_for_2d_and_3d_transformations|determinant]] of this matrix, treating the basis vectors as if they were numbers <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

This computation yields a linear combination of the basis vectors <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. The resulting vector is unique: it is perpendicular to `v` and `w`, its magnitude is the area of the appropriate parallelogram, and its direction obeys the [[geometric_representation_of_cross_products|right hand rule]] <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. While it appears to be a notational trick, there is a deeper reason involving duality for why the [[computing_determinants_for_2d_and_3d_transformations|determinant]] is once again important <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. However, understanding the [[geometric_representation_of_cross_products|geometric representation of cross products]] is the crucial aspect <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.