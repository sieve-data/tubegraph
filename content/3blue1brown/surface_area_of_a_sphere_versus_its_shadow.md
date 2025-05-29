---
title: Surface area of a sphere versus its shadow
videoId: GNcFjFmqEc8
---

From: [[3blue1brown]] <br/> 

The formula for the [[surface_area_of_a_sphere | surface area of a sphere]] is commonly known as 4πR², a multiple of the area of a circle with the same radius (πR²) <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While the formula is familiar, understanding *why* it is true can be explored through different geometric approaches <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. A simple fitting of four circles onto a sphere's surface is not possible due to differences in curvature <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Nevertheless, there are two distinct ways to conceptualize this [[surface_area_of_a_sphere | surface area]] in relation to circles <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## [[Archimedes proof of sphere surface area | Sphere Surface Area Through an Enclosing Cylinder]]

One classic approach, sometimes referred to as [[archimedes_proof_of_sphere_surface_area | Archimedes' proof]], demonstrates that the [[surface_area_of_a_sphere | surface area of a sphere]] is identical to the lateral [[surface_area_of_a_sphere | surface area]] of a cylinder that encloses it <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This cylinder has the same radius (R) and height (2R) as the sphere, excluding its top and bottom caps <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

When this "label" of the cylinder is unwrapped, it forms a rectangle <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The width of this rectangle is the cylinder's circumference (2πR), and its height is the sphere's height (2R) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Multiplying these dimensions gives the formula: 2πR * 2R = 4πR² <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### The Projection Principle

The core of this [[comparing_sphere_surface_area_to_enclosing_cylinder | cylinder comparison]] lies in the idea that if a sphere's surface is approximated by many tiny rectangles, projecting these rectangles directly outward onto the enclosing cylinder (as if casting a [[projection_of_sphere_onto_a_cylinder | shadow]] from lights parallel to the xy-plane) results in cylinder rectangles that have the same area as the original sphere rectangles <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

This equivalence is due to two counteracting effects <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>:
1.  **Width Scaling**: As a rectangle on the sphere is projected outward, its width is scaled up <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Rectangles closer to the poles experience a greater scaling effect than those near the equator <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. The scaling factor for the width is R/d, where R is the sphere's radius and d is the distance of the rectangle from the z-axis <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
2.  **Height Compression**: Because the rectangles on the sphere are slanted relative to the z-direction, their height is scaled down during the [[mathematical_concepts_of_shadows_and_projections | projection]] <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Rectangles near the poles, being more slanted, have their heights compressed more significantly <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The scaling factor for the height is d/R <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

These two effects, stretching the width and squishing the height, perfectly cancel each other out, meaning the area of the projected rectangle on the cylinder is equal to the area of the original rectangle on the sphere <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This holds true for increasingly smaller rectangles, leading to the conclusion that the total [[surface_area_of_a_sphere | surface area of the sphere]] equals the area of the cylinder's label <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. This [[geometric_reasoning_and_sphere_surface_area | geometric reasoning]], employing approximations that become precise in the limit, is foundational to calculus concepts <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

### Visualizing Four Circles

The connection to four circles comes from realizing that the area of each circle (πR²) can be "unwrapped" into a triangle with a base of 2πR and a height of R <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. This concept is explored in detail in the [[surface_area_of_a_sphere_visual_proof | visual proof of sphere surface area]] video <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. Four such triangles fit perfectly into the 2πR by 2R rectangle that represents the unwrapped cylindrical surface, thus visually confirming the 4πR² formula <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

## [[Mathematical concepts of shadows and projections | Sphere Surface Area Through its Shadow]]

A second line of reasoning directly relates the [[surface_area_of_a_sphere | sphere's surface area]] to its [[mathematical_concepts_of_shadows_and_projections | shadow]]. This approach involves cutting the sphere into many thin rings parallel to the xy-plane and comparing the area of these rings to the area of their [[mathematical_concepts_of_shadows_and_projections | shadows]] on the xy-plane <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. The collective [[mathematical_concepts_of_shadows_and_projections | shadows]] of all rings from one hemisphere form a circle with the same radius as the sphere <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

The core idea is to establish a correspondence between these ring [[mathematical_concepts_of_shadows_and_projections | shadows]] and "every second ring" on the sphere <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Rings are labeled by an angle (θ) from the z-axis (ranging from 0 at the north pole to π radians at the south pole), with a thickness of R * dθ <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

To understand this correspondence, a series of guided questions can be posed:

> [!NOTE] Structured Exercises (from the video)
> 1.  What is the circumference of one of these rings (e.g., at its inner edge) in terms of R and θ? Multiply this by the thickness (R * dθ) to approximate the ring's area <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
> 2.  What is the area of the [[mathematical_concepts_of_shadows_and_projections | shadow]] of one of these rings on the xy-plane, expressed in terms of R, θ, and dθ? <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>
> 3.  Each ring's [[mathematical_concepts_of_shadows_and_projections | shadow]] has precisely half the area of *another* ring on the sphere. Which ring is it? (Hint: consider trigonometric identities) <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>
> 4.  The [[mathematical_concepts_of_shadows_and_projections | shadows]] from the northern hemisphere form a circle of radius R. Based on your answer to the previous question, describe the exact correspondence between these [[mathematical_concepts_of_shadows_and_projections | shadow]] rings and the rings on the sphere <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.
> 5.  How does this imply that the area of the circle (πR²) is exactly one-fourth the [[surface_area_of_a_sphere | surface area of the sphere]], especially as the rings become thinner and thinner? <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>

## [[General principles of surface area for convex shapes | General Principle for Convex Shapes]]

The fourfold relationship seen with the [[surface_area_of_a_sphere | sphere's surface area]] is not unique to spheres. It is a specific instance of a more [[general_principles_of_surface_area_for_convex_shapes | general fact]] applicable to all convex shapes in three dimensions <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. If one takes any [[general_principles_of_surface_area_for_convex_shapes | convex shape]] and calculates the [[average_shadow_area_of_geometric_figures | average area of all its shadows]], averaged over all possible orientations in 3D space, that average will be exactly one-fourth the [[general_principles_of_surface_area_for_convex_shapes | surface area of the shape]] <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.