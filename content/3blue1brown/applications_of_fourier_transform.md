---
title: Applications of Fourier Transform
videoId: spUNpyF58BY
---

From: [[3blue1brown]] <br/> 
The Fourier transform is a super important idea from math, with this video serving as an [[introduction_to_fourier_transform | introduction to the topic]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Even for those already familiar with it, seeing its components visually can be enriching <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The idea of the Fourier transform extends broadly beyond sound and frequency into many seemingly disparate areas of math and physics, highlighting its ubiquitous nature <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Decomposing Frequencies from Sound

The central example to understand the Fourier transform is the classic one: decomposing frequencies from sound <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

Sound waves, like a pure A at 440 beats per second, cause air pressure to oscillate as a function of time <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. When multiple notes are played simultaneously, the resulting pressure-versus-time graph becomes a complex, non-pure sine wave, as the pressure differences sum up at any given time <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. As more notes are added, the wave grows increasingly complicated <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

A microphone records only the final sum of these pressures over time <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. The core application of the Fourier transform in this context is to take such a complex signal and decompose it back into the pure frequencies that comprise it <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This process is akin to unmixing multiple paint colors that have been stirred together <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### The "Winding Machine" Analogy

The strategy to achieve this decomposition involves building a mathematical machine that treats signals with a given frequency differently from others <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This "machine" involves "winding up" the intensity-versus-time graph of a signal around a circle <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

1.  **Wrapping the graph**: Imagine a rotating vector whose length at any point in time equals the height of the signal graph <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. The rate at which the graph is wound around the circle is called the "winding frequency" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
2.  **Center of Mass**: When the winding frequency matches the frequency of the signal, the high points of the graph align on one side of the circle (e.g., right), and low points align on the opposite side (e.g., left) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. For most other winding frequencies, peaks and valleys are spaced out, causing the center of mass of the wound-up graph to remain close to the origin <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
3.  **Spike Detection**: When the winding frequency matches the signal's frequency, the center of mass moves unusually far from the origin <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. By plotting the x-coordinate of this center of mass against various winding frequencies, a significant spike appears at the signal's frequency <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This plot is what's called the "almost Fourier transform" <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Decomposing Mixed Signals

This machine becomes particularly useful because of its linearity: if two signals are added together, applying this "almost Fourier transform" to their sum yields the same result as applying the transform to each signal individually and then adding their results <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Since the transform of a pure frequency generates a spike only around that specific frequency, the transform of a combined signal will show peaks corresponding to all the individual frequencies present in the original mixture <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This allows the machine to pull out the original frequencies from their jumbled sums, effectively "unmixing" the signal <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

## Sound Editing and Filtering

A direct application of this principle is in sound editing <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. If a recording has an annoying high-pitched sound that needs to be removed:
1.  The sound signal, initially represented as intensities over time, is converted into its frequency domain representation using the Fourier transform <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
2.  The annoying high pitch will appear as a distinct spike at its corresponding high frequency in the Fourier transform <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
3.  This spike can then be "smashed down" or filtered out <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
4.  An inverse Fourier transform can then be applied to this modified frequency representation to convert it back into a time-domain signal, which will be the original recording without the unwanted high frequency <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

## Broader Applications

The Fourier transform is a critical tool for [[fourier_transforms_and_their_role_in_frequency_analysis | frequency analysis]] across many disciplines <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. While the video primarily focuses on sound, the concept extends to other areas of math and physics. Future discussions will delve into further applications beyond extracting frequencies from signals <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.

## Mathematical Formulation

The full mathematical expression for the Fourier transform builds upon the "winding machine" concept. The x-coordinate of the center of mass is only half the story; the wound-up graph exists in two dimensions, with a y-coordinate as well <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. In mathematics, two-dimensional concepts are elegantly represented using complex numbers, where the center of mass becomes a complex number with both a real (x-coordinate) and an imaginary (y-coordinate) part <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

Complex numbers are especially useful for describing rotation and winding. Euler's formula, `e^(iθ)`, represents a point on the unit circle after walking `θ` units counterclockwise <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. To represent a vector rotating clockwise at a frequency `f`, the expression becomes `e^(-2πift)` <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

When this exponential expression is multiplied by the signal function `g(t)`, it scales the rotating complex number according to the signal's value, effectively drawing the wound-up graph <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

The center of mass of this wound-up graph is found by integrating this product over a time interval <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. For the actual Fourier transform, this integral is performed without dividing by the time interval, meaning the output is scaled up by the duration of the signal <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This implies that a frequency persisting for a longer time will have a larger magnitude in its Fourier transform <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.

The Fourier transform, denoted as `g-hat(f)`, is a new function that takes a frequency as input and outputs a complex number representing the strength of that frequency in the original signal <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. While the plot shown in the video only graphs the real component (x-coordinate), the imaginary component could also be plotted for a complete description <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>. The theory of Fourier transforms often considers the integral over an infinite time interval, asking for the limit as the time interval grows to infinity <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.