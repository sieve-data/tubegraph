---
title: coordinate systems in linear algebra
videoId: k7RM-ot2NWY
---

From: [[3blue1brown]] <br/> 

In [[linear_algebra_foundations | linear algebra]], [[coordinate_systems_and_basis_vectors | vector coordinates]] provide a fundamental way to describe [[understanding_vectors_in_linear_algebra | vectors]] numerically, creating a bridge between pairs of numbers (or tuples) and multi-dimensional [[understanding_vectors_in_linear_algebra | vectors]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. A deeper understanding of these [[coordinate_systems_and_basis_vectors | coordinates]] is central to the field <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Coordinates as Scalars

When a pair of numbers, like (3, -2), describes a [[understanding_vectors_in_linear_algebra | vector]], each coordinate should be thought of as a scalar <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. These scalars indicate how much to stretch or squish other [[understanding_vectors_in_linear_algebra | vectors]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

In the standard XY [[coordinate_systems_and_basis_vectors | coordinate system]], there are two special [[coordinate_systems_and_basis_vectors | vectors]]:
*   **i-hat**: The unit [[understanding_vectors_in_linear_algebra | vector]] pointing right along the x-axis <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **j-hat**: The unit [[understanding_vectors_in_linear_algebra | vector]] pointing straight up along the y-axis <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

The x-coordinate of a [[understanding_vectors_in_linear_algebra | vector]] scales i-hat, and the y-coordinate scales j-hat <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The described [[understanding_vectors_in_linear_algebra | vector]] is the sum of these two scaled [[understanding_vectors_in_linear_algebra | vectors]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Basis of a Coordinate System

The [[coordinate_systems_and_basis_vectors | vectors]] i-hat and j-hat are collectively called the **basis of a [[coordinate_systems_and_basis_vectors | coordinate system]]** <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This means that when [[coordinate_systems_and_basis_vectors | coordinates]] are viewed as scalars, the [[coordinate_systems_and_basis_vectors | basis vectors]] are what these scalars actually scale <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Importance of [[importance_of_understanding_alternate_coordinate_systems | Alternate Coordinate Systems]]

It's possible to choose different [[coordinate_systems_and_basis_vectors | basis vectors]] to create a new, valid [[coordinate_systems_and_basis_vectors | coordinate system]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. For example, two non-aligned [[understanding_vectors_in_linear_algebra | vectors]] can serve as new [[coordinate_systems_and_basis_vectors | basis vectors]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. By scaling these new [[coordinate_systems_and_basis_vectors | basis vectors]] and adding them, any two-dimensional [[understanding_vectors_in_linear_algebra | vector]] can be reached <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

This highlights a crucial point: whenever [[understanding_vectors_in_linear_algebra | vectors]] are described numerically, it relies on an implicit choice of what [[coordinate_systems_and_basis_vectors | basis vectors]] are being used <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## Linear Combination

The process of scaling two or more [[understanding_vectors_in_linear_algebra | vectors]] and adding them together is called a **linear combination** <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. One way to conceptualize the "linear" aspect is that if one scalar is fixed and the other varies, the tip of the resulting [[understanding_vectors_in_linear_algebra | vector]] traces a straight line <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Span of Vectors

The **span** of a given pair of [[understanding_vectors_in_linear_algebra | vectors]] is the set of all possible [[understanding_vectors_in_linear_algebra | vectors]] that can be reached by a linear combination of those [[understanding_vectors_in_linear_algebra | vectors]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. Essentially, it asks what [[understanding_vectors_in_linear_algebra | vectors]] can be reached using only [[understanding_vectors_in_linear_algebra | vector]] addition and scalar multiplication <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

*   **In 2D Space**:
    *   For most pairs of two-dimensional [[understanding_vectors_in_linear_algebra | vectors]], their span is all [[understanding_vectors_in_linear_algebra | vectors]] of 2D space (the entire plane) <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
    *   If the two original [[understanding_vectors_in_linear_algebra | vectors]] are aligned (point in the same or opposite direction), their span is limited to a single line passing through the origin <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
    *   If both [[understanding_vectors_in_linear_algebra | vectors]] are zero, the span is just the origin <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

*   **In 3D Space**:
    *   If two [[understanding_vectors_in_linear_algebra | vectors]] in 3D space are not pointing in the same direction, their span is a flat sheet (a plane) cutting through the origin <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
    *   Adding a third [[understanding_vectors_in_linear_algebra | vector]]:
        *   If the third [[understanding_vectors_in_linear_algebra | vector]] is already on the span of the first two, the span does not change <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
        *   If the third [[understanding_vectors_in_linear_algebra | vector]] is not on the span of the first two, it unlocks access to every possible three-dimensional [[understanding_vectors_in_linear_algebra | vector]], sweeping the plane through all of space <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

### Visualizing Collections of Vectors

When dealing with collections of [[understanding_vectors_in_linear_algebra | vectors]], it's common to represent each one with just a point in space, specifically the point at the tip of the [[understanding_vectors_in_linear_algebra | vector]] when its tail is at the origin <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This simplifies visualization:
*   A collection of [[understanding_vectors_in_linear_algebra | vectors]] sitting on a line can be thought of as the line itself <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   All two-dimensional [[understanding_vectors_in_linear_algebra | vectors]] can be conceptualized as the infinite flat sheet of two-dimensional space <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## Linear Dependence and Independence

This terminology describes whether [[understanding_vectors_in_linear_algebra | vectors]] add new dimensions to a span:
*   **Linearly Dependent**: A set of multiple [[understanding_vectors_in_linear_algebra | vectors]] where at least one [[understanding_vectors_in_linear_algebra | vector]] is redundant, meaning its removal does not reduce the span <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. This implies one [[understanding_vectors_in_linear_algebra | vector]] can be expressed as a linear combination of the others <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Linearly Independent**: A set of [[understanding_vectors_in_linear_algebra | vectors]] where each [[understanding_vectors_in_linear_algebra | vector]] genuinely adds another dimension to the span <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

The technical definition of a [[coordinate_systems_and_basis_vectors | basis]] of a space is a set of linearly independent [[understanding_vectors_in_linear_algebra | vectors]] that span that space <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.