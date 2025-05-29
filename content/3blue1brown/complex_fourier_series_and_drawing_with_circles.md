---
title: Complex Fourier series and drawing with circles
videoId: r6sGWTCMz2k
---

From: [[3blue1brown]] <br/> 

A [[fourier_series_and_rotating_vectors | complex Fourier series]] is a mathematical concept that describes how complex shapes can be drawn by combining simple rotations. This method utilizes [[complex_numbers_and_fourier_transform | complex numbers]] and [[application_of_complex_numbers_and_exponentials_in_fourier_series | complex exponentials]] to represent and manipulate rotating vectors <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Core Concept: Drawing with Rotating Vectors

The fundamental idea involves multiple vectors, each rotating at a constant integer frequency <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. When these vectors are added together tip-to-tail, their final tip traces out a specific shape over time <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. By adjusting the initial size and angle of each vector, virtually any desired shape can be drawn <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

While the action of each individual arrow—rotation at a steady rate—is simple, the collective sum creates intricate and complex patterns <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Despite the chaotic appearance of the individual components, their underlying clockwork rigidity allows the swarm to coordinate and trace out precise shapes <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This emergent complexity is entirely controllable and describable by mathematics, allowing precise tuning of starting conditions to draw any desired form, provided enough "little arrows" are available <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Historical Context: Fourier and the Heat Equation

Historically, [[fourier_series_and_rotating_vectors | Fourier series]] were often described as functions of real numbers broken down into sums of sine waves <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This approach is a special case of the more general rotating vector phenomenon <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Fourier developed this idea while working on the [[fourier_series_in_solving_heat_equations | heat equation]] <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

The [[fourier_series_in_solving_heat_equations | heat equation]] describes how temperature distribution evolves on a rod, and it is a [[connection_between_fourier_series_and_differential_equations | linear equation]] <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. A key property of linear equations is that if you have two solutions, their sum is also a new solution, and they can be scaled by constants <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. For the heat equation, a simple solution exists if the initial temperature distribution resembles a cosine wave with specific frequencies (flat at endpoints) <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. These cosine waves decay exponentially over time, with higher frequency waves decaying faster <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This means a sum of such waves will tend to smooth out over time as high-frequency terms quickly vanish <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

### Fourier's Insight: Representing Discontinuous Functions

Fourier's significant contribution was to ask how any initial distribution, even a discontinuous one like a step function (e.g., two rods at different uniform temperatures brought into contact) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>, could be expressed as a sum of sine waves <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This question, initially seemingly absurd for functions that are flat or discontinuous, led to the development of [[fourier_series_and_rotating_vectors | Fourier series]] <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

Fourier recognized that an *infinite sum* of sine waves could approximate, and in the limit, *equal* a discontinuous function <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. For example, a step function can be represented by an infinite sum with coefficients like `1`, `-1/3`, `1/5`, `-1/7`, and so on, for odd frequencies, scaled by `4/pi` <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. This concept of infinite sums, where a sequence of partial sums approaches a value (like an irrational number from rational ones), allows for qualitative changes, enabling continuous functions to sum to a discontinuous one <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

## Expanding to Complex Numbers and 2D Drawings

While Fourier initially focused on real numbers and sine waves, a more general and computationally cleaner approach involves [[complex_numbers_and_fourier_transform | complex numbers]] <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. This broader view allows the function's output to be any [[complex_numbers_and_fourier_transform | complex number]] in the 2D plane, effectively treating a function as a "drawing" where a pencil tip traces points in the complex plane as the input `t` varies <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

The fundamental building block in this complex context is not sine waves, but rather little vectors rotating at constant integer frequencies <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. A function with real number outputs can be seen as a "boring drawing" confined to one dimension <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. In this case, pairs of vectors rotating in opposite directions (e.g., at frequency 1 and -1) will have the same length and be horizontal reflections, summing to produce an oscillation along the real number line—which is what a sine wave looks like in this context <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. Thus, the original [[fourier_series_and_rotating_vectors | Fourier series]] of real-valued functions is a special case of this more general 2D drawing concept <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

### The Role of the Complex Exponential

The heart of [[fourier_series_and_rotating_vectors | Fourier series]] lies in the [[application_of_complex_numbers_and_exponentials_in_fourier_series | complex exponential]], `e^(i*t)` <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>. As the input `t` progresses, this value moves around the unit circle at one unit per second <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. While Fourier series can be described purely in terms of vectors without `i` (the square root of negative one), the formulas become more convoluted, and it loses the authentic connection to why this idea is so useful for [[connection_between_fourier_series_and_differential_equations | solving differential equations]] <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. For understanding, `e^(i*t)` can be thought of as a shorthand for describing rotating vectors <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.

A general rotating vector for [[fourier_series_and_rotating_vectors | Fourier series]] is represented by `c_n * e^(n * 2pi * i * t)` <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
*   `n` is an integer representing the frequency (positive or negative) <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
*   `2pi` ensures that `e^(n * 2pi * i * t)` completes `n` full rotations as `t` goes from 0 to 1 <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.
*   `c_n` is a [[complex_numbers_and_fourier_transform | complex constant]] that determines the initial size (magnitude) and direction (angle) of the vector <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. For example, `c_0` represents the constant term (frequency 0), which is the average or "center of mass" of the drawing <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

## Calculating Fourier Coefficients `c_n`

The key challenge in using [[fourier_series_and_rotating_vectors | Fourier series]] to draw a function `f(t)` is to find these coefficients `c_n` <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

To find `c_0`, which represents the average value of the function `f(t)` over the interval (e.g., from 0 to 1), one can compute the integral of `f(t)` from 0 to 1 <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. When integrating the sum of rotating vectors, all terms that rotate (i.e., `n` is not 0) average out to zero, leaving only `c_0` <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

To find any other coefficient `c_n`, the "clever part" is to multiply the original function `f(t)` by `e^(-n * 2pi * i * t)` before integrating <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. This operation effectively "stops" the `n`-th vector (making its frequency 0) while causing all other vectors to rotate at non-zero frequencies <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. When the integral (average) is then computed, all the moving vectors average out to zero, leaving only the desired `c_n` <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.

The general formula for `c_n` is:
`c_n = ∫ f(t) * e^(-n * 2pi * i * t) dt` (over the interval from 0 to 1) <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

This expression effectively modifies the 2D drawing so that the `n`-th vector holds still, and then averages it, thereby isolating the constant part `c_n` <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>. Computers render these animations by treating the path as a complex function and numerically computing these integrals for a range of `n` values to find the coefficients `c_n` <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>. As the number of vectors (and thus computed `c_n` values) approaches infinity, the approximation of the original path becomes more accurate <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

## Broad Applications

The idea of breaking down functions and patterns into combinations of simple oscillations is profoundly important and far-reaching in mathematics and beyond <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. Although its origin lies in a seemingly unrelated physics problem (the [[fourier_series_in_solving_heat_equations | heat equation]]), the general applicability of [[fourier_series_and_rotating_vectors | Fourier series]] is immense <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

This concept of decomposing a function into [[application_of_complex_numbers_and_exponentials_in_fourier_series | exponential functions]] and using this decomposition to [[connection_between_fourier_series_and_differential_equations | solve a differential equation]] reappears repeatedly in various forms, especially with [[connection_between_fourier_series_and_differential_equations | linear equations]] <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>. The principles demonstrated by [[fourier_series_and_rotating_vectors | Fourier series]] are foundational to broader concepts like the [[mathematical_principles_of_fourier_transform | Fourier Transform]] and [[introduction_to_fourier_transform | Laplace Transform]] <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.