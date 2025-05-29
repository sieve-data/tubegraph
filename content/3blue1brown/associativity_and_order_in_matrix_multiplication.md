---
title: Associativity and order in matrix multiplication
videoId: XkY2DOUCWMU
---

From: [[3blue1brown]] <br/> 

## Recap: Linear Transformations and their Matrix Representation

[[Linear transformations and matrices | Linear transformations]] are functions that take vectors as inputs and produce vectors as outputs <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Visually, they "smoosh around" space such that grid lines remain parallel and evenly spaced, and the origin stays fixed <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

A key property of [[linear transformations and matrices | linear transformations]] is that they are entirely determined by where they map the basis vectors (e.g., i-hat and j-hat in two dimensions) <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Any other vector can be described as a [[vector addition and scalar multiplication | linear combination]] of these basis vectors <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For a vector with coordinates (x, y), it's x times i-hat plus y times j-hat <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. After a transformation, the transformed vector will be x times the transformed i-hat plus y times the transformed j-hat <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

The convention for [[matrix representation of linear transformations | representing a linear transformation with a matrix]] is to record the coordinates of where i-hat and j-hat land as the columns of the matrix <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. [[Matrix vector multiplication | Matrix-vector multiplication]] is defined as the sum of the scaled versions of these columns, which computationally applies the transformation to a vector <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Matrix Multiplication as Composition of Transformations

Often, one might want to describe the combined effect of applying one transformation and then another, such as rotating the plane 90 degrees counterclockwise and then applying a shear <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. The overall effect is another [[linear transformations and matrices | linear transformation]], known as the *composition* of the two separate transformations <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

Like any [[linear transformations and matrices | linear transformation]], this new composite transformation can be described by its own unique matrix <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This new matrix is formed by tracking where the basis vectors (i-hat and j-hat) ultimately land after *both* transformations are applied <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. For instance, if i-hat ultimately lands at (1,1) and j-hat at (-1,0) after a rotation then a shear, the composition matrix would have columns (1,1) and (-1,0) <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This new matrix captures the overall effect as a single action <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

Numerically, applying a sequence of transformations (e.g., rotation then shear) to a vector means first [[matrix vector multiplication | multiplying]] the vector by the rotation matrix, then multiplying the resulting vector by the shear matrix <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This result will be identical to [[matrix vector multiplication | multiplying]] the vector directly by the new composition matrix <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This implies that the new composition matrix is the *product* of the original two matrices <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Computing the Matrix Product

To compute the product of two matrices, say M2 (left matrix) and M1 (right matrix) to get the composition matrix:
1.  **First Column**: Determine where i-hat lands after M1 (the first column of M1) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. Then, [[matrix vector multiplication | multiply]] this resulting vector by M2 to find its final landing spot <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This final vector becomes the first column of the composition matrix <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
2.  **Second Column**: Similarly, determine where j-hat lands after M1 (the second column of M1) <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. Then, [[matrix vector multiplication | multiply]] this resulting vector by M2 to find its final landing spot <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This becomes the second column of the composition matrix <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

This process highlights that the first column of the composition matrix is the left matrix times the first column of the right matrix, and similarly for the second column <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

> [!NOTE] Geometric Meaning of [[matrix multiplication and transformations | Matrix Multiplication]]
> Always remember that [[matrix multiplication as applying transformations | multiplying two matrices]] like this has the geometric meaning of applying one transformation then another <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This conceptual understanding is more important than rote memorization of the multiplication algorithm <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Order of Application (Reading Right to Left)

When performing [[matrix multiplication and transformations | matrix multiplication]] $M_2 M_1$, it implies applying the transformation represented by $M_1$ (the matrix on the right) first, and then applying the transformation represented by $M_2$ (the matrix on the left) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This right-to-left reading order stems from standard function notation, where functions are written to the left of variables <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Does Order Matter? Non-Commutativity

A natural question arises: does the order of matrices matter when multiplying them?
Consider a shear transformation and a 90-degree rotation <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>:
*   **Shear then Rotate**: If you apply a shear first, then a rotation, i-hat might end up at (0,1) and j-hat at (-1,1) <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
*   **Rotate then Shear**: If you apply a rotation first, then a shear, i-hat might end up at (1,1) and j-hat at (-1,0) <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

The overall effects in these two scenarios are clearly different <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Therefore, the order in which matrices are multiplied **does matter**; [[matrices and their properties | matrix multiplication]] is generally non-commutative. Thinking about this in terms of transformations allows for visualization and understanding without numerical calculation <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

## Associativity of Matrix Multiplication

[[Matrices and their properties | Matrix multiplication]] is, however, *associative* <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This means for three matrices A, B, and C, it does not matter if you compute (A * B) * C or A * (B * C); the result is the same <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

While proving this numerically can be "horrible" <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>, its truth becomes "trivial" when considering the geometric interpretation of [[matrix multiplication as applying transformations | matrix multiplication]]:

> [!BLOCKQUOTE]
> What it's saying is that if you first apply C, then B, then A, it's the same as applying C, then B, then A <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. I mean, there's nothing to prove. You're just applying the same three things one after the other, all in the same order <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. This is an honest-to-goodness proof that [[matrices and their properties | matrix multiplication]] is associative, and even better than that, it's a good explanation for why that property should be true <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

Understanding [[matrix multiplication as applying transformations | matrix multiplication]] through the lens of composing [[linear transformations and matrices | linear transformations]] provides a powerful conceptual framework for understanding its properties <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.