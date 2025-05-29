---
title: Higher dimensions and their relevance
videoId: piJkuavhV50
---

From: [[3blue1brown]] <br/> 

The study of higher dimensions often reveals surprising insights and elegant solutions to problems that initially appear to be purely two-dimensional or three-dimensional. This phenomenon highlights how mathematical constructs in higher dimensions can simplify complex problems or provide a new intuitive framework for understanding them <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Two-Dimensional Puzzles Solved with Three-Dimensional Intuition

Many puzzles initially presented in two dimensions can be profoundly simplified by considering their analogues in three dimensions.

### The Rhombus Tiling Puzzle

Consider a rhombus with internal angles of 60 and 120 degrees <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Copies of this rhombus can tile an infinite plane in various ways, but some patterns, like a squished rectangular grid, contain no small hexagons that could be rotated <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

The puzzle shifts to tiling a finite hexagon (with side length `n`, using tiles of side length 1) and asks if it's possible to transform any tiling pattern into any other by rotating hexagonal clusters of three rhombuses <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. If so, what is the maximum number of moves required as a function of `n` <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>?

By coloring the tiles based on their orientation, one can visualize this 2D tiling as a [[highdimensional_geometry_and_cube_coloring | projection of a stack of cubes]] in 3D space <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. The fundamental move of rotating a hexagon of three rhombuses corresponds to adding or removing a small cube from this stack <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

*   **Solution**: Any pattern can be reached from any other by removing all cubes to reach an "empty" state, then adding the necessary cubes for the target pattern <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **Maximum Moves**: The maximum number of moves involves going from an empty configuration to a fully filled one, which corresponds to `n` cubed steps <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This `n` cubed answer directly reflects the underlying three-dimensionality of the problem <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

### The Tarski-Planck Problem: Covering a Unit Circle with Strips

This puzzle asks for the minimum possible sum of widths `d` when a unit circle is completely covered by multiple strips (regions bounded by two parallel chords) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. A simple covering using one fat strip of width 2 (the diameter) yields a sum of 2 <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

The key insight involves projecting the 2D problem into 3D. When these strips are projected onto a hemisphere sitting above the circle, the area of each strip in 3D becomes directly proportional to its width (`πd`) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. This fact is related to Archimedes' proof for the surface area of a sphere, where projecting areas from a sphere onto an encompassing cylinder preserves their area <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

*   **Solution**: If the 2D strips cover the circle, their 3D projections must cover the hemisphere <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. The sum of the projected areas (Σ `πd`) must be at least the area of the hemisphere (2π) <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   **Minimum Sum**: Therefore, the sum of the widths (Σ`d`) must be at least 2 <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This demonstrates how a 3D perspective clarifies a difficult 2D geometric problem <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### Three Circles and External Tangents

Given three distinct circles in a 2D plane, the puzzle (known as Monge's Theorem or a special case of Desargues' Theorem) states that the three intersection points of their external tangents always fall on the same line <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

An initial attempt to solve this involves imagining each circle as the equator of a sphere in 3D <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. A plane resting on top of all three spheres would intersect the original plane (where the circles lie) along the line containing the three intersection points <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. However, this argument fails if one sphere is small and located in the middle, as no single plane can rest on all three <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

The refined argument uses cones instead of spheres. Imagine three cones, each with a base at one of the circles and the same angle at the top <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. The intersection point of the external tangents of two circles is the "center of similarity" for those two shapes <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. The line passing through the tips of any two cones will also pass through their corresponding center of similarity <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.

*   **Solution**: The three tips of the cones uniquely determine a plane in 3D space <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. This plane intersects the original 2D plane along a line, and since the centers of similarity (the points of interest) lie on both planes, they must lie on this intersection line <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Generalization**: This approach is robust and works even when one circle is inside another, as the concept of a center of similarity still applies <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. It also generalizes to any three similar shapes in the same orientation <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.

## Attempting Three-Dimensional Puzzles with Four-Dimensional Intuition

The success of using 3D intuition for 2D problems naturally leads to questions about whether 4D (or higher) intuition can aid 3D problems <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.

### Volume of a Tetrahedron

The challenge is to write an explicit formula for the volume of a tetrahedron given the coordinates of its four vertices in 3D space <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This problem has an elegant solution involving the [[matrix_dimensions_and_their_geometric_interpretations | determinant of a certain 4x4 matrix]] <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>, analogous to finding the area of a triangle using a 3x3 determinant based on 2D coordinates <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

### Tiling with Projections of Hypercubes

Inspired by the rhombus tiling, one can attempt to construct a 3D tiling puzzle that a 4D creature might intuitively solve by seeing it as a stack of 4D hypercubes <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

A 4D hypercube can be defined by vertices with coordinates consisting of 0s and 1s, and edges connecting vertices that differ in only one coordinate <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. Projecting a 4D hypercube along its main diagonal (the 1,1,1,1 vector) onto a 3D subspace results in a beautiful and symmetric shape known as a rhombic dodecahedron <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>. This shape can tessellate 3D space <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

The cells of the hypercube (its 3D "faces") project down to squished cube shapes that fit together to form the rhombic dodecahedron <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>. The equivalent of the 2D rhombus rotation move is to allow each of these projected 3D cubical cells to "slide through the origin" <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>.

*   **The Puzzle**: How many moves does it take to get from one tiling of a large rhombic dodecahedron (side length `n`) with these smaller rhombic dodecahedra to another, using the "sliding through the origin" move <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>?
*   **Solution**: If understood as a projection of a stack of hypercubes, the answer is `n` to the power of 4 <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>.

## Broader Relevance and the Limits of Intuition

The puzzles demonstrate a broader mathematical phenomenon: higher-dimensional constructs can be surprisingly relevant to solving problems in lower dimensions, or even problems that don't initially appear geometric <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.

*   **[[Quaternion multiplication and fourdimensional geometry | Quaternions]]**: These numbers naturally live in four dimensions and offer an elegant way to encode and work with 3D rotations <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>. They represent a unique kind of "extra rigidity" in [[exploring_fourdimensional_geometry_and_its_implications | 4D hyperspheres]] <a class="yt-timestamp" data-t="00:26:37">[00:26:37]</a>.
*   **[[Highdimensional spheres | Sphere Packing in 24 Dimensions]]**: There's an unusually elegant way to pack spheres together in 24 dimensions, which is closely tied to error correction codes used on Voyager spacecraft <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>.
*   **[[Geometry in higher dimensions | Statistics of Random Vectors]]**: In very high dimensions, random vectors have a very high chance of being nearly perpendicular <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>. This fact is relevant to large language models and compression algorithms <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.

While analysis is crucial for mathematical rigor, intuition provides the "guiding lights" for exploring possible solutions <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. The inherent sadness of higher dimensions is the lack of direct human intuition beyond three dimensions <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. While we can analyze higher dimensions, we cannot "picture" them in our mind's eye in the same way we can visualize planes intersecting in 3D space <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. This means insights that might be obvious to a creature capable of perceiving four or more dimensions remain inaccessible to us through direct intuition <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.