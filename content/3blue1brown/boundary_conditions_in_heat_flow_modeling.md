---
title: Boundary conditions in heat flow modeling
videoId: ToIXSwZ1pJU
---

From: [[3blue1brown]] <br/> 

When modeling [[the_heat_equation_and_its_applications | heat flow]] in a one-dimensional rod, the mathematical description involves more than just a [[partial_differential_equations_and_boundary_conditions | partial differential equation]] (PDE) for the interior of the rod <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. To accurately describe [[heat_equation_in_onedimensional_rod | heat flow]], the temperature function must also satisfy specific [[partial_differential_equations_and_boundary_conditions | boundary conditions]] and an initial condition <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. These added constraints are crucial because a vast number of functions can solve the PDE itself <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Importance of Boundary Conditions

Boundary conditions define the behavior of the system at its edges or boundaries <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. In practice, almost every time a [[partial_differential_equations_and_boundary_conditions | partial differential equation]] needs to be solved, there will be accompanying [[partial_differential_equations_and_boundary_conditions | boundary conditions]] that demand as much attention as the PDE itself <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. The way boundaries are modeled with their own special rules, distinct from the main differential equation characterizing the interior, is a very regular and important theme in [[differential_equations_in_physics | differential equations]], especially PDEs <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

### Example: Heat Flow in a Rod with No Heat Loss

Consider a scenario where no heat flows into or out of the rod <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. In such a case, the simulation treats the two boundary points of the rod differently from all other points <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. The intuition for the [[role_of_derivatives_in_the_heat_equation | second derivative]] in the [[heat_equation_in_onedimensional_rod | heat equation]] is that each point tends towards the average value of its two neighbors <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. However, at the boundary, there is no neighbor on one side <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

In the continuous limit, the slope of the temperature curve at the boundaries will be zero for all times after the start <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. This means that if no heat flows into or out of the rod, the slope (which is proportional to the rate of [[the_heat_equation_and_its_applications | heat flow]]) at either end must be zero <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

Mathematically, this **boundary condition** is expressed as: the [[role_of_derivatives_in_the_heat_equation | partial derivative]] with respect to x of the temperature function at `x=0` and at `x=L` (where `L` is the length of the rod) must be zero for all times `T` greater than zero <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

## How Solutions Must Satisfy Boundary Conditions

A function satisfying only the [[heat_equation_in_onedimensional_rod | heat equation]] itself is insufficient. It must also be "flat" (have a zero slope) at each of the endpoints for all times greater than zero <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Failing Examples

*   **Sine Wave Initial Condition**: Even if a rod started with a perfect sine wave temperature distribution, it would not evolve by simple exponential decay if the "no heat flow" boundary condition applies <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. Points at the boundaries would be heated or cooled by their neighbors, changing the shape <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Straight Line Initial Condition**: A straight line temperature function, like `T(x) = c*x`, satisfies the [[heat_equation_in_onedimensional_rod | heat equation]] because its [[role_of_derivatives_in_the_heat_equation | second partial derivative]] with respect to x is zero (no curvature), and its [[role_of_derivatives_in_the_heat_equation | partial derivative]] with respect to time is also zero <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. However, if simulated with the no-heat-flow boundary conditions, it would change over time, approaching a uniform temperature, because the slope at the boundary points is not zero <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. As soon as the clock starts, the boundary values shift to make the slope zero, and it remains that way <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Adapting Sine/Cosine Solutions

While a simple sine wave might not work, [[role_of_sine_and_cosine_waves_in_heat_equation_solutions | sine waves]] and [[role_of_sine_and_cosine_waves_in_heat_equation_solutions | cosine waves]] are still key to finding solutions <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

1.  **Using Cosine**: A [[role_of_sine_and_cosine_waves_in_heat_equation_solutions | cosine function]] can be used instead of a sine, as it is naturally flat at `x=0` (assuming the rod starts at `x=0`) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. The [[role_of_derivatives_in_the_heat_equation | second derivative]] of cosine of x is also negative one times itself, so `cosine(x) * e^(-αt)` still satisfies the PDE <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

2.  **Adjusting Frequency**: To ensure flatness at the right boundary (`x=L`), the frequency of the wave must be adjusted <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. This involves introducing a constant, `omega (ω)`, multiplied by the input of the [[role_of_sine_and_cosine_waves_in_heat_equation_solutions | cosine function]] (e.g., `cosine(ωx)`) <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
    *   The [[role_of_derivatives_in_the_heat_equation | second derivative]] of `cosine(ωx)` is `-ω² * cosine(ωx)` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
    *   This means the exponential decay term in the solution must also pick up an `ω²` in its exponent to balance the equation <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. So, the solution looks like `cosine(ωx) * e^(-αω²t)` <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This intuitively means sharper curves (higher frequency) decay more quickly towards equilibrium <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

3.  **Finding Harmonics**: For a rod of length `L`, the lowest frequency (`ω`) that results in a flat rightmost point is `pi/L` <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This makes the input to the cosine `pi` at `x=L`, which is half the period of a cosine wave <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. All other frequencies that satisfy this boundary condition are whole number multiples of this base frequency (`n * pi / L`, where `n` is an integer) <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Even `n=0` works, resulting in a constant function, which is a valid solution <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

This process provides an infinite family of functions that satisfy both the [[heat_equation_in_onedimensional_rod | heat equation]] (PDE) and the necessary [[partial_differential_equations_and_boundary_conditions | boundary conditions]] <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. These solutions, which are a mixture of [[role_of_sine_and_cosine_waves_in_heat_equation_solutions | sine waves]]/[[role_of_sine_and_cosine_waves_in_heat_equation_solutions | cosine waves]] in space and exponentials in time, are common in [[idealized_physics_in_theoretical_simulations | idealized physics]] cases across [[differential_equations_in_physics | differential equations]] <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. By combining these solutions, it becomes possible to construct a more general solution for any complicated initial temperature distribution using [[fourier_series_in_solving_heat_equations | Fourier series]] <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.