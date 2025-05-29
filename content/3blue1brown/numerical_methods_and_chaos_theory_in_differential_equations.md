---
title: Numerical methods and chaos theory in differential equations
videoId: p_di4Zn4wz4
---

From: [[3blue1brown]] <br/> 

[[differential_equations_and_their_applications | Differential equations]] are considered the "language of physics" and are also spoken in fields beyond physics, adding a new perspective to understanding the world <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. They arise when it's easier to describe change than absolute amounts <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, such as how population sizes grow or shrink, or how motion is described in terms of force and acceleration in Newtonian mechanics <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

[[differential_equations_and_their_applications | Differential equations]] come in two main types:
*   **[[introduction_to_ordinary_and_partial_differential_equations | Ordinary Differential Equations (ODEs)]]** involve functions with a single input, often time <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. They describe a finite collection of values changing over time <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **[[introduction_to_partial_differential_equations_and_the_heat_equation | Partial Differential Equations (PDEs)]]** deal with functions that have multiple inputs, often involving a continuum of values changing with time, like temperature across a solid body or fluid velocity in space <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## The Challenge of Solving Differential Equations

A common puzzle in [[differential_equations_and_their_applications | differential equations]] is finding a function whose derivative(s) are defined in terms of the function itself <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. While simple examples, like the trajectory of a thrown object under constant gravity, can be [[solving_simple_differential_equations | solved]] by direct integration <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>, many [[differential_equations_and_their_applications | differential equations]] are challenging to [[solving_simple_differential_equations | solve]] analytically <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

Consider the example of a pendulum's motion, described by a second-order [[differential_equations_and_their_applications | differential equation]] involving the sine of the angle and a dampening term for air resistance <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. Even without the dampening term, an analytic solution is "hilariously complicated" and involves functions unfamiliar to most <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. If a dampening term is included, an exact analytic solution might not even be known <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. The true purpose of finding a solution is to make computations and build understanding of the [[applications_of_divergence_and_curl_to_dynamic_systems | dynamics]] <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

In such cases, a "short circuit" approach is often taken: instead of seeking an exact analytic solution, the focus shifts directly to building understanding and making computations from the equations themselves <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## Numerical Methods for Understanding and Computation

### Visualizing Differential Equations with Phase Space

To understand how a system, like a pendulum, evolves from different starting conditions, it's often easier and more general to visualize all possible states in a multi-dimensional plane, known as [[phase_space_and_visualization_of_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

For a pendulum, its state can be described by two numbers: its angle and its angular velocity <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. Each point in this two-dimensional [[phase_space_and_visualization_of_differential_equations | phase space]] fully describes the pendulum at any given moment, representing all possible initial conditions <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. An inward spiral trajectory in this space for a damped pendulum signifies that its peak velocity and displacement decrease with each swing, as it loses energy to air resistance <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

This concept of [[phase_space_and_visualization_of_differential_equations | phase space]] is a powerful invention, allowing questions to be asked about a spectrum of initial states, not just a single one <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. The collection of all possible trajectories in [[phase_space_and_visualization_of_differential_equations | phase space]] is called **phase flow** <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.

**Example: Love Dynamics**
Even seemingly unrelated [[dynamic systems]] can share structural similarities when viewed in [[phase_space_and_visualization_of_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>. For instance, a model of two people's changing affection, where one's love increases with the other's interest and vice-versa, can exhibit dynamics similar to a pendulum. If one partner's feelings are slowed by "fear of vulnerability," it acts like the friction in a pendulum, leading to an inward spiral towards mutual ambivalence in [[phase_space_and_visualization_of_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

### Visualizing Differential Equations as Vector Fields

Any system of [[introduction_to_ordinary_and_partial_differential_equations | ordinary differential equations]] can be described by a vector field <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.
*   A state vector (e.g., angle and angular velocity for a pendulum) defines a point in [[phase_space_and_visualization_of_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.
*   The derivative of this state vector gives its rate of change (direction and speed of movement in the diagram) <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   This derivative vector, which can be expressed entirely in terms of the state vector itself, is visualized as an arrow attached to the relevant point in [[phase_space_and_visualization_of_differential_equations | phase space]] <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   By calculating this for all points, a vector field emerges, showing how the state tends to change from any position <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
*   This process effectively breaks a single higher-order [[differential_equations_and_their_applications | equation]] into a system of two first-order equations, representing the first derivative of a vector value <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

### Numerical Solving: Simulation with Finite Time Steps

One way to compute an approximate answer to a [[differential_equations_and_their_applications | differential equation]] is to simulate what the system would do using finite time steps, rather than the infinitesimals of calculus <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

The basic idea of this [[numerical_computation_and_integration_in_fourier_series | numerical method]] is as follows:
1.  Start at a point in the [[phase_space_and_visualization_of_differential_equations | phase space]] (initial conditions) <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
2.  Take a small time step (`delta t`) based on the vector at the current position <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>. The step equals `delta t` multiplied by that vector <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.
3.  Repeat this process many times <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.
4.  The final location in [[phase_space_and_visualization_of_differential_equations | phase space]] provides an approximation of the system's state at a later time <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

Using a small `delta t` (e.g., 0.01) yields a much more accurate approximation, although it requires more repeated steps <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. This method is often implemented computationally, for example, using a programming language like Python <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>.

```python
# Conceptual Python code for numerical solution (Euler's method)
def solve_pendulum_numerically(initial_theta, initial_theta_dot, total_time, delta_t, g, L, mu):
    theta = initial_theta
    theta_dot = initial_theta_dot
    
    # Loop corresponding to taking many little time steps
    for _ in range(int(total_time / delta_t)):
        # Calculate theta_double_dot from the differential equation
        # theta_double_dot = -g/L * sin(theta) - mu * theta_dot
        theta_double_dot = -(g / L) * math.sin(theta) - mu * theta_dot
        
        # Update theta and theta_dot for the next step
        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
        
    return theta

# Note: Requires 'import math' for math.sin
```
This process, known as [[numerical_computation_and_integration_in_fourier_series | numerical computation]], allows studying [[differential_equations_and_their_applications | differential equations]] even when exact analytic solutions are not attainable <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.

## Chaos Theory

While [[numerical_computation_and_integration_in_fourier_series | numerical methods]] provide ways to compute solutions, another field, **chaos theory**, reveals further limitations on how well these [[dynamic systems]] can be used for long-term prediction <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>.

Chaos theory demonstrates that for some [[dynamic systems]], small variations in initial conditions (e.g., due to imperfect measurements) can lead to wildly different trajectories <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>. For example, the famous three-body problem, which predicts the motion of three masses interacting gravitationally, is known to contain "seeds of chaos" <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>. This means that even with solutions, their utility for long-term prediction can be severely limited <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>.

Despite these challenges, the ability to study complex [[dynamic systems]] through [[differential_equations_and_their_applications | differential equations]] and [[phase_space_and_visualization_of_differential_equations | phase space]] provides hope that the complexity observed in the world can be understood through this mathematical framework <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>.