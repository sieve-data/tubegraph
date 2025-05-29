---
title: Inscribed square problem
videoId: IQqtsm-bBRU
---

From: [[3blue1brown]] <br/> 

The [[inscribed_square_and_rectangle_problem | inscribed square problem]] poses a question: does every closed continuous loop necessarily contain an inscribed square? <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a> This means finding four points on the loop that form the vertices of a square <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. A "closed continuous curve" or "loop" is defined as any squiggle that can be drawn on paper without lifting the pen, ending where it starts <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. As of the transcript's creation, nobody in the world knows the answer to this question <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Origin and Related Problems

The question was originally posed by Otto Toeplitz in 1911 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. A simpler, but related, version of the problem asks whether every closed continuous loop necessarily has an [[inscribed_square_and_rectangle_problem | inscribed rectangle]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The argument for the inscribed rectangle problem is attributed to Herbert Vaughan <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This proof is considered a "favorite piece of math" by the video's creator <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Motivation and Connection to Topology

While there are no known practical applications for proving the existence of an inscribed rectangle, engaging with such [[puzzles_and_geometric_problemsolving | challenging puzzles]] can sharpen problem-solving instincts applicable to other areas <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

The proof for the inscribed rectangle problem provides a fundamental understanding of topology <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Topology is often misrepresented in recreational math as the study of bizarre shapes like the Möbius strip <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a> or as "rubber sheet geometry" where shapes are considered the same if one can be deformed into another without tearing <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. However, these notions do not fully capture what topology is truly about, which is the study of continuous associations between things and what is or is not possible under those associations <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a><a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a>. The proof demonstrates how seemingly bizarre shapes and their properties become tools for logic and deduction <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Proof of the Inscribed Rectangle Theorem

The proof for the inscribed rectangle theorem involves reframing the question and constructing geometric representations.

### Reframing the Question

Instead of searching for four points forming a rectangle, the problem is reframed as searching for two distinct pairs of points on the loop <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. These two pairs must satisfy two conditions:
1.  They have the same midpoint <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
2.  They have the same length <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

If these conditions are met, the four endpoints of these two distinct line segments will necessarily form a rectangle <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This is a straightforward [[mathematical_exercises_and_problemsolving_in_geometry | geometry exercise]] to prove <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### Mapping Pairs of Points to 3D Space

For any pair of points on a given loop, two pieces of data are important:
1.  **Midpoint coordinates (x, y)**: The two-dimensional coordinates of the midpoint of the segment connecting the pair <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
2.  **Distance (d)**: The distance between the two points in the pair <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

These three numbers (x, y, d) can be packaged together as a single point in a three-dimensional space <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The x and y coordinates represent the midpoint's location on the plane where the loop sits, and the z-coordinate (or height) represents the distance between the points <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

This process creates a continuous mapping from pairs of points on the loop to points in three-dimensional space <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Continuity means that slightly wiggling the input pair of points only slightly wiggles the output point in 3D space, with no sudden jumps <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

The search for an inscribed rectangle now amounts to finding a "coincidence" where two *distinct* pairs of points on the loop map to the *same* output point in 3D space <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This means they would share the same midpoint and distance, forming a rectangle <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### The "Wild Surface" of Outputs

Collecting all possible outputs of this mapping from all possible pairs of points on the loop forms a complex, "wild surface" in 3D space <a class="yt-timestamp" data-t="00:05:58">[00:06:02]</a>. Self-intersections within this surface correspond to inscribed rectangles <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

*   **Cross-sections**: Near the base (xy-plane), cross-sections of this surface approximately resemble the loop itself <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Circle Example**: For a circular loop, the surface forms a dome shape <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. While it may not visually appear to self-intersect, a circle has infinitely many inscribed rectangles, all sharing the circle's center as their midpoint and the diameter as their diagonal length <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This means infinitely many pairs of points map to a single point at the top of the dome, representing a "collision" or self-intersection in the sense of the mapping <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   **Ellipse Example**: Squishing a circle into an ellipse causes this single point of intersection to become a vertical line of self-intersections <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

It is important to note that this surface is not a function graph, but rather the set of all possible outputs from the mapping <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### The "Gun on the Wall": Pairs of Identical Points

A crucial detail, referred to as "the gun on the wall," is what happens when the two points in a pair are infinitesimally close or even the same point on the loop (e.g., x, x) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. In this extreme case, the distance between them is zero, so the output point in 3D space will have a z-coordinate of zero <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. The midpoint will be the point itself. Therefore, all such pairs (x, x) map directly onto the original loop lying on the xy-plane <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### Constructing a Second Surface: The Möbius Strip

To prove that the "wild surface" must self-intersect, another natural surface is constructed that also represents pairs of points on the loop.

1.  **Coordinate System on the Loop**: Assign each point on the loop a number between 0 and 1 <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. This is like snipping the loop and flattening it onto the unit interval, where 0 and 1 map to the same point <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
2.  **Unit Square for Pairs**: For a pair of points (P1, P2) on the loop, they can be represented by coordinates (x, y) in a unit square, where x is the coordinate for P1 and y for P2 <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
3.  **Gluing for a Torus (Ordered Pairs)**: To account for the loop's continuity (0 and 1 being the same point), edges of the unit square are "glued" together:
    *   The left (x=0) and right (x=1) vertical edges are glued, forming a tube <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.
    *   The bottom (y=0) and top (y=1) horizontal edges are then glued, curling the tube into a donut shape, or a torus <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
    This torus continuously and bijectively represents all *ordered* pairs of points on the loop <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

4.  **From Torus to Möbius Strip (Unordered Pairs)**: For the inscribed rectangle problem, the order of the points in a pair doesn't matter (a,b is the same as b,a) <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. In the unit square, this means points (x, y) and (y, x) are equivalent. This is represented by folding the square along its main diagonal (from (0,0) to (1,1)) <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
    *   The diagonal itself (where x=y) represents pairs of identical points (x, x) <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
    *   After folding, the remaining edges need to be glued. This process, involving cutting and re-gluing with a half-twist, naturally results in a Möbius strip <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a><a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.

This Möbius strip continuously and bijectively represents all possible *unordered* pairs of points on a loop <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. The edge of this Möbius strip corresponds precisely to the diagonal line where x=y, representing pairs of identical points (x, x) <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

### The Topological Argument

1.  **Mapping the Möbius Strip to the Wild Surface**: Since both the Möbius strip and the "wild surface" represent unordered pairs of points on the loop via continuous bijections, there must be a continuous function from the Möbius strip onto the "wild surface" in 3D space <a class="yt-timestamp" data-t="00:16:56">[00:17:05]</a>.
2.  **The Crucial Constraint**: The edge of the Möbius strip (representing pairs like x,x) *must* land on the original loop, which lies on the xy-plane (z=0) <a class="yt-timestamp" data-t="00:17:33">[00:17:42]</a>. Additionally, by its construction, the "wild surface" must always exist *above* the xy-plane (distance d > 0) for distinct points <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

The proof then relies on the claim that it is impossible to embed a Möbius strip into 3D space such that its edge is confined to the xy-plane and its interior is strictly above the plane, *without* the strip self-intersecting <a class="yt=" data-t="00:19:41">[00:19:41]</a>.

*   **Dan Asimov's Counterexample**: Initially, it might seem impossible to embed a Möbius strip with its edge on a plane at all without self-intersection. However, mathematician Dan Asimov demonstrated a construction where a Möbius strip's boundary lies on a circle in a plane, without self-intersection <a class="yt-timestamp" data-t="00:18:36">[00:18:40]</a>. This embedding, however, has parts of the strip going both above and below the plane <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. This refinement is critical for the proof.

3.  **Connection to the Klein Bottle**: Consider the "wild surface" together with its reflection underneath the xy-plane <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. This combined surface is topologically equivalent to what you get when you glue the edges of two Möbius strips together <a class="yt-timestamp" data-t="00:20:15">[00:20:18]</a>. This composite surface is famously known as a Klein bottle <a class="yt-timestamp" data-t="00:21:29">[00:21:31]</a>.
    *   A Klein bottle is a "celebrity shape" in math because it has no clear interior or exterior <a class="yt-timestamp" data-t="00:21:31">[00:21:34]</a>.
    *   A fundamental property of the Klein bottle is that it is *impossible* to properly represent it in three dimensions without the surface intersecting itself <a class="yt-timestamp" data-t="00:21:43">[00:21:49]</a>. This is a general fact about any closed, non-orientable surface <a class="yt-timestamp" data-t="00:21:57">[00:22:01]</a>.

4.  **Conclusion**: Because the "wild surface" combined with its reflection forms a Klein bottle, and Klein bottles cannot be embedded in 3D without self-intersection, the original "wild surface" must also self-intersect <a class="yt-timestamp" data-t="00:22:07">[00:22:12]</a>. This self-intersection means there are two distinct pairs of points on the loop that map to the same point in 3D space (same midpoint and distance), thus forming a rectangle <a class="yt-timestamp" data-t="00:22:20">[00:22:23]</a>.

## The Unsolved [[inscribed_square_and_rectangle_problem | Inscribed Square Problem]] Revisited

The [[inscribed_square_and_rectangle_problem | inscribed square problem]] is harder because it requires a specific 90-degree difference in angle between the two diagonals, in addition to sharing a midpoint and length <a class="yt-timestamp" data-t="00:22:43">[00:23:01]</a>. This additional piece of information might lead one to consider embeddings into four dimensions <a class="yt-timestamp" data-t="00:23:10">[00:23:14]</a>.

### Smooth Curves

In 2020, mathematicians Joshua Green and Andrew Lobb proved a significant extension of this result for *smooth curves* <a class="yt-timestamp" data-t="00:23:22">[00:23:26]</a>. Smooth curves are those where derivatives can be taken as many times as desired, meaning every point has a well-defined tangent line <a class="yt-timestamp" data-t="00:24:15">[00:24:23]</a>. For smooth curves, it was already known that an inscribed square could always be found <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. Green and Lobb showed that for smooth curves, rectangles of *every possible aspect ratio* can be found <a class="yt-timestamp" data-t="00:24:44">[00:24:47]</a>. Their paper involves embedding Möbius strips and [[klein_bottle | Klein bottles]] into four-dimensional space <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>.

### Rough Curves

What makes the general [[inscribed_square_and_rectangle_problem | inscribed square problem]] (for *all* closed continuous curves) unsolved is the case of "rough curves," like fractals <a class="yt-timestamp" data-t="00:25:02">[00:25:05]</a>. For rough curves, the angle of a line segment connecting two points might not have a clean limiting behavior as the points get closer, making the topological argument more complex or inapplicable <a class="yt-timestamp" data-t="00:24:57">[00:25:02]</a>.

## Takeaways

*   **Purpose of Abstract Math**: Mathematicians study seemingly bizarre shapes like Möbius strips and [[klein_bottle | Klein bottles]] not for their oddity, but because they are tools for solving complex problems and provide logical constraints essential for proofs <a class="yt-timestamp" data-t="00:25:10">[00:25:22]</a>.
*   **Topological Space**: A Möbius strip is not just one specific physical shape; it represents an "infinite family of shapes" or a "topological space," all connected by a certain notion of equivalence <a class="yt-timestamp" data-t="00:25:42">[00:25:47]</a><a class="yt-timestamp" data-t="00:26:00">[00:26:03]</a>. Examples include the familiar twisted strip, Asimov's snail-shell shape, or even the abstract idea of unordered pairs of points on a loop <a class="yt-timestamp" data-t="00:25:47">[00:25:55]</a>.
*   **Topology Defined**: Topology fundamentally involves understanding continuous associations between different mathematical objects and determining what is or is not possible under those associations <a class="yt-timestamp" data-t="00:26:22">[00:26:29]</a>. Constraints and impossibilities revealed through topological reasoning are crucial for mathematical progress <a class="yt-timestamp" data-t="00:26:44">[00:26:53]</a>.