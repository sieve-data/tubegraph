---
title: Fourier series and rotating vectors
videoId: r6sGWTCMz2k
---

From: [[3blue1brown]] <br/> 

A [[complex_fourier_series_and_drawing_with_circles | complex Fourier series]] provides the mathematical foundation for animations depicting shapes drawn by rotating vectors <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. In this concept, each vector rotates at a constant integer frequency <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. When these vectors are added together, tip to tail, the final tip traces out a specific shape over time <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. By adjusting the initial size and angle of each vector, virtually any desired shape can be drawn <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

Although the action of each individual arrow is simple, rotating at a steady rate, the collective sum of these arrows results in mind-boggling complexity <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This "swarm" acts with a kind of coordination to trace specific shapes <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, a phenomenon that can be completely described and controlled mathematically <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. The remarkable aspect is that the ultimate formula for this intricate process is incredibly short <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Connection to Traditional Fourier Series
Traditional Fourier series often describe functions of real numbers as a sum of sine waves <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This is a special case of the more general rotating vector phenomenon <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Historical Context: The Heat Equation
The origin of Fourier series lies in the problem of the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This equation describes how temperature distribution on a rod evolves over time and applies to many other phenomena <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

For the [[heat_equation_and_its_connection_to_fourier_series | heat equation]], a simple solution exists if the initial function is a cosine wave with frequencies tuned to remain flat at each endpoint <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. These waves simply scale down exponentially over time, with higher frequency waves decaying faster <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

The [[heat_equation_and_its_connection_to_fourier_series | heat equation]] is a linear equation, meaning that the sum of two solutions is also a solution, and solutions can be scaled by constants <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This linearity allows for constructing custom functions that solve the equation by combining exponentially decaying cosine waves <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. The complexity of heat distribution evolution is captured by the differing decay rates for pure frequency components <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

Joseph Fourier achieved lasting recognition by asking a seemingly absurd question: How can *any* initial temperature distribution, even a discontinuous one like a step function, be expressed as an infinite sum of sine waves? <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a> <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a> These sums must be restricted to waves satisfying specific boundary conditions, such as cosine functions whose frequencies are whole number multiples of a base frequency <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

While any finite sum of sine waves is continuous and cannot perfectly represent a discontinuous function like a step function <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>, Fourier considered infinite sums <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. An infinite sum of continuous functions can equal a discontinuous function by approaching it in a limit <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. When all infinitely many solutions to the [[heat_equation_and_its_connection_to_fourier_series | heat equation]] associated with these cosine waves are summed, they yield an exact solution for how a step function evolves over time <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

## Functions as Drawings in the Complex Plane
For computational purposes, Fourier series can be generalized to functions whose output can be any complex number in the 2D plane <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. This is where the rotating vectors from the animation come into play <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

A function with a real input (e.g., time `t` from 0 to 1) and a complex output can be thought of as a "drawing," where a pencil tip traces points in the complex plane <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. Instead of sine waves, the fundamental building blocks become sums of little vectors rotating at constant integer frequencies <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

Functions with real number outputs are considered "boring drawings" confined to one dimension <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. When such a 1D drawing is decomposed into rotating vectors, vectors with frequencies `n` and `-n` will have the same length and be horizontal reflections of each other <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. Their sum remains on the real number line and oscillates like a sine wave <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. Thus, Fourier's original context of breaking down real-valued functions into sine waves is a special case of this more general idea of 2D drawings and rotating vectors <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

## The Role of [[application_of_complex_numbers_and_exponentials_in_fourier_series | Complex Exponentials]]
The core of [[complex_fourier_series_and_drawing_with_circles | Fourier series]] lies in the [[application_of_complex_numbers_and_exponentials_in_fourier_series | complex exponential]], `e^(i*t)` <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>. As the input `t` progresses, this value moves around the unit circle at a rate of one unit per second <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. While Fourier series *could* be described purely in terms of vectors without using the imaginary unit `i`, the formulas would be more convoluted <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. More importantly, leaving out `e^x` would not authentically reflect why this idea is so useful for solving [[connection_between_fourier_series_and_differential_equations | differential equations]] <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. For now, `e^(i*t)` can be thought of as a shorthand for rotating vectors, but it holds deeper significance <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.

## Formulating Rotating Vectors
Each rotating vector can be described by a formula using complex exponentials <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
*   The constant vector (frequency 0) is `e^(0 * 2pi * i * t)`, which simplifies to 1 <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.
*   A vector rotating one cycle per second is `e^(2pi * i * t)` <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.
*   A vector rotating one cycle per second in the opposite direction is `e^(-2pi * i * t)` <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   The general formula for a vector rotating `n` cycles per second (where `n` is any integer, positive or negative) is `e^(n * 2pi * i * t)` <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

The "knobs and dials" for controlling the initial size and direction of these vectors are complex constants, denoted as `c_n` <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. Each `c_n` is multiplied by its corresponding exponential term `e^(n * 2pi * i * t)`, determining its initial angle and total magnitude <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

The goal is to express any arbitrary function `f(t)` (e.g., one that draws an eighth note) as a sum of these terms, requiring a way to pick out each `c_n` constant from the function data itself <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.

## Computing Fourier Coefficients (`c_n`)
The easiest term to find is `c_0`, the constant term, which represents the "center of mass" for the drawing <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. It can be found by integrating (or continuously averaging) the function `f(t)` from 0 to 1 <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. This works because all other rotating vectors (those with non-zero frequencies) average out to zero over a full cycle <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

To compute any other coefficient, `c_n`, a "clever trick" is used:
1.  Multiply the entire function `f(t)` by `e^(-n * 2pi * i * t)` <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. This effectively makes the `n`-th vector component "hold still" <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.
2.  Because multiplying exponentials results in adding their exponents, the frequency term in each original vector's exponent gets shifted down by `n` <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
3.  Now, when an average (integral) is taken of this modified function, all terms except `c_n` will rotate a whole number of times and average out to zero <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.
4.  The `c_n` term, having been "held still," is the only one that remains after averaging <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.

This results in a general formula for `c_n`:
$$c_n = \int_0^1 f(t) \cdot e^{-n \cdot 2\pi i t} dt$$
This expression encapsulates the process of making the *n*-th vector hold still and then averaging to isolate its coefficient <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.

## Practical Application
When rendering animations, this integral is computed numerically for a range of `n` values (e.g., from -50 to 50 for 101 vectors) <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a> <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>. The path data itself can be read from an SVG file <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>. Numerical integration involves chopping the input interval into small pieces and summing the function's values <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>. Once the `c_n` constants are computed, they determine the initial angle and magnitude for each vector <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>. Setting them all rotating and adding them tip to tail creates an approximation of the original path <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. The accuracy of the approximation improves as the number of vectors used approaches infinity <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

### Step Function Example Revisited
Applying this to the step function, which models heat dissipation between two rods <a class="yt-timestamp" data-t="00:22:14">[00:22:14]</a>, the vector sum closely approximates the function's values, jumping discontinuously at the midpoint <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>. Each pair of vectors rotating in opposite directions in the complex plane corresponds to one of the cosine waves from the traditional [[fourier_series_in_solving_heat_equations | Fourier series]] formulation <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.

The ability to break down a function into a combination of exponentials and use that to solve a [[connection_between_fourier_series_and_differential_equations | differential equation]] is a fundamental idea that recurs in many forms, including the Laplace transform <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.