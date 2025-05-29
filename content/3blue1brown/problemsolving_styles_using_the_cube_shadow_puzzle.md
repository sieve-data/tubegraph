---
title: Problemsolving styles using the cube shadow puzzle
videoId: ltLUadnCyi0
---

From: [[3blue1brown]] <br/> 

This article explores two distinct [[problemsolving_strategies_in_math | problem-solving styles]] through the lens of a geometric puzzle: finding the average area of a cube's shadow <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. These styles are personified by two students, Alice and Bob <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

*   **Bob** embodies a calculation-oriented approach, preferring to dig into concrete details and precise formulas <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   **Alice** represents a high-level, generalized approach, seeking a broad understanding of the problem's shape before detailed computations <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Her aim is to find swift and elegant computations through a more general view <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## The Cube Shadow Puzzle

The puzzle asks to find the average area for the shadow of a cube <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
The shadow's area is influenced by the cube's size and orientation <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. The objective is to average over all possible orientations for a given cube size <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

**Assumptions**:
For simplicity, the light source is assumed to be directly above the cube and infinitely far away <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This means the shadow is a flat projection onto the `x, y, 0` plane <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

**Special Cases**:
*   If the cube is straight up with faces parallel to the ground, the shadow is a square with area `s²` (where `s` is the side length) <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   If the cube's long diagonal is parallel to the light direction, the shadow is a regular hexagon with an area of `√3` times the area of one of its square faces <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

**Defining "Average"**:
Intuitively, averaging means simulating many random tosses of the cube, freezing it, recording the shadow area, and taking the mean <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Formally, this involves defining a probability distribution over the space of all possible 3D orientations, known as SO3 (Special Orthogonal Group of 3x3 matrices) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. The video will postpone a formal definition of "random toss" until the end <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

## Initial Problem Simplification

A common [[problemsolving_strategies_in_math | problem-solving strategy]] for a hard question is to find its simplest non-trivial variant <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. In this case, it means:
1.  Forget about averaging over all orientations <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
2.  Forget about overlapping faces of the cube <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
3.  Focus on computing the shadow area for one particular face in one particular orientation <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

*   If the face is parallel to the ground, its shadow area equals its own area (`s²`) <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   If tilted 90 degrees, its shadow is a straight line with zero area <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Bob's Approach: The Calculator

Bob, being detail-oriented, seeks a precise formula for a single face's shadow <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. He considers the normal vector perpendicular to the face and the angle (theta) it makes with the vertical light direction <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

**Formula for a Single Face**:
Through a 2D slice analysis, Bob proves that the area of the shadow of a face is the area of the face multiplied by the absolute value of the cosine of theta (`Area_shadow = Area_face * |cos(theta)|`) <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. The absolute value is crucial because shadow area cannot be negative <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

**Averaging a Square's Shadow**:
Bob then tackles finding the average shadow area for a square face over all possible orientations <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
He realizes that the shadow area depends only on the normal vector's direction <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>. These normal vectors trace out the surface of a unit sphere <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>. He assumes a uniform probability distribution on this sphere's surface <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

To compute this average, Bob uses an integral <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>:
He considers infinitesimally thin "bands of latitude" on the sphere <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.
The probability of a normal vector landing in a band is proportional to that band's area <a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a>.
Area of band ≈ `(2π sin(theta)) * d(theta)` <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.
Probability of landing in band ≈ `(2π sin(theta) d(theta)) / (4πr²) ` <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
The average shadow area for a square of side `s` (or area `s²`) is then calculated by the integral:
`Average Area = s² * ∫[0 to π] |cos(theta)| * (sin(theta)/2) d(theta)` <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>.

**Bob's Result**:
After performing the integration, Bob finds that the average area for a square's shadow is exactly **one half** the area of that square (`s² * 1/2`) <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>. This provides the universal proportionality constant Alice is looking for.

## Alice's Approach: The Generalist

Alice focuses on the high-level structure of the problem <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
She notes that both rotation and flat projection are [[ProblemSolving Strategies in Mathematics | linear transformations]] <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. A key property of linear transformations is that they scale areas by a constant factor (the determinant), which depends only on the transformation, not the original shape <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. This means the shadow area is proportional to the original shape's area <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This is only true for a distant light source (flat projection); a closer light source would result in a non-linear projection <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

