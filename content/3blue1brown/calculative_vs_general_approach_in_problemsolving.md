---
title: Calculative vs general approach in problemsolving
videoId: ltLUadnCyi0
---

From: [[3blue1brown]] <br/> 

This article explores two distinct [[approaches_to_mathematical_problem_solving | problem-solving styles]] through the lens of a puzzle involving the average area of a cube's shadow <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. These styles are personified by two students, Bob and Alice <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>:

*   **Bob**: The calculator, who thrives on diving into concrete details and computations <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   **Alice**: Prefers a high-level, general overview, seeking insights that lead to swift and [[Mathematical Insights and Elegant Solutions | elegant computations]] later <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## The Cube Shadow Puzzle

The central puzzle is to determine the average area of a cube's shadow when averaged over all possible orientations <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Key conditions are:
*   The light source is directly above and effectively infinitely far away, resulting in a flat projection <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   The cube has side length *s* (often assumed to be 1 for animations) <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

### Special Cases for Cube Shadow Area
*   **Cube straight up**: Shadow is a square with area s² <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Long diagonal parallel to light**: Shadow is a regular hexagon with area √3 times the area of one face <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Defining "Average Over All Orientations"
Intuitively, averaging means taking the mean of shadow areas from many random tosses of the cube <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. More formally, it requires defining a probability distribution over the space of all possible orientations, known as SO3 <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. The article postpones a full definition of this distribution until after exploring both solutions <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

## Initial Problem Simplification (Common to Both)

A common [[ProblemSolving Strategies in Mathematics | problem solving strategy]] is to simplify the problem <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. Instead of averaging over all orientations for the whole cube, a first step is to consider the shadow area of a single face of the cube <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Face parallel to ground**: Shadow area equals face area (s²) <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **Face tilted 90 degrees**: Shadow is a straight line with zero area <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Bob's Calculative Approach: Area of a Single Face's Shadow

Bob seeks a precise formula for the shadow area of a single face <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. He focuses on the normal vector perpendicular to the face and its angle, theta, with the vertical light direction <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

Bob's derivation:
1.  He considers a 2D slice of the face <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
2.  By constructing a right triangle, he uses trigonometry: the cosine of theta relates the shadow length to the slice's length <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
3.  The factor by which the slice is squished is cos(theta) <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This applies uniformly to all slices in that direction <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
4.  In the perpendicular direction, there is no squishing <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
5.  Thus, the area of the shadow of a face with area A_face is A_face * |cos(theta)| <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. The absolute value is used because area must be non-negative <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

## Alice's General Approach: Linear Transformations

Alice approaches the problem by [[Conceptualizing Mathematical Problems | conceptualizing]] the process as a sequence of linear transformations: rotation followed by flat projection <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   She knows from linear algebra that applying a linear transformation to a shape changes its area by a constant factor, the determinant of the transformation <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   Crucially, this proportionality constant between the original shape's area and its shadow's area does *not* depend on the original shape <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. It only depends on the rotation being applied <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   This insight highlights why the problem is simpler with a distant light source (linear projection) compared to a closer one (non-linear projection), where proportionality would not hold <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
*   Alice aims for a [[Converting analytic reasoning to geometric intuition | general overview]] that shows the average shadow area of any 2D shape, averaged over all orientations, is proportional to its original area by a universal constant <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This constant does not depend on the specific shape <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

## Alice's Clever Insights for the Cube Shadow

Alice develops three key insights to solve the problem for the entire cube <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>:

### Insight 1: Face Shadows Double-Cover the Cube Shadow
For a convex solid like a cube, any ray of light forming the shadow passes through exactly two points of the cube: one entry and one exit <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   This means the sum of the areas of all individual face shadows is exactly *twice* the area of the cube's total shadow for any given orientation <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   Mathematically: Area(Shadow_cube) = 1/2 * Σ Area(Shadow_face_j) <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
*   This relies on the cube's **convexity**: any line connecting two points within the shape is entirely contained within the shape <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. Non-convex shapes (like a donut) would not have this simple two-to-one correspondence <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.

### Insight 2: Swapping Summation and Averaging Order
Alice notes that the average of a sum is the same as the sum of the averages <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.
*   Average(Area(Shadow_cube)) = 1/2 * Σ Average(Area(Shadow_face_j)) <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.
*   Since all faces of a cube are identical squares, their average shadow areas will be the same.
*   Combining this with her earlier insight about the universal proportionality constant, she concludes that the average shadow area of the cube is proportional to its total surface area by this same universal constant <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. This holds for *any* convex solid <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>.

