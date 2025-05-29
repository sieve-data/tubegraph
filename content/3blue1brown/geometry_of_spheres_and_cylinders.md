---
title: Geometry of spheres and cylinders
videoId: GNcFjFmqEc8
---

From: [[3blue1brown]] <br/> 

The surface area of a [[Highdimensional spheres | sphere]] is given by the formula `4πR²` <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This formula is notable because it is a direct multiple of `πR²`, which is the [[Geometry and circles | area of a circle]] with the same radius <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. While it's impossible to perfectly fit four flat circles onto the curved surface of a sphere due to differences in curvature, there are conceptual approaches that demonstrate a deep [[Connection between sphere and circle area formulas | connection between the sphere's surface area and these four circles]] <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

Two primary ways to understand this relationship are:
1.  By comparing the sphere's surface area to that of a [[Geometric analysis of sphere and cylinder | cylinder]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  By relating the sphere's surface area to the area of its shadow <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### [[Geometric analysis of sphere and cylinder | Comparing Sphere Surface Area with Cylinder Surface Area]]

A classic geometric insight, often attributed to [[Archimedes proof of spheres surface area | Archimedes]], reveals that the surface area of a sphere is equal to the lateral surface area of a cylinder that has the same radius and a height equal to the sphere's diameter (2R) <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

To visualize this, imagine "unwrapping" the cylinder's lateral surface into a flat rectangle <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   The width of this rectangle is the cylinder's circumference, which is `2πR` <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   The height of the rectangle is the cylinder's height, which is `2R` (the sphere's diameter) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   Multiplying these dimensions (`2πR * 2R`) yields `4πR²`, thus deriving the sphere's surface area formula <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

#### Connecting to Four Circles

This `4πR²` area can be visually connected to four circles of radius R. Each circle has an area of `πR²`. One method to fit these circles into the cylinder's unfolded label involves unwrapping each circle into a triangle <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

To unwrap a circle into a triangle without changing its area:
*   Imagine the circle made of thin concentric rings <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
*   The circumference of each ring is `2π * radius` <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   If these rings are straightened and lined up from smallest to largest, their ends form a straight line, creating a triangle <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   This triangle has a base equal to the circle's full circumference (`2πR`) and a height equal to the circle's radius (`R`) <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   The area of this triangle is `(1/2) * base * height = (1/2) * 2πR * R = πR²`, which is the circle's area <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

Four such unwrapped circles (each a triangle with base `2πR` and height `R`) can perfectly fit into the `2πR` by `2R` rectangle representing the cylinder's lateral surface area <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

#### Why Sphere and Cylinder Areas are Equal: The Projection Method

The equality between the sphere's surface area and the cylinder's lateral surface area can be demonstrated by approximating the sphere's surface with many tiny rectangles <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

The idea is to [[Projection of spherical rectangles and area relationships | project these small spherical rectangles directly outward]] onto the cylinder, as if casting a shadow from a light source parallel to the xy-plane <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Surprisingly, the projection of each rectangle onto the cylinder ends up having the same area as the original rectangle <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

This is due to two competing effects that perfectly cancel each other out <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>:
1.  **Width scaling:** As a spherical rectangle is projected outward, its width (along latitude lines) gets scaled up <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This effect is more pronounced for rectangles closer to the poles <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. The scaling factor for the width is `R/d`, where `R` is the sphere's radius and `d` is the distance of the rectangle from the z-axis <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
2.  **Height scaling (squishing):** Because the spherical rectangles are at a slant with respect to the z-direction, their height (along longitude lines) gets scaled down during projection <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Rectangles near the poles are highly slanted, so their height is squished significantly <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Using [[Geometry and circles | properties of circles]] and similar triangles, it can be shown that the scaling factor for the height is `d/R` <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

Since the width is scaled by `R/d` and the height by `d/R`, the product of the dimensions (and thus the area) remains unchanged after projection (`width * (R/d) * height * (d/R) = width * height`) <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This holds true for infinitesimally small rectangles, meaning that as the approximation gets finer, the total surface area of the sphere matches that of the cylinder <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

### Connecting Sphere Surface Area to its Shadow

Another approach involves slicing the sphere into many thin rings parallel to the xy-plane <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a> and comparing the area of these rings to the area of their shadows on the xy-plane <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. The shadow of the entire northern hemisphere forms a circle with the same radius as the sphere <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

*   Let `R` be the sphere's radius and `theta` be the angle between a line from the sphere's center to a ring and the z-axis <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   The radius of a specific ring is `R * sin(theta)` <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   The circumference of this ring is `2πR * sin(theta)` <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   The thickness of the ring, corresponding to a small change in angle `d-theta`, is `R * d-theta` <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
*   Thus, the approximate area of a ring is `(2πR * sin(theta)) * (R * d-theta) = 2πR² * sin(theta) * d-theta` <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

The area of the shadow of one of these rings on the xy-plane can be found by considering the projection of the ring's thickness. This projected thickness is `R * cos(theta) * d-theta`. The radius of the shadow ring is `R * sin(theta)`. Therefore, the area of the shadow ring is approximately `2πR * sin(theta) * R * cos(theta) * d-theta`.

It can be shown that each ring's shadow has precisely half the area of one of the rings on the sphere, though not necessarily the one directly above it <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This correspondence implies that the area of the circle (the shadow of the northern hemisphere) is exactly one-fourth the total surface area of the sphere <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

### Generalization

The `4πR²` relation for spheres is a specific instance of a more general fact in [[Geometry in higher dimensions | geometry]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>: For any convex shape in three dimensions, the average area of all its possible two-dimensional shadows, averaged over all orientations, is exactly one-fourth of the shape's total surface area <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.