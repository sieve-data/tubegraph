---
title: The inscribed square problem
videoId: IQqtsm-bBRU
---

From: [[3blue1brown]] <br/> 

The [[inscribed_square_problem | inscribed square problem]] asks whether every closed continuous loop necessarily contains an inscribed square <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. An inscribed square is defined as four points on the loop that form the vertices of a square <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This question was originally posed by Otto Toeplitz in 1911 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a> and remains unsolved <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## The Inscribed Rectangle Problem

A simpler version of the [[inscribed_square_problem | inscribed square problem]] asks whether every closed continuous loop necessarily has an inscribed rectangle <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This problem *has* a beautiful proof, originally due to Herbert Vaughan <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. While there are no known practical applications for proving this, engaging with such pure [[problemsolving_strategies_in_mathematical_puzzles | mathematical puzzles]] sharpens problem-solving instincts <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. More specifically, this proof provides a deep insight into the nature of topology <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

> [!INFO] What is Topology?
> Topology is often presented as the study of bizarre shapes (like a Möbius strip) or as "rubber sheet geometry" where shapes are considered the same if they can be deformed into one another without tearing <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. However, these notions may not fully capture its essence. This proof demonstrates how seemingly bizarre shapes and their properties become tools for logic and deduction <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Topology is about understanding continuous associations between things and what is or is not possible under those associations <a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a>.

### Reframing the Question

To prove the existence of an inscribed rectangle, the problem is reframed: instead of searching for four points forming a rectangle, search for two distinct pairs of points on the loop such that the lines connecting each pair have the same midpoint and the same length <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. The four endpoints of these two line segments will necessarily form a rectangle <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Mapping Pairs of Points to 3D Space

For any pair of points on the loop, two pieces of information are relevant:
1.  The `xy` coordinates of their midpoint <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
2.  The distance `d` between them <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

These three numbers (`x`, `y`, `d`) can be packaged together as a single point in a three-dimensional space <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. This creates a continuous mapping from pairs of points on the loop to points in 3D space <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. The search for inscribed rectangles then becomes a search for "coincidences" or "collisions" where two distinct pairs of points map to the same output point in this 3D space <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

### The "Output" Surface

The set of all possible outputs from this mapping forms a complex surface in 3D space <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   Near the plane of the original loop, cross-sections of this surface look approximately like the loop itself <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. This is because pairs of points very close together have a small `d` (z-coordinate) and their midpoint is near both points <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Specifically, pairs of identical points `(x,x)` map to the point `x` on the loop itself (where `d=0`) <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   An inscribed rectangle corresponds to points of "self-intersection" on this surface <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>, where two different input pairs map to the same output point.

#### Examples of the Output Surface:
*   **Circle**: For a circle, the output surface looks like a dome <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. The "self-intersection" occurs at the very top of the dome, where infinitely many pairs of points (all diagonals of inscribed rectangles) map to the single point representing the circle's center and diameter <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **Ellipse**: If the circle is squished into an [[geometry_of_ellipses | ellipse]], the single point of many intersections becomes a vertical line of self-intersections <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

## The "Input" Space: A Möbius Strip

To understand how self-intersection *must* happen, mathematicians create a second, abstract surface that represents all possible pairs of points on the loop.

1.  **Coordinates**: Assign each point on the loop a number between 0 and 1 <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. A pair of points (x, y) can then be represented as a point in a unit square <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
2.  **Loop Gluing**: Since 0 and 1 map to the same point on the loop, the edges of the square corresponding to `x=0` and `x=1` must be glued together, and similarly for `y=0` and `y=1` <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. This results in a torus (donut shape) <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
3.  **Unordered Pairs**: However, the problem requires unordered pairs of points (meaning `a,b` is the same as `b,a`) to avoid trivial solutions (infinitely thin rectangles) <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. This means points `(x,y)` in the square should be considered the same as `(y,x)` <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. Geometrically, this involves folding the square along its diagonal line (`x=y`) <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
    *   The points on the diagonal `(x,x)` (where `x` is the same point listed twice) form a special "red edge" <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
    *   After the fold and further topological manipulation (cutting and regluing), this process naturally yields a Möbius strip <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

