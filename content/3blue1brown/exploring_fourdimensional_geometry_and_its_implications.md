---
title: Exploring fourdimensional geometry and its implications
videoId: piJkuavhV50
---

From: [[3blue1brown]] <br/> 

Mathematics often presents puzzles that seem intractable in their original dimension, only to reveal elegant solutions when viewed from a [[higher_dimensions_and_their_relevance | higher dimension]] <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. This article explores how [[geometry_in_higher_dimensions | higher-dimensional geometry]] can provide profound insights, culminating in a discussion of four-dimensional space and its unique challenges to human intuition.

## Leveraging Three Dimensions for Two-Dimensional Puzzles

The journey into [[higher_dimensions_and_their_relevance | higher dimensions]] often begins by observing how a step up from two to three dimensions can simplify complex problems:

### The Rhombus Tiling Puzzle
Consider a rhombus with internal angles of 60 and 120 degrees <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Copies of this shape can tile a plane in various ways, often forming pseudo-hexagonal patterns <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. A key "move" in this puzzle involves identifying three rhombuses forming a small hexagon and rotating them 60 degrees to generate a slightly different tiling <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

The puzzle asks if it's possible to get from any tiling of a finite hexagon (composed of these rhombuses) to any other tiling using only these hexagonal rotation steps <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

The insight comes from [[highdimensional_geometry_and_cube_coloring | suggestively coloring]] the tiles based on their orientation, allowing one to perceive the 2D tiling as a projection of a stack of cubes in three dimensions <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Any stack of cubes within an *n* x *n* x *n* frame produces one of these rhombus tiling patterns, and conversely, any tiling corresponds to a stack of cubes <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

The fundamental rotation move in the 2D puzzle is equivalent to adding or removing cubes from the 3D stack <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This transformation makes it clear that any pattern can be reached from any other (by emptying the stack and then rebuilding to the desired pattern) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. The maximum number of steps required to get from an empty configuration to a full one is *n* cubed <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. This numerical answer, involving a cube, directly indicates the inherent three-dimensionality of the problem <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### The Tarski-Planck Problem: Covering a Circle with Strips
This puzzle involves covering a unit circle with multiple "strips," defined as regions bounded by two parallel chords <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. The question is to find the minimum possible sum of the widths (*d*) of all these strips required to completely cover the circle <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. A simple solution using a single strip of width 2 (the diameter) or parallel strips yields a sum of 2 <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

Proving that 2 is the minimum is challenging in two dimensions because a strip's area is not directly proportional to its width without knowing its position <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. The key insight again involves stepping into three dimensions: Projecting the circle and its strips onto a hemisphere sitting above it <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. On this 3D hemisphere, the area of a projected strip happens to be *π* times its width (*d*), regardless of its position <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This fact is related to Archimedes' proof for the surface area of a sphere, where projecting areas onto a cylinder preserves them <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

If the strips cover the 2D circle, their 3D projections cover the hemisphere. The sum of the areas of these projected strips (Σ *πd*) must be at least the area of the hemisphere (2*π*) <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. Therefore, the sum of the widths (Σ*d*) must be at least 2 <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

### Tangent Points of Three Circles
This puzzle asks for a proof that the three intersection points of the external tangents drawn between each pair of three distinct circles in a plane always lie on a single line <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

The initial [[visualizing_transformations_in_three_dimensions | 3D intuition]] involves imagining each circle as the equator of a sphere <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. Around any pair of spheres, external tangents form a cone intersecting at a point <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. The key is to consider a plane tangent to all three spheres <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. This plane passes through the three intersection points because the lines connecting the tangency points on the plane are themselves external tangents to the spheres <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. Since these three points also lie on the original 2D plane of the circles, they must lie on the intersection of these two planes, which is a line <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

However, this argument has a limitation: it doesn't work if one sphere is significantly smaller and positioned in the middle, as a single plane cannot be tangent to all three <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

The proof can be saved by using cones instead of spheres, where each circle is the base of a cone with the same vertex angle <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. The intersection point of the external tangents between two circles is the "center of similarity" for their respective cones <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>. The line passing through the tips of any two cones also passes through their center of similarity <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. A plane can always be defined by the three tips of the cones <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. The intersection of this plane with the original 2D plane where the circles live forms the line containing the three centers of similarity (and thus the tangent intersection points) <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. This revised argument is more general and even applies when one circle is inside another <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. This principle applies not just to circles but to any three similar shapes in the same orientation <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.

