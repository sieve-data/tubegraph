---
title: Applications of phase space in differential equations
videoId: p_di4Zn4wz4
---

From: [[3blue1brown]] <br/> 

Differential equations are fundamental to describing how things change in the world, often making it easier to define rates of change rather than absolute amounts <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. For example, in Newtonian mechanics, motion is described by force, which determines acceleration—a statement about change <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. However, solving these equations analytically can be extremely challenging, or even impossible, for many complex systems <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.

## Visualizing Dynamics with Phase Space

To gain understanding and make computations for differential equations, especially when exact analytic solutions are unattainable, mathematicians and scientists often use a concept known as [[phase_space_and_population_dynamics | phase space]] <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>. This approach involves a "short circuit," skipping the explicit solution and going straight to building understanding from the equations themselves <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.

### What is Phase Space?
In the context of differential equations, a [[phase_space_and_population_dynamics | phase space]] is an abstract multi-dimensional space that represents all possible "states" of a system at any given moment <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>. For a system, its state can be described by a collection of values, and each point in this space corresponds to a unique combination of these values <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>.

*   **Distinction from Physical Space**: It's crucial to remember that [[phase_space_and_population_dynamics | phase space]] is an abstract construct, distinct from the physical space where the system itself exists and moves <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>.
*   **Physics Terminology**: In physics, particularly Hamiltonian mechanics, the term [[phase_space_and_population_dynamics | phase space]] is often specifically reserved for spaces where axes represent position and momentum <a class="yt-timestamp" data-t="18:33:00">[18:33:00]</a>. More broadly, it can be referred to as a [[state_space_and_conservation_laws_in_classical_physics | state space]] <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.

### Differential Equations as Vector Fields
A powerful application of [[phase_space_and_population_dynamics | phase space]] is visualizing a differential equation as a vector field <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>.

1.  **State Vector**: The system's state can be represented as a vector (e.g., `[theta, theta_dot]`) <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.
2.  **Rate of Change**: The derivative of this state vector gives its rate of change, indicating the direction and speed it tends to move in the [[phase_space_and_population_dynamics | phase space]] diagram <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>. This derivative, itself a vector, can be expressed in terms of the state vector using the differential equation <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>.
3.  **Vector Field**: By computing this rate-of-change vector at every point in the [[phase_space_and_population_dynamics | phase space]], a vector field is created, showing how the system's state tends to change from any given position <a class="yt-timestamp" data-t="14:41:00">[14:41:00]</a>.
4.  **Trajectories**: As the system evolves from an initial state, its representation as a point in [[phase_space_and_population_dynamics | phase space]] moves along a trajectory. At every moment, the velocity of this point matches the vector from the field at that location <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>.

## Examples and Applications of Phase Space

### The Pendulum
For a pendulum, its state can be described by two numbers: its angle (`theta`) and its angular velocity (`theta_dot`) <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>. The differential equation for a pendulum (including air resistance) is:
`theta_double_dot = -g/L * sin(theta) - mu * theta_dot` <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>, <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>.

To visualize this in a two-dimensional [[phase_space_and_population_dynamics | phase space]], the second-order equation is broken down into a system of two first-order equations <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>:
1.  `theta_dot = angular_velocity` (first component of rate of change vector) <a class="yt-timestamp" data-t="14:06:00">[14:06:00]</a>
2.  `angular_velocity_dot = -g/L * sin(theta) - mu * angular_velocity` (second component) <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>

*   **Trajectory Interpretation**: A typical trajectory in this [[phase_space_and_population_dynamics | phase space]] spirals inward, indicating that the pendulum loses energy due to air resistance. The peak velocity and peak displacement decrease with each swing, and the point is "attracted" to the origin (where `theta` and `theta_dot` are both zero, meaning the pendulum is at rest) <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>, <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.
*   **Parameter Effects**: Changing parameters like air resistance (`mu`) directly impacts the vector field. Increasing `mu` results in trajectories that spiral inward faster, meaning the pendulum slows down more quickly <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>.

