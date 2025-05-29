---
title: Introduction to partial differential equations
videoId: ly4S0oi3Yz8
---

From: [[3blue1brown]] <br/> 

[[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | Partial differential equations (PDEs)]] represent a significant expansion of the concepts introduced in [[basics_and_significance_of_differential_equations | ordinary differential equations (ODEs)]]. While [[basics_and_significance_of_differential_equations | ODEs]] describe how a handful of changing numbers interact, [[partial_differential_equations_and_boundary_conditions | PDEs]] model scenarios where infinitely many values within a continuum change in concert over time <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. This often makes [[solving_differential_equations_with_examples | PDEs]] generally harder to [[numerical_methods_for_solving_differential_equations | solve]] than [[basics_and_significance_of_differential_equations | ODEs]] <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

## The Heat Equation: A Fundamental Example

The heat equation is a quintessential [[partial_differential_equations_and_boundary_conditions | partial differential equation]] used to describe how heat is distributed across an object and how this distribution changes over time as heat flows from warmer to cooler spots <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The core idea is that it's easier to describe how a system changes from moment to moment than to immediately define its full evolution <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>.

Variations of the heat equation appear in many areas of [[differential_equations_in_physics | physics]] and mathematics, including Brownian motion, the Black-Scholes equations in finance, and various diffusion processes <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>. Despite the general difficulty of [[solving_differential_equations_with_examples | PDEs]], the heat equation is one that can actually be [[solving_differential_equations_with_examples | solved]] <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.

### Temperature Function Representation

For a one-dimensional object like a rod, the temperature at any point `x` also changes over time `t` <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. Therefore, the temperature is a function of both position and time, `T(x, t)` <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>. This can be visualized as a surface above a two-dimensional input space (space and time) or as a graph of temperature changing over time <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.

## Partial Derivatives

Since the temperature function has multiple input dimensions (space and time), there are multiple rates of change at play <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>. These are described using partial derivatives:
*   **Derivative with respect to x (`∂T/∂x`)**: Measures how rapidly the temperature changes as one moves along the rod (slope of the surface parallel to the x-axis) <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.
*   **Derivative with respect to t (`∂T/∂t`)**: Measures the rate at which the temperature at a single point on the rod changes over time (slope of the surface parallel to the time axis) <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.

The notation for partial derivatives uses a special curly 'D', often called 'del' <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. Conceptually, a derivative can be thought of as the ratio between a small change in the function's output and the small change in the input that caused it, taken as a limit for increasingly small nudges to the input <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>. This applies to partial derivatives just as it does to ordinary derivatives <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>.

## Deriving the Heat Equation

The heat equation states that the rate of change of temperature with respect to time is proportional to the second partial derivative of temperature with respect to space <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>:

`∂T/∂t = α * ∂²T/∂x²`

Where `α` is a proportionality constant <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.

### Intuition from a Discrete Model

To understand the second derivative's role, consider a discrete setup with finitely many points in a row <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>. For any point, say `T₂`, if its two neighbors (`T₁` and `T₃`) are, on average, hotter than it, `T₂` will heat up. If they are cooler, `T₂` will cool down <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>. The rate of temperature change for `T₂` is proportional to the difference between the average of its neighbors and its own value <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>:

`dT₂/dt = α * ((T₁ + T₃)/2 - T₂)`

This expression can be rewritten as:

`dT₂/dt = α/2 * ((T₁ - T₂) - (T₂ - T₃))` <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>

The term `(T₁ - T₂) - (T₂ - T₃)` is known as a "second difference" <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>. It essentially measures how much `T₂` differs from the average of its neighbors <a class="yt-timestamp" data-t="11:08:00">[11:08:00]</a>. If the two differences `(T₁ - T₂)` and `(T₂ - T₃)` are the same, `T₂` will not tend to change, meaning it is the average of its neighbors <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>.

In the continuous case, the analog of a second difference is the second derivative, `∂²T/∂x²` <a class="yt-timestamp" data-t="11:29:00">[11:29:00]</a>. The second derivative measures how the rate of change itself changes <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>. Specifically, it indicates how a value compares to the average of its neighbors <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>. Points where the temperature distribution curves (positive second derivative) tend to flatten out, changing more quickly in the direction of that curvature <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.

## Generalization: The [[laplacian_and_multivariable_calculus_in_pdes | Laplacian]]

For objects spread out in more than one dimension, such as a plate or a three-dimensional body, the heat equation is similar but includes second derivatives with respect to all spatial directions <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>. The sum of these second spatial derivatives is a common operation known as the [[laplacian_and_multivariable_calculus_in_pdes | Laplacian]] <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>. Often written as `∇²` (nabla squared or an upside-down triangle squared), the [[laplacian_and_multivariable_calculus_in_pdes | Laplacian]] is a multivariable version of the second derivative and still measures how a point differs from the average of its neighbors, now considering all surrounding points <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>.

## Connection to [[connection_between_fourier_series_and_differential_equations | Fourier Series]]

The heat equation is historically significant because it was the physical problem that Jean-Baptiste Joseph Fourier was attempting to [[solving_differential_equations_with_examples | solve]] when he developed the mathematical concept of [[connection_between_fourier_series_and_differential_equations | Fourier series]] <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. [[connection_between_fourier_series_and_differential_equations | Fourier series]] demonstrate how any arbitrary curve can be approximated by summing many little rotating vectors, each rotating at a constant integer frequency <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. The more circles included, the closer the approximation gets <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. This seemingly abstract mathematical concept is directly related to the [[differential_equations_in_physics | physics]] of heat flow <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. The ability to [[solving_differential_equations_with_examples | solve]] the heat equation via [[connection_between_fourier_series_and_differential_equations | Fourier series]] involves constructing solutions from simple, idealized building blocks <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>.

---
**Further Reading:**
*   For those interested in exploring the ideas of calculus and their applications, especially in areas like [[differential_equations_in_physics | differential equations]], Stephen Strogatz's book *Infinite Powers* is recommended for its accessible communication of core concepts <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>.