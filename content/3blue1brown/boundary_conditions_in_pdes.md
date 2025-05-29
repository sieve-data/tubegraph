---
title: Boundary conditions in PDEs
videoId: ToIXSwZ1pJU
---

From: [[3blue1brown]] <br/> 

When studying [[solving_partial_differential_equations | partial differential equations]] (PDEs), such as the [[heat_equation_in_onedimensional_case | heat equation]], a solution describing a physical phenomenon must satisfy more than just the equation itself <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>. It must also adhere to specific "boundary conditions" and an "initial condition" <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>. These added constraints are where the primary challenge in [[solving_partial_differential_equations | solving PDEs]] often lies <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>.

## Context: The Heat Equation
The [[heat_equation_in_onedimensional_case | heat equation]], as applied to a one-dimensional rod, describes how temperature distribution changes over time <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. It states that the rate of temperature change at a point depends on the second derivative of the temperature with respect to space at that point <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This means that where there is curvature in space, there is change in time <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>.

While there is a "vast ocean of functions" that technically satisfy the PDE itself, only a subset of these functions will satisfy the correct boundary conditions <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. Joseph Fourier's key contribution in 1822 was to gain control of this "ocean" to select the particular solution fitting a given initial condition <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

## The Problem with Idealized Solutions
An idealized solution, such as a temperature function at time `t=0` being simply `sin(x)`, while appearing to solve the PDE (e.g., `sin(x) * e^(-alpha*t)`), would not accurately describe actual heat flow <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>, <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>. Similarly, a straight line (`Temperature = constant * x`) satisfies the PDE (its second partial derivative with respect to x is zero, and its partial derivative with respect to time is zero) <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>. However, in reality, such a distribution would change over time, approaching a uniform temperature <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>.

The discrepancy arises because simulations or natural heat flow treat the boundary points of the rod differently from interior points <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>. The intuition for the second derivative in the heat equation is rooted in each point tending towards the average of its neighbors <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. At a boundary, there is no neighbor on one side <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.

## Specific Boundary Condition: No Heat Flow
When modeling a rod where no heat flows in or out, the simulation shows that the distribution looks flat at either boundary point almost immediately after the clock starts <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>. In the continuous case, the slope of the curve at the boundary will be zero for all times after `t > 0` <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.

This boundary condition is often described as:
*   The slope at any given point is proportional to the rate of heat flow at that point <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>.
*   Therefore, to model no heat flowing into or out of the rod, the slope at either end must be zero <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>.

Mathematically, this means:
*   `partial(Temperature)/partial(x) (0, T) = 0` <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>
*   `partial(Temperature)/partial(x) (L, T) = 0` <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>
    *   Where `L` is the length of the rod, and these conditions hold for all times `T > 0` <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

## Impact on Solutions
To satisfy this "flat at both endpoints" condition, a sine wave solution is tweaked into a cosine function <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>, <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>. A cosine function is naturally flat at `x=0` <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>. The second derivative of `cos(x)` is also `-1 * cos(x)`, so `cos(x) * e^(-alpha*t)` still satisfies the PDE <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>.

To satisfy the boundary condition on the right side (`x=L`), the frequency of the wave must be adjusted <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. Introducing a constant `omega` multiplied by `x` (e.g., `cos(omega*x)`) means:
*   The second derivative becomes `-omega^2 * cos(omega*x)` <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>.
*   To balance the PDE, the exponential decay part must also pick up an `omega^2` term (e.g., `e^(-alpha * omega^2 * t)`) <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>. This means sharper curves (higher frequency) decay more quickly <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.

For a rod of length `L`, the frequencies `omega` that satisfy the boundary condition (zero slope at `x=L`) are whole number multiples of `pi/L` (i.e., `omega = n * pi/L`, where `n` is an integer) <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>, <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>. This includes `n=0`, which results in a constant function, a valid solution <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>.

## General Significance
The necessity of boundary conditions is a very regular theme in the field of [[differential_equations_and_their_applications | differential equations]], especially in the context of [[introduction_to_ordinary_and_partial_differential_equations | partial differential equations]] <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>. Solving a PDE in practice virtually always involves satisfying some boundary condition, which demands as much attention as the PDE itself <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.

A common strategy in [[solving_partial_differential_equations | solving PDEs]] is to break down a general situation into simpler, idealized cases that often involve mixtures of sine curves and exponentials <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>. These simpler cases are then combined to construct a more general solution that satisfies all necessary boundary conditions <a class="yt-timestamp" data-t="13:03:00">[13:03:00]</a>.