## Bob's Calculation: Average Shadow Area of a Single Face

While Alice pursues generality, Bob calculates the universal constant <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>. He needs to find the average value of |cos(theta)| over all possible orientations of the square face <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.

1.  **Space of Normal Vectors**: The normal vector of a square face, as it takes on all orientations, traces out the surface of a unit sphere <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>.
2.  **Uniform Probability**: Bob assumes a uniform probability distribution on the sphere, meaning the likelihood of the normal vector landing in any patch of area is proportional to that area <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. The shadow area only depends on theta, the angle of the normal vector from the vertical <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.
3.  **Integral Setup**: To average |cos(theta)| over the sphere, Bob sets up an integral. He considers "bands of latitude" on the sphere, where the area of a band is approximately 2π * sin(theta) * delta_theta <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>.
4.  **Probability Density**: The probability of the normal vector falling into a band is its area divided by the total surface area of the sphere (4πr²) <a class="yt-timestamp" data-t="00:27:17">[00:27:17]</a>.
5.  **Average Calculation**: The average is found by integrating (Area_shadow * Probability_density) over all possible angles from 0 to π radians <a class="yt-timestamp" data-t="00:27:36">[00:27:36]</a>. This leads to the integral: (1/2) * ∫[0 to π] |cos(theta)| * sin(theta) d(theta) <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>.
6.  **Result**: After performing the calculus, Bob finds that the average area for a square's shadow is precisely **one half** the area of that square <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>. This is the universal proportionality constant.

## Alice's Grand Finale: Solving the Cube Shadow Problem

Armed with the knowledge that the average shadow area of any convex solid is proportional to its surface area by the same universal constant, Alice seeks a simpler convex solid for which this relationship is trivial to determine <a class="yt-timestamp" data-t="00:30:21">[00:30:21]</a>.

*   **The Sphere**: The most symmetric convex solid is a sphere <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.
    *   No matter its orientation, its flat projection shadow is always a circle with area πr² <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. So, its average shadow area is also πr² <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>.
    *   The surface area of a sphere is 4πr² <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>.
    *   Therefore, for a sphere, the ratio of its average shadow area to its surface area is (πr²) / (4πr²) = **1/4** <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.

*   **Applying to the Cube**: Since this proportionality constant (1/4) is universal for all convex solids, Alice applies it to the cube <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>.
    *   The surface area of a cube with side length *s* is 6s² <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.
    *   Average(Area(Shadow_cube)) = (1/4) * (Surface Area of Cube) = (1/4) * 6s² = **3/2 s²** <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.

### Justifying the Sphere Extension
While a cube has flat faces and a sphere does not, Alice can justify extending her argument by imagining a sequence of polyhedra that successively approximate a sphere <a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>. For each polyhedron, the average shadow is proportional to its surface area by the universal constant. In the limit, as the polyhedra approach a sphere, the relationship holds, confirming the 1/4 constant <a class="yt-timestamp" data-t="00:33:48">[00:33:48]</a>.

## Reflections on Calculative vs. General Approaches

This problem highlights the strengths of both problem-solving styles <a class="yt-timestamp" data-t="00:34:12">[00:34:12]</a>:
*   **Bob's approach** (detailed calculation) provides a concrete, verifiable answer for a specific case and is crucial for building [[Mathematical intuition versus analysis | intuition]] <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>. For more complex variations (e.g., closer light sources), Bob's method might be the only viable one <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>. Historically, early proofs like Cauchy's (1832) resembled Bob's calculations <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>.
*   **Alice's approach** (generalization and abstraction) reveals deeper mathematical truths and connections <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>. It's often seen as more "elegant" and can lead to unexpected solutions by applying knowledge from other areas (like linear algebra or the properties of a sphere) <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>. This infatuation with generality can help solve specific cases more efficiently <a class="yt-timestamp" data-t="00:38:40">[00:38:40]</a>.

Both styles are essential for discovering new math, often blending together <a class="yt-timestamp" data-t="00:36:17">[00:36:17]</a>. The emphasis on "slick proofs" in popular math can sometimes obscure the importance of the diligent, computational work that builds the foundation for such insights <a class="yt-timestamp" data-t="00:34:34">[00:34:34]</a>.

### The Unanswered Question: Random Orientation
The article concludes by prompting reflection on what "random orientation" truly means <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. This question is explored further in discussions of concepts like [[TarskiPlanck problem solving | Bertrand's paradox]] <a class="yt-timestamp" data-t="00:39:18">[00:39:18]</a>, highlighting subtle assumptions hidden within the problem-solving process.