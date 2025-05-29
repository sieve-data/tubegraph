---
title: Role of linear algebra and calculus in geometry
videoId: ltLUadnCyi0
---

From: [[3blue1brown]] <br/> 

The problem of finding the average area for the shadow of a cube can be approached using two distinct problem-solving styles, personified by two students, Alice and Bob. Bob's approach emphasizes detailed calculations using calculus, while Alice's approach leverages the power of [[Understanding linear algebra | linear algebra]] and abstraction to find a general solution <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## The Cube Shadow Puzzle

The puzzle involves determining the average area of a cube's shadow when averaged over all possible orientations <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. Key assumptions for this problem include:
*   The light source is directly above the cube and effectively infinitely far away <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.
*   This setup results in a flat projection, where space coordinates (x, y, z) project to (x, y, 0) <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   The average is taken over all possible orientations for a particular cube size <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

The area of the shadow varies with orientation. For a cube with side length *s*:
*   When a face is parallel to the ground, the shadow is a square with area *s²* <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.
*   When a long diagonal is parallel to the light, the shadow is a regular hexagon with an area of √3 times the area of one of the square faces <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.

The concept of "averaging over all possible orientations" implies taking the mean of shadow areas from an infinite number of random tosses, or more formally, defining a probability distribution over the space of all orientations, often described by mathematicians as SO3 (a family of 3x3 matrices) <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.

## Bob's Approach: Calculus for Specifics

Bob prefers detailed calculations to understand concrete situations <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.

### Shadow Area of a Single Face
To find the shadow area of a single square face, Bob considers the normal vector perpendicular to that face and the angle it makes with the vertical (theta) <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.
*   If theta = 0°, the shadow area is *s²* (face parallel to ground) <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.
*   If theta = 90°, the shadow area is 0 (face perpendicular to ground) <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.

Through geometric analysis involving slicing the face and using trigonometry, Bob proves that the area of the shadow of a single face is given by `s² * |cos(theta)|` <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>. The absolute value is taken to ensure positive area <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>.

### Averaging Over Orientations Using Calculus
To find the average shadow area for a square face over all possible orientations, Bob considers the distribution of its normal vector across a unit sphere <a class="yt-timestamp" data-t="22:14:00">[22:14:00]</a>. He assumes a uniform probability distribution, meaning the likelihood of the normal vector landing in any patch of area on the sphere is proportional to that area <a class="yt-timestamp" data-t="23:01:00">[23:01:00]</a>.

Bob calculates this average using an integral, which is the continuous equivalent of summing over discrete probabilities <a class="yt-timestamp" data-t="25:05:00">[25:05:00]</a>. The setup involves:
1.  Identifying the range of theta (0 to 180 degrees or π radians) <a class="yt-timestamp" data-t="24:36:00">[24:36:00]</a>.
2.  Determining the area of a "band of latitude" on the sphere corresponding to a small range of theta (delta theta), which is approximately `2π * sin(theta) * delta_theta` <a class="yt-timestamp" data-t="26:55:00">[26:55:00]</a>.
3.  Calculating the probability of the normal vector falling into this band: `(2π * sin(theta) * delta_theta) / (4πr²) = (1/2) * sin(theta) * delta_theta` (for a unit sphere, r=1) <a class="yt-timestamp" data-t="27:21:00">[27:21:00]</a>.
4.  Multiplying this probability by the shadow area formula `s² * |cos(theta)|` and integrating over all theta values:
    ```
    Average Area = ∫[from 0 to π] (s² * |cos(theta)| * (1/2) * sin(theta)) d(theta)
    ```
    <a class="yt-timestamp" data-t="27:44:00">[27:44:00]</a>
Solving this integral, Bob finds that the average area for a square's shadow is precisely `(1/2) * s²`, or half the area of the square itself <a class="yt-timestamp" data-t="29:33:00">[29:33:00]</a>.

## Alice's Approach: Linear Algebra and Generality

Alice prefers a high-level, general overview before diving into computations <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. Her approach demonstrates the power of [[Understanding linear algebra | linear algebra]] in understanding geometric transformations.

### Linear Transformations and Area Scaling
Alice notes that the rotation of the cube and its flat projection are both [[Linear transformations in linear algebra | linear transformations]] <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>. A key concept from [[Understanding linear algebra | linear algebra]] is that applying a [[Linear transformations in linear algebra | linear transformation]] to a shape scales its area by a constant factor, known as the determinant of the transformation <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>. This constant factor depends only on the transformation (rotation), not on the original shape.

### Key Insights from Alice
Alice's solution relies on three clever insights:

#### Insight 1: Convexity and Double Coverage
For a convex solid like a cube, any ray of light passing through it enters at exactly one point and exits at exactly one point <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>. This means every point in the shadow corresponds to exactly two faces above it (one entering, one exiting). Therefore, the area of the cube's shadow for a given orientation is exactly one half the sum of the areas of all its faces <a class="yt-timestamp" data-t="14:35:00">[14:35:00]</a>. This property relies on the geometric concept of convexity <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>.

