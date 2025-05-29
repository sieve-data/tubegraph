---
title: Inverse Pythagorean theorem
videoId: d-o3eB9sfls
---

From: [[3blue1brown]] <br/> 

The Inverse Pythagorean theorem is a lesser-known but significant mathematical relation, often appearing in geometric contexts involving distances and inverse squares <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. It is described as a "cousin" of the more common [[Pythagorean theorem and triples]] <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

## Formula and Setup

In the context of light and observers, the theorem relates distances from an observer to a light source. Imagine an observer at the origin of an XY plane <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

Consider:
*   A single lighthouse at some point on the plane <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Let `H` be the distance from the observer to this original lighthouse <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   Draw a line from the lighthouse to the observer <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   Draw another line perpendicular to the first line, passing through the lighthouse <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   Place two new lighthouses, 'A' and 'B', where this perpendicular line intersects the coordinate axes <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   Let `a` be the distance from the observer to lighthouse A, and `b` be the distance from the observer to lighthouse B <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

The Inverse Pythagorean theorem states the relationship between these distances:
`1/a² + 1/b² = 1/H²` <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>

## Connection to Apparent Brightness

This theorem is particularly useful when considering the apparent brightness of light sources, which follows the [[Inverse square law and its applications]] <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. The apparent brightness of a light source is inversely proportional to the square of its distance from the observer <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

If all lighthouses emit the same power <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>:
*   Brightness from lighthouse A is proportional to `1/a²`.
*   Brightness from lighthouse B is proportional to `1/b²`.
*   Brightness from the original lighthouse (H) is proportional to `1/H²`.

The theorem then implies that the combined brightness experienced by the observer from lighthouses A and B together is equal to the brightness experienced from the original lighthouse (H) <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This allows for the transformation of a single lighthouse into two others without changing the total observed brightness <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

## Geometric Proof Using Light and Screens

A visually intuitive proof of the Inverse Pythagorean theorem involves concepts of light and screens <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>:

1.  **Miniature Right Triangle:** Imagine scaling down the right triangle formed by the observer and the lighthouses into a miniature version <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
2.  **Hypotenuse as a Screen:** Think of the miniature hypotenuse as a screen receiving light from the first lighthouse <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
3.  **Reshaping the Screen:** If this screen is reshaped to be the combination of the two legs of the miniature triangle, it still receives the same total amount of light <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. The rays hitting the legs are precisely the same as those hitting the hypotenuse <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
4.  **Angle of Rays:**
    *   The amount of light from the first lighthouse (H) that hits the left leg of the reshaped screen is exactly the same as the amount of light from lighthouse A that hits that same side <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. This is because the angle of the rays hitting that part of the screen is identical <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
    *   Symmetrically, the amount of light from the first lighthouse (H) hitting the bottom leg of the screen is the same as the amount of light hitting that portion from lighthouse B <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
5.  **Similar Triangles:** This equivalence in light received (or "limited angle of rays") is fundamentally due to the principle of similar triangles <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This principle applies in the limiting case of a very tiny screen <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

## Application in the Basel Problem

The Inverse Pythagorean theorem is a crucial building block in a geometric proof for the [[basel_problem | Basel problem]], which seeks to find the sum of the infinite series `1 + 1/4 + 1/9 + 1/16 + ...` (inverses of square numbers) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

In this proof, the theorem is repeatedly applied to transform lighthouses around increasingly larger circles:
1.  **Initial Setup:** An observer on the edge of a circular lake, with a single lighthouse directly opposite <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. The apparent brightness is calculated based on the distance (diameter) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
2.  **First Transformation:** The original lighthouse is replaced by two new ones on a larger circle, positioned such that the [[inverse_square_law_and_its_applications | Inverse Pythagorean theorem]] applies, preserving the total brightness <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. This relies on the geometric fact that a triangle formed by a circle's diameter and any point on its circumference will have a 90-degree angle at that point <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
3.  **Subsequent Transformations:** This process is iterated. Each lighthouse is transformed into two new ones on an even larger circle, maintaining the total apparent brightness <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. The lighthouses become evenly spaced around the circumference <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. This even spacing is confirmed by the [[inscribed_angle_theorem | Inscribed Angle Theorem]] <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

By repeating this transformation infinitely, the circular lake effectively flattens into an infinite horizontal line with evenly spaced lighthouses in both directions <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. The total apparent brightness, which remained constant at `pi²/4` throughout the process, represents the sum of the inverse squares of all odd integers (positive and negative) <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. This provides a geometric intuition for why pi emerges in the solution to the Basel problem <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.