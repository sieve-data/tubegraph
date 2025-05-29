---
title: Finding intersections of tangents
videoId: piJkuavhV50
---

From: [[3blue1brown]] <br/> 

This puzzle, also known as Monge's Theorem, explores the unexpected collinearity of intersection points derived from the [[tangent_lines_and_their_slopes_on_curves | external tangents]] of three circles <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## The Puzzle Setup
Consider three distinct circles in a two-dimensional plane <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. For each pair of circles, draw their two external tangents <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. These external tangents will intersect at a single point <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. Doing this for all three pairs of circles yields three such intersection points <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

The puzzle asks: What is special about these three intersection points? <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>

> [!INFO] Claim
> No matter where the three circles are positioned (assuming no two circles have the same size and no circle is inside another, initially), the three intersection points of their external tangents always fall on the same line <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a> <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a> <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

## Initial 3D Approach (Flawed)
The common approach to solving this 2D geometry problem involves stepping into the third dimension <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a> <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>:

1.  **Represent circles as spheres**: Imagine each 2D circle as the equator of a 3D sphere <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a> <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
2.  **External tangents in 3D**: For any pair of spheres, there is a cone of external tangents that all intersect at a single point <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a> <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>. This point is the 3D analogue of the 2D intersection point <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
3.  **The shared plane**: Consider a plane that rests on top of all three spheres <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
4.  **Connecting points**: If you draw a line between the tangency point of this plane on one sphere and the tangency point on another sphere, this line is one of the external tangents and passes through the relevant intersection point <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a> <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a> <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
5.  **Three points on the plane**: Since the three tangency points lie on this resting plane, and the lines connecting them pass through the three intersection points, the resting plane itself must pass through all three intersection points <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a> <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
6.  **Intersection of planes**: These three intersection points also lie on the original 2D plane where the circles reside <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a> <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. Any two non-parallel planes in 3D space intersect along a line <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a> <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
7.  **Conclusion**: Therefore, the three points must lie on the intersection line formed by these two planes <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a> <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

### The Flaw
This argument is not fully general <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. If one of the spheres is significantly smaller than the other two and positioned between them, it's impossible for a single plane to rest on top of all three <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a> <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a> <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a> <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

## Corrected 3D Approach
To save the proof and maintain the higher-dimensional insight, the key is to use cones instead of spheres <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a> <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a> <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

1.  **Cones with similar angles**: Each circle forms the base of a cone <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. The crucial condition is that all three cones must have the same angle at their tips, making them similar shapes <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a> <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a> <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
2.  **Center of Similarity**: The line passing through the tips of any two of these cones also passes through the intersection point of the external tangents of their base circles <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a> <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. This intersection point is the "center of similarity" for the two circles <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a> <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
    *   If you scale one circle about this point, it will coincide with the other <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
    *   The diagram of a smaller circle with its external tangents intersecting at that point is a scaled-down version of the larger circle's diagram <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a> <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
3.  **Plane through cone tips**: There exists a plane that passes through the tips of all three cones <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a> <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. Any three points in space define a unique plane <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>. This resolves the generality issue of the previous proof <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a> <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
4.  **Intersection with the base plane**: This plane, defined by the cone tips, intersects with the original 2D (xy) plane (where the circles lie) <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a> <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>. The line of intersection between these two planes is precisely the line that contains the three centers of similarity (the intersection points of the external tangents) <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a> <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

## Generalizations
This concept extends beyond just circles:
*   **Circles inside each other**: The concept of a "center of similarity" still applies even if one circle is entirely inside another, making the claim valid in more cases than just non-intersecting circles <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a> <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a> <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
*   **Any similar shapes**: The theorem can be generalized to any three similar shapes, provided they are all in the same orientation <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a> <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a> <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. The argument would use pyramid-like shapes instead of cones <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a> <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.