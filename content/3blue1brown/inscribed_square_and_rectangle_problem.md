---
title: Inscribed square and rectangle problem
videoId: AmgkSdhK4K8
---

From: [[3blue1brown]] <br/> 

This article explores a fascinating area of geometry, touching on an unsolved problem, an elegant solution to a related, weaker version, and the practical application of topology <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The discussed solution highlights how mathematical concepts like topology can be used to solve concrete [[puzzles_and_geometric_problemsolving | problems]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## The Inscribed Square Problem

The [[inscribed_square_problem | Inscribed Square Problem]] is a long-standing unsolved problem in mathematics <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. It asks: For any given closed loop (a continuous line that ends where it started, no matter how complex or "crazy" its path), can you always find four points on that loop that form the vertices of a square? <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>

For simple shapes:
*   **Circle**: It's easy to find an infinite number of inscribed squares <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Ellipse**: It's still relatively easy to find an inscribed square <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

The challenge lies in proving this for *every* possible closed loop, no matter how irregular <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. The fact that this problem remains unsolved means current mathematical tools cannot definitively confirm or deny the existence of a loop without an inscribed square <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This highlights the [[challenges_in_solving_geometric_problems | challenges in solving geometric problems]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## The Inscribed Rectangle Problem

While the square problem remains unsolved, a weaker version asking about inscribed rectangles instead of squares *does* have a beautiful, video-worthy solution <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This solution is considered by some to be a favorite piece of mathematics <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Key Property of Rectangles

The solution leverages a fundamental property of rectangles:
*   For any rectangle ABCD, the diagonal pair of points (A, C) shares the same midpoint as the diagonal pair (B, D) <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   Additionally, the distance between A and C is equal to the distance between B and D <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

Conversely, if two distinct pairs of points in space (A, C) and (B, D) share a midpoint and have equal distances between them, those four points necessarily form a rectangle <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Therefore, to prove that any closed loop always has an inscribed rectangle, the goal is to show that it's always possible to find two *distinct* pairs of points on the loop that share a midpoint and are the same distance apart <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Mapping Pairs of Points to a 3D Surface

To achieve this, a function is defined that takes pairs of points on the loop and outputs a single point in 3D space, encoding their midpoint and distance <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

1.  Imagine the closed loop sitting on the XY-plane in 3D space <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
2.  For any given pair of points on the loop, locate their midpoint `m` (which will be on the XY-plane) <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
3.  Measure the distance `d` between these two points <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
4.  Plot a point in 3D space that is exactly `d` units above the midpoint `m` in the Z-direction <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

As this process is applied to all possible pairs of points on the loop, it generates a continuous surface in 3D space <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The function is continuous, meaning small adjustments to the input pair of points result in only small adjustments to the output 3D point <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

Notably, as a pair of points on the loop gets closer, the plotted point gets lower (closer to the XY-plane), and its midpoint gets closer to the loop <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. When the two points of a pair coincide (e.g., `(x, x)`), their distance `d` is zero, so the plotted point lies *exactly* on the loop itself <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

The objective is to show that this 3D surface must intersect itself <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. An intersection implies that two *distinct* pairs of points on the loop map to the same spot in 3D space, meaning they share a common midpoint and distance, thus forming a rectangle <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Representing Pairs of Points Geometrically

To understand why this surface must intersect itself, it's necessary to understand the geometry of "pairs of points on a loop" <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

#### Ordered Pairs and the Torus

1.  **Straighten the Loop**: Imagine cutting the closed loop at one point and deforming it into a straight line segment, like the interval from 0 to 1 on a number line <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. The cut point corresponds to both 0 and 1 <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
2.  **Form a Square**: To represent *ordered* pairs of points (where (A, B) is distinct from (B, A)), create a 1x1 square where the x-axis represents the first point from 0 to 1, and the y-axis represents the second point from 0 to 1 <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. Each point `(x, y)` in this square corresponds to an ordered pair of points on the loop <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
3.  **Gluing Edges**: Because the endpoints 0 and 1 of the interval correspond to the same point on the original loop:
    *   The left edge of the square (where x=0) must be glued to the right edge (where x=1) <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. This forms a cylinder, similar to [[unwrapping_cylinder_into_a_rectangle | unwrapping a cylinder into a rectangle]] in reverse <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
    *   The bottom edge (where y=0) must be glued to the top edge (where y=1) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
4.  **Result: A Torus**: Performing these gluings transforms the square into a torus (the surface of a doughnut) <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Every point on this torus corresponds to a unique ordered pair of points on the loop, and vice versa, in a continuous manner <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

#### Unordered Pairs and the Möbius Strip

The problem requires considering *unordered* pairs of points (where (A, B) is the same as (B, A)) to avoid trivial solutions <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

1.  **Folding the Square**: In the 1x1 square representing ordered pairs, points `(x, y)` and `(y, x)` represent the same unordered pair <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. To reflect this, the square must be folded diagonally, identifying `(x, y)` with `(y, x)` <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
2.  **The Diagonal Line**: The diagonal line where `x = y` (the crease of the fold) represents pairs where the two points coincide (e.g., `(x, x)`) <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. This line will become the edge of the resulting shape <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
3.  **Complex Gluing**: After folding, the bottom edge needs to be glued to the right edge with a specific orientation (e.g., bottom-left to top-right) <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This complex gluing process involves making a diagonal cut and then performing a twist <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
4.  **Result: A Möbius Strip**: This series of operations results in a Möbius strip <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. The edge of this Möbius strip corresponds precisely to those "coincident" pairs of points (`x, x`) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. The Möbius strip serves as the natural topological surface representing all unordered pairs of points on the loop <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

### The Topological Proof

With the understanding that the Möbius strip naturally represents all unordered pairs of points on the loop, the solution to the inscribed rectangle problem becomes clear <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

1.  **Mapping the Möbius Strip**: The special 3D surface defined earlier (where pairs of points on the loop map to `(midpoint, distance)`) effectively maps the Möbius strip onto this surface in 3D space <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
2.  **Edge Mapping**: As established, pairs of points like `(x, x)` map directly onto the original closed loop in the XY-plane <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. Since the edge of the Möbius strip represents these `(x, x)` pairs, when the strip is mapped onto the 3D surface, its single edge must be mapped directly onto the original closed loop on the XY-plane <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
3.  **Forced Intersection**: The crucial point from topology is that it is impossible to attach the single edge of a Möbius strip to a two-dimensional plane (or a loop within it) without forcing the strip to intersect itself <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
4.  **Conclusion**: Since points on the Möbius strip represent pairs of points on the loop, if the strip intersects itself during this mapping, it means there are at least two *distinct* pairs of points on the loop that map to the *same* spot on the 3D surface <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. This implies they share a common midpoint and are the same distance apart, thus guaranteeing that they form a rectangle <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

This forms the proof for the inscribed rectangle problem <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

### The Role of Topology

This elegant solution beautifully demonstrates the practical application of topology <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. Concepts like the Möbius strip and the torus are not merely abstract curiosities but arise naturally as ways to understand and solve concrete [[mathematical_exercises_and_problemsolving_in_geometry | geometric problems]] <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. The rigorous justification of the "forced intersection" step requires developing the field of topology, showing why topologists define certain concepts the way they do <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. [[Geometric visualization in puzzlesolving | Geometric visualization]] plays a critical role in understanding these complex relationships <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.