---
title: State space and conservation laws in classical physics
videoId: 6dTyOl1fmDo
---

From: [[3blue1brown]] <br/> 

The seemingly simple puzzle of two colliding blocks on a frictionless plane, rebounding off each other and a wall, provides a surprising connection to the mathematical constant pi. Beyond its recreational appeal, analyzing this system serves as a powerful demonstration of fundamental concepts in classical physics, particularly the application of [[conservation_of_energy_and_momentum | conservation laws]] and the utility of [[applications_of_phase_space_in_differential_equations | state space]] representations to clarify [[differential_equations_in_physics | dynamical situations]] <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.

## The Colliding Blocks Puzzle

The setup involves two blocks on a frictionless plane with a wall to the left <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. Initially, a smaller block on the left is stationary (e.g., 1 kg), and a larger block on the right moves towards it with some speed <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>. The goal is to determine the total number of collisions between the blocks and with the wall <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

For a mass ratio of 1:1, there are 3 collisions <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. With a ratio of 100:1, the count is 31 <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. When the ratio is 10,000:1, the total is 314 <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. For a million-to-one mass ratio, the count reaches 3,141 <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. This pattern, where the digits of pi emerge as the mass ratio increases by powers of 100, is a key observation <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>.

### Idealizing Assumptions

To achieve this "delightful result," several [[idealized_physics_in_theoretical_simulations | idealizing assumptions]] are made, stripping away the messiness of the real world to expose core connections <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a> <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>:
*   **Perfectly Elastic Collisions**: No energy is lost during collisions <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>. This implies no sound is produced <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.
*   **Massive, Fixed Wall**: The wall is assumed to be supermassive or fixed, so any momentum transfer to it results in negligible movement <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.
*   **Non-Relativistic Speeds**: For very large mass ratios, the smaller block would move so fast that relativistic effects should be considered, but these are ignored, treating it as a purely [[idealized_physics_in_theoretical_simulations | idealized classical physics]] puzzle <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a> <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.

## Conservation Laws in Classical Physics

To analyze the system, fundamental conservation laws are applied:

*   **Conservation of Energy**: For perfectly elastic collisions, the total kinetic energy of the system remains constant throughout the experiment <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a> <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>.
    *   Kinetic energy of a block: `½ * mass * velocity^2` <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>.
    *   If `m1` and `v1` are the mass and velocity of the big block, and `m2` and `v2` for the small block, the total kinetic energy `½m1v1^2 + ½m2v2^2` is conserved <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>.
*   **Conservation of Momentum**: The total momentum of the two blocks is conserved during collisions between them <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a> <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>.
    *   Momentum of a block: `mass * velocity` <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.
    *   Total momentum `m1v1 + m2v2` remains constant *except* when the small block collides with the wall <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a> <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>. The wall absorbs some momentum, causing the total momentum of the blocks to change <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>.

## Introducing State Space

A powerful problem-solving principle in physics is to **draw pictures** and visualize the system's state <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>. For this problem, where the velocities `v1` and `v2` are constantly changing, a "state space" or "velocity space" can be constructed:
*   A coordinate plane is used where the x-coordinate represents `v1` and the y-coordinate represents `v2` <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>.
*   As the blocks collide and velocities change, a single point in this space moves, its coordinates always reflecting the current `v1` and `v2` <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.
*   Studying the path of this point can yield insights into the underlying dynamics <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>. This approach is common in physics for [[differential_equations_in_physics | dynamical situations]] with multiple changing variables <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.

### Energy Conservation in State Space: The Ellipse

In the initial `(v1, v2)` state space, the [[conservation_of_energy_and_momentum | conservation of energy]] equation `½m1v1^2 + ½m2v2^2 = Constant` takes the form of an ellipse <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.
*   The ellipse is squished in the `v1` (x) direction because `m1` is typically larger than `m2` <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>.
*   The size of the ellipse depends on the total energy, which is determined by the initial velocity of the big block. Crucially, the initial velocity value itself doesn't change the *final number of collisions*, only how quickly the experiment unfolds <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.
*   As the experiment progresses, the state point is always constrained to this ellipse <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>.

### Symmetries and the Circular State Space

Another problem-solving principle is to **respect symmetries** <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>. Since the final answer involves pi (related to circles), it's desirable to transform the elliptical state space into a circular one <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.
*   A circle equation is `x^2 + y^2 = Constant` <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>.
*   By redefining the coordinates:
    *   `X = √(m1) * v1` <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>
    *   `Y = √(m2) * v2` <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>
*   The conservation of energy equation becomes `½X^2 + ½Y^2 = Constant`, or `X^2 + Y^2 = Constant`, which is the equation of a circle in this new `(X, Y)` coordinate system <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>.
*   The initial condition (big block moving left, small block stationary) corresponds to the leftmost point on this circle, as `v1` is negative and `v2` is zero <a class="yt-timestamp" data-t="11:26:00">[11:26:00]</a>.

### Momentum Conservation in State Space: The Lines