#### Insight 2: Swapping Summation Order
Alice observes that the average of a sum is equal to the sum of the averages <a class="yt-timestamp" data-t="19:44:00">[19:44:00]</a>.
*   Average(Shadow of Cube) = Average(1/2 * Sum of Face Shadows)
*   Since the constant factor (1/2) can be pulled out, and the sum of averages is the same as the average of the sum, this simplifies to:
*   Average(Shadow of Cube) = 1/2 * Sum of (Average Shadow of each Face) <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>

Because the average shadow area for any 2D object (like a face) is a universal proportionality constant times its area (as discussed with Bob's calculus results), Alice concludes that the average shadow area of the cube is proportional to its total surface area <a class="yt-timestamp" data-t="20:00:00">[20:00:00]</a>. This proportionality constant is the same for all convex solids <a class="yt-timestamp" data-t="21:16:00">[21:16:00]</a>.

#### Insight 3: Leveraging Universal Proportionality with a Sphere
Since the proportionality constant is universal for all convex solids, Alice chooses the simplest convex solid to calculate it: a sphere <a class="yt-timestamp" data-t="30:46:00">[30:46:00]</a>.
*   The shadow of a sphere, regardless of its orientation, is always a circle with area πr² <a class="yt-timestamp" data-t="30:50:00">[30:50:00]</a>.
*   The surface area of a sphere is 4πr² <a class="yt-timestamp" data-t="31:01:00">[31:01:00]</a>.
*   Therefore, for a sphere, (Average Shadow Area) / (Surface Area) = πr² / 4πr² = 1/4 <a class="yt-timestamp" data-t="31:20:00">[31:20:00]</a>.

This means the universal proportionality constant is 1/4. Alice can then apply this constant back to the cube:
*   Average Shadow Area of Cube = (1/4) * Surface Area of Cube
*   Since a cube has 6 faces, each of area *s²*, its surface area is 6*s²*.
*   Average Shadow Area of Cube = (1/4) * 6*s² = (3/2)*s² <a class="yt-timestamp" data-t="31:39:00">[31:39:00]</a>.

Alice's argument extends to spheres by considering a sequence of polyhedra approximating a sphere <a class="yt-timestamp" data-t="33:11:00">[33:11:00]</a>. As the number of faces increases, the polyhedra approach a sphere, and the ratio of average shadow area to surface area remains the constant 1/4.

## The Interplay of Calculus and Linear Algebra in Geometry

This problem highlights the distinct yet complementary roles of calculus and [[Understanding linear algebra | linear algebra]] in solving geometric problems:

*   **Calculus (Bob's approach)**: Excels at concrete calculations, dealing with continuous probabilities, and finding exact formulas for specific cases by integrating over varying parameters. It provides the [[Geometric versus numeric understanding in linear algebra | numeric understanding]] <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>. Cauchy's original proof of this problem in 1832 largely resembled Bob's calculational approach <a class="yt-timestamp" data-t="35:53:00">[35:53:00]</a>. This approach is essential for building intuition and for problems where a generalized solution isn't readily apparent (e.g., a closer light source scenario) <a class="yt-timestamp" data-t="35:38:00">[35:38:00]</a>. The importance of [[Challenges students face in learning linear algebra | computational practice]] for building intuition is significant in learning mathematics <a class="yt-timestamp" data-t="36:42:00">[36:42:00]</a>.

*   **Linear Algebra (Alice's approach)**: Provides a framework for understanding and generalizing transformations, focusing on abstract properties like linearity and convexity. It offers a [[Geometric versus numeric understanding in linear algebra | geometric understanding]] of how shapes transform and scale. This allows for elegant solutions by leveraging universal truths across a class of shapes <a class="yt-timestamp" data-t="38:48:00">[38:48:00]</a>. The abstraction inherent in [[Understanding linear algebra | linear algebra]] can be a powerful tool for solving specific problems, making it a valuable part of [[Educational resources for teaching linear algebra | mathematical education]] <a class="yt-timestamp" data-t="38:40:00">[38:40:00]</a>.

The solution demonstrates that the average shadow area for *any convex solid* is one-fourth of its surface area <a class="yt-timestamp" data-t="31:24:00">[31:24:00]</a>. This is a profound geometric result, often referred to as Cauchy's Surface Area Formula. It can even suggest ways to quantify convexity, where a ratio of one indicates a convex solid, and less than one indicates a non-convex solid <a class="yt-timestamp" data-t="38:15:00">[38:15:00]</a>.

Both approaches are vital for a complete understanding of geometric problems and for fostering effective problem-solving mindsets <a class="yt-timestamp" data-t="34:12:00">[34:12:00]</a>.