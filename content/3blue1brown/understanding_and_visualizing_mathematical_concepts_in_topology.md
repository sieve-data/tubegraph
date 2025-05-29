---
title: Understanding and visualizing mathematical concepts in topology
videoId: IQqtsm-bBRU
---

From: [[3blue1brown]] <br/> 

The field of [[the_concept_of_topology|topology]] explores the properties of shapes and spaces that are preserved under continuous deformations, such as stretching, bending, or twisting, without tearing or gluing <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. This discipline focuses on [[continuous_mapping_and_its_application_in_topology|continuous associations]] between mathematical objects, understanding what is and is not possible under such transformations <a class="yt-timestamp" data-t="02:26:29">[02:26:29]</a>.

## Common Misconceptions of Topology

[[introduction_to_topology | Topology]] is often presented in recreational math settings as merely the study of "bizarre shapes" <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. Examples might include classroom activities like forming a [[the_concept_of_topology|Möbius strip]] by twisting and gluing a piece of paper <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>, or describing it as a "rubber sheet geometry" where shapes are equivalent if one can be deformed into another without tearing <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>. However, these notions do not fully capture the essence of what [[the_concept_of_topology|topology]] is truly about <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>. For many, these initial examples leave a "frustrating open question: How is this math? How does any of this actually help you solve problems?" <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

## [[role_of_topology_in_solving_mathematical_problems | Topology]] as a Problem-Solving Tool

The true power of [[the_concept_of_topology|topology]] lies in its [[role_of_topology_in_solving_mathematical_problems | ability to serve as a tool for logic and deduction]] <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Engaging with challenging puzzles, even pure ones, sharpens problem-solving instincts that can be applied to practical situations <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. For many, including the speaker, the proof for the inscribed rectangle problem was the first time they felt a true sense for what [[the_concept_of_topology|topology]] is "actually all about" <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.

### The Inscribed Rectangle Problem

The inscribed square problem, posed by Otto Toeplitz in 1911 <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>, asks whether every closed, continuous loop necessarily has an inscribed square <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. A simpler version, proving the existence of an inscribed rectangle, has a beautiful proof attributed to Herbert Vaughan <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

The core idea is to reframe the search for four points forming a rectangle as finding two distinct pairs of points on the loop that share the same midpoint and have the same length <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. These two line segments, if they share a center and length, must form a rectangle with their four endpoints <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

### [[visualizing_mathematical_operations_using_vector_fields | Visualizing]] the Mapping of Loop Pairs

To approach this, one considers all possible pairs of points on a given loop <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. For each pair, two pieces of information are crucial:
1.  The `xy` coordinates of its midpoint <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.
2.  The distance `d` between the two points <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.

These three numbers (`x`, `y`, `d`) can be "packaged together" as a single point in a three-dimensional space <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. This creates a [[continuous_mapping_and_its_application_in_topology | continuous mapping]] from pairs of points on the loop to points in 3D space, meaning small wiggles in the input (the pair of points) result in only small wiggles in the output (the 3D point) <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

The search for an inscribed rectangle then becomes a search for a "coincidence" where two distinct pairs of points map to the same output point in 3D space <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.

#### The "Wild Surface" of Outputs

Collecting all possible outputs of this mapping forms a "wild surface" in 3D space <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>. This surface's self-intersections are key to the proof <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>. For instance, if two distinct pairs of points map to the same `(x, y, d)` point, it signifies a rectangle.

-   **Cross-sections**: Near the base, cross-sections of this surface resemble the loop itself <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>. This is because pairs of points that are very close together have a small `z`-coordinate (distance) and their midpoint is close to the loop itself <a class="yt-timestamp" data-t="10:00:00">[10:00:00]</a>.
-   **Self-intersection as a feature**: When an inscribed rectangle exists, the surface appears to cross through itself at the corresponding `(x, y, d)` point <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>.
-   **Example of a Circle**: For a circle, the surface looks like a dome <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>. While it may not *look* like self-intersection, all inscribed rectangles in a circle share the same midpoint (the circle's center) and diagonal length (the circle's diameter) <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. This means infinitely many distinct pairs map to a *single point* at the dome's peak, representing a collision <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.
-   **Example of an Ellipse**: Squishing a circle into an ellipse transforms this single point of collision into a vertical line of self-intersections <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.
-   **Not a function graph**: This surface is not a function graph. It's the set of all outputs of a function where inputs are pairs of loop points and outputs are 3D points <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

### Representing Pairs of Points Geometrically

To understand the nature of this "wild surface," a second, complementary surface is constructed to represent all possible pairs of points on the loop <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.

1.  **Loop as a Unit Interval**: By assigning each point on the loop a number between 0 and 1, the loop can be thought of as a unit interval where 0 and 1 are glued together <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>.
2.  **Pairs in a Unit Square**: A pair of points on the loop (e.g., `p1`, `p2`) can be represented by a point `(x, y)` in a unit square, where `x` is the coordinate for `p1` and `y` for `p2` <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>.
3.  **Gluing for Ordered Pairs (Torus)**:
    *   Since 0 and 1 represent the same point on the loop, the vertical lines `x=0` and `x=1` in the square represent the same loop pairs and should be glued together <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>. This forms a tube <a class="yt-timestamp" data-t="12:52:00">[12:52:00]</a>.
    *   Similarly, the horizontal lines `y=0` and `y=1` represent the same loop pairs and should be glued <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>. This requires curling the tube into a donut shape, or a [[the_concept_of_topology|torus]] <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>. This [[the_concept_of_topology|torus]] naturally represents all *ordered* pairs of points on the loop <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>.
