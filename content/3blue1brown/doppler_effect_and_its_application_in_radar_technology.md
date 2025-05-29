---
title: Doppler effect and its application in radar technology
videoId: MBnnXbOM5S4
---

From: [[3blue1brown]] <br/> 

The [[general_uncertainty_principle_in_nonquantum_contexts_like_sound_waves_and_doppler_radar | general uncertainty principle]], which describes a trade-off between how concentrated a wave and its frequency representation can be, is tangibly demonstrated in [[general_uncertainty_principle_in_nonquantum_contexts_like_sound_waves_and_doppler_radar | Doppler radar]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This application is closely analogous to the quantum mechanical Heisenberg uncertainty principle <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

## Introduction to Radar

Radar technology involves sending out a radio wave pulse <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This pulse reflects off objects, and the time it takes for the echo signal to return allows for the deduction of how far away those objects are <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

## Deducing Velocity with the Doppler Effect

Radar can be used to deduce the velocities of objects by employing the [[general_uncertainty_principle_in_nonquantum_contexts_like_sound_waves_and_doppler_radar | Doppler effect]] <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. If a pulse is sent out with a specific frequency and reflects off an object moving towards the radar, the wave beats are "smushed together," resulting in the returned echo having a slightly higher frequency <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Conversely, an object moving away would cause a lower frequency echo. The size of this frequency shift allows for the calculation of the object's speed <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## The Fourier Transform Perspective

[[Fourier transform as a tool for analyzing frequency content of signals | Fourier transforms]] provide a method to analyze radar signals <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. The [[Fourier transform as a tool for analyzing frequency content of signals | Fourier transform]] of the original signal reveals its frequency components <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. For a short pulse, its [[Fourier transform as a tool for analyzing frequency content of signals | Fourier transform]] is necessarily spread out across a range of frequencies <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

When considering the Doppler-shifted echo, its [[Fourier transform as a tool for analyzing frequency content of signals | Fourier transform]] appears as a similar plot, but shifted up or down in frequency, corresponding to the object's velocity <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. The magnitude of this shift allows for the deduction of the object's speed <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## The Uncertainty Principle in Doppler Radar

A radar operator faces a dilemma where increased certainty about an object's position leads to less certainty about its velocity, and vice versa <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This is because the time and frequency of the echo signal correspond to the position and velocity of the measured object, respectively <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

*   **Long Pulse / Certain Velocity, Uncertain Position:** Sending out a pulse that persists over a long period of time means the echo is also spread out over time <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. While this allows for a very clear and sharp view of velocities (as a signal concentrated in frequency space must be spread out in time) <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>, it can lead to ambiguity in the precise locations of multiple objects because their echoes may overlap <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

*   **Short Pulse / Certain Position, Uncertain Velocity:** To achieve a precise understanding of objects' distances, a very quick, short pulse confined to a small amount of time is required <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. However, the [[Fourier transform as a tool for analyzing frequency content of signals | Fourier transform]] of such a short pulse is necessarily more spread out in frequency <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. This means that Doppler-shifted echoes from objects with various velocities, despite being well-separated in time, are more likely to overlap in frequency space, making it ambiguous to distinguish individual velocities <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

This trade-off is fundamental: it is impossible to have crisp delineation for both position (time) and velocity (frequency) simultaneously in radar <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.