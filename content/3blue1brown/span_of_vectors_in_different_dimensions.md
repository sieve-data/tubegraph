---
title: Span of vectors in different dimensions
videoId: k7RM-ot2NWY
---

From: [[3blue1brown]] <br/> 

When describing a vector numerically, such as `[3, -2]`, each coordinate can be thought of as a scalar that stretches or squishes a corresponding basis vector <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. In the standard xy-coordinate system, the two special basis vectors are:
*   **i-hat**: The unit vector pointing right (length 1) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **j-hat**: The unit vector pointing straight up (length 1) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

For instance, the vector `[3, -2]` represents the sum of i-hat scaled by 3, and j-hat scaled by -2 (flipping and stretching it) <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This concept of adding together two scaled vectors is fundamental <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Basis of a Coordinate System

The vectors i-hat and j-hat are collectively called the **basis of a coordinate system** <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. The basis vectors are what the coordinate scalars actually scale <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. It's possible to choose different basis vectors to create a new, valid coordinate system <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Any numerical description of vectors depends on an implicit choice of basis vectors <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Linear Combination

The process of scaling two or more vectors and then adding them together is called a **linear combination** of those vectors <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. If one scalar is fixed while the other changes freely, the tip of the resulting vector will trace a straight line <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Span of Vectors

The **span** of a set of vectors is the collection of all possible vectors that can be reached by forming a linear combination of those vectors <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. It represents all possible vectors one can reach using only [[understanding_vectors | vector addition]] and [[matrixvector_multiplication | scalar multiplication]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

When dealing with collections of vectors, it's often convenient to represent each vector simply by the point at its tip (assuming its tail is at the origin) <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Span of Two-Dimensional Vectors

For a pair of two-dimensional vectors:
*   **Most pairs**: If the two original vectors do not line up, their span will be every possible point in the plane, meaning all vectors in two-dimensional space <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Collinear pairs**: If the two original vectors happen to line up (are pointing in the same or opposite directions), the tip of the resulting vector will be limited to a single line passing through the origin <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Zero vectors**: If both vectors are zero, the span is just the origin <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Span of Three-Dimensional Vectors

The concept of span extends to [[basis_vectors_in_three_dimensions | vectors in three dimensions]]:
*   **Two vectors in 3D**: If two vectors in 3D space are not pointing in the same direction, their span is a flat sheet (a plane) cutting through the origin of three-dimensional space <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Three vectors in 3D**:
    *   If the third vector already sits on the span (the plane) of the first two, adding it to the linear combination does not expand the span <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. The span remains the same plane.
    *   If the third vector is not sitting on the span of the first two, it unlocks access to every possible three-dimensional vector. The span becomes all of three-dimensional space <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This can be visualized as the third vector sweeping the plane of the first two through all of space <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

## Linear Dependence and Independence

When considering multiple vectors and their span:
*   **Linearly Dependent**: A set of vectors is linearly dependent if you could remove one or more vectors without reducing the span <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This means at least one of the vectors is redundant or can be expressed as a linear combination of the others (i.e., it is already in the span of the others) <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Examples include two 2D vectors that line up, or a third 3D vector that lies on the plane spanned by the first two <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Linearly Independent**: If each vector genuinely adds another dimension to the span (i.e., cannot be formed by a linear combination of the others), the vectors are said to be linearly independent <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

## Basis: A Formal Definition

The technical definition of a basis of a space is a set of linearly independent vectors that span that space <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This definition aligns with the idea that basis vectors allow coordinates to represent any vector in the space without redundancy.