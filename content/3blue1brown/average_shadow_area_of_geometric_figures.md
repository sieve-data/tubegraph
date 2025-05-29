---
title: Average shadow area of geometric figures
videoId: ltLUadnCyi0
---

From: [[3blue1brown]] <br/> 

This article explores the problem of finding the average area of the shadow of a cube, examining two distinct problem-solving approaches: a calculation-focused method (Bob) and a high-level, generalized method (Alice) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. The primary focus is on shadows formed by a light source positioned directly above and effectively infinitely far away, resulting in a flat projection <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.

## Defining "Average Area"

The problem asks for the average shadow area over "all possible orientations" <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
Intuitively, this can be understood as the mean area obtained by tossing the object (e.g., a cube like a die) many times, freezing it, and recording its shadow area <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. The true average is what this experimental mean approaches with infinitely many tosses <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

More formally, this requires defining a [[probability_in_geometry | probability distribution]] over the space of all possible orientations, which mathematicians refer to as SO3 (Special Orthogonal Group of 3x3 matrices) <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.

### Initial Examples: Cube Shadow Area

*   **Straight Up:** When a cube (with side length *s*) is oriented with two faces parallel to the ground, its shadow is a square with an area of *s²* <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.
*   **Long Diagonal Parallel to Light:** When the cube's long diagonal is parallel to the light, its shadow forms a regular hexagon with an area of *√3* times the area of one of its square faces <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.

## Problem-Solving Approaches

### Bob's Approach: Calculation-Focused

Bob prioritizes detailed calculations <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. His first step is to calculate the shadow area of a single face.

#### Shadow Area of a Single Face

For a single flat face, Bob considers the normal vector perpendicular to it <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>. The area of its shadow depends on the angle (θ) this normal vector makes with the vertical (direction of light) <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.

*   If θ = 0° (face parallel to ground), shadow area = face area (*s²*) <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.
*   If θ = 90° (face perpendicular to ground), shadow area = 0 (a straight line) <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.

Through [[geometric_analysis_of_light_projection | geometric reasoning]], Bob proves that the area of the shadow of a single face is the area of the face multiplied by the absolute value of cos(θ) <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>, <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>. This means `Area_shadow = Area_face * |cos(θ)|` <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>. The absolute value is necessary because angles greater than 90° would yield negative cosines, and area cannot be negative <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>.

#### Averaging the Shadow Area of a Face

To find the average shadow area of a single square face over all possible orientations, Bob uses integral calculus <a class="yt-timestamp" data-t="24:09:00">[24:09:00]</a>. He notes that the normal vectors of all possible orientations trace out the [[surface_area_of_a_sphere | surface of a sphere]] (unit sphere of radius 1) <a class="yt-timestamp" data-t="22:21:00">[22:21:00]</a>, <a class="yt-timestamp" data-t="22:27:00">[22:27:00]</a>. He assumes a uniform [[probability_in_geometry | probability distribution]] on this sphere, meaning the probability of a normal vector landing in any patch of area is proportional to that area <a class="yt-timestamp" data-t="23:01:00">[23:01:00]</a>.

The average value of `|cos(θ)|` over the sphere is computed using an integral. The process involves:
1.  Discretizing the sphere into "bands of latitude" with width *Δθ* <a class="yt-timestamp" data-t="26:17:00">[26:17:00]</a>.
2.  Calculating the area of each band, which is approximately `2π * sin(θ) * Δθ` for a unit sphere <a class="yt-timestamp" data-t="26:55:00">[26:55:00]</a>.
3.  The probability of a normal vector falling into a band is `(Area_band) / (Total surface area of sphere)` <a class="yt-timestamp" data-t="27:21:00">[27:21:00]</a>. (Total surface area of a unit sphere is `4πr²`, so `4π` for `r=1`) <a class="yt-timestamp" data-t="27:25:00">[27:25:00]</a>.
4.  Multiplying this probability by the shadow area formula `|cos(θ)|` for that angle <a class="yt-timestamp" data-t="27:44:00">[27:44:00]</a>.
5.  Summing these products and taking the limit as *Δθ* approaches zero, which becomes an integral <a class="yt-timestamp" data-t="28:46:00">[28:46:00]</a>.

The resulting integral to find the average value of `|cos(θ)|` over all possible normal vector orientations (i.e., over the surface of a sphere) yields a value of `1/2` <a class="yt-timestamp" data-t="29:33:00">[29:33:00]</a>.
Therefore, Bob finds that the average area for a square's shadow is precisely `1/2` times the area of that square <a class="yt-timestamp" data-t="29:38:00">[29:38:00]</a>.

### Alice's Approach: High-Level and Generalized

Alice seeks a general overview before detailed computations <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. She recognizes that both rotation and flat projection are linear transformations <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>. This means the shadow area is proportional to the original area, with a constant factor (the determinant of the transformation) independent of the original shape <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>, <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>. This linearity is crucial and would not hold for a closer light source <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>.

#### Insight 1: [[general_principles_of_surface_area_for_convex_shapes | Convexity]] and Double Cover

Alice's first key insight is that for any convex solid (like a cube), the area of its shadow for a given orientation is exactly **one half the sum of the areas of all of its faces** <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>. This is because each ray of light passing through the object hits exactly two faces: one when it enters and one when it exits <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>. This property relies on the definition of [[general_principles_of_surface_area_for_convex_shapes | convexity]], where a line connecting any two points within the set remains entirely within the set <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>. Non-convex shapes (like a donut) would not have this property <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>.

