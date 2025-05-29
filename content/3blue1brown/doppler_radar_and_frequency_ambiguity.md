---
title: Doppler radar and frequency ambiguity
videoId: MBnnXbOM5S4
---

From: [[3blue1brown]] <br/> 

Doppler radar is a technology that utilizes radio wave pulses to detect objects and determine their properties <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. The primary idea involves sending out a radio wave pulse and measuring the time it takes for an echo signal to return after reflecting off objects <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This return time allows for the deduction of how far away those objects are <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

## Deducing Velocity with the Doppler Effect

Beyond position, Doppler radar can also deduce the velocities of objects using the [[doppler_effect | Doppler effect]] <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. If a pulse is sent out and reflected off an object moving towards the radar, the wave's beats are "smushed together," resulting in a slightly higher frequency for the returned echo <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. Conversely, an object moving away would result in a lower frequency. By analyzing the size of this frequency shift, the object's speed can be determined <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## Fourier Transforms and Signal Analysis
[[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transforms]] are crucial for analyzing the frequencies within these signals <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. The Fourier transform of the original signal reveals its constituent frequencies <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. If the signal is a short pulse, its Fourier transform will necessarily be spread out <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. The Doppler-shifted echo, returning at a different frequency, means its Fourier transform will be a shifted version of the original plot <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## The Uncertainty Trade-off in Radar

The application of the [[general_uncertainty_trade_off_and_its_applications_to_sound_waves | general uncertainty trade-off]] to Doppler radar highlights a fundamental dilemma for radar operators: the more certain one is about an object's position, the less certain one can be about its velocity, and vice versa <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This trade-off is often referred to as the Fourier trade-off <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

### Position Certainty vs. Velocity Uncertainty
To achieve a precise understanding of an object's distance, radar systems require a very quick, short pulse of radio waves <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. However, a short pulse means its [[fourier_transforms_and_their_role_in_frequency_analysis | Fourier transform]] is necessarily more spread out in frequency space <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. For multiple objects with varying velocities, this leads to their Doppler-shifted echoes, though well-separated in time, overlapping significantly in frequency space <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. This overlap makes it ambiguous to decompose the summed signal and determine individual velocities accurately <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

### Velocity Certainty vs. Position Uncertainty
Conversely, to obtain a clean, sharp view of an object's velocity, the radar would need an echo signal that occupies a very small amount of frequency space <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. For a signal to be concentrated in frequency space, it must necessarily be spread out over time <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. If the transmitted pulse persists over a long period, the echo from an object is also spread out in time <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. In a practical scenario with multiple objects, these extended echoes would overlap, combined with noise and imperfections, making the precise locations of objects extremely ambiguous <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### The Dilemma
This inherent [[general_uncertainty_trade_off_and_its_applications_to_sound_waves | trade-off]] means that crisp delineation for both position and velocity cannot be achieved simultaneously <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. The radar operator must choose to prioritize certainty in one measurement at the cost of precision in the other.

## Analogy to Quantum Mechanics
This scenario in Doppler radar provides a tangible analogy to the quantum mechanical [[heisenberg_uncertainty_principle | Heisenberg uncertainty principle]] <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. In this context, the time and frequency of the echo signal correspond respectively to the position and velocity of the measured object <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This highlights that the Heisenberg uncertainty principle is a specific instance of a more general [[general_uncertainty_trade_off_and_its_applications_to_sound_waves | trade-off]] seen in wave phenomena <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The core idea relates to the interplay between a wave's frequency and its duration <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.