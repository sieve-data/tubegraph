---
title: Archimedes proof of sphere surface area
videoId: EPDZTLavmcg
---

From: [[3blue1brown]] <br/> 

The [[surface_area_of_a_sphere | surface area of a sphere]] is given by the formula 4π times its radius squared <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This is exactly four times the area of a circle with the same radius <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Archimedes' Insight

Archimedes developed a remarkable [[surface_area_of_a_sphere_visual_proof | proof]] demonstrating that the [[surface_area_of_a_sphere | surface area of a sphere]] is equivalent to the lateral surface area of a cylinder that perfectly encloses it <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This comparison disregards the circular caps of the cylinder <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## The Projection Method

The core idea of Archimedes' [[geometric_reasoning_and_sphere_surface_area | geometric reasoning]] involves a [[projection_of_sphere_onto_a_cylinder | projection of the sphere onto the cylinder]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
Imagine shining light from the z-axis, perpendicular to that axis <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. If you compare the area of a small rectangular patch drawn on the sphere to the area of the shadow it casts on the enclosing cylinder, these two areas turn out to be identical <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This concept relates to the [[surface_area_of_a_sphere_versus_its_shadow | surface area of a sphere versus its shadow]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Geometric Cancellation

While it may not be immediately obvious, the shadow cast on the cylinder is a transformed version of the original small rectangle from the sphere <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. It is effectively squished down in one direction and stretched out in another <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. However, when the relevant [[geometric_reasoning_and_sphere_surface_area | geometry]] is analyzed, these two effects perfectly cancel each other out <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Summation and Inference

By treating the sphere as a sum of all its infinitesimally small patches, and the cylinder as a sum of all the corresponding shadows cast by those patches, it can be inferred that the total [[surface_area_of_a_sphere | surface area of the sphere]] is equal to the lateral surface area of the enclosing cylinder <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>, <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This aligns with [[general_principles_of_surface_area_for_convex_shapes | general principles of surface area for convex shapes]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Calculating the Cylinder's Area

The cylinder can be unwrapped into a rectangle <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   One side length of this rectangle corresponds to the circumference of the sphere, which is 2πr <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   The other side length corresponds to the height of the sphere, which is its diameter, or 2 times its radius (2r) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>, <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

Multiplying these two dimensions (2πr * 2r) yields the area of the cylinder's lateral surface: 4πr² <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This is the desired formula for the [[surface_area_of_a_sphere | surface area of a sphere]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

This proof provides a visual and intuitive understanding for [[comparing_sphere_surface_area_to_enclosing_cylinder | comparing sphere surface area to an enclosing cylinder]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
If one is familiar with the trick of showing a circle's area by unwrapping it into a triangle (height r, base 2πr), it becomes clear how four of these unwrapped circles would perfectly fit into the unwrapped cylinder shape <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.