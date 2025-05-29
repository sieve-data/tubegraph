---
title: Mathematical modeling of heat flow
videoId: ToIXSwZ1pJU
---

From: [[3blue1brown]] <br/> 

Mathematical modeling of heat flow involves understanding how temperature distribution changes over time, often studied in a simplified one-dimensional case like a rod <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This process provides a foundational example for an [[introduction_to_partial_differential_equations_and_the_heat_equation | partial differential equation]] (PDE) <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## The Heat Equation

The [[heat_equation_in_onedimensional_case | heat equation in the one-dimensional case]] describes that the rate at which temperature at a given point changes over time depends on the second derivative of that temperature at that point with respect to space <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Essentially, where there is curvature in space, there is a change in time <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Constraints in Solving the Heat Equation

[[solving_partial_differential_equations | Solving the heat equation]] is more complex than just satisfying the PDE itself, as it represents only one of three essential constraints for accurately describing heat flow <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>:

1.  **The PDE:** The core equation relating temperature change over time to spatial curvature <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
2.  **Boundary Conditions:** Specific conditions that the temperature function must satisfy at the physical boundaries of the system <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
3.  **Initial Condition:** The initial temperature distribution at time t=0, which is not chosen but given <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

These added constraints are where the primary challenge in [[solving_partial_differential_equations | solving the problem]] lies <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### Joseph Fourier's Contribution

In 1822, Joseph Fourier made a key contribution by developing a method to control the vast number of functions that solve the PDE and satisfy boundary conditions, allowing for the selection of a particular solution that fits a given initial condition <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. His solution is based on three fundamental observations <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:

1.  Certain sine waves offer simple solutions to the heat equation <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  If multiple solutions are known, their sum is also a solution <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  Any function can be expressed as a sum of sine waves, potentially infinitely many <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This last idea is the essence of [[fourier_series_and_their_relation_to_the_heat_equation | Fourier series]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

Sine waves are particularly useful because their relatively clean second derivatives make it easier to solve the heat equation for each wave component <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. Since a sum of solutions to the equation yields another solution, this provides a recipe for [[solving_partial_differential_equations | solving the heat equation]] for any complex initial temperature distribution <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Sine Waves and Exponential Decay in Solutions

Consider a simple initial temperature function *u(x,0) = sin(x)* for a rod <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   The second derivative of *sin(x)* with respect to *x* is *-sin(x)* <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   This means the amount the wave curves is equal and opposite to its height at each point <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   At time t=0, each point changes its temperature at a rate proportional to its own temperature, with a consistent proportionality constant <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   This implies that sine waves will be uniformly scaled down over time, maintaining their sine curve shape but looking like some constant times *sin(x)* for all times *t* <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

When a value changes at a rate proportional to itself, it points to an exponential relationship <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. The derivative of *e^(kt)* is *k* times *e^(kt)* <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. For a sine wave, the right-hand side of the heat equation becomes *-α* times the temperature function itself, where *α* is a constant <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Therefore, the solution is proposed to be scaled down by a factor of *e^(-αt)* <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

A function of *x* and *t* of the form *sin(x) * e^(-αt)* satisfies the [[introduction_to_partial_differential_equations_and_the_heat_equation | partial differential equation]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>:
*   The second partial derivative with respect to *x* is *-sin(x) * e^(-αt)* <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   The partial derivative with respect to *t* is *-α * sin(x) * e^(-αt)* <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   This confirms the function satisfies the heat equation <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

### Boundary Conditions for Heat Flow

The simple sine wave solution doesn't fully describe actual heat flow because it doesn't account for how the boundaries of the rod behave <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. For example, if no heat flows into or out of the rod, the slope of the temperature curve at either end must be zero <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This is described precisely as the partial derivative of the temperature function with respect to *x* at *0T* and *LT* (where L is the length of the rod) being zero for all times *T > 0* <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. This is a crucial "boundary condition" <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

To incorporate boundary conditions:
*   A cosine function *cos(x)* can be used instead of *sin(x)*, as its second derivative is also *-cos(x)*, and it naturally starts flat at *x=0* <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. So, *cos(x) * e^(-αt)* also satisfies the PDE <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   To satisfy the boundary condition at the right side (x=L), the frequency of the wave must be adjusted <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
*   Introducing a constant *ω* multiplied by *x* (e.g., *cos(ωx)*), the second derivative becomes *-ω² * cos(ωx)* <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
*   This means the exponential decay term in the solution must also include *ω²*, becoming *e^(-αω²t)* <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This makes intuitive sense: sharper curves (higher frequency) decay more quickly towards equilibrium <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   For the rightmost point to be flat (slope zero) at *x=L*, *ω* must be chosen such that *sin(ωL) = 0*. The frequencies that satisfy this are integer multiples of *π/L* (i.e., *ω = nπ/L*, where *n* is a whole number) <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. These are analogous to harmonics <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

This leads to an infinite family of functions that satisfy both the PDE and the boundary conditions, each looking like a cosine curve in space and exhibiting exponential decay in time <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. This framework then allows for constructing a more general solution in the next step <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

## General Themes in [[differential_equations_as_a_language_of_physics | Differential Equations]]

The approach used in [[modeling_heat_distribution_and_change_over_time | modeling heat distribution and change over time]] highlights several common themes in the field of [[differential_equations_as_a_language_of_physics | differential equations]] <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>:

*   Modeling boundaries with special rules distinct from the main differential equation for the interior is a regular theme, especially in [[introduction_to_partial_differential_equations_and_the_equation | PDEs]] <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   The strategy of breaking down general situations into simpler, idealized cases is ubiquitous <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   These simpler cases frequently involve mixtures of sine curves and exponentials, which is not unique to the heat equation <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.