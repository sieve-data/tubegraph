---
title: Introduction to ordinary and partial differential equations
videoId: p_di4Zn4wz4
---

From: [[3blue1brown]] <br/> 

According to Stephen Strogatz, since Isaac Newton, humanity has understood that the laws of physics are consistently expressed in the [[differential_equations_as_a_language_of_physics | language of differential equations]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This language extends beyond physics, adding a new perspective to understanding the world <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

Differential equations emerge when it is easier to describe change rather than absolute amounts <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For example, it's simpler to explain why population sizes grow or shrink than to pinpoint their exact values at a specific moment <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. In Newtonian mechanics, motion is often described by force, which determines acceleration—a statement about change <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

To understand this topic, a basic knowledge of [[introduction_to_calculus | calculus]], including derivatives and integrals, is assumed <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Some basic linear algebra will also be useful in later discussions <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Types of Differential Equations

Differential equations primarily come in two forms:

*   **Ordinary Differential Equations (ODEs)**: These involve functions with a single input, commonly time <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. ODEs focus on a finite collection of values changing over time <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Partial Differential Equations (PDEs)**: These deal with functions that have multiple inputs <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. PDEs typically involve a continuum of values changing with time, such as temperature across a solid body or fluid velocity at every point in space <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. [[introduction_to_partial_differential_equations_and_the_heat_equation | Partial differential equations]] will be explored more closely in subsequent videos <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Simple Example: Projectile Motion

Physics provides a useful starting point for understanding [[differential_equations and their applications | differential equations]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Consider the trajectory of an object thrown in the air <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Near Earth's surface, gravity causes a downward acceleration of 9.8 meters per second per second (denoted as `g`) <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This means that an object's velocity gains an additional downward component of 9.8 meters per second every second <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

Focusing on the vertical coordinate `y` as a function of time `t`:
*   The first derivative, `y-dot` (dy/dt), gives the vertical component of velocity <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   The second derivative, `y-double-dot` (d²y/dt²), gives the vertical component of acceleration <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

Thus, the differential equation for projectile motion under constant gravity is `y-double-dot = -g` <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

### Solving a Simple Differential Equation

This equation can be [[solving_simple_differential_equations | solved by integrating]] <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>:
1.  **Finding Velocity**: What function has `-g` as its derivative? `y-dot = -gt + C₁` (where `C₁` is the initial velocity) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   There are many functions with this derivative, introducing a degree of freedom determined by an initial condition <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
2.  **Finding Position**: What function has `-gt + C₁` as its derivative? `y = -½gt² + C₁t + C₂` (where `C₂` is the initial position) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   Again, an additional constant `C₂` is determined by another initial condition <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

This demonstrates [[solving_simple_differential_equations | solving a differential equation]] by determining a function based on information about its rate of change <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## More Complex Scenarios

Things become more intricate when forces depend on the body's position <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. For instance, in planetary motion, gravity is not constant but inversely proportional to the square of the distance between bodies <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Here, acceleration becomes a function of position, creating a dynamic interplay between variables <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

Often, differential equations involve finding a function whose derivatives (or higher-order derivatives) are defined in terms of the function itself <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. In physics, second-order differential equations (involving a second derivative) are most common <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. [[solving_partial_differential_equations | Solving these puzzles]] feels like an "infinite continuous jigsaw puzzle," where infinitely many numbers (for each point in time) are constrained by their rates of change <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### The Pendulum: A "Juicy" Example

Consider a pendulum, typically introduced in physics as undergoing harmonic motion (oscillating like a sine wave) <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. The period is often given as `2π√(L/g)` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. However, this is an approximation valid only for small angles <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. For larger swings, the period is longer, and the motion doesn't resemble a sine wave <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

To set up the true differential equation for a pendulum:
*   Let `θ` be the angle with the vertical, and `x = Lθ` be the arc distance <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   Gravity's component in the direction of motion is `-g sin(θ)` <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   The second derivative of `x` (acceleration) is `x-double-dot = -g sin(θ)` <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   Since `x = Lθ`, this becomes `θ-double-dot = -g/L * sin(θ)` <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   Adding air resistance (proportional to velocity), represented by `μ`, the equation becomes: `θ-double-dot = -g/L * sin(θ) - μ * θ-dot` <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

This equation is challenging to solve analytically <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. The `sine` function within the equation is precisely why real pendulums *don't* oscillate with a perfect sine wave pattern <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Even without the dampening term, an analytic solution is "hilariously complicated," involving complex functions <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

## Understanding Through Phase Space

Given the difficulty of finding exact analytic solutions, the study of differential equations often involves skipping direct solutions and moving straight to building understanding and making computations from the equations themselves <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

### State Space and Vector Fields

A powerful approach is to visualize all possible "states" of a system in a multi-dimensional space, known as **phase space** (or state space) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. For the pendulum, its state can be described by two numbers: its angle (`θ`) and its angular velocity (`θ-dot`) <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. Each point in this two-dimensional plane represents a unique state, including all possible initial conditions <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

*   A typical trajectory for a damped pendulum in phase space is an inward spiral, where `θ` and `θ-dot` both eventually approach zero (the origin) <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. This represents the pendulum slowing down due to air resistance <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
*   A differential equation can be visualized as a **vector field** in phase space <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. Each point in the space has an associated vector indicating the direction and speed the system will move from that state <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   The pendulum's second-order equation can be broken into a system of two first-order equations: one for `θ-dot` (angular velocity) and one for `θ-double-dot` (angular acceleration) <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. `θ-double-dot` is then expressed in terms of `θ` and `θ-dot`, forming the components of the vector field <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
*   [[solving_partial_differential_equations | Solving the equation]] visually means following a trajectory where, at every moment, the point's velocity matches the vector from the field <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. Different trajectories correspond to different initial conditions (e.g., a high initial velocity causing the pendulum to rotate fully before spiraling inward) <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

This vector field approach is generalizable to any system of ordinary differential equations <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. However, systems can have many more dimensions; for instance, the famous three-body problem (predicting the motion of three masses under gravity) has an 18-dimensional phase space <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>. This concept of dynamics in phase space is considered one of "the most powerful inventions of modern science" <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.

The collection of all possible trajectories in phase space is called **phase flow** <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. Phase flow helps analyze concepts like **stability**: whether a system, given a tiny nudge, tends to return to a fixed point or move away from it <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

### Applications Beyond Physics

The underlying structural similarities exposed by phase diagrams extend to other fields. Stephen Strogatz modeled affection dynamics between two people as a system of differential equations <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. For example, if one person's affection increases when the other shows interest but decreases when they seem cold, while the other person is oppositely attracted to disinterest, their romantic dynamic might resemble the endless oscillation of a pendulum in phase space <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>. Adding a term for "fear of vulnerability" could mimic friction, leading to an inward spiral towards mutual ambivalence <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>. This demonstrates how similar structures in phase diagrams can connect vastly different phenomena <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>.

## Numerical Methods

To actually compute solutions when analytic ones are intractable, **numerical methods** are used <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. This involves simulating the system using finite time steps instead of calculus's infinitesimals <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

The basic idea:
1.  From a given point in phase space, take a step equal to `delta t` (a small time step) multiplied by the vector at that point <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
2.  Repeat this process many times <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.
3.  The final location will be an approximation of the system's state at time `t` <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

This is simple enough to be programmed; for instance, a Python program can compute the pendulum's angle at time `t` by iteratively updating `theta` and `theta-dot` based on the differential equation and a small `delta t` <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>. While more sophisticated numerical methods exist, this "Euler method" illustrates the core principle <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.

## Limitations and Chaos Theory

Despite the utility of numerical and analytical methods, there are fundamental limits to prediction:

*   **Intractability**: Many differential equations simply do not have known exact analytic solutions <a class="yt-timestamp" data-t="00:32:05">[00:32:05]</a>.
*   **Chaos Theory**: This field, which emerged in the last century, reveals that for some systems, even tiny, unavoidable variations in initial conditions (due to imperfect measurements) can lead to wildly different long-term trajectories <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>. The three-body problem, for example, is known to contain elements of [[numerical_methods_and_chaos_theory_in_differential_equations | chaos theory]] <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>.

This means that even if a solution could be found, it might be useless for long-term prediction <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>. However, this paradox can be reassuring: the complexity observed in the world can be studied within these mathematical frameworks, rather than being attributed to a mismatch between model and reality <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>.