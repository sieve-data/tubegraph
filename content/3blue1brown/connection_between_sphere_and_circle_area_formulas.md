---
title: Connection between sphere and circle area formulas
videoId: GNcFjFmqEc8
---

From: [[3blue1brown]] <br/> 

The [[surface_area_of_a_sphere | surface area of a sphere]] is commonly known as 4πR², a formula that curiously stands as a clean multiple of the more familiar πR², which represents the area of a circle with the same radius [[00:00:02 | 00:00:02]]. This article explores the underlying reasons for this relationship, offering two distinct lines of reasoning to provide a deeper, more visceral understanding of how the area of a sphere relates to that of four circles [[00:00:19 | 00:00:19]].

## Method 1: Connecting the Sphere to a Cylinder

One classic approach in [[geometry_of_spheres_and_cylinders | geometry]] demonstrates that the [[surface_area_of_a_sphere | surface area of a sphere]] is equivalent to the lateral [[surface area of a cylinder]] that shares the same radius and height as the sphere [[00:01:29 | 00:01:29]]. This method involves [[comparing_sphere_surface_area_with_cylinder_surface_area | comparing sphere surface area with cylinder surface area]]. The cylinder in question is imagined without its top and bottom caps, effectively just its "label" [[00:01:37 | 00:01:37]].

### Unwrapping the Cylinder

