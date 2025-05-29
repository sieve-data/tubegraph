---
title: Geometric reasoning and sphere surface area
videoId: GNcFjFmqEc8
---

From: [[3blue1brown]] <br/> 

The [[surface_area_of_a_sphere | surface area of a sphere]] is famously given by the formula 4πR², which is four times the area of a circle with the same radius (πR²) <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While the formula itself can be proven, the goal is to develop a visceral connection to why this four-fold relationship exists <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This presents a challenge because a sphere's curvature differs from a flat plane, making it impossible to perfectly flatten its surface <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

This article explores two geometric lines of reasoning to understand this relationship:

1.  A classic geometric argument often attributed to [[Archimedes proof of sphere surface area | Archimedes]], comparing the sphere's [[surface_area_of_a_sphere | surface area]] to an enclosing cylinder <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
2.  A more direct approach relating the sphere to its [[Surface area of a sphere versus its shadow | shadow]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Finally, it touches upon a more general principle for all convex shapes <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Sphere and Cylinder Comparison

A fundamental insight is that the [[surface_area_of_a_sphere | surface area of a sphere]] is identical to the lateral [[surface_area_of_a_sphere | surface area]] of a cylinder that encloses it, having the same radius and a height equal to the sphere's diameter <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

The lateral surface of such a cylinder, when unwrapped, forms a rectangle. Its width is the cylinder's circumference (2πR), and its height is the sphere's diameter (2R) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Multiplying these dimensions yields the formula: 2πR × 2R = 4πR² <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Visualizing Four Circles

To see how four circles with radius R fit into this, one can [[surface_area_of_a_sphere_visual_proof | unwrap each circle into a triangle]] without changing its area <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This transformation works by relating thin concentric rings of the circle to horizontal slices of a triangle. The circumference of each ring, 2π times its radius, increases linearly, allowing them to form a straight line when unwrapped and stacked <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. This creates a triangle with a base of 2πR and a height of R <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. Four such triangles fit perfectly into the 2πR by 2R rectangle formed by the unwrapped cylinder <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

### The Underlying Geometric Proof: Projection Method

The core of the [[Archimedes proof of sphere surface area | Archimedes proof]] lies in demonstrating why the sphere's area equals the cylinder's lateral area. This is achieved by approximating the sphere's [[surface_area_of_a_sphere | surface area]] with many tiny rectangles <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. The key insight is that if these rectangles are projected directly outward onto the enclosing cylinder (as if casting a shadow by lights positioned along the z-axis) <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>, the projected rectangle on the cylinder surprisingly maintains the same area as the original rectangle on the sphere <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

Two competing effects are at play during this [[projection_of_sphere_onto_a_cylinder | projection]]:
*   **Width Stretching:** The width of the rectangle (along latitude lines) gets scaled up as it projects outward. This effect is more pronounced closer to the poles <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. The scaling factor for the width is R/d, where R is the sphere's radius and d is the distance from the z-axis to the rectangle <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   **Height Squishing:** Because the rectangles on the sphere are slanted relative to the z-direction, their height (along longitude lines) gets scaled down during projection. This squishing effect is greater closer to the poles, where the slant is more extreme <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

Remarkably, these two effects *perfectly cancel each other out* <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
To demonstrate this cancellation, consider a cross-section of the sphere and a tiny rectangle. The height of the sphere's rectangle is the hypotenuse of a small right triangle, and its projection onto the cylinder is one of the legs <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. By drawing a radius to the point of tangency (which is perpendicular to the tangent plane), another right triangle is formed <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. These two right triangles are similar <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. The ratio by which the height is scaled down is also R/d <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

Since the width is scaled up by R/d and the height is scaled down by d/R (the reciprocal of the width scaling), their product (representing the area) remains unchanged: (width * R/d) * (height * d/R) = width * height <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

This argument holds true for infinitesimally small rectangles, meaning that as the approximation gets finer, the total [[surface_area_of_a_sphere | surface area]] of the sphere is indeed equal to that of the cylinder <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. This method exemplifies [[converting_analytic_reasoning_to_geometric_intuition | geometric reasoning]] that leads to calculus concepts without formal jargon <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

## Sphere and Its Shadow

Another approach directly connects the sphere to its [[Surface area of a sphere versus its shadow | shadow]] on a flat plane. This method involves slicing the sphere into many thin rings parallel to the xy-plane <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. The shadows of all rings from one hemisphere combine to form a circle with the same radius as the sphere <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

By labeling each ring by its angle theta from the z-axis (ranging from 0 at the north pole to π at the south pole) and its thickness d-theta, the area of a ring can be approximated <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

Through a series of guided exercises, one can demonstrate:
*   The circumference of a ring at angle theta is 2πR sin(theta) <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   The area of the ring is approximately 2πR sin(theta) * R d-theta <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   The area of the shadow of one of these rings on the xy-plane is 2πR cos(theta) * R d-theta, which is precisely half the area of a specific ring on the sphere <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

This leads to the conclusion that the area of the circle (formed by the shadows of one hemisphere) is exactly one-fourth the [[surface_area_of_a_sphere | surface area]] of the sphere <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

## Generalization to Convex Shapes

The four-fold relationship between the [[surface_area_of_a_sphere | surface area]] and its shadows is not unique to spheres <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. For any convex shape in three dimensions, the average area of all its shadows, averaged over all possible orientations, is exactly one-fourth the total [[surface_area_of_a_sphere | surface area]] of the shape <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>. This principle showcases deeper connections in [[geometric_reasoning_in_higher_dimensions | geometric reasoning in higher dimensions]] and [[understanding_higher_dimensional_spheres_and_shapes | understanding higher dimensional spheres and shapes]].