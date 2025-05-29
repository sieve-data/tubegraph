---
title: The heat equation and its applications
videoId: ly4S0oi3Yz8
---

From: [[3blue1brown]] <br/> 

The [[heat_equation_and_its_connection_to_fourier_series | heat equation]] is an example of a [[introduction_to_partial_differential_equations | partial differential equation]] used to describe how heat is distributed across an object and how that distribution changes over time <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It models how heat flows from warmer spots to cooler ones <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Modeling Heat Distribution
To understand the [[heat_equation_and_its_connection_to_fourier_series | heat equation]], imagine an object like a piece of metal, where the temperature of every individual point is known at a given moment <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The fundamental question is how this temperature distribution will evolve over time <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

### One-Dimensional Example: A Rod
Consider a concrete one-dimensional example, such as a rod <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. If two rods at different, uniform temperatures are brought into contact, heat will flow from the hotter rod to the cooler one, tending to equalize the temperature across the entire system <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The [[heat_equation_in_onedimensional_rod | heat equation]] seeks to describe the exact temperature distribution at each point in time <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### The Temperature Function
For a one-dimensional rod, the temperature is considered a function of both position (x) and time (t), denoted as T(x, t) <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. This input space can be visualized as two-dimensional, with temperature graphed as a surface above it <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## The Nature of Differential Equations
Similar to [[differential_equations_in_physics | differential equations]] in general, the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] simplifies the problem by describing how the setup changes from moment to moment, rather than attempting to describe its full evolution immediately <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### [[role_of_derivatives_in_the_heat_equation | Role of Derivatives]]
The rule of change for temperature is expressed using derivatives <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Since the temperature function T(x,t) has multiple input dimensions (space and time), there are multiple rates of change involved:
*   The derivative with respect to x (∂T/∂x) describes how rapidly the temperature changes as one moves along the rod <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   The derivative with respect to t (∂T/∂t) describes the rate at which the temperature at a single point on the rod changes over time <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

These are called [[introduction_to_partial_differential_equations | partial derivatives]], denoted by a special curly 'D' (del) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Conceptually, a derivative can be read as a ratio between a small change in the function's output and the small change in the input that caused it, considering the limit as the input nudge approaches zero <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

### Deriving the [[heat_equation_and_its_connection_to_fourier_series | Heat Equation]]
The [[heat_equation_and_its_connection_to_fourier_series | heat equation]] is written in terms of these [[introduction_to_partial_differential_equations | partial derivatives]] <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. It states that the way the temperature function changes with respect to time depends on how it changes with respect to space, specifically, it's proportional to the second [[role_of_derivatives_in_the_heat_equation | partial derivative]] with respect to x <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

#### Intuition from a Discrete System
To build the [[heat_equation_and_its_connection_to_fourier_series | heat equation]], one can start with a discrete version: a row of finitely many points <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
The core intuition is that a particular point will heat up if its two neighbors are, on average, hotter than it is, and cool down if they are cooler <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. The rate of heating or cooling is proportional to this difference <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

This relationship can be rewritten in terms of "differences of differences," also known as a "second difference" <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This [[role_of_derivatives_in_the_heat_equation | second difference]] measures how much a point's temperature differs from the average of its neighbors <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

#### Transition to Continuous Case
As this finite, discrete model transitions to the infinite, continuous case, the analog of a [[role_of_derivatives_in_the_heat_equation | second difference]] is the [[role_of_derivatives_in_the_heat_equation | second derivative]] <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. The [[role_of_derivatives_in_the_heat_equation | second partial derivative]] of the function with respect to x (∂²T/∂x²) measures how the rate of change itself changes, corresponding to the curvature of the temperature graph <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

The **heat equation** is formally written as:
$$ \frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2} $$
Where α is a proportionality constant <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>, and this equation states that the rate of change of temperature at a point over time is proportional to the [[role_of_derivatives_in_the_heat_equation | second partial derivative]] of temperature with respect to space <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This intuitively means that "curved points tend to flatten out" <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

### PDEs vs. ODEs
Unlike [[solving_differential_equations_with_examples | ordinary differential equations]] (ODEs) which analyze a handful of changing numbers, [[introduction_to_partial_differential_equations | partial differential equations]] (PDEs) model infinitely many values changing in concert <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. PDEs generally tell a richer story and are much harder to solve than ODEs <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. The [[heat_equation_and_its_connection_to_fourier_series | heat equation]], in particular, acts like a system of infinitely many equations, where each point's temperature change depends only on its immediate neighbors <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

## Applications and Extensions
The [[heat_equation_and_its_connection_to_fourier_series | heat equation]] and its variations appear in many areas of mathematics and physics, including:
*   Brownian motion <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   The Black-Scholes equations in finance <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   Various diffusion processes <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>

### Higher Dimensions: The Laplacian
For objects spread out in more than one dimension (e.g., a plate or a three-dimensional body), the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] is similar but includes [[role_of_derivatives_in_the_heat_equation | second derivatives]] with respect to all spatial directions <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. The sum of these [[role_of_derivatives_in_the_heat_equation | second spatial derivatives]] is known as the Laplacian operator, often written as ∇² (upside-down triangle squared) <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. The Laplacian can be intuitively understood as measuring how different a point is from the average of its neighbors, considering neighbors in all directions <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

## Connection to [[fourier_series_in_solving_heat_equations | Fourier Series]]
The [[heat_equation_and_its_connection_to_fourier_series | heat equation]] is a solvable PDE <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. Historically, the physicist Joseph Fourier developed [[fourier_series_in_solving_heat_equations | Fourier series]] while attempting to solve this very physical problem <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. [[fourier_series_in_solving_heat_equations | Fourier series]] involve expressing arbitrary shapes or functions as a sum of many little rotating vectors, each rotating at a constant integer frequency <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This mathematical concept is deeply connected to the physics of heat flow <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Solving the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] is a foundational step in understanding [[fourier_series_in_solving_heat_equations | Fourier series]] further <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.