4.  **Folding for Unordered Pairs ([[the_concept_of_topology|Möbius Strip]])**: For the inscribed rectangle problem, the order of the points in a pair doesn't matter (e.g., `(a, b)` is the same as `(b, a)`) <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>. This means points `(x, y)` and `(y, x)` in the unit square should be considered the same. This implies folding the square along its diagonal <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>. After strategic cuts and gluing, this process naturally leads to the formation of a [[the_concept_of_topology|Möbius strip]] <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>. This [[the_concept_of_topology|Möbius strip]] serves as a geometric representation of all possible *unordered* pairs of points on a loop <a class="yt-timestamp" data-t="16:13:00">[16:13:00]</a>.
    *   The edge of this [[the_concept_of_topology|Möbius strip]] (the red line from the original diagonal fold) corresponds to pairs of points that are actually the same point listed twice (`x,x`) <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>.

### Connecting the Visualizations: [[the_concept_of_topology|Möbius Strip]] and the "Wild Surface"

There is a [[continuous_mapping_and_its_application_in_topology | continuous function]] from the [[the_concept_of_topology|Möbius strip]] (representing all unordered pairs) onto the "wild surface" (representing the `(x,y,d)` data of those pairs) <a class="yt-timestamp" data-t="17:05:00">[17:05:00]</a>. The crucial constraint ("the gun hanging on the wall") is that the boundary of this [[the_concept_of_topology|Möbius strip]] (the `x,x` pairs) must land on the original loop itself, confined to the `xy`-plane <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>. Furthermore, all points of the "wild surface" (and thus the mapped [[the_concept_of_topology|Möbius strip]]) are necessarily *above* the `xy`-plane, because distance `d` is always positive <a class="yt-timestamp" data-t="19:31:00">[19:31:00]</a>.

The proof then relies on the topological fact that it's impossible to embed a [[the_concept_of_topology|Möbius strip]] into 3D space such that its edge is confined to a plane *and* its interior is strictly above that plane, without the surface intersecting itself <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>. If this claim holds, self-intersection must occur, meaning two distinct points from the strip (two distinct pairs of loop points) map to the same point on the surface, thus forming a rectangle <a class="yt-timestamp" data-t="18:10:00">[18:10:00]</a>.

### The [[the_concept_of_topology|Klein Bottle]] and Impossibility Proofs

To strengthen this argument, consider the reflection of the "wild surface" below the `xy`-plane <a class="yt-timestamp" data-t="20:05:00">[20:05:00]</a>. Gluing the original surface to its reflection along their shared edge is equivalent to gluing the edges of two [[the_concept_of_topology|Möbius strips]] together <a class="yt-timestamp" data-t="20:15:00">[20:15:00]</a>. This construction yields a [[the_concept_of_topology|Klein bottle]] <a class="yt-timestamp" data-t="21:29:00">[21:29:00]</a>.

A key property of the [[the_concept_of_topology|Klein bottle]] is its celebrity status as a shape that cannot be properly represented in three dimensions without self-intersection <a class="yt-timestamp" data-t="21:46:00">[21:46:00]</a>. This is a general fact about any closed, non-orientable surface <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>. The fact that [[the_concept_of_topology|Klein bottles]] cannot exist in 3D without self-intersection implies that the combined surface (the "wild surface" and its reflection) must have self-intersection. This confirms the existence of the desired rectangle <a class="yt-timestamp" data-t="22:07:00">[22:07:00]</a>.

## Broader Takeaways on [[introduction_to_topology | Understanding and Visualizing Mathematical Concepts]]

This problem demonstrates that [[the_concept_of_topology|topology]] is not simply about studying "bizarreness for its own sake" <a class="yt-timestamp" data-t="25:13:00">[25:13:00]</a>. Instead, the "mind-bending" structures like the [[the_concept_of_topology|Möbius strip]] and [[the_concept_of_topology|Klein bottle]] emerge naturally as tools for problem-solving <a class="yt-timestamp" data-t="25:22:00">[25:22:00]</a>. These shapes are not specific physical objects but rather "representatives of huge families of shapes that all have essentially the same kind of behavior under [[continuous_mapping_and_its_application_in_topology | continuous maps]]" <a class="yt-timestamp" data-t="26:33:00">[26:33:00]</a>.

The definition of a [[the_concept_of_topology|topological space]] is subtle, but at its heart, [[the_concept_of_topology|topology]] is a "game of understanding [[continuous_mapping_and_its_application_in_topology | continuous associations]] between things, and understanding what is or is not possible under those associations" <a class="yt-timestamp" data-t="26:22:00">[26:22:00]</a>. For mathematicians, "constraints and impossibilities are your fuel for progress" in constructing logical proofs <a class="yt-timestamp" data-t="26:50:00">[26:50:00]</a>. This particular proof exemplifies the power of [[visualizing_mathematical_concepts | visualizing mathematical concepts]] and [[spatial_intuition_in_math | spatial intuition in math]] to solve complex problems, a contrast to [[graphical_intuition_versus_transformational_understanding_in_calculus | graphical intuition versus transformational understanding in calculus]] <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.

The unsolved inscribed square problem, which requires tracking more information (like the angle of the line segment), leads to considering embeddings into higher-dimensional spaces, such as four dimensions <a class="yt-timestamp" data-t="23:10:00">[23:10:00]</a>. The work of Joshua Green and Andrew Lobb in 2020 on smooth curves further demonstrates how thinking about [[the_concept_of_topology|Möbius strips]] and [[the_concept_of_topology|Klein bottles]] in four-dimensional space becomes an "utterly reasonable" approach <a class="yt-timestamp" data-t="23:51:00">[23:51:00]</a>. The challenge in the general inscribed square problem lies with "rough curves" like fractals, where properties like tangent lines (and thus angles) lack clean limiting behavior <a class="yt-timestamp" data-t="25:02:00">[25:02:00]</a>.