> [!NOTE] The Möbius Strip
> The Möbius strip is a geometric representation of all possible unordered pairs of points on a loop <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. It's a continuous, two-way association <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. The red edge of the Möbius strip corresponds to all pairs `(x,x)` (the same point listed twice) <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

## The Proof of Inscribed Rectangles

There is a continuous function from this Möbius strip (representing all unordered pairs of points) onto the 3D output surface (representing their midpoints and distances) <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.

A critical constraint is that the red edge of the Möbius strip (representing pairs like `(x,x)`) must map to the original loop itself, which lies on the xy-plane <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. Furthermore, by definition, the distance `d` (z-coordinate) is always positive, so the interior of the output surface must lie strictly *above* the xy-plane <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

The core of the proof relies on the topological property that it is impossible to embed a Möbius strip into 3D space such that its edge is confined to a plane, and its interior is strictly *above* that plane, without the surface somehow crossing through itself (self-intersection) <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

*   **Clarification on Embedding**: While a Möbius strip *can* be embedded with a planar circular boundary (as shown by mathematician Dan Asimov) <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>, such an embedding allows the interior of the strip to go *both* above and below the plane <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. This does not satisfy the conditions of the problem.

### The Klein Bottle Connection

Consider the 3D output surface together with its reflection underneath the xy-plane <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. This combined surface is formed by gluing the edge of one Möbius strip to the edge of another <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>. Topologically, gluing two Möbius strips edge-to-edge results in a [[tarski_planck_problem_and_circle_coverings | Klein bottle]] <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.

The [[tarski_planck_problem_and_circle_coverings | Klein bottle]] is a famous shape that cannot be properly represented in three dimensions without somehow intersecting itself <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. This is a general property of any closed, non-orientable surface <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.

Since the combined surface (the output surface and its reflection) is a [[tarski_plank_problem_and_circle_coverings | Klein bottle]] and cannot be embedded in 3D without self-intersection, the original output surface (which is half of the Klein bottle) must also exhibit self-intersection when constrained to remain above the plane <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>. This self-intersection means there are two distinct pairs of points on the loop that map to the same output (same midpoint and distance), thus proving the existence of an inscribed rectangle <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.

> [!NOTE] [[mathematical_proofs_involving_inscribed_rectangles | Mathematical proofs involving inscribed rectangles]] for closed curves are a classic example of applying advanced topology to seemingly simple [[geometry_puzzles_involving_tiling_and_shapes | geometry puzzles involving tiling and shapes]].

## The Unsolved Inscribed Square Problem Revisited

To prove the [[inscribed_square_problem | inscribed square problem]], one might extend the approach by also tracking the angle of the line segment connecting a pair of points <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>. If two segments share a midpoint and length, and their angles differ by 90 degrees, they would form a square <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. This introduces a fourth piece of information, suggesting thinking about embeddings into four-dimensional space <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

In 2020, mathematicians Joshua Green and Andrew Lobb proved a significant extension for *smooth* curves (curves where derivatives can be taken infinitely many times) <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. They showed that for smooth curves, not only can inscribed squares always be found, but rectangles of every possible aspect ratio can be found <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>. Their proof involves embedding Möbius strips and Klein bottles into a four-dimensional space <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.

The challenge of the general [[inscribed_square_problem | inscribed square problem]] lies with "rough" curves, like fractals, where the angle of a line segment might not have a clean limiting behavior as points get arbitrarily close <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>.

> [!SUMMARY] Key Takeaways
> *   Topology is not just about bizarre shapes, but provides tools for logic and deduction, often using "constraints and impossibilities" as fuel for mathematical progress <a class="yt-timestamp" data-t="00:25:22">[00:25:22]</a>.
> *   A "Möbius strip" (or other topological space) is not a single particular shape but an infinite family of shapes connected by a notion of continuous equivalence <a class="yt-timestamp" data-t="00:25:42">[00:25:42]</a>.
> *   The [[spatial_intuition_in_math | spatial intuition in math]] developed through these puzzles can be applied to other areas, such as understanding musical intervals or solving other [[problemsolving_strategies_in_mathematical_puzzles | problemsolving strategies in mathematical puzzles]] like [[mosers_circle_problem | Moser's Circle Problem]] or [[the_impossible_chessboard_prisoner_puzzle | The Impossible Chessboard Prisoner Puzzle]].