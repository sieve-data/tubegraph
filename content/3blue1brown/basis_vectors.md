---
title: basis vectors
videoId: k7RM-ot2NWY
---

From: [[3blue1brown]] <br/> 

When describing [[understanding_vectors_in_linear_algebra | vectors]] using coordinates, there's a close relationship between the numbers and the visual representation of the vector <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. A deeper understanding of these [[coordinate_systems_and_basis_vectors | coordinates]] is central to linear algebra <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Coordinates as Scalars of Basis Vectors

Consider a pair of numbers like (3, -2) meant to describe a [[nature_of_vectors | vector]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</sup>. Each coordinate should be thought of as a scalar that stretches or squishes [[understanding_vectors_in_linear_algebra | vectors]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

In the standard XY [[coordinate_systems_and_basis_vectors | coordinate system]], two special [[understanding_vectors_in_linear_algebra | vectors]] exist:
*   **i-hat**: The unit vector pointing right with length 1 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This is also called the unit vector in the x-direction <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **j-hat**: The unit vector pointing straight up with length 1 <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This is also called the unit vector in the y-direction <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

The x-coordinate of a vector acts as a scalar that scales i-hat (e.g., stretching it by a factor of 3) <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Similarly, the y-coordinate scales j-hat (e.g., flipping it and stretching it by a factor of 2) <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The vector that these [[coordinate_systems_and_basis_vectors | coordinates]] describe is the sum of these two scaled [[understanding_vectors_in_linear_algebra | vectors]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

These two [[understanding_vectors_in_linear_algebra | vectors]], i-hat and j-hat, are collectively called the **basis of a coordinate system** <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. When [[coordinate_systems_and_basis_vectors | coordinates]] are viewed as scalars, the [[basis_vectors_in_threedimensional_space | basis vectors]] are what those scalars operate upon <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Choosing Different Basis Vectors

It's possible to choose different [[basis_vectors_in_threedimensional_space | basis vectors]] to establish a new, valid [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. For example, two different [[understanding_vectors_in_linear_algebra | vectors]] not aligned can serve this purpose <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

A new pair of [[basis_vectors_in_threedimensional_space | basis vectors]] still allows for a direct correlation between pairs of numbers and two-dimensional [[understanding_vectors_in_linear_algebra | vectors]], though the specific association will differ from the standard i-hat and j-hat basis <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This highlights that any numerical description of [[understanding_vectors_in_linear_algebra | vectors]] implicitly relies on the choice of [[basis_vectors_in_threedimensional_space | basis vectors]] being used <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### Linear Combinations

The process of scaling two [[understanding_vectors_in_linear_algebra | vectors]] and then adding them together is called a **linear combination** of those two [[understanding_vectors_in_linear_algebra | vectors]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   If one scalar is fixed and the other varies freely, the tip of the resulting vector traces a straight line <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   If both scalars vary freely, two outcomes are possible for two-dimensional [[understanding_vectors_in_linear_algebra | vectors]]:
    *   For most pairs of [[understanding_vectors_in_linear_algebra | vectors]], every possible point in the plane can be reached <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
    *   If the two original [[understanding_vectors_in_linear_algebra | vectors]] are collinear, the resulting vector's tip is confined to a single line passing through the origin <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
    *   If both [[understanding_vectors_in_linear_algebra | vectors]] are zero, the only reachable point is the origin <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Span of Vectors

The **[[span_of_vectors | span of vectors]]** refers to the set of all possible [[understanding_vectors_in_linear_algebra | vectors]] that can be reached using a linear combination of a given set of [[understanding_vectors_in_linear_algebra | vectors]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

The [[span_of_vectors | span of most]] pairs of two-dimensional [[understanding_vectors_in_linear_algebra | vectors]] covers all of 2D space <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. However, if the [[understanding_vectors_in_linear_algebra | vectors]] align, their [[span_of_vectors | span]] is limited to all [[understanding_vectors_in_linear_algebra | vectors]] whose tips lie on a specific line <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. The [[span_of_vectors | span]] essentially asks what [[understanding_vectors_in_linear_algebra | vectors]] are reachable using only [[vector_space_axioms | vector addition]] and [[scalar_multiplication | scalar multiplication]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

When conceptualizing collections of [[understanding_vectors_in_linear_algebra | vectors]] (like a [[span_of_vectors | span]]), it's common to represent each vector simply by the point at its tip, assuming its tail is at the origin <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Thus, the [[span_of_vectors | span]] of two vectors that fill a plane can be thought of as the infinite flat sheet of 2D space itself <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### Basis Vectors in Three-Dimensional Space

The concept of [[span_of_vectors | span]] extends to [[basis_vectors_in_threedimensional_space | three-dimensional space]] <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   The [[span_of_vectors | span]] of two non-collinear [[basis_vectors_in_threedimensional_space | vectors in 3D space]] is a flat plane that passes through the origin <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This plane represents all possible [[linear_combination | linear combinations]] of those two [[understanding_vectors_in_linear_algebra | vectors]] <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   Adding a third vector to the [[linear_combination | linear combination]] <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>:
    *   If the third vector already lies within the [[span_of_vectors | span]] of the first two (i.e., on the same plane), adding it doesn't change the [[span_of_vectors | span]]; it remains the same flat sheet <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   If the third vector does *not* lie on the [[span_of_vectors | span]] of the first two, it unlocks access to every possible [[basis_vectors_in_threedimensional_space | three-dimensional vector]], sweeping the plane through all of space <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

### Linear Dependence and Independence

[[linear_dependence_and_independence | Linear dependence]] and [[linear_dependence_and_independence | independence]] describe whether [[understanding_vectors_in_linear_algebra | vectors]] in a set are redundant in terms of their [[span_of_vectors | span]]:
*   **Linearly Dependent**: A set of [[understanding_vectors_in_linear_algebra | vectors]] is linearly dependent if one or more vectors can be removed without reducing the [[span_of_vectors | span]] <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This means one of the [[understanding_vectors_in_linear_algebra | vectors]] can be expressed as a [[linear_combination | linear combination]] of the others <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Linearly Independent**: If each vector in a set genuinely adds another dimension to the [[span_of_vectors | span]], they are said to be linearly independent <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

## Technical Definition of a Basis

> [!INFO] Definition
> A **basis of a space** is defined as a set of [[linear_dependence_and_independence | linearly independent]] [[understanding_vectors_in_linear_algebra | vectors]] that [[span_of_vectors | span]] that space <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

This definition reinforces the idea that [[basis_vectors_in_threedimensional_space | basis vectors]] are a minimal set of [[understanding_vectors_in_linear_algebra | vectors]] capable of generating the entire space they reside in, without any redundancy.