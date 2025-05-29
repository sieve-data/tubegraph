---
title: Ordinary differential equations ODEs vs Partial differential equations PDEs
videoId: p_di4Zn4wz4
---

From: [[3blue1brown]] <br/> 
Differential equations serve as the fundamental language for describing the laws of physics and are widely applicable beyond physics, offering a new perspective on the world <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. They arise when it is easier to describe change rather than absolute amounts, such as population growth or the motion of objects <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Types of Differential Equations

Differential equations primarily come in two forms:
*   **Ordinary Differential Equations (ODEs)** <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>
*   **Partial Differential Equations (PDEs)** <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>

#### Ordinary Differential Equations (ODEs)
[[basics_and_significance_of_differential_equations | ODEs]] involve functions with a single input, which is often considered time <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. They describe situations where a finite collection of values changes over time <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. While time is a prototypical example, the single independent variable can be something else <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

An example of an ODE is describing the vertical motion of an object thrown in the air, where its acceleration is a constant (due to gravity) <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. The position (y-coordinate) is a function of time, and its second derivative is the vertical acceleration <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. This specific equation (y-double-dot = -g) can be solved by integration, leading to expressions for velocity and position that include constants determined by initial conditions <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

More complex [[solving_differential_equations_with_examples | ODEs]] occur when forces depend on the body's position, such as in the motion of planets where gravity is not constant <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. In these cases, the rate of change of velocity (acceleration) becomes a function of position, creating an interplay between mutually interacting variables <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Often, these puzzles involve finding a function whose derivative(s) are defined in terms of the function itself <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

Physics frequently uses second-order differential equations, where the highest derivative in the expression is a second derivative <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Higher-order equations involve third, fourth, or even higher derivatives <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

> "The sensation you get when really meditating on one of these equations is one of solving an infinite continuous jigsaw puzzle." <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>

#### Partial Differential Equations (PDEs)
[[introduction_to_partial_differential_equations | PDEs]] deal with functions that have multiple inputs <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. They describe situations where a whole continuum of values changes with time, such as:
*   The temperature at every point of a solid body <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>
*   The velocity of a fluid at every point in space <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

PDEs are a topic for more detailed exploration in subsequent discussions <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Understanding Differential Equations: The Pendulum Example (ODE)
A pendulum provides a "juicy" example of an ODE <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. The acceleration of the pendulum's position (x) along its arc is given by negative g times the sine of theta (the angle it makes with the vertical) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Since x is the length (L) times theta, the second derivative of theta is negative g over L times sine of theta <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Adding a damping term for air resistance (proportional to velocity) results in the equation:
$\ddot{\theta} = -\frac{g}{L} \sin(\theta) - \mu \dot{\theta}$ <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

Ironically, the presence of the sine function in this equation is precisely why real pendulums do not oscillate with a perfect sine wave pattern, unlike the common small-angle approximation taught in introductory physics <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

#### Challenges in Solving Differential Equations
Solving differential equations, especially for complex systems like the pendulum with damping, can be very challenging <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Exact analytic solutions are often hilariously complicated or simply not known <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. Because of this, it is common to skip direct analytic solutions and instead focus on building understanding and making computations directly from the equations <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

#### [[applications_of_phase_space_in_differential_equations | Phase Space]]
A powerful approach to understanding ODEs is through visualizing all possible states in a multi-dimensional "state space" or [[applications_of_phase_space_in_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. For the pendulum, its state can be described by two numbers: its angle ($\theta$) and its angular velocity ($\dot{\theta}$) <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. Each point in this 2D plane represents a unique state or initial condition of the pendulum <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

A differential equation can be visualized as a [[laplacian_and_multivariable_calculus_in_pdes | vector field]] in this phase space <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. The rate of change of the state vector (angle, angular velocity) at any given point is represented by a vector from this field, indicating the direction and speed of movement <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. This means a single second-order ODE is effectively broken down into a system of two first-order equations <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

In this visualization, solving the equation means tracing a trajectory through the phase space such that, at every moment, the velocity of the point matches the vector from the field it is currently on <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This allows for qualitative understanding of system behavior, such as spiraling inward trajectories indicating energy loss due to air resistance in a pendulum <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

Phase space is a general concept; for example, the famous three-body problem (predicting the motion of three masses under gravity) has an 18-dimensional phase space <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

#### [[numerical_methods_for_solving_differential_equations | Numerical Methods]]
When analytic solutions are unattainable, [[numerical_methods_for_solving_differential_equations | numerical methods]] provide a way to approximate the solution by simulating the system using finite time steps <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. The basic idea involves taking small steps in the phase diagram based on the local vector field, repeatedly <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. By using sufficiently small time steps, a highly accurate approximation of the system's evolution can be obtained <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. Computers are essential for performing the many repeated calculations required for these methods <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>.

Despite the challenges of finding exact solutions, and even limits on prediction due to [[chaos_theory_and_differential_equations | chaos theory]] where small initial variations can lead to wildly different trajectories <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>, studying differential equations provides meaningful ways to understand complex systems <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>. The tactics developed for one case often transfer to many others, revealing underlying structural similarities between seemingly disparate dynamic systems <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.