---
title: Inscribed square problem
videoId: AmgkSdhK4K8
---

From: [[3blue1brown]] <br/> 

The [[the_inscribed_square_problem | inscribed square problem]] is an unsolved mathematical problem that asks whether it is always possible to find four points on any closed loop that form a square <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. A "closed loop" refers to any continuous line drawn through space that eventually returns to its starting point, regardless of its complexity <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.

For familiar shapes like a circle or an ellipse, it is relatively straightforward to find an [[the_inscribed_square_problem | inscribed square]] <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. However, for an arbitrarily complex closed loop, it remains unknown whether such a square always exists <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. The fact that current mathematical tools cannot confirm or deny the existence of a loop without an [[the_inscribed_square_problem | inscribed square]] highlights the problem's intriguing nature <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.

## Inscribed Rectangles: A Solved Weaker Version

While the [[the_inscribed_square_problem | inscribed square problem]] remains open, a weaker version focusing on [[mathematical_proofs_involving_inscribed_rectangles | inscribed rectangles]] has a beautiful and elegant solution <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>. This solution provides insight into how topology can be used to solve concrete problems <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

### Proof for Inscribed Rectangles

The proof for [[mathematical_proofs_involving_inscribed_rectangles | inscribed rectangles]] shifts focus from individual points on the loop to pairs of points <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

#### Key Property of Rectangles

Any rectangle ABCD has two defining properties for its diagonal pairs of points (AC and BD):
1.  The distance between A and C equals the distance between B and D <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.
2.  The midpoint of A and C is the same as the midpoint of B and D <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
Conversely, if two distinct pairs of points in space (AC and BD) share a midpoint and have equal distances, they automatically form a rectangle <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

#### Proof Strategy

The goal is to prove that for any closed loop, it is always possible to find two distinct pairs of points on that loop that share a common midpoint and are the same distance apart <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.

#### Mapping Pairs of Points to 3D Space

1.  **Define a Function:** Imagine the closed loop resting on the xy-plane in 3D space <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. For any given pair of points on the loop, label their midpoint as `m` (on the xy-plane) and the distance between them as `d` <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. Plot a new point in 3D space that is `d` units directly above `m` in the z-direction <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.
2.  **Forming a Surface:** As this process is repeated for all possible pairs of points on the loop, a continuous surface is generated in 3D space <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>.
3.  **Surface Properties:**
    *   The surface "hugs" the loop: As a pair of points on the loop gets closer, the plotted point on the surface gets lower (since `d` decreases) and closer to the loop <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>. When the two points coincide (e.g., `x` and `x`), the plotted point is exactly on the loop at `x` <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.
    *   The function is continuous: Small adjustments to the input pair of points result in only small adjustments to the output point in 3D space <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
4.  **Goal Refined:** The proof aims to show that this function must have a "collision"—meaning two distinct pairs of points map to the exact same spot in 3D space <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. Such a collision implies that these two distinct pairs share a common midpoint and the same distance `d`, thereby forming a rectangle <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. In essence, the proof shows that this 3D surface must intersect itself <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.

#### Representing Pairs of Points Topologically

To understand why the surface must intersect itself, it's necessary to build a topological representation of "pairs of points on a loop" <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

1.  **Ordered Pairs and the Torus:**
    *   Straighten the loop into an interval (e.g., from 0 to 1 on a number line) <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>.
    *   Ordered pairs of points on the loop can be represented as points in a 1x1 square, with x and y coordinates representing the two points <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a>.
    *   Because the ends of the interval (0 and 1) correspond to the same point on the original loop, the edges of this square must be "glued": the left edge to the right edge, and the bottom edge to the top edge <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.
    *   This gluing process transforms the square into a torus (the surface of a doughnut) <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>.
    *   The torus thus provides a continuous one-to-one association for all ordered pairs of points on the loop <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>.

2.  **Unordered Pairs and the Möbius Strip:**
    *   For [[mathematical_proofs_involving_inscribed_rectangles | inscribed rectangles]], the order of points in a pair does not matter (AB is the same as BA) <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
    *   In the 1x1 square representation, this means that point (x,y) must represent the same pair as (y,x) <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>.
    *   This equivalence is achieved by folding the square diagonally, gluing points (x,y) to (y,x) <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>.
    *   The diagonal line created by this fold represents pairs where the points coincide (e.g., xx) <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.
    *   The remaining edges (bottom and right of the original square) must also be glued, but with a twist <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>. This process results in a Möbius strip <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.
    *   The Möbius strip is the natural topological shape representing all unordered pairs of points on the loop <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>. Its single edge corresponds to the pairs where both points are the same (xx) <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.

#### The Topological Argument

1.  **Mapping the Möbius Strip to the 3D Surface:** Since there's a continuous one-to-one association between unordered pairs on the loop and points on the Möbius strip, the Möbius strip can be mapped onto the 3D surface created by the midpoint-distance function <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>.
2.  **Edge Constraint:** When pairs of points on the loop are very close, the function's output is just above the loop <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>. Crucially, when the pair of points are identical (xx), the output is *exactly* on the loop in the xy-plane <a class="yt-timestamp" data-t="14:14:00">[14:14:00]</a>. This means the edge of the Möbius strip (which represents xx pairs) *must* map directly onto the original closed loop in the xy-plane <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>.
3.  **Self-Intersection:** From a topological perspective, it is impossible to glue the edge of a Möbius strip to a two-dimensional plane (where the loop lies) without forcing the strip itself to intersect <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.
4.  **Conclusion:** Because the mapping of the Möbius strip onto the 3D surface forces it to intersect itself, it implies that there must be at least two distinct unordered pairs of points on the loop that map to the same point in 3D space <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>. This collision means these two pairs share the same midpoint and are the same distance apart, thereby forming an [[mathematical_proofs_involving_inscribed_rectangles | inscribed rectangle]] <a class="yt-timestamp" data-t="15:02:00">[15:02:00]</a>.

This proof beautifully demonstrates how abstract topological concepts, like the properties of the Möbius strip, can be applied to solve concrete problems in geometry <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>.