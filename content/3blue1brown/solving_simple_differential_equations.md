---
title: Solving simple differential equations
videoId: p_di4Zn4wz4
---

From: [[3blue1brown]] <br/> 

[[differential_equations_and_their_applications | Differential equations]] describe change, and understanding them adds a new perspective to viewing the world <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. They arise whenever it's easier to describe a rate of change rather than absolute amounts <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. For instance, it's simpler to explain why population sizes grow or shrink than to state their exact values at a specific time <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

[[differential_equations_as_a_language_of_physics | In physics]], particularly Newtonian mechanics, motion is often described by force, and force determines acceleration, which is a statement about change <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

[[introduction_to_ordinary_and_partial_differential_equations | Differential equations]] come in two main types:
*   **Ordinary Differential Equations (ODEs)**: Involve functions with a single input, often representing time <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. For example, a finite collection of values changing over time <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **[[introduction_to_partial_differential_equations_and_the_heat_equation | Partial Differential Equations (PDEs)]]**: Deal with functions that have multiple inputs <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. These often involve a continuum of values changing with time, such as temperature across a solid body or fluid velocity in space <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Solving by Integration: A Simple Example

A straightforward example of [[solving_partial_differential_equations | solving a differential equation]] can be seen in the trajectory of an object thrown into the air <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Near Earth's surface, gravity causes objects to accelerate downward at 9.8 meters per second per second <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>, a constant denoted as 'g' <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

Consider the y-coordinate of the object as a function of time:
1.  The first derivative of the y-coordinate (`y-dot`) gives the vertical component of velocity <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
2.  The second derivative of the y-coordinate (`y-double-dot`) gives the vertical component of acceleration <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

Thus, the differential equation for vertical motion under constant gravity is:
`y-double-dot = -g` <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

This equation can be solved by integration, essentially working backward <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>:
1.  **To find velocity**: What function has `-g` as its derivative?
    *   The answer is `-gt`, plus an initial velocity constant (`v_0`) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
    *   `y-dot = -gt + v_0` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
    *   This constant is determined by the "initial condition" – the velocity at time t=0 <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
2.  **To find position**: What function has `(-gt + v_0)` as its derivative?
    *   The answer is `-1/2 gt^2 + v_0t`, plus an initial position constant (`y_0`) <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   `y = -1/2 gt^2 + v_0t + y_0` <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   This constant is determined by the initial position at time t=0 <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

This process demonstrates how a function can be determined based on information about its rate of change <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Complexity of Solutions

While the example above is simple, most [[differential_equations_and_their_applications | differential equations]] are challenging to solve analytically (i.e., finding an exact formula) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Even for a seemingly simple system like a pendulum with no air resistance, the exact analytic solution is hilariously complicated and involves functions not commonly known <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. Often, there isn't a known way to write down an exact analytic solution at all, especially when factors like dampening (e.g., air resistance) are added <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

Because finding exact solutions can be impractical or impossible, the study of [[differential_equations_and_their_applications | differential equations]] often bypasses direct solution methods to build understanding and make computations from the equations themselves <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## [[numerical_methods_and_chaos_theory_in_differential_equations | Numerical Methods]] for Solving

When an exact solution is not feasible, [[numerical_methods_and_chaos_theory_in_differential_equations | numerical methods]] provide a way to approximate the solution <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. The core idea is to simulate the system's evolution using finite time steps instead of the infinitesimals of calculus <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.

The basic process involves:
1.  Starting at a known state (e.g., a point in [[phase_space_and_visualization_of_differential_equations | phase space]] defined by angle and angular velocity) <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
2.  Taking a small step in time (`delta t`) in the direction indicated by the system's rate of change (the vector at that point) <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>. This step is equal to `delta t` multiplied by that vector <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.
3.  Repeating this process many times <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.

The final location after these repeated steps approximates the state of the system at the sum of all those time steps <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>. A smaller `delta t` leads to a more accurate approximation, though it requires more steps <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. Computers are ideal for performing the many repeated calculations required <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>.

For a pendulum, if `theta` is the angle and `theta_dot` is the angular velocity, the numerical solution would involve a loop that updates `theta` and `theta_dot` in small increments <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>:
*   `theta += theta_dot * delta_t`
*   `theta_dot += theta_double_dot * delta_t` (where `theta_double_dot` is computed from the differential equation) <a class="yt-timestamp" data-t="00:25:02">[00:25:02]</a>.

This method, called [[numerical_methods_and_chaos_theory_in_differential_equations | solving a differential equation numerically]], allows for meaningful study of systems even when exact solutions are unattainable <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>. More sophisticated numerical methods exist to balance accuracy and efficiency <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.

[[numerical_methods_and_chaos_theory_in_differential_equations | Chaos theory]] further highlights that even with solutions, perfect long-term prediction for some systems is limited, as small variations in initial conditions can lead to wildly different trajectories <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>.