**Alice's First Clever Insight: Convexity and Double Cover**
For any convex solid, the area of its shadow for a given orientation is exactly one half the sum of the areas of all its faces <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
This is because every ray of light passing through the solid hits exactly two faces: one when it enters and one when it exits <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. This property relies on the shape being [[puzzles_and_geometric_problemsolving | convex]] <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. A set is convex if the line connecting any two points within it is entirely contained within the set <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.

**Alice's Second Clever Insight: Swapping Sums and Averages**
The average of the sum of the face shadows is the same as the sum of the average of the face shadows <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.
This allows Alice to relate the average shadow area of the cube to the average shadow area of a single face <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
Since the average shadow for a particular face is `C * Area_face` (where `C` is a universal proportionality constant independent of the 2D shape <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>), the average shadow area of the cube equals `(1/2) * C * (Sum of all face areas)` <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.
This means the average shadow area of a cube is proportional to its total surface area <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>. Crucially, this proportionality constant `C` is *universal* for *any convex solid* <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>.

**Alice's Third Clever Insight: The Sphere**
Alice's final step uses a highly symmetric convex solid: a sphere <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>.
*   The shadow of a sphere (under flat projection) is *always* a circle with area `πr²` <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. Therefore, its average shadow area is `πr²` <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>.
*   The surface area of a sphere is `4πr²` <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>.

Using the relationship `Average_Shadow_Area = (1/2) * C * Surface_Area` from Alice's second insight, applied to a sphere:
`πr² = (1/2) * C * 4πr²` <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>
`πr² = 2Cπr²`
`C = 1/2` <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>

This means the constant `C` that Bob found (1/2) is indeed correct and universal <a class="yt-timestamp" data-t="00:32:12">[00:32:12]</a>.
The argument for using a sphere relies on approximating it with polyhedra, for which the face-based argument holds, and then taking a limit <a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>.

**Alice's Final Answer for the Cube**:
Applying the universal constant `C = 1/2` to the cube:
Average Shadow Area of Cube = `(1/2) * C * Surface_Area_Cube`
Average Shadow Area of Cube = `(1/2) * (1/2) * (6 * s²) ` <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>
Average Shadow Area of Cube = `(1/4) * (6 * s²) = (3/2)s²` <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.

## Reflection on Problem-Solving Styles

The contrast between Alice and Bob's approaches highlights different aspects of [[problemsolving_strategies_in_math | mathematical problem-solving]] <a class="yt-timestamp" data-t="00:34:12">[00:34:12]</a>.

*   **Bias for Slick Proofs**: There is often a bias in popular math explanations towards showing "slick proofs" (like Alice's) that avoid heavy calculation <a class="yt-timestamp" data-t="00:34:34">[00:34:34]</a>. Alice's approach is aesthetically pleasing due to its "aha moments" and broad applicability <a class="yt-timestamp" data-t="00:34:52">[00:34:52]</a>.
*   **Importance of Computation**: Bob's computational approach, while appearing less elegant, is crucial for building intuition and tackling more complex variants of problems (e.g., a closer light source where Alice's linear transformation insight wouldn't apply) <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>. Historically, mathematicians like Cauchy, who proved this fact in 1832, relied on calculations similar to Bob's <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. Developing intuition through "hundreds of concrete examples" and "piles and piles of calculations" is vital for discovering new mathematical insights <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>.
*   **Synergy**: The act of discovering new math often requires a blend of both mindsets: the eagerness to dive into calculations and the drive for general facts <a class="yt-timestamp" data-t="00:36:17">[00:36:17]</a>.
*   **Value of Generality**: Alice's approach demonstrates the power of generality and abstraction. It shows that solving a specific case can be made simpler by finding a universal principle that applies to a wide family of shapes <a class="yt-timestamp" data-t="00:38:40">[00:38:40]</a>.
*   **Quantifying Convexity**: Alice's results suggest a way to quantify convexity beyond a simple yes/no answer: `(4 * Average_Shadow_Area) / Surface_Area`. This ratio is 1 for convex solids and less than 1 for non-convex ones <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>.

**Unanswered Question: Defining Random Orientation**
The problem implicitly relies on a definition of "random orientation" <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>. Bob defines it by uniform distribution of the normal vector on a sphere <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. Alice's method implicitly defines this distribution in a more subtle way through her generalizations <a class="yt-timestamp" data-t="00:39:30">[00:39:30]</a>. This concept relates to [[prisoner_puzzle_and_strategy_development | Bertrand's Paradox]] in probability <a class="yt-timestamp" data-t="00:39:18">[00:39:18]</a>.