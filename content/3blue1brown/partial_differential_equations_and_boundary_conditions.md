---
title: Partial differential equations and boundary conditions
videoId: ToIXSwZ1pJU
---

From: [[3blue1brown]] <br/> 

When studying heat flow in a one-dimensional rod, the temperature distribution's change over time is described by the heat equation, a fundamental example of a [[introduction_to_partial_differential_equations | partial differential equation]] (PDE) <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a> <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This equation states that the rate of temperature change at a given point is dependent on the second derivative of that temperature with respect to space, meaning where there is curvature in space, there is change in time <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a> <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Constraints for Solving the Heat Equation

[[Solving differential equations with examples | Solving]] the heat equation involves more than just satisfying the PDE itself <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. A temperature function must meet three critical conditions to accurately describe heat flow:
1.  **The PDE:** The function must satisfy the heat equation <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
2.  **[[Boundary conditions in heat flow modeling | Boundary Conditions]]:** Specific conditions that the function must satisfy at the edges or boundaries of the system <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
3.  **Initial Condition:** The function must reflect the temperature distribution at time t=0 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

These added constraints, particularly the [[boundary_conditions_in_heat_flow_modeling | boundary]] and initial conditions, are where the primary challenge lies <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### Joseph Fourier's Contribution

In 1822, Joseph Fourier made a significant breakthrough in [[solving_differential_equations_with_examples | solving]] the heat equation <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. His approach was based on three fundamental observations <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
1.  Certain sine waves provide simple solutions to the heat equation <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  If multiple solutions exist, their sum is also a valid solution <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  Perhaps most surprisingly, almost any function can be expressed as a sum of sine waves (potentially infinitely many), a concept central to Fourier series <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a> <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

Sine waves are often advantageous in [[differential_equations_in_physics | differential equations]] due to their clean second derivatives <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a> <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This property allows for the individual solution of each wave in a sum, and because sums of solutions yield another solution, a recipe for solving the heat equation for any complex initial distribution emerges <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a> <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Sine Waves and Exponential Decay

Consider an idealized scenario where the initial temperature distribution along a rod is simply sine(x) <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a> <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. The second derivative of sine(x) is -sine(x) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a> <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. This implies that the rate at which each point's temperature changes is proportional to the temperature of the point itself <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a> <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. Such a relationship, where the rate of change is proportional to the value, inherently points to an exponential function <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a> <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

Thus, a proposed solution for the heat equation, when the initial state is a sine wave, is:
T(x,t) = sine(x) * e^(-alpha*t) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a> <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a> <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a> <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>
Where:
*   T(x,t) is temperature at position x and time t.
*   Alpha (α) is a proportionality constant from the heat equation.

Taking the partial derivatives of this function confirms it satisfies the heat equation:
*   Second partial derivative with respect to x: -sine(x) * e^(-alpha*t) <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a> <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a> <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>
*   First partial derivative with respect to t: -alpha * sine(x) * e^(-alpha*t) <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a> <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>

Since the partial derivative with respect to t is equal to alpha times the second partial derivative with respect to x (from the heat equation), this function is a valid solution to the PDE <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## Incorporating Boundary Conditions

However, this idealized sine wave solution does not reflect actual heat flow due to the influence of boundaries <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. The [[basics_and_significance_of_differential_equations | intuition]] behind the heat equation suggests that each point tends towards the average of its neighbors <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. At the boundaries of a rod, there is only one neighbor <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. For a rod where no heat flows in or out, the slope of the temperature curve at the boundaries (the rate of heat flow) must be zero <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a> <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

This specific [[boundary_conditions_in_heat_flow_modeling | boundary condition]] is precisely stated as:
The partial derivative of the temperature function with respect to x at x=0 and x=L (the length of the rod) must be zero for all times T > 0 <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a> <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a> <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This is a common requirement when [[numerical_methods_for_solving_differential_equations | solving partial differential equations]] in practice <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

To satisfy this boundary condition, the simple sine wave solution needs adjustment:
*   **Using Cosine:** A cosine function is flat (has a zero slope) at x=0, making it a better starting point than sine for this boundary condition <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a> <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. The second derivative of cosine(x) is also -cosine(x), so cosine(x) * e^(-alpha*t) still satisfies the PDE <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a> <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a> <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Adjusting Frequency:** To satisfy the boundary condition at the right end (x=L), the frequency of the wave needs adjustment. Introducing a constant 'omega' (ω) multiplied by x inside the cosine function allows for this <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a> <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a> <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a> <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. Due to the chain rule, the second derivative of cosine(ωx) becomes -ω² * cosine(ωx) <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a> <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a> <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. Consequently, the exponential decay part of the solution must also include ω² to balance the equation: e^(-αω²t) <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a> <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a> <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This means sharper curves decay more quickly, and quadratically <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a> <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

The frequencies that satisfy the zero-slope boundary condition at both ends (x=0 and x=L) are multiples of π/L. Specifically, ω = nπ/L, where 'n' is a non-negative integer (n=0, 1, 2, ...) <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a> <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a> <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a> <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a> <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a> <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. For n=0, this results in a constant function, which is a valid solution <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a> <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

This leads to an infinite family of functions that satisfy both the PDE and the [[boundary_conditions_in_heat_flow_modeling | boundary conditions]] <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a> <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. The overarching strategy of breaking down complex problems into simpler, idealized cases, often involving sine waves and exponentials, is a recurring theme in the field of [[differential_equations_in_physics | differential equations]], especially [[introduction_to_partial_differential_equations | PDEs]] <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a> <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a> <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a> <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a> <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.