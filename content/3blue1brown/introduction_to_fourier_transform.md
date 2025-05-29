---
title: Introduction to Fourier Transform
videoId: spUNpyF58BY
---

From: [[3blue1brown]] <br/> 

The [[Fourier transforms and their role in frequency analysis | Fourier transform]] is a super important idea in mathematics <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This article serves as an introduction to the topic <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While the central example involves decomposing frequencies from sound <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, the idea extends well beyond sound into many seemingly disparate areas of math and physics, highlighting its ubiquity <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Decomposing Frequencies from Sound

A pure note, like an A at 440 beats per second, causes air pressure to oscillate up and down around its equilibrium, completing 440 oscillations each second <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. A lower pitch note, such as a D, has the same structure but with fewer beats per second <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

When multiple notes are played simultaneously, the resulting air pressure at any given time is the sum of the individual pressures from each note <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This can lead to a complicated pressure vs. time graph where peaks might align for high pressure, or cancel each other out <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The resulting wave is not a pure sine wave but something more complex <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Adding more notes further complicates the wave <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. A microphone records only this final sum of air pressure over time <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

The central question addressed by the [[Fourier transforms and their role in frequency analysis | Fourier transform]] is how to take such a complex signal and decompose it back into the pure frequencies that comprise it <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This process is akin to "unmixing" multiple paint colors that have been stirred together <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### The Winding Machine Concept

The general strategy for frequency decomposition involves building a mathematical "machine" that treats signals with a given frequency differently from others <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

Consider a pure signal, for example, one with 3 beats per second, and a finite portion of its graph between 0 and 4.5 seconds <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The key idea is to "wrap" this graph around a circle <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

This is visualized by imagining a rotating vector whose length at any given time is equal to the height of the signal graph at that time <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. High points on the graph correspond to a greater distance from the origin, while low points are closer <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. The rate at which the graph is wrapped around the circle is called the "winding frequency" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This winding frequency can be adjusted <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, and it determines the appearance of the wound-up graph <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

A significant observation occurs when the winding frequency matches the frequency of the signal <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. For a signal of 3 beats per second, when the winding frequency is also 3 cycles per second, all the high points of the graph align on one side of the circle (e.g., the right), and all the low points align on the opposite side (e.g., the left) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Center of Mass and the "Almost Fourier Transform"

To quantify this alignment, imagine the wound-up graph as a metal wire with mass <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. The center of mass of this wire will wobble as the winding frequency changes <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. For most winding frequencies, the peaks and valleys are spaced out, keeping the center of mass close to the origin <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. However, when the winding frequency matches the signal's frequency, the center of mass moves unusually far from the origin, for example, to the right <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

A plot can be created to track the x-coordinate of this center of mass for each winding frequency <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   For a winding frequency of zero (no winding), all points are bunched up, resulting in a relatively high x-coordinate if the original signal was shifted up from zero <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This spike around zero in the frequency plot corresponds to the overall vertical shift of the original signal <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   As the winding frequency increases, the x-coordinate of the center of mass generally moves closer to zero <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   Crucially, at the signal's true frequency (e.g., 3 beats per second), there is a distinct spike in the x-coordinate, indicating strong alignment <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

This plot of the winding frequency vs. the center of mass (specifically its x-coordinate) is an "almost Fourier transform" <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. It demonstrates how to pick out the frequency of a signal <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. If a different pure signal, such as one with 2 beats per second, is used, a spike will appear at 2 cycles per second instead <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

### Handling Multiple Frequencies

The power of this machine lies in its ability to analyze signals composed of multiple frequencies <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. If two signals (e.g., 2 beats/second and 3 beats/second) are added together, the resulting complex wave can still be fed into the winding machine <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. The wound-up graph will appear complex, but distinct alignments will occur at both 2 and 3 cycles per second <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

This works because applying the "almost Fourier transform" to individual signals and then adding the results yields the same outcome as adding the signals first and then applying the transform <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Since the transform of a pure frequency produces a spike only at that frequency, the transform of a sum of pure frequencies will show peaks corresponding to each original frequency <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This allows the machine to "unmix" the original frequencies from their combined sum <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

### Glimpse of [[applications_of_fourier_transform | Applications of Fourier Transform]]

