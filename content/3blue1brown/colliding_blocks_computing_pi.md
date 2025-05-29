---
title: Colliding blocks computing pi
videoId: 6dTyOl1fmDo
---

From: [[3blue1brown]] <br/> 

In 2019, a video was released demonstrating how two colliding blocks can compute pi, which became the most popular content from its creator <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This phenomenon involves a surprising connection to pi, though the full connection is technically an unsolved problem <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>, <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The mechanism is also secretly connected to quantum computing, specifically [[grovers_algorithm_for_search | Grover's Algorithm for Search]] <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## The Puzzle Setup

The original puzzle involves two blocks on a frictionless plane <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Initially, the block on the left (e.g., 1 kilogram) is stationary, and the block on the right approaches with some speed <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. There is a wall to the left <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The goal is to determine the total number of collisions, including those with the wall <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Collision Examples

*   **Mass ratio 1:1:** If both blocks have the same mass, the total collision count is 3 <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Mass ratio 100:1:** If the right block is 100 kilograms and the left is 1 kilogram, the total collision count is 31 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **Mass ratio 10,000:1:** The count is 314 <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Mass ratio 1,000,000:1:** The count is 3,141 <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

As the large mass grows by powers of 100, the total number of collisions consistently has the same digits as pi <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### Idealized Assumptions

To achieve this "delightful result," several idealizing assumptions are made:
*   **Perfectly [[physics_of_elastic_collisions | elastic collisions]]:** No energy is lost during collisions <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Fixed wall:** The wall is considered supermassive or fixed, so its movement is negligible <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>, <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   **Classical physics:** Relativistic effects are ignored, even when velocities might become very high <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

These assumptions strip away the messiness of the real world, allowing for the exposure of hidden mathematical connections <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>, <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.

## Problem-Solving Approach

The problem can be solved using general problem-solving principles <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>:

### 1. List Relevant Equations
For colliding blocks, the conservation laws of energy and momentum are relevant <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Kinetic Energy:** $E = \frac{1}{2}m_1v_1^2 + \frac{1}{2}m_2v_2^2$ (conserved throughout the experiment) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>, <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
*   **Momentum:** $P = m_1v_1 + m_2v_2$ (conserved when blocks collide with each other, but changes when a block hits the wall) <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>, <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

### 2. Draw Pictures (State Space)
Since the velocities $v_1$ and $v_2$ are changing, a coordinate plane can be drawn where the x-axis represents $v_1$ and the y-axis represents $v_2$ <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>, <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. As the experiment unfolds, the point $(v_1, v_2)$ moves through this "state space" <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### 3. Respect Symmetries (Transforming to a Circle)
The conservation of energy equation ($ \frac{1}{2}m_1v_1^2 + \frac{1}{2}m_2v_2^2 = \text{constant} $) describes an ellipse in the $(v_1, v_2)$ state space <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>, <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. To leverage the connection to pi, which relates to circles, the coordinate system can be rescaled to transform the ellipse into a circle <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>, <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

New coordinates are defined as:
*   $x = \sqrt{m_1} v_1$ <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>
*   $y = \sqrt{m_2} v_2$ <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>

In these rescaled coordinates, the conservation of energy equation becomes $x^2 + y^2 = \text{constant}$, which is the equation for a circle <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. The initial state of the system, where the big block has a negative velocity and the small block is stationary, corresponds to the leftmost point of this circle ($y=0$, $x<0$) <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

## Geometric Solution in State Space

In this circular state space:
*   **Block-block collision:** The conservation of momentum ($ \sqrt{m_1}x + \sqrt{m_2}y = \text{constant} $) is a linear equation, representing a line with a slope of $ -\sqrt{\frac{m_1}{m_2}} $ <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>, <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. A collision between blocks means the state point hops from its current position on the circle to the other intersection point of the momentum line with the circle <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>, <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   **Block-wall collision:** The small block hitting the wall simply flips the sign of its y-coordinate ($v_2 \rightarrow -v_2$), causing the point to move straight up or down across the x-axis to a new point on the circle <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>. This changes the total momentum, so a new momentum line is drawn through the new point <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

The process continues by alternating between these two types of movements until the experiment ends <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. The experiment is complete when both blocks are moving to the right ($x>0, y>0$) and the little block is moving slower than the big block ($v_1 > v_2$), which translates to a specific "end zone" in the state space <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>, <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

The problem transforms into counting how many "zig-zags" (lines) are drawn on the circle <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

### Connecting to Pi via Angles

The key observation is that each movement (collision) along the circle corresponds to an arc of the same size <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>, <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
*   Using the inscribed angle theorem, the angle between the vertical line and the diagonal momentum lines (let's call it $\theta$) is related to the arc length covered by each step on the circle <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>, <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.
*   Each step covers an angle of exactly $2\theta$ radians around the center of the circle <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>, <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.
*   The process stops when the total angular distance covered reaches the circumference of the circle, which is $2\pi$ radians <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
*   The number of lines (collisions) is approximately $N = \frac{2\pi}{2\theta} = \frac{\pi}{\theta}$ <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.

The slope of the momentum line is $-\sqrt{\frac{m_1}{m_2}}$ <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>, and the tangent of the angle $\theta$ is $\sqrt{\frac{m_2}{m_1}}$ <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.
For a mass ratio of 100:1 ($m_1=100, m_2=1$), $\tan(\theta) = \sqrt{\frac{1}{100}} = 0.1$ <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
The angle $\theta = \arctan(0.1)$ <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

### Small Angle Approximation

The reason the number of collisions aligns with the digits of pi is due to the small angle approximation <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>, which states that for small angles, $\tan(\theta) \approx \theta$ (when $\theta$ is in radians) <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.
So, if $\tan(\theta)$ is a clean power of 10 (e.g., 0.1, 0.01), then $\theta$ is approximately that same power of 10 <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>, and thus the number of collisions $N \approx \frac{\pi}{\theta}$ will have the same digits as pi <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.

## The Unsolved Problem

While the small angle approximation is robust (error is on the order of $\theta^3$ via Taylor approximation) <a class="yt-timestamp" data-t="00:23:33">[00:23:33]</a>, it's theoretically possible for the total number of collisions to be off by one if a sequence of digits in pi were to be all nines (e.g., 3.14159999...) <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>. Proving that this does not happen for pi's digits is currently beyond the scope of mathematical tools <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>, making the precise correspondence between colliding blocks and pi's digits an unsolved problem from a rigorous mathematical standpoint <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>, <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## Significance of the Puzzle

This puzzle, while idealized, serves as an excellent general problem-solving lesson <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>, <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>, <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Stripping away real-world messiness often exposes hidden connections <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>. For example, this problem has an analogy to a beam of light bouncing between two mirrors <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>, <a class="yt-timestamp" data-t="00:26:14">[00:26:14]</a>. Most surprisingly, the solution is secretly mirrored in an algorithm within quantum computing <a class="yt-timestamp" data-t="00:26:34">[00:26:34]</a>. The purity of the idealized problem allows for the discovery of such fundamental links between seemingly unrelated fields <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>.