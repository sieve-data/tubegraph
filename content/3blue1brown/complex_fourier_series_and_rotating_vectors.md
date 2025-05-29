---
title: Complex Fourier series and rotating vectors
videoId: r6sGWTCMz2k
---

From: [[3blue1brown]] <br/> 

A [[breaking_down_complex_functions_with_rotating_vectors | complex Fourier series]] is a mathematical concept where complex functions are broken down into a sum of vectors, each rotating at a constant integer frequency <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. When these vectors are added together tip-to-tail, their final tip draws out a specific shape over time <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. By adjusting the initial size and angle of each vector, virtually any desired shape can be drawn <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Visual Phenomenon
An animation illustrating this concept can feature hundreds of rotating arrows <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. While the action of each individual arrow is simple (rotation at a steady rate), the collective sum exhibits mind-boggling complexity and intricate detail, especially when zoomed in to reveal the contributions of smaller, faster-rotating arrows <a class="yt-timestamp" data-t="00:00:50">[00:01:09]</a>. Despite the chaotic frenzy, the swarm of vectors acts with coordination to trace out specific shapes <a class="yt-timestamp" data-t="00:01:12">[00:01:21]</a>. This emergent complexity is entirely controllable and describable by mathematics, simply by tuning the starting conditions <a class="yt-timestamp" data-t="00:01:27">[00:01:31]</a>. The formula governing this phenomenon is remarkably concise <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Connection to Traditional Fourier Series
Often, [[fourier_series_and_sine_waves | Fourier series]] are described as functions of real numbers broken down into a sum of [[fourier_series_and_sine_waves | sine waves]] <a class="yt-timestamp" data-t="00:01:52">[00:01:56]</a>. This is a special case of the more general rotating vector phenomenon <a class="yt-timestamp" data-t="00:02:01">[00:02:04]</a>. The origin of this idea traces back to Fourier's work on the [[fourier_series_and_their_relation_to_the_heat_equation | heat equation]] <a class="yt-timestamp" data-t="00:02:11">[00:02:14]</a>.

The [[fourier_series_and_their_relation_to_the_heat_equation | heat equation]] describes how [[applications_of_fourier_series_in_heat_distribution | temperature distribution]] on a rod evolves over time and also applies to many other phenomena <a class="yt-timestamp" data-t="00:02:32">[00:02:40]</a>. While challenging to solve for arbitrary heat distributions, a simple solution exists if the initial function resembles a cosine wave with frequencies tuned to be flat at endpoints <a class="yt-timestamp" data-t="00:02:44">[00:02:57]</a>. These waves decay exponentially over time, with higher frequency waves decaying faster <a class="yt-timestamp" data-t="00:03:01">[00:03:04]</a>.

The [[fourier_series_and_their_relation_to_the_heat_equation | heat equation]] is a linear equation, meaning that the sum of two solutions is also a new solution <a class="yt-timestamp" data-t="00:03:10">[00:03:15]</a>. This property allows for constructing custom solutions by scaling and combining exponentially decaying cosine waves <a class="yt-timestamp" data-t="00:03:34">[00:03:45]</a>. As higher frequency components decay faster, the combined sum tends to smooth out over time, leaving only low-frequency terms <a class="yt-timestamp" data-t="00:03:50">[00:04:02]</a>.

## Fourier's Breakthrough Insight
Fourier's significant contribution was asking how to express *any* initial distribution, even discontinuous ones like a step function (representing two rods at different initial temperatures), as a sum of [[fourier_series_and_sine_waves | sine waves]] <a class="yt-timestamp" data-t="00:04:18">[00:05:21]</a>. This question, seemingly absurd given the smooth nature of sine waves, led to the fundamental idea of breaking down functions and patterns into simple oscillations, a concept that became incredibly important and far-reaching across many fields <a class="yt-timestamp" data-t="00:05:10">[00:06:09]</a>.

### Infinite Sums and Approximation
While finite sums of [[fourier_series_and_sine_waves | sine waves]] can only approximate functions, Fourier considered infinite sums <a class="yt-timestamp" data-t="00:06:42">[00:06:46]</a>. An infinite sum is defined by the limit of its partial sums <a class="yt-timestamp" data-t="00:07:06">[00:07:37]</a>. For example, an infinite sum of rational numbers can equal an irrational number <a class="yt-timestamp" data-t="00:07:13">[00:07:26]</a>. Similarly, an infinite sum of continuous, wavy functions can precisely equal a discontinuous, flat function like a step function <a class="yt-timestamp" data-t="00:08:36">[00:08:40]</a>.

