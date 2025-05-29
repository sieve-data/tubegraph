---
title: Symmetry and scaling in dot products
videoId: LyGKycYT2v0
---

From: [[3blue1brown]] <br/> 

The dot product is typically introduced early in [[linear_transformations_in_linear_algebra | linear algebra]] courses <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. While a basic understanding of vectors is sufficient for its initial introduction, a fuller understanding requires the context of [[linear_transformations_in_linear_algebra | linear transformations]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

Numerically, the dot product of two vectors of the same dimension involves pairing up coordinates, multiplying those pairs, and adding the results <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For example, the dot product of `(1, 2)` and `(3, 4)` is `(1 * 3) + (2 * 4)` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Geometric Interpretation and Symmetry

The numerical computation of the dot product has a [[geometric_interpretation_of_dot_products | geometric interpretation]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. For two vectors `v` and `w`, one way to think about their dot product (`v` dot `w`) is to:
1.  Project `w` onto the line passing through the origin and the tip of `v` <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
2.  Multiply the length of this projection by the length of `v` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

If the projection of `w` points in the opposite direction from `v`, the dot product will be negative <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   Vectors pointing in generally the same direction have a positive dot product <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Perpendicular vectors have a dot product of zero, as the projection of one onto the other is the zero vector <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   Vectors pointing in generally opposite directions have a negative dot product <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Order Does Not Matter
This geometric interpretation appears asymmetric, treating the two vectors differently <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. However, the order of the vectors in a dot product does not matter <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Projecting `v` onto `w` and multiplying by the length of `w` yields the same result as the reverse <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

This symmetry can be understood by considering vectors of equal length <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. If `v` and `w` have the same length, projecting `w` onto `v` (and multiplying by `v`'s length) is a mirror image of projecting `v` onto `w` (and multiplying by `w`'s length) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Effect of Scaling

Scaling one of the vectors, such as `v` by a constant like 2, breaks the geometric symmetry <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. However, the effect on the dot product value remains consistent across interpretations:
*   **Projecting `w` onto `v`**: If `v` is scaled by 2 (e.g., `2v`), the length of `w`'s projection onto `v` does not change, but the length of `v` (the vector being projected onto) doubles <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This causes the dot product (`2v` dot `w`) to be exactly twice `v` dot `w` <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Projecting `v` onto `w`**: If `v` is scaled by 2, the length of `v`'s projection onto `w` also scales by 2, while the length of `w` (the vector being projected onto) remains constant <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. The overall effect is still to double the dot product <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

Even though the visual symmetry is broken, the quantitative effect of scaling on the dot product value is the same under both [[geometric_interpretation_of_dot_products | interpretations]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

This consistency is rooted in the concept of [[duality_in_mathematical_transformations | duality]], particularly between vectors and [[linear_transformations_in_linear_algebra | linear transformations]] that map multiple dimensions to one dimension (the number line) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Any such linear transformation can be described by a matrix, and applying this transformation is computationally identical to taking a dot product with a corresponding vector <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

### Non-Unit Vectors
The dot product with a unit vector (`u-hat`) can be interpreted as projecting another vector onto the span of `u-hat` and taking the length <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. For non-unit vectors, scaling the unit vector (e.g., by a factor of 3) numerically scales each of its components by that factor <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. This means the associated matrix for the transformation also scales, projecting any vector and multiplying the result by the scaling factor <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

Therefore, the dot product with a non-unit vector is interpreted as first projecting onto that vector, then scaling the length of that projection by the length of the non-unit vector itself <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

The dot product is a useful [[geometric_interpretation_of_dot_products | geometric tool]] for understanding projections and comparing vector directions <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. At a deeper level, it connects vectors to the world of [[linear_transformations_in_linear_algebra | linear transformations]], revealing that a vector can be seen as a conceptual shorthand for a specific transformation <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Another example of this [[duality_in_mathematical_transformations | duality]] can be seen with the [[introduction_to_cross_products | cross product]] <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.