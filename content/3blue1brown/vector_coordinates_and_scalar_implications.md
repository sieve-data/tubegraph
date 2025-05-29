---
title: Vector coordinates and scalar implications
videoId: k7RM-ot2NWY
---

From: [[3blue1brown]] <br/> 

This article explores how vector coordinates relate to scalars and introduces fundamental concepts in [[linear_transformations_in_linear_algebra | linear algebra]], including basis vectors, linear combinations, and the span of vectors. It also touches on [[geometric_versus_numeric_understanding_in_linear_algebra | visualizing transformations with vectors]].

## Vector Coordinates as Scalar Multipliers

Building on the concepts of [[vector_addition_and_scalar_multiplication | vector addition and scalar multiplication]], [[vector_representation_and_coordinate_systems | vector coordinates]] establish a connection between pairs of numbers and two-dimensional vectors <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. When describing a vector numerically, such as `(3, -2)`, each coordinate should be thought of as a scalar <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. These scalars determine how much to stretch or squish other vectors <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

In the standard Cartesian (xy) coordinate system, two special vectors are crucial:
*   **i-hat**: A unit vector of length 1 pointing to the right (in the x-direction) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **j-hat**: A unit vector of length 1 pointing straight up (in the y-direction) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

For instance, with the vector `(3, -2)`, the x-coordinate `3` scales i-hat, stretching it by a factor of 3. The y-coordinate `-2` scales j-hat, stretching it by a factor of 2 and flipping its direction <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The vector described by these coordinates is the sum of these two scaled vectors <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This idea of adding two scaled vectors is a fundamental concept in linear algebra <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Basis of a Coordinate System

The two vectors, i-hat and j-hat, are collectively called the [[coordinate_systems_and_basis_vectors | basis]] of a coordinate system <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This means that when coordinates are viewed as scalars, the basis vectors are what those scalars actually operate on <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

An important point is that other basis vectors could be chosen to create a new, perfectly valid coordinate system <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. For example, any two vectors that don't line up can serve as basis vectors <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. By choosing two scalars to scale each of these new basis vectors and then adding the results, you can reach every possible two-dimensional vector <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This demonstrates that any numerical description of vectors depends on an implicit choice of basis vectors <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## Linear Combinations

The act of scaling two vectors and adding them together is known as a **linear combination** of those two vectors <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. The term "linear" can be intuitively understood by imagining one scalar fixed while the other changes freely; the tip of the resulting vector traces a straight line <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

If both scalars in a linear combination are allowed to range freely, two primary outcomes are possible:
1.  **Most pairs of vectors**: You will be able to reach every possible point in the plane, meaning every two-dimensional vector is accessible <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
2.  **Aligned vectors**: If the two original vectors happen to line up (are collinear), the tip of the resulting vector will be limited to a single line passing through the origin <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
3.  **Zero vectors**: If both vectors are zero, the combination is stuck at the origin <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Span of Vectors

The **span** of a given pair of vectors is the set of all possible vectors that can be reached using a linear combination of those vectors <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. In two dimensions:
*   The span of most pairs of 2D vectors is all vectors of 2D space <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   If the vectors line up, their span is all vectors whose tips sit on a certain line <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

The concept of span essentially asks what vectors can be reached using only the fundamental operations of [[vector_addition_and_scalar_multiplication | vector addition and scalar multiplication]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Visualizing Span

To visualize collections of vectors, it's common to represent each vector simply by the point at its tip, assuming the vector's tail is at the origin <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Thus, to think about all vectors whose tips sit on a line, one simply considers the line itself <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Similarly, all two-dimensional vectors can be conceptualized as the infinite flat sheet of two-dimensional space <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

### Span in Three Dimensions

The idea of span becomes more complex in three-dimensional space <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Span of two 3D vectors**: If two vectors in 3D space are not collinear, their span forms a flat sheet (a plane) cutting through the origin of 3D space <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This sheet represents all possible linear combinations of the two vectors <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   **Span of three 3D vectors**: A linear combination of three vectors involves choosing three scalars, scaling each vector, and adding them together <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   If the third vector is already within the span of the first two (i.e., it lies on the plane defined by the first two), then adding it does not change the span; you remain on the same flat sheet <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   If the third vector is chosen randomly and is not in the span of the first two, it unlocks access to every possible three-dimensional vector. This can be visualized as the third vector moving the plane defined by the first two throughout all of 3D space <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

## Linear Dependence and Independence

When considering multiple vectors, if one or more vectors can be removed without reducing the span of the set, these vectors are said to be **linearly dependent** <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. This also means that one of the vectors can be expressed as a linear combination of the others, as it's already within their span <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

Conversely, if each vector in a set genuinely adds another dimension to the span, they are considered **linearly independent** <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

## Technical Definition of a Basis

With these concepts in mind, the technical definition of a [[coordinate_systems_and_basis_vectors | basis]] of a space is: **a set of linearly independent vectors that span that space** <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This definition makes intuitive sense because:
*   "Span that space" means the basis vectors can combine to form any vector in that space.
*   "Linearly independent" means that no vector in the basis is redundant; each one contributes uniquely to the span, ensuring the most efficient set of vectors to describe the space.