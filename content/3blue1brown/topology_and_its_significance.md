---
title: Topology and its significance
videoId: IQqtsm-bBRU
---

From: [[3blue1brown]] <br/> 

The field of [[introduction_to_topology|topology]] is often introduced through abstract concepts like [[topological_surfaces_and_their_properties|Möbius strips]] or the idea of "rubber sheet geometry." While these demonstrations can seem disconnected from practical problem-solving, [[topology]] offers powerful tools for logical deduction and understanding continuous associations between diverse elements <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. This becomes evident when exploring complex mathematical puzzles, such as the inscribed rectangle problem.

## The Inscribed Rectangle Problem

The inscribed square problem, originally posed by Otto Toeplitz in 1911, asks whether every closed continuous loop necessarily contains four points that form the vertices of a square <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This question remains unsolved <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. However, a related, simpler version — proving that every closed continuous loop necessarily has an inscribed rectangle — has a beautiful proof attributed to Herbert Vaughan <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>. This proof highlights how seemingly bizarre [[topological_surfaces_and_their_properties|shapes]] become natural problem-solving tools <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.

### Reframing the Problem

To prove the existence of an inscribed rectangle, the question is reframed: instead of searching for four points forming a rectangle, one searches for two distinct pairs of points on the loop where the line segments connecting them have the same midpoint and the same length <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. If such pairs exist, their four endpoints must form a rectangle <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

### Mapping Loop Pairs to 3D Space

For any pair of points on a given loop, two pieces of information are relevant:
1.  **Midpoint Coordinates (x, y):** The location of the midpoint in the plane where the loop resides <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.
2.  **Distance (d):** The distance between the two points in the pair <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.

These three numbers (x, y, d) can be packaged as a single point (x, y, z) in a three-dimensional space, where z corresponds to the distance `d` <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. This creates a continuous mapping from pairs of points on the loop to points in 3D space, meaning slight changes in the input pair result in only slight changes in the output 3D point <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

The set of all possible outputs from this mapping forms a complex "wild surface" in 3D space <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>. An inscribed rectangle corresponds to a "collision" or "self-intersection" on this surface, where two distinct pairs of points map to the same output 3D point <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. For instance, a circular loop maps to a dome-like surface where the top represents infinitely many inscribed rectangles <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>. An elliptical loop maps to a surface with a vertical line of self-intersections <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.

### Representing Unordered Pairs with a [[role_of_mbius_strip_in_topology|Möbius Strip]]

To prove that such a self-intersection must always occur, mathematicians turn to a different, natural way to represent pairs of points on a loop:

1.  **Loop Coordinates:** Points on the loop are assigned a number between 0 and 1, where 0 and 1 represent the same point (as if the loop were snipped and flattened) <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>.
2.  **Pair Coordinates:** A pair of points (P1, P2) on the loop corresponds to a point (x, y) in a unit square, where x is P1's coordinate and y is P2's coordinate <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.
3.  **Gluing for Continuity:** Since 0 and 1 are the same point on the loop, the edges of the unit square must be "glued" to reflect this. Gluing opposite edges (x=0 to x=1, and y=0 to y=1) results in a torus (donut shape) <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>. This torus continuously represents *ordered* pairs of points on the loop <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>.
4.  **Unordered Pairs and the [[role_of_mbius_strip_in_topology|Möbius Strip]]:** For the inscribed rectangle problem, the order of points in a pair doesn't matter (e.g., A,B is the same as B,A) <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>. To represent unordered pairs, every point (x,y) in the unit square must be considered the same as (y,x). Geometrically, this means folding the square along its main diagonal <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>. This folding, combined with the original edge gluings, results in a [[role_of_mbius_strip_in_topology|Möbius strip]] <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>. The edge of this [[role_of_mbius_strip_in_topology|Möbius strip]] corresponds to pairs where both points are the same (x,x), which was the diagonal of the unit square <a class="yt-timestamp" data-t="16:35:00">[16:35:00]</a>.

### The Proof through [[Topological Surfaces and Their Properties|Non-Orientable Surfaces]]

