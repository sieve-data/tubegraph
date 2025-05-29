---
title: General uncertainty trade off and its applications to sound waves
videoId: MBnnXbOM5S4
---

From: [[3blue1brown]] <br/> 

The [[heisenberg_uncertainty_principle_in_quantum_mechanics | Heisenberg uncertainty principle]], often associated with the quantum realm, is actually a specific instance of a more general trade-off that appears in many everyday circumstances involving waves <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This fundamental concept revolves around the interplay between a wave's frequency and its duration <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Intuitive Understanding: Turn Signals and Musical Notes

Even without delving into complex mathematics, an intuitive grasp of this principle is possible <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

Consider the flashing turn signals of a car <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>:
*   If observed for only a few seconds, they might appear to have the same frequency <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. However, this short observation provides low confidence, as they could fall out of sync over more time, revealing different frequencies <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   Conversely, if observed for a full minute, and the signals remain in sync, there is much greater confidence that their frequencies are identical <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
    *   This demonstrates that certainty about frequency information requires an observation spread out over time <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

This trade-off—between the duration of an observation and the confidence in determining frequency—is an example of the general uncertainty principle <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

The same principle applies to musical notes <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>:
*   The shorter a musical note lasts, the less certain its exact frequency can be <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. For instance, it's impossible for even someone with perfect pitch to determine the pitch of a clap or shockwave due to its extremely short duration <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   Conversely, a more definite frequency necessitates a longer duration signal <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   More accurately, a short signal highly correlates with a wider range of frequencies, while a signal strongly correlating with only a narrow range of frequencies must last for a longer time <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Explaining with the Fourier Transform

The [[application_of_sine_waves_in_modeling | Fourier transform]] is the mathematical construct used to analyze frequencies within a signal <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. It transforms a signal, typically viewed as intensity over time, into a representation of the strength of its various component frequencies <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### How the Fourier Transform Works
The core idea involves "winding" a signal around a circle <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Imagine a rotating vector whose length is determined by the signal's height at each point in time <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

*   When the winding frequency matches the signal's dominant frequency (e.g., 5 cycles per second), the signal's peaks align on one side of the circle and valleys on the other <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This causes the "center of mass" of the wound-up graph to be significantly off-center <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   The position of this center of mass encodes the strength of that specific frequency in the original signal <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The distance from the origin indicates the frequency's strength, and its angle corresponds to the frequency's phase <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Essentially, this winding mechanism measures how well a signal correlates with a given pure frequency <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Frequency Spread and Signal Duration

When plotted, the Fourier transform shows a spike at the dominant frequency (e.g., 5 beats per second) <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Crucially, the spread of this spike around the dominant frequency indicates that pure sine waves *near* that frequency also correlate well with the signal <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This spread is central to the uncertainty principle <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

*   **Long-duration signal**: If a signal persists over a long period, even a slight difference in winding frequency from the dominant one will cause the signal to balance itself out around the circle <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This results in a sharp drop-off in the magnitude of the Fourier transform as the frequency shifts away from the dominant one, indicating a narrow, concentrated frequency range <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Short-duration signal**: If a signal is localized to a short period, it doesn't have enough time to balance out around the circle when the winding frequency is adjusted away from its dominant frequency <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This leads to a much broader peak in the frequency plot, meaning the signal correlates with a wider range of frequencies <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

This is the essence of the general uncertainty principle, phrased mathematically <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>:
> A signal concentrated in time must have a spread-out Fourier transform, meaning it correlates with a wide range of frequencies <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Conversely, a signal with a concentrated Fourier transform (narrow frequency range) has to be spread out in time <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

This fundamental [[numerical_methods_and_chaos_theory_in_differential_equations | Fourier tradeoff]] means that crisp delineation for both time and frequency is impossible <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.