---
title: Matrix multiplication as applying transformations
videoId: XkY2DOUCWMU
---

From: [[3blue1brown]] <br/> 

## Recap: Linear Transformations and Matrices

[[linear_transformations_and_matrices | Linear transformations]] are functions that take vectors as inputs and produce vectors as outputs <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Visually, they "smoosh around space" such that grid lines remain parallel and evenly spaced, and the origin stays fixed <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A key takeaway is that a [[linear_transformations_and_matrices | linear transformation]] is entirely determined by where it moves the basis vectors of the space, such as i-hat and j-hat in two dimensions <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

Any vector can be described as a linear combination of these basis vectors (e.g., a vector `(x, y)` is `x` times i-hat plus `y` times j-hat) <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. After a [[linear_transformations_and_matrices | transformation]], the vector's new position will be `x` times the transformed i-hat plus `y` times the transformed j-hat <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

The convention is to record the coordinates where i-hat and j-hat land as the columns of a [[linear_transformations_and_matrices | matrix]] <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. [[matrix_vector_multiplication | Matrix-vector multiplication]] is defined as the sum of the scaled versions of these columns by `x` and `y` <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. In this way, a [[matrix_representation_of_linear_transformations | matrix represents a specific linear transformation]], and [[matrix_vector_multiplication | multiplying a matrix by a vector]] computationally applies that [[linear_transformations_and_matrices | transformation]] to the vector <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Composing Transformations

Often, one might want to describe the effect of applying one [[linear_transformations_and_matrices | transformation]] and then another <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. For example, rotating a plane 90 degrees counterclockwise and then applying a shear <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. The overall effect is another [[linear_transformations_and_matrices | linear transformation]], distinct from the individual ones <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This new [[linear_transformations_and_matrices | transformation]] is called the *composition* of the two separate [[linear_transformations_and_matrices | transformations]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

Like any [[linear_transformations_and_matrices | linear transformation]], this composed transformation can be described by its own [[linear_transformations_and_matrices | matrix]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. To find this new [[linear_transformations_and_matrices | matrix]], one must follow where i-hat and j-hat ultimately land after both [[linear_transformations_and_matrices | transformations]] <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. The final landing spot of i-hat becomes the first column of the new [[linear_transformations_and_matrices | matrix]], and j-hat's final position becomes the second column <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

This new [[linear_transformations_and_matrices | matrix]] captures the overall effect of the successive [[linear_transformations_and_matrices | transformations]] as a single action <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## [[Matrix multiplication and transformations | Matrix Multiplication]]

If a vector is put through a sequence of [[linear_transformations_and_matrices | transformations]] (e.g., rotation then shear), computing its final position numerically involves [[matrix_vector_multiplication | multiplying]] the vector by the first [[linear_transformations_and_matrices | transformation's]] [[linear_transformations_and_matrices | matrix]], and then [[matrix_vector_multiplication | multiplying]] the result by the second [[linear_transformations_and_matrices | transformation's]] [[linear_transformations_and_matrices | matrix]] <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. The result should be the same as if the vector was simply [[matrix_vector_multiplication | multiplied]] by the single, new "composition" [[linear_transformations_and_matrices | matrix]] <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

This suggests that the new composition [[linear_transformations_and_matrices | matrix]] can be seen as the [[matrix_multiplication_and_transformations | product]] of the original two [[linear_transformations_and_matrices | matrices]] <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Computing the [[matrix_multiplication_and_transformations | Matrix Product]]

To compute the [[matrix_multiplication_and_transformations | product]] of two [[linear_transformations_and_matrices | matrices]] (let's say `M2` then `M1`, where `M1` is applied first), follow these steps:
1.  **Follow i-hat**: The initial landing spot of i-hat after applying the first [[linear_transformations_and_matrices | transformation]] (`M1`) is the first column of `M1` <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. To find where it ends up after the second [[linear_transformations_and_matrices | transformation]] (`M2`), [[matrix_vector_multiplication | multiply]] the [[linear_transformations_and_matrices | matrix]] `M2` by the vector representing i-hat's position after `M1` <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This result forms the first column of the [[matrix_multiplication_and_transformations | composition matrix]] <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
2.  **Follow j-hat**: Similarly, j-hat initially lands on the second column of `M1` <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. [[matrix_vector_multiplication | Multiply]] the [[linear_transformations_and_matrices | matrix]] `M2` by this vector to find its final position <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This result forms the second column of the [[matrix_multiplication_and_transformations | composition matrix]] <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

This process demonstrates that the first column of the [[matrix_multiplication_and_transformations | composition matrix]] will always equal the left [[linear_transformations_and_matrices | matrix]] times the first column of the right [[linear_transformations_and_matrices | matrix]] <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>, and similarly for the second column <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

> [!NOTE] Reading Order
> When [[matrix_multiplication_and_transformations | multiplying two matrices]], the [[linear_transformations_and_matrices | transformation]] represented by the [[linear_transformations_and_matrices | matrix]] on the right is applied first, followed by the [[linear_transformations_and_matrices | transformation]] on the left <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This "right-to-left" reading order stems from function notation <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Properties of [[Matrix multiplication and transformations | Matrix Multiplication]]

Thinking about [[matrix_multiplication_and_transformations | matrix multiplication]] as applying one [[linear_transformations_and_matrices | transformation]] after another provides a strong conceptual framework for understanding its properties <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

### Non-Commutativity (Order Matters)
The order in which [[linear_transformations_and_matrices | matrices]] are [[matrix_multiplication_and_transformations | multiplied]] typically matters <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. For example, if a shear [[linear_transformations_and_matrices | transformation]] is applied first, then a 90-degree rotation, the overall effect is different from applying the rotation first and then the shear <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This visual difference clearly shows that the order of [[matrix_multiplication_and_transformations | multiplication]] changes the final outcome <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Associativity (Parentheses Don't Matter)
[[Matrix multiplication and transformations | Matrix multiplication]] is associative, meaning that for three [[linear_transformations_and_matrices | matrices]] A, B, and C, `(A × B) × C` is the same as `A × (B × C)` <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Numerically proving this can be complex <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. However, when viewed through the lens of [[linear_transformations_and_matrices | transformations]], this property is trivial <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

> [!EXAMPLE] Proof of Associativity
> The statement `(A × B) × C = A × (B × C)` simply means that if you first apply C, then B, then A, it's the same as applying C, then B, then A <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. The sequence of [[linear_transformations_and_matrices | transformations]] is identical regardless of how the [[matrix_multiplication_and_transformations | matrix multiplications]] are grouped <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. This geometric interpretation provides an honest and intuitive proof of associativity <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

Visualizing [[linear_transformations_and_matrices | transformations]] and their compositions can provide a deeper understanding of [[matrix_multiplication_and_transformations | matrix multiplication]] than rote memorization of formulas <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.