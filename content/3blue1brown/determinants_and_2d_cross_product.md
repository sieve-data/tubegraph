---
title: Determinants and 2D cross product
videoId: eu6i7WJeinw
---

From: [[3blue1brown]] <br/> 

This article explores the standard introduction to the cross product, particularly its definition and computation in two dimensions, and its connection to [[Understanding determinants in linear algebra | determinants]]. It follows a previous discussion on the [[Linear transformations and dot products | dot product]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Introduction to Cross Products <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>

The cross product, like the dot product, has both a standard introduction and a deeper understanding when viewed through [[Linear transformations and dot products | linear transformations]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This discussion focuses on the main points typically taught about the cross product <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## The 2D Cross Product <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>

In two dimensions, given two vectors `v` and `w`, their cross product relates to the parallelogram they span <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This parallelogram is formed by placing a copy of `v` at the tip of `w`, and a copy of `w` at the tip of `v` <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

The cross product of `v` and `w` (written as `v x w`) is defined as the area of this parallelogram, with a crucial addition: orientation <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Orientation and Order <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>

*   If `v` is to the right of `w`, then `v x w` is positive and equal to the parallelogram's area <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   If `v` is to the left of `w`, then `v x w` is negative, specifically the negative area of the parallelogram <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

This implies that the order of the vectors matters: `w x v` will be the negative of `v x w` <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The standard way to remember the ordering is that `i-hat x j-hat` (the two basis vectors in order) should result in a positive value <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. The order of basis vectors inherently defines the orientation <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

For example, if the parallelogram's area is 7 and `v` is to the left of `w`, then `v x w` is -7 <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Computing the 2D Cross Product with Determinants <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

The computation of the 2D cross product utilizes the [[Understanding determinants in linear algebra | determinant]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. To compute `v x w`:

1.  Create a matrix where the coordinates of `v` form the first column.
2.  The coordinates of `w` form the second column <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
3.  Compute the determinant of this 2x2 matrix <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

This method works because a matrix with `v` and `w` as its columns represents a [[Linear transformations and dot products | linear transformation]] that maps the basis vectors `i-hat` and `j-hat` to `v` and `w`, respectively <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

The [[Understanding determinants in linear algebra | determinant]] measures how areas change under a transformation <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. The unit square, initially defined by `i-hat` and `j-hat` (with area 1), transforms into the parallelogram spanned by `v` and `w` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Therefore, the [[Understanding determinants in linear algebra | determinant]] directly yields the area of this parallelogram <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. A negative [[Understanding determinants in linear algebra | determinant]] indicates that the orientation was flipped during the transformation, meaning `v` is to the left of `w` <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### Example <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>

Let `v = (-3, 1)` and `w = (2, 1)`:
```
v x w = det(
    [-3,  2],
    [ 1,  1]
)
```
The [[Understanding determinants in linear algebra | determinant]] is `(-3 * 1) - (2 * 1) = -3 - 2 = -5` <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. This means the parallelogram has an area of 5, and since the result is negative, `v` is to the left of `w` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Properties of the 2D Cross Product <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>

Exploring the concept intuitively reveals several properties:

*   **Perpendicularity and Magnitude**: When two vectors are perpendicular, or close to it, their cross product is larger <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This is because the area of the parallelogram is maximized when its sides are close to being perpendicular <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Scaling**: If one of the vectors is scaled (e.g., `v` is multiplied by 3), the area of the parallelogram also scales by the same factor <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Thus, `3v x w` will be exactly 3 times the value of `v x w` <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

## Transition to the 3D Cross Product <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>

While the 2D operation described is a valid mathematical concept, the "true" cross product is typically defined in three dimensions <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. It combines two 3D vectors to produce a new 3D vector <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The area of the parallelogram spanned by the two vectors still plays a significant role <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The length of the resulting vector is this area <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. The direction of this new vector is perpendicular to the parallelogram, determined by the [[3D cross product and the right hand rule | right hand rule]] <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

For computing the 3D cross product, a process involving the 3D [[Understanding determinants in linear algebra | determinant]] is commonly used <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. This involves setting up a 3D matrix where the second and third columns contain the coordinates of the vectors `v` and `w`, and the first column contains the basis vectors `i-hat`, `j-hat`, and `k-hat` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. While this might seem like a "notational trick" <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>, computing the [[Understanding determinants in linear algebra | determinant]] of this matrix yields a linear combination of the basis vectors, representing the cross product vector <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. The underlying reason for this connection lies in the concept of [[Symmetry in dot products | duality]] <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.