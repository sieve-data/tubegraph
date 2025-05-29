---
title: Fourier series in solving heat equations
videoId: ToIXSwZ1pJU
---

From: [[3blue1brown]] <br/> 

The [[the_heat_equation_and_its_applications | heat equation]] describes how temperature distributes and changes over time in a medium, such as a one-dimensional rod <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It is a type of partial differential equation (PDE) <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The equation states that the rate of temperature change at a given point over time depends on the [[role_of_derivatives_in_the_heat_equation | second derivative]] of the temperature with respect to space at that point, implying that where there is curvature in space, there is change in time <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Challenges in Solving the Heat Equation

Solving the [[the_heat_equation_and_its_applications | heat equation]] involves more than just satisfying the PDE itself <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. A temperature function must also satisfy:
*   **Partial Differential Equation (PDE)**: The core equation describing the relationship between time and spatial derivatives <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Boundary Conditions**: Specific conditions at the edges or boundaries of the system <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Initial Condition**: The temperature distribution at time t=0 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

These additional constraints pose the main challenge in finding a unique and accurate solution <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Joseph Fourier's Key Contributions

In 1822, Joseph Fourier provided a method to solve the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] by gaining control over the vast number of functions that could potentially satisfy the PDE and boundary conditions <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. His approach is based on three fundamental observations:

1.  **Sine Waves as Simple Solutions**: Certain [[role_of_sine_and_cosine_waves_in_heat_equation_solutions | sine waves]] inherently offer simple solutions to the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  **Superposition Principle**: If multiple functions are solutions to the equation, their sum is also a solution <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This principle is crucial for building complex solutions from simpler ones.
3.  **Fourier Series (Representation of Functions)**: Most surprisingly, almost any function—even discontinuous ones—can be expressed as a sum of [[role_of_sine_and_cosine_waves_in_heat_equation_solutions | sine waves]], potentially infinitely many <a class="yt-timestamp" data-t="00:01:43">[00:02:01]</a>. This concept is central to [[connection_between_fourier_series_and_differential_equations | Fourier series]] and allows for the [[fourier_transform_as_a_tool_for_analyzing_frequency_content_of_signals | breaking down of complex functions into simpler components]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### Why Sine Waves Are Ideal

Sine waves are particularly useful in dealing with [[connection_between_fourier_series_and_differential_equations | differential equations]] because of their predictable derivatives <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. For the [[heat_equation_and_its_connection_to_fourier_series | heat equation]], writing a function as a sum of these waves simplifies the computation of second derivatives, making the equation easier to solve for each component <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## Solving with a Single Sine Wave

Consider an idealized initial temperature distribution along a rod at `t=0` as `T(x, 0) = sin(x)` <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
The [[role_of_derivatives_in_the_heat_equation | second derivative]] of `sin(x)` with respect to `x` is `-sin(x)` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This means the curvature of the wave is equal and opposite to its height at each point <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

At `t=0`, the rate at which each point changes temperature is proportional to the temperature of the point itself <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This leads to a uniform scaling down of the sine curve shape over time <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. When the rate of change of a value is proportional to the value itself, it suggests an [[application_of_complex_numbers_and_exponentials_in_fourier_series | exponential]] relationship <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

For a temperature function `T(x,t)`, if `∂T/∂t = α * ∂²T/∂x²` (the general form of the heat equation), and for a sine wave `∂²T/∂x² = -T`, then `∂T/∂t = -αT`. This form indicates an [[application_of_complex_numbers_and_exponentials_in_fourier_series | exponential]] decay over time <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Thus, a proposed solution for a sine wave initial condition is `T(x,t) = sin(x) * e^(-αt)` <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This function satisfies the PDE <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## The Role of Boundary Conditions

While `T(x,t) = sin(x) * e^(-αt)` satisfies the PDE, it does not necessarily describe actual heat flow <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. A key constraint in realistic scenarios is the **boundary condition** that no heat flows into or out of the rod <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This implies that the slope (or the [[role_of_derivatives_in_the_heat_equation | partial derivative]] with respect to `x`) of the temperature distribution at the ends of the rod must be zero for all times greater than zero <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

Phrased mathematically, for a rod of length L, the boundary conditions are:
`∂T/∂x (0, T) = 0` and `∂T/∂x (L, T) = 0` for `T > 0` <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

## Adjusting for Boundary Conditions: Cosine Waves and Frequencies

To meet these boundary conditions, adjustments are made:

*   **Cosine Waves**: Instead of a [[role_of_sine_and_cosine_waves_in_heat_equation_solutions | sine wave]], a [[role_of_sine_and_cosine_waves_in_heat_equation_solutions | cosine function]] `cos(x)` is preferred because its derivative at `x=0` is `0`, which satisfies the boundary condition at one end <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. The [[role_of_derivatives_in_the_heat_equation | second derivative]] of `cos(x)` is also `-cos(x)`, so `cos(x) * e^(-αt)` also satisfies the PDE <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

*   **Adjusting Frequency**: To satisfy the boundary condition at the other end of the rod (at `x=L`), the frequency of the wave must be adjusted <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. Introducing a constant `ω` (omega) as `cos(ωx)`:
    *   The [[role_of_derivatives_in_the_heat_equation | second derivative]] of `cos(ωx)` is `-ω²cos(ωx)` <a class="yt-timestamp" data-t="00:11:01">[00:11:12]</a>.
    *   This means the exponential decay part must also include `ω²` to balance the equation, becoming `e^(-αω²t)` <a class="yt-timestamp" data-t="00:11:14">[00:11:22]</a>. This implies that sharper curves (higher frequency `ω`) decay more quickly <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

*   **Harmonic Frequencies**: For a rod of length L, the frequencies `ω` that result in a flat slope at `x=L` are the "harmonics" <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. These are integer multiples of a base frequency: `ω = n * (π/L)`, where `n` is a whole number (0, 1, 2, ...).
    *   For `n=1`, the lowest frequency `ω = π/L` makes the input to cosine `π` when `x=L`, ensuring the slope is flat <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
    *   `n=0` results in a constant function, which is also a valid solution satisfying all conditions <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

This process yields an infinite family of functions that satisfy both the PDE and the boundary conditions <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

## Conclusion

The approach to solving the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] through [[connection_between_fourier_series_and_differential_equations | Fourier series]] highlights several recurring themes in differential equations <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>:
*   The distinct treatment of boundaries versus the interior of a system <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   The strategy of breaking down complex problems into simpler, idealized cases <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   The common appearance of [[role_of_sine_and_cosine_waves_in_heat_equation_solutions | sine curves]] and [[application_of_complex_numbers_and_exponentials_in_fourier_series | exponentials]] as fundamental components of solutions, not just for the [[the_heat_equation_and_its_applications | heat equation]] but across various differential equations <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.