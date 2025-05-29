---
title: Differential equations as a language of physics
videoId: p_di4Zn4wz4
---

From: [[3blue1brown]] <br/> 

Differential equations serve as the fundamental language through which the laws of physics are expressed <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This mathematical language extends beyond physics, adding a new perspective to understanding the world <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. [[differential_equations_and_their_applications | Differential equations]] typically arise when it's simpler to describe rates of change rather than absolute amounts <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

> "Since Newton, mankind has come to realize that the laws of physics are always expressed in the language of differential equations."
> <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a> - *Stephen Strogatz*

## Core Concepts

Understanding [[introduction_to_ordinary_and_partial_differential_equations | differential equations]] requires a basic knowledge of calculus, including derivatives and integrals <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Later concepts might also require some basic linear algebra <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### Types of Differential Equations

[[introduction_to_ordinary_and_partial_differential_equations | Differential equations]] come in two main types <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>:

*   **Ordinary Differential Equations (ODEs)**: These involve functions with a single input, often representing time <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. ODEs typically describe a finite collection of values changing over time <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Partial Differential Equations (PDEs)**: These deal with functions that have multiple inputs <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. [[introduction_to_partial_differential_equations_and_the_heat_equation | PDEs]] often describe a continuum of values changing with time, such as temperature distribution in a solid body or fluid velocity at various points in space <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Physics as a Playground for Differential Equations

Physics provides an excellent context for exploring differential equations, starting with simple examples and progressing to more intricate systems <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Newtonian Mechanics

In Newtonian mechanics, motion is frequently described by force, which in turn determines acceleration – a statement about change <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

#### Projectile Motion

Consider the trajectory of an object thrown in the air <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Near Earth's surface, gravity causes a downward acceleration of 9.8 meters per second per second, a constant referred to as 'g' <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

Focusing on the vertical y-coordinate as a function of time:
*   Its first derivative (y-dot) represents vertical velocity <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   Its second derivative (y-double-dot) represents vertical acceleration <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

The differential equation for this motion is: `y-double-dot = -g` <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

This simple [[solving_simple_differential_equations | differential equation]] can be solved by integration <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>:
1.  **Velocity (y-dot)**: The function whose derivative is `-g` is `-gt + C₁` (where `C₁` is the initial velocity) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
2.  **Position (y)**: The function whose derivative is `-gt + C₁` is `-½gt² + C₁t + C₂` (where `C₂` is the initial position) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

This demonstrates how a function can be determined based on information about its rate of change <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

#### Planetary Motion

When studying the motion of planets, stars, and moons, gravity is not constant, and the force depends on the inverse square of the distance between bodies <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Here, acceleration becomes a function of position, leading to a dynamic interplay between variables <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. These problems often involve finding a function whose derivative (or higher-order derivatives) are defined in terms of the function itself <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. Physics commonly deals with second-order differential equations, where the highest derivative is a second derivative <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### The Pendulum Problem

A more complex example is a pendulum <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. While often approximated as harmonic motion (like a sine wave) for small angles <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, real pendulums exhibit more complex behavior, with longer periods when pulled farther out <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

The differential equation for a pendulum, considering the angle `theta` and damping due to air resistance (`mu`), is:
`theta-double-dot = -g/L * sin(theta) - mu * theta-dot` <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>, <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

This equation is challenging to solve analytically <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, and the presence of the `sine` function is precisely why real pendulums do not oscillate with a pure sine wave pattern <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

## Solving and Understanding Differential Equations

Due to the inherent difficulty in finding exact analytic solutions for many [[differential_equations_and_their_applications | differential equations]] <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>, alternative methods are used to build understanding and make computations <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

### [[phase_space_and_visualization_of_differential_equations | Phase Space]]

A powerful visualization tool is the [[phase_space_and_visualization_of_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. For a pendulum, its "state" can be described by two numbers: its angle (`theta`) and its angular velocity (`theta-dot`) <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. These two values define a point in a two-dimensional plane, where each point represents a possible initial condition of the pendulum <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

*   A trajectory in [[phase_space_and_visualization_of_differential_equations | phase space]] shows how the pendulum's state evolves over time <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. For a damped pendulum, the trajectory spirals inward, indicating a loss of energy and a reduction in peak velocity and displacement <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
*   [[phase_space_and_visualization_of_differential_equations | Differential equations]] can be visualized as a **vector field** in [[phase_space_and_visualization_of_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. Each point in this space has an associated vector representing the rate of change (direction and speed) of the system's state at that point <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   This approach effectively transforms a single second-order equation into a system of two first-order equations <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   Solving the equation visually means tracing a path through the vector field, where the path's velocity at every moment matches the vector from the field <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.

[[phase_space_and_visualization_of_differential_equations | Phase space]] is a general method applicable to any system of [[differential_equations_and_their_applications | ordinary differential equations]] <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>, even those with many dimensions (e.g., the 18-dimensional space for the three-body problem) <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>. The collection of all possible trajectories is known as **phase flow** <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. This concept helps in analyzing properties like **stability** of fixed points (states where the system is at rest) <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

### Numerical Methods

When analytic solutions are unavailable, [[numerical_methods_and_chaos_theory_in_differential_equations | numerical methods]] provide a way to approximate solutions by simulating the system's evolution using finite time steps <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>. The basic idea is to repeatedly take small steps based on the current state and the vector field <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.

For example, to compute `theta(t)` for the pendulum:
1.  Define initial `theta` and `theta-dot` <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>.
2.  Loop through small time steps (`delta-t`) <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.
3.  In each step, update `theta` by `theta-dot * delta-t` and `theta-dot` by `theta-double-dot * delta-t` <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.
4.  `theta-double-dot` is computed using the differential equation itself <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.

This process, though computationally intensive, allows for accurate approximations when `delta-t` is sufficiently small <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>.

## Limitations and [[numerical_methods_and_chaos_theory_in_differential_equations | Chaos Theory]]

While numerical methods offer computational solutions, there are further limitations. [[numerical_methods_and_chaos_theory_in_differential_equations | Chaos theory]] reveals that for some systems, even small variations in initial conditions can lead to vastly different long-term trajectories <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>. The three-body problem, for instance, contains elements of chaos <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>. This means that even if a solution could be found, its predictive power for long-term behavior might be limited due to the unavoidable imperfection of initial measurements <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>.