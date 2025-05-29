---
title: Matrix representations of linear transformations
videoId: kYB8IZa5AuE
---

From: [[3blue1brown]] <br/> 

The concept of a [[linear_transformations_in_linear_algebra | linear transformation]] and its relationship to matrices is a fundamental topic in linear algebra, often clarifying many other concepts <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This article focuses on [[threedimensional_linear_transformations | two-dimensional linear transformations]] and their connection to matrix-vector multiplication, aiming for a [[visual_understanding_of_linear_transformations | visual understanding]] rather than memorization <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## What is a Transformation?

A transformation is essentially a function that takes inputs and produces outputs <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. In linear algebra, transformations typically take an input vector and output another vector <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

The term "transformation" suggests a visual way to understand this input-output relationship:
*   **Movement**: Imagine an input vector *moving* to become its output vector <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Space Morphing**: To understand the transformation as a whole, visualize every possible input vector moving to its corresponding output vector <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   **Points not Arrows**: Rather than arrows, vectors can be conceptualized as single points at their tips <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Thus, a transformation involves every point in space moving to another point <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **Grid Visualization**: For [[threedimensional_linear_transformations | two-dimensional transformations]], visualizing how an infinite grid of points moves can provide a clear understanding of the transformation's overall shape <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Keeping a copy of the original grid in the background can help track relative movement <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This gives the feeling of space itself squishing and morphing <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## What is a [[linear_transformations_in_linear_algebra | Linear Transformation]]?

While arbitrary transformations can be complex <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>, linear algebra focuses on a special, easier-to-understand type: [[linear_transformations_in_linear_algebra | linear transformations]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Visually, a transformation is linear if it satisfies two key properties:
1.  **Lines Remain Lines**: All lines in the grid must remain straight lines; they cannot become curved <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
2.  **Origin Fixed**: The origin (0,0) must remain in its original position <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

**Examples of Non-Linear Transformations:**
*   A transformation where lines become curvy is not linear <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   A transformation that keeps lines straight but moves the origin is not linear <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   A transformation that appears to keep horizontal/vertical lines straight but curves diagonal lines (or otherwise distorts spacing unevenly) is not linear <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

In general, [[visual_intuition_of_linear_transformations | linear transformations]] keep grid lines parallel and evenly spaced <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Examples include rotations about the origin <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

## Describing [[linear_transformations_in_linear_algebra | Linear Transformations]] Numerically with Matrices

A remarkable property of [[linear_transformations_in_linear_algebra | linear transformations]] is that to describe them numerically, you only need to record where the two standard basis vectors, i-hat (unit vector along the x-axis) and j-hat (unit vector along the y-axis), land after the transformation <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

This is because the properties of a [[linear_transformations_in_linear_algebra | linear transformation]] (grid lines remaining parallel and evenly spaced) have a crucial consequence:
*   If a vector **v** starts as a [[composition_of_linear_transformations | linear combination]] of i-hat and j-hat (e.g., v = `x` * i-hat + `y` * j-hat) <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>, then after the transformation, the new vector **v'** will be the *same* [[composition_of_linear_transformations | linear combination]] of where i-hat and j-hat landed (e.g., v' = `x` * (transformed i-hat) + `y` * (transformed j-hat)) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

This means you can determine where *any* vector lands based solely on where i-hat and j-hat land <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

### [[matrix_representation_of_transformations | Matrix Representation]]

A two-dimensional [[linear_transformations_in_linear_algebra | linear transformation]] is completely described by just four numbers: the two coordinates for where i-hat lands and the two coordinates for where j-hat lands <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. These coordinates are conventionally packaged into a 2x2 grid of numbers called a **2x2 matrix** <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

*   The **columns** of the [[matrix_representation_of_linear_transformations | matrix]] represent the coordinates of the transformed i-hat and j-hat basis vectors <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
    *   The first column (A, C) represents where the first basis vector (i-hat) lands <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
    *   The second column (B, D) represents where the second basis vector (j-hat) lands <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Matrix-Vector Multiplication

If you are given a 2x2 [[matrix_representation_of_linear_transformations | matrix]] describing a [[linear_transformations_in_linear_algebra | linear transformation]] and a specific vector (x, y), you can find where the transformation takes that vector by performing **matrix-vector multiplication** <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

The process is:
1.  Take the coordinates of the vector.
2.  Multiply them by the corresponding columns of the [[matrix_representation_of_linear_transformations | matrix]].
3.  Add the results together <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

Given a [[matrix_representation_of_linear_transformations | matrix]] `[[A B], [C D]]` and a vector `[x, y]`:

```
| A  B |   | x |   =   x * | A |   +   y * | B |   =   | Ax + By |
| C  D |   | y |       | C |       | D |       | Cx + Dy |
```
This calculation corresponds to finding the [[composition_of_linear_transformations | linear combination]] of the transformed basis vectors <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Thinking of the columns as the transformed basis vectors and the result as their appropriate [[composition_of_linear_transformations | linear combination]] provides an intuitive understanding of matrix-vector multiplication <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### Examples of [[matrix_representation_of_linear_transformations | Matrix Representations]]

*   **90-degree Counterclockwise Rotation**:
    *   i-hat lands at (0, 1) <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
    *   j-hat lands at (-1, 0) <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
    *   Matrix: `[[0 -1], [1 0]]` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

*   **Shear Transformation**:
    *   i-hat remains fixed at (1, 0) <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
    *   j-hat moves to (1, 1) <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
    *   Matrix: `[[1 1], [0 1]]` <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### Deducing Transformation from a Matrix

Given a [[matrix_representation_of_linear_transformations | matrix]], such as `[[1 3], [2 1]]`, one can deduce its transformation by imagining where i-hat (1, 2) and j-hat (3, 1) land and observing how the rest of space moves while keeping gridlines parallel and evenly spaced <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

If the vectors where i-hat and j-hat land are linearly dependent (one is a scaled version of the other), the [[linear_transformations_in_linear_algebra | linear transformation]] will squish all of two-dimensional space onto a single line (the one-dimensional span of those vectors) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## Conclusion

[[Linear_transformations_in_linear_algebra | Linear transformations]] are a way to move space such that gridlines remain parallel and evenly spaced, and the origin stays fixed <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. These transformations can be described using a few numbers: the coordinates of where each basis vector lands <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

Matrices provide a language to describe these transformations, where the columns represent the transformed basis vectors <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Matrix-vector multiplication is simply a way to compute the effect of that transformation on a given vector <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

Understanding that every [[matrix_representation_of_linear_transformations | matrix]] can be interpreted as a transformation of space is crucial for grasping deeper concepts in linear algebra, such as matrix multiplication, determinants, change of basis, and eigenvalues <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.