There is a continuous function from the [[role_of_mbius_strip_in_topology|Möbius strip]] (representing all unordered pairs of points) to the 3D surface (representing their midpoints and distances) <a class="yt-timestamp" data-t="17:05:00">[17:05:00]</a>. Crucially, the edge of the [[role_of_mbius_strip_in_topology|Möbius strip]] (representing pairs like x,x) must map onto the original loop itself, which lies on the xy-plane <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>. Additionally, by definition, the interior of the 3D surface (representing distances) must be strictly above the xy-plane <a class="yt-timestamp" data-t="19:31:00">[19:31:00]</a>.

The proof hinges on the fact that it is impossible to embed a [[role_of_mbius_strip_in_topology|Möbius strip]] into 3D space such that its edge is confined to a plane and its interior remains strictly above that plane, without the surface intersecting itself <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>. This impossibility is a core [[topological_surfaces_and_their_properties|property]] of the [[role_of_mbius_strip_in_topology|Möbius strip]].

This can be understood by considering the reflection of the 3D surface (which is a [[role_of_mbius_strip_in_topology|Möbius strip]] with its edge on the plane and interior above) beneath the plane <a class="yt-timestamp" data-t="20:05:00">[20:05:00]</a>. Gluing the original surface to its reflection along their shared edge is equivalent to gluing two [[role_of_mbius_strip_in_topology|Möbius strips]] together along their boundaries <a class="yt-timestamp" data-t="20:15:00">[20:15:00]</a>. This operation results in a [[topological_surfaces_and_their_properties|Klein bottle]] <a class="yt-timestamp" data-t="21:29:00">[21:29:00]</a>.

A well-known [[topological_surfaces_and_their_properties|property]] of the [[topological_surfaces_and_their_properties|Klein bottle]] is that it cannot be properly represented (embedded) in three dimensions without self-intersection <a class="yt-timestamp" data-t="21:46:00">[21:46:00]</a>. This is a more general fact about any closed, non-orientable surface <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>. Since the combined surface forms a [[topological_surfaces_and_their_properties|Klein bottle]] and must self-intersect, and the construction of the surface means these self-intersections correspond to distinct pairs of points with the same midpoint and distance, it proves that every closed continuous loop must have an inscribed rectangle <a class="yt-timestamp" data-t="22:04:00">[22:04:00]</a>.

## The Unsolved Inscribed Square Problem

For the inscribed square problem, the approach is similar but more complex. It would involve not only the midpoint and distance of a pair of points but also the angle of the line segment connecting them <a class="yt-timestamp" data-t="22:52:00">[22:52:00]</a>. This adds another dimension to the data, leading mathematicians to consider embeddings into four-dimensional space <a class="yt-timestamp" data-t="23:10:00">[23:10:00]</a>. Recent work by Joshua Green and Andrew Lobb (2020) extended the inscribed rectangle result to smooth curves, proving the existence of inscribed rectangles of every aspect ratio by embedding [[role_of_mbius_strip_in_topology|Möbius strips]] and [[topological_surfaces_and_their_properties|Klein bottles]] into a specific four-dimensional space <a class="yt-timestamp" data-t="23:22:00">[23:22:00]</a>.

The challenge for the inscribed square problem lies in "rough curves," like fractals, which lack well-defined tangent lines and thus complicate the limiting behavior of the angle data as points get closer <a class="yt-timestamp" data-t="24:57:00">[24:57:00]</a>.

## Significance of [[Topology]]

The [[historical_and_practical_significance_of_topology|significance of topology]] is not about bizarre [[topological_surfaces_and_their_properties|shapes]] for their own sake <a class="yt-timestamp" data-t="25:10:00">[25:10:00]</a>. Instead, it is a mathematical field that defines and understands continuous associations between things, exploring what is and is not possible under these associations <a class="yt-timestamp" data-t="26:22:00">[26:22:00]</a>. Famous [[topological_surfaces_and_their_properties|shapes]] are representatives of vast families of shapes that share fundamental behaviors under continuous maps <a class="yt-timestamp" data-t="26:33:00">[26:33:00]</a>. The excitement mathematicians find in impossible or counter-intuitive properties is rooted in their utility as "fuel for progress" in constructing rigorous proofs <a class="yt-timestamp" data-t="26:44:00">[26:44:00]</a>.