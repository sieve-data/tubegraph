---
title: Geometric reasoning in higher dimensions
videoId: zwAD6dRSVyI
---

From: [[3blue1brown]] <br/> 

Mathematics often entices with the beauty of [[geometric_reasoning_and_sphere_surface_area | geometric reasoning]] in two and three dimensions, where there is a strong interplay between numerical coordinates and spatial visualization <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. For example, a circle with radius 1 centered at the origin represents every pair of numbers (x,y) satisfying `x² + y² = 1` <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This connection is invaluable because facts that appear opaque in a purely analytic context can become clear geometrically, and vice versa <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This approach, especially the link between sums of squares and circles/spheres, has been fundamental to various mathematical concepts, including the connection between pi and number theory, visualizing Pythagorean triples, and applying the Borsuk-Ulam theorem <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The ability to frame analytic facts geometrically is highly beneficial in mathematics <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

However, this ease of visualization becomes a "tease" when dealing with more than three dimensions <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Our physical space constrains our geometric intuitions, leading to a loss of this helpful back-and-forth between numbers and spatial understanding <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Many problems could have elegant solutions if we could conceptualize lists of 10 or more numbers as individual points in a space <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. For mathematicians, computer scientists, and physicists, problems involving lists of more than three numbers are common <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The standard approach typically involves using two and three dimensions for [[analogy_between_2d_3d_and_higher_dimensions | analogy]] but fundamentally reasoning analytically, much like a pilot relying on instruments rather than sight when flying through clouds <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Visualizing Higher Dimensions with Sliders and "Real Estate"

To bridge the gap between purely geometric and purely analytic views, a hybrid method can be employed, making [[analytic_reasoning_to_geometric_intuition | analytic reasoning]] more visual in a way that generalizes to arbitrarily high dimensions <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This method helps to intuitively grasp counterintuitive phenomena that occur only in higher dimensions <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

