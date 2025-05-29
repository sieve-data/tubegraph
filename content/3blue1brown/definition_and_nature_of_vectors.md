---
title: Definition and Nature of Vectors
videoId: TgKwz5Ikpc8
---

From: [[3blue1brown]] <br/> 

The fundamental question of "What are [[understanding_vectors|vectors]]?" can be approached from several perspectives <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Perspectives on Vectors

### Vectors as Lists of Numbers
One definition considers a two-dimensional [[understanding_vectors|vector]] as fundamentally a pair of real numbers, which is conveniently visualized as an arrow on a flat plane <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Defining [[understanding_vectors|vectors]] primarily as a list of numbers offers clarity and unambiguousness <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This perspective makes concepts like four-dimensional or 100-dimensional [[understanding_vectors|vectors]] seem concrete and workable <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Vectors as Spatial Entities
However, for those fluent in linear algebra, particularly with changing [[unit_vectors_and_basis_vectors|basis]], there's a common sensation that one is dealing with a space that exists independently from the coordinates assigned to it <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Coordinates are seen as somewhat arbitrary, depending on the chosen [[unit_vectors_and_basis_vectors|basis vectors]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Core linear algebra concepts like determinants and [[dot_products_and_vectors|eigenvectors]] appear indifferent to the choice of coordinate systems <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. These properties are inherently spatial, and the underlying values do not change with a change in the coordinate system <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## [[functions_as_vectors|Functions as Vectors]]: A Generalization
[[functions_as_vectors|Functions]] can also possess "vector-ish" qualities and are another type of [[understanding_vectors|vector]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Vector Operations on Functions
Just as [[understanding_vectors|vectors]] can be added, there's a sensible way to add two [[functions_as_vectors|functions]], `f` and `g`, to produce a new [[functions_as_vectors|function]], `f + g` <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. The output of this new [[functions_as_vectors|function]] at any input `x` is the sum of the outputs of `f(x)` and `g(x)` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This process is analogous to adding [[understanding_vectors|vectors]] coordinate by coordinate, but with potentially infinitely many coordinates <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Similarly, scaling a [[functions_as_vectors|function]] by a real number involves scaling all its outputs by that number, mirroring [[understanding_vectors|vector]] scaling <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### Linear Transformations for Functions
Since [[understanding_vectors|vectors]] can be added and scaled, the problem-solving techniques of linear algebra can be applied to [[functions_as_vectors|functions]] <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. There is a concept of a [[visualizing_transformations_with_vectors|linear transformation]] for [[functions_as_vectors|functions]], which takes one [[functions_as_vectors|function]] and converts it into another <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
A familiar example from calculus is the derivative, which transforms one [[functions_as_vectors|function]] into another [[functions_as_vectors|function]] <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. These transformations are sometimes called "operators" in this context <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

A transformation is defined as [[visualizing_transformations_with_vectors|linear]] if it satisfies two properties:
*   **Additivity**: Applying the transformation to the sum of two [[understanding_vectors|vectors]] (`v` and `w`) yields the same result as adding the transformed versions of `v` and `w` <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Scaling**: Applying the transformation to a scaled [[understanding_vectors|vector]] (`c * v`) yields the same result as scaling the transformed version of `v` by the same amount (`c`) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

In essence, [[visualizing_transformations_with_vectors|linear transformations]] "preserve" the operations of [[understanding_vectors|vector]] addition and scalar multiplication <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. The visual concept of gridlines remaining parallel and evenly spaced is an illustration of these properties in 2D space <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

A significant consequence of these properties is that a [[visualizing_transformations_with_vectors|linear transformation]] is entirely defined by how it transforms the [[unit_vectors_and_basis_vectors|basis vectors]] <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. Any [[understanding_vectors|vector]] can be expressed as a combination of scaled and added [[unit_vectors_and_basis_vectors|basis vectors]], so its transformed version is found by scaling and adding the transformed [[unit_vectors_and_basis_vectors|basis vectors]] in the same manner <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This principle applies to [[functions_as_vectors|functions]] as well <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

### Example: The Derivative as a Matrix Transformation
The derivative is linear <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. For instance, the derivative of a sum of [[functions_as_vectors|functions]] is the sum of their derivatives, and the derivative of a scaled [[functions_as_vectors|function]] is the scaled derivative of the [[functions_as_vectors|function]] <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

To describe the derivative with a matrix, even for [[functions_as_vectors|function]] spaces which can be infinite-dimensional (e.g., polynomials) <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>:
1.  **Choose a Basis**: For polynomials, natural [[unit_vectors_and_basis_vectors|basis functions]] are pure powers of `x` (e.g., `1`, `x`, `x^2`, `x^3`, etc.) <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. This set of [[unit_vectors_and_basis_vectors|basis functions]] can be infinite, meaning polynomials can have infinitely many coordinates (though any single polynomial will have an infinite tail of zeros) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
2.  **Represent Polynomials as Coordinates**: A polynomial like `x^2 + 3x + 5` would be represented by coordinates `(5, 3, 1, 0, 0, ...)` <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
3.  **The Derivative Matrix**: In this coordinate system, the derivative is represented by an infinite matrix with positive integers counting down an offset diagonal <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
    *   This matrix can be constructed by taking the derivative of each [[unit_vectors_and_basis_vectors|basis function]] and placing the coordinates of the result into each column <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

This demonstrates that matrix-vector multiplication and taking a derivative, seemingly disparate concepts, are part of the same family, due to the derivative's linearity <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Many linear algebra concepts, like the [[dot_products_and_vectors|dot product]] or [[dot_products_and_vectors|eigenvectors]], have direct parallels in the world of [[functions_as_vectors|functions]] (e.g., inner product, eigenfunction) <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## What is a Vector? The Axiomatic Definition

There are many "vectorish" things in mathematics <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. As long as a set of objects has a reasonable notion of scaling and addition, the tools of linear algebra can be applied <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

These sets of "vectorish" things (e.g., arrows, lists of numbers, [[functions_as_vectors|functions]]) are called [[vector_spaces_and_axioms|vector spaces]] <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. To ensure that all definitions and discoveries in linear algebra apply generally, a list of rules, called [[vector_spaces_and_axioms|axioms]], is established for how [[understanding_vectors|vector]] addition and scaling must behave <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

> [!info] The Eight Axioms of [[vector_spaces_and_axioms|Vector Spaces]]
> These axioms serve as a checklist. If a defined set of objects and their operations satisfy these eight axioms, then the results of linear algebra can be applied to them <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This allows mathematicians to prove results abstractly, based only on these axioms, without needing to consider every specific type of [[vector_spaces_and_axioms|vector space]] <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

Consequently, modern linear algebra textbooks often define [[visualizing_transformations_with_vectors|linear transformations]] in terms of additivity and scaling, rather than more intuitive, specific geometric interpretations <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

The mathematician's answer to "What are [[understanding_vectors|vectors]]?" tends to ignore the specific form they take <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. Arrows, lists of numbers, [[functions_as_vectors|functions]], or even abstract "pi creatures" can be [[understanding_vectors|vectors]], provided their operations of addition and scaling adhere to the defined [[vector_spaces_and_axioms|axioms]] <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. Similar to how the number 3 is an abstraction for all possible triplets of things, [[understanding_vectors|vectors]] are an abstraction for all possible embodiments of objects within a [[vector_spaces_and_axioms|vector space]] <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

While starting with a concrete, visualizable setting like 2D space with arrows is beneficial for intuition <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>, it's important to understand that linear algebra tools apply much more generally, which is why academic texts often use abstract phrasing <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.