This implies that with infinite sums, qualitative changes are possible that finite sums alone cannot achieve <a class="yt-timestamp" data-t="00:08:47">[00:08:50]</a>. The field of [[mathematical_analysis_of_fourier_series | real analysis]] addresses the technical nuances of these infinite sums, such as convergence and the implications for discontinuous initial conditions in differential equations <a class="yt-timestamp" data-t="00:09:13">[00:09:25]</a>.

## Transition to Complex Numbers
While Fourier originally worked with real-valued functions, using complex numbers offers cleaner computations and a more general understanding <a class="yt-timestamp" data-t="00:59:53">[00:10:16]</a>. This approach also lays a foundation for later concepts like the [[introduction_to_fourier_transform | Laplace transform]] and the significance of exponential functions <a class="yt-timestamp" data-t="00:10:20">[00:10:28]</a>.

In this broader view, functions are inputs of real numbers (e.g., from 0 to 1) that output complex numbers, effectively drawing a path in the 2D complex plane <a class="yt-timestamp" data-t="00:10:29">[00:10:47]</a>. Real-valued functions are seen as "boring drawings" confined to the real number line <a class="yt-timestamp" data-t="00:11:03">[00:11:09]</a>.

Instead of [[fourier_series_and_sine_waves | sine waves]] as the fundamental building blocks, the focus shifts to breaking functions down into a sum of little vectors rotating at constant integer frequencies <a class="yt-timestamp" data-t="00:10:53">[00:11:00]</a>. For a real-valued function, vectors with frequencies `n` and `-n` will have the same length and be horizontal reflections, with their sum oscillating like a sine wave on the real number line <a class="yt-timestamp" data-t="00:11:25">[00:12:04]</a>. Thus, the original [[fourier_series_and_sine_waves | Fourier series]] for real-valued functions is a special case of this more general complex vector approach <a class="yt-timestamp" data-t="00:12:19">[00:12:25]</a>.

The core of [[fourier_series_and_sine_waves | Fourier series]] lies in the complex exponential, `e^(i*t)` <a class="yt-timestamp" data-t="00:12:58">[00:13:04]</a>. As the input `t` progresses, `e^(i*t)` traces a path around the unit circle at a rate of one unit per second <a class="yt-timestamp" data-t="00:13:04">[00:13:07]</a>. While the concept could be described purely with 2D vectors, `e^(i*t)` is more than just shorthand; it is crucial for solving differential equations <a class="yt-timestamp" data-t="00:13:27">[00:13:42]</a>. Thinking of complex numbers as "little arrows" simplifies visualizing their summation <a class="yt-timestamp" data-t="00:13:58">[00:14:06]</a>.

## Mathematical Formulation of Rotating Vectors
Each rotating vector can be described by the formula `c_n * e^(n * 2 * pi * i * t)` <a class="yt-timestamp" data-t="00:14:13">[00:15:29]</a>.
*   `e^(n * 2 * pi * i * t)`: Represents a vector rotating at a frequency `n` (number of cycles per second). The `2 * pi` factor ensures one full rotation for every unit increase in `t` (assuming `t` goes from 0 to 1) <a class="yt-timestamp" data-t="00:14:33">[00:14:42]</a>.
    *   `n = 0`: Represents a constant vector, `e^0 = 1` <a class="yt-timestamp" data-t="00:15:29">[00:15:35]</a>.
    *   `n = 1`: `e^(2 * pi * i * t)` rotates one cycle per second <a class="yt-timestamp" data-t="00:14:33">[00:14:36]</a>.
    *   `n = -1`: `e^(-2 * pi * i * t)` rotates one cycle per second in the opposite direction <a class="yt-timestamp" data-t="00:14:55">[00:14:59]</a>.
    *   This applies to all positive and negative integers `n` <a class="yt-timestamp" data-t="00:15:20">[00:15:25]</a>.
*   `c_n`: A complex constant that controls the initial size (magnitude) and direction (angle) of each vector <a class="yt-timestamp" data-t="00:15:40">[00:15:51]</a>. For example, `c_0` is the constant term representing the center of mass of the drawing <a class="yt-timestamp" data-t="00:15:53">[00:15:59]</a>.

