---
title: Threedimensional puzzles and fourdimensional insights
videoId: piJkuavhV50
---

From: [[3blue1brown]] <br/> 

Many mathematical puzzles, particularly those involving geometry, can be effectively solved or understood by "stepping up" into a higher dimension. This approach leverages intuitions from familiar dimensions to gain insight into problems in lower or even higher dimensions [00:00:11].

## Higher-Dimensional Thinking in Lower-Dimensional Puzzles

### Rhombus Tiling Puzzle

One puzzle involves tiling a finite hexagon with rhombus shapes, each having internal angles of 60 and 120 degrees [01:52:00]. A specific move allows rotating a small hexagon formed by three rhombuses by 60 degrees [02:13:00]. The core questions are:
*   Is it possible to transform any tiling pattern into any other using these rotations? [02:06:00]
*   If not, how many distinct patterns exist? [02:25:00]
*   If yes, what is the maximum number of moves required to get from one state to another, as a function of the hexagon's size? [02:32:00]

#### Three-Dimensional Insight
The solution to this puzzle becomes clear by [[geometric_visualization_in_puzzlesolving | visualizing]] the 2D tiling as a projection of a stack of 1x1x1 cubes in a 3D space [04:42:00]. Each unique tiling of rhombuses corresponds to a specific stack of cubes [05:03:00]. The rotation move of three rhombuses in the 2D plane is equivalent to adding or removing a single cube from the 3D stack [05:38:00].

From this [[geometric_visualization_in_puzzlesolving | three-dimensional perspective]], it becomes evident that any tiling pattern can be transformed into any other: one can remove all cubes to reach an empty state, then add the necessary cubes to form the desired pattern [05:43:00]. The maximum number of moves required to transition between any two configurations is equivalent to moving from an empty configuration to a full one, which for an *n* x *n* x *n* frame of cubes, is *n*<sup>3</sup> steps [06:09:00] - <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>. This numerical answer, *n*<sup>3</sup>, inherently indicates the puzzle's three-dimensional nature [06:33:00].

### Tarski-Planck Problem

The Tarski-Planck problem, or "covering the unit disk with strips," asks for the minimum sum of widths of parallel-chord-bound strips required to completely cover a unit circle [03:02:00] - <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. A simple covering using a single strip with a width equal to the circle's diameter (2 units) yields a sum of 2 [03:55:00]. Subdividing this into multiple parallel strips also results in a sum of 2 [04:07:00]. The challenge is to prove whether a sum less than 2 is possible [04:17:00].

#### Three-Dimensional Insight
Directly relating the area of a strip to its width in 2D is difficult because the area depends on the strip's position within the circle [07:36:00]. However, this relationship simplifies if the problem is projected onto a hemisphere sitting above the circle [08:02:00]. On the 3D hemisphere, the area of a projected strip is proportional to its width (specifically, π times its width for a unit radius sphere), regardless of its position [08:15:00] - <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>.

This principle is related to Archimedes' proof for the surface area of a sphere, which demonstrates that projecting areas from a sphere onto an encompassing cylinder preserves their area [08:35:00] - <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>. By projecting the 2D strips onto the hemisphere, the sum of their 3D areas (π times the sum of widths) must be at least the area of the hemisphere (2π) [09:50:00] - <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>. This implies that the sum of the widths cannot be less than 2, proving that 2 is the minimum possible value [10:11:00] - <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>.

### Three Circles and External Tangents

A classic [[puzzles_and_geometric_problemsolving | geometric problem]] states that for three distinct circles in a 2D plane (no two having the same size and none inside another), the three intersection points formed by the external tangents to each pair of circles always lie on a single straight line [11:02:00] - <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>.

#### Three-Dimensional Insight (Initial)
The common proof involves imagining each circle as the equator of a sphere in 3D space [12:26:00]. The external tangents to two circles in 2D correspond to a cone of external tangents to the two spheres in 3D, all intersecting at a single point [12:31:00] - <a class="yt-timestamp" data-t="12:52:00">[12:52:00]</a>. A key insight is to consider a plane that rests on top of all three spheres [13:01:00]. This plane contains the tangency points and thus passes through the three intersection points of the external tangents [13:09:00] - <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>. Since these three points also lie on the original 2D plane of the circles, they must lie on the intersection of these two planes, which is a line [13:37:00] - <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>.