One practical [[applications_of_fourier_transform | application]] is sound editing <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. If a recording has an annoying high-pitched sound, the original signal (intensity vs. time) can be transformed into the frequency domain using the [[Fourier transforms and their role in frequency analysis | Fourier transform]] <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. The unwanted high pitch will appear as a spike at a specific high frequency <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. By "smushing" this spike down (effectively removing that frequency), one can obtain the [[Fourier transforms and their role in frequency analysis | Fourier transform]] of the sound without the high pitch <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. An inverse [[Fourier transforms and their role in frequency analysis | Fourier transform]] can then convert this modified frequency representation back into a time-domain signal, yielding a cleaned-up sound <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

## The Actual [[Fourier transforms and their role in frequency analysis | Fourier Transform]]

The "almost Fourier transform" described above only considers the x-coordinate of the center of mass <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. Since the center of mass is a two-dimensional entity, it also has a y-coordinate <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. In mathematics, two-dimensional concepts are often elegantly represented using the [[Complex Fourier series and rotating vectors | complex plane]] <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. In this context, the center of mass becomes a complex number with both a real (x-coordinate) and an imaginary (y-coordinate) part <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Complex numbers are particularly well-suited for describing winding and rotation <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

[[Complex Fourier series and rotating vectors | Euler's formula]] ($e^{ix} = \cos(x) + i\sin(x)$) famously connects complex exponentials to rotation <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. Specifically, $e^{i \cdot \theta}$ lands on a point obtained by walking $\theta$ units counterclockwise around a unit circle starting from the positive real axis <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. To describe rotation at a rate of 1 cycle per second, the expression $e^{2\pi i t}$ is used, where $t$ is time <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. For a different frequency, $f$, the expression becomes $e^{2\pi i f t}$ <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

In the context of [[Fourier transforms and their role in frequency analysis | Fourier transforms]], the convention is to think of rotation in the clockwise direction, which introduces a negative sign in the exponent: $e^{-2\pi i f t}$ <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

### Deriving the Formula

To represent the winding process mathematically, a signal intensity function `g(t)` (e.g., a pure cosine wave) is multiplied by this exponential expression: `g(t) * e^(-2πi f t)` <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. This product signifies a rotating complex number whose length is scaled up or down according to the value of `g(t)`, effectively drawing the wound-up graph <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

To track the center of mass of this wound-up graph, one can approximate it by sampling many points from the original signal, mapping them to the wound-up graph, and then averaging their complex number representations <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. In the limit, as the number of sampled points approaches infinity, this average becomes an integral of the complex-valued function divided by the size of the time interval being considered <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. The integral of a complex-valued function can be interpreted as the center of mass of the wound-up graph <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.

The final distinction between this concept and the actual [[Fourier transforms and their role in frequency analysis | Fourier transform]] is that the [[Fourier transforms and their role in frequency analysis | Fourier transform]] simply takes the integral part, without dividing by the time interval <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This means the [[Fourier transforms and their role in frequency analysis | Fourier transform]] output is scaled up by the duration of the original graph <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. Physically, this means that a frequency persisting for a longer time will have a larger magnitude in its [[Fourier transforms and their role in frequency analysis | Fourier transform]] output <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.

The common notation for the [[Fourier transforms and their role in frequency analysis | Fourier transform]] of a function `g(t)` is `g-hat(f)` ($ \hat{g}(f) $) <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. The output `g-hat(f)` is a complex number, a point in the 2D plane, representing the strength of a given frequency in the original signal <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. While the real component (x-coordinate) can be plotted, the imaginary component (y-coordinate) also provides a fuller description <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.

The formula for the [[Fourier transforms and their role in frequency analysis | Fourier transform]] is:

$ \hat{g}(f) = \int_{-\infty}^{\infty} g(t)e^{-2\pi i f t} dt $ <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>

Although in practice, finite time intervals are used (e.g., in sound editing), the theory of [[Fourier transforms and their role in frequency analysis | Fourier transforms]] often defines the integral with bounds from negative infinity to infinity <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. This implies considering the limit as the time interval grows infinitely large <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

This formula, though daunting at first glance, encapsulates the rich intuitive meaning of winding a graph around a circle, using exponentials for rotation, and interpreting the integral as a center of mass <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.

The [[Fourier transforms and their role in frequency analysis | Fourier transform]] extends to many other areas of mathematics beyond extracting frequencies from signals <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.