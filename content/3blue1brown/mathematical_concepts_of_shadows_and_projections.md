---
title: Mathematical concepts of shadows and projections
videoId: ltLUadnCyi0
---

From: [[3blue1brown]] <br/> 

This article explores the [[conceptualizing_mathematical_problems | problem-solving]] styles reflected in two different approaches to a puzzle involving the shadow of a cube <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The core puzzle is to find the [[average_shadow_area_of_geometric_figures | average area for the shadow of a cube]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Two Problem-Solving Approaches

The video introduces two distinct problem-solving styles, anthropomorphized by two students, Alice and Bob <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>:

*   **Bob's Style**: Bob loves calculation and prefers to delve into the concrete details of a problem <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. He is most pleased when he has a very concrete view of the situation <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **Alice's Style**: Alice is inclined to procrastinate computations <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. She prefers to gain a high-level, general overview of the problem's shape before getting into calculations <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Alice finds satisfaction in understanding how to generalize a problem and how a more general view can lead to swift and elegant computations <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Defining the Puzzle: Average Shadow of a Cube

The puzzle requires finding the average area for the shadow of a cube <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The shadow's area is influenced by the cube's size and its orientation <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. The "average" refers to averaging over all possible orientations for a particular size of the cube <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

For simplicity, the problem assumes the light source is directly above the cube and infinitely far away <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This means the problem deals with a flat projection, where a point (x, y, z) in space projects to (x, y, 0) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

Special cases for a unit side length cube (s=1) include:
*   **Straight up orientation**: The shadow is a square with an area of s² <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Long diagonal parallel to light**: The shadow is a regular hexagon with an area of exactly the square root of 3 times the area of one of the square faces <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Defining "Average Over All Orientations"

Intuitively, averaging over all orientations means imagining tossing the cube like a die, recording the shadow area, and repeating many times to take the mean of the sample <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The true average is what this experimental mean approaches with infinitely many tosses <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

More formally, this involves describing the space of all possible orientations, known as SO3 (Special Orthogonal Group of 3x3 matrices) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, and defining a probability distribution over this space <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. For this puzzle, the heuristic approach of random tosses is sufficient initially <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## Shadow of a Single Face

A useful first step in [[conceptualizing_mathematical_problems | problemsolving]] is to simplify the problem <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. For a single face of the cube:
*   If a face is parallel to the ground, its shadow area is the same as the face's area <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   If tilted 90 degrees, its shadow is a straight line with an area of zero <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Bob's Approach: Detailed Calculation

Bob seeks a precise formula for the shadow's area <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. He considers the normal vector perpendicular to the face and the angle (theta) it makes with the vertical (light direction) <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

Through [[geometric_analysis_of_light_projection | geometric analysis of light projection]], Bob determines that the area of the shadow of a single face (with side length s) is its original area (s²) multiplied by the absolute value of the cosine of theta (|cos(theta)|) <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. The absolute value is necessary because a negative cosine would imply negative area <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### Alice's Approach: High-Level View

Alice analyzes the transformations involved: a rotation that positions the shape in 3D space, followed by a flat projection into 2D space <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. She recognizes that both are [[applications_of_linear_algebra_concepts | linear transformations]] <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

From [[applications_of_linear_algebra_concepts | linear algebra]], Alice knows that for a linear transformation, the area of the output shape is a constant (the determinant) times the original area <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. This constant depends only on the rotation applied, not on the specific shape <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This property, where the proportionality constant is independent of the original shape, is crucial for Alice's generalization <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. This would not be true for a closer light source, as the projection would not be linear <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

## Alice's Key Insights on the Cube's Shadow

Alice's method involves three clever insights:

### Insight 1: Convexity and Double Cover

Alice states that for a given orientation, the area of the shadow of the whole cube is exactly one half the sum of the areas of all its faces <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. She justifies this by explaining that for a convex solid like a cube, any ray of light hitting the shadow passes through exactly two points of the cube (one entry, one exit) <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. This means the sum of the individual face shadows "double cover" the actual cube shadow <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.

This relies on the property of **convexity**: a set is convex if the line connecting any two points within the set is entirely contained within the set <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. A cube is convex, ensuring that light rays pass through it at only two points <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. This property would not hold for non-convex shapes like a donut <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

### Insight 2: Swapping Sum and Average

Using abbreviated notation (S_cube for shadow of cube, S_f for shadow of a face), Alice considers the average shadow area across many rotations <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. The key insight is that the average of the sum of the face shadows is the same as the sum of the average of the face shadows <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>. This is effectively a [[duality_in_mathematical_transformations | duality in mathematical transformations]] where summing over rotations and summing over faces can be interchanged <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.

This leads to the conclusion that the average area for the shadow of a cube is proportional to its total surface area <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. Furthermore, this proportionality constant is universal for any convex solid <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>.

## Bob's Detailed Calculation of the Proportionality Constant

While Alice focuses on generality, Bob proceeds to calculate the average shadow area for a single square face.

He models the possible orientations of the square's normal vector as points on the surface of a unit sphere <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>. He assumes a uniform probability distribution on the sphere, meaning the probability of a normal vector landing in any patch of area is proportional to that area <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. The area of the shadow of a face only depends on the angle (theta) of its normal vector to the vertical, not on rotations around that normal <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.

To find the average value of |cos(theta)| over all possible normal vectors, Bob uses an integral <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. This integral calculates the average by summing the product of the shadow area formula (s² * |cos(theta)|) and the probability of a given angle range occurring (derived from the area of a band on the sphere) <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.

The setup for the integral involves:
*   The circumference of a band on the sphere at angle theta: 2π * sin(theta) <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.
*   The area of a band: 2π * sin(theta) * d(theta) <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>.
*   Dividing by the total surface area of a unit sphere (4πr² = 4π) to get probability <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.

The integral Bob computes is:
Average Shadow Area (square) = (s² / (4π)) * ∫[0 to π] |cos(theta)| * (2π * sin(theta)) d(theta) <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>
After calculation, Bob finds that the [[average_shadow_area_of_geometric_figures | average area for a square's shadow]] is precisely one half the area of that square (s²/2) <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>. This is the universal proportionality constant.

## Alice's Final Insight: The Sphere Trick

Alice's final, most delightful insight comes from the universality of the proportionality constant <a class="yt-timestamp" data-t="00:30:21">[00:30:21]</a>. Since the average shadow area of any convex solid is proportional to its surface area by the *same* constant <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>, Alice only needs to find one convex solid for which she already knows this relationship <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>.

### The Sphere as a Special Case

The most symmetric convex solid is a sphere <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.
*   No matter its orientation, the flat projection shadow of a sphere is always a circle with an area of πr² <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. This is its average shadow area.
*   The surface area of a sphere is 4πr² <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>.

Therefore, for a sphere, the average shadow area (πr²) is 1/4th of its surface area (4πr²) <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>. This immediately reveals the universal proportionality constant: 1/4.

Applying this to the cube:
Since the proportionality constant is 1/4, the average shadow area of a cube is 1/4th of its surface area <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>. For a cube with side length *s*, its surface area is 6s² <a class="yt-timestamp" data-t="00:31:42">[00:31:42]</a>.

Thus, the average shadow area of a cube = (1/4) * (6s²) = 1.5s² <a class="yt-timestamp" data-t="00:31:42">[00:31:42]</a>.

## Generalization and Nuance

Alice's argument, while elegant, relies on the assumption of flat faces for decomposing the solid into face shadows <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>. However, it can be rigorously extended to a sphere by considering a sequence of polyhedra that approximate a sphere <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>. In the limit, the properties hold, confirming the result for a sphere <a class="yt-timestamp" data-t="00:33:31">[00:33:31]</a>.

### Reflecting on Problem-Solving Styles

The contrast between Alice and Bob highlights different strengths in [[teaching_and_understanding_mathematical_concepts | mathematical exercises and problemsolving in geometry]] <a class="yt-timestamp" data-t="00:34:12">[00:34:12]</a>.
*   **Bob's detailed computations** are often more productive for specific, complex problems (e.g., a closer light source, where Alice's linear transformation assumption breaks down) <a class="yt-timestamp" data-t="00:35:38">[00:35:38]</a>. Historically, mathematicians like Cauchy (who proved this in 1832) used methods similar to Bob's, involving integrals <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>.
*   **Alice's generalized, abstract approach** offers profound insights into broader mathematical principles. Her method reveals that the result applies to a huge family of convex shapes <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>. This infatuation with generality can help solve specific cases more elegantly <a class="yt-timestamp" data-t="00:38:48">[00:38:48]</a>.

Alice's solution also suggests a quantitative way to define convexity: by taking the average area of a solid's shadow, multiplying by four, and dividing by its surface area; if the number is one, the solid is convex <a class="yt-timestamp" data-t="00:38:19">[00:38:19]</a>.

The seemingly simple question of what it means to choose a "random orientation" is complex and relates to concepts like Bertrand's paradox <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>. Both Alice and Bob implicitly define this distribution in their approaches, though Alice's definition is more subtle <a class="yt-timestamp" data-t="00:39:25">[00:39:25]</a>.