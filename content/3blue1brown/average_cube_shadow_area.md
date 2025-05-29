---
title: Average cube shadow area
videoId: ltLUadnCyi0
---

From: [[3blue1brown]] <br/> 

This article explores a puzzle involving the average area of a cube's shadow, highlighting two distinct problem-solving approaches personified by "Alice" and "Bob" <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Bob embodies a detail-oriented, calculation-heavy style <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, while Alice prefers a high-level, generalized overview before diving into computations <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## The Puzzle: Average Shadow of a Cube

The puzzle is to find the average area of a cube's shadow <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The shadow's area depends on the cube's size and its orientation <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. The "average" refers to averaging over all possible orientations for a given cube size <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

For simplicity, the light source is assumed to be directly above and infinitely far away, resulting in a flat projection (e.g., `x, y, z` projects to `x, y, 0`) <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

*   **Special Case 1: Cube upright**
    If two faces are parallel to the ground, the shadow is a square <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. For a cube with side length `s`, the shadow area is `s²` <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Special Case 2: Long diagonal parallel to light**
    The shadow forms a regular hexagon <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>, with an area of `√3` times the area of one square face <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

The definition of "averaging over all possible orientations" can be intuitively understood as repeatedly tossing the cube and taking the mean shadow area <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. More formally, it involves defining a probability distribution over the space of all 3D orientations (known as SO3) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Simplest Variant: Shadow of a Single Face

A good first step for any hard question is to consider its simplest non-trivial variant <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. In this case, finding the shadow area of a single face for a particular orientation <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Bob's Approach: Direct Calculation

Bob considers the normal vector perpendicular to the face and the angle `theta` it makes with the vertical (direction of light) <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   If `theta = 0°` (face parallel to ground), shadow area = face area (`s²`) <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   If `theta = 90°` (face perpendicular to ground), shadow area = `0` (a straight line) <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>, <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

Bob proves the area of the shadow of a single face is `Area_face * |cos(theta)|` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>, <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. The absolute value is necessary because `cosine` can be negative for `theta > 90°`, but area must be positive <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This relies on breaking the shape into slices and applying trigonometry <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Alice's Approach: General Principles

Alice views the problem through [[linear_algebra_and_determinants|linear algebra]], seeing the rotation and projection as linear transformations <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. She knows that for a linear transformation, the area of the output shape is a constant (the determinant) times the original area <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
Crucially, this proportionality constant does not depend on the specific shape being transformed <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. It only depends on the transformation itself (i.e., the rotation applied) <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

> [!NOTE] Importance of Linearity
> This linearity is key. If the light source were close, the projection would not be linear, and the area would not scale proportionally <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. Alice emphasizes that the problem's linearity allows for generalization <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

Alice deduces that the average shadow area for any 2D shape will be some universal proportionality constant times its original area <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. This constant is independent of the shape's size and form <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Cube Shadow and Face Shadows Relationship

Alice connects the shadow of the entire cube to the shadows of its individual faces.

### Alice's First Insight: Convexity and Double Cover

Alice realizes that for a convex solid like a cube, the area of its shadow for a given orientation is exactly one half the sum of the areas of all its faces <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>, <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. This is because any ray of light hitting the shadow passes through the cube at exactly two points (entry and exit) <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.

> [!INFO] What is Convexity?
> A set is convex if the line connecting any two points within the set is entirely contained within the set <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. A cube is convex, ensuring each light ray passes through exactly two faces <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. Non-convex shapes, like a donut, would not have this property <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

### Alice's Second Insight: Sum of Averages

Using compact notation (e.g., `S(R(Cube))` for the shadow area of a rotated cube) <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>, Alice writes the average shadow area as:
`Average(S(R(Cube))) = (1/N) * Σ S(R_i(Cube))` <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
Since `S(R(Cube)) = (1/2) * Σ S(R(Face_j))` for each rotation <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>, she can swap the order of summation and averaging <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>:
`Average(S(R(Cube))) = (1/2) * Σ Average(S(R(Face_j)))` <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
This means the average of the sum of face shadows is the same as the sum of the average of the face shadows <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.

Combining this with her earlier insight that the average shadow for a face is `Constant * Area_face`, she concludes that the average shadow area of the cube is proportional to its total surface area <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>, and this proportionality constant is universal for all convex solids <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>.

## Bob's Calculation of the Proportionality Constant

While Alice was generalizing, Bob was calculating the constant. He focused on finding the average value of `|cos(theta)|` for all possible normal vectors of a square face <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.

He notes that all possible unit normal vectors trace out the surface of a unit [[surface_area_of_a_sphere|sphere]] <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>. A "uniform distribution" on the sphere means the probability of a normal vector landing in any patch of area is proportional to that patch's area <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

