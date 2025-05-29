---
title: Mathematical proofs and logical deduction
videoId: IQqtsm-bBRU
---

From: [[3blue1brown]] <br/> 

Mathematical proofs often involve intricate [[logical_deduction|logical deduction]] to establish truths, sometimes relying on counter-intuitive concepts and abstract structures to solve problems <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. The process of engaging with challenging puzzles, even pure ones, sharpens problem-solving instincts applicable to other practical areas <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## The Inscribed Square Problem

A prominent unsolved question in mathematics, posed by Otto Toeplitz in 1911, is whether every closed continuous loop necessarily has an inscribed square <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. An inscribed square means four points on the loop form the vertices of a square <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This is known as the inscribed square problem <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### The Inscribed Rectangle Problem (A Simpler Version)

While the square problem remains unsolved for all curves, a beautiful proof exists for a simpler version: whether every closed continuous loop necessarily has an inscribed rectangle <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The argument for this, originally due to Herbert Vaughan, involves the concept of a [[klein_bottle|Klein bottle]] as a natural problem-solving tool <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

This proof provides significant insight into [[conceptualizing_mathematical_problems|conceptualizing mathematical problems]] and understanding the essence of topology <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Topology, in this context, is not merely the study of bizarre shapes or "rubber sheet geometry", but a field where shapes and their properties become tools for logic and deduction <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Reframing the Problem for Rectangles

The first step in the proof is to reframe the question <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>: instead of four rectangle vertices, search for two distinct pairs of points on the loop such that the lines connecting each pair have the same midpoint and the same length <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This condition necessarily forms a rectangle <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### The 3D Surface Representation

For any pair of points on a given closed loop, two pieces of information are relevant:
1.  The `xy` coordinates of their midpoint <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
2.  The distance between the two points (`d`) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

This three-number dataset (`x`, `y`, `d`) can be packaged as a single point in a three-dimensional space, where the distance `d` is represented as the `z`-coordinate <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
This process creates a continuous mapping from pairs of points on the loop to a unique point in 3D space <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. The property of this mapping being continuous means that slight adjustments to the input pair result in only slight adjustments to the output point <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

Searching for inscribed rectangles then becomes equivalent to searching for a "coincidence" where two distinct pairs of points map to the same output point in this 3D space <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. This coincidence typically appears as a self-intersection of the surface formed by all possible output points <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

*   For a circle, the output surface is a dome <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. Infinitely many pairs of points (forming rectangles) map to the single point at the top of the dome, representing the center and diameter of the circle <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   For an ellipse, this single point of many intersections becomes a vertical line of self-intersections <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

An important observation is that near the plane of the curve, the cross-sections of this 3D surface look approximately like the curve itself <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. This is because pairs of points that are very close together (or the same point listed twice) correspond to points on the curve itself, with a very small `z`-coordinate (distance) <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### The Möbius Strip and Unordered Pairs

To connect the 3D surface to a provable topological property, it's necessary to represent the input space – all possible *unordered* pairs of points on the loop <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

1.  **Coordinate System**: Assigning each point on the loop a number between 0 and 1 provides an internal coordinate system <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
2.  **Unit Square**: Pairs of points (x, y) can be represented as points in a unit square <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
3.  **Gluing Edges**: Because the loop connects at 0 and 1, the edges of the unit square (x=0 glued to x=1, and y=0 glued to y=1) are identified, which topologically forms a torus <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
4.  **Unordered Pairs**: Since (a,b) and (b,a) represent the same unordered pair, points (x,y) and (y,x) in the unit square must be considered the same <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. This requires "folding" the square along its diagonal <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
5.  **Formation of a Möbius Strip**: Through a sequence of cuts and glues on the folded square, this topological space ultimately forms a Möbius strip <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

The Möbius strip is a natural way to geometrically represent all possible unordered pairs of points on a loop, maintaining a two-way continuous association <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. The edge of this Möbius strip corresponds to pairs of points where x=x (i.e., the same point listed twice), which in the 3D surface representation means these points must land on the loop itself (the `xy`-plane, where distance `d=0`) <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.

### Connecting to the Klein Bottle and Proof

The problem then reduces to understanding whether a Möbius strip can be continuously mapped ("embedded") into 3D space such that its edge is confined to the `xy`-plane, and its interior remains strictly above the plane, *without self-intersection* <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

To further develop the proof, consider the reflection of the 3D surface (representing loop pairs) underneath the `xy`-plane <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. This combined surface (the original and its reflection) forms a new closed surface <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. Topologically, this is equivalent to gluing the edge of one Möbius strip to the edge of another <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>.

This gluing process, as demonstrated by the diagram of the unit square with identified edges, results in the formation of a [[klein_bottle|Klein bottle]] <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>.

### The Impossibility and Conclusion

A fundamental property of [[klein_bottle|Klein bottles]] is that they are impossible to properly represent in three dimensions without the surface intersecting itself <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. This is a general fact about any closed, non-orientable surface <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.

Since the constructed surface (and its reflection) must form a [[klein_bottle|Klein bottle]], and a [[klein_bottle|Klein bottle]] cannot exist in 3D without self-intersection, it logically follows that the original surface representing loop pairs must also have self-intersection <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>.

This self-intersection, by definition, means there are two distinct pairs of points on the original loop that map to the same point in 3D space, thus having the same midpoint and the same distance <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>. Therefore, they must form a rectangle <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>. This elegant proof demonstrates how abstract topological properties provide the [[logical_deduction|logical deduction]] needed to solve the problem.

### The Unsolved Square Problem Revisited

The unsolved inscribed square problem is harder, especially for "rough curves" (e.g., fractals) <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. If, in addition to midpoint and distance, one also tracks the angle of the line segment, the problem becomes finding two segments that share a midpoint and length and differ by 90 degrees <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. This would involve embedding [[moebius_strip|Möbius strips]] into four dimensions <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

For smooth curves, mathematicians Joshua Green and Andrew Lobb (2020) proved that not only can a square always be found, but rectangles of every possible aspect ratio can be found <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>. Their proof indeed involves embedding [[moebius_strip|Möbius strips]] and [[klein_bottle|Klein bottles]] into a four-dimensional space, leveraging the clean limiting behavior of angles for smooth curves <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.

### The Role of Topology in Proofs

This example highlights that mathematicians study shapes like [[moebius_strip|Möbius strips]] and [[klein_bottle|Klein bottles]] not for their inherent bizarreness, but because they serve as crucial tools in [[mathematical_proofs_and_logical_deduction|mathematical proofs]] and [[logical_deduction|logical deduction]] <a class="yt-timestamp" data-t="00:25:13">[00:25:13]</a>. A topological space is not a single shape, but an infinite family of shapes connected by continuous equivalence <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>. Topology is about understanding continuous associations and what is or is not possible under those associations <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.

The excitement around [[paradoxical_and_nonintuitive_mathematical_truths|bizarre properties]] and impossibilities in topology is not merely aesthetic; when seeking [[mathematical_proofs_and_logical_deduction|logical proofs]], constraints and impossibilities are fundamental to progress <a class="yt-timestamp" data-t="00:26:50">[00:26:50]</a>.