The goal is to express any arbitrary function `f(t)` as a sum of these terms <a class="yt-timestamp" data-t="00:16:32">[00:16:40]</a>:
`f(t) = Σ (from n = -∞ to ∞) c_n * e^(n * 2 * pi * i * t)`

### Finding the Coefficients (`c_n`)
The coefficients `c_n` are found using an integral formula.
1.  **Finding `c_0` (the constant term):** This term is the average value of the function `f(t)` over its input range (e.g., from 0 to 1) <a class="yt-timestamp" data-t="00:16:51">[00:17:11]</a>. This average is represented by an integral:
    `c_0 = ∫ (from 0 to 1) f(t) dt` <a class="yt-timestamp" data-t="00:17:20">[00:17:24]</a>
    When this integral (average) is applied to the infinite sum, all rotating terms average to zero, leaving only the constant term `c_0` <a class="yt-timestamp" data-t="00:17:42">[00:18:44]</a>.

2.  **Finding any `c_n`:** To find a specific coefficient `c_n`, the trick is to first multiply `f(t)` by `e^(-n * 2 * pi * i * t)`. This effectively makes the `n`-th vector hold still <a class="yt-timestamp" data-t="00:18:48">[00:19:01]</a>. When the entire modified function is then averaged (integrated), all other terms `e^((k-n) * 2 * pi * i * t)` (where `k != n`) will perform a whole number of rotations and average out to zero <a class="yt-timestamp" data-t="00:19:16">[00:19:55]</a>. Only the `c_n` term remains, as its corresponding exponential becomes `e^0 = 1`, making it a constant in the modified function <a class="yt-timestamp" data-t="00:19:16">[00:19:55]</a>.

    The general formula for `c_n` is:
    `c_n = ∫ (from 0 to 1) f(t) * e^(-n * 2 * pi * i * t) dt` <a class="yt-timestamp" data-t="00:20:02">[00:20:08]</a>
    This expression represents modifying the 2D drawing to make the `n`-th vector still, then averaging to isolate that still part <a class="yt-timestamp" data-t="00:20:10">[00:20:23]</a>.

## Implementation and Application
When rendering animations of [[breaking_down_complex_functions_with_rotating_vectors | complex Fourier series]], computers treat the path as a complex function and compute these integrals numerically for a range of `n` values (e.g., from -50 to 50 for 101 vectors) <a class="yt-timestamp" data-t="00:20:36">[00:21:14]</a>. Numerical integration involves chopping the input interval into small pieces and summing discrete values <a class="yt-timestamp" data-t="00:21:18">[00:21:31]</a>. Once the coefficients `c_n` are found, they determine the initial angle and magnitude of each vector <a class="yt-timestamp" data-t="00:21:38">[00:21:42]</a>. Setting these vectors in motion and adding them tip-to-tail produces an approximation of the original path <a class="yt-timestamp" data-t="00:21:47">[00:21:51]</a>. As the number of vectors approaches infinity, the approximation becomes increasingly accurate <a class="yt-timestamp" data-t="00:21:55">[00:21:57]</a>.

For a step function, which is a real-valued (one-dimensional) and discontinuous function used in [[applications_of_fourier_series_in_heat_distribution | heat distribution]] modeling, the complex Fourier series approximation means the vector sum stays close to its initial value, then quickly jumps to the next value, and so on <a class="yt-timestamp" data-t="00:22:14">[00:22:53]</a>. Each pair of oppositely rotating vectors in this complex series corresponds to one of the cosine waves found in traditional [[fourier_series_and_sine_waves | Fourier series]] <a class="yt-timestamp" data-t="00:22:57">[00:23:01]</a>. Computing these coefficients involves performing the integral for `c_n` for the step function <a class="yt-timestamp" data-t="00:23:06">[00:23:16]</a>.

## Broader Implications
The decomposition of functions into combinations of exponential functions, as seen in [[fourier_series_and_sine_waves | Fourier series]], is a fundamental idea that reappears in various forms throughout mathematics and physics, especially in the context of linear differential equations <a class="yt-timestamp" data-t="00:24:01">[00:24:23]</a>. This includes applications in [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transforms]] and the [[introduction_to_fourier_transform | Laplace transform]].