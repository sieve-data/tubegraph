---
title: Breaking down complex functions with rotating vectors
videoId: r6sGWTCMz2k
---

From: [[3blue1brown]] <br/> 

A [[complex_fourier_series_and_rotating_vectors | complex Fourier series]] is a mathematical concept that describes how a complex function can be represented as a sum of rotating vectors <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This method is visually striking, as it allows for the [[animating_mathematical_functions | animating mathematical functions]] by showing how simple rotations combine to draw intricate shapes <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## The Visual Intuition

In a complex Fourier series animation, each small vector rotates at a constant integer frequency <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. When these vectors are added together tip-to-tail, their final tip traces out a shape over time <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. By adjusting the initial size and angle of each vector, virtually any shape can be drawn <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. For example, an animation might involve 300 rotating arrows <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. The action of each individual arrow is simple (rotation at a steady rate), yet their combined collection results in remarkable complexity <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This emergent complexity is controlled entirely by mathematics <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, where tuning the starting conditions allows the "swarm" to conspire and draw any desired shape, given enough arrows <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The underlying formula for this phenomenon is remarkably short <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Historical Context and Generalization

Traditionally, Fourier series are described in terms of functions of real numbers broken down as a sum of sine waves <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This approach is a special case of the more general rotating vector phenomenon <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

The origin of Fourier's idea stems from his work on the heat equation <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>, a linear equation that describes how temperature distribution evolves over time <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Simple solutions to this equation exist when the initial function resembles a cosine wave, which decays exponentially over time, with higher frequencies decaying faster <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Due to the linear nature of the heat equation, multiple solutions can be added together (and scaled) to form new solutions <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

Fourier's groundbreaking insight was to ask how any arbitrary initial distribution—even a discontinuous one like a step function (e.g., two rods of different temperatures brought into contact)—could be expressed as a sum of sine waves <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This idea, breaking down [[functions_as_vectors | functions and patterns]] as combinations of simple oscillations, became fundamental in mathematics and science <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### Infinite Sums and Approximations

While any finite sum of sine waves provides only an approximation, Fourier considered infinite sums <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. An infinite sum is understood as the limit of its partial sums <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. This means that a sum of continuous, wavy functions can indeed equal a discontinuous, flat function in the limit <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Applying this to the heat equation, an infinite sum of solutions associated with cosine waves can precisely describe the evolution of a discontinuous step function over time <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

## Complex Functions as Drawings

The mathematical framework for [[complex_functions_and_transformations | complex functions and transformations]] simplifies the computation of Fourier series <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
Instead of real-valued functions whose outputs lie on a number line, complex functions allow outputs to wander anywhere in the 2D complex plane <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. Such a function can be visualized as a drawing, where a "pencil tip" traces out different points in the complex plane as the input (e.g., time `t`) ranges from 0 to 1 <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. Real-valued functions are thus "boring drawings" confined to a one-dimensional line <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

## The Building Blocks: Rotating Vectors (Complex Exponentials)

The fundamental building block for breaking down complex functions is the complex exponential, specifically `e^(i * t)` <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. As the input `t` progresses, `e^(i * t)` traces a path around the unit circle at a rate of one unit per second <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. While the concept can be described purely with vectors, using complex numbers and the complex exponential `e^(x)` provides a cleaner computational approach and better reflects its utility in solving differential equations <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

For a Fourier series, each rotating vector is generally described by the formula `e^(n * 2π * i * t)` <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>:
*   `n`: An integer representing the frequency (positive for counter-clockwise rotation, negative for clockwise).
*   `2π`: Ensures one full cycle as `t` goes from 0 to 1.
*   `i`: The imaginary unit.
*   `t`: The input variable, often thought of as time.

The "control knobs" in this system are the initial size and direction of each vector <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. This is achieved by multiplying each `e^(n * 2π * i * t)` term by a complex constant, `c_n` <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. For example, `c_0` represents the constant vector (frequency 0) <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.

## Calculating the Coefficients (`c_n`)

The main challenge in Fourier series decomposition is finding these coefficients, `c_n` <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

The constant term `c_0` (representing the center of mass of the drawing) is the average value of the function `f(t)` over its input range (e.g., from 0 to 1) <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. This average is calculated using an integral:
`c_0 = ∫[0 to 1] f(t) dt` <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

All other rotating vectors (where `n ≠ 0`) make a whole number of rotations, so their average value over one cycle is 0 <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>. Thus, integrating `f(t)` effectively isolates `c_0` by "killing" all other terms <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

To find any other coefficient `c_n`, a clever trick is used:
1.  Multiply the entire function `f(t)` by `e^(-n * 2π * i * t)` <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. This operation shifts the frequency of each term in the sum <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
2.  Crucially, it makes the specific `n`-th vector (the one associated with `c_n`) "hold still" by canceling out its rotation <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.
3.  Then, take the average (integral) of this modified function <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. Since all other vectors will now make a whole number of rotations (and thus average to zero), only `c_n` remains <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.

The general formula for `c_n` is:
`c_n = ∫[0 to 1] f(t) * e^(-n * 2π * i * t) dt` <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.

This expression can be read as modifying the 2D drawing to make the `n`-th little vector hold still, and then performing an average that eliminates all moving vectors, leaving only the stationary part <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.

## Practical Application and Mathematical Nuances

In practice, these integrals are often computed numerically <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>, by chopping the input interval into small pieces and summing up the values <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. With a sufficient number of rotating vectors, the sum provides a highly accurate approximation of the original path <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

For real-valued functions like the step function, each pair of vectors rotating in opposite directions (`n` and `-n`) corresponds to one of the sine or cosine wave components <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.

While Fourier series are powerful, mathematical nuances exist regarding convergence, especially for discontinuous functions <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. These questions are addressed in real analysis <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

## Broader Implications

Beyond solving specific physical problems like the heat equation, the Fourier series concept offers a glimpse into a deeper mathematical idea: the critical role of exponential functions (including their complex and matrix generalizations) in differential equations, particularly linear ones <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>. The approach of breaking down a function into a combination of exponentials to solve differential equations reappears in various forms throughout mathematics <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.