#### Refined Three-Dimensional Insight
This initial argument has limitations; it fails if one sphere is significantly smaller than the other two and located in the middle, preventing a single plane from resting on all three [14:09:00] - <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>. A more robust argument involves using cones instead of spheres [14:45:00]. Each circle serves as the base of a cone, with all cones having the same angle at their tips (making them similar shapes) [14:50:00].

The line passing through the tips of any two cones also passes through the intersection point of the external tangents of their base circles. This is because the intersection point is the "center of similarity" for the two shapes [15:01:00] - <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>. Since there are three such cones, the three lines connecting their tips correspond to the three intersection points [15:50:00]. The three tips of the cones always define a unique plane in 3D space [16:04:00]. The intersection of this plane with the original 2D plane (where the circles lie) is the line on which the three intersection points must fall [16:16:00] - <a class="yt-timestamp" data-t="16:26:00">[16:26:00]</a>. This refined argument handles all configurations, including cases where one circle is inside another, by reframing the points as centers of similarity rather than intersection points of tangents [16:40:00] - <a class="yt-timestamp" data-t="17:04:00">[17:04:00]</a>. This [[analogy_between_2d_3d_and_higher_dimensions | analogy]] can be extended to any three similar shapes in the same orientation, with their centers of similarity also falling on a line [17:07:00] - <a class="yt-timestamp" data-t="17:18:00">[17:18:00]</a>.

## Three-Dimensional Puzzles and Four-Dimensional Insights

While the previous examples show how 3D insights solve 2D problems, the question arises whether 3D problems can be solved by stepping into four or more dimensions [17:32:00] - <a class="yt-timestamp" data-t="17:40:00">[17:40:00]</a>.

### Volume of a Tetrahedron

The problem of finding an explicit formula for the volume of a tetrahedron given the coordinates of its four vertices in 3D space [17:44:00] - <a class="yt-timestamp" data-t="18:04:00">[18:04:00]</a>.

#### Four-Dimensional Hint
A major hint is that one elegant solution involves thinking about the determinant of a 4x4 matrix [18:13:00] - <a class="yt-timestamp" data-t="18:17:00">[18:17:00]</a>. This problem is analogous to finding the area of a triangle from its 2D coordinates [18:20:00]. The solution to this problem and its lower-dimensional analogs can provide a deeper understanding of the determinant formula in [[threedimensional_linear_transformations | linear algebra]] [18:35:00].

### Tiling with Rhombic Dodecahedra

Inspired by the first puzzle, a conceptual 3D puzzle can be constructed that mirrors its structure but requires a 4D insight [19:06:00]. The goal is to find a 3D tiling pattern that a 4D creature could "squint their eyes" and see as a stack of 4D hypercubes [19:10:00] - <a class="yt-timestamp" data-t="19:21:00">[19:21:00]</a>. What is the equivalent 3D move that corresponds to adding or removing 4D hypercubes? [19:26:00] - <a class="yt-timestamp" data-t="19:35:00">[19:35:00]</a>

#### Four-Dimensional Insight
A cube in 3D space can be represented by vertices with coordinates (0,0,0) to (1,1,1) [19:52:00] - <a class="yt-timestamp" data-t="20:08:00">[20:08:00]</a>. Projecting a cube along its main diagonal (1,1,1) onto a perpendicular plane results in a hexagon [21:09:00].
Similarly, a 4D hypercube has vertices represented by four coordinates (0 or 1) [20:18:00]. Projecting a 4D hypercube along its main diagonal (1,1,1,1) onto a 3D subspace results in a beautiful and symmetric shape called a rhombic dodecahedron [21:56:00] - <a class="yt-timestamp" data-t="22:18:00">[22:18:00]</a>. The rhombic dodecahedron is known to tessellate 3D space, which is apparent when understood as a projection of a stack of hypercubes [22:26:00] - <a class="yt-timestamp" data-t="22:40:00">[22:40:00]</a>.

