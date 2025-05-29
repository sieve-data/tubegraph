---
title: Convex shapes and their surface area properties
videoId: GNcFjFmqEc8
---

From: [[3blue1brown]] <br/> 

The [[Surface area of a sphere | surface area of a sphere]] is commonly known as 4πR², a formula that curiously stands as a clean multiple of πR², the area of a circle with the same radius <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This article explores the underlying reasons for this relationship and extends the concept to other [[Convexity in mathematical geometry | convex shapes]] <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Understanding the Sphere's Surface Area

While a flat piece of paper cannot perfectly fit around a sphere due to differing curvatures <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, two main approaches offer satisfying connections between a sphere's surface area and circles <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Method 1: Comparison to a Cylinder

A classic geometric approach demonstrates that the [[Surface area of a sphere | surface area of a sphere]] is equal to the lateral surface area of a cylinder that shares the same radius and height as the sphere <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This cylinder, without its top and bottom, can be unwrapped into a rectangle <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

The rectangle's width is the cylinder's circumference (2πR) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, and its height is the sphere's diameter (2R) <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Multiplying these dimensions yields 4πR², which is the formula for the sphere's surface area <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

To further visualize the connection, four circles with radius R can be unwrapped into triangles <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. Each circle can be conceptualized as being composed of thin concentric rings, whose circumferences increase linearly with radius (2π times radius) <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. When these rings are straightened and lined up, they form a triangle with a base of 2πR and a height of R <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. These four unwrapped triangles perfectly fit into the unfolded cylinder label, representing the sphere's surface <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

#### The Core Argument: Area Preservation Through Projection

The equality between the sphere's and cylinder's surface areas can be demonstrated by approximating the sphere's area with many tiny rectangles <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. If these rectangles are projected directly outward onto the cylinder, their area surprisingly remains the same <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This concept is a key aspect of the [[Archimedes proof of spheres surface area | Archimedes proof of spheres surface area]] and the broader [[Geometry of spheres and cylinders | geometry of spheres and cylinders]].

There are two competing effects during this [[Projection of spherical rectangles and area relationships | projection]]:
1.  **Width Scaling Up:** As a rectangle is projected outward, its width is scaled up <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. For rectangles near the poles, this scaling is significant, while near the equator, it is minimal <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. The scaling factor for the width is R/d, where R is the sphere's radius and d is the rectangle's distance from the z-axis <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
2.  **Height Scaling Down:** Because these rectangles are slanted relative to the z-direction, their height is scaled down during [[Projection of spherical rectangles and area relationships | projection]] <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Rectangles near the poles are highly slanted, leading to a significant reduction in height, whereas those near the equator experience less effect <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Using similar triangles formed by the radius and the rectangle's position, it can be shown that the height is scaled down by a factor of d/R <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

These two effects—stretching the width by R/d and squishing the height by d/R—perfectly cancel each other out, ensuring that the area of each projected rectangle on the cylinder is identical to its original area on the sphere <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This reasoning, while geometric, is fundamentally calculus-based, relying on the idea that the approximation improves with finer coverings, leading to the same true surface area for both <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.

### Method 2: Sphere to Circle (Shadows)

Another approach involves cutting the sphere into many thin rings parallel to the xy-plane and comparing their areas to the areas of their shadows on the xy-plane <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. The shadows of all rings from, for example, the northern hemisphere, together form a circle with the same radius as the sphere <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

The core idea is to show a correspondence between these ring shadows and rings on the sphere <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. If each ring is defined by an angle theta from the z-axis, and its thickness is R * d-theta <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>, it can be demonstrated through trigonometric [[proofs_of_sphere_surface_area_and_triangle_properties | proofs]] that each ring's shadow on the xy-plane has precisely half the area of *another* ring on the sphere <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This correspondence ultimately implies that the area of the circle (formed by the shadows of one hemisphere) is exactly one-fourth the total [[Surface area of a sphere | surface area of the sphere]] <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

## General Property for [[Convexity in mathematical geometry | Convex Shapes]]

The fourfold relation observed with spheres is not unique to them <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. It is a specific instance of a more general fact applicable to all [[Convexity in mathematical geometry | convex shapes]] in three dimensions <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. If you take any [[Convexity in mathematical geometry | convex shape]] and calculate the average area of all its shadows (averaged over all possible orientations in 3D space), that average will be exactly one-fourth of the shape's total surface area <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.