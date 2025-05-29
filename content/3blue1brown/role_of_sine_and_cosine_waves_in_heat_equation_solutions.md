---
title: Role of sine and cosine waves in heat equation solutions
videoId: ToIXSwZ1pJU
---

From: [[3blue1brown]] <br/> 

The [[heat_equation_in_onedimensional_rod | heat equation]] describes how temperature distribution along a one-dimensional rod changes over time <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. It states that the rate of temperature change at a point over time depends on the [[role_of_derivatives_in_the_heat_equation | second derivative]] of the temperature at that point with respect to space <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This means where there is curvature in space, there is change in time <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

However, solving the [[the_heat_equation_and_its_applications | partial differential equation (PDE)]] alone is not enough; the temperature function must also satisfy specific boundary conditions and an initial condition <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. These added constraints are where the main challenge lies <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Fourier's Approach to Solving the Heat Equation

In 1822, Joseph Fourier made a key contribution by developing a method to solve the heat equation while accounting for initial conditions <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. His solution is based on three fundamental observations:

1.  Certain sine waves provide a simple solution to the heat equation <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  The sum of multiple solutions to the heat equation is also a solution <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  Any function can be expressed as a sum of sine waves, potentially infinitely many <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This last idea is central to [[Fourier series in solving heat equations | Fourier series]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

This approach is particularly useful because sine waves are often easier to work with in many applications, especially in the context of [[differential_equations_in_physics | differential equations]] <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. When a function is written as a sum of these waves, their clean second derivatives simplify solving the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] for each component <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. The sum of these individual solutions then provides a recipe for solving the heat equation for any complex initial temperature distribution <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Why Sine Waves Are Suitable

Let's consider a simplified temperature function at time `t = 0` as `sin(x)` <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. The heat equation involves the [[role_of_derivatives_in_the_heat_equation | second derivative]] with respect to space.
*   The derivative of `sin(x)` is `cos(x)` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   The second derivative of `sin(x)` (derivative of `cos(x)`) is `-sin(x)` <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

This means the amount a sine wave curves is "equal and opposite to its height" at each point <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. Consequently, for a sine wave, the rate at which each point's temperature changes is proportional to the temperature of the point itself <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This proportionality suggests an exponential decay <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

The derivative of `e^(constant * t)` is `constant * e^(constant * t)` <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
If the heat equation's right side is `-alpha * temperature_function`, then the solution is `e^(-alpha * t)` multiplied by the initial function <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Verifying the Solution

A proposed solution for the heat equation could be `T(x, t) = sin(x) * e^(-alpha*t)` <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. Let's check its partial derivatives:

*   **Second partial derivative with respect to x**:
    *   `dT/dx = cos(x) * e^(-alpha*t)` <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>
    *   `d^2T/dx^2 = -sin(x) * e^(-alpha*t)` <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>

*   **First partial derivative with respect to t**:
    *   `dT/dt = -alpha * e^(-alpha*t) * sin(x)` <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>

Substituting these into the heat equation (`dT/dt = K * d^2T/dx^2`, where `K` is a constant implicitly handled by `alpha`), we find that `T(x, t) = sin(x) * e^(-alpha*t)` indeed satisfies the PDE <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## Incorporating Boundary Conditions

The simple `sin(x)` solution, however, does not describe actual heat flow in a rod with no heat entering or leaving its ends <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. In such a scenario, the slope of the temperature curve at the boundaries (ends of the rod) must be zero for all times greater than zero <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. This is because the slope at a point is proportional to the rate of heat flow, and if no heat flows in or out, the slope must be zero <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

Mathematically, for a rod of length `L`, the boundary condition is:
`dT/dx (0, T) = 0` and `dT/dx (L, T) = 0` for all `T > 0` <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

### Adapting with Cosine Waves

To satisfy this boundary condition, we can adjust the function:

1.  **Using Cosine instead of Sine**: A cosine function `cos(x)` has a derivative of `-sin(x)`. At `x=0`, the derivative is `0`, meaning it's flat at that endpoint <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
2.  **Adjusting Frequency**: To ensure flatness at both ends, the frequency of the wave needs adjustment <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. Introducing a constant `omega` such that the function is `cos(omega*x)`:
    *   The first derivative is `-omega * sin(omega*x)` <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
    *   The second derivative is `-omega^2 * cos(omega*x)` <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
    *   This `omega^2` term must now appear in the exponential decay part of the solution, so the decay factor becomes `e^(-alpha * omega^2 * t)` <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. Higher frequency waves (`omega` values) decay more quickly <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

For a rod of length `L`, the frequencies `omega` that make the rightmost point flat are `n * pi / L`, where `n` is a whole number (0, 1, 2, ...) <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   When `omega = 0`, it results in a constant function, which is a valid solution as it has zero slope everywhere <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
*   When `omega = pi / L`, as `x` goes to `L`, `omega*x` goes to `pi`. The derivative of `cos(pi)` is `0`, satisfying the boundary condition.

This gives an infinite family of functions that satisfy both the PDE and the boundary conditions <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. This method of breaking down a general situation into simpler, idealized cases, often involving mixtures of [[understanding_basic_trigonometric_functions_and_waves | sine and cosine curves]] and exponentials, is a common strategy in [[connection_between_fourier_series_and_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.