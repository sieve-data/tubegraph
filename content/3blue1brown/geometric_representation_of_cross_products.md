---
title: Geometric representation of cross products
videoId: eu6i7WJeinw
---

From: [[3blue1brown]] <br/> 

The cross product is an operation that has both a standard introduction and a deeper understanding related to linear transformations <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This article covers the typical geometric interpretations of the cross product in two and three dimensions <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.

## Two-Dimensional Cross Product

In two dimensions, given two vectors `v` and `w`, their cross product, written as `v × w`, is directly related to the area of the parallelogram they span <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. This parallelogram is formed by taking copies of `v` and `w` and moving their tails to the tips of the other vector <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.

### Area and Orientation

The value of the 2D cross product is the area of this parallelogram, with an added consideration for orientation <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.
*   If `v` is to the right of `w`, `v × w` is positive and equal to the parallelogram's area <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
*   If `v` is to the left of `w`, `v × w` is negative, specifically the negative area of the parallelogram <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

This implies that the order of the vectors matters; `w × v` will be the negative of `v × w` <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. The orientation is defined by the order of basis vectors, such as `i-hat × j-hat` resulting in a positive value <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. For example, if `v` is to the left of `w` and their parallelogram has an area of 7, then `v × w` is -7 <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

### Computation using Determinants

The 2D cross product can be computed using the [[determinants_and_2d_cross_product | determinant]] <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. To find `v × w`, you create a matrix where the coordinates of `v` form the first column and the coordinates of `w` form the second column, then compute its determinant <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

This method works because the determinant measures how areas change due to a linear transformation <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. A matrix with `v` and `w` as columns represents a transformation that maps the unit square (defined by `i-hat` and `j-hat`) to the parallelogram spanned by `v` and `w` <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. Since the unit square has an area of 1, the determinant gives the area of the transformed parallelogram <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. A negative determinant indicates that the orientation was flipped during the transformation, which aligns with `v` being on the left of `w` <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

For instance, if `v = (-3, 1)` and `w = (2, 1)`, the determinant of the matrix `[[-3, 2], [1, 1]]` is `(-3 * 1) - (2 * 1) = -5` <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. This means the parallelogram has an area of 5, and the negative sign indicates `v` is to the left of `w` <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

### Intuitive Properties
*   The cross product is larger when the vectors are closer to being perpendicular, as this creates a larger parallelogram area <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.
*   Scaling one of the vectors scales the parallelogram's area by the same factor. For example, `(3v) × w` will be three times the value of `v × w` <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>.

## Three-Dimensional Cross Product

The "true" cross product combines two 3D vectors to produce a new 3D vector <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>. While the parallelogram spanned by the two vectors still plays a central role, the result is not a scalar area, but a vector <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

### Magnitude and Direction
*   **Magnitude**: The length of the resulting 3D cross product vector is the area of the parallelogram formed by the two input vectors <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
*   **Direction**: The direction of this new vector is perpendicular to the plane containing the parallelogram <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.

### [[3d_cross_product_and_the_right_hand_rule | Right Hand Rule]]
To determine the specific direction of the cross product vector, the [[3d_cross_product_and_the_right_hand_rule | right hand rule]] is used <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>:
1.  Point the forefinger of your right hand in the direction of the first vector (`v`).
2.  Stick out your middle finger in the direction of the second vector (`w`).
3.  Your thumb will then point in the direction of `v × w` <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

For example, if `v` points up in the z-direction (length 2) and `w` points in the y-direction (length 2), they form a square with an area of 4 <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>. Using the [[3d_cross_product_and_the_right_hand_rule | right hand rule]], their cross product will point in the negative x-direction, resulting in a vector of `negative 4 * i-hat` <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>.

### Computation using 3D Determinant
A common method for computing the 3D cross product involves a specific process using a 3D determinant <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>. This involves setting up a 3D matrix where:
*   The first column contains the basis vectors `i-hat`, `j-hat`, and `k-hat`.
*   The second column contains the coordinates of `v`.
*   The third column contains the coordinates of `w` <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>.

When the determinant of this matrix is computed by treating `i-hat`, `j-hat`, and `k-hat` as if they were numbers, the result is a linear combination of these basis vectors, which forms the cross product vector <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>. Students are often taught to accept this as a "notational trick," but it's crucial to understand that the resulting vector is indeed the unique vector that is perpendicular to `v` and `w`, has a magnitude equal to the parallelogram's area, and its direction adheres to the [[3d_cross_product_and_the_right_hand_rule | right hand rule]] <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>.

A deeper understanding of why the determinant is relevant here and the significance of placing basis vectors in the matrix involves the concept of duality, which is explored in a separate discussion <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>. The fundamental takeaway for [[geometric_representation_of_cross_products | geometric representation]] is the meaning of the cross product vector itself <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>.