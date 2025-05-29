---
title: Solving partial differential equations
videoId: ToIXSwZ1pJU
---

From: [[3blue1brown]] <br/> 

Solving a partial differential equation (PDE) involves more than just finding a function that satisfies the equation itself <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. It also requires the function to meet specific [[boundary_conditions_in_pdes|boundary conditions]] and an initial condition <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. These additional constraints pose the primary challenge in finding an accurate solution <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

The heat equation, for a one-dimensional rod, describes how temperature distribution changes over time <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It states that the rate of temperature change at a point over time depends on the second derivative of temperature with respect to space at that point <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, meaning "where there's curvature in space, there's change in time" <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This serves as a foundational example of a [[introduction_to_partial_differential_equations_and_the_heat_equation|partial differential equation]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Fourier's Approach to the Heat Equation

Joseph Fourier's key contribution in 1822 was gaining control over the "vast ocean of functions" that solve the heat equation, allowing him to select the specific solution fitting a given initial condition <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. His solution is based on three fundamental observations:

1.  Certain sine waves offer a very simple solution to the heat equation <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  If multiple solutions are known, their sum is also a solution <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  Any function can be expressed as a sum of sine waves, potentially infinitely many <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This concept is central to Fourier series <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

Sine waves are particularly useful in [[differential_equations_and_their_applications|many applications]] because their clean derivatives simplify the process of solving [[differential_equations_and_their_applications|differential equations]] <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. By writing a function as a sum of these waves, the heat equation can be easily solved for each component, and then summed to solve for any complex initial temperature distribution <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Why Sine Waves Work with the Heat Equation

Consider a simplified scenario where the initial temperature function is `sine(x)` <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
The second derivative of `sine(x)` with respect to `x` is `negative sine(x)` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This means the amount a sine wave curves is "equal and opposite to its height" <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

At time `t=0`, each point's temperature changes at a rate proportional to its own temperature, with the same proportionality constant across all points <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This causes the sine curve shape to scale down uniformly over time <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

This phenomenon suggests an exponential relationship: if a value's rate of change is proportional to the value itself, the solution involves an exponential function <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. For a sine wave, the heat equation's right-hand side (the second spatial derivative) is proportional to the temperature function itself (e.g., negative alpha times the temperature function) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Therefore, the solution for a sine wave is proposed to scale down by a factor of `e` to the power of `negative alpha t` <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

A function like `sine(x) * e^(-alpha * t)` satisfies the heat equation <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. Taking the second partial derivative with respect to `x` yields `negative sine(x) * e^(-alpha * t)` <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Taking the partial derivative with respect to `t` yields `negative alpha * e^(-alpha * t) * sine(x)` <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. These match the heat equation's form.

### The Importance of Boundary Conditions

However, this simple solution does not fully describe actual heat flow <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. A straight line temperature distribution, for example, is a solution to the PDE itself (second derivative with respect to `x` is zero, derivative with respect to `t` is zero) <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>, but it would actually change over time in a simulation, approaching a uniform temperature <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

This discrepancy arises because real-world scenarios, like a rod with no heat flowing in or out, involve specific [[boundary_conditions_in_pdes|boundary conditions]] at the ends <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. The intuition for the second derivative in the heat equation is based on each point tending towards the average of its neighbors <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. At the boundary, there is no neighbor on one side <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

In a continuous model, if no heat flows into or out of the rod, the slope (first partial derivative with respect to `x`) at the boundary points must be zero for all times greater than zero <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. This is often described as the slope being proportional to the rate of heat flow <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. For a rod of length `L`, this means `∂T/∂x (0, T) = 0` and `∂T/∂x (L, T) = 0` for `T > 0` <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. This property is a crucial example of a [[boundary_conditions_in_pdes|boundary condition]] <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

### Adjusting Solutions for Boundary Conditions

To satisfy the boundary condition of zero slope at the endpoints, the sine wave solution needs adjustment:

*   **Cosine functions:** Using a cosine function instead of a sine function is a natural first step, as cosine of `x` is flat at `x=0` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. The second derivative of `cosine(x)` is also `negative cosine(x)`, so `cosine(x) * e^(-alpha * t)` still satisfies the PDE <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   **Adjusting Frequency:** To ensure the rightmost point also has a zero slope, the frequency of the wave must be adjusted <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Introducing a constant `omega` multiplied by `x` (e.g., `cosine(omega * x)`) means the second derivative will be `negative omega^2 * cosine(omega * x)` <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
    *   This implies that the exponential decay term must also include `omega^2` (i.e., `e^(-alpha * omega^2 * t)`) to balance the equation <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. Intuitively, sharper curves (higher frequency) decay more quickly <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Harmonic Frequencies:** For a rod of length `L`, the lowest frequency where the rightmost point is flat is when `omega` equals `pi / L` <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. All other frequencies satisfying this condition are whole-number multiples of `pi / L` <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Even `omega = 0` works, resulting in a constant function, which is a valid solution <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

This process yields an infinite family of functions that satisfy both the PDE and the [[boundary_conditions_in_pdes|boundary condition]] <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

## Recurring Themes in Differential Equations

Many concepts encountered while [[introduction_to_ordinary_and_partial_differential_equations|solving partial differential equations]] for the heat equation are common throughout the field of [[differential_equations_as_a_language_of_physics|differential equations]]:

*   **Boundary modeling:** The practice of modeling boundaries with special rules, distinct from the main differential equation characterizing the interior, is a very regular theme, especially in the context of PDEs <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   **Decomposition into simpler cases:** Breaking down a general situation into simpler, idealized cases is a common and effective strategy <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Sine waves and exponentials:** It's frequently observed that these simpler cases involve mixtures of sine curves and exponentials, a pattern not unique to the heat equation <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.