In the original 2D puzzle, square faces of the cube project as rhombuses, and rotating the hexagon corresponds to sliding these rhombuses through the origin [23:04:00] - <a class="yt-timestamp" data-t="23:50:00">[23:50:00]</a>. Analogously, the 3D "cubical cells" of a 4D hypercube (formed by choosing three out of four basis vectors) project into squished cube shapes [23:50:00] - <a class="yt-timestamp" data-t="24:04:00">[24:04:00]</a>. Four of these squished cubes together form a rhombic dodecahedron [24:04:00] - <a class="yt-timestamp" data-t="24:10:00">[24:10:00]</a>.

The "move" in this 3D puzzle would be to take a small 1x1x1 rhombic dodecahedron within a larger tiling and slide its constituent pieces through the middle [25:11:00] - <a class="yt-timestamp" data-t="25:29:00">[25:29:00]</a>. The problem then asks for the maximum number of moves to get from one tiling to another [25:29:00]. The 4D insight leads to the answer: *n*<sup>4</sup>, where *n* is the size of the large rhombic dodecahedron [25:36:00] - <a class="yt-timestamp" data-t="25:45:00">[25:45:00]</a>.

## Broader Implications of Higher Dimensions

These [[puzzles_and_geometric_problemsolving | puzzles]] highlight a significant phenomenon in mathematics: higher-dimensional constructs can be remarkably relevant to solving problems in lower dimensions or even non-geometric contexts [26:01:00] - <a class="yt-timestamp" data-t="26:11:00">[26:11:00]</a>.

*   **Quaternions**: These are an extension of complex numbers that naturally exist in four dimensions. They provide an elegant way to encode and work with 3D rotations, even if the user doesn't directly visualize 4D [26:15:00] - <a class="yt-timestamp" data-t="26:26:00">[26:26:00]</a>. Quaternions describe a rigid motion of a hypersphere in 4D space [26:37:00] - <a class="yt-timestamp" data-t="26:41:00">[26:41:00]</a>. [[understanding_higher_dimensional_spheres_and_shapes | Further exploration of 4D motion]].
*   **Sphere Packing**: In 24 dimensions, there's an unusually elegant way to pack spheres, which is directly tied to error correction codes used on spacecraft like Voyager [26:54:00] - <a class="yt-timestamp" data-t="27:09:00">[27:09:00]</a>.
*   **Random Vectors**: In very high dimensions, random vectors have a high probability of being nearly perpendicular [27:09:00] - <a class="yt-timestamp" data-t="27:21:00">[27:21:00]</a>. This fact is relevant to neural networks, explaining the improved performance of large language models at scale, and to various compression algorithms [27:21:00] - <a class="yt-timestamp" data-t="27:32:00">[27:32:00]</a>.

## Intuition vs. Analysis in Higher Dimensions

While higher dimensions offer powerful analytical tools, there's a distinction between **analysis** (logical rigor) and **intuition** (mental visualization and guiding insights) [27:37:00] - <a class="yt-timestamp" data-t="27:41:00">[27:41:00]</a>. For 2D problems solved with 3D insights, people can often intuitively visualize the transformation (e.g., rhombus tiling as cube stacks, circle strips on a hemisphere, intersecting planes for tangents) [27:41:00] - <a class="yt-timestamp" data-t="28:11:00">[28:11:00]</a>.

However, [[geometric_reasoning_in_higher_dimensions | problems using even higher dimensions]] often rely purely on analysis, as human intuition struggles to visualize four or more dimensions [28:11:00] - <a class="yt-timestamp" data-t="28:19:00">[28:19:00]</a>. While analogies might be drawn, the reasoning must be purely analytical [28:19:00] - <a class="yt-timestamp" data-t="28:28:00">[28:28:00]</a>. Analysis provides rigor, but intuition guides the exploration of possible solutions, which can be vast without such guidance [28:30:00] - <a class="yt-timestamp" data-t="28:52:00">[28:52:00]</a>. The challenge and inherent sadness lie in the possibility that there are 3D problems that could be easily solved with 4D intuition, which remains inaccessible to us [28:54:00] - <a class="yt-timestamp" data-t="29:04:00">[29:04:00]</a>.