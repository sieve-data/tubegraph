---
title: Comparing sphere surface area with cylinder surface area
videoId: EPDZTLavmcg
---

From: [[3blue1brown]] <br/> 

The [[surface_area_of_a_sphere | surface area of a sphere]] is calculated as 4π times its radius squared, which is precisely four times the area of a circle with the same radius <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## [[archimedes_proof_of_spheres_surface_area | Archimedes' Proof]]

[[archimedes_proof_of_spheres_surface_area | Archimedes]] provided a proof demonstrating that the [[surface_area_of_a_sphere | surface area of a sphere]] is equivalent to the area of a cylinder that perfectly encloses the sphere, specifically excluding the cylinder's circular caps <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This concept is a fundamental aspect of [[geometry_of_spheres_and_cylinders | the geometry of spheres and cylinders]] and [[geometric_analysis_of_sphere_and_cylinder | geometric analysis of sphere and cylinder]].

### Method of Projection

The core idea behind this proof involves projecting light onto the sphere and observing the resulting shadow on the enclosing cylinder <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   If light is shone from the z-axis, perpendicular to that axis, and one compares a small rectangular area on the sphere to its shadow cast on the cylinder, these two areas are found to be identical <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   While not immediately apparent, the shadow is effectively a transformed copy of the original small rectangle, squished in one direction and stretched in another <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   Through [[geometric_analysis_of_sphere_and_cylinder | analysis of the relevant geometry]], these squishing and stretching effects perfectly cancel each other out <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This demonstrates the key principle in [[projection_of_spherical_rectangles_and_area_relationships | projection of spherical rectangles and area relationships]].

By considering the sphere as a collection of these tiny patches and the cylinder as a sum of their corresponding shadows, it can be inferred that the [[surface_area_of_a_sphere | surface area of the sphere]] equals the area of the enclosing cylinder (excluding its caps) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Calculating the Area

To find the area, the cylinder can be conceptually "unwrapped" into a rectangle <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   One side length of this rectangle corresponds to the cylinder's circumference, which is 2πr <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   The other side length corresponds to the height of the sphere, which is two times its radius (2r) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   Multiplying these dimensions (2πr * 2r) yields the desired area: 4πr² <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### [[connection_between_sphere_and_circle_area_formulas | Connection to Circle Area]]

This derivation also highlights a [[connection_between_sphere_and_circle_area_formulas | strong connection to the area of a circle]]. Just as a cylinder can be unwrapped into a rectangle, a circle's area can be shown by unwrapping it into a triangle <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This triangle has a height equal to the circle's radius (r) and a base equal to its circumference (2πr) <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Visually, four of these unwrapped circles fit perfectly into the unwrapped cylinder shape <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.