## Stepping Up to Four Dimensions

The previous examples highlight how [[higher_dimensions_and_their_relevance | higher dimensions]] can provide insights. This leads to the question of whether a three-dimensional puzzle might require a four-dimensional solution.

### Volume of a Tetrahedron
One such puzzle is finding an explicit formula for the volume of a tetrahedron given the [[matrix_dimensions_and_their_geometric_interpretations | coordinates]] of its four vertices in three-dimensional space <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. A significant hint suggests that an elegant solution involves thinking about the determinant of a 4x4 matrix <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.

### Constructing a 4D Tiling Puzzle

Inspired by the rhombus tiling puzzle, one can try to construct its four-dimensional analog <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. This involves:

1.  **Representing a Cube**: A 3D cube's vertices can be defined by combinations of 0s and 1s for its (x, y, z) coordinates <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. Edges connect vertices that differ in only one coordinate <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.
2.  **Representing a Hypercube**: A 4D hypercube's vertices would similarly be lists of four numbers (0s and 1s) <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. Edges connect vertices differing in only one coordinate <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.
3.  **Projection**: The 2D rhombus tiling is a projection of a 3D cube (or stack) when staring down its diagonal <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. This involves projecting onto a plane perpendicular to the (1, 1, 1) [[vectors_in_two_and_three_dimensions | vector]] <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.
4.  **4D to 3D Projection**: Applying the same principle to a 4D hypercube, by projecting it onto a 3D subspace perpendicular to the (1, 1, 1, 1) [[vectors_in_two_and_three_dimensions | vector]], results in a beautiful and symmetric shape called a rhombic dodecahedron <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>. This shape is known to [[highdimensional_spheres | tessellate]] 3D space <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.
5.  **Analogous "Move"**: In the 2D puzzle, rotating the hexagon (three rhombuses) corresponds to adding or removing a cube in 3D <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>. The three rhombuses are projections of the three visible faces of the cube <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>. In 4D, the hypercube has "cubical cells" (analogous to 3D faces), and these project down as four squished cubes that form the rhombic dodecahedron <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>. The analogous move would involve sliding each of these four projected cubes through the origin, offering a distinct way to tile the rhombic dodecahedron <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>.

The constructed puzzle asks: if you tile a large rhombic dodecahedron with these "squished cube" shapes, and each time you find a small 1x1x1 rhombic dodecahedron, you make the "sliding through the middle" move, what is the maximum number of moves to get from one tiling to another <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>? The answer, derived from the 4D hypercube analogy, is *n* to the power of 4, where *n* is the side length of the large rhombic dodecahedron <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>.

## Broader Implications and the Sadness of Higher Dimensions

These puzzles illustrate a broader mathematical phenomenon: [[higher_dimensions_and_their_relevance | higher-dimensional constructs]] can be bizarrely relevant to solving problems in lower dimensions, or even non-geometric problems <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.

*   **Quaternions**: An extension of complex numbers, [[quaternion_multiplication_and_fourdimensional_geometry | quaternions]] naturally live in four dimensions and offer an elegant way to encode and work with three-dimensional rotations <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>. They describe a unique type of "extra rigidity" involving the rotation of a hypersphere in 4D <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
*   **Sphere Packing**: In 24 dimensions, there is an unusually elegant way to pack spheres, which is tied to error correction codes used on spacecraft <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>.
*   **Random Vectors**: In very [[higher_dimensions_and_their_relevance | high dimensions]], random [[vectors_in_two_and_three_dimensions | vectors]] tend to be nearly perpendicular, a fact relevant to neural networks and compression algorithms <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>.

However, the profound aspect of [[geometry_in_higher_dimensions | higher-dimensional geometry]] also carries a hint of sadness. While we can use analysis to prove concepts in [[higher_dimensions_and_their_relevance | higher dimensions]], our human intuition is fundamentally limited to three dimensions <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. We can "squint our eyes" and intuitively grasp the 2D-to-3D insights <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>, but stepping beyond three dimensions necessitates purely analytical reasoning <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.

Intuition acts as a guiding light, steering us through the vast space of logical possibilities towards a proof <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. The "sadness" arises from the thought that there might be incredibly elegant solutions to three-dimensional problems that remain inaccessible to us, requiring a four-dimensional (or higher) intuition that humans simply do not possess <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.