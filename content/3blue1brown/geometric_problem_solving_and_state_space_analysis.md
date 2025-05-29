---
title: Geometric problem solving and state space analysis
videoId: 6dTyOl1fmDo
---

From: [[3blue1brown]] <br/> 

When tackling complex mathematical or physics problems, [[problemsolving_strategies_in_mathematics | drawing pictures]] and utilizing visual intuition can be incredibly helpful for thinking about things in different ways and exposing solutions <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>. This approach is particularly effective when dealing with dynamical situations involving multiple changing numbers, where packaging these numbers as a single point in a higher-dimensional space can clarify the entire problem <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>. This concept is often referred to as a "state space" <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>. This specific state space holds a key connection to [[Grover's Algorithm for Search | quantum computing]] <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.

## State Space Analysis in Colliding Blocks Problem

The problem of two colliding blocks on a frictionless plane serves as an excellent illustration of [[Geometric problem solving and state space analysis | geometric problem solving]] and state space analysis <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>. The objective is to determine the total number of collisions between the blocks and a wall <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

To analyze this, two key conservation laws are relevant:
*   **Conservation of Energy** <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>: The total kinetic energy of the system remains constant throughout the experiment, assuming perfectly elastic collisions <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>, <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>. The total kinetic energy is expressed as `½ m1 v1² + ½ m2 v2²` <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.
*   **Conservation of Momentum** <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>: The total momentum `m1 v1 + m2 v2` <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a> of the blocks is conserved during collisions between them <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>, but changes when a block collides with the wall, which is assumed to be supermassive <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.

### Constructing the State Space

In the context of the colliding blocks, the changing values are the velocities of the two blocks, `v1` (big block) and `v2` (small block) <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>. These can be encoded as coordinates in a 2D plane: `v1` as the x-coordinate and `v2` as the y-coordinate <a class="yt-timestamp" data-t="07:58:00">[07:58:00]</a>. As the experiment unfolds, the point representing `(v1, v2)` moves around this "velocity space" <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.

In this `(v1, v2)` coordinate system:
*   The conservation of energy `½ m1 v1² + ½ m2 v2² = Constant` is the equation for an **ellipse** <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>.
*   The conservation of momentum `m1 v1 + m2 v2 = Constant` is the equation for a **line** <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>.

#### Respecting Symmetries: Transforming to a Circle

One of the general [[problemsolving_strategies_in_mathematics | problem-solving principles]] in mathematics is to respect symmetries <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>. Since the problem's answer relates to pi, which is connected to circles, it is more natural and promising to work with a circle instead of an ellipse <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>.

This can be achieved by redefining the state space coordinates:
*   Let `x = √(m1) v1` <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>
*   Let `y = √(m2) v2` <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>

In these new coordinates, the conservation of energy becomes `x² + y² = Constant` <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>, which is the equation for a **circle** <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. The size of the circle depends on the initial total energy, but the final collision count is independent of the initial velocity <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>. The conservation of momentum `√(m1) x + √(m2) y = Constant` becomes a **line** in this new coordinate system with a slope of `-√(m1/m2)` <a class="yt-timestamp" data-t="12:43:00">[12:43:00]</a>, <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>. This slope is critical for finding the numerical answer related to pi <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>.

### Translating Physics to Geometry

By transforming the problem into this circular state space, a complex physics question is translated into a pure [[Geometric problem solving and state space analysis | geometry]] question <a class="yt-timestamp" data-t="14:59:00">[14:59:00]</a>. The process of collisions is visualized as a point moving around the circle:
1.  **Block-to-block collision**: The point hops to the other intersection of the momentum line with the circle <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>.
2.  **Block-to-wall collision**: The y-coordinate flips sign (velocity reverses), and the momentum line shifts to pass through this new point <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>.

The process continues until both blocks are moving to the right (x and y coordinates are positive) and the small block is moving slower than the big block (below a specific line in the state space), marking the "end zone" <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>, <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>. Each zig-zag movement (block-to-block collision followed by block-to-wall collision) corresponds to dropping an arc on the circle <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>.

### Geometric Analysis and Pi

Analyzing the arcs on the circle reveals that each zig-zag covers an angle of exactly `2 * theta` along the circumference <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>. The angle `theta` is related to the slope of the momentum line <a class="yt-timestamp" data-t="17:24:00">[17:24:00]</a>. Specifically, `tan(theta) = √(m2/m1)` <a class="yt-timestamp" data-t="20:50:00">[20:50:00]</a>.

The total number of collisions corresponds to how many `2 * theta` arcs can be fit onto the circle's circumference (2 pi radians) without exceeding it <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>. This is equivalent to finding the largest integer `N` such that `N * theta < pi` <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>, <a class="yt-timestamp" data-t="18:53:00">[18:53:00]</a>.

#### The Small Angle Approximation

When the mass ratio `m1/m2` is a power of 100, `√(m2/m1)` becomes a small power of 10 <a class="yt-timestamp" data-t="19:44:00">[19:44:00]</a>. For small angles, `arctan(x)` is approximately `x` (or `tan(theta)` is approximately `theta`) <a class="yt-timestamp" data-t="21:14:00">[21:14:00]</a>. This is known as a small angle approximation <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>. Due to this approximation, the number of collisions is the integer whose digits match pi <a class="yt-timestamp" data-t="22:42:00">[22:42:00]</a>.

For example, with a mass ratio of 100 to 1, `tan(theta) = 0.1`, so `theta = arctan(0.1)` <a class="yt-timestamp" data-t="20:56:00">[20:56:00]</a>, <a class="yt-timestamp" data-t="21:01:00">[21:01:00]</a>. The number of collisions is 31 <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>, <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. For 10,000 to 1, it's 314 <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. For 1,000,000 to 1, it's 3141 <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.

> [!NOTE|Unsolved Problem]
> While the small angle approximation explains the connection, rigorously proving that the final integer count never differs from pi's digits by one due to approximation error is currently beyond the scope of mathematical tools <a class="yt-timestamp" data-t="24:23:00">[24:23:00]</a>. This means the full connection of colliding blocks to pi's digits is technically an unsolved problem <a class="yt-timestamp" data-t="24:32:00">[24:32:00]</a>.

## Justification for Abstraction

Stripping away the messiness of the real world (e.g., assuming perfectly elastic collisions, frictionless planes, supermassive walls, ignoring relativistic effects) <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>, <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a> allows for problem simplification and deeper insights <a class="yt-timestamp" data-t="25:23:00">[25:23:00]</a>.
*   **Simplification**: Starting with the simplest variant of a problem provides a first approximation of reality, which can then be slowly modified to account for real-world details <a class="yt-timestamp" data-t="25:33:00">[25:33:00]</a>.
*   **Exposing Hidden Connections**: Purity in problem definition can reveal unexpected relationships <a class="yt-timestamp" data-t="26:03:00">[26:03:00]</a>. For instance, this block collision problem has an analogy to a beam of light bouncing between two mirrors <a class="yt-timestamp" data-t="26:14:00">[26:14:00]</a>, and a deeper connection to [[Grover's Algorithm for Search | quantum computing]] <a class="yt-timestamp" data-t="26:34:00">[26:34:00]</a>. These hidden connections are how mathematicians make progress, as a confusing problem in one context might become clearer in another <a class="yt-timestamp" data-t="27:06:00">[27:06:00]</a>.