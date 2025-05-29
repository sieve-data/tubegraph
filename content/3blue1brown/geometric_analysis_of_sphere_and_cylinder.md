---
title: Geometric analysis of sphere and cylinder
videoId: EPDZTLavmcg
---

From: [[3blue1brown]] <br/> 

The [[surface_area_of_a_sphere | surface area of a sphere]] is defined as 4π times its radius squared, which is exactly four times the area of a [[geometry_and_circles | circle]] with the same radius <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## [[Archimedes_proof_of_spheres_surface_area | Archimedes' Proof]] for Sphere Surface Area

[[Archimedes_proof_of_spheres_surface_area | Archimedes]] devised a method to show that the [[surface_area_of_a_sphere | surface area of a sphere]] is equivalent to the surface area of a cylinder that perfectly encloses it, specifically without considering the cylinder's circular caps <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This provides a clear [[comparing_sphere_surface_area_with_cylinder_surface_area | comparison between sphere and cylinder surface areas]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

### The Shadow Projection Concept

The core idea of [[Archimedes_proof_of_spheres_surface_area | Archimedes' proof]] involves projecting light from an axis (e.g., the z-axis) perpendicular to it <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. If a small rectangular patch on the sphere is compared to the shadow it casts on the enclosing cylinder, these two areas are surprisingly found to be identical <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

While not immediately apparent, the shadow cast is a transformed version of the original rectangle: it is squished in one direction and simultaneously stretched in another <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Through careful [[geometry_of_spheres_and_cylinders | geometric analysis]], these two counteracting effects cancel out perfectly <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

By conceptualizing the sphere as a sum of these small patches and the cylinder as a sum of their corresponding shadows, it can be inferred that the [[surface_area_of_a_sphere | surface area of the sphere]] matches the area of the enclosing cylinder (excluding its caps) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Deriving the Formula

To calculate the cylinder's lateral surface area, one can "unwrap" it into a rectangle <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   One side of this rectangle corresponds to the cylinder's circumference, which is 2πr <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   The other side corresponds to the height of the sphere, which is 2 times its radius (2r) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

Multiplying these dimensions yields the area: (2πr) * (2r) = 4πr² <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This confirms the [[surface_area_of_a_sphere | surface area of a sphere]] formula.

### Connection to Circle Area

A well-known method for demonstrating a [[geometry_and_circles | circle's area]] involves unwrapping it into a triangle <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This triangle has a height equal to the [[geometry_and_circles | circle's]] radius (r) and a base equal to its circumference (2πr) <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Its area is (1/2) * base * height = (1/2) * (2πr) * r = πr² <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

This visual demonstration of the [[connection_between_sphere_and_circle_area_formulas | circle's area formula]] provides a clear insight into why the [[surface_area_of_a_sphere | sphere's surface area]] is exactly four times the area of a [[geometry_and_circles | circle]] with the same radius: four of these unwrapped [[geometry_and_circles | circles]] fit perfectly into the unwrapped cylinder shape <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.