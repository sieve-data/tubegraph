---
title: Laplacian and multivariable calculus in PDEs
videoId: ly4S0oi3Yz8
---

From: [[3blue1brown]] <br/> 

The study of how values change across space and time often requires [[multivariable_calculus_and_complex_analysis | multivariable calculus]], particularly when dealing with [[introduction_to_partial_differential_equations | partial differential equations]] (PDEs). Unlike [[ordinary_differential_equations_odes_vs_partial_differential_equations_pdes | ordinary differential equations]] (ODEs) which model a handful of changing numbers, PDEs involve modeling infinitely many values changing in concert across a continuum [00:01:49]. They tend to be much harder to solve than ODEs but tell a richer story [00:07:29].

## The Heat Equation: An Introduction to PDEs

The heat equation is a prime example of a [[introduction_to_partial_differential_equations | partial differential equation]] [00:00:08]. It describes how heat distributes and changes over time within an object, such as a piece of metal or a rod [00:00:13]. The core question is how the temperature distribution across every point of an object will change over time as heat flows from warmer spots to cooler ones [00:00:24].

Similar to other [[differential_equations_in_physics | differential equations]], the approach is to describe how the setup changes from moment to moment rather than directly predicting the full evolution [00:01:01]. Variations of the heat equation are found in various fields, including Brownian motion, the Black-Scholes equations in finance, and other diffusion processes [00:01:24].

### Representing Temperature with Multiple Inputs

For a one-dimensional rod, the temperature at any point can be described as a function of its position `x` and time `t`, written as `T(x, t)` [00:04:01]. This means the function has multiple input dimensions: one for space and one for time [00:05:06]. This input space can be visualized as two-dimensional, with the temperature graphed as a surface above it, where each slice across time shows the temperature distribution at a given moment [00:04:05].

## Partial Derivatives

When a function has multiple input dimensions, there are multiple rates of change at play, leading to the concept of partial derivatives [00:05:10].

*   **Derivative with respect to `x`**: This measures how rapidly the temperature changes as you move along the rod [00:05:14]. It can be thought of as the slope of the temperature surface when sliced parallel to the `x`-axis [00:05:21].
*   **Derivative with respect to `t`**: This measures the rate at which the temperature of a single point on the rod changes over time [00:05:34]. It can be thought of as the slope of the surface when sliced parallel to the time axis [00:05:38].

These are called "partial derivatives" because each tells only part of the story of how the temperature function changes [00:05:44]. The notation for partial derivatives uses a special curly `D`, often called "del," instead of the ordinary `D` [00:05:51]. This notation emphasizes that the `delT` terms in the numerators refer to different changes: a small change to temperature after a small change in time, or a small change to temperature after a small step in space [00:06:04].

### Intuition Behind the Heat Equation

The heat equation states that the rate of change of temperature with respect to time is proportional to the second partial derivative with respect to space (x) [00:06:57]. This is expressed as:
∂T/∂t ∝ ∂²T/∂x² <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>

At a high level, this means that points where the temperature distribution curves tend to change more quickly in the direction of that curvature [00:07:09].

To understand how this equation arises, consider a discrete version with finitely many points in a row [00:08:01]:
*   If a point's two neighbors are, on average, hotter than it, the point will heat up [00:08:18].
*   If they are cooler on average, it will cool down [00:08:26].

More formally, the derivative of a point's temperature `T₂` with respect to time is proportional to the difference between the average of its neighbors (`T₁` and `T₃`) and its own value (`T₂`) [00:09:02]. This can be rearranged to show that it's proportional to the "difference of the differences" between neighboring temperatures, also known as a "second difference" [00:10:13]. The second difference effectively measures how much `T₂` differs from the average of its neighbors [00:11:08].

As this finite concept transitions to the infinite, continuous case, the analog of a second difference is the second derivative [00:11:32]. The second partial derivative with respect to `x` (`∂²T/∂x²`) measures how the rate of change of temperature itself changes along the rod [00:12:18]. Where the graph curves upwards, this slope increases (positive second derivative), and where it curves downwards, the slope decreases (negative second derivative) [00:12:32].

This leads to a meaningful intuition: second derivatives provide a measure of how a value compares to the average of its neighbors [00:12:53]. The heat equation thus intuitively states that curved temperature distributions tend to flatten out over time [00:13:02].

## The Laplacian

For objects spread out in more than one dimension, such as a plate or a three-dimensional body, the heat equation becomes more complex [00:13:31]. It includes the second derivative with respect to each spatial direction [00:13:39].

The sum of all these second spatial derivatives is a common operation with its own special name: the **Laplacian** [00:14:45]. It is often written as an upside-down triangle squared (∇²) [00:14:52].

The Laplacian is essentially a [[multivariable_calculus_and_complex_analysis | multivariable version of the second derivative]] [00:14:56]. Its intuition remains the same as in the one-dimensional case: it measures how different a point is from the average of its neighbors, but now these neighbors include points in all spatial directions (e.g., up, down, left, right, forward, back) [00:15:03]. For those familiar with [[multivariable_calculus_and_complex_analysis | multivariable calculus]], the Laplacian can be understood as the divergence of the gradient [00:15:23].