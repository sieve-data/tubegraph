---
title: Heat equation in onedimensional rod
videoId: ToIXSwZ1pJU
---

From: [[3blue1brown]] <br/> 

The [[the_heat_equation_and_its_applications|heat equation]] studies how temperature distribution along a one-dimensional rod changes over time <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It serves as a foundational example for a [[introduction_to_partial_differential_equations|partial differential equation]] (PDE) <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The equation states that the rate at which temperature at a given point changes over time depends on the second derivative of that temperature with respect to space <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This implies that where there is curvature in space, there is change in time <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Solving the Heat Equation: Constraints

Solving the [[the_heat_equation_and_its_applications|heat equation]] is more complex than just the PDE itself <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The temperature function must satisfy three constraints to accurately describe heat flow <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>:
1.  **The PDE itself** <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
2.  **[[partial_differential_equations_and_boundary_conditions|Boundary conditions]]**: These define how the rod interacts with its environment at its ends <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
3.  **Initial condition**: This specifies the temperature distribution at time t=0 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

These added constraints introduce the primary challenge in solving the problem <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. While a vast number of functions satisfy the PDE, only a subset of those also satisfy the correct [[boundary_conditions_in_heat_flow_modeling|boundary conditions]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Joseph Fourier's Contribution

Joseph Fourier, in 1822, provided a key contribution to solving this problem by developing a method to select the particular solution fitting a given initial condition from the "ocean" of possible functions <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. His solution is based on three fundamental observations <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:

1.  Certain sine waves offer simple solutions to the [[the_heat_equation_and_its_applications|heat equation]] <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  If multiple functions are solutions, their sum is also a solution <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  Any practical function can be expressed as a sum of sine waves, possibly infinitely many <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This last idea is central to [[fourier_series_in_solving_heat_equations|Fourier series]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

The utility of breaking down a function into a sum of sine waves lies in the fact that sine waves are simpler to work with in many applications, especially [[differential_equations_in_physics|differential equations]] <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. For the [[the_heat_equation_and_its_applications|heat equation]], the relatively clean second derivatives of sine waves make it easier to solve the equation for each individual wave <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## Why Sine Waves are Special

Consider a simple temperature function at t=0 as sine(x), where x is the point on the rod <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The [[role_of_derivatives_in_the_heat_equation|second derivative]] of sine(x) is -sine(x) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This means the amount the wave curves is essentially equal and opposite to its height <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

For a sine wave initial condition, the [[the_heat_equation_and_its_applications|heat equation]] implies that each point changes its temperature at a rate proportional to its own temperature <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This leads to the entire sine curve scaling down uniformly over time <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. A rate of change proportional to the value itself suggests an exponential function <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

The proposed solution for a sine wave is `Temperature(x, t) = sin(x) * e^(-alpha*t)` <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   Taking the second partial derivative with respect to x: `d²T/dx² = -sin(x) * e^(-alpha*t)` <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   Taking the first partial derivative with respect to t: `dT/dt = -alpha * sin(x) * e^(-alpha*t)` <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
This function indeed satisfies the [[the_heat_equation_and_its_applications|partial differential equation]] <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## The Importance of Boundary Conditions

While the sine wave solution satisfies the PDE, it alone does not accurately describe real-world heat flow in a rod <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. This is because the [[the_heat_equation_and_its_applications|heat equation]] primarily characterizes the interior of the rod, while the boundary points behave differently <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

The intuition behind the [[role_of_derivatives_in_the_heat_equation|second derivative]] in the [[the_heat_equation_and_its_applications|heat equation]] is that each point tends towards the average of its neighbors <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. At the boundaries, there's only one neighbor <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

A common [[boundary_conditions_in_heat_flow_modeling|boundary condition]] for a rod where no heat flows in or out is that the slope of the temperature distribution at either end must be zero <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. More precisely, the partial derivative with respect to x of the temperature function at x=0 and x=L (length of the rod) must be zero for all times t > 0 <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. This is a crucial aspect of [[partial_differential_equations_and_boundary_conditions|partial differential equations]] in practice <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

### Adjusting for Boundary Conditions

To satisfy the [[boundary_conditions_in_heat_flow_modeling|boundary condition]] of zero slope at the ends, we can modify the sine wave solution.

*   **Using Cosine Waves**: A cosine function is naturally flat (has zero slope) at x=0 <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. The second derivative of cosine(x) is also -cosine(x), so `cos(x) * e^(-alpha*t)` still satisfies the PDE <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

*   **Adjusting Frequency**: To make the function flat at both ends (x=0 and x=L), the frequency of the wave needs to be adjusted <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
    *   Introducing a constant `omega` multiplied by `x` (e.g., `cos(omega*x)`) changes the frequency <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
    *   The [[role_of_derivatives_in_the_heat_equation|second derivative]] of `cos(omega*x)` becomes `-omega² * cos(omega*x)` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
    *   To balance the [[the_heat_equation_and_its_applications|heat equation]], the exponential decay term must include `omega²` in its exponent: `e^(-alpha * omega² * t)` <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This means sharper curves (higher frequency `omega`) decay more quickly <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

*   **Harmonics for Boundary Conditions**: For a rod of length L, the frequencies (`omega`) that satisfy the zero-slope [[boundary_conditions_in_heat_flow_modeling|boundary condition]] are multiples of `pi/L` <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This means `omega` can be `n * (pi/L)` for `n = 0, 1, 2, ...` <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This results in an infinite family of functions that satisfy both the PDE and the [[boundary_conditions_in_heat_flow_modeling|boundary condition]] <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

This process demonstrates how breaking down a general problem into simpler, idealized cases (like [[role_of_sine_and_cosine_waves|sine and cosine waves]]) is a common strategy in [[differential_equations_in_physics|differential equations]], especially in the context of [[introduction_to_partial_differential_equations|PDEs]] <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.