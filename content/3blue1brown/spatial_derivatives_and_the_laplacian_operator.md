---
title: Spatial derivatives and the Laplacian operator
videoId: ly4S0oi3Yz8
---

From: [[3blue1brown]] <br/> 

## Introduction to Partial Differential Equations
After studying ordinary differential equations (ODEs), which describe how a handful of numbers change over time, the focus shifts to **partial differential equations (PDEs)** <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. PDEs involve functions with multiple input dimensions, where changes in one dimension can affect changes in another <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

A common example of a PDE is the **heat equation** <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This equation describes how heat distributes across an object, like a metal plate or a rod, over time <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The core question is how temperature distribution changes as heat flows from warmer to cooler spots <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### Applications of the Heat Equation
Variations of the heat equation appear in numerous fields beyond heat diffusion, including:
*   [[brownian_motion | Brownian motion]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   The Black-Scholes equations in finance <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   Various forms of diffusion <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>

While many differential equations are hard to solve, the heat equation is one that can actually be solved <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Its solution is historically linked to the development of Fourier series, which Fourier conceived while trying to solve this physical problem <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## Temperature as a Function of Space and Time
To analyze heat flow in a one-dimensional object, like a rod, the temperature is considered a function of both position (`x`) and time (`t`) <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. This function is often denoted as `T(x, t)` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

This input space (x and t) can be thought of as two-dimensional, with the temperature `T` graphed as a surface above it <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Each "slice" across time on this surface shows the temperature distribution at a given moment <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Partial Derivatives: Rates of Change in Multiple Dimensions
When a function, like `T(x, t)`, has multiple input dimensions, there are multiple rates of change at play <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. These are described using **partial derivatives** <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Types of Partial Derivatives for T(x, t)
1.  **Partial derivative with respect to x (`∂T/∂x`)**:
    *   Measures how rapidly the temperature changes as you move along the rod (spatial change) <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
    *   Can be visualized as the slope of the temperature surface when sliced parallel to the x-axis <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
2.  **Partial derivative with respect to t (`∂T/∂t`)**:
    *   Measures the rate at which the temperature of a *single point* on the rod changes over time <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
    *   Can be visualized as the slope of the surface when sliced parallel to the time axis <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### Notation for Partial Derivatives
Partial derivatives use a special curly 'D' symbol, called 'del' (`∂`), instead of the ordinary 'd' <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Despite the notation change, the fundamental operation is the same as [[computing_derivatives_of_functions | computing derivatives of functions]] <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

Similar to [[calculating_derivatives_and_their_applications | ordinary derivatives]], partial derivatives can be initially understood as the ratio of a small change in the function's output to the small change in the input that caused it <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This ratio is then considered in the limit as the input nudge approaches zero <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## The Heat Equation: `∂T/∂t ∝ ∂²T/∂x²`
The heat equation states that the rate of change of temperature with respect to time (`∂T/∂t`) is proportional to the **second partial derivative with respect to space (`∂²T/∂x²`)** <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### Intuition Behind the Heat Equation
At a high level, this means that points where the temperature distribution *curves* tend to change more quickly in the direction of that curvature <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Essentially, curved points tend to flatten out over time <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

### Deriving the Heat Equation from a Discrete Model
To understand this intuition, consider a discrete model of a rod with finitely many points (e.g., `x₁, x₂, x₃`) and corresponding temperatures (`T₁, T₂, T₃`) <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

The core idea is:
*   If a point's neighbors are, on average, hotter than it is, it will heat up <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   If they are cooler on average, it will cool down <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   The rate of change is proportional to this difference <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

This can be formalized for point `x₂` as:
`dT₂/dt ∝ ((T₁ + T₃)/2) - T₂` <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>

This expression can be rearranged to highlight "differences of differences":
`dT₂/dt ∝ ((T₁ - T₂) - (T₂ - T₃))` (with a proportionality constant) <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>

This term is known as a **second difference** <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. It compactly expresses how much `T₂` differs from the average of its neighbors <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

### The Second Derivative as the Continuous Analog
As the discrete steps shrink towards zero, the **second difference** in the discrete model becomes the **second derivative** in the continuous case <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. The second derivative (`∂²T/∂x²`) measures how the *rate of change itself changes* <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

*   If `∂²T/∂x²` is positive, the slope increases, indicating upward curvature <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
*   If `∂²T/∂x²` is negative, the slope decreases, indicating downward curvature <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

**General intuition**: Second derivatives provide a measure of how a value compares to the average of its neighbors <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. This mechanistic derivation from the idea of points tending towards the average of their neighbors provides satisfying insight into the heat equation <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.

## The Laplacian Operator
For objects spread out in more than one dimension (e.g., a 2D plate or a 3D volume), the heat equation looks similar but includes second derivatives with respect to all other spatial directions <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

Adding up all these second spatial derivatives is a common operation with its own special name: the **Laplacian** <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. It's often denoted by `∇²` (an upside-down triangle squared) <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

The Laplacian is essentially a multivariable version of the second derivative <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. Its intuition remains the same as the one-dimensional case: it measures how different a point is from the average of its neighbors, but now these neighbors are all around it, not just to the left and right <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. For those familiar with [[linear_transformations_and_dot_products | multivariable calculus]], the Laplacian can be seen as the divergence of the gradient <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.

Understanding PDEs like the heat equation and the concept of spatial derivatives with operators like the Laplacian is a powerful addition to one's mathematical vocabulary for describing the world <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.