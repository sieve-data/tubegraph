---
title: Projection of spherical rectangles and area relationships
videoId: GNcFjFmqEc8
---

From: [[3blue1brown]] <br/> 

The [[surface_area_of_a_sphere | surface area of a sphere]] is commonly known as 4πR² <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This formula is "suspiciously suggestive" because it is a clean multiple of πR², the area of a circle with the same radius <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. While perfectly fitting four flat circles onto a sphere is impossible due to differences in curvature <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, there are satisfying ways to connect the sphere's surface area to these four circles <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

One classic method, a "true gem of [[geometry_of_spheres_and_cylinders | geometry]]" <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, involves comparing the sphere's surface to a cylinder. Another approach draws a direct line between the sphere and its shadow <a class="yt-timestamp" data-t="01:10:08">[01:10:08]</a>. This fourfold relationship is not unique to spheres but is a specific instance of a more general fact for all convex shapes in three dimensions <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.

## [[Archimedes proof of spheres surface area | Archimedes' Proof]]: Sphere to Cylinder
The first approach, attributed to [[Archimedes proof of spheres surface area | Archimedes]], demonstrates that the [[surface_area_of_a_sphere | surface area of a sphere]] is identical to the lateral surface area of a cylinder that shares the same radius and height as the sphere <a class="yt-timestamp" data-t="01:25:06">[01:25:06]</a>. This cylinder is considered without its top and bottom caps <a class="yt-timestamp" data-t="01:37:06">[01:37:06]</a>.

Once conceptually "unwrapped," the cylinder's lateral surface forms a rectangle <a class="yt-timestamp" data-t="01:43:08">[01:43:08]</a>.
*   The width of this rectangle corresponds to the cylinder's circumference: 2πR <a class="yt-timestamp" data-t="01:48:06">[01:48:06]</a>.
*   The height of the rectangle matches the height of the sphere (and cylinder): 2R <a class="yt-timestamp" data-t="01:52:06">[01:52:06]</a>.

