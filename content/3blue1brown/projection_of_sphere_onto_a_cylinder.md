---
title: Projection of sphere onto a cylinder
videoId: GNcFjFmqEc8
---

From: [[3blue1brown]] <br/> 

A fundamental concept in understanding the [[surface_area_of_a_sphere | surface area of a sphere]] involves its relationship to an enclosing cylinder. Specifically, the [[surface_area_of_a_sphere | surface area of a sphere]] is equivalent to the lateral [[surface_area_of_a_sphere | surface area]] of a cylinder that has the same radius and height as the sphere <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This cylinder is considered without its top and bottom, effectively its "label" <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Unwrapping the Cylinder

Once the cylinder's lateral [[surface_area_of_a_sphere | surface area]] is obtained, it can be [[unwrapping_cylinder_into_a_rectangle | unwrapped into a rectangle]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   The width of this rectangle corresponds to the cylinder's circumference, which is 2πR <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   The height of the rectangle comes from the sphere's height, which is 2R (two times the radius) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
Multiplying these dimensions (2πR * 2R) yields the formula 4πR² for the [[surface_area_of_a_sphere | surface area of a sphere]] <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## The Projection Principle

The core of this [[geometric_reasoning_and_sphere_surface_area | geometric reasoning]] lies in demonstrating why the [[surface_area_of_a_sphere | surface area]] of the sphere is identical to that of the cylinder's label <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This is achieved by approximating the sphere's [[surface_area_of_a_sphere | surface area]] with many tiny rectangles covering it <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

The key insight is that if these rectangles are projected directly outward onto the cylinder, as if casting a shadow by lights positioned along the z-axis and pointing parallel to the xy-plane, the projection of each rectangle onto the cylinder surprisingly retains the same area as the original rectangle on the sphere <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Compensating Effects

The preservation of area during projection is due to two counteracting effects <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>:
1.  **Width Scaling Up:** As a rectangle on the sphere is projected outward, its width (along latitude lines) gets scaled up <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Rectangles closer to the poles experience a greater scaling effect due to the longer projection distance, while those near the equator experience minimal change <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  **Height Scaling Down:** Because these rectangles are slanted with respect to the z-direction, their height (along longitude lines) gets scaled down during projection <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Rectangles near the poles are significantly slanted, leading to a substantial reduction in height, whereas those closer to the equator, being more parallel to the z-axis, experience less height reduction <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

Remarkably, these two effects—the stretching of the width and the squishing of the height—cancel each other out perfectly, resulting in the projected rectangle having the same area as the original <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This [[geometric_reasoning_and_sphere_surface_area | geometric reasoning]] is considered elegant <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Detailed Geometric Proof

To delve into *why* these effects cancel, consider a specific rectangle on the sphere with radius `r` <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Let `d` be the distance between this rectangle and the z-axis <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. For tiny rectangles, the ambiguity of `d` is negligible <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

1.  **Width Scaling:**
    *   To understand the width projection, two similar triangles are pictured <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
    *   The first triangle has its base on the sphere's rectangle and its tip on the z-axis at the same height, a distance `d` away <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   The second triangle is a scaled-up version that extends to the cylinder, meaning its long side now has length `R` (the sphere's radius) <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
    *   The ratio of their bases, which represents how much the rectangle's width is stretched, is `R` divided by `d` (R/d) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

2.  **Height Scaling:**
    *   Consider a cross-section of the sphere for a cleaner view <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
    *   A small right triangle is formed where the height of the spherical rectangle is the hypotenuse, and its projection is one of the legs <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
    *   A crucial geometric principle states that any line tangent to a circle is perpendicular to the radius drawn to that point of tangency <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
    *   Drawing the radial line and considering the distance `d` forms another right triangle <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   Through angle analysis (e.g., using angles alpha and beta and the 90-degree angle from the radius-tangent perpendicularity), it's revealed that this small triangle is similar to the larger triangle involving `R` and `d` <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   By similarity, the ratio of the projected height to the original height (hypotenuse to leg) is `d` divided by `R` (d/R) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### Cancellation of Effects

The width is scaled by `R/d` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>, and the height is scaled by `d/R` <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. When these are multiplied together (Area_projected = Width_original * (R/d) * Height_original * (d/R)), the `R/d` and `d/R` terms cancel out perfectly <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. This ensures that the projected area is equal to the original area.

### Visualizing the Transformation

As a side note, for this specific parameterization of the sphere, the projected rectangle appears as a 90-degree rotation of the original rectangle, due to the ratio of width to height starting as `d` to `r` <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This allows for a visualization where each rectangular piece is rotated 90 degrees and rearranged to form the cylinder's surface <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

### Connection to Calculus

This method, relying on approximating [[surface_area_of_a_sphere | surface area]] with increasingly tiny rectangles, is essentially a [[geometric_reasoning_and_sphere_surface_area | geometric reasoning]] approach to calculus, without using explicit jargon <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. As the approximation gets finer, the combined area of the sphere's rectangles approaches its true [[surface_area_of_a_sphere | surface area]], and similarly for the cylinder. Since the area of each corresponding rectangle is the same, the true [[surface_area_of_a_sphere | surface areas]] must also be equal <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This idea serves as a rigorous way to define area for smooth, curved surfaces <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

This proof, often attributed to [[archimedes_proof_of_sphere_surface_area | Archimedes]], is considered a "true gem of geometry" <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a> and demonstrates the elegant relationship between a sphere and its enclosing cylinder, leading to the well-known formula for the [[surface_area_of_a_sphere | surface area of a sphere]]. It also provides a [[surface_area_of_a_sphere_visual_proof | visual proof]] for [[comparing_sphere_surface_area_to_enclosing_cylinder | comparing sphere surface area to enclosing cylinder]].