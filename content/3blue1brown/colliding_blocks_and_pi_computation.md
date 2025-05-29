---
title: Colliding blocks and pi computation
videoId: 6dTyOl1fmDo
---

From: [[3blue1brown]] <br/> 

In 2019, a video was released demonstrating how two colliding blocks can be used to compute the digits of pi. This concept, along with its adaptations, has become widely popular online <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This article revisits the topic, exploring previously undiscussed details and a surprising connection to quantum computing and [[Grover's Algorithm for Search | Grover's Algorithm for Search]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. While the connection to [[Pi and its formulas involving primes | pi]] is a crowd-pleaser, the full connection to [[Pi and its formulas involving primes | pi]] technically remains an unsolved problem <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## The Collision Puzzle Setup

The original setup involves two blocks on a frictionless plane <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The block on the left is initially stationary and smaller (e.g., 1 kilogram), while the block on the right approaches with some speed <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The puzzle asks for the total number of collisions, including those with a wall to the left of the blocks <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Collision Examples

*   **Equal Mass Ratio (1:1)**: If both blocks have the same mass, momentum is transferred with each collision. Including one collision with the wall, the total count is 3 <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Mass Ratio (100:1)**: If the right block is 100 kilograms, it takes more collisions to redirect its momentum. The total number of collisions is 31 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Mass Ratio (10,000:1)**: For an even larger mass ratio, the smaller block gets "crammed" against the wall, resulting in a rapid burst of collisions. The total count is 314 <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Mass Ratio (1,000,000:1)**: This ratio leads to nearly 3,000 collisions in a burst, with a final count of 3,141 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

The core surprise is that as the large mass grows by powers of 100, the total number of collisions consistently displays the digits of [[Pi and its formulas involving primes | pi]] <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Idealized Assumptions

To achieve this delightful result, several idealizing assumptions are made <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>:

*   **Perfectly Elastic Collisions**: No energy is lost during collisions <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Sounds, if present, are an artistic choice to visually communicate the density of collisions <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **Classical Physics**: Relativistic effects, which would become significant for very high speeds, are ignored <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Immovable Wall**: The wall is assumed to be supermassive or fixed, so its movement due to momentum transfer is negligible <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

While these assumptions simplify reality, the phenomenon can be observed in practice for smaller ratios. For instance, students at the University of Bonn demonstrated 31 collisions with a 100:1 mass ratio <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## Connecting to Quantum Computing

The reason for the powers of 100 (as opposed to powers of 10, which might be expected in base 10) is deeply connected to why [[Grover's Algorithm for Search | search algorithms]] can be faster for quantum computers than classical ones <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. This connection will be explored in a subsequent discussion <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

## Problem-Solving Approach: The State Space

Solving this puzzle effectively involves applying general problem-solving principles <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>:

1.  **List Relevant Equations**: The [[algorithm_for_computing_pi_using_physics | problem]] involves colliding blocks, so the conservation of energy and conservation of momentum are relevant laws <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
    *   Kinetic energy ($½mv^2$) for each block, with the total kinetic energy conserved throughout the experiment <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
    *   Momentum ($mv$) for each block, with the total momentum conserved during block-to-block collisions (but not when the small block hits the wall) <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

2.  **Draw Pictures/Visualize**: Representing the changing velocities ($v1$ and $v2$) in a coordinate plane ($v1$ on x-axis, $v2$ on y-axis) creates a "state space" <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. As the experiment unfolds, a point representing the velocities moves within this space <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### Transforming to a Circular State Space

In this state space, the conservation of energy equation ($½m_1v_1^2 + ½m_2v_2^2 = \text{constant}$) describes an ellipse <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. To leverage the connection to [[pis_relationship_to_circles_and_geometry | pi]] more directly, respecting symmetry is key <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. By redefining the coordinates:
*   $X = \sqrt{m_1}v_1$
*   $Y = \sqrt{m_2}v_2$

The energy conservation equation transforms into $X^2 + Y^2 = \text{constant}$, which is the equation of a circle <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. This rescaled coordinate system directly relates to the energy of each block <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

In this circular state space:
*   **Initial State**: The big block approaches from the left (negative $v1$), and the small block is stationary ($v2=0$), so the starting point is the leftmost point of the circle <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
*   **Block-to-Block Collision**: The conservation of momentum in these new coordinates is a linear equation in X and Y <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. This means a collision causes the state point to move along a straight line with a slope of $-\sqrt{m_1/m_2}$ to another point on the circle <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. This slope value is crucial for determining the numerical answer <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Collision with Wall**: The small block bouncing off the wall only flips the sign of its velocity, so the Y-coordinate flips <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>. This shifts the momentum line, which then intersects the circle at a new point <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   **Experiment Ends**: The experiment concludes when both blocks are moving to the right ($X > 0, Y > 0$) and the small block is moving slower than the big block ($v_1 > v_2$) <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. In the rescaled coordinates, this defines an "end zone" bounded by a line with a slope of $\sqrt{m_2/m_1}$ <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

This transformation converts the physics problem into a pure geometry problem: how many times does the point "zig and zag" (reflect along a diagonal line, then vertically) around the circle until it enters the "end zone"? <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>

## The [[Relationship between counting and pi | Relationship between Counting and Pi]]

The key insight comes from observing the arcs formed by the points where the lines hit the circle <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. These arcs are of equal size due to the inscribed angle theorem <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. Each "zig" or "zag" corresponds to covering an angle of $2\theta$ radians along the circle, where $\theta$ is the angle between the vertical lines and the diagonal lines <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

The process continues until the total angle covered is just under $2\pi$ radians (the full circumference of the circle) <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. The number of collisions (lines drawn) is the largest integer $N$ such that $N \times (2\theta)$ is less than $2\pi$ <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. This simplifies to $N < \pi/\theta$ <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.

### Slope, Angle, and the Small Angle Approximation

The slope of the diagonal lines in the state space is $-\sqrt{m_1/m_2}$ <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. The tangent of the angle $\theta$ is related to the inverse of this ratio: $\tan(\theta) = \sqrt{m_2/m_1}$ <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. Therefore, $\theta = \arctan(\sqrt{m_2/m_1})$ <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

For mass ratios that are powers of 100 (e.g., 100:1, 10000:1), the ratio $\sqrt{m_2/m_1}$ becomes a small power of 10 (e.g., 0.1, 0.01) <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. For small numbers, the arctangent function is very close to its input value. This is known as the small angle approximation ($\arctan(x) \approx x$ for small $x$) <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>.

Because $\theta \approx \sqrt{m_2/m_1}$ for small angles, and $\sqrt{m_2/m_1}$ is a power of 10, the number of collisions $N \approx \pi / (\text{power of 10})$ <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. This explains why the digits of the collision count match the digits of [[Pi and its formulas involving primes | pi]] <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.

### The Unsolved Problem Aspect

While the small angle approximation is incredibly accurate, a slight deviation (on the order of $\theta^3$) exists between $\tan(\theta)$ and $\theta$ itself <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>. This means there's a theoretical possibility of an "off by one" error in the final integer count if [[Pi and its formulas involving primes | pi]] were to have a sufficiently long sequence of nines in its decimal expansion at a relevant point <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>. Rigorously proving that such a sequence of nines does not occur for the digits of pi is beyond current mathematical tools, making the precise link between colliding blocks and [[Pi and its formulas involving primes | pi]] technically an unsolved problem <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>.

Nonetheless, the explicit formula for the number of collisions can be written, and the concept extends to other number bases; for example, in base two, mass ratios that are powers of four would yield the bits of [[Pi and its formulas involving primes | pi]] in binary <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.

## Justifications for Idealization

Stripping away the complexities of the real world in this problem serves two main purposes <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>:

1.  **Simplification**: Starting with the simplest possible variant provides a foundational understanding that can later be built upon to account for real-world details (e.g., energy loss could be modeled as the circle shrinking) <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>.
2.  **Exposing Hidden Connections**: Purity in mathematical problems can reveal unexpected relationships between seemingly disparate fields <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>. [[gregory_galperins_discovery_and_pi_puzzles | Gregory Galperin's discovery]] originally presented this phenomenon in the context of an analogy to light bouncing between mirrors <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>. Even more surprisingly, this entire solution is mirrored within an [[algorithm_for_computing_pi_using_physics | algorithm for computing pi using physics]] in quantum computing <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>. This highlights how abstracting problems to their core essence can clarify complex concepts and drive mathematical progress by developing a richer web of connections <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>.