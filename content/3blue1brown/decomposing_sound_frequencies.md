---
title: Decomposing sound frequencies
videoId: spUNpyF58BY
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_fourier_transform | Fourier transform]] is a fundamental mathematical idea used to analyze signals by decomposing them into their constituent frequencies <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Its application extends beyond sound and frequency into various fields of mathematics and physics, highlighting its ubiquity <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Sound as a Combination of Frequencies

A pure musical note, like an A at 440 beats per second, corresponds to an air pressure wave oscillating 440 times each second <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. A lower pitch note, such as a D, has the same wave structure but with fewer oscillations per second <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

When multiple pure notes are played simultaneously, the resulting air pressure wave is the sum of the individual waves <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This combined wave is often more complicated than a pure sine wave, as peaks and valleys from different notes can either reinforce or cancel each other out <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. A microphone records this final, complex sum of air pressure changes over time <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. The central challenge is to take such a complex signal and [[fourier_transform_as_a_tool_for_analyzing_frequency_content_of_signals | decompose it into the pure frequencies]] that make it up, similar to unmixing stirred paint colors <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## The Winding Machine: An Intuitive Approach

The general strategy for decomposition involves a "mathematical machine" that treats signals with specific frequencies differently <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

Consider a simple signal, such as a pure cosine wave with 3 beats per second, observed over a finite time interval <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The key idea is to "wrap" this graph around a circle <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This is visualized by imagining a rotating vector whose length at any given time corresponds to the height of the signal's graph at that time <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

There are two distinct frequencies at play:
*   The **signal frequency**: how many times the original signal oscillates per second (e.g., 3 beats per second) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   The **winding frequency**: how quickly the graph is wrapped around the circle (e.g., half a rotation per second) <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

The appearance of the wound-up graph changes depending on the winding frequency <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Center of Mass and Frequency Detection

To quantify this, imagine the wound-up graph as a metal wire with mass <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. A small dot represents the center of mass of this "wire" <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

*   For most winding frequencies, the peaks and valleys of the signal are spaced out around the circle, causing the center of mass to stay relatively close to the origin <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   However, when the winding frequency precisely matches the signal's frequency (e.g., 3 cycles per second), all the signal's high points align on one side of the circle (e.g., the right), and low points align on the opposite side (e.g., the left) <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This causes the center of mass to be unusually far from the origin in a specific direction <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

By plotting the x-coordinate of this center of mass against varying winding frequencies, a clear spike appears at the signal's inherent frequency <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. If the original signal oscillates around zero (without an overall upward shift), this plot will only show a spike at its specific frequency <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### Decomposing Mixed Signals

This "almost [[introduction_to_fourier_transform | Fourier transform]]" machine is particularly useful because it can unmix signals <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. If you combine two signals (e.g., a 3-beats-per-second wave and a 2-beats-per-second wave) and then apply this winding process, the resulting plot of the center of mass will exhibit spikes at *both* 2 and 3 cycles per second <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

This works because the transform has a property where applying it to two individual signals and then adding the results yields the same outcome as adding the signals first and then applying the transform <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Since the transform of a pure frequency is nearly zero everywhere except for a spike at that frequency, the transform of a sum of pure frequencies simply shows peaks corresponding to each original frequency <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Practical Application: [[application_of_fourier_transform_in_sound_editing | Sound Editing]]

The [[introduction_to_fourier_transform | Fourier transform]] provides a direct utility in [[application_of_fourier_transform_in_sound_editing | sound editing]] <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. If a recording has an unwanted high-pitched noise, the process is as follows:
1.  **Transform**: Take the [[introduction_to_fourier_transform | Fourier transform]] of the signal <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. The annoying high pitch will appear as a distinct spike at its corresponding high frequency <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
2.  **Filter**: "Smush down" or remove this unwanted spike in the frequency domain <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
3.  **Inverse Transform**: Apply an inverse [[introduction_to_fourier_transform | Fourier transform]] to convert the modified frequency data back into an audio signal <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. This new signal will be the original recording without the undesired frequency <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

## The Mathematical Formalism of the Fourier Transform

The "almost [[introduction_to_fourier_transform | Fourier transform]]" only considers the x-coordinate of the center of mass <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. The full [[mathematical_principles_of_fourier_transform | Fourier transform]] considers both the x and y coordinates, which is elegantly handled by [[Complex numbers and Fourier Transform | complex numbers]] <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. The center of mass becomes a [[Complex numbers and Fourier Transform | complex number]] with both a real and imaginary part <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

[[Complex numbers and Fourier Transform | Complex numbers]] are particularly suited for describing rotation <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Euler's formula, `e^(i*theta)`, describes a point on the complex plane obtained by rotating `theta` units counter-clockwise around a unit circle starting from the positive real axis <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. To represent a rotation at a specific frequency `f` (cycles per second) in the clockwise direction, the expression becomes `e^(-2*pi*i*f*t)`, where `t` is time <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

If `g(t)` represents the signal intensity over time, multiplying `e^(-2*pi*i*f*t)` by `g(t)` means the rotating [[Complex numbers and Fourier Transform | complex number]] is scaled by the signal's value at each moment in time <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This mathematically encapsulates the idea of winding the graph around a circle <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

To find the center of mass of this wound-up graph, one can approximate it by sampling many points from the signal, mapping them to the wound-up graph, and then averaging their [[Complex numbers and Fourier Transform | complex number]] positions <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. In the limit, as more points are sampled closer together, this sum becomes an integral <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

The **actual [[introduction_to_fourier_transform | Fourier transform]]** is defined as this integral without dividing by the time interval <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This means the result is the center of mass scaled up by the duration of the time interval <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. Consequently, if a specific frequency persists for a longer duration, the magnitude of the [[introduction_to_fourier_transform | Fourier transform]] at that frequency will be larger <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.

The [[introduction_to_fourier_transform | Fourier transform]] of a signal `g(t)` is a new function, denoted `g-hat(f)`, which takes a frequency `f` (the winding frequency) as input and outputs a [[Complex numbers and Fourier Transform | complex number]] <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. This [[Complex numbers and Fourier Transform | complex number]] represents the strength of that frequency in the original signal <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>. While visualizations often plot only the real component (x-coordinate), the imaginary component (y-coordinate) also provides information <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.

```latex
$$\hat{g}(f) = \int_{-\infty}^{\infty} g(t)e^{-2\pi i f t} dt$$
```

This formula encapsulates the entire winding machine concept:
*   `g(t)`: The original signal's intensity over time <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.
*   `e^(-2*pi*i*f*t)`: Represents the winding around the complex plane at a specific frequency `f` <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   The integral: Calculates the sum of all scaled complex numbers, essentially finding the weighted sum or "center of mass" of the wound-up graph <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

While in practical applications like [[application_of_fourier_transform_in_sound_editing | sound editing]], the integral is over a finite time interval, the theoretical definition often uses infinite bounds, considering the limit as the time interval extends infinitely <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.

The [[introduction_to_fourier_transform | Fourier transform]] extends its utility far beyond signal frequency extraction, touching many other areas of mathematics and physics <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.