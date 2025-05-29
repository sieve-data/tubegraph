---
title: Connection between Fourier series and differential equations
videoId: ly4S0oi3Yz8
---

From: [[3blue1brown]] <br/> 

The study of how systems change over time often involves [[basics_and_significance_of_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. While ordinary differential equations (ODEs) describe how a handful of numbers change, partial differential equations (PDEs) are used when an entire function changes over time <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. PDEs typically involve modeling infinitely many values changing in concert <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a> and are generally more challenging to solve than ODEs <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## The Heat Equation

The [[heat_equation_and_its_connection_to_fourier_series | heat equation]] is a prime example of a partial differential equation <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It describes how heat is distributed across an object over time, as heat flows from warmer to cooler spots <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. For instance, if two rods at different temperatures are brought into contact, the heat equation can determine the temperature distribution at each point over time <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Significance and Applications
Variations of the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] are fundamental in many areas of math and physics, including Brownian motion, the Black-Scholes equations in finance, and various diffusion processes <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. A deep understanding of this single setup yields numerous benefits <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### The Solvable PDE
Unlike many [[differential_equations_in_physics | differential equations]] that are difficult to solve <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, the heat equation is one that can actually be solved <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. This solvability is where [[fourier_series_in_solving_heat_equations | Fourier series]] come into play <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## Fourier Series: A Powerful Connection

The mathematical foundation of [[fourier_series_in_solving_heat_equations | Fourier series]] was discovered by Fourier while he was attempting to solve the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Visualizing Fourier Series with Rotating Vectors
One way to visualize [[fourier_series_and_rotating_vectors | Fourier series]] is through the concept of rotating vectors <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Many small rotating vectors, each spinning at a constant integer frequency, can be added tip-to-tail to trace out complex, arbitrary shapes <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. By adjusting the initial size and angle of each vector, it is possible to approximate any desired curve <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

The remarkable insight is that the mathematics enabling this "neat art project" is precisely the same as the mathematics describing the physics of heat flow <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

## Building the Heat Equation

To understand the [[heat_equation_and_its_connection_to_fourier_series | heat equation]], we consider the temperature `T` as a function of position `x` and time `t`, denoted `T(x, t)` <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. This function can be visualized as a surface in a two-dimensional input space (space and time) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### Partial Derivatives
Since the temperature function has multiple input dimensions, there are multiple rates of change involved, known as partial derivatives <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>:
*   The derivative with respect to `x` (∂T/∂x) describes how rapidly temperature changes as one moves along the rod <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   The derivative with respect to `t` (∂T/∂t) describes how a single point's temperature changes over time <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
These partial derivatives are denoted using a special curly 'D' symbol, called 'del' <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### The Equation Form
The [[heat_equation_and_its_connection_to_fourier_series | heat equation]] is expressed in terms of these partial derivatives <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>:
∂T/∂t = α * ∂²T/∂x² <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
This equation states that the rate of change of temperature with respect to time (∂T/∂t) is proportional to the second partial derivative with respect to `x` (∂²T/∂x²) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. The constant `α` is a proportionality constant <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### Intuition Behind the Second Derivative
The intuition for this equation comes from a discrete model:
*   **Discrete Case:** For a given point, if its two neighbors are on average hotter than it, it will heat up; if cooler, it will cool down <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. The rate of change of temperature for a point is proportional to how much it differs from the average of its neighbors <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This can be expressed as a "second difference" <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **Continuous Case:** The continuous analog of a second difference is the second derivative (∂²T/∂x²) <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. A key intuition is that second derivatives measure how a value compares to the average of its neighbors <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. Where the temperature graph curves upwards, the second derivative is positive, and the temperature tends to increase, and vice versa <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

> [!NOTE] The heat equation arising "mechanistically from thinking about each point as simply tending towards the average of its neighbors" <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a> provides satisfying intuition for this partial differential equation.

### Higher Dimensions: The Laplacian
For objects in more than one dimension (e.g., a plate), the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] includes second derivatives with respect to all spatial directions <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. The sum of these second spatial derivatives is known as the **Laplacian** (often written as ∇²) <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. The Laplacian also measures how a point differs from the average of its neighbors, but in multiple dimensions <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

## From Equation to Solution

The [[heat_equation_and_its_connection_to_fourier_series | heat equation]], in essence, represents a system of infinitely many equations, one for each point on the rod, where each point's change depends only on its immediate neighbors <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. The next step in understanding this topic is to learn how to solve these equations, which leads directly to the powerful mathematical tool of [[fourier_series_in_solving_heat_equations | Fourier series]] <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>. This approach exemplifies constructing solutions to complex real-world problems from simple, idealized building blocks <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.