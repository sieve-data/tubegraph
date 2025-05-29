---
title: Convexity in mathematical geometry
videoId: ltLUadnCyi0
---

From: [[3blue1brown]] <br/> 

Convexity is a fundamental property of shapes in [[geometry_in_higher_dimensions | mathematical geometry]] <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. It's often understood intuitively as shapes that "bulge out" and "never dent inward" <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

## Formal Definition <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>

A set is considered [[convex_shapes_and_their_surface_area_properties | convex]] if, for any two points chosen within that set, the straight line connecting those two points is entirely contained within the set itself <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.

## Examples of Convex and Non-Convex Shapes

### Convex Examples
*   **Square**: A square is [[convex_shapes_and_their_surface_area_properties | convex]] because any line segment connecting two points inside it will always remain within the square <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **Cube**: Similar to a square, a cube is a [[convex_shapes_and_their_surface_area_properties | convex]] three-dimensional solid <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
*   **Sphere**: A sphere is the most symmetric [[convex_shapes_and_their_surface_area_properties | convex]] solid <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.

### Non-Convex Examples
*   **The symbol π**: This symbol is not [[convex_shapes_and_their_surface_area_properties | convex]] because one can easily find two points within it such that the line connecting them passes outside the symbol <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
*   **Letters in the word "convex"**: None of the letters in the word "convex" are themselves [[convex_shapes_and_their_surface_area_properties | convex]] <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
*   **Donut**: A donut is a non-[[convex_shapes_and_their_surface_area_properties | convex]] shape, as a ray of light passing through it could enter and exit multiple times <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

## Properties of Convex Shapes Related to Shadows

The concept of [[convex_shapes_and_their_surface_area_properties | convexity]] is crucial when calculating the average area of a shadow <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

### Ray of Light Principle for Convex Solids
For a [[convex_shapes_and_their_surface_area_properties | convex]] solid, any ray of light that hits a point in its shadow will pass through the solid at exactly two points: one point where it enters and one point where it exits <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. This is a direct consequence of the definition of [[convex_shapes_and_their_surface_area_properties | convexity]] <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. The line segment connecting these entry and exit points must remain entirely within the solid <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

> [!INFO] Double Coverage of Shadow Area
> Due to this property, the area of the shadow for a given orientation of a [[convex_shapes_and_their_surface_area_properties | convex]] solid (like a cube) is exactly half the sum of the areas of all its faces that are illuminated by the light source <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. This means the individual face shadows "double cover" the total shadow area <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. If the shape were non-[[convex_shapes_and_their_surface_area_properties | convex]], this clean two-to-one cover would not hold <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.

### Universal Proportionality Constant for Average Shadow Area
For any [[convex_shapes_and_their_surface_area_properties | convex]] solid, the average area of its shadow (when considering a distant light source resulting in a flat projection) is proportional to its surface area <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>. Crucially, this proportionality constant is the *same* for all [[convex_shapes_and_their_surface_area_properties | convex]] solids <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>.

This universal constant can be determined by considering a simple [[convex_shapes_and_their_surface_area_properties | convex]] shape whose shadow area is known, such as a sphere <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>. The shadow of a sphere is always a circle with area πr², and its surface area is 4πr² <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. Thus, the average shadow area of a sphere is 1/4th its surface area <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>. Since this constant applies to all [[convex_shapes_and_their_surface_area_properties | convex]] solids, the average shadow area of a cube is also 1/4th of its surface area <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.

The argument for this universal constant can be extended to shapes without flat faces, such as spheres, by considering a sequence of polyhedra that increasingly [[approximations_and_limits_in_geometry | approximate]] the sphere <a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>. The ratio of average shadow area to surface area remains constant for each approximation, and thus holds true in the limit for the sphere itself <a class="yt-timestamp" data-t="00:33:31">[00:33:31]</a>.

## Quantifying Convexity <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>

The relationship between average shadow area and surface area for [[convex_shapes_and_their_surface_area_properties | convex]] solids suggests a way to quantify the degree of [[convex_shapes_and_their_surface_area_properties | convexity]] for any solid <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.

> [!TIP] Convexity Metric
> Consider the average area of a solid's shadow, multiply it by four, and then divide it by the solid's surface area <a class="yt-timestamp" data-t="00:38:22">[00:38:22]</a>.
>
> *   If this number is **one**, the solid is [[convex_shapes_and_their_surface_area_properties | convex]] <a class="yt-timestamp" data-t="00:38:27">[00:38:27]</a>.
> *   If it is **less than one**, the solid is non-[[convex_shapes_and_their_surface_area_properties | convex]] <a class="yt-timestamp" data-t="00:38:31">[00:38:31]</a>.
> *   The closer the value is to one, the closer the shape is to being [[convex_shapes_and_their_surface_area_properties | convex]] <a class="yt-timestamp" data-t="00:38:31">[00:38:31]</a>.