---
title: Cross product and parallelogram area
videoId: eu6i7WJeinw
---

From: [[3blue1brown]] <br/> 
The cross product is a mathematical operation that can be understood through its geometric interpretation, particularly concerning the area of a parallelogram spanned by two vectors.

## [[Introduction to cross products | Introduction to Cross Products]]

The concept of the cross product, like the dot product, can be approached with a standard [[introduction_to_cross_products | introduction]] and a deeper understanding related to [[linear_transformations | linear transformations]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This article focuses on the main points typically taught about the cross product <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Two-Dimensional Cross Product

We begin by considering the cross product in two dimensions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Geometric Interpretation

Given two vectors, `v` and `w`, the [[geometric_representation_of_cross_products | cross product]] `v × w` (written with an x-shaped multiplication symbol) is the area of the parallelogram they span <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This parallelogram is formed by taking a copy of `v` to the tip of `w` and a copy of `w` to the tip of `v` <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

This definition also incorporates **orientation**:
*   If `v` is to the right of `w`, `v × w` is positive and equals the parallelogram's area <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   If `v` is to the left of `w`, `v × w` is negative, representing the negative area of the parallelogram <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

This orientation means that **order matters**: swapping `v` and `w` to compute `w × v` will result in the negative of `v × w` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The order of basis vectors (i-hat cross j-hat being positive) defines this orientation <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

For example, if the parallelogram formed by `v` and `w` has an area of 7, and `v` is to the left of `w`, then `v × w` is -7 <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Computing with [[Determinants and 2D cross product | Determinants]]

To compute the 2D cross product without knowing the area, one uses the determinant <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
If `v` has coordinates `(v_x, v_y)` and `w` has `(w_x, w_y)`, the 2D cross product `v × w` is computed by forming a matrix where `v`'s coordinates are the first column and `w`'s coordinates are the second column, then calculating its determinant <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>:

$$ \text{det} \begin{pmatrix} v_x & w_x \\ v_y & w_y \end{pmatrix} = v_x w_y - w_x v_y $$

The determinant measures how areas change due to a linear transformation <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. When a matrix's columns are `v` and `w`, it represents a transformation that moves the unit square (defined by basis vectors i-hat and j-hat, which have area 1) into the parallelogram spanned by `v` and `w` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Thus, the determinant gives the area of this parallelogram <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. If `v` is to the left of `w`, the orientation is flipped, resulting in a negative determinant <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

**Example**:
If `v = (-3, 1)` and `w = (2, 1)` <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>:

$$ \text{det} \begin{pmatrix} -3 & 2 \\ 1 & 1 \end{pmatrix} = (-3)(1) - (2)(1) = -3 - 2 = -5 $$

The area of the parallelogram is 5, and since `v` is to the left of `w`, the cross product is -5 <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Properties of the 2D Cross Product

*   **Perpendicularity**: When two vectors are perpendicular (or close to it), their cross product is larger because the parallelogram's area is maximized when its sides are close to being perpendicular <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **Scalar Multiplication**: Scaling one of the vectors (e.g., multiplying `v` by 3) scales the area of the parallelogram by the same factor. So, `(3v) × w` will be 3 times the value of `v × w` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Three-Dimensional Cross Product

While the 2D interpretation is valid, the "true" cross product combines two 3D vectors to produce a new 3D vector <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### Geometric Interpretation

Similar to 2D, the [[geometric_representation_of_cross_products | parallelogram]] defined by the two vectors still plays a crucial role <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   The **length** (magnitude) of the resulting 3D vector is the area of this parallelogram <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   The **direction** of this new vector is perpendicular to the parallelogram <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### [[3D cross product and the right hand rule | The Right-Hand Rule]]

To determine the specific direction (which of the two perpendicular directions), the [[3d_cross_product_and_the_right_hand_rule | right-hand rule]] is used <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>:
1.  Point the forefinger of your right hand in the direction of the first vector (`v`).
2.  Stick out your middle finger in the direction of the second vector (`w`).
3.  Your thumb will then point in the direction of `v × w` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

**Example**:
If `v` is a vector of length 2 pointing in the `z` direction, and `w` is a vector of length 2 pointing in the `y` direction <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>:
*   They form a square (a parallelogram) with an area of 4 <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   Using the right-hand rule, `v × w` will point in the negative `x` direction <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   Therefore, `v × w` is a vector with length 4 pointing in the negative `x` direction, i.e., -4 times the i-hat basis vector <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### Computing with the 3D Determinant

For general 3D vectors, a formula involving the 3D determinant is commonly used <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
One creates a 3D matrix where:
*   The second column contains the coordinates of `v`.
*   The third column contains the coordinates of `w`.
*   The first column contains the basis vectors `i-hat`, `j-hat`, and `k-hat` <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

Calculating the determinant of this matrix as if `i-hat`, `j-hat`, and `k-hat` were numbers results in a linear combination of these basis vectors, which defines the cross product vector <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

> [!NOTE] Notational Trick
> Students are often told that putting vectors in a matrix is a "notational trick" <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. The resulting vector is indeed the unique vector perpendicular to `v` and `w`, whose magnitude is the area of the appropriate parallelogram, and whose direction obeys the right-hand rule <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
>
> This method isn't just a coincidence; it's related to the concept of [[duality]] in linear algebra, which explains why the determinant is important here <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. While the geometric representation of the cross product vector is the essential takeaway, understanding the underlying mathematical reasons for this determinant trick can be explored in a deeper discussion on duality <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.