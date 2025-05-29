---
title: Geometric analysis of light projection
videoId: EPDZTLavmcg
---

From: [[3blue1brown]] <br/> 

The surface area of a sphere is calculated as 4π times its radius squared <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, which is exactly four times the area of a circle with the same radius <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Archimedes' Proof for Sphere Surface Area

[[Geometric reasoning and sphere surface area | Archimedes]] devised a notable proof demonstrating that the surface area of a sphere is identical to the area of a cylinder that perfectly encloses it, specifically excluding the cylinder's circular caps <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

### The Light Projection Method

The core idea of this proof involves a [[mathematical_concepts_of_shadows_and_projections | light projection]] experiment:
*   Imagine shining light from the z-axis, directed perpendicular to that axis <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   Compare the area of a small rectangle drawn on the sphere's surface to the area of the [[mathematical_concepts_of_shadows_and_projections | shadow]] it casts on the enclosing cylinder <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   Surprisingly, these two areas are identical <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Geometric Compensation

While not immediately obvious, the [[mathematical_concepts_of_shadows_and_projections | shadow]] cast on the cylinder is a transformed copy of the original small rectangle from the sphere <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. It is simultaneously squished in one direction and stretched out in another <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. A detailed analysis of the relevant [[Geometric reasoning and sphere surface area | geometry]] reveals that these two opposing effects perfectly cancel each other out <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

### Inference of Equal Areas

By treating the sphere as an aggregate of these numerous small patches and the cylinder as a sum of their corresponding [[mathematical_concepts_of_shadows_and_projections | shadows]] due to the [[projection_of_sphere_onto_a_cylinder | projection onto a cylinder]], one can logically deduce that the surface area of the sphere is precisely the same as the area of the cylindrical surface <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Calculating the Cylinder's Area

A cylinder's surface can be unwrapped into a flat rectangle <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   One side length of this rectangle corresponds to the cylinder's circumference, which is 2π times the radius ($2\pi r$) <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   The other side length corresponds to the height of the sphere, which is 2 times its radius ($2r$) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

Multiplying these dimensions ($2\pi r \times 2r$) yields the cylinder's area: $4\pi r^2$ <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This confirms the formula for the sphere's surface area.

## Relation to Circle Area

A circle's area can be visualized by unwrapping it into a triangle <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This triangle has a height equal to the circle's radius ($r$) and a base equal to its circumference ($2\pi r$) <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
This geometric insight reveals that four such unwrapped circles fit perfectly into the unwrapped rectangular shape of the cylinder <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.