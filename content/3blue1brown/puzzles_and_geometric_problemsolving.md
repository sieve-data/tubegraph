---
title: Puzzles and geometric problemsolving
videoId: piJkuavhV50
---

From: [[3blue1brown]] <br/> 

This article explores a series of puzzles, primarily geometric, that often find their most elegant solutions by conceptualizing the problem in a higher dimension than initially presented <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. While the initial puzzles begin simply as pure geometry problems with surprising solutions, the underlying theme eventually touches upon the nature and utility of higher dimensions in mathematics <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Rhombus Tiling Puzzle

The first puzzle involves a rhombus shape with internal angles of 60 and 120 degrees <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Copies of this rhombus can tile a plane, often forming a pseudo-hexagonal pattern <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. A key observation is that three of these rhombuses can form a small hexagon <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Rotating these three tiles by 60 degrees generates a slightly different tiling pattern <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

The puzzle then asks:
*   Is it possible to get from any one tiling pattern of a finite hexagon (e.g., a hexagon with side length 4, tiled by unit rhombuses) to any other pattern using these hexagonal rotation steps? <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>
*   If not, how many fundamentally distinct patterns exist? <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>
*   If yes, how to get from any one to another? <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>
*   What is the maximum number of moves required to transform one pattern into another, as a function of the hexagon's size? <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>

### The Higher-Dimensional Insight

The solution to this puzzle becomes clear by applying [[geometric_reasoning_in_higher_dimensions | geometric reasoning in higher dimensions]] <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. By coloring the tiles based on their orientation, one can visualize the two-dimensional tiling as a projection of a stack of three-dimensional cubes <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. Any stack of cubes within an n by n by n frame corresponds to one of these rhombus tiling patterns, and conversely, any rhombus tiling corresponds to a stack of cubes <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

The fundamental move of rotating a hexagon by 60 degrees corresponds to adding or removing a cube from this stack <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

*   **Reachability:** It is possible to get from any pattern to any other <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. One can remove all cubes to reach an "empty" configuration, then add the necessary cubes to form the desired pattern <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **Maximum Moves:** The maximum number of moves occurs when transforming an "empty" configuration to a "full" configuration, which requires `n³` steps, indicating the inherent three-dimensionality of the puzzle <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Tarski-Planck Problem: Covering a Circle with Strips

This puzzle, also known as the Tarski-Planck problem, involves covering a unit circle with strips <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. A "strip" is defined as any region bounded by two parallel chords, and its "width" (`d`) is the distance between these chords <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. The question asks for the minimum possible sum of the widths of all strips required to completely cover the circle's area <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

A simple way to cover the circle is with one strip of width 2 (the diameter), resulting in a sum of 2 <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The challenge is to prove if a sum less than 2 is possible, or if 2 is the minimum <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### The Higher-Dimensional Insight

The difficulty arises because the area of a strip is not directly proportional to its width in two dimensions <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. However, this proportionality becomes true when applying [[geometric_reasoning_in_higher_dimensions | geometric reasoning in higher dimensions]] by projecting everything onto a hemisphere sitting above the circle <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. On this three-dimensional hemisphere, the area of a projected strip is `πd`, regardless of its position <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

This insight relates to Archimedes' proof for the surface area of a sphere <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, which shows that projecting areas from a sphere onto an enclosing cylinder preserves their size <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

*   If a set of strips covers the circle, their projections cover the hemisphere <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   The sum of the areas of these projected strips is `Σ (πd_i) = π Σ d_i` <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   This sum must be at least the area of the hemisphere, which is `2π` (since a unit sphere has surface area `4π`, and a hemisphere is half of that) <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   Therefore, `π Σ d_i ≥ 2π`, implying `Σ d_i ≥ 2` <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
This proves that 2 is indeed the minimum possible value for the sum of the widths <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Three Circles and Their External Tangents

This problem asks to prove that for any three circles in two-dimensional space, the three intersection points formed by the external tangents of each pair of circles always lie on the same line <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. It's assumed that no circle is inside another and no two circles have the same size (as this would make tangents parallel) <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

### Initial Higher-Dimensional Insight (and its limitation)

The common approach involves imagining each circle as the equator of a sphere in three dimensions <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. For any pair of spheres, there's a cone of external tangents that intersect at a single point <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. The insight suggests that a single plane can rest on top of all three spheres <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. This plane passes through the tangency points, and lines connecting these points are external tangents that pass through the desired intersection points <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. Since these three points lie on this "top" plane and also on the original two-dimensional plane of the circles, they must lie on the intersection of these two planes, which is a line <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

However, this argument has a limitation: it doesn't work if one of the spheres is smaller and positioned between the other two, as a single plane cannot rest on all three <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

