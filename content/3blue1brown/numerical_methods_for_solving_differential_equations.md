---
title: Numerical methods for solving differential equations
videoId: p_di4Zn4wz4
---

From: [[3blue1brown]] <br/> 

When finding exact analytical solutions to [[basics_and_significance_of_differential_equations | differential equations]] is unattainable, numerical methods provide a way to build understanding and make computations directly from the equations themselves <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. This approach involves simulating the system's evolution using finite time steps <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.

## Core Idea

The fundamental concept behind numerical [[solving_differential_equations_with_examples | solutions]] is to approximate the continuous change of a system by taking many small, discrete steps in time <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.

For a system described by a [[applications_of_phase_space_in_differential_equations | phase diagram]] where the system's state is represented as a point in a vector field, the process is as follows:
1.  **Initial State**: Start at a given point in the [[applications_of_phase_space_in_differential_equations | phase diagram]] <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
2.  **Vector Field Guidance**: Identify the vector at that point, which indicates the direction and speed the system tends to move in the diagram <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
3.  **Small Step**: Take a small time step, `delta t` (Δt), and move the point a distance equal to `delta t` multiplied by the vector at the current position <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.
4.  **Repetition**: Repeat this process, continuously updating the point's position based on the vector field at each new location <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.
5.  **Approximation**: The final location of the point after many such steps provides an approximation of the system's state at time `t`, where `t` is the sum of all the `delta t` steps <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.

## Accuracy and Efficiency

The accuracy of a numerical solution is directly related to the size of `delta t` <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>. A larger `delta t` (e.g., 0.5) can lead to gross inaccuracies, while a smaller `delta t` (e.g., 0.01) yields a much more accurate approximation <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. However, a smaller `delta t` requires more repeated steps to cover the same total time `t` <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.

Fortunately, modern computers excel at repeating simple tasks many times, making this computationally intensive process feasible <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>.

## Example: Pendulum Simulation

Consider the pendulum system, described by a [[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | second-order ordinary differential equation]] involving `theta` (angle) and `theta dot` (angular velocity) <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This can be broken down into a system of two first-order [[solving_systems_of_differential_equations_using_matrices | equations]] <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

To compute the value of `theta` at a given time `t` using a simple numerical method (like Euler's method):
1.  **Define Variables**: Initialize `theta` and `theta dot` based on the system's initial conditions (e.g., `theta` at `pi/3` radians, `theta dot` at 0) <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>.
2.  **Set Time Step**: Choose a small `delta t` (e.g., 0.01) <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>.
3.  **Loop for Time Evolution**: Iterate through a loop for the desired total time `t` <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>:
    *   Update `theta`: `theta = theta + (theta dot * delta t)` <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.
    *   Update `theta dot`: `theta dot = theta dot + (theta double dot * delta t)` <a class="yt-timestamp" data-t="00:25:02">[00:25:02]</a>.
    *   Compute `theta double dot` using the differential equation itself <a class="yt-timestamp" data-t="00:25:06">[00:25:06]</a>.
4.  **Return Result**: After all steps, the final value of `theta` is the numerical solution <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>.

This process, while conceptually simple, forms the basis for more sophisticated numerical methods that balance accuracy and efficiency <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.

## Limitations and Significance

While numerical methods provide a powerful tool for studying [[basics_and_significance_of_differential_equations | differential equations]] even when exact solutions are not possible <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>, it's important to recognize their limitations. One major limitation arises from chaos theory, which reveals that for some systems, minor variations in initial conditions (due to imperfect measurements) can lead to vastly different long-term trajectories <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>. This means that even with accurate numerical [[solving_differential_equations_with_examples | solutions]], long-term prediction may still be impractical or impossible for chaotic systems <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>.