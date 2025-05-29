---
title: Mathematical intuition versus analysis
videoId: piJkuavhV50
---

From: [[3blue1brown]] <br/> 

Mathematical problem-solving often relies on a blend of analytical rigor and intuitive understanding <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. While analysis provides the necessary rigor and logical steps for a proof <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>, intuition acts as a "guiding light" <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>, suggesting which paths are worth exploring in the vast space of possible logical moves <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>. This concept is beautifully illustrated through geometric puzzles that benefit from considering higher dimensions <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

## The Power of Higher-Dimensional Intuition

Many two-dimensional (2D) geometric problems can be simplified and solved more elegantly by visualizing them within a three-dimensional (3D) space <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. This [[converting_analytic_reasoning_to_geometric_intuition | conversion of analytic reasoning to geometric intuition]] offers powerful [[mathematical_insights_and_elegant_solutions | mathematical insights and elegant solutions]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

### Rhombus Tiling Puzzle

One puzzle involves tiling an infinite plane or a finite hexagon with specific rhombus shapes that have internal angles of 60 and 120 degrees <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. A key move in this puzzle is rotating a small hexagon formed by three rhombuses by 60 degrees <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The question is whether any tiling pattern can be reached from another using these hexagonal rotation steps <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

The answer is no for an infinite plane because some patterns, like a squished rectangular grid, contain no hexagons, preventing movement into or out of them <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. However, for a finite hexagon tiling, the problem becomes much clearer by projecting it onto a stack of cubes in 3D <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Intuition from 3D:** Each rhombus tiling pattern corresponds to a stack of cubes <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. The 60-degree rotation of a hexagon is equivalent to adding or removing a cube from this stack <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Solution:** This insight reveals that any pattern can be reached from any other by simply adding or removing cubes <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. The maximum number of moves required to go from an empty configuration to a full one in an *n* x *n* x *n* frame is *n* cubed <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. The appearance of "n cubed" in the numerical answer reinforces the inherent three-dimensionality of the problem <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### The Tarski-Planck Problem (Covering a Circle with Strips)

This puzzle asks for the minimum sum of widths for strips that completely cover a unit circle <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. A trivial solution is a single strip with a width of 2 (the diameter), resulting in a sum of 2 <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. The challenge is to determine if a smaller sum is possible <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

*   **Intuition from 3D:** While the area of a strip in 2D is not directly proportional to its width, this relationship becomes true if the strips are projected onto a hemisphere sitting above the circle <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. The area of such a projected strip in 3D is pi times its width (πd), regardless of its position on the hemisphere <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This is related to Archimedes' proof for the surface area of a sphere <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, which states that projecting areas onto a cylinder preserves them <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   **Solution:** If the strips cover the circle, their projections must cover the hemisphere <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. The sum of the areas of these projected strips must be at least the area of the hemisphere, which is 2π <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Since the sum of areas is Σ(πd) = πΣd, it follows that πΣd ≥ 2π, meaning the sum of the widths (Σd) can never be below 2 <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. This [[visual_intuition_in_calculus | visual intuition]] from 3D space simplifies the proof <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### Three Circles Problem (Radical Axis Theorem)

The problem states that if you have three circles in 2D space, the three intersection points of the external tangents drawn between each pair of circles always lie on a single line <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This is known as the Radical Axis Theorem. Initial attempts to prove this by considering a plane resting on top of three spheres (where circles are their equators) are partially valid but fail if one circle is significantly smaller than the others <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

*   **Refined Intuition from 3D:** A more robust approach involves using cones instead of spheres <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Each circle is the base of a cone, and all three cones have the same angle at their tips <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. The intersection point of the external tangents of two circles is the "center of similarity" for those two shapes <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>. The line passing through the tips of any two cones also passes through this center of similarity <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
*   **Solution:** The three tips of the cones uniquely determine a plane in 3D space <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. This plane intersects the original 2D plane (where the circles reside) along a line <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. Since the centers of similarity (the intersection points of tangents) lie on the lines connecting the cone tips, and those lines lie on the plane formed by the cone tips, the intersection points must lie on the intersection line of the two planes <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. This argument holds universally, even if one circle is inside another <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>, and it generalizes to any three similar shapes <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.

## Extending to Even Higher Dimensions

While 3D intuition can aid 2D problems, the jump to four or more dimensions presents significant challenges for human visualization <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.

### Volume of a Tetrahedron

A common puzzle involves finding an explicit formula for the volume of a tetrahedron given the coordinates of its four vertices in 3D space <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. A major spoiler is that an elegant solution involves the determinant of a 4x4 matrix <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. This problem is analogous to finding the area of a triangle from its 2D corner coordinates using a 3x3 determinant <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. The relationship between determinants and volumes/areas is a key insight in linear algebra <a class="yt-timestamp" data-t="00:18:35">[00:18:35]</a>.

### Constructing a 3D Puzzle from 4D Intuition

The challenge here is to create a 3D tiling puzzle that a hypothetical 4D creature could intuit as a stack of 4D hypercubes <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.
*   **Hypercube Projection:** A 4D hypercube can be defined by vertices with coordinates consisting of 0s and 1s <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. Projecting this hypercube along its main diagonal (the 1,1,1,1 vector) into a 3D subspace results in a beautiful, symmetric shape called a rhombic dodecahedron <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>. This shape is known to tessellate 3D space <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.
*   **The Analogy:** Just as the 2D rhombus tiling projected from 3D cubes showed 3 rhombuses forming a hexagon <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>, the 3D projection of a 4D hypercube consists of four "cubical cells" (squished cubes) that fit together to form the rhombic dodecahedron <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>. The "move" in the 3D puzzle involves sliding these constituent squished cubes through their common origin <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>.
*   **The Absurd Puzzle:** The puzzle asks for the maximum number of moves to get from one tiling of a large rhombic dodecahedron (side length *n*) with small squished cubes to another <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>.
*   **Solution:** Knowing this is a projection of hypercubes, the answer is *n* to the power of 4 (*n*<sup>4</sup>) <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>, reflecting the 4D nature of the underlying concept.

## Beyond Geometric Intuition

The principle of leveraging higher dimensions extends beyond geometry:
*   **Quaternions:** These extensions of complex numbers naturally reside in four dimensions and offer an elegant way to encode and work with 3D rotations, performing a kind of "extra rigidity" rotation of a hypersphere <a class="yt-timestamp" data-t="00:26:15">[00:26:15]</a>.
*   **Sphere Packing in 24 Dimensions:** An unusually elegant way to pack spheres together in 24 dimensions is related to error correction codes used on Voyager spacecrafts <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>.
*   **Random Vectors in High Dimensions:** In very high dimensions, random vectors have a high chance of being nearly perpendicular <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>. This fact is relevant to large language models (neural networks) and compression algorithms <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.

## The Sadness of Lost Intuition

While higher dimensions offer powerful analytical tools, there's a distinction between analysis and [[converting_analytic_reasoning_to_geometric_intuition | intuition]] <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. For 2D problems that map to 3D, humans can often "squint their eyes" and genuinely picture the higher-dimensional analogy <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>. We can visualize a line as the intersection of two planes in 3D space <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>.

However, for problems requiring insights from four or more dimensions, true intuition often becomes inaccessible <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>. While analogies to lower dimensions might exist, the reasoning ultimately relies on pure analysis <a class="yt-timestamp" data-t="00:28:19">[00:28:19]</a>.
*   **Analysis without Intuition:** Although all mathematical rigor comes from analysis <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>, conducting analysis without [[conceptualizing_mathematical_problems | conceptualizing mathematical problems]] through intuition is "daunting" <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>. The sheer volume of logical moves possible for a proof can be too vast to explore without guidance <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>.
*   **Inaccessible Insights:** The "sadness" lies in the thought that there might be 3D problems whose solutions become clear with a 4D (or higher) intuition that is simply beyond human grasp <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>. These "guiding lights" remain inaccessible to creatures limited to three spatial dimensions <a class="yt-timestamp" data-t="00:29:04">[00:29:04]</a>.

For additional related problems, a bonus video explores two more 2D puzzles with 3D solutions <a class="yt-timestamp" data-t="00:29:15">[00:29:15]</a>.