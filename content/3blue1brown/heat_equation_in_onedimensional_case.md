---
title: Heat equation in onedimensional case
videoId: ToIXSwZ1pJU
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_partial_differential_equations_and_the_heat_equation | heat equation]] describes how temperature distribution along a one-dimensional rod changes over time <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This equation serves as a primary example of a [[introduction_to_ordinary_and_partial_differential_equations | partial differential equation]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Equation Description
The [[mathematical_modeling_of_heat_flow | heat equation]] states that the rate at which temperature at a given point changes over time depends on the second derivative of that temperature with respect to space <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This means where there is curvature in space, there is change in time <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Constraints for Solving the Heat Equation
To accurately describe [[mathematical_modeling_of_heat_flow | heat flow]], the temperature function must satisfy three constraints <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>:
1.  **The Partial Differential Equation (PDE) itself**: Describes how temperature changes internally <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
2.  **Boundary Conditions**: Specific conditions at the ends of the rod <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
3.  **Initial Condition**: The temperature distribution at time *t* = 0 <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

The primary challenge in [[solving_partial_differential_equations | solving]] the heat equation lies in satisfying these added constraints, as a vast number of functions solve the PDE alone <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Joseph Fourier's Contribution
In 1822, Joseph Fourier's key contribution was to develop a method to select a particular solution that fits a given initial condition from the numerous functions satisfying the PDE and boundary conditions <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. His solution is based on three fundamental observations <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
1.  Certain sine waves provide a simple solution to the heat equation <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  The sum of multiple solutions is also a solution <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  Any function can be expressed as a sum of sine waves (potentially infinitely many), which is the basis of [[fourier_series_and_their_relation_to_the_heat_equation | Fourier series]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a> <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

Sine waves are particularly useful in [[differential_equations_as_a_language_of_physics | differential equations]] because their clean second derivatives simplify [[solving_simple_differential_equations | solving]] the heat equation for each wave component <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a> <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## Solving for a Simple Sine Wave Initial Condition
Consider an idealized case where the initial temperature function at *t* = 0 is `sine(x)` <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
The second derivative of `sine(x)` is `negative sine(x)` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This means the curvature of the wave is equal and opposite to its height at each point <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
At *t* = 0, each point's temperature changes at a rate proportional to its own temperature, with a consistent proportionality constant across all points <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This leads to the sine curve shape scaling down uniformly over time <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

This proportionality of the rate of change to the value itself is characteristic of exponential decay <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. If the heat equation's right-hand side for a sine wave becomes `negative alpha * temperature_function`, the solution can be proposed as `e^(-alpha*t)` times the initial spatial distribution <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

The proposed solution for a sine wave in space and exponential decay in time is:
`T(x, t) = sine(x) * e^(-alpha*t)` <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>

Let's check the partial derivatives for this function:
*   Partial derivative with respect to *x*: `cosine(x) * e^(-alpha*t)` <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>
*   Second partial derivative with respect to *x*: `negative sine(x) * e^(-alpha*t)` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>
*   Partial derivative with respect to *t*: `negative alpha * e^(-alpha*t) * sine(x)` <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>

Indeed, this function satisfies the partial differential equation <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## Importance of Boundary Conditions
While the simple sine wave solution satisfies the PDE, it may not accurately describe actual [[mathematical_modeling_of_heat_flow | heat flow]] because it doesn't account for how the ends of the rod behave <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. For example, a straight line temperature distribution (e.g., `T(x) = C*x`) satisfies the PDE (its second spatial derivative is zero, and its temporal derivative is zero if it never changes), but in reality, it would change over time to approach a uniform temperature <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a> <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

The intuition for the second derivative in the heat equation comes from each point tending towards the average of its neighbors <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. At the boundaries, there is no neighbor on one side <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. If no heat flows into or out of the rod, the slope of the temperature curve at either end must be zero <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a> <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

Mathematically, this [[boundary_conditions_in_pdes | boundary condition]] is expressed as:
`∂T/∂x(0,T) = 0` and `∂T/∂x(L,T) = 0` for all times *T* > 0, where *L* is the length of the rod <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

> [!NOTE]
> [[boundary_conditions_in_pdes | Boundary conditions]] are almost always present when [[solving_partial_differential_equations | solving partial differential equations]] in practice and require as much attention as the PDE itself <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

## Adjusting for Boundary Conditions with Cosine Waves
To meet the [[boundary_conditions_in_pdes | boundary condition]] of zero slope at the endpoints, a cosine function is more suitable than a sine function, as it is naturally "flat" (has zero slope) at *x* = 0 <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
The second derivative of `cosine(x)` is also `negative one * itself` <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>, so `cosine(x) * e^(-alpha*t)` still satisfies the PDE <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

To ensure the function is also flat at the other end (*x* = *L*), the frequency of the wave must be adjusted <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
Introducing a constant `omega` multiplied by the input to the cosine function (e.g., `cosine(omega*x)`) changes its derivatives:
*   First derivative with respect to *x*: `negative omega * sine(omega*x)` <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>
*   Second derivative with respect to *x*: `negative omega^2 * cosine(omega*x)` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>

This `omega^2` term must also be balanced on the left-hand side of the heat equation, meaning the exponential decay part will have an additional `omega^2` term in its exponent <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. This implies that sharper (higher frequency) curves decay more quickly towards equilibrium, quadratically with frequency <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

For a rod of length *L*, the frequencies `omega` that satisfy the zero-slope [[boundary_conditions_in_pdes | boundary condition]] at both ends are integer multiples of `pi / L` <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a> <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. These are analogous to harmonics. A constant function (where `omega` = 0) is also a valid solution that satisfies both the PDE and boundary conditions <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

This provides an infinite family of functions that satisfy both the PDE and the necessary [[boundary_conditions_in_pdes | boundary conditions]] <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. The next step is to use this family to construct a more general solution, which will involve [[applications_of_fourier_series_in_heat_distribution | Fourier series]] <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

## General Themes in Differential Equations
Many considerations encountered in solving the heat equation are frequent themes throughout the field of [[differential_equations_as_a_language_of_physics | differential equations]] <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>:
*   Modeling boundaries with special rules distinct from the interior's main differential equation is a regular pattern, especially in [[introduction_to_ordinary_and_partial_differential_equations | PDEs]] <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   Breaking down general situations into simpler, idealized cases is a common strategy <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   These simpler cases often involve mixtures of sine/cosine curves and exponentials, which is a broader principle beyond just the heat equation <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.