Multiplying these dimensions (2πR * 2R) directly yields the [[surface_area_of_a_sphere | formula for the sphere's surface area]]: 4πR² <a class="yt-timestamp" data-t="02:00:06">[02:00:06]</a>.

### The Underlying Principle: Area Preservation by Projection
The core of this proof lies in approximating the sphere's surface with many tiny rectangles <a class="yt-timestamp" data-t="02:33:04">[02:33:04]</a>. The idea is that if these spherical rectangles are projected directly outward onto the surrounding cylinder, their area surprisingly remains the same <a class="yt-timestamp" data-t="02:39:06">[02:39:06]</a>.

This area preservation occurs despite two competing effects <a class="yt-timestamp" data-t="03:01:09">[03:01:09]</a>:
1.  **Width Scaling Up**: As a rectangle from the sphere is projected outward, its width is scaled up. This effect is more pronounced for rectangles closer to the poles <a class="yt-timestamp" data-t="03:12:09">[03:12:09]</a>.
2.  **Height Scaling Down**: Because the rectangles on the sphere are slanted with respect to the z-direction, their height gets scaled down during projection. Rectangles near the poles are highly slanted, leading to significant height reduction <a class="yt-timestamp" data-t="03:34:07">[03:34:07]</a>.

Crucially, these two effects—the stretching of the width and the squishing of the height—perfectly cancel each other out <a class="yt-timestamp" data-t="04:08:08">[04:08:08]</a>.

### [[Geometric analysis of sphere and cylinder | Geometric Analysis]] of the Projection
To understand why the effects cancel, consider a specific rectangle on the sphere with radius `r` and distance `d` from the z-axis <a class="yt-timestamp" data-t="04:43:04">[04:43:04]</a>.

#### Width Scaling
*   Imagine two similar triangles used to visualize the projection <a class="yt-timestamp" data-t="05:18:02">[05:18:02]</a>.
*   The first triangle has its base on the sphere's rectangle and its tip on the z-axis <a class="yt-timestamp" data-t="05:24:06">[05:24:06]</a>.
*   The second triangle is a scaled-up version that just reaches the cylinder, meaning its long side has length `R` (the sphere's radius) <a class="yt-timestamp" data-t="05:33:02">[05:33:02]</a>.
*   The ratio of their bases, which determines how much the rectangle's width is stretched, is `R / d` <a class="yt-timestamp" data-t="05:43:08">[05:43:08]</a>.

#### Height Scaling
*   Consider a cross-section of the sphere <a class="yt-timestamp" data-t="05:57:04">[05:57:04]</a>.
*   A small right triangle can be formed where the hypotenuse is the height of the spherical rectangle, and one leg is its projection onto the cylinder <a class="yt-timestamp" data-t="06:05:05">[06:05:05]</a>.
*   A key [[geometry_of_spheres_and_cylinders | geometric]] principle is that anything tangent to a circle is perpendicular to the radius drawn to that point <a class="yt-timestamp" data-t="06:17:09">[06:17:09]</a>.
*   Drawing a radial line and considering the distance `d` forms another right triangle <a class="yt-timestamp" data-t="06:33:08">[06:33:08]</a>.
*   These two triangles are similar <a class="yt-timestamp" data-t="06:51:03">[06:51:03]</a>. For instance, if one angle in the larger triangle is `alpha` and another is `beta`, then `alpha + beta + 90° = 180°` <a class="yt-timestamp" data-t="07:06:06">[07:06:06]</a>. Due to the perpendicularity of the tangent and radius, the angles in the smaller triangle also become `alpha`, `beta`, and `90°` <a class="yt-timestamp" data-t="07:27:01">[07:27:01]</a>.
*   By similarity, the ratio of the hypotenuse (original height) to the projected leg (scaled height) is `R / d` <a class="yt-timestamp" data-t="08:09:05">[08:09:05]</a>. This implies the height is scaled down by `d / R`.

Therefore, the effect of stretching the width by `R/d` is perfectly canceled out by the height being squished by `d/R` <a class="yt-timestamp" data-t="08:15:06">[08:15:06]</a>. This means the area of each small rectangle on the sphere is the same as its projection onto the cylinder <a class="yt-timestamp" data-t="09:35:01">[09:35:01]</a>. This reasoning, though without jargon, is essentially calculus, relying on the idea that approximations get closer to the true value for finer coverings <a class="yt-timestamp" data-t="09:23:09">[09:23:09]</a>.

## [[Connection between sphere and circle area formulas | Connecting to Four Circles]]
The [[connection_between_sphere_and_circle_area_formulas | connection between the sphere's surface area and four circles]] can be made visually by showing how the area of circles (πR²) can be "unwrapped" into triangles <a class="yt-timestamp" data-t="10:31:05">[10:31:05]</a>. This process involves relating thin concentric rings of the circle to horizontal slices of a triangle <a class="yt-timestamp" data-t="10:45:01">[10:45:01]</a>. Because the circumference of each ring increases linearly with its radius (2π times radius), when unwrapped and lined up, their ends form a straight line, creating a triangle with a base of 2πR and a height of R <a class="yt-timestamp" data-t="10:52:06">[10:52:06]</a>.

Four of these unwrapped circular triangles perfectly fit into the rectangle (2πR by 2R) that represents the unfolded cylinder label, which is also the sphere's surface <a class="yt-timestamp" data-t="11:13:06">[11:13:06]</a>.

## [[Mathematical proofs involving inscribed rectangles | Alternative Proof]]: Sphere to Shadow Circle
Another approach involves cutting the sphere into many thin rings parallel to the xy-plane and comparing the area of these rings to the area of their shadows on the xy-plane <a class="yt-timestamp" data-t="12:06:05">[12:06:05]</a>. The shadows of all rings from the northern hemisphere combine to form a circle with the same radius as the sphere <a class="yt-timestamp" data-t="12:18:05">[12:18:05]</a>.

The key insight is to show a correspondence between these ring shadows and "every second ring" on the sphere <a class="yt-timestamp" data-t="12:25:05">[12:25:05]</a>.

<div class="callout">
<div class="callout-title">Challenge Mode: Guided Exercises</div>

To understand this [[proofs_of_sphere_surface_area_and_triangle_properties | proof]], consider the following exercises:

1.  **Circumference and Ring Area**: For a ring at an angle `theta` (from the z-axis) with thickness `R * d-theta`, what is its circumference and approximate area? <a class="yt-timestamp" data-t="13:11:06">[13:11:06]</a>
2.  **Shadow Area**: What is the area of the shadow of one of these rings on the xy-plane, in terms of R, `theta`, and `d-theta`? <a class="yt-timestamp" data-t="13:48:07">[13:48:07]</a>
3.  **Area Relationship**: Each ring's shadow has precisely half the area of one of the rings on the sphere (though not necessarily the one directly above it). Which spherical ring corresponds to a given shadow in this relationship? (Hint: Use trigonometric identities) <a class="yt-timestamp" data-t="14:09:07">[14:09:07]</a>
4.  **Correspondence**: The shadows from the northern hemisphere form a circle of radius R. Using your answer from the previous question, explain the exact correspondence between these shadows and rings on the sphere. <a class="yt-timestamp" data-t="14:34:07">[14:34:07]</a>
5.  **Final Implication**: Why does this correspondence imply that the area of the circle is exactly one-fourth the [[surface_area_of_a_sphere | surface area of the sphere]], especially as the rings become infinitesimally thin? <a class="yt-timestamp" data-t="14:56:05">[14:56:05]</a>
</div>

## Generalization
The fourfold relationship between the [[surface_area_of_a_sphere | surface area of a sphere]] and the area of circles is a specific instance of a more general mathematical fact <a class="yt-timestamp" data-t="15:15:06">[15:15:06]</a>. For any convex shape, the average area of all its shadows, averaged over all possible orientations in 3D space, is exactly one-fourth the surface area of that shape <a class="yt-timestamp" data-t="15:24:06">[15:24:06]</a>.