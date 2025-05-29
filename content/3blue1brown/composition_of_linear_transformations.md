---
title: Composition of linear transformations
videoId: XkY2DOUCWMU
---

From: [[3blue1brown]] <br/> 

[[Linear transformations]] are functions that take vectors as inputs and produce vectors as outputs <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Visually, they [[visualizing_linear_transformations | smoosh space around]] in a way that grid lines remain parallel and evenly spaced, and the origin stays fixed <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

A [[linear_transformations | linear transformation]] is entirely defined by where it moves the basis vectors of the space, such as i-hat and j-hat in two dimensions <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Any other vector, expressed as a linear combination of these basis vectors (e.g., x,y is `x*i-hat + y*j-hat`) <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, will land at `x` times the transformed i-hat plus `y` times the transformed j-hat <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

The coordinates of where i-hat and j-hat land form the columns of a [[matrix_representation_of_linear_transformations | matrix]], and multiplying this [[matrix_representation_of_linear_transformations | matrix]] by a vector computationally applies the transformation to that vector <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Describing Successive Transformations

Often, it's necessary to describe the combined effect of applying one [[linear_transformations | transformation]] and then another <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. For example, first rotating the plane 90 degrees counterclockwise, then applying a shear <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. The overall effect of these sequential actions is itself another [[linear_transformations | linear transformation]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

This new, combined [[linear_transformations | linear transformation]] is referred to as the **composition** of the individual transformations <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Like any [[linear_transformations | linear transformation]], this composition can be described by its own [[matrix_representation_of_transformations | matrix]], determined by where i-hat and j-hat ultimately land after both transformations are applied <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

For instance, if i-hat ultimately lands at (1,1) and j-hat lands at (-1,0) after a rotation then a shear, the composition matrix would have columns (1,1) and (-1,0) respectively <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This single matrix encapsulates the entire effect of applying both transformations sequentially <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## Matrix Multiplication: The Product of Transformations

Numerically, applying one transformation then another to a vector involves multiplying the vector by the first transformation's [[matrix_representation_of_transformations | matrix]], and then multiplying the result by the second transformation's [[matrix_representation_of_transformations | matrix]] <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. The result of this two-step process should be identical to multiplying the original vector by the composition matrix <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This relationship leads to the definition of **matrix multiplication**: the composition matrix is the product of the original two matrices <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

The process of computing the columns of the composite matrix involves following the journey of the basis vectors:
1.  **For the first column of the composite matrix**: Determine where i-hat lands after the first transformation (this is the first column of the rightmost matrix). Then, apply the second transformation (the leftmost matrix) to this intermediate vector. This matrix-vector product gives the first column of the composite matrix <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
2.  **For the second column of the composite matrix**: Similarly, determine where j-hat lands after the first transformation (the second column of the rightmost matrix). Apply the second transformation to this intermediate vector. This matrix-vector product gives the second column of the composite matrix <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

This means that the first column of the composition matrix is the left matrix multiplied by the first column of the right matrix, and the second column of the composition matrix is the left matrix multiplied by the second column of the right matrix <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

### Order of Operations

When performing matrix multiplication, the transformations are read from right to left <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. The transformation represented by the matrix on the right is applied first, followed by the transformation represented by the matrix on the left <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This convention aligns with standard function notation <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## [[Properties of linear transformations | Properties of Matrix Multiplication]]

### Non-Commutativity

A crucial [[properties_of_linear_transformations | property]] of matrix multiplication is that the order of the matrices matters <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. That is, `A * B` is generally not equal to `B * A`.

For example, consider a shear transformation and a 90-degree rotation <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>:
-   If you first shear, then rotate, the final positions of the basis vectors (and thus the overall transformation) will be different than if you first rotate, then shear <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
-   The visual effect of these two sequences of transformations is clearly distinct <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

Understanding matrix multiplication as a composition of transformations makes this non-commutative [[properties_of_linear_transformations | property]] intuitive without needing numerical computation <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

### Associativity

Matrix multiplication *is* associative, meaning that for three matrices A, B, and C, `(A * B) * C` is equal to `A * (B * C)` <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This means the grouping of multiplications does not change the final product.

While numerically proving associativity can be "horrible" <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>, conceptually it is trivial when thinking about transformations <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. `(A * B) * C` means first applying C, then B, then A. `A * (B * C)` also means first applying C, then B, then A. Since both expressions describe the exact same sequence of transformations applied in the same order, they must be equal <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. This provides a direct and illuminating proof of the [[properties_of_linear_transformations | property]] <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

Understanding matrix multiplication as the composition of [[linear_transformations | linear transformations]] provides a powerful conceptual framework for grasping the [[properties_of_linear_transformations | properties of matrix multiplication]] <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.