In this new circular state space, the [[conservation_of_energy_and_momentum | conservation of momentum]] `m1v1 + m2v2 = Constant` also transforms:
*   Substituting the new coordinates, the momentum equation becomes `√(m1)X + √(m2)Y = Constant` <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>.
*   This is a linear equation, representing a line in the `(X, Y)` diagram <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>.
*   The slope of this line is `-√(m1/m2)` <a class="yt-timestamp" data-t="12:43:00">[12:43:00]</a>. This slope is a critical quantity for the numerical answer <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>.
*   **Block-Block Collision**: When the blocks collide, the state point "hops" along the momentum line to the *other* intersection point with the circle <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>.
*   **Block-Wall Collision**: When the small block hits the wall, only its velocity `v2` (and thus `Y`) flips sign. This causes the state point to move vertically across the circle to the point with `Y` having the opposite sign <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>. Since momentum is transferred to the wall, the momentum line itself shifts horizontally to pass through this new point <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>.

## The Geometric Puzzle and Connection to Pi

The entire physics problem is translated into a pure geometry puzzle: starting at the leftmost point of a circle, repeatedly moving along a line of a specific slope to another point on the circle, then vertically to a new point on the circle, and so on, until the point lands in an "end zone" <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>.

*   The "end zone" is defined by both blocks moving to the right (X and Y positive quadrant) and the small block moving slower than the big block (below the line `√(m1)X = √(m2)Y`, which is perpendicular to the momentum lines) <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a> <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>.
*   Each "zig" (block-block collision) and "zag" (block-wall collision) corresponds to a step in this geometric process.
*   The key insight is that each "zig-zag" sequence sweeps out an arc of constant angular size, `2θ` radians, on the circle <a class="yt-timestamp" data-t="17:27:00">[17:27:00]</a>. This is proven using the inscribed angle theorem <a class="yt-timestamp" data-t="16:35:00">[16:35:00]</a>.
*   The angle `θ` is related to the slope of the momentum line: `tan(θ) = √(m2/m1)` <a class="yt-timestamp" data-t="20:06:00">[20:06:00]</a>.

The number of collisions is equivalent to how many of these `2θ` arcs can be traversed before entering the end zone. This is essentially asking how many times `2θ` can be added to itself before exceeding the total circumference of the circle (which is `2π` radians) <a class="yt-timestamp" data-t="18:31:00">[18:31:00]</a> <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>. This simplifies to finding the largest integer `N` such that `N * θ < π` <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a> <a class="yt-timestamp" data-t="18:53:00">[18:53:00]</a>.

### The Small Angle Approximation

When the mass ratio `m1/m2` is a power of 100 (e.g., 100:1, 10,000:1), then `√(m2/m1)` is a small power of 10 (e.g., 0.1, 0.01) <a class="yt-timestamp" data-t="20:08:00">[20:08:00]</a>. The angle `θ` is then `arctan(small number)` <a class="yt-timestamp" data-t="21:01:00">[21:01:00]</a>.

A crucial insight from [[applications_of_taylor_polynomials_in_physics | applications of Taylor polynomials in physics]] is the small angle approximation, which states that for small `x`, `arctan(x) ≈ x` (or `tan(x) ≈ x`) <a class="yt-timestamp" data-t="21:14:00">[21:14:00]</a> <a class="yt-timestamp" data-t="21:43:00">[21:43:00]</a>.
*   This means `θ` is approximately a small power of 10.
*   When `θ` is `0.01` radians, for instance, `N` becomes `314`, as `314 * 0.01 = 3.14`, which is the largest integer multiple that stays below `π` <a class="yt-timestamp" data-t="19:04:00">[19:04:00]</a>.

The accuracy of this approximation for very large mass ratios is the subject of an [[unsolved_problem_in_physics_and_math | unsolved problem in physics and math]] <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a> <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. While the error `tan(θ) - θ` is of the order `θ^3` <a class="yt-timestamp" data-t="23:26:00">[23:26:00]</a>, it is theoretically possible for `N` to be off by one if `π` had a sufficiently long string of nines in its decimal expansion at a relevant point, something not observed in the known digits of pi but unproven to be impossible <a class="yt-timestamp" data-t="23:50:00">[23:50:00]</a> <a class="yt-timestamp" data-t="24:20:00">[24:20:00]</a>.

## Broader Implications

This problem, despite its [[idealized_physics_in_theoretical_simulations | idealized physics in theoretical simulations]], highlights the power of abstraction and the profound interconnections within mathematics and physics. The elegant geometric solution in state space reveals why pi appears. Furthermore, this system is deeply connected to concepts in [[relationship_between_classical_and_quantum_waves | quantum mechanics]], particularly [[polarization_and_superposition_in_quantum_mechanics | Grover's Algorithm for Search]] in quantum computing <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a> <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>, demonstrating that distilling problems to their core essence can expose unexpected analogies <a class="yt-timestamp" data-t="26:03:00">[26:03:00]</a> <a class="yt-timestamp" data-t="26:57:00">[26:57:00]</a>.