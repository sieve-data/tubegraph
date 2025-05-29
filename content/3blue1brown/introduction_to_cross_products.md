---
title: Introduction to cross products
videoId: eu6i7WJeinw
---

From: [[3blue1brown]] <br/> 

The cross product is an operation that combines two vectors to produce a third vector <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This article covers the standard introduction to the cross product, which is typically taught to students <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. A deeper understanding, involving linear transformations, will be explored in a separate video <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## 2D Cross Product

In two dimensions, given two vectors `v` and `w`, their cross product `v x w` is related to the area of the parallelogram they span <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This parallelogram is formed by taking copies of `v` and `w` and moving their tails to the tip of the other vector <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

The cross product `v x w` is the area of this parallelogram, with an important consideration for orientation <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>:
*   If `v` is on the right of `w`, `v x w` is positive and equal to the parallelogram's area <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   If `v` is on the left of `w`, `v x w` is negative, specifically the negative area of that parallelogram <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

This implies that order matters: swapping `v` and `w` (i.e., taking `w x v` instead of `v x w`) will result in the negative of the original cross product <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The order of basis vectors (e.g., `i-hat` cross `j-hat` being positive) defines orientation <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. For example, if `v` is on the left of `w` and the parallelogram's area is 7, then `v x w` is -7 <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Calculation using Determinants
To compute the 2D cross product `v x w`, you write the coordinates of `v` as the first column of a matrix and the coordinates of `w` as the second column, then compute the [[Determinants and 2D cross product | determinant]] of this matrix <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

The reason this works is connected to [[linear_transformations_and_dot_products | linear transformations]] <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. A matrix with columns representing `v` and `w` corresponds to a [[linear_transformations_and_dot_products | linear transformation]] that moves the basis vectors `i-hat` and `j-hat` to `v` and `w` <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. The [[Determinants and 2D cross product | determinant]] measures how areas change due to a transformation <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. The unit square, resting on `i-hat` and `j-hat` with an area of one, gets transformed into the parallelogram defined by `v` and `w` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Thus, the [[Determinants and 2D cross product | determinant]] directly gives the area of this parallelogram <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. If `v` is on the left of `w`, the orientation was flipped during the transformation, which is why the [[Determinants and 2D cross product | determinant]] is negative <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

For example, if `v = (-3, 1)` and `w = (2, 1)`, the [[Determinants and 2D cross product | determinant]] of the matrix with these as columns is `(-3 * 1) - (2 * 1) = -5` <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This means the parallelogram's area is 5, and the negative sign indicates `v` is to the left of `w` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Intuitive Properties
*   When two vectors are perpendicular, their cross product is larger than if they were pointing in similar directions, because the area of the parallelogram is maximized when the sides are closer to being perpendicular <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   Scaling one of the vectors, such as multiplying `v` by 3, scales the area of the parallelogram by the same factor. Therefore, `3v x w` will be exactly 3 times the value of `v x w` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## 3D Cross Product

The "true" cross product combines two 3D vectors to produce a new 3D vector <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Like the 2D case, it still considers the parallelogram defined by the two vectors being crossed, and the area of this parallelogram plays a significant role <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

For the 3D cross product:
*   **Length:** The length (magnitude) of the new vector is the area of the parallelogram spanned by the two input vectors <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Direction:** The direction of the new vector is perpendicular to the plane containing the parallelogram <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

To determine which of the two possible perpendicular directions is correct, the [[3D cross product and the right hand rule | right hand rule]] is used <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Point your right hand's forefinger in the direction of `v`, your middle finger in the direction of `w`, and your thumb will point in the direction of `v x w` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

For example, if `v` has a length of 2 pointing in the z-direction, and `w` has a length of 2 pointing in the y-direction, they define a square with an area of 4 <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Using the [[3D cross product and the right hand rule | right hand rule]], their cross product will be a vector of length 4 pointing in the negative x-direction, i.e., `-4 * i-hat` <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

### Calculation using 3D Determinants
For general computations, a process involving a 3D [[Determinants and 2D cross product | determinant]] is commonly used <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. This involves writing a 3D matrix where the second and third columns contain the coordinates of `v` and `w`, and the first column contains the basis vectors `i-hat`, `j-hat`, and `k-hat` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. When computing the [[Determinants and 2D cross product | determinant]] by treating the basis vectors as if they were numbers, the result is a linear combination of these basis vectors <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. This resulting vector is unique, perpendicular to `v` and `w`, has a magnitude equal to the parallelogram's area, and its direction obeys the [[3D cross product and the right hand rule | right hand rule]] <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

This method, while appearing as a "notational trick," is important because the [[Determinants and 2D cross product | determinant]] is once again central <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. A deeper understanding of this connection involves the idea of duality, which is covered in a subsequent video <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. The main takeaway is to understand what the [[Geometric representation of cross products | cross product]] vector geometrically represents <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.