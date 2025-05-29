---
title: Mathematical principles of Fourier Transform
videoId: spUNpyF58BY
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_fourier_transform | Fourier Transform]] is a fundamental mathematical idea that extends across many areas of math and physics <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This article introduces its core concepts and mathematical underpinnings.

## Decomposing Frequencies from Sound

The central example for understanding the [[introduction_to_fourier_transform | Fourier Transform]] is decomposing frequencies from sound <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

A pure sound note, like an A (440 beats per second), causes air pressure to oscillate in a wave 440 times each second <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. When multiple notes are played simultaneously, the resulting air pressure graph is a sum of the individual pressure differences, leading to a more complicated, non-pure sine wave <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. A microphone records this final summed pressure <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. The core question is how to take such a complex signal and decompose it back into its constituent pure frequencies <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This process is analogous to "unmixing" paint colors that have been stirred together <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

The strategy involves building a mathematical "machine" that differentiates signals based on their frequency <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### The Winding Machine Concept

Consider a pure signal, such as a sine wave oscillating at 3 beats per second, over a finite time interval (e.g., 0 to 4.5 seconds) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

The key idea is to "wrap" this graph around a circle <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>:
1.  Imagine a rotating vector whose length at any given time equals the height of the signal graph at that time <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. High points on the graph correspond to greater distances from the origin, and low points to closer distances <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
2.  The rate at which this graph is wrapped around the circle is called the "winding frequency" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This winding frequency can be adjusted independently of the signal's own frequency <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Center of Mass and Frequency Detection

When the winding frequency is adjusted, the wound-up graph changes shape <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. If we imagine this wound-up graph as a metal wire, it has a center of mass <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

*   For most winding frequencies, the peaks and valleys of the signal are spread out around the circle, causing the center of mass to remain close to the origin <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   However, when the winding frequency precisely matches the signal's frequency (e.g., 3 cycles per second for a 3-beats-per-second signal), all the high points align on one side (e.g., the right) and low points on the opposite side (e.g., the left) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This causes the center of mass to be unusually far from the origin in a specific direction (e.g., to the right) <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

By plotting the x-coordinate of this center of mass against different winding frequencies, a spike appears at the frequency of the original signal <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. If the signal is shifted up (i.e., its lowest values are still positive), there will also be a spike near zero frequency, corresponding to this upward shift <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

This plot is referred to as the "almost [[introduction_to_fourier_transform | Fourier Transform]]" of the original signal <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Unmixing Multiple Frequencies

The power of this machine lies in its ability to unmix multiple frequencies <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. If a signal is composed of multiple pure frequencies (e.g., 2 beats per second and 3 beats per second), the "almost [[introduction_to_fourier_transform | Fourier Transform]]" of their sum will show distinct spikes at each of those component frequencies <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

This is due to a property called linearity: applying the "almost [[introduction_to_fourier_transform | Fourier Transform]]" to two signals individually and then adding the results is the same as first adding the signals and then applying the transform <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Since the transform of a pure frequency is nearly zero everywhere except at that frequency, the combined transform clearly indicates the presence of each original frequency <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Formalizing the [[introduction_to_fourier_transform | Fourier Transform]] with [[complex_numbers_and_fourier_transform | Complex Numbers]]

The center of mass is a two-dimensional quantity with both an x and y coordinate <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. In mathematics, it's elegant to represent this 2D nature using [[complex_numbers_and_fourier_transform | complex numbers]] <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

[[complex_numbers_and_fourier_transform | Complex numbers]] are well-suited for describing winding and rotation <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

### Euler's Formula and Rotation

[[application_of_complex_numbers_and_exponentials_in_fourier_series | Euler's formula]] states that `e^(ix)` lands on a point on the unit circle after walking `x` units counter-clockwise from the positive real axis <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. To describe rotation at a rate of `f` cycles per second, the expression `e^(2πift)` can be used, where `t` is time <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. For the purpose of the [[introduction_to_fourier_transform | Fourier Transform]], the convention is to consider clockwise rotation, so a negative sign is added to the exponent: `e^(-2πift)` <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

### The [[introduction_to_fourier_transform | Fourier Transform]] Integral

Let `g(t)` be a function describing signal intensity versus time <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

Multiplying the rotation term `e^(-2πift)` by `g(t)` means the rotating complex number's length is scaled up and down according to the signal's value at that time <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This effectively describes the wound-up graph <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

To find the center of mass of this wound-up graph, one can sample many points, find where they land on the graph, add them as [[complex_numbers_and_fourier_transform | complex numbers]], and then divide by the number of sampled points to take an average <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. In the limit of infinitely many infinitesimally close points, this average is represented by an integral <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

The **[[introduction_to_fourier_transform | Fourier Transform]]** is defined as this integral, without the division by the time interval that would yield the exact center of mass <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This means the result is the center of mass scaled up by the duration of the time interval being considered <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. This scaling has the physical effect of increasing the magnitude of the transform at a certain frequency if that frequency persists for a long time in the original signal <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.

> [!definition] The [[introduction_to_fourier_transform | Fourier Transform]] Formula
> The [[introduction_to_fourier_transform | Fourier Transform]] of an intensity vs. time function, `g(t)`, is a new function, typically denoted `g-hat(f)`, which takes in a frequency `f` (the winding frequency) and outputs a [[complex_numbers_and_fourier_transform | complex number]] corresponding to the strength of that frequency in the original signal <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.
>
> Mathematically, it is expressed as:
> `g-hat(f) = ∫ g(t) * e^(-2πift) dt`
>
> Often, the bounds of this integral are negative infinity and infinity, considering the limit as the time interval grows <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.

This formula, though appearing complex, encapsulates the intuitive idea of winding a graph around a circle and tracking the resulting complex-valued "center of mass" to identify component frequencies <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

## Applications of the [[introduction_to_fourier_transform | Fourier Transform]]

One practical application of the [[introduction_to_fourier_transform | Fourier Transform]] is in [[application_of_fourier_transform_in_sound_editing | sound editing]] <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   An audio signal, initially represented as intensities over time, can be transformed into the frequency domain using the [[introduction_to_fourier_transform | Fourier Transform]] <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   An unwanted high-pitched sound will appear as a distinct spike at its corresponding high frequency in the [[introduction_to_fourier_transform | Fourier Transform]] output <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   This spike can then be "smashed down" or filtered out <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   An [[introduction_to_fourier_transform | inverse Fourier Transform]] can then be applied to convert the modified frequency data back into a time-domain signal, yielding the sound without the annoying frequency <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

The [[introduction_to_fourier_transform | Fourier Transform]]'s utility extends far beyond just extracting frequencies from signals, reaching into various areas of mathematics and physics <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.