To find the average `|cos(theta)|`, Bob sets up an integral <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. He considers small "bands of latitude" on the sphere, each with a width `delta theta` <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.
*   The radius of a band at angle `theta` is `sin(theta)` <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.
*   Its circumference is `2πsin(theta)` <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.
*   Its area is approximately `2πsin(theta) * delta_theta` <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>.
*   The probability of landing in this band is `(Area_band) / (4πr²)`, where `4πr²` is the [[surface_area_of_a_sphere|surface area of a sphere]] <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.

The average shadow area is the sum (which becomes an integral) of `(|cos(theta)| * probability_of_theta_band)` <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>, <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>.

After performing the integral (from `0` to `π` radians), Bob finds that the average area for a square's shadow is precisely one half the area of that square <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>, <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>. This is the universal constant `1/2`.

## Alice's Elegant Conclusion

Alice's critical insight is that the proportionality constant relating average shadow area to surface area is the *same* for *any* convex solid <a class="yt-timestamp" data-t="00:30:21">[00:30:21]</a>. To find this constant, she simply needs to apply it to a convex solid for which both the average shadow area and surface area are easily known <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>.

The most symmetric solid is a [[highdimensional_spheres|sphere]] <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.
*   No matter its orientation, a sphere's flat projection shadow is always a circle <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>.
*   If the sphere has radius `r`, its shadow area is `πr²` <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>. Therefore, its average shadow area is also `πr²` <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>.
*   The [[surface_area_of_a_sphere|surface area of a sphere]] is `4πr²` <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>. [[archimedes_proof_of_spheres_surface_area|Archimedes proved this millennia ago without calculus]] <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>.

By comparing the average shadow area (`πr²`) to the surface area (`4πr²`) for a sphere, Alice finds the universal proportionality constant:
`πr² / 4πr² = 1/4` <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>, <a class="yt-timestamp" data-t="00:31:24">[00:31:24]</a>.

Applying this constant to the cube:
*   A cube with side length `s` has a surface area of `6s²` <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.
*   Its average shadow area is `(1/4) * (6s²) = (3/2)s²` <a class="yt-timestamp" data-t="00:31:42">[00:31:42]</a>.

> [!NOTE] Justification for Spheres (without flat faces)
> The argument can be extended to spheres by imagining a sequence of polyhedra that increasingly approximate a sphere <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>. For each polyhedron, the average shadow area is `(1/4)` of its surface area. In the limit, this ratio holds true for the sphere <a class="yt-timestamp" data-t="00:33:31">[00:33:31]</a>.

## Reflection on Problem-Solving Styles

The contrast between Alice and Bob's methods highlights different aspects of mathematical problem-solving <a class="yt-timestamp" data-t="00:34:12">[00:34:12]</a>. Popular math often biases towards "slick" proofs (Alice's approach), which can be explained broadly <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>. Bob's detailed calculations, though fundamental, are harder to generalize for diverse audiences <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>.

Historically, complex problems like this were often solved through rigorous computation. Cauchy's 1832 proof of this fact relied on integrals similar to Bob's work <a class="yt-timestamp" data-t="00:35:56">[00:35:56]</a>. Many famous mathematicians, including Newton, Euler, and Gauss, had immense patience for tedious calculations <a class="yt-timestamp" data-t="00:37:24">[00:37:24]</a>. [[cross_product_and_parallelogram_area|Drilling computations]] builds intuition necessary for finding elegant insights <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>.

However, Alice's mindset is also crucial for seeing the "forest for the trees" <a class="yt-timestamp" data-t="00:37:44">[00:37:44]</a>. Her generalization reveals that this result applies to a huge family of shapes, not just cubes <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>. This focus on generality and abstraction is a core aspect of mathematics, as it often leads to simpler solutions for specific cases <a class="yt-timestamp" data-t="00:38:40">[00:38:40]</a>.

Alice's approach also suggests a way to quantify [[highdimensional_geometry_and_cube_coloring|convexity]]: `(4 * Average_Shadow_Area) / Surface_Area`. If this ratio is one, the solid is convex; if less than one, it is non-convex, with the value indicating its proximity to convexity <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.

### The Unanswered Question: Random Orientation

The puzzle's premise of "choosing a random orientation" introduces a subtle challenge in probability. While Bob implicitly defines this by using a uniform distribution on the normal vectors on the [[surface_area_of_a_sphere|sphere]], Alice's definition is less obvious <a class="yt-timestamp" data-t="00:39:25">[00:39:25]</a>. This topic is further explored in Bertrand's Paradox <a class="yt-timestamp" data-t="00:39:18">[00:39:18]</a>.