#### Insight 2: Swapping Summation and Averaging

Using compact notation (S(Cube) for shadow area of cube, S(Fj) for shadow area of face j), Alice writes:
`S(Rotation(Cube)) = 1/2 * Σ S(Rotation(Fj))` <a class="yt-timestamp" data-t="17:34:00">[17:34:00]</a>.

To find the average shadow area of the cube, she averages this expression over many rotations. Her second insight is that the average of the sum of the face shadows is the same as the sum of the average of the face shadows <a class="yt-timestamp" data-t="19:44:00">[19:44:00]</a>. This allows her to deduce that the average area for the shadow of a cube is proportional to its [[surface_area_of_a_sphere | surface area]] <a class="yt-timestamp" data-t="20:11:00">[20:11:00]</a>.

### The Universal Proportionality Constant

Alice realizes that this proportionality constant is universal for *any* convex solid <a class="yt-timestamp" data-t="21:16:00">[21:16:00]</a>, <a class="yt-timestamp" data-t="30:26:00">[30:26:00]</a>.

#### Insight 3: The Sphere

Alice's final, most elegant insight is to apply this principle to a shape whose shadow area is trivial to calculate: a sphere <a class="yt-timestamp" data-t="30:37:00">[30:37:00]</a>, <a class="yt-timestamp" data-t="30:46:00">[30:46:00]</a>.
*   No matter its orientation, the flat projection shadow of a sphere is always a circle with area `πr²` <a class="yt-timestamp" data-t="30:50:00">[30:50:00]</a>. Thus, its average shadow area is `πr²` <a class="yt-timestamp" data-t="30:58:00">[30:58:00]</a>.
*   The [[surface_area_of_a_sphere | surface area of a sphere]] is `4πr²` <a class="yt-timestamp" data-t="31:01:00">[31:01:00]</a>.

Comparing these:
`Average Shadow Area (Sphere) = πr²`
`Surface Area (Sphere) = 4πr²`

The ratio is `(πr²) / (4πr²) = 1/4`.
Therefore, the universal proportionality constant relating average shadow area to [[surface_area_of_a_sphere | surface area]] for any convex solid is `1/4` <a class="yt-timestamp" data-t="31:20:00">[31:20:00]</a>, <a class="yt-timestamp" data-t="31:24:00">[31:24:00]</a>.

Although a sphere does not have flat faces, Alice's argument can be rigorously extended by imagining a sequence of polyhedra that successively approximate a sphere <a class="yt-timestamp" data-t="33:08:00">[33:08:00]</a>. The ratio holds true for each polyhedron, and in the limit, it holds for the sphere <a class="yt-timestamp" data-t="33:31:00">[33:31:00]</a>.

### Solution for the Cube

Knowing the universal constant `1/4`, Alice can now solve the original problem for the cube.
*   The cube has 6 faces. If its side length is *s*, each face has an area of *s²* <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.
*   The [[surface_area_of_a_sphere | surface area of the cube]] is `6 * s²` <a class="yt-timestamp" data-t="31:39:00">[31:39:00]</a>.

Using the derived constant:
`Average Shadow Area (Cube) = 1/4 * Surface Area (Cube)`
`Average Shadow Area (Cube) = 1/4 * (6s²) = 3/2 * s²` <a class="yt-timestamp" data-t="31:39:00">[31:39:00]</a>.

This demonstrates that the average shadow area of a cube is `1.5` times the area of one of its faces <a class="yt-timestamp" data-t="31:39:00">[31:39:00]</a>.

## Comparison of Approaches and Implications

*   **Bob's strength:** Ability to dive into concrete calculations and derive precise formulas, crucial for understanding specific cases or harder problems (e.g., closer light source where projections are non-linear) <a class="yt-timestamp" data-t="35:38:00">[35:38:00]</a>. This approach was similar to how Cauchy proved the general fact in 1832 <a class="yt-timestamp" data-t="35:56:00">[35:56:00]</a>.
*   **Alice's strength:** Identifying general principles and abstracting concepts, leading to elegant solutions and deeper understanding of a problem's universal properties <a class="yt-timestamp" data-t="30:06:00">[30:06:00]</a>, <a class="yt-timestamp" data-t="38:40:00">[38:40:00]</a>. Her method highlights that the specific shape (cube vs. dodecahedron vs. sphere) doesn't change the universal proportionality constant <a class="yt-timestamp" data-t="31:47:00">[31:47:00]</a>.

This problem illustrates how [[challenges_in_solving_geometric_problems | problem-solving]] often benefits from a blend of both detailed calculation and high-level generalization. The [[geometric_reasoning_and_sphere_surface_area | geometric reasoning and sphere surface area]] is a key part of this. The intuitive understanding gained from doing extensive calculations can often lead to the insights needed for more general, elegant proofs <a class="yt-timestamp" data-t="37:34:00">[37:34:00]</a>.

The concept of a [[surface_area_of_a_sphere_visual_proof | surface area of a sphere visual proof]] and [[surface_area_of_a_sphere_versus_its_shadow | surface area of a sphere versus its shadow]] are related to this problem. The [[mathematical_concepts_of_shadows_and_projections | mathematical concepts of shadows and projections]] are fundamental here.