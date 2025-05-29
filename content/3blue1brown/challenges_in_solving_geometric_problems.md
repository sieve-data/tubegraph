---
title: Challenges in solving geometric problems
videoId: IQqtsm-bBRU
---

From: [[3blue1brown]] <br/> 

Solving [[mathematical_exercises_and_problemsolving_in_geometry | geometric problems]] often involves unique complexities, from understanding abstract concepts to employing non-obvious strategies.

## The Inscribed Square Problem: An Unsolved Challenge
A prime example of a persistent [[puzzles_and_geometric_problemsolving | geometric problem]] is the inscribed square problem, first posed by Otto Toeplitz in 1911 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The question asks whether every closed continuous loop necessarily contains four points that form the vertices of an inscribed square <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This remains an unsolved question globally <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

### The Simpler Inscribed Rectangle Problem
While the square problem remains open, a related question about inscribed rectangles has a beautiful proof <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This proof, originally due to Herbert Vaughan, demonstrates that any closed continuous loop necessarily contains an inscribed rectangle <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Value of Engaging with Geometric Puzzles
Despite some [[mathematical_exercises_and_problemsolving_in_geometry | geometric problems]] lacking direct applications, engaging with them is valuable for several reasons:
*   **Sharpening Instincts** [[problemsolving_strategies_in_math | Engaging with challenging puzzles]], even purely abstract ones, can sharpen [[problemsolving_strategies_in_math | problem-solving instincts]] that can be applied to practical situations later <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Conceptual Understanding** Solving these problems can provide a deep sense of what abstract mathematical fields like topology are truly about <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Challenges in Understanding Topology
Topology, a field crucial for solving certain [[geometric_reasoning_in_higher_dimensions | geometric problems]], often presents [[challenges_students_face_in_learning_linear_algebra | challenges for students]]:
*   **Misleading Introductions** In recreational math, topology is sometimes simplistically presented as the study of "bizarre shapes" or "rubber sheet geometry" <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Such explanations often leave students wondering, "How is this math? How does any of this actually help you solve problems?" <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Abstract Tools** The true value of topological concepts, such as the Möbius strip or [[klein_bottle | Klein bottle]], lies in their utility as "tools for logic and deduction" rather than mere curiosities <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Strategies for Tackling Geometric Problems

### Reframing the Question
A key [[problemsolving_strategies_in_mathematics | problem-solving strategy]] is to reframe the original question <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. For the inscribed rectangle problem, instead of searching for four points, one can search for two distinct pairs of points on the loop that share the same midpoint and the same length <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This is a straightforward [[mathematical_exercises_and_problemsolving_in_geometry | geometry exercise]] to prove equivalent <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

### Visualizing Data in Higher Dimensions
To solve complex [[puzzles_and_geometric_problemsolving | geometric problems]], it's often helpful to [[converting_analytic_reasoning_to_geometric_intuition | convert analytic reasoning to geometric intuition]]:
*   **Packaging Data** For each pair of points on a loop, their midpoint's (x, y) coordinates and the distance (d) between them can be packaged as a single point in a three-dimensional space (x, y, d) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This creates a "wild surface" representing all possible outputs, which can be challenging to visualize <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **Identifying Self-Intersection** The goal becomes finding "coincidences" where two distinct pairs of points map to the same point in this 3D space, indicating a "self-intersection" of the surface <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This visual cue implies the existence of an inscribed rectangle <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Even for a simple circle, the self-intersection can be subtle, appearing as a single point at the "top of the dome" <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

### Constructing Abstract Geometric Spaces
A critical step involves constructing a specific geometric space that naturally represents the problem's inputs:
*   **Pairs of Points as a Torus** By assigning coordinates (0-1) to points on the loop, pairs of points can be represented in a unit square <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. Gluing the edges of this square (x=0 to x=1, y=0 to y=1) topologically yields a torus <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>, which naturally represents ordered pairs of points on the loop <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **Unordered Pairs and the Möbius Strip** Since the order of points in a pair doesn't matter for a rectangle, pairs (a,b) and (b,a) must be considered the same <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. This requires folding the unit square along its diagonal, and then carefully gluing the remaining edges, which ultimately forms a Möbius strip <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. This construction shows how the Möbius strip naturally represents all possible unordered pairs of points on a loop <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

### The Role of Non-Orientable Surfaces
The proof of the inscribed rectangle relies on the properties of non-orientable surfaces:
*   **The Klein Bottle** By reflecting the constructed surface (which embodies a Möbius strip) underneath the plane and gluing its edge to the original surface, a new closed surface is formed <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>. This process of gluing two Möbius strips together results in a [[klein_bottle | Klein bottle]] <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.
*   **Self-Intersection Constraint** A key fact in topology is that it's impossible to properly represent a [[klein_bottle | Klein bottle]] in three dimensions without it intersecting itself <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. This property, true for any closed non-orientable surface, is central to the proof <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>. The inevitable self-intersection in the [[geometric_reasoning_and_sphere_surface_area | geometric reasoning]] implies the existence of a rectangle <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.

## The Continuing Challenge: Rough Curves
The inscribed square problem remains unsolved, especially for "rough" curves like fractals <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. While extensions exist for smooth curves (e.g., proving the existence of rectangles of every aspect ratio, which involves embedding Möbius strips and [[klein_bottle | Klein bottles]] into four-dimensional space) <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>, rough curves lack the "clean limiting behavior" for attributes like tangent line angles, which are crucial for proofs in higher dimensions <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>. This highlights a significant challenge in [[geometric_reasoning_in_higher_dimensions | geometric reasoning in higher dimensions]].

## Topology as a Problem-Solving Framework
Ultimately, the study of topology isn't just about bizarre shapes; it's about understanding continuous associations and the possibilities and impossibilities within those associations <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>. The "bizarre properties and impossibilities" of topological spaces provide "fuel for progress" in [[problemsolving_strategies_in_mathematics | logical proofs]] <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.