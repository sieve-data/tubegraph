---
title: Linear combinations and their significance
videoId: k7RM-ot2NWY
---

From: [[3blue1brown]] <br/> 
[[Understanding linear algebra | Linear algebra]] often involves understanding how vectors can be combined and what spaces these combinations can reach. This concept, known as a **linear combination**, is fundamental to working with vectors and coordinate systems.

### What is a Linear Combination?
A linear combination of vectors involves scaling each vector by a numerical factor (a scalar) and then adding the results together <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. For example, for two vectors, you choose two different scalars, scale each vector by its respective scalar, and then add the scaled vectors <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This extends to any number of vectors <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Coordinates and Basis Vectors
The idea of [[Vector coordinates and scalar implications | vector coordinates]] is closely tied to linear combinations <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. When a pair of numbers describes a vector (e.g., 3, -2), each coordinate should be thought of as a scalar that stretches or squishes vectors <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

In the standard xy coordinate system, there are two special vectors:
*   **i-hat**: The unit vector pointing to the right (length 1) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **j-hat**: The unit vector pointing straight up (length 1) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

The x-coordinate of a vector scales i-hat, and the y-coordinate scales j-hat <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Thus, the vector these coordinates describe is the sum of two scaled vectors <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This concept of adding two scaled vectors is surprisingly important <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

These two vectors, i-hat and j-hat, are together called the **basis** of a coordinate system <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. When coordinates are viewed as scalars, the basis vectors are what those scalars actually scale <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

It's possible to choose different basis vectors to create a new coordinate system <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Any time vectors are described numerically, it depends on an implicit choice of basis vectors <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

### The Span of Vectors
The set of all possible vectors that can be reached with a linear combination of a given set of vectors is called their **span** <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The span essentially asks what vectors are reachable using only vector addition and scalar multiplication <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

#### Span in 2D Space
If you take two vectors in 2D space and let both their scaling scalars range freely, two outcomes are possible:
*   **Most pairs of 2D vectors**: Their span will be *all vectors of 2D space* (the entire plane) <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Vectors that line up**: If the two original vectors happen to point in the same direction, the tip of the resulting vector will be limited to a single line passing through the origin <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Their span is thus all vectors whose tips sit on that line <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Both vectors are zero**: If both vectors are zero, the span is just the origin <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

#### Span in 3D Space
The concept of span extends to three-dimensional space <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>:
*   **Two vectors in 3D (not lined up)**: Their span is a flat sheet (a plane) cutting through the origin of 3D space <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Three vectors in 3D**:
    *   If the third vector is already within the span of the first two (i.e., sitting on their plane), adding it to the linear combination does not change the span <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. The span remains that same flat sheet <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   If the third vector is not sitting on the span of the first two, it unlocks access to every possible three-dimensional vector <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. The span becomes all vectors of 3D space <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Visualizing Collections of Vectors
When dealing with collections of vectors, it is common to represent each vector simply by the point at its tip, assuming the vector's tail is at the origin <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This makes it easier to visualize spaces like lines or planes that represent the span of vectors <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### Linear Dependence and Independence
When working with multiple vectors, if you can remove one vector without reducing the span of the set, the vectors are said to be **linearly dependent** <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This means one of the vectors can be expressed as a linear combination of the others, as it's already in their span <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

Conversely, if each vector truly adds another dimension to the span, they are said to be **linearly independent** <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### Basis: A Technical Definition
The technical definition of a basis of a space is a set of [[Linear dependence and independence | linearly independent]] vectors that span that space <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This definition makes sense because:
*   **Span the space**: The basis vectors must be able to reach every point in the space through their linear combinations.
*   **Linearly independent**: There should be no redundant vectors; each basis vector must contribute uniquely to the span.