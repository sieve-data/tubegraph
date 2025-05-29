---
title: Decomposing sound into frequencies
videoId: spUNpyF58BY
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_fourier_transform | Fourier transform]] is a fundamental mathematical idea that allows for an animated approach to understanding its components <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Its primary goal is to provide an [[introduction_to_fourier_transform | introduction]] to the topic <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The core example often used to understand the Fourier transform is the decomposition of frequencies from sound <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This idea extends beyond sound and frequency into various areas of math and physics <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Sound as a Time-Varying Signal

A pure sound, like an A at 440 beats per second, causes air pressure to oscillate up and down around its equilibrium, forming a wave <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This means it completes 440 oscillations each second <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. A lower pitch note, like a D, has the same wave structure but with fewer beats per second <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

When multiple notes are played simultaneously, the resulting pressure versus time graph is the sum of the individual notes' pressure differences <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This sum creates a more complex, wave-ish graph that is not a pure [[fourier_series_and_sine_waves | sine wave]] <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. As more notes are added, the wave becomes increasingly complicated <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. A microphone records this final sum of air pressure over time <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. The central question is how to take such a complex signal and decompose it back into its pure constituent frequencies <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## The Winding Machine Concept

The general strategy for decomposing frequencies is to build a [[mathematical_analysis_of_fourier_series | mathematical machine]] that treats signals with a specific frequency differently from others <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Wrapping the Graph Around a Circle

1.  **Initial Signal**: Consider a pure signal, for example, 3 beats per second, over a finite time interval (e.g., 0 to 4.5 seconds) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
2.  **Rotating Vector**: The key idea is to "wrap" this graph around a circle <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This is visualized by imagining a [[breaking_down_complex_functions_with_rotating_vectors | rotating vector]] whose length at each point in time corresponds to the height of the graph at that time <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. High points on the graph result in a greater distance from the origin, while low points are closer to the origin <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
3.  **Winding Frequency**: The speed at which this vector rotates around the circle is called the [[complex_plane_and_winding_frequency | winding frequency]] <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This is distinct from the signal's own frequency <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. Adjusting the [[complex_plane_and_winding_frequency | winding frequency]] changes the appearance of the wound-up graph <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### Center of Mass Analysis

When the [[complex_plane_and_winding_frequency | winding frequency]] matches the frequency of the signal (e.g., 3 beats per second), something special occurs: all the high points of the signal align on one side of the circle, and all the low points align on the opposite side <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

To quantify this, imagine the wound-up graph as a metal wire with mass <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. The center of mass of this wire will wobble as the [[complex_plane_and_winding_frequency | winding frequency]] changes <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. For most winding frequencies, peaks and valleys are spread out, keeping the center of mass close to the origin <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. However, when the [[complex_plane_and_winding_frequency | winding frequency]] matches the signal's frequency, the center of mass shifts significantly, for instance, unusually far to the right <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

A plot tracking the x-coordinate of this center of mass against different winding frequencies will show a spike at the signal's frequency <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. If the original signal is shifted up (oscillates around a positive value), there will also be a large spike around zero winding frequency, corresponding to the overall shift <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Decomposing Multiple Frequencies

This "almost [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]]" becomes particularly powerful when dealing with signals composed of multiple frequencies <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. If a signal is a sum of two pure frequencies (e.g., 2 beats per second and 3 beats per second), applying this winding machine will result in spikes at both 2 and 3 cycles per second <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This linearity means that the transform of a sum of signals is the sum of their individual transforms <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Since the transform of a pure frequency is close to zero everywhere except for a spike at that frequency, adding together two pure frequencies results in a transform graph with peaks at those specific frequencies <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This machine effectively unmixes the original frequencies from their jumbled sum <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Practical Application: Sound Editing

One practical application of this concept is in [[applications_of_fourier_transform | sound editing]] <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. If a recording has an unwanted high-pitch frequency, its [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] will show a distinct spike at that high frequency <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. By "smushing down" this spike in the frequency domain, one effectively filters out that high frequency from the sound <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. An inverse [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] can then convert this modified frequency representation back into a time-domain signal, yielding the original recording without the annoying pitch <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

## The Actual Fourier Transform

The "almost [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]]" described above primarily focuses on the x-coordinate of the center of mass <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. However, the center of mass is a two-dimensional entity, also possessing a y-coordinate <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

### Complex Numbers and Rotation

In mathematics, particularly when dealing with two-dimensional concepts like rotation, it is elegant to think of them in the [[complex_plane_and_winding_frequency | complex plane]] <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. The center of mass then becomes a complex number with both a real (x) and an imaginary (y) part <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

Euler's formula provides a concise way to describe winding and rotation using complex numbers: `e^(iθ)` corresponds to a point on the unit circle <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. For rotation at a rate of 1 cycle per second (clockwise), this can be expressed as `e^(-2πift)`, where `t` is time and `f` is frequency <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

Multiplying this exponential expression by the signal function `g(t)` (representing intensity versus time) causes the [[breaking_down_complex_functions_with_rotating_vectors | rotating vector]] to be scaled up and down according to the signal's value, effectively drawing the wound-up graph <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This small expression elegantly encapsulates the idea of winding a graph around a circle with a variable [[complex_plane_and_winding_frequency | winding frequency]] <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

### The Integral Formulation

To capture the center of mass of this wound-up graph, one can sum up many sampled points of the original signal on the wound-up graph as complex numbers and then divide by the number of points <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. In the limit, this sum becomes an integral <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

The **actual [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]]** is defined as this integral, without dividing out by the time interval <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This means it scales the center of mass by the length of the time interval considered <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. Consequently, if a certain frequency persists for a longer time, the magnitude of the [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] at that frequency increases <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. For other frequencies, longer time intervals allow the wound-up graph to balance itself around the circle, cancelling out contributions <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.

The common notation for the [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] of a function `g(t)` is `ĝ(f)` (g-hat of f) <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. This new function `ĝ(f)` takes in a frequency (`f`, the [[complex_plane_and_winding_frequency | winding frequency]]) and outputs a complex number <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>. This complex number represents the strength of that given frequency in the original signal, with its real part being the x-coordinate and its imaginary part being the y-coordinate <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.

The theoretical definition of the [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] often uses integration bounds from negative infinity to infinity, meaning it considers the limit as the time interval grows infinitely large <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.

For a [[visual_representation_of_signal_processing | visual representation]], see the process of the "winding machine" to derive the [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier Transform]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

### Extension Beyond Sound
The [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] extends to many other areas of mathematics and physics, beyond merely extracting frequencies from signals <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. For further [[applications_of_fourier_transform | applications of Fourier Transform]], refer to related topics.