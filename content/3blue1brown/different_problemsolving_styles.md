---
title: Different problemsolving styles
videoId: ltLUadnCyi0
---

From: [[3blue1brown]] <br/> 

This article explores two distinct [[problemsolving_strategies_in_mathematics | problem-solving]] styles, personified by two hypothetical students, Alice and Bob, through the lens of a puzzle involving the shadow of a cube <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The goal is not just to solve the puzzle, but to understand the different mindsets brought to [[problem_solving_strategies_in_mathematics | problem solving]] <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Bob's Approach: The Computationalist

Bob embodies a [[mathematical_problemsolving_and_flexibility | problem-solving]] style that favors calculation and concrete details <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. He is most satisfied when he can "dig into the details" and gain a very concrete view of the situation <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

### Calculating the Shadow of a Single Face
When faced with a simplified version of the problem—finding the area of the shadow of a single square face of a cube—Bob seeks an exact formula <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
He considers the [[different_perspectives_on_vectors | normal vector]] perpendicular to the face and the angle, theta, it makes with the vertical light direction <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
Bob's detailed proof involves:
*   Considering a 2D variant of the problem by slicing the shape <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   Using trigonometry, specifically the cosine of theta, to determine the squishing factor of the shadow <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. The area of the shadow is the area of the face multiplied by the absolute value of the cosine of theta (due to negative cosine for angles greater than 90 degrees) <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### Averaging Over Orientations (Integral Calculus)
To find the average area of a square's shadow over all possible orientations, Bob uses integral calculus <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.
*   He considers all possible [[different_perspectives_on_vectors | normal vectors]] of the square, which trace the surface of a sphere, assuming a uniform probability distribution over the sphere's surface <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.
*   The average shadow area depends on the average value of the absolute value of cosine of theta across all points on the sphere <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>.
*   He sets up a definite integral from 0 to pi (180 degrees) for the function, which takes into account the area of "bands of latitude" on the sphere <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>.
*   The result of Bob's calculation is that the average area for a square's shadow is exactly one half the area of that square <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>.

## Alice's Approach: The Generalist

Alice's style involves procrastinating computations and instead seeking a high-level, general overview of the problem's structure <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. She prefers to understand how the problem can be generalized, hoping that a more general view leads to "more swift and elegant computations" <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

### Initial Abstraction (Linear Transformations)
For the shadow of a single face, Alice notes that both rotation and flat projection are linear transformations <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. This means the area of the shadow is proportional to the original area of the shape, with a constant of proportionality (the determinant) that depends only on the transformation, not the specific shape <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. This observation is crucial because it highlights that the specific shape (e.g., a square versus a cat outline) doesn't matter for the proportionality constant <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

### Key Insights for the Cube Shadow
Alice's approach for the entire cube relies on three clever insights:

#### 1. The Double-Covering Principle (Convexity)
Alice realizes that for a given orientation, the area of the cube's shadow is exactly one half the sum of the areas of all its faces <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   This is justified by observing that any ray of light hitting the shadow passes through exactly two points of the cube (one entering, one exiting) <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   This principle holds true because a cube is a **convex** shape <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. A set is convex if the line connecting any two points within it is entirely contained within the set <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. This means light rays will enter and exit only twice, unlike non-convex shapes (e.g., a donut) <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.

#### 2. Swapping Summation and Averaging
Alice shows that the average of the sum of the face shadows is the same as the sum of the average of the face shadows <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.
*   By writing out the sum of shadow areas across many rotations as a grid, she can swap from summing row-by-row (average of cube shadows) to column-by-column (sum of average face shadows) <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   This leads to the conclusion that the average area for the shadow of a cube is proportional to its total surface area <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.

#### 3. The Universal Proportionality Constant
Alice's crucial realization is that the proportionality constant between average shadow area and surface area is universal for **any convex solid** <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>. This means she can find this constant using *any* convex solid for which the average shadow area is easily known <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>.

#### 4. The Sphere as a Shortcut
The most symmetric solid, and one for which the average shadow area is trivial, is a sphere <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.
*   The flat projection shadow of a sphere is always a circle with area πr² <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. Thus, its average shadow area is also πr² <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>.
*   The surface area of a sphere is 4πr² <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>.
*   Therefore, for a sphere, the ratio of its average shadow area to its surface area is πr² / 4πr² = 1/4 <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.
*   Since this constant is universal for all convex solids, Alice concludes that the average shadow area of a cube (or any convex solid) is one-fourth its surface area <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>. For a cube with side length *s*, its surface area is 6s², so its average shadow area is (1/4) * 6s² = (3/2)s² <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.

Alice's argument can be rigorously extended to a sphere by considering a sequence of polyhedra that successively approximate a sphere <a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>.

## Comparison and Reflection

The contrast between Alice's and Bob's approaches is not a value judgment <a class="yt-timestamp" data-t="00:34:12">[00:34:12]</a>.

### Avoiding Calculations vs. Detailed Work
Alice's approach appears "slick" because it seemingly avoids complex calculations, leading to "aha moments" <a class="yt-timestamp" data-t="00:34:19">[00:34:19]</a>. Bob's method, while concrete and detailed, requires familiarity with calculus <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>. Historically, mathematicians like Cauchy (who proved this in 1832) used methods more akin to Bob's, involving integrals <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>.

### The Bias in Math Popularization
There's a bias in popularizations of mathematics towards showcasing "slick proofs" that avoid calculations <a class="yt-timestamp" data-t="00:34:34">[00:34:34]</a>. This can be misleading, as the intuition for such insights often comes from extensive computational practice <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>. Mathematicians throughout history, such as Newton, Euler, and Gauss, had immense patience for "tedious calculations" <a class="yt-timestamp" data-t="00:37:24">[00:37:24]</a>.

### The Importance of Both Styles
Both approaches are vital in [[problemsolving_strategies_in_mathematical_puzzles | mathematical problemsolving]].
*   **Bob's approach** provides a grounded understanding of the problem and is often the most productive path when dealing with more complex scenarios (e.g., a closer light source, which breaks the linearity Alice leverages) <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>. It emphasizes the importance of drilling on computations to build intuition <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.
*   **Alice's approach** demonstrates the power of generality and abstraction <a class="yt-timestamp" data-t="00:38:40">[00:38:40]</a>. It reveals that the specific object (a cube) was not as important as its general properties (convexity) <a class="yt-timestamp" data-t="00:31:47">[00:31:47]</a>. This kind of generalization can lead to new ideas, such as quantifying convexity as a numerical value <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.

The act of discovering new math likely involves a blend of both mindsets <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>.

### Unanswered Questions: Defining "Random Orientation"
A subtle but crucial aspect of this problem, and many in probability, is the precise definition of "averaging over all possible orientations" or choosing a "random orientation" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. While the initial intuition of tossing a cube many times helps <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>, a formal definition requires understanding the space of all possible orientations (SO3) and the probability distribution on it <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Both Alice and Bob implicitly define this distribution in their methods <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This challenge in defining "randomness" is related to concepts like Bertrand's paradox in probability <a class="yt-timestamp" data-t="00:39:18">[00:39:18]</a>, and highlights the [[challenges_in_assessing_problem_difficulty | challenges in assessing problem difficulty]].