---
title: Unit vectors and basis vectors
videoId: k7RM-ot2NWY
---

From: [[3blue1brown]] <br/> 

In [[coordinate_systems_and_basis_vectors | vector coordinates]], there is a relationship between pairs of numbers and two-dimensional vectors <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Each coordinate of a vector, such as `3, -2`, can be thought of as a scalar that stretches or squishes other vectors <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Unit Vectors: i-hat and j-hat

In the Cartesian (xy) [[coordinate_systems_and_basis_vectors | coordinate system]], there are two specific [[understanding_vectors | vectors]] known as unit vectors:
*   **i-hat**: The vector pointing to the right with a length of 1 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. It is also known as the unit vector in the x-direction <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   **j-hat**: The vector pointing straight up with a length of 1 <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It is also known as the unit vector in the y-direction <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

A vector's x-coordinate scales i-hat, while its y-coordinate scales j-hat <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. For example, a vector `3, -2` is formed by scaling i-hat by 3 and j-hat by -2, and then adding them together <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. In this sense, the vector is the sum of two scaled vectors <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Basis of a Coordinate System

The two vectors, i-hat and j-hat, are together called the **basis of a [[coordinate_systems_and_basis_vectors | coordinate system]]** <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. When coordinates are viewed as scalars, the basis vectors are what those scalars actually scale <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Different Basis Vectors
It is possible to choose different basis vectors to create a new, equally reasonable [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. For instance, two vectors pointing in different directions, such as one up-and-right and another down-and-right, can serve as a new basis <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

By choosing two scalars and scaling each of these new basis vectors before adding them, every possible two-dimensional vector can be reached <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This new pair of basis vectors provides a valid way to associate pairs of numbers with two-dimensional vectors, although this association will differ from that of the standard i-hat and j-hat basis <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Any numerical description of [[understanding_vectors | vectors]] depends on an implicit choice of basis vectors <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### Linear Combinations

When two [[understanding_vectors | vectors]] are scaled and then added together, this operation is called a **linear combination** of those two [[understanding_vectors | vectors]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. The term "linear" can be intuitively understood by noting that if one scalar is fixed and the other varies freely, the tip of the resulting vector traces a straight line <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

For three [[understanding_vectors | vectors]], a linear combination involves choosing three different scalars, scaling each vector, and then adding them all together <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Span of Vectors

The **span** of a given set of [[understanding_vectors | vectors]] is the set of all possible [[understanding_vectors | vectors]] that can be reached by a linear combination of those [[understanding_vectors | vectors]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. It asks what vectors can be reached using only [[understanding_vectors | vector addition]] and [[understanding_vectors | scalar multiplication]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

#### Span in Two Dimensions
When considering two [[understanding_vectors | vectors]] in two dimensions:
*   For most pairs of [[understanding_vectors | vectors]], their span is all [[understanding_vectors | vectors]] in two-dimensional space, meaning every point in the plane can be reached <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   If the two original [[understanding_vectors | vectors]] happen to line up (are collinear), the span is limited to a single line passing through the origin <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   If both vectors are zero, the span is just the origin <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

#### Span in Three Dimensions
When considering [[understanding_vectors | vectors]] in three dimensions:
*   The span of two non-collinear [[understanding_vectors | vectors]] in 3D space is a flat sheet (a plane) cutting through the origin <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This is the collection of all possible linear combinations of those two vectors <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   Adding a third vector to the combination:
    *   If the third vector is already within the span of the first two (i.e., it lies on the plane defined by the first two), the span does not change <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   If the third vector is not on the span of the first two, it "unlocks" access to every possible three-dimensional vector, meaning the span becomes all of 3D space <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

> [!INFO] Representing Collections of Vectors
> When dealing with collections of [[understanding_vectors | vectors]], it is common to represent each vector with just the point at its tip, assuming the vector's tail is at the origin <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Thus, a line can represent all vectors whose tips sit on that line <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>, and the entire infinite flat sheet of 2D space can represent all possible 2D vectors <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Linear Dependence and Independence

*   **Linearly Dependent**: A set of [[understanding_vectors | vectors]] is linearly dependent if one vector is redundant, meaning it can be removed without reducing the span of the set <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. This also means that one of the vectors can be expressed as a linear combination of the others <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
    *   Example: Two vectors in 2D that line up are linearly dependent <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
    *   Example: A third vector in 3D that sits on the span of the first two is linearly dependent with them <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Linearly Independent**: If each vector in a set genuinely adds another dimension to the span, they are said to be linearly independent <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### Technical Definition of a Basis

The technical definition of a [[coordinate_systems_and_basis_vectors | basis]] of a space is a set of **linearly independent [[understanding_vectors | vectors]] that span that space** <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.