When this cylindrical "label" is unwrapped, it forms a rectangle [[00:01:43 | 00:01:43]]. The width of this rectangle corresponds to the cylinder's circumference, 2πR, and its height matches the sphere's diameter (and thus the cylinder's height), which is 2R [[00:01:48 | 00:01:48]]. Multiplying these dimensions (2πR * 2R) directly yields 4πR², the formula for the [[surface_area_of_a_sphere | surface area of a sphere]] [[00:02:00 | 00:02:00]].

### The Projection Principle (Archimedes' Proof)

The core of this elegant argument, often attributed to [[archimedes_proof_of_spheres_surface_area | Archimedes]], lies in approximating the [[surface_area_of_a_sphere | sphere's surface area]] with numerous tiny rectangles. The key insight is that if these spherical rectangles are projected directly outward onto the surrounding cylinder (as if casting a shadow by lights parallel to the xy-plane), the projected area on the cylinder surprisingly matches the original area of the spherical rectangle [[00:02:33 | 00:02:33], [00:02:47 | 00:02:47], [00:02:53 | 00:02:53]]. This demonstrates the fundamental principle behind [[geometric_analysis_of_sphere_and_cylinder | geometric analysis of spheres and cylinders]].

There are two counteracting effects during this projection:
1.  **Width Scaling**: Rectangles further from the equator (closer to the poles) experience a significant scaling up of their width as they are projected over a longer distance [[00:03:12 | 00:03:12], [00:03:20 | 00:03:20]].
2.  **Height Compression**: Due to their slant relative to the projection direction, the height of each rectangle is scaled down [[00:03:34 | 00:03:34], [00:03:39 | 00:03:39]]. Rectangles near the poles are more slanted, leading to greater height compression [[00:03:54 | 00:03:54]].

Remarkably, these two effects—stretching the width and squishing the height—cancel each other out perfectly [[00:04:08 | 00:04:08], [00:04:11 | 00:04:11]].

#### Detailed Geometric Explanation

To understand this cancellation, consider a small rectangle on the sphere at a distance 'd' from the z-axis (the axis of projection) [[00:04:48 | 00:04:48]].
*   **Width Scaling Factor**: By considering similar triangles formed by the sphere's radius (R) and the distance 'd', the width of the projected rectangle is scaled up by a factor of R/d [[00:05:24 | 00:05:24], [00:05:43 | 00:05:43], [00:05:49 | 00:05:49]].
*   **Height Scaling Factor**: By examining a cross-section and using the property that a tangent to a circle is perpendicular to the radius at the point of tangency [[00:06:20 | 00:06:20], [00:06:24 | 00:06:24]], another set of similar triangles reveals that the height of the projected rectangle is scaled down by a factor of d/R [[00:06:51 | 00:06:51], [00:07:53 | 00:07:53], [00:08:09 | 00:08:09], [00:08:12 | 00:08:12]].

Since the width is scaled by R/d and the height by d/R, their product, and thus the area, remains unchanged (Area_projected = Width_original * (R/d) * Height_original * (d/R) = Area_original) [[00:08:15 | 00:08:15], [00:08:18 | 00:08:18], [00:08:23 | 00:08:23]]. This holds true as the rectangles become infinitesimally small, providing a rigorous definition of [[surface_area_of_a_sphere | surface area]] for curved surfaces [[00:09:27 | 00:09:27], [00:09:55 | 00:09:55], [00:09:59 | 00:09:59]]. This type of reasoning is a fundamental concept in [[calculus]] presented without its formal jargon [[00:10:05 | 00:10:05]].

### Fitting the Circles

The visual connection between the sphere and four circles can be made by unwrapping each circle into a triangle [[00:10:34 | 00:10:34]]. This is done by relating thin concentric rings of the circle to horizontal slices of a triangle [[00:10:45 | 00:10:45]]. Because the circumference of each ring increases linearly with its radius (2π times radius), when these rings are "unwrapped" and lined up, their ends form a straight line, resulting in a triangle with a base of 2πR and a height of R [[00:10:52 | 00:10:52], [00:10:57 | 00:10:57], [00:11:00 | 00:11:00], [00:11:03 | 00:11:03], [00:11:08 | 00:11:08], [00:11:13 | 00:11:13]]. Four of these unwrapped circular triangles perfectly fit into the 2πR by 2R rectangle derived from the unwrapped cylinder, visually confirming the 4πR² formula [[00:11:17 | 00:11:17]]. This relates to [[geometry_and_circles | geometry and circles]] and [[pis_relationship_to_circles_and_geometry | pi's relationship to circles and geometry]].

## Method 2: Sphere to its Shadow (Direct Circle Connection)

Another way to connect the sphere's area directly to circles is by slicing the sphere into many thin rings parallel to the xy-plane [[00:12:10 | 00:12:10]]. The total area of the shadows of these rings from, say, the northern hemisphere, forms a circle with the same radius as the sphere [[00:12:18 | 00:12:18], [00:12:21 | 00:12:21]]. This approach involves comparing the area of these spherical rings to the area of their shadows on the xy-plane.

### Structured Exercises (Conceptual Framework)

To illustrate this connection, one can consider the following:

*   **Ring Circumference**: For a ring at an angle θ from the z-axis (measured from the sphere's center), its circumference is 2πR sin(θ) [[00:13:16 | 00:13:16]].
*   **Ring Area**: The approximate area of a thin ring with thickness R dθ is its circumference multiplied by its thickness: 2πR sin(θ) * R dθ [[00:13:25 | 00:13:25], [00:13:02 | 00:13:02]].
*   **Shadow Area**: The area of the shadow of one of these rings on the xy-plane needs to be determined [[00:13:53 | 00:13:53]]. It can be shown that each ring's shadow has precisely half the area of a specific ring on the sphere (not necessarily the one directly above it) [[00:14:12 | 00:14:12], [00:14:16 | 00:14:16]]. This involves [[projection_of_spherical_rectangles_and_area_relationships | projection of spherical rectangles and area relationships]] and [[proofs_of_sphere_surface_area_and_triangle_properties | triangle properties]].
*   **Correspondence**: There is a direct correspondence between all the shadows from the northern hemisphere (which form a circle of radius R) and every second ring on the sphere [[00:14:38 | 00:14:38], [00:14:41 | 00:14:41]].
*   **Implication**: This correspondence, as rings become infinitesimally thin, demonstrates that the area of the circle is exactly one-fourth the [[surface_area_of_a_sphere | surface area of the sphere]] [[00:14:58 | 00:14:58], [00:15:03 | 00:15:03]].

## Generalization

The four-fold relationship observed with spheres is not unique. For any convex shape in three dimensions, the average area of all its shadows (averaged over all possible orientations) is exactly one-fourth of the shape's total [[surface area of the sphere | surface area]] [[00:15:19 | 00:15:19], [00:15:24 | 00:15:24], [00:15:29 | 00:15:29], [00:15:33 | 00:15:33]].