### Romance Dynamics
[[phase_space_and_population_dynamics | Phase space]] is not limited to physics. Stephen Strogatz modeled affection between two people using differential equations <a class="yt-timestamp" data-t="20:50:00">[20:50:00]</a>. If one person's affection increases with their companion's interest, but the companion's affection decreases when the first person seems too keen, the [[phase_space_and_population_dynamics | phase space]] shows an endless cycle of affection and repulsion, similar to the central part of the pendulum diagram <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>. Adding a term for "fear of vulnerability" (like friction in the pendulum) leads to an inward spiral towards mutual ambivalence <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>. This illustrates how different systems can share similar dynamic structures when viewed in [[phase_space_and_population_dynamics | phase space]] <a class="yt-timestamp" data-t="22:21:00">[22:21:00]</a>.

### The Three-Body Problem
More complex systems, like the famous three-body problem (predicting the motion of three masses under mutual gravity), require high-dimensional [[phase_space_and_population_dynamics | phase spaces]] <a class="yt-timestamp" data-t="17:22:00">[17:22:00]</a>. For this problem, each mass has three position coordinates and three momentum coordinates, leading to an 18-dimensional [[phase_space_and_population_dynamics | phase space]] of possible states <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>. Although such spaces cannot be visualized directly, the conceptual power of representing dynamics as a single point meandering through this high-dimensional space remains <a class="yt-timestamp" data-t="17:50:00">[17:50:00]</a>.

## Advantages and Insights from Phase Space

*   **Holistic View**: [[phase_space_and_population_dynamics | Phase space]] allows for asking questions not just about a single initial condition but about a "whole spectrum of initial states" <a class="yt-timestamp" data-t="19:35:00">[19:35:00]</a>.
*   **Phase Flow**: The collection of all possible trajectories in [[phase_space_and_population_dynamics | phase space]] is referred to as "phase flow," reminiscent of a moving fluid <a class="yt-timestamp" data-t="19:40:00">[19:40:00]</a>, <a class="yt-timestamp" data-t="19:45:00">[19:45:00]</a>.
*   **Stability Analysis**: A key application is analyzing stability. Fixed points (where the system is at rest) in [[phase_space_and_population_dynamics | phase space]] can be examined to see if tiny nudges lead the system back towards (stable) or away from (unstable) that point <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a>. This is done by observing whether the phase flow tends to contract or expand around the fixed point <a class="yt-timestamp" data-t="20:36:00">[20:36:00]</a>.
*   **Structural Similarities**: [[phase_space_and_population_dynamics | Phase diagrams]] expose underlying structural similarities between vastly different dynamical systems, even if their governing equations differ significantly <a class="yt-timestamp" data-t="22:36:00">[22:36:00]</a>.

## Numerical Methods in Phase Space

Even without exact analytic solutions, [[phase_space_and_population_dynamics | phase space]] facilitates numerical computations. The basic idea is to simulate the system's evolution by taking small, finite time steps along the vectors defined by the differential equation in [[phase_space_and_population_dynamics | phase space]] <a class="yt-timestamp" data-t="23:05:00">[23:05:00]</a>.

For example, to compute the pendulum's angle (`theta`) at time `t`:
1.  Define initial conditions for `theta` and `theta_dot` <a class="yt-timestamp" data-t="24:34:00">[24:34:00]</a>.
2.  Loop through small time steps (`delta_t`) <a class="yt-timestamp" data-t="24:47:00">[24:47:00]</a>.
3.  In each step, update `theta` by `theta_dot * delta_t` and `theta_dot` by `theta_double_dot * delta_t` (where `theta_double_dot` is calculated from the differential equation based on the current `theta` and `theta_dot`) <a class="yt-timestamp" data-t="24:58:00">[24:58:00]</a>.
This process is known as solving a differential equation numerically, and while more sophisticated methods exist, this iterative approach forms the core idea <a class="yt-timestamp" data-t="25:16:00">[25:16:00]</a>.

## Limitations: Chaos Theory
Despite the power of [[phase_space_and_population_dynamics | phase space]] and numerical methods, there are fundamental limits to prediction. Chaos theory has revealed that for some systems, even tiny variations in initial conditions can lead to wildly different trajectories in [[phase_space_and_population_dynamics | phase space]] <a class="yt-timestamp" data-t="25:58:00">[25:58:00]</a>. The three-body problem, for instance, contains "seeds of chaos" <a class="yt-timestamp" data-t="26:23:00">[26:23:00]</a>, meaning that even with precise models, long-term prediction can be impossible. This highlights that the complexity observed in the real world can be inherent in the mathematical models themselves <a class="yt-timestamp" data-t="26:45:00">[26:45:00]</a>.