The focus here is on [[understanding_higher_dimensional_spheres_and_shapes | higher-dimensional spheres]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. For instance, a four-dimensional sphere with radius one centered at the origin is the set of all quadruplets of numbers (x,y,z,w) where the sum of their squares is one (x² + y² + z² + w² = 1) <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. While visualizations of 4D spheres as 3D slices can be confusing and don't scale well to higher dimensions, a more literal approach is to think about each coordinate separately <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### The Slider Analogy

This approach involves picturing multiple vertical number lines, each with a slider to represent a coordinate <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Each configuration of these sliders represents a point in an N-dimensional space (e.g., a quadruplet in 4D space) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Being on a unit sphere centered at the origin means the sum of the squares of these slider values is one <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. The goal is to understand how slider movements correspond to movements on the sphere <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### The "Real Estate" Metaphor

To understand the relationship `x² + y² = 1` for a 2D circle, consider the value of `x²` as "real estate" belonging to `x`, and `y²` as real estate belonging to `y` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. They share a total of one unit of real estate <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Moving around the circle corresponds to a constant exchange of real estate between the variables <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

A crucial insight is that "real estate is cheap near zero and more expensive away from zero" <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   If `x=1` and `y=0`, `x` has all the real estate (1 unit). If `x` moves down slightly to `0.9`, `x²` becomes `0.81`, meaning `x` gave up `0.19` units of real estate <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   For `y²` to gain `0.19` units, `y` must move a significant distance (0.44 units) away from 0 <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. This implies `x` moved a little (giving up expensive real estate) for `y` to move a lot (gaining cheap real estate) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This corresponds to the steep slope on the circle <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   Visualizing tick marks indicating fixed units of real estate shows that sliders move slower away from zero, where real estate is more expensive <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   The square root of the total real estate among all coordinates gives the distance from the origin <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### Extending to 3D and Beyond

For a unit sphere in three dimensions (`x² + y² + z² = 1`), a third slider for `z` is added, and these three sliders still share one unit of real estate <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
*   If `x` is held at `0.5` (occupying `0.25` units of real estate), `y` and `z` trade off the remaining `0.75` units <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This corresponds to a circular slice of the sphere <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   As `x` increases, less real estate is left for `y` and `z`, making the circular slice smaller <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. When `x` reaches `1`, `y` and `z` are forced to be `0` (a singularity point) <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

In four dimensions and higher, the global spatial view is lost, but the fundamental rules of "real estate" exchange remain <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Fixing one slider and observing the others trade off represents a slice of the higher-dimensional sphere <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

## The Counterintuitive Nature of Higher Dimensions

This slider method can be used to explore famous problems that are intuitive in 2D/3D but become counterintuitive in higher dimensions <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

Consider a cube (or square in 2D) centered at the origin, with side length 2 (corners at ±1 for each coordinate). Unit spheres are centered at each of its vertices <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. The problem is to find the radius of the largest sphere centered at the origin that is tangent to all these corner spheres <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### 2D Case (Square with 4 Circles)

*   In 2D, a 2x2 square has corners like (1,1), (1,-1), etc. Four circles of radius 1 are centered at these corners <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   The distance from the origin to a corner (e.g., (1,1)) is `sqrt(1² + 1²) = sqrt(2)` (approx. 1.414) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   Subtracting the radius of a corner circle (1) gives the inner circle's radius: `sqrt(2) - 1` (approx. 0.414) <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. This seems reasonable <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### 3D Case (Cube with 8 Spheres)

*   In 3D, a 2x2x2 cube has 8 corners like (1,1,1) <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. Eight spheres of radius 1 are centered at these vertices <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   The distance from the origin to a corner (e.g., (1,1,1)) is `sqrt(1² + 1² + 1²) = sqrt(3)` (approx. 1.73) <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   Subtracting the radius of a corner sphere (1) gives the inner sphere's radius: `sqrt(3) - 1` (approx. 0.73) <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. Again, this seems reasonable <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

### Analyzing with Sliders: The Tangency Point

To understand the inner sphere's radius in higher dimensions, analyze the point of tangency between a corner sphere and the inner sphere using the slider method. For a sphere centered at (1,1,...,1) with radius 1, the point on it closest to the origin is where all coordinates are equal <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. At this point, the "real estate" is shared evenly among the coordinates when measured relative to the corner center <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. This point is also a point on the inner sphere centered at the origin <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

### 4D Case (Tesseract with 16 Hyperspheres)

*   In 4D, a 2x2x2x2 hypercube has 16 vertices <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. Sixteen unit spheres are centered at these corners <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.
*   Consider the corner sphere centered at (1,1,1,1). The point closest to the origin is where all four coordinates are equal <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.
*   At this point, each coordinate is 0.5 (halfway between 1 and 0) <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. The square of each coordinate (relative to origin) is `0.5² = 0.25` <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.
*   The total "real estate" with respect to the origin is `0.25 * 4 = 1` <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
*   This means the inner sphere has a radius of `sqrt(1) = 1` <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   Numerically, the distance from origin to corner (1,1,1,1) is `sqrt(1² + 1² + 1² + 1²) = sqrt(4) = 2` <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. Subtracting the corner sphere's radius (1) yields `2 - 1 = 1` <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
*   The surprising result is that the inner sphere is the same size as the corner spheres <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>, and it touches the bounding hypercube faces (e.g., at (1,0,0,0)) <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>. This feels too big if thinking in 2D/3D <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

### 5D Case

*   In 5D, there are 32 corner spheres <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.
*   The point closest to the origin on a corner sphere (centered at (1,1,1,1,1)) is where all five coordinates split the real estate evenly <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. Each coordinate will be slightly higher than 0.5 (e.g., if it were 0.5, total real estate would be `5 * 0.25 = 1.25`, which is too much) <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
*   From the origin's perspective, this configuration has more than one unit of real estate <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   The radius of the inner sphere is approximately 1.24 <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   This means the inner sphere actually *pokes outside* the 2x2x2x2x2 bounding hypercube <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.

### 10D Case

*   In 10 dimensions, points have ten coordinates <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. A unit sphere means one unit of real estate shared among ten coordinates <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>.
*   The point closest to the origin on a corner sphere (e.g., (1,1,...,1)) is where all ten coordinates split the real estate evenly <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>. This point feels "very far away from the origin" <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.
*   The inner sphere has a radius of approximately 2.16 <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
*   This 10D inner sphere is large enough to poke *outside* of a 4x4x4...x4 bounding hypercube (whose faces are 2 units from the origin) <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.
*   This phenomenon occurs because the corner point (1,1,...,1) is `sqrt(10)` units from the origin, which is about 3.16 <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>. The radius of the inner sphere is `sqrt(N) - 1`, where N is the dimension. As N increases, the inner sphere grows without bound, and the proportion of the inner sphere lying inside the bounding box decreases exponentially towards zero <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.

## Conclusion

The slider method provides a tangible way to reason about higher dimensions, making them feel less abstract and more like what mathematicians might discuss <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. It helps to move beyond simply asking if higher-dimensional space is "real" and instead explore properties of [[understanding_higher_dimensional_spheres_and_shapes | higher-dimensional spheres and shapes]] using this framework <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. While it's limited to understanding one point and local movements at a time, and it's coordinate-dependent, it offers a concrete foothold for conceptualizing high-dimensional shapes <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. Representing coordinates literally and using metaphors like "real estate" can illuminate counterintuitive aspects of higher dimensions, such as the increasing distance of a box's corner from its center <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. This approach reframes analytic reasoning as a visual instrument, leveraging our brain's image processing capabilities to think visually about what cannot be directly visualized <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.