### Refined Higher-Dimensional Insight

The argument can be saved by using cones instead of spheres <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. Imagine three different cones, each with a base at one of the circles, and all having the same angle at their tips, making them similar shapes <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

The line passing through the tip of any two cones also passes through the intersection point of the external tangents of their base circles <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. This point is the "center of similarity" for the two shapes <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

*   Now, consider the plane that passes through the tips of all three cones <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>. Any three points in space (the cone tips) define a plane <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.
*   This plane intersects the original `xy` plane (where the circles lie) <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   The line of intersection of these two planes is precisely the line on which the three desired points (the centers of similarity) must lie <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
This revised argument is more general and also allows for cases where one circle is inside another, as the concept of a center of similarity still applies even without external tangents <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. Furthermore, this principle extends to any three similar shapes (not just circles) as long as they are in the same orientation, using pyramid-like shapes instead of cones <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

## Stepping into Four Dimensions

Having seen how [[geometric_reasoning_in_higher_dimensions | three-dimensional insights]] can illuminate two-dimensional problems, a natural progression is to consider how four-dimensional insights might solve three-dimensional problems <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

### Puzzle: Volume of a Tetrahedron

The challenge is to write an explicit formula for the volume of a tetrahedron given the coordinates of its four vertices in three-dimensional space <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. A significant hint suggests that an elegant approach involves thinking about the determinant of a 4x4 matrix <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. Considering the analogous problem in lower dimensions—finding the area of a triangle given its corner coordinates—is also helpful <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. This problem's solution provides a nice explanation for the determinant formula itself <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.

### Constructing a 3D Puzzle with 4D Insights: Hypercube Projections

Inspired by the first puzzle, one can attempt to construct a three-dimensional tiling pattern that a four-dimensional creature could perceive as a stack of four-dimensional hypercubes <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. The goal is to find an equivalent "move" in 3D that a 4D creature would understand as adding or removing hypercubes <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

*   **Hypercube Coordinates:** A 4D hypercube can be defined by vertices with coordinates consisting of every combination of 0s and 1s <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. Edges connect vertices that differ in only one coordinate <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.
*   **Projection:** Analogous to projecting a 3D cube onto a 2D plane (which appears as a hexagon), a 4D hypercube can be projected onto a 3D subspace <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>. Projecting along the 4D diagonal (vector 1,1,1,1) results in a beautiful and symmetric shape known as a rhombic dodecahedron <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>. This shape is known to tessellate 3D space, which becomes evident when considering it as a projection of stacked hypercubes <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.
*   **The Tiling Pieces:** The "cubical cells" of the hypercube (3D components) project down as "squished cube" shapes <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>. These four squished cubes fit together to form a rhombic dodecahedron <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.
*   **The "Move":** The 2D rotation of rhombuses (corresponding to adding/removing cubes) can be reinterpreted as sliding faces perpendicular to themselves <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>. In the 4D to 3D projection, the analogous move is to take each of the four squished cubes and slide it through the origin, which provides a distinct way to tile the rhombic dodecahedron <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>.

The "absurd puzzle" then asks: If you use many copies of this squished cube shape to tile a large rhombic dodecahedron, and every time you find a small 1x1x1 rhombic dodecahedron within the tiling, you make the "slide through the middle" move, what is the maximum number of moves required to get from one tiling to another? <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a> The insight from hypercubes reveals the answer: `n^4`, where `n` is the size of the large rhombic dodecahedron <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>.

## Analysis vs. Intuition in Higher Dimensions

While these puzzles are fun and illustrative, they highlight a broader phenomenon in mathematics where constructs in higher dimensions can simplify problems in lower dimensions, even non-geometric ones <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. Examples include:
*   **Quaternions:** An extension of complex numbers in four dimensions that elegantly encode and work with three-dimensional rotations <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>.
*   **Sphere Packing:** An unusually elegant way to pack spheres in 24 dimensions is related to error correction codes used on Voyager spacecrafts <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>.
*   **Random Vectors:** In very high dimensions, random vectors tend to be nearly perpendicular, a fact relevant to neural networks and compression algorithms <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>.

However, a key distinction exists between analysis and intuition in higher dimensions <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. We can intuitively grasp the 3D insights for 2D problems (e.g., picturing a line as the intersection of two planes) <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>. But problems leveraging dimensions four and higher often rely purely on analytical reasoning, with analogies offering guiding lights but the core proof residing in abstract analysis <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>. This reliance on pure analysis can be daunting, as intuition is crucial for navigating the vast space of possible logical moves in [[problemsolving strategies in math | mathematical problem solving]] <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>. The "sadness" arises from the thought that there might be three-dimensional problems solvable with a higher-dimensional intuition that remains inaccessible to our three-dimensional minds <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.