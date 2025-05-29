---
title: composition of linear transformations
videoId: XkY2DOUCWMU
---

From: [[3blue1brown]] <br/> 

## Recap: Understanding Linear Transformations
[[linear_transformations | Linear transformations]] are functions that take vectors as inputs and produce vectors as outputs <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. [[visual_understanding_of_linear_transformations | Visually]], they can be thought of as "smooshing around space" in a way that grid lines remain parallel and evenly spaced, and the origin stays fixed <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

A key concept is that a [[linear_transformations | linear transformation]] is entirely determined by where it moves the basis vectors of the space, such as i-hat and j-hat in two dimensions <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Any other vector can be described as a [[Linear Transformations and Linearity | linear combination]] of these basis vectors <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For a vector with coordinates (x, y), it is `x` times i-hat plus `y` times j-hat <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

After a [[linear_transformations | transformation]], the vector's new position will be `x` times the transformed i-hat plus `y` times the transformed j-hat <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. The coordinates where i-hat and j-hat land are conventionally recorded as the columns of a [[matrix_representation_of_linear_transformations | matrix]] <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. [[matrix_representation_of_linear_transformations | Matrix-vector multiplication]] is defined as the sum of the scaled versions of these columns by `x` and `y` <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Thus, a [[matrix_representation_of_linear_transformations | matrix]] represents a specific [[linear_transformations | linear transformation]], and multiplying a [[matrix_representation_of_linear_transformations | matrix]] by a vector computationally applies that transformation <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Composing Linear Transformations
The **composition of [[linear_transformations | linear transformations]]** refers to the effect of applying one transformation and then another <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. For instance, rotating a plane 90 degrees counterclockwise and then applying a shear <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. The overall effect of these successive actions is itself another [[linear_transformations | linear transformation]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Representing Composed Transformations with Matrices
Like any [[linear_transformations | linear transformation]], a composite transformation can be described by its own unique [[matrix_representation_of_linear_transformations | matrix]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This matrix is found by tracking where the basis vectors (i-hat and j-hat) ultimately land after both transformations have been applied <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

**Example:**
If a rotation then a shear is applied:
- The ultimate landing spot for i-hat becomes the first column of the new matrix <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
- The ultimate landing spot for j-hat becomes the second column of the new matrix <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
This new matrix captures the entire effect of applying the rotation then the shear as a single action <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## Matrix-Matrix Multiplication
When a vector is first multiplied by a rotation [[matrix_representation_of_linear_transformations | matrix]] and then the result is multiplied by a shear [[matrix_representation_of_linear_transformations | matrix]], this sequence of operations is equivalent to applying the new composition matrix to the original vector <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This is what it means computationally to apply a sequence of [[linear_transformations | transformations]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

This concept leads to the definition of **matrix-matrix multiplication**, where the new matrix (the composition matrix) is considered the product of the original two matrices <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Calculating Matrix Products
To find the columns of the product matrix (representing M1 then M2):
1.  **For the first column:**
    *   Find where i-hat lands after applying the first transformation (M1) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. This is the first column of M1 <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   Multiply this resulting vector by the second transformation's matrix (M2) <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. The result is the first column of the composite matrix <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
2.  **For the second column:**
    *   Find where j-hat lands after applying the first transformation (M1) <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This is the second column of M1 <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
    *   Multiply this resulting vector by the second transformation's matrix (M2) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. The result is the second column of the composite matrix <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

> [!NOTE] Geometric Interpretation is Key
> Always remember that multiplying two matrices has the geometric meaning of applying one transformation then another <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This conceptual understanding is more valuable than rote memorization of the algebraic formula for matrix multiplication <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Reading Order
When performing matrix multiplication `M_left * M_right`, the transformations are applied from right to left <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. You first apply the transformation represented by the matrix on the right, then the transformation represented by the matrix on the left <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This convention stems from function notation, where functions are written to the left of variables (e.g., `f(g(x))`), requiring a right-to-left reading when composing functions <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Properties of Matrix Multiplication

### Non-Commutativity (Order Matters)
The order in which matrices are multiplied **does** matter <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
**Example:**
-   Applying a shear then a 90-degree rotation results in a different final state for the basis vectors compared to <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>
-   Applying a 90-degree rotation then a shear <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
Since the overall effect is clearly different, the order of matrix multiplication affects the outcome <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This can often be visualized without performing explicit matrix calculations <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### Associativity
Matrix multiplication is **associative** <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. For three matrices A, B, and C, `(A * B) * C` is equal to `A * (B * C)` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This means the grouping of operations (where parentheses are placed) does not change the final result <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

From a geometric perspective, this property is trivial: if you apply transformation C, then B, then A, it's the same sequence of actions regardless of how you group the matrix multiplications <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. It's simply applying the same three [[linear_transformations | transformations]] one after the other, in the same order <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This conceptual understanding serves as a robust proof for associativity <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

> [!TIP] Engage with the Concepts
> To deepen understanding, it's recommended to visualize two different [[linear_transformations | transformations]], consider the outcome of applying one after the other, and then numerically work out the [[matrix_representation_of_linear_transformations | matrix]] product <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

These concepts can be extended beyond two dimensions, which will be explored in future discussions <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.