---
title: Mathematical exercises and problemsolving in geometry
videoId: GNcFjFmqEc8
---

From: [[3blue1brown]] <br/> 

[[ProblemSolving Strategies in Mathematics | Mathematical problem solving]] often goes beyond merely proving formulas, aiming for a "visceral feeling" of connection between concepts <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. This approach involves understanding *why* certain mathematical relationships hold true <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

## Key Strategies in Geometric Problem Solving

Several effective [[Problemsolving strategies in math | problem-solving strategies]] are employed in geometric contexts:

*   **Approximation with Tiny Rectangles** Dividing a complex surface, like a sphere, into many tiny rectangles allows for approximation of its area <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>. The accuracy of this approximation increases with finer subdivisions, ultimately approaching the true surface area <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>. This method inherently relies on concepts fundamental to [[Role of linear algebra and calculus in geometry | calculus]] <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.
*   **Projection and Shadow Casting** Visualizing how parts of a 3D shape project onto another surface (like casting a shadow) can reveal surprising relationships. For instance, projecting tiny rectangles from a sphere onto a surrounding cylinder can show how their areas are preserved <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>, despite competing effects of stretching and squishing <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.
*   **Identifying and Cancelling Competing Effects** When projections occur, different dimensions (e.g., width and height) might scale in opposite directions. A key insight in geometric [[mathematical_insights_and_elegant_solutions | arguments]] is to demonstrate how these scaling effects perfectly cancel each other out, preserving area or other properties <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.
*   **Naming Conventions** Assigning clear names to variables and dimensions (e.g., radius `r`, distance `d`, angles `alpha`, `beta`) is a fundamental first step in any [[approaches_to_mathematical_problem_solving | mathematical problem solving]] <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>, <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.
*   **Using Similar Triangles** [[Geometric reasoning in higher dimensions | Geometric proofs]] frequently leverage the properties of similar triangles to establish ratios between lengths and areas <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>. Identifying and proving the similarity of relevant triangles is a powerful technique <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>, <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.
*   **Slicing Cross-Sections** Simplifying a 3D problem by examining a 2D cross-section can provide a clearer view of the relationships at play <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.
*   **Fundamental Geometric Properties** Remembering core facts, such as a tangent to a circle being perpendicular to the radius at the point of tangency, can be incredibly helpful for making progress in geometric problems <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.
*   **Tweaking Parameters** Imagining how shapes and relationships change when parameters are adjusted can lead to informed guesses about underlying connections <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
*   **Unwrapping Shapes** For [[geometric_visualization_in_puzzlesolving | visualization]] and calculation, shapes like circles can be conceptually "unwrapped" into simpler forms, such as triangles, while preserving their area <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>. This involves relating concentric rings of a circle to horizontal slices of a triangle <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>.

## Guided Exercises and Problem-Solving

To truly learn mathematics, engaging in [[puzzles_and_geometric_problemsolving | problem solving]] is crucial <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>. One effective approach to tackle [[challenges_in_solving_geometric_problems | complex geometric problems]] is through a heavily-guided sequence of exercises.

### Deriving the Sphere's Surface Area from its Shadow

This approach involves cutting a sphere into many thin rings parallel to a plane (e.g., the xy-plane) and comparing their areas to the areas of their shadows on that plane <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>. The total shadow of, say, the northern hemisphere forms a circle with the same radius as the sphere <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>.

Let's label each ring by the angle `theta` between a line from the sphere's center to that ring and the z-axis, where `theta` ranges from 0 (north pole) to `pi` radians (south pole) <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>. The thickness of these rings can be represented as `R` times `d-theta` <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>.

**Exercise Sequence:**

1.  **Ring Circumference and Area:** What is the circumference of a thin ring at its inner edge, in terms of `R` and `theta`? Multiply this by the thickness (`R` times `d-theta`) to approximate the ring's area <a class="yt-timestamp" data-t="13:12:00">[13:12:00]</a>.
2.  **Shadow Area:** What is the area of the shadow of one of these rings on the x-y plane, expressed in terms of `R`, `theta`, and `d-theta`? Considering tiny right triangles from earlier discussions might be helpful <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>.
3.  **Area Correspondence:** Each ring's shadow has precisely half the area of one of the rings on the sphere. Identify which spherical ring corresponds to the shadow, not necessarily the one directly above it <a class="yt-timestamp" data-t="14:12:00">[14:12:00]</a>. Trigonometric identities may be useful here <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>.
4.  **Northern Hemisphere Correspondence:** Spell out the exact correspondence between all shadows from the northern hemisphere (which form a circle with radius `R`) and specific rings on the sphere, using the answer from the previous question <a class="yt-timestamp" data-t="14:34:00">[14:34:00]</a>.
5.  **Final Implication:** Explain why this correspondence implies that the area of the circle is exactly one-fourth the surface area of the sphere, especially as the rings become infinitesimally thin <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>.

This specific fourfold relationship (surface area being four times the area of a circle with the same radius) is not unique to spheres. It is a specific instance of a more general fact: for any convex shape in three dimensions, the average area of all its shadows (averaged over all possible 3D orientations) is exactly one-fourth of the shape's total surface area <a class="yt-timestamp" data-t="15:15:00">[15:15:00]</a>.