---
title: Mathematical proofs involving inscribed rectangles
videoId: IQqtsm-bBRU
---

From: [[3blue1brown]] <br/> 

The question of whether every closed continuous loop necessarily has an inscribed square is an unsolved problem originally posed by Otto Toeplitz in 1911, and it is commonly known as [[the_inscribed_square_problem | the inscribed square problem]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. While the square problem remains open, a beautiful proof exists for a simpler version of this question: whether every closed continuous loop necessarily has an inscribed rectangle <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This argument is originally due to Herbert Vaughan <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Why Study Inscribed Rectangles?

While there might not be a direct practical application for proving that any closed loop has an inscribed rectangle, engaging with such pure puzzles sharpens problem-solving instincts that can be carried over to other practical applications <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This particular proof offers a profound insight into topology, illustrating how abstract shapes and their properties can be powerful tools for logic and deduction, rather than just bizarre curiosities <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Topology is understood as the study of continuous associations and what is or is not possible under those associations <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.

## Proof for Inscribed Rectangles

The proof for inscribed rectangles involves reframing the problem and constructing specific topological spaces to demonstrate that a collision (and thus, a rectangle) must occur.

### Reframing the Problem
Instead of searching for four points forming a rectangle, the problem is reframed as searching for two distinct pairs of points on the loop, such that the line segments connecting each pair have the same midpoint and the same length <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. If two line segments share the same center and length, their four endpoints must form a rectangle <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### The 3D Output Surface
For any pair of points on a given closed loop, two pieces of data are important:
1.  **Midpoint:** The (x, y) coordinates of the midpoint of the segment connecting the two points <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
2.  **Distance:** The distance (d) between the two points <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

These three numbers (x, y, d) can be packaged as a single point in a three-dimensional space <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. This creates a continuous mapping from pairs of points on the loop to a unique surface in 3D space <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. An "inscribed rectangle" corresponds to two distinct pairs of points on the loop mapping to the same output point in this 3D space, meaning the surface "self-intersects" <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

For a circular loop, the resulting 3D surface is a dome <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. While it appears to have no self-intersection, the center point on top of the dome represents infinitely many inscribed rectangles (all having the circle's center as their midpoint and the diameter as their diagonal length) <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. When a circle is squished into an [[Geometry_of_ellipses | ellipse]], this single point expands into a vertical line of self-intersections <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

A crucial observation is that if a pair of points on the loop is "really just the same spot," the output of this mapping is that same point on the curve, lying on the xy-plane (where z=0) <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. This means the edge of the constructed surface must lie on the loop itself in the xy-plane <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### The Möbius Strip and Klein Bottle
The next step involves a second, natural way to associate pairs of points on a loop with a surface <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. By representing each point on the loop with a number between 0 and 1 (with 0 and 1 mapping to the same point), a pair of points can be represented by a point in a unit square <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

To account for the loop's continuous nature (0 and 1 are the same point), the edges of the unit square are "glued." Gluing the x-coordinate edges (x=0 to x=1) creates a tube <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. Gluing the y-coordinate edges (y=0 to y=1) by curling the tube results in a torus (donut shape) <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. This torus represents all *ordered* pairs of points on the loop <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

However, for inscribed rectangles, the order of points in a pair does not matter (a,b is the same as b,a) <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. This means points (x,y) and (y,x) in the unit square must be considered the same <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This is achieved by "folding" the square along its diagonal, like a grilled cheese sandwich <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. After this fold and further gluing, the resulting surface is a [[Möbius strip]] <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. The edge of this [[Möbius strip]] (the diagonal x=x) represents pairs where both points are the same <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.

There is a continuous function from this [[Möbius strip]] (representing unordered pairs of points) onto the 3D surface constructed earlier (representing midpoints and distances) <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. The key insight is that the edge of the [[Möbius strip]] (where x=x) must map to the original loop itself, confined to the xy-plane <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.

It is impossible to embed a [[Möbius strip]] into 3D space such that its boundary is confined to a plane and its interior is strictly above that plane, without the surface somehow crossing through itself <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. This self-intersection means that two distinct points from the [[Möbius strip]] map to the same point on the 3D surface, which in turn means two distinct pairs of points have the same midpoint and distance, forming an inscribed rectangle <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.

To further support this, consider the reflection of the 3D surface underneath the xy-plane <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. Gluing this reflected surface to the original surface along their common boundary (the original loop) creates a new closed surface <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. This new surface is equivalent to gluing together the edges of two [[Möbius strip | Möbius strips]] <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>. The result of gluing two [[Möbius strip | Möbius strips]] together in this manner is a [[Klein bottle]] <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>.

A fundamental property of the [[Klein bottle]] is that it is impossible to represent it properly in three dimensions without it intersecting itself <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. This general fact applies to any closed, non-orientable surface <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>. Since the constructed surface (plus its reflection) must form a [[Klein bottle]] which cannot be embedded in 3D without self-intersection, the original surface must also exhibit self-intersection, proving the existence of inscribed rectangles <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>.

## The Unsolved Inscribed Square Problem

The original [[inscribed square problem]] (proving every loop has an inscribed square) remains unsolved <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. A natural extension of the rectangle proof would be to also record the angle of the line segment connecting the pair of points <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>. If two segments share a midpoint, length, and differ by 90 degrees, they form a square <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. This would involve embedding [[Möbius strip | Möbius strips]] into four dimensions, as there are now four numbers (x, y, d, angle) to track <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

In 2020, mathematicians Joshua Green and Andrew Lobb proved an extension for *smooth curves* (curves where derivatives can be taken infinitely many times), showing that for these curves, not only can a square always be found, but rectangles of every possible aspect ratio can be found <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. Their paper involves embedding [[Möbius strip | Möbius strips]] and [[Klein bottle | Klein bottles]] into a four-dimensional space <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.

The difficulty in solving the [[inscribed square problem]] for *all* curves lies in the "rough curves" like fractals <a class="yt-timestamp" data-t="00:25:02">[00:25:02]</a>. For smooth curves, the angle of the line connecting two points has a clean limiting behavior as the points get closer (approaching the tangent line angle) <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>. However, for rough curves, this limiting behavior for the angle might not exist, complicating the proof <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>.

## Topology as a Problem-Solving Tool
This proof illustrates how abstract mathematical objects like [[Möbius strip | Möbius strips]] and [[Klein bottle | Klein bottles]] are not merely curiosities but are fundamental tools in logical deduction and [[creative_approaches_in_mathematical_proofs | creative approaches in mathematical proofs]] <a class="yt-timestamp" data-t="00:25:13">[00:25:13]</a>. The "bizarre" properties and impossibilities within topology, such as the non-embeddability of certain surfaces in lower dimensions, provide the necessary constraints and "fuel for progress" in constructing proofs <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>. This highlights the [[role_of_visual_reasoning_in_mathematical_proofs | role of visual reasoning]] and abstract thinking in mathematics.