---
title: Basics and significance of differential equations
videoId: p_di4Zn4wz4
---

From: [[3blue1brown]] <br/> 

Differential equations are a fundamental language of physics, used to express its laws <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This language extends beyond physics, adding a new perspective to how the world is viewed <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. These equations arise when it's simpler to describe change rather than absolute amounts <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For example, it's easier to explain why population sizes grow or shrink than their specific values at a given time <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. In Newtonian mechanics, motion is described by force, which determines acceleration—a statement about change <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Types of Differential Equations

Differential equations primarily come in two forms:

*   **[[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | Ordinary Differential Equations (ODEs)]]**: These involve functions with a single input, often conceptualized as time <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. They describe a finite collection of values changing over time <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **[[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | Partial Differential Equations (PDEs)]]**: These deal with functions that have multiple inputs <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. [[partial_differential_equations_and_boundary_conditions | PDEs]] often describe a continuum of values changing over time, such as temperature at every point of a solid body or fluid velocity at every point in space <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

Most physical phenomena, especially in physics, are expressed as second-order differential equations, meaning the highest derivative present is a second derivative <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

> "The sensation you get when really meditating on one of these equations is one of solving an infinite continuous jigsaw puzzle." <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>

## Basic Example: Projectile Motion

Consider the trajectory of an object thrown in the air <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Near Earth's surface, gravity causes a downward acceleration of 9.8 meters per second per second, denoted as `g` <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

Focusing on the y-coordinate as a function of time, its first derivative represents vertical velocity, and its second derivative represents vertical acceleration <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
Let `y-dot` be the first derivative and `y-double-dot` be the second derivative <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. The equation for projectile motion is:
`y-double-dot = -g` <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>

This simple [[solving_differential_equations_with_examples | differential equation]] can be solved by integration, essentially working backward <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>:
1.  **To find velocity**: What function has `-g` as a derivative? `negative g times t`, plus an initial velocity (integration constant) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
2.  **To find position**: What function has `negative gt + initial velocity` as a derivative? `negative one-half g times t squared + initial velocity times t`, plus an initial position (another integration constant) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

This demonstrates how a function's behavior can be determined from information about its rate of change, with initial conditions providing the necessary "degrees of freedom" to find a specific solution <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Complexity and Challenges

Things become more intricate when forces acting on a body depend on its position, such as in the study of planetary motion where gravity is not constant <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. In these cases, the rate of change of velocity (acceleration) is a function of position, leading to a dynamic interaction between mutually dependent variables <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. This often means finding a function whose derivative(s) are defined in terms of the function itself <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

A deceptively simple example is the pendulum <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. While introductory physics classes often approximate its motion as harmonic (a sine wave) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, this is only accurate for small angles <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. An actual pendulum's period lengthens as it's pulled farther out, and its plot of angle versus time deviates from a sine wave <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

The differential equation for a pendulum, including air resistance (dampening), is:
`theta-double-dot = -g/L * sin(theta) - mu * theta-dot` <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a> (derived from <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a> and <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>)
Here, `g` is gravity, `L` is pendulum length, `theta` is the angle, `theta-dot` is angular velocity, `theta-double-dot` is angular acceleration, and `mu` accounts for air resistance <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. The presence of `sin(theta)` in the equation is precisely why real pendulums do not oscillate with a perfect sine wave pattern <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

This example highlights a key truth: differential equations are often very difficult to solve analytically <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Even without the dampening term, an analytic solution is hilariously complicated <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. More often, an exact analytic solution isn't known at all <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

## Understanding Through Phase Space

Given the difficulty of finding exact analytic solutions, the study of differential equations often bypasses direct solution to build understanding and enable computations directly from the equations <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

One powerful tool for this is **[[applications_of_phase_space_in_differential_equations | phase space]]** <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. A [[applications_of_phase_space_in_differential_equations | phase space]] visualizes all possible states of a system <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. For the pendulum, its state can be described by two numbers: its angle (`theta`) and its angular velocity (`theta-dot`) <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. Each point in this two-dimensional [[applications_of_phase_space_in_differential_equations | phase space]] represents a unique state, or possible initial condition, of the pendulum <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. Knowing the initial angle and angular velocity allows prediction of how the system evolves <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

*   **Trajectory Visualization**: A typical pendulum trajectory in [[applications_of_phase_space_in_differential_equations | phase space]] appears as an inward spiral <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. This means the pendulum's peak velocity and displacement decrease with each swing, as it loses energy to air resistance <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. The point in [[applications_of_phase_space_in_differential_equations | phase space]] is "attracted" to the origin (where `theta` and `theta-dot` are both 0), representing the pendulum coming to rest <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
*   **Vector Fields**: A [[applications_of_phase_space_in_differential_equations | differential equation]] can be visualized as a vector field in [[applications_of_phase_space_in_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. The system's state is a vector (`theta`, `theta-dot`), and its derivative (`theta-dot`, `theta-double-dot`) gives the direction and speed of movement in the [[applications_of_phase_space_in_differential_equations | phase diagram]] <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. The second-order equation is effectively broken into a system of two first-order equations <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   **Phase Flow**: The collection of all possible trajectories in [[applications_of_phase_space_in_differential_equations | phase space]] is called **phase flow**, resembling a moving fluid <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. This allows for questions about a spectrum of initial states, not just a single one <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.
    *   **Stability**: Phase flow helps analyze stability, such as whether a fixed point (where the system is at rest) will attract or repel nearby states <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. For the pendulum, the resting position at the bottom is stable, while the perfectly balanced upright position is unstable <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.

[[applications_of_phase_space_in_differential_equations | Phase space]] is a general and powerful invention, applicable to any system of [[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | ODEs]], even those with many dimensions, like the 18-dimensional [[applications_of_phase_space_in_differential_equations | phase space]] of the three-body problem <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.

> "One of the most powerful inventions of modern science." - James Glick on [[applications_of_phase_space_in_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>

## Numerical Solutions

When exact analytic solutions are impossible, [[numerical_methods_for_solving_differential_equations | numerical methods]] provide a way to approximate solutions <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. The basic idea is to simulate the system's evolution using finite time steps <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

If starting at a point in the [[applications_of_phase_space_in_differential_equations | phase diagram]], one can take a small step equal to `delta t` (a small time step) times the vector at that point <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. Repeating this process many times yields an approximation of the function's value at time `t` <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.

For example, to compute the pendulum's angle at time `t`, a program can define `theta` and `theta-dot` based on initial conditions <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>. Then, in a loop for many small time steps (`delta_t = 0.01`), update `theta` by `theta-dot * delta_t` and `theta-dot` by `theta-double-dot * delta_t` (where `theta-double-dot` is computed from the [[differential_equations_in_physics | differential equation]]) <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.

This iterative approach is known as [[numerical_methods_for_solving_differential_equations | solving a differential equation numerically]] <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>. More sophisticated [[numerical_methods_for_solving_differential_equations | numerical methods]] exist to balance accuracy and efficiency <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.

## Limitations: Chaos Theory

Despite these methods, there are further limits to understanding and predicting systems using [[differential_equations_in_physics | differential equations]]. Chaos theory, a field that emerged in the last century, reveals that for some systems, minor variations in initial conditions (e.g., from imperfect measurements) lead to wildly different trajectories <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>. The three-body problem, for instance, is known to contain elements of chaos <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>. This means that for chaotic systems, even exact solutions might be useless for long-term prediction <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>. However, this inherent complexity also suggests that the intricate behaviors observed in the world can be studied within the framework of this mathematics <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>.