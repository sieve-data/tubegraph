---
title: Introduction to Fourier Transform
videoId: spUNpyF58BY
---

From: [[3blue1brown]] <br/> 

The Fourier transform is a fundamental [[mathematical_principles_of_fourier_transform | mathematical idea]] that provides an animated approach to understanding how signals can be decomposed into their constituent frequencies <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This concept extends far beyond sound and frequency analysis into many seemingly disparate areas of mathematics and physics, highlighting its ubiquity <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Decomposing Frequencies from Sound

A common introductory example of the Fourier transform's utility is decomposing frequencies from sound <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### Sound Waves and Superposition
A pure musical note, such as an A at 440 beats per second (Hz), is characterized by air pressure oscillating in a wave 440 times each second <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. A lower-pitched note, like a D, has the same wave structure but with fewer oscillations per second <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

When multiple notes are played simultaneously, the resulting air pressure at any given time is the sum of the individual pressure differences from each note <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This summation creates a complex, non-pure sine wave <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. As more notes are added, the wave becomes increasingly complicated <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. A microphone records only this final, summed air pressure signal <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### The Central Question
The core problem is how to take a complex signal and [[fourier_transform_as_a_tool_for_analyzing_frequency_content_of_signals | decompose it into the pure frequencies]] that constitute it <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This process is analogous to "unmixing multiple paint colors that have all been stirred up together" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. The strategy involves building a "mathematical machine" that distinguishes signals of a given frequency from others <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## The Winding Machine Concept

### Wrapping a Signal Around a Circle
Consider a pure signal, for example, a sine wave with 3 beats per second <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Limit observation to a finite portion of this graph, such as 0 to 4.5 seconds <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. The key idea is to "wrap this graph up around a circle" <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

Imagine a rotating vector whose length at any point in time is equal to the height of the signal's graph at that time <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Higher points on the graph correspond to a greater distance from the origin, while lower points are closer <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. The speed at which this vector rotates around the circle is called the "winding frequency" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This is distinct from the signal's own frequency <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The choice of winding frequency dictates the appearance of the "wound-up graph" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Center of Mass
When the winding frequency is adjusted to match the signal's frequency (e.g., 3 cycles per second for a 3-beat-per-second signal), a special alignment occurs: all high points of the signal fall on one side of the circle, and all low points on the opposite side <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

To leverage this alignment, consider the wound-up graph as having mass, like a metal wire <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. A small dot represents the center of mass of this wire <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. For most winding frequencies, the peaks and valleys are distributed around the circle, keeping the center of mass close to the origin <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. However, when the winding frequency matches the signal frequency, the alignment causes the center of mass to be unusually far from the origin, indicating a "spike" <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

Plotting the x-coordinate of this center of mass against different winding frequencies reveals a peak at the signal's intrinsic frequency <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. A large spike near a winding frequency of zero indicates that the original cosine wave was shifted upwards (not oscillating around zero) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. This plot is termed the "almost Fourier transform" of the signal <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Decomposing Multiple Frequencies
The power of this "machine" lies in its ability to analyze signals composed of multiple frequencies <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. If a signal is formed by summing two pure frequencies (e.g., 2 and 3 beats per second), applying the winding machine to this combined signal will produce distinct spikes at both 2 and 3 cycles per second <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

This works due to a linearity property: the transform of a sum of signals is equivalent to the sum of the transforms of each individual signal <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Since the transform of a pure frequency signal is close to zero everywhere except for a spike at that specific frequency, summing the transforms results in a plot with peaks corresponding to all constituent frequencies <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This effectively "unmixes" the jumbled frequencies <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

## Glimpse of Application: [[application_of_fourier_transform_in_sound_editing | Sound Editing]]
The Fourier transform finds practical use in [[application_of_fourier_transform_in_sound_editing | sound editing]] <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. If a recording has an unwanted high-pitched noise, the signal, initially represented as intensities over time, can be converted into the frequency domain using the Fourier transform <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. The annoying pitch appears as a distinct spike at a high frequency <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. By "smushing down" this spike (effectively removing that frequency component), one obtains the Fourier transform of the desired, filtered sound <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. An inverse Fourier transform can then convert this back into a time-domain signal, yielding the recording without the unwanted noise <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

## From "Almost" to Actual Fourier Transform

### The Role of [[Complex numbers and Fourier Transform | Complex Numbers]]
The "almost Fourier transform" only considers the x-coordinate of the center of mass <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. However, the center of mass is a two-dimensional entity, also possessing a y-coordinate <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. In mathematics, it is elegant to represent two-dimensional concepts using [[complex_numbers_and_fourier_transform | complex numbers]] <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. The center of mass becomes a complex number with both a real (x) and an imaginary (y) part <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

[[application_of_complex_numbers_and_exponentials_in_fourier_series | Complex numbers]] are particularly well-suited for describing winding and rotation <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Euler's formula, `e^(iθ)`, maps an angle `θ` to a point on the unit circle in the [[application_of_complex_numbers_and_exponentials_in_fourier_series | complex plane]] <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. To represent continuous rotation at a rate of `f` cycles per second in a clockwise direction (the Fourier transform convention), the expression `e^(-2πift)` is used, where `t` is time <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### The Mathematical Formula
Given a signal intensity function `g(t)`, multiplying it by the exponential `e^(-2πift)` scales the rotating complex number according to the signal's value, effectively drawing the wound-up graph <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

To find the center of mass of this wound-up graph, one would traditionally sample many points, find their complex values, sum them, and divide by the number of points <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. In the limit of infinitely many points, this summation becomes an integral <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. The integral of this complex-valued function `g(t) * e^(-2πift) dt` represents the center of mass <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

The final distinction between this and the actual Fourier transform is that the Fourier transform simply takes the integral without dividing by the time interval <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This means the result is the center of mass scaled up by the length of the time interval <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. Physically, this implies that if a certain frequency persists for a longer duration, the magnitude of the Fourier transform at that frequency will be larger <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. For other frequencies, longer time intervals allow the wound-up graph more opportunity to balance out, effectively canceling out <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.

The **Fourier Transform** of a signal `g(t)` is commonly denoted as `g-hat(f)` (written as `G(f)` in many contexts) and is given by the integral:
$$
\hat{g}(f) = \int_{-\infty}^{\infty} g(t) e^{-2\pi i f t} dt
$$
<a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>

This formula:
*   Takes an intensity vs. time function, `g(t)`, as input <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.
*   Outputs a new function, `g-hat(f)`, which takes a frequency `f` (the winding frequency) as input <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
*   The output is a [[complex_numbers_and_fourier_transform | complex number]] (a point in the 2D plane), indicating the strength of that specific frequency in the original signal <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. The plot of the "almost Fourier transform" shown earlier was just the real (x) component of this complex output <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.

The theoretical definition often uses integral bounds from negative infinity to infinity, signifying that the expression is considered as the limit of finite time intervals as they grow indefinitely <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.

Despite its initial daunting appearance, understanding how [[application_of_complex_numbers_and_exponentials_in_fourier_series | exponentials]] relate to rotation, how `g(t)` scales this rotation to draw a wound-up graph, and how an integral can be interpreted as a center of mass, reveals the rich intuitive meaning behind the Fourier transform <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

The Fourier transform is a powerful tool with applications extending far beyond simple frequency extraction from signals <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.