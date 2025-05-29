---
title: Geometry puzzles involving tiling and shapes
videoId: piJkuavhV50
---

From: [[3blue1brown]] <br/> 

This article explores a series of geometry puzzles, many of which can be solved or better understood by considering them from the perspective of [[geometry_in_higher_dimensions | higher dimensions]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While the initial problems are set in two or three dimensions, their elegant solutions often emerge from a shift in perspective to an additional dimension <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Puzzle 1: Rhombus Tiling of a Hexagon

The first puzzle involves a rhombus shape with internal angles of 60 degrees and 120 degrees <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Copies of this rhombus can tile the plane in various distinct, pseudo-hexagonal patterns <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### The "Hexagonal Rotation" Move
When three rhombus shapes form a small hexagon, these three tiles can be rotated 60 degrees to generate a slightly different tiling <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This rotation might create new hexagons that can also be rotated, leading to a sequence of different tiling patterns <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### The Puzzle Questions
For a finite hexagon (e.g., with side length 4) filled with these unit rhombuses <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>:
1.  Is it possible to get from any tiling of this finite hexagon to any other tiling using these hexagonal rotation moves <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>?
2.  If no, how many fundamentally distinct patterns exist <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>?
3.  If yes, which two states are farthest apart (requiring the maximum number of moves) and what is that number as a function of the hexagon's size <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>?

### Solution through Higher Dimensions
The key insight comes from coloring the tiles based on their orientation and perceiving the 2D tiling as a projection of a stack of cubes in three dimensions <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. Any stack of cubes within an *n* by *n* by *n* frame corresponds to one of these rhombus tiling patterns, and conversely, any tiling corresponds to a stack of cubes <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

The fundamental "hexagonal rotation" move is equivalent to adding or removing cubes from the stack <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Reachability**: It becomes clear that any pattern can be reached from any other by first removing all cubes to an empty configuration, then adding the necessary cubes to form the desired pattern <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Maximum Moves**: Since each move corresponds to adding or removing a cube, the maximum number of steps required to get from one configuration to another is to go from the empty configuration to the full configuration, which takes *n*<sup>3</sup> steps <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This reveals the inherent three-dimensionality baked into the 2D puzzle <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Puzzle 2: Tarski-Planck Problem (Covering a Circle with Strips)

This problem, also known as the Tarski-Planck problem, asks about covering a unit circle with multiple "strips" <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. A strip is a region bounded by two parallel chords, and its width (*d*) is the distance between these chords <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### The Puzzle Question
If enough strips are used to completely cover the area of the circle, what is the minimum possible value for the sum of the widths of all those strips <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>?
*   Trivial examples, such as a single strip with width 2 (the diameter) or multiple parallel strips, result in a sum of widths equal to 2 <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. The question is whether a sum less than 2 is possible <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Solution through Higher Dimensions
Directly relating the area of a strip to its width is awkward in 2D because a strip's area depends on its position within the circle <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. However, this relationship simplifies if one projects everything onto a hemisphere sitting above the circle <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

The "magic" is that the area of a projected strip on the 3D hemisphere is always pi times its width (*πd*), regardless of its position <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. This property is related to Archimedes' proof for the surface area of a sphere, where projecting areas from a sphere onto a surrounding cylinder preserves the area <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

Since the sum of the areas of the projected strips on the hemisphere (Σ *πd*) must be at least the area of the hemisphere (2*π*), it follows that the sum of the widths (Σ *d*) must be at least 2 <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Thus, 2 is the minimum possible value, again leveraging [[spatial_intuition_in_math | 3D intuition]] for a 2D problem <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

## Puzzle 3: External Tangents of Three Circles

This puzzle, related to Monge's theorem, involves three circles in a 2D plane <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

### The Puzzle Claim
Draw the external tangents to each pair of circles. The three points where these pairs of external tangents intersect always fall on the same line <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. (Assumptions: no circle is inside another, and no two circles have the same size, as parallel tangents would not intersect <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>).

### Initial 3D Insight (and its flaw)
A common proof involves imagining each circle as the equator of a sphere in 3D space <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. The external tangents of a pair of circles become cones of external tangents around their respective spheres, all intersecting at a single point <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

The idea is that a plane tangent to the top of all three spheres would pass through these three intersection points <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. Since these three points also lie on the original 2D plane where the circles resided, they must lie on the intersection of these two planes, which is a line <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

*   **The Flaw**: This argument fails if one of the spheres is significantly smaller and placed in the middle, as there is no single plane that can rest on top of all three <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

### Corrected 3D Insight: Using Cones
To save the proof, one can use cones instead of spheres <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. Each circle forms the base of a cone, with the condition that all three cones have the same angle at their tips, making them similar shapes <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

The intersection point of the external tangents for two circles is the "center of similarity" for those two shapes <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. The line passing through the tips of any two cones also passes through their corresponding center of similarity <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. Therefore, the three intersection points correspond to the three lines connecting the cone tips.

Since any three points in space define a plane (unless collinear), the three tips of the cones define a plane <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>. This plane intersects the original 2D plane of the circles along a line, on which the three intersection points must lie <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. This refined argument works generally, even if one circle is inside another or if they are of differing sizes <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. The theorem also extends to any three similar shapes in the same orientation <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.

## Puzzle 4: Volume of a Tetrahedron

This puzzle, while not fully solved in the provided transcript, demonstrates how [[matrix_dimensions_and_their_geometric_interpretations | matrix dimensions]] can hint at higher-dimensional connections.

### The Puzzle Question
Given four points in three-dimensional space that form the vertices of a tetrahedron, write an explicit formula for its volume in terms of the coordinates of those four points <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.

### Hint
One elegant way to view this problem involves the determinant of a 4x4 matrix <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>. Thinking about the analogous problem one dimension lower—finding the area of a triangle given its corner coordinates—can be helpful <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>. Solving this type of puzzle across different dimensions can explain the formula for the determinant <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.

## Puzzle 5: Three-Dimensional Tiling from a 4D Perspective (Rhombic Dodecahedron)

This puzzle is an attempt to construct a 3D tiling problem that requires [[geometry_in_higher_dimensions | four-dimensional insight]] for its solution, analogous to how the first puzzle required 3D insight.

### The 4D Cube and its Projection
A 4D cube (hypercube) can be defined by vertices where each coordinate is 0 or 1 <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. By projecting this 4D cube onto the 3D subspace perpendicular to the diagonal vector (1,1,1,1), one obtains a highly symmetric shape known as a rhombic dodecahedron <a class="yt-timestamp" data-t="00:22:18">[00:22:18]</a>. The fact that the rhombic dodecahedron can tessellate 3D space becomes evident from this 4D projection <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>.

### The Analogous Tiling Puzzle
In the 2D rhombus tiling puzzle, the rhombuses were projections of square faces of 3D cubes <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>. In 4D, the analogous elements are the cubical "cells" of the hypercube. Each of these 3D cubical cells projects into a "squished cube shape" <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>. Four of these squished cubes together perfectly form a rhombic dodecahedron <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>.

The "move" in this puzzle is an analogy to the 2D rotation. Just as 2D rhombuses could "slide" through the origin in their projection (representing adding/removing a cube in 3D) <a class="yt-timestamp" data-t="00:24:32">[00:24:32]</a>, these 3D squished cubes can slide through the origin of the rhombic dodecahedron to create different tilings <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>.

### The Absurd Puzzle Question
Describe the "squished cube shape" (a polyhedron formed by six rhombuses) <a class="yt-timestamp" data-t="00:25:02">[00:25:02]</a>. Use many copies of this shape to tile a large rhombic dodecahedron. The game involves making a "move" every time a small 1x1x1 rhombic dodecahedron is found within the tiling, where each piece slides through the middle <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>.

What is the maximum number of moves that it might take to get from one tiling to another <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>?
*   **Answer**: If one understands this as a projection of a stack of 4D hypercubes, the answer is *n*<sup>4</sup>, where *n* is the size of the large rhombic dodecahedron <a class="yt-timestamp" data-t="00:25:45">[00:25:45]</a>.

## Broader Theme: The Power and Limits of Higher Dimensions

These puzzles highlight a broader mathematical phenomenon: constructs in [[geometry_in_higher_dimensions | higher dimensions]] can be remarkably useful for solving problems in lower dimensions, even non-geometric ones <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>.

### Examples of Higher-Dimensional Utility
*   **Quaternions**: An extension of complex numbers that naturally live in four dimensions, offering an elegant way to encode and work with 3D rotations <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. They involve a "rigid motion" of a hypersphere unlike anything in two or three dimensions <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.
*   **Sphere Packing**: In 24 dimensions, there's an unusually elegant way to pack spheres, which is closely tied to error correction codes used on Voyager spacecrafts <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a>.
*   **Random Vectors**: In very high dimensions, random vectors tend to be nearly perpendicular, a fact relevant to neural networks (e.g., explaining why large language models perform better at scale) and compression algorithms <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>.

### Intuition vs. Analysis in Higher Dimensions
While mathematical rigor relies on analysis, [[spatial_intuition_in_math | intuition]] is crucial for guiding [[problemsg_strategies_in_mathematical_puzzles | problem-solving strategies]] <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. For 2D and 3D problems, humans can often develop a visual intuition for higher-dimensional solutions (e.g., seeing a 2D tiling as a stack of 3D cubes, or a line as the intersection of two planes in 3D) <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.

However, direct spatial intuition for dimensions beyond three is generally inaccessible to humans <a class="yt-timestamp" data-t="00:28:19">[00:28:19]</a>. Solutions involving even higher dimensions (e.g., 4D or beyond) rely more on analogies and pure analysis, lacking the intuitive "guiding light" that lower-dimensional problems afford <a class="yt-timestamp" data-t="00:28:24">[00:28:24]</a>. This limitation leads to a "sadness" about the potential for solutions that remain beyond human intuitive grasp <a class="yt-timestamp" data-t="00:29:04">[00:29:04]</a>.