---
title: Modeling heat distribution and change over time
videoId: ly4S0oi3Yz8
---

From: [[3blue1brown]] <br/> 

Understanding how heat distributes across an object and changes over time is a core problem in physics and mathematics <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This involves determining the temperature of every individual point within an object at any given moment and predicting how this distribution will evolve <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Heat naturally flows from warmer spots to cooler ones, tending to equalize the temperature throughout an object over time <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## The Heat Equation: A Partial Differential Equation

To describe this change, mathematicians use a [[introduction_to_partial_differential_equations_and_the_heat_equation | partial differential equation, the heat equation]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Typically, it is easier to describe how a system changes from moment to moment rather than directly predicting its full evolution <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The rule of change is expressed using derivatives, requiring an expansion beyond ordinary derivatives to handle multiple variables <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

Variations of the heat equation appear in various fields, including:
*   Brownian motion <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   Black-Scholes equations in finance <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   Various diffusion processes <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>

While many differential equations are difficult to solve, the heat equation is one that can actually be solved <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. Its solution is historically linked to [[applications_of_fourier_series_in_heat_distribution | Fourier series]], which were developed by Joseph Fourier while attempting to solve this physical problem <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Fourier series involve representing functions as a sum of simpler oscillating functions, a concept later applied to many areas of mathematics <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### One-Dimensional Case: The Rod

For a concrete [[heat_equation_in_onedimensional_case | one-dimensional example]], consider a rod placed along an x-axis, where each point is labeled by a unique number `x` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The temperature, `T`, at any point `x` also changes over time, `t` <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Therefore, the temperature is a function of both position and time, `T(x, t)` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. This function can be visualized as a surface in a two-dimensional input space (space and time), where slices across time show the temperature distribution at different moments <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### Partial Derivatives

When a function has multiple input dimensions, like the temperature function `T(x, t)`, there are multiple rates of change involved <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>:
*   **Derivative with respect to `x`**: How rapidly the temperature changes as you move along the rod <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **Derivative with respect to `t`**: The rate at which the temperature of a single point on the rod changes over time <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

These are called **partial derivatives** because each tells only part of the story of how the temperature function changes <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. They are denoted using a special curly `D`, called `del` (e.g., `∂T/∂x`, `∂T/∂t`) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Conceptually, a derivative can be read as a ratio between a small change to the function's output and the small change to the input that caused it, in the limit as the input change approaches zero <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. This applies to partial derivatives just as it does to ordinary derivatives <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

The heat equation states that the way the temperature function changes with respect to time is proportional to its second partial derivative with respect to space (`x`) <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Intuitively, points where the temperature distribution curves tend to change more quickly in the direction of that curvature <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

## Intuition Behind the Heat Equation

The heat equation can be derived from a simpler, discrete model:

### Discrete Setup
Imagine the rod is composed of a finite number of points, each with a temperature <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. For any specific point, say `x2` with temperature `T2`, its temperature will change based on its neighbors, `x1` and `x3`, with temperatures `T1` and `T3` <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

*   If the average of `T1` and `T3` is hotter than `T2`, `T2` will heat up <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   If the average of `T1` and `T3` is cooler than `T2`, `T2` will cool down <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   The rate of change of `T2` with respect to time (`dT2/dt`) is proportional to the difference between the average of its neighbors and its own value: `dT2/dt ∝ ( (T1 + T3) / 2 ) - T2` <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

This expression can be rewritten to highlight "differences of differences": `dT2/dt ∝ (T1 - T2) - (T2 - T3)` <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This is known as a **second difference** <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. It's a compact way to express how much a point's temperature differs from the average of its neighbors <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. The upshot is that the rate of change for a point's temperature is proportional to the second difference around it <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

### From Discrete to Continuous

As the discrete points become infinitesimally close, the analog of a second difference is the **second derivative** <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. Instead of absolute differences, one considers the rate of change of the rate of change <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. The heat equation, `∂T/∂t = α * (∂²T/∂x²)`, means that the rate of temperature change at a point is proportional to the second partial derivative of temperature with respect to position <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. A positive second derivative (graph curving upwards) means the temperature tends to increase, while a negative second derivative (graph curving downwards) means it tends to decrease <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.

This intuition is powerful: **second derivatives measure how a value compares to the average of its neighbors** <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. This mechanistic derivation from the idea of points tending towards the average of their neighbors provides a satisfying understanding of why the heat equation takes this form <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## Comparison to Ordinary Differential Equations (ODEs)

In contrast to [[introduction_to_partial_differential_equations_and_the_heat_equation | partial differential equations]] (PDEs), ordinary differential equations (ODEs) typically describe systems where a handful of numbers change over time, such as the coordinates of objects under gravity <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. The rate of change for any one value depends on the values of the other numbers, often written as a system of equations <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

For PDEs like the heat equation, we have infinitely many values changing across a continuum <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Each value's change depends on its immediate neighbors in a limiting sense, rather than a direct sum or product <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. The relationship on the right-hand side of a PDE is a derivative with respect to space, not time <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. In a sense, a single PDE can be viewed as a system of infinitely many equations, one for each point in the continuum <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

## Higher Dimensions: The Laplacian

For objects spread out in more than one dimension (e.g., a plate or a three-dimensional body), the heat equation is similar but includes second derivatives with respect to all spatial directions <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. The sum of these second spatial derivatives is a common operation known as the **Laplacian**, often written as `∇²` (upside-down triangle squared) <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. The Laplacian is a multivariable version of the second derivative <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>, and its intuition remains the same: it measures how different a point is from the average of its neighbors, now considering neighbors in all surrounding directions <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

## Further Reading

For those interested in exploring calculus and [[mathematical_modeling_of_heat_flow | mathematical modeling of heat flow]] further, *Infinite Powers* by Steve Strogatz is recommended <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>. The book emphasizes the idea of constructing solutions to complex real-world problems from simple, idealized building blocks, a principle exemplified by Fourier's work on the heat equation <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.