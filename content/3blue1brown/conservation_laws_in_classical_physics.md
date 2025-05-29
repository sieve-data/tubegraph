---
title: Conservation laws in classical physics
videoId: 6dTyOl1fmDo
---

From: [[3blue1brown]] <br/> 

The study of classical physics often relies on fundamental principles, including [[Conservation of energy and hidden circles | conservation of energy]] and momentum. These principles are key to understanding systems like colliding blocks, which, when idealized, can even demonstrate a surprising connection to the mathematical constant Pi <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## The Colliding Blocks Puzzle

A classic problem involves two blocks on a frictionless plane, one stationary (smaller, e.g., 1 kg) and the other moving towards it (larger, e.g., 100 kg) <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The objective is to determine the total number of collisions between the blocks and a wall to their left <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

For a mass ratio of 1 to 1, there are 3 collisions <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. With a mass ratio of 100 to 1, there are 31 collisions <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Surprisingly, for a mass ratio of 10,000 to 1, the total count is 314 <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. As the large mass increases by powers of 100, the total number of collisions consistently displays the digits of Pi <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Idealizing Assumptions

To achieve this "delightful result," several idealizing assumptions are made <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>:
*   **[[Elastic collisions in physics | Perfectly Elastic Collisions]]**: No energy is lost during collisions, meaning sounds (energy loss) are an artistic choice for visualization, not a physical reality of the model <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **Supermassive Wall**: The wall is assumed to be so massive or fixed that any momentum transferred to it results in negligible movement <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Classical Physics**: Relativistic effects are ignored, and the puzzle is treated purely within idealized classical physics <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## Fundamental Conservation Laws

For a system of colliding blocks, two primary conservation laws are relevant:

### Conservation of Energy

The kinetic energy of a moving block is defined as ½ times its mass times its velocity squared (½mv²) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. In this ideal system, the total kinetic energy of the two blocks remains constant throughout the experiment <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>, <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. This holds true as long as no energy is lost to friction or collisions <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

### Conservation of Momentum

The momentum for each block is its mass times its velocity (mv) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The total momentum of the two blocks is conserved during their collisions with each other <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>, <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. However, when a block collides with the wall, its momentum changes because some of it is transferred to the wall <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

## Problem-Solving with State Space

A powerful problem-solving principle in physics is to visualize the system <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. For the colliding blocks, where the velocities (v1 and v2) are changing, a *state space* can be drawn as a coordinate plane where the x-coordinate represents v1 and the y-coordinate represents v2 <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. As the blocks collide, the point representing their velocities moves within this space <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### The Ellipse of Energy Conservation

In this initial velocity state space, the [[Conservation of energy and hidden circles | conservation of energy]] equation (½m1v1² + ½m2v2² = constant) defines an ellipse <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. The state space point is always constrained to this ellipse <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. The initial velocity of the big block determines the total energy and thus the size of the ellipse, but it doesn't affect the final number of collisions <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

### Leveraging Symmetry: The Circle

Another principle is to respect symmetries within mathematical or physical problems <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Given the connection to Pi, which is tied to circles, it's beneficial to transform the ellipse into a circle. This can be done by redefining the coordinates:
*   x-coordinate: $\sqrt{m_1} \cdot v_1$ <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>
*   y-coordinate: $\sqrt{m_2} \cdot v_2$ <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>

In these rescaled coordinates, the conservation of energy equation becomes $x^2 + y^2 = \text{constant}$, which is the equation of a circle <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This symmetric representation simplifies the problem <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

### Momentum as a Line

In this new coordinate system, the conservation of momentum ($m_1 v_1 + m_2 v_2 = \text{constant}$) translates into a linear equation <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. The slope of this line is given by $-\sqrt{m_1/m_2}$ <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. This slope is crucial for the numerical result linked to Pi and later for understanding quantum computing analogies <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

### The Geometry of Collisions

The problem is transformed into a geometric puzzle on the circle <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>:
1.  **Block-Block Collision**: When blocks collide, the state point hops from one intersection of the momentum line with the circle to the other <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
2.  **Block-Wall Collision**: When the small block hits the wall, only its velocity sign flips, meaning the y-coordinate changes sign while the x-coordinate remains constant. This moves the point vertically on the circle <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>. The momentum line shifts horizontally to pass through this new point <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

The process continues until both blocks are moving to the right and the small block is slower than the big block, which corresponds to a specific "end zone" in the upper-right quadrant of the state space <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

Each "zig and zag" (block-wall then block-block collision) corresponds to the state point traversing an arc of constant angle, $2\theta$, on the circle <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. The angle $\theta$ is determined by the slope of the momentum line: $\tan(\theta) = \sqrt{m_2/m_1}$ <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. The number of lines drawn (total collisions) is roughly the total angle traversed (2π radians) divided by the angle of each arc (2θ), or $\pi / \theta$ <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.

### The Role of Small Angle Approximation

For large mass ratios (e.g., 10,000 to 1), $\sqrt{m_2/m_1}$ becomes a very small number (e.g., 0.01 for 10,000:1). The crucial insight is that for a small angle, $\theta$, the tangent of $\theta$ is approximately equal to $\theta$ itself ($\tan(\theta) \approx \theta$) <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>, <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. This is known as the small angle approximation <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.

Therefore, $\theta \approx \sqrt{m_2/m_1}$. When $m_1/m_2$ is a power of 100, $\sqrt{m_1/m_2}$ is a power of 10. So $\theta$ becomes a small power of 10 (e.g., 0.01 radians) <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. The number of collisions is then approximately $\pi / \theta$. If $\theta$ is a power of 10, then the result will contain the digits of Pi <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

### An Unsolved Problem?

While the small angle approximation is robust for practical purposes, ensuring that it never leads to an "off by one" error in the integer count of collisions requires knowing that the digits of Pi do not exhibit a specific pattern (e.g., a long sequence of nines) that would push the result past an integer boundary due to the small error term <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>. Rigorously proving this about Pi's digits is currently beyond the scope of mathematical tools <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>. Thus, the exact connection of colliding blocks computing Pi remains, technically, an unsolved problem <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>.

This idealization of the problem highlights how stripping away real-world messiness can expose [[Conservation of energy and hidden circles | hidden connections]] within physics and mathematics <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>. This abstract approach can reveal parallels, such as the unexpected link between this classical mechanics problem and [[Quantum mechanics basics for beginners | quantum computing]]'s Grover's Algorithm for Search <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>.