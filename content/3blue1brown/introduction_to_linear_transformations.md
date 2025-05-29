---
title: Introduction to linear transformations
videoId: kYB8IZa5AuE
---

From: [[3blue1brown]] <br/> 

The concept of a [[linear_transformations_in_linear_algebra | linear transformation]] and its connection to [[matrix_representation_of_linear_transformations | matrices]] is a foundational topic in [[understanding_linear_algebra | linear algebra]] that helps other concepts "click" into place <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This article focuses on two-dimensional transformations and their relationship to [[matrix_representation_of_linear_transformations | matrix]]-vector multiplication <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## What is a Transformation?

A transformation is essentially a fancy word for a function <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. It takes inputs and produces an output for each one <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. In [[understanding_linear_algebra | linear algebra]], transformations typically take an input vector and output another vector <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

The word "transformation" is used to suggest a visual way of understanding this input-output relationship <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. To visualize transformations, one can imagine an input vector "moving over" to its output vector <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. To grasp the transformation as a whole, one might imagine watching every possible input vector move to its corresponding output vector <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

For a clearer [[visual_intuition_of_linear_transformations | visual intuition]], each vector can be conceptualized as a single point—the point where its tip sits <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This allows for imagining every point in space moving to some other point <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. In two dimensions, this can be visualized by applying the transformation to all points on an infinite grid <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Keeping a copy of the original grid in the background helps track relative movements <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This creates the feeling of space itself squishing and morphing <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## What Defines a Linear Transformation?

While arbitrary transformations can be complex, [[understanding_linear_algebra | linear algebra]] focuses on a special type called [[linear_transformations_and_linearity | linear transformations]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Visually, a transformation is linear if it possesses two key properties <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>:
1.  **Lines remain lines**: All lines in space must remain straight lines, without becoming curved <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
    *   For example, a transformation where lines get curvy is not linear <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
    *   Even if horizontal/vertical lines appear straight, a diagonal line might reveal curving, indicating it's not linear <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
2.  **Origin remains fixed**: The origin (0,0) must not move from its position <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   A transformation that moves the origin, even if it keeps lines straight, is not linear <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

In general, [[linear_transformations_and_linearity | linear transformations]] keep grid lines parallel and evenly spaced <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Examples include rotations about the origin <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

## Numerical Description of Linear Transformations

To describe these transformations numerically, especially for programming animations, one needs a formula to determine where a vector's coordinates land after the transformation <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

The crucial insight is that you only need to record where the two basis vectors, i-hat (1,0) and j-hat (0,1), land <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Everything else follows from this <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

Consider a vector `v` with coordinates (-1, 2), which can be written as `-1 * i-hat + 2 * j-hat` <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Due to the property that grid lines remain parallel and evenly spaced in a [[linear_transformations_and_linearity | linear transformation]], the transformed `v` will be `-1 * (where i-hat landed) + 2 * (where j-hat landed)` <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   If i-hat lands on (1, -2) <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   If j-hat lands on (3, 0) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
Then, `v` will land at `-1 * (1, -2) + 2 * (3, 0) = (-1, 2) + (6, 0) = (5, 2)` <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

This means that a vector, which starts as a linear combination of `i-hat` and `j-hat`, ends up as the *same* linear combination of where those two basis vectors landed <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This technique allows deducing where *any* vector lands, solely based on where `i-hat` and `j-hat` land <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

For a general vector `(x, y)`, if i-hat lands on `(a, c)` and j-hat lands on `(b, d)`, the vector `(x, y)` will land on `x * (a, c) + y * (b, d) = (ax + by, cx + dy)` <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Matrix Representation of Linear Transformations

A two-dimensional [[linear_transformations_in_linear_algebra | linear transformation]] is completely described by just four numbers: the two coordinates for where i-hat lands and the two coordinates for where j-hat lands <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

These coordinates are commonly packaged into a 2x2 grid of numbers called a [[matrix_representation_of_linear_transformations | matrix]] <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The columns of this [[matrix_representation_of_linear_transformations | matrix]] represent the transformed i-hat and j-hat vectors <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

If you have a 2x2 [[matrix_representation_of_linear_transformations | matrix]] describing a [[linear_transformations_in_linear_algebra | linear transformation]] and a specific vector, to find where the transformation takes that vector, you:
1.  Take the coordinates of the vector <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
2.  Multiply them by the corresponding columns of the [[matrix_representation_of_linear_transformations | matrix]] <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
3.  Add the results together <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

This process is known as [[matrix_representation_of_linear_transformations | matrix]]-vector multiplication <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. For a [[matrix_representation_of_linear_transformations | matrix]] `[[A, B], [C, D]]` and a vector `(x, y)`:
*   The first column `(A, C)` represents where i-hat lands <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   The second column `(B, D)` represents where j-hat lands <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   The resulting vector is `x * (A, C) + y * (B, D) = (Ax + By, Cx + Dy)` <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

It's more intuitive to think of the columns as the transformed basis vectors and the result as the appropriate linear combination of those vectors <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### [[applications_and_examples_of_linear_transformations | Examples]] of Linear Transformations represented by Matrices

*   **Rotation (90 degrees counterclockwise)**:
    *   i-hat lands on (0, 1) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
    *   j-hat lands on (-1, 0) <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
    *   [[matrix_representations_of_linear_transformations | Matrix]]: `[[0, -1], [1, 0]]` <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

*   **Shear**:
    *   i-hat remains fixed on (1, 0) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
    *   j-hat moves to (1, 1) <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
    *   [[matrix_representations_of_linear_transformations | Matrix]]: `[[1, 1], [0, 1]]` <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

*   **Deducing Transformation from a Matrix**:
    *   Given a [[matrix_representation_of_linear_transformations | matrix]] like `[[1, 3], [2, 1]]` <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
    *   Imagine moving i-hat to (1, 2) and j-hat to (3, 1) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. The rest of space moves while keeping gridlines parallel and evenly spaced <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
    *   If the vectors where i-hat and j-hat land are linearly dependent (one is a scaled version of the other), the transformation squishes all of 2D space onto a single line (the one-dimensional span of those two vectors) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## Key Takeaway

[[linear_transformations_in_linear_algebra | Linear transformations]] move space such that gridlines remain parallel and evenly spaced, and the origin stays fixed <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. These transformations are described by a few numbers: the coordinates of where each basis vector lands <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. [[matrix_representation_of_linear_transformations | Matrices]] provide a language to describe these transformations, with columns representing the transformed basis vectors <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. [[matrix_representation_of_linear_transformations | Matrix]]-vector multiplication is simply a way to compute the effect of the transformation on a given vector <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

The crucial understanding is that every time you see a [[matrix_representation_of_linear_transformations | matrix]], you can interpret it as a specific [[visual_understanding_of_linear_transformations | transformation]] of space <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. This deep understanding simplifies many advanced topics in [[understanding_linear_algebra | linear algebra]], including [[composition_of_linear_transformations | matrix multiplication]], determinants, change of basis, and eigenvalues <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.