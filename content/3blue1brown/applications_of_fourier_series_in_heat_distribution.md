---
title: Applications of Fourier series in heat distribution
videoId: r6sGWTCMz2k
---

From: [[3blue1brown]] <br/> 

The concept of [[complex_fourier_series_and_rotating_vectors | complex Fourier series]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, where rotating vectors sum to draw out complex shapes <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>, is a generalized form of how [[fourier_series_and_sine_waves | Fourier series are often described as sums of sine waves]] <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This fundamental idea, particularly its application in decomposing functions into simple oscillations <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>, originated from Fourier's efforts to solve the [[fourier_series_and_their_relation_to_the_heat_equation | heat equation]] <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## The Heat Equation and its Properties

The [[mathematical_modeling_of_heat_flow | heat equation]] is an equation that describes how temperature distribution on a rod evolves over time <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. It also applies to many other phenomena unrelated to heat <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Linearity of the Heat Equation
The heat equation is a "linear equation" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This means:
*   If two solutions are known, their sum is also a new solution <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   Solutions can be scaled by a constant, providing "dials to turn" to construct custom functions <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

This linearity is crucial because it allows for the combination of simple solutions to address more complex initial conditions <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Simple Solutions: Cosine Waves
A simple solution to the heat equation exists if the initial temperature distribution looks like a cosine wave, with its frequency tuned so it's flat at each endpoint <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. When graphed over time, these cosine waves simply get scaled down exponentially <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Higher frequency waves experience a faster exponential decay <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

When combining these waves, the higher frequency components decay faster, causing the overall sum to smooth out over time as these terms quickly approach zero <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This difference in decay rates for various frequency components captures the complexity in the evolution of heat distribution <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

## Fourier's Bold Idea: Decomposing Arbitrary Distributions

Despite the convenience of solving the heat equation for initial conditions that are simple waves or sums of waves, most real-world temperature distributions do not resemble this <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. For example, the initial temperature distribution of two rods at different uniform temperatures brought into contact would be a discontinuous "step function" <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. This function is flat, not wavy, and discontinuous <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

Fourier famously asked what seemed an absurd question at the time: How can any initial distribution, even a discontinuous one like a step function, be expressed as a sum of sine waves <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>? This sum must also be constrained to waves that satisfy specific boundary conditions, such as cosine functions whose frequencies are whole number multiples of a base frequency <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Infinite Sums and Approximations
Any finite sum of sine waves will only be an approximation, never perfectly flat or discontinuous <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Fourier, however, considered **infinite sums** <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. For the step function example (temperature 1 degree for the left rod, -1 degree for the right), it equals an infinite sum with specific coefficients (e.g., 1, -1/3, +1/5, -1/7 for odd frequencies, scaled by 4/pi) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

An infinite sum means that as more terms are added, the sequence of partial sums approaches a specific value <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. For functions, this means that for a given input, the sum of the scaled functions will approach the target function's value <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This allows an infinite sum of wavy, continuous functions to equal a discontinuous, flat function <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

### Mathematical Rigor and Real Analysis
While practical, this approach introduces technical nuances:
*   How does prescribing a value at a discontinuity affect the heat flow problem <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>?
*   What does it mean to solve a partial differential equation (PDE) with a discontinuous initial condition <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>?
*   Is the limit of solutions to the heat equation also a solution <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>?
*   Do all functions have a [[fourier_series_and_their_relation_to_the_heat_equation | Fourier series]] <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>?

These questions are addressed by [[mathematical_analysis_of_fourier_series | real analysis]] <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. The key takeaway is that summing all (infinitely many) heat equation solutions associated with these cosine waves does yield an exact solution for how a step function (representing the initial heat distribution) will evolve over time <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

## Complex Fourier Series and Coefficients

To find the coefficients of the Fourier series, a more general approach involving functions with complex number outputs is beneficial <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Functions with real number outputs (like temperature functions) are a special case of this broader view <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>, where [[fourier_series_and_sine_waves | sine waves correspond to pairs of vectors rotating in opposite directions]] <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

This broader context simplifies computations and provides a better foundation for understanding concepts like the Laplace transform <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. The heart of Fourier series lies in the complex exponential $e^{it}$ <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>, which describes a value moving around the unit circle as its input progresses <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

The coefficients ($c_n$) for each rotating vector (represented by $e^{n \cdot 2\pi i t}$) <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a> are determined by multiplying the original function $f(t)$ by $e^{-n \cdot 2\pi i t}$ and then taking its average (integral) over the interval <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. This effectively "kills" all moving vector terms, leaving only the desired coefficient <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

For the step function example (modeling heat dissipation), this calculation of coefficients allows the sum of rotating vectors to approximate the initial temperature distribution, quickly jumping between values as required <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>. Computing this integral allows for an exact answer for the coefficients, which can then be related back to the concept of cosine waves <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>.

## Conclusion

Fourier's breakthrough, the idea of breaking down functions into simple oscillations, proved incredibly important and far-reaching <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. Its origin in the [[mathematical_modeling_of_heat_flow | physics of heat flow]] <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>, seemingly unrelated to frequencies, highlights the general applicability of [[fourier_series_and_their_relation_to_the_heat_equation | Fourier series]] <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

This decomposition of a function into a combination of exponentials, used to solve differential equations like the heat equation, is a recurring and vital concept in mathematics <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.