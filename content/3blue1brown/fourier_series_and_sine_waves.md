---
title: Fourier series and sine waves
videoId: ToIXSwZ1pJU
---

From: [[3blue1brown]] <br/> 

[[Fourier series and their relation to the heat equation | Fourier series]] and the use of sine waves are central to solving partial differential equations (PDEs), such as the heat equation. Joseph Fourier's key contributions in 1822 provided a method to manage the vast number of potential solutions to the heat equation by leveraging the properties of sine waves <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## The Heat Equation and Its Constraints

The heat equation describes how temperature distribution along a rod changes over time <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It states that the rate of temperature change at a point over time depends on the second derivative of the temperature at that point with respect to space, meaning where there is curvature in space, there is change in time <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

Solving the heat equation requires satisfying three types of constraints <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>:
1.  The PDE itself <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
2.  Certain boundary conditions <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
3.  A specific initial condition (temperature at t=0) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Fourier's Fundamental Observations

Fourier's approach to solving the heat equation is based on three key observations <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
1.  **Sine waves offer a simple solution**: Certain sine waves inherently provide a straightforward solution to the heat equation <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
2.  **Superposition principle**: If multiple functions are solutions to the heat equation, their sum is also a solution <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  **Any function can be expressed as a sum of sine waves**: Most surprisingly, almost any practical temperature distribution, including discontinuous ones, can be represented as a sum of sine waves, potentially infinitely many <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This last concept is foundational to [[Fourier series and their relation to the heat equation | Fourier series]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## Why Sine Waves are Special

[[Application of sine waves in modeling | Sine waves]] are particularly useful in differential equations because they simplify calculations <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. For the heat equation, expressing a function as a sum of sine waves allows for easier computation of second derivatives, which are crucial for solving the equation <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

Consider a simple initial temperature distribution in the shape of `sine(x)` <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. The second derivative of `sine(x)` with respect to `x` is `negative sine(x)` <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. This means the amount a sine wave curves is equal and opposite to its height at each point <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

This unique property leads to a peculiar effect: each point's temperature changes at a rate proportional to its own temperature <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. As time progresses, the sine wave shape is uniformly scaled down, maintaining its form <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Connection to Exponentials

When a value's rate of change is proportional to the value itself, it indicates an exponential relationship <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. For the heat equation, because the right-hand side (second spatial derivative) of a sine wave solution is proportional to the function itself (negative sine of x), the solution involves scaling the sine wave by an exponential decay factor of `e^(negative alpha t)` <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

For a proposed function `T(x,t) = sine(x) * e^(-alpha t)` <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>:
*   The second partial derivative with respect to `x` is `negative sine(x) * e^(-alpha t)` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   The partial derivative with respect to `t` is `negative alpha * e^(-alpha t) * sine(x)` <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
This confirms that the function satisfies the heat equation <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## Incorporating Boundary Conditions

Real-world heat flow simulations often involve boundary conditions, such as no heat flowing into or out of the rod <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This implies that the slope of the temperature distribution at the ends of the rod must be zero for all times greater than zero <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. Specifically, the partial derivative of the temperature function with respect to `x` at `x=0` and `x=L` (where `L` is the rod's length) must be zero for all `t > 0` <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

To satisfy these boundary conditions, a cosine function can be used instead of a sine function, as it naturally has a zero slope at `x=0` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. To satisfy the condition at `x=L` as well, the frequency of the wave must be adjusted <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

When a frequency constant `omega` is introduced to `cosine(omega*x)`, the second derivative with respect to `x` becomes `negative omega^2 * cosine(omega*x)` <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. To balance the heat equation, the exponential decay term `e^(-alpha t)` must incorporate this `omega^2` factor, becoming `e^(-alpha * omega^2 * t)` <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This means sharper curves (higher frequency) lead to faster decay towards equilibrium <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

The frequencies `omega` that satisfy the zero-slope boundary condition at `x=L` are whole number multiples of `pi/L` (e.g., `omega = n * pi/L`, where `n` is an integer) <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. Even `omega=0` works, resulting in a constant function, which is a valid solution <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

These `cosine` functions with specific frequencies, combined with exponential decay, form an infinite family of functions that satisfy both the heat equation and the boundary conditions <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. This approach of breaking down complex problems into simpler, idealized cases (often involving sine or cosine curves and exponentials) is a common and powerful strategy in the field of differential equations <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.