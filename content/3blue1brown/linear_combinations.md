---
title: linear combinations
videoId: k7RM-ot2NWY
---

From: [[3blue1brown]] <br/> 

A linear combination of vectors involves scaling two or more vectors and then adding them together <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This concept is fundamental to [[linear_algebra_foundations | linear algebra]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Components of a Linear Combination
*   **Scalars**: Each coordinate of a vector can be thought of as a scalar, which stretches or squishes vectors <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **Scaled Vectors**: For example, in a two-dimensional vector like (3, -2), the '3' scales the x-direction vector (i-hat), and the '-2' scales the y-direction vector (j-hat) <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Vector Sum**: The final vector described by these [[coordinate_systems_in_linear_algebra | coordinates]] is the sum of these two scaled vectors <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Basis Vectors and Coordinates
The standard `xy` [[coordinate_systems_in_linear_algebra | coordinate system]] utilizes two special vectors:
*   **i-hat**: The unit vector pointing right with length 1 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **j-hat**: The unit vector pointing straight up with length 1 <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

These two vectors, i-hat and j-hat, are together called the [[coordinate_systems_in_linear_algebra | basis]] of a [[coordinate_systems_in_linear_algebra | coordinate system]] <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. When [[coordinate_systems_in_linear_algebra | coordinates]] are viewed as scalars, the [[coordinate_systems_in_linear_algebra | basis]] vectors are what those scalars act upon <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. It's possible to choose different [[coordinate_systems_in_linear_algebra | basis]] vectors to form a new, equally valid [[coordinate_systems_in_linear_algebra | coordinate system]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Any numerical description of vectors relies on an implicit choice of [[coordinate_systems_in_linear_algebra | basis]] vectors <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## The Span of Vectors
The set of all possible vectors that can be reached with a linear combination of a given pair of vectors is called their **span** <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The span essentially answers what vectors can be created using only [[vector_addition_and_scalar_multiplication | vector addition and scalar multiplication]] with the given vectors <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Two-Dimensional Span
*   **Most pairs of 2D vectors**: The span is all vectors of 2D space <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>, meaning every possible point in the plane is reachable <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Vectors that line up**: If two vectors are aligned (pointing in the same or opposite directions), their span is limited to a single line passing through the origin <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. If both vectors are zero, the span is just the origin <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Three-Dimensional Span
*   **Two non-aligned vectors**: The span is a flat sheet (a plane) cutting through the origin of [[threedimensional_linear_transformations | three-dimensional space]] <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Three vectors**:
    *   If the third vector is already within the span (the plane) of the first two, the span remains the same flat sheet <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   If the third vector is not in the span of the first two, it "unlocks access" to every possible [[threedimensional_linear_transformations | three-dimensional vector]], effectively sweeping the plane through all of space <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

### Visualizing Span
When dealing with collections of vectors, it's often convenient to represent each vector as a point at its tip, assuming the vector's tail is at the origin <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. This allows for visualizing a line to represent all vectors whose tips sit on that line, or the infinite flat sheet of 2D space to represent all 2D vectors <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## [[linear_dependence_and_independence | Linear Dependence and Independence]]
These terms describe situations where vectors are redundant or contribute uniquely to the span:

*   **[[linear_dependence_and_independence | Linearly Dependent]]**: Multiple vectors are [[linear_dependence_and_independence | linearly dependent]] if one can be removed without reducing the span <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This means one vector can be expressed as a linear combination of the others, as it already sits within their span <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Examples include two vectors lining up in 2D space, or a third vector lying on the plane spanned by two others in 3D space <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **[[linear_dependence_and_independence | Linearly Independent]]**: Vectors are [[linear_dependence_and_independence | linearly independent]] if each vector truly adds a new dimension to the span <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

The technical definition of a [[coordinate_systems_in_linear_algebra | basis]] of a space is a set of [[linear_dependence_and_independence | linearly independent]] vectors that span that space <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.