---
title: Heisenberg uncertainty principle and its relation to frequency and duration
videoId: MBnnXbOM5S4
---

From: [[3blue1brown]] <br/> 

The Heisenberg uncertainty principle in quantum mechanics states that the more precisely a particle's position is known, the less certain one can be of its momentum, and vice versa <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This principle is a specific instance of a much broader trade-off observed in everyday, non-quantum wave phenomena <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. Understanding this [[general_uncertainty_principle_in_nonquantum_contexts_like_sound_waves_and_doppler_radar | general uncertainty principle]] involves exploring the relationship between frequency and duration <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Core Idea: Frequency and Duration

An intuitive understanding of this trade-off can be seen in common scenarios:
*   **Turn Signals:** Observing a car's turn signals flashing in sync for a few seconds gives low confidence in their exact frequency, as they could fall out of sync later <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. However, observing them in sync for a full minute provides much greater certainty about their frequencies <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This demonstrates that certainty about frequency requires an observation spread out over time <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Musical Notes:** The shorter a musical note lasts, the less certain one can be about its exact frequency <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. For example, a clap or shockwave has no discernible pitch <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Conversely, a more definite frequency necessitates a longer duration signal <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. A short signal correlates with a wider range of frequencies, while a signal correlating with only a narrow range of frequencies must last for a longer time <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## The Fourier Transform and Signal Analysis

The Fourier transform is a mathematical tool for analyzing the frequencies present within any signal <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. It allows viewing a signal not by its intensity over time, but by the strength of its various frequencies <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

The process involves "winding" the signal around a circle at different frequencies <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. When the winding frequency matches the signal's dominant frequency, peaks and valleys align, shifting the "center of mass" of the wound-up graph <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. The position of this center of mass encodes the strength and phase of that frequency in the original signal <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

The **uncertainty principle** is revealed in how the signal's duration affects its Fourier transform:
*   **Long-duration signal:** If a signal persists over a long period, even slight differences in winding frequency cause the signal to balance out when wrapped around the circle <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This results in a very sharp drop-off in the Fourier transform's magnitude as the frequency shifts away from the dominant one, indicating a concentrated frequency representation <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Short-duration signal:** If a signal is localized to a short period, it doesn't have enough time to balance out when the winding frequency is adjusted <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This leads to a much broader peak in the Fourier transform, meaning the signal correlates with a wider range of frequencies <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

In essence, a signal concentrated in time must have a spread-out Fourier transform (correlating with a wide range of frequencies), and a signal with a concentrated Fourier transform must be spread out in time <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Doppler Radar Analogy

The [[general_uncertainty_principle_in_nonquantum_contexts_like_sound_waves_and_doppler_radar | general uncertainty principle]] is tangibly present in Doppler radar <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. Radar involves sending out radio wave pulses and analyzing their echoes to determine object distance and velocity <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Position and Time:** The time it takes for an echo to return indicates an object's distance <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   **Velocity and Frequency:** The Doppler effect causes the frequency of the echo to shift based on the object's velocity (e.g., higher frequency for objects moving towards the radar) <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

A radar operator faces a dilemma due to this trade-off <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>:
*   **Precise Position:** To achieve precise understanding of object distances, a very quick, short pulse is needed <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. However, a short pulse's Fourier transform is necessarily spread out in frequency <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. This means Doppler-shifted echoes from multiple objects are more likely to overlap in frequency space, making it ambiguous to determine individual velocities <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
*   **Precise Velocity:** To obtain a clean, sharp view of velocities, an echo occupying a small amount of frequency space is required <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. But for a signal to be concentrated in frequency space, it must be spread out in time <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Such a long echo would overlap with echoes from other objects, making their exact locations ambiguous <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

This is a clear example of the Fourier trade-off: crisp delineation for both position and velocity is impossible <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

## The Quantum Case: Particles as Waves

The [[Wave nature of particles and de Broglies hypothesis | Heisenberg uncertainty principle]] extends to the quantum realm through the concept of [[Wave nature of particles and de Broglies hypothesis | wave-particle duality]]. [[Wave nature of particles and de Broglies hypothesis | Louis de Broglie]], in his 1924 PhD thesis, proposed that all matter exhibits wave-like properties <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. Crucially, he concluded that the momentum of any moving particle is proportional to the spatial frequency of its associated wave (how many times the wave cycles per unit distance) <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

De Broglie's reasoning involved an analogy to the Doppler effect, but applied to spatial frequency and in the context of special relativity <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. He considered the energy of a particle as an oscillating phenomenon, similar to photons <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. Due to relativistic effects, observing this oscillating energy while moving relative to it causes the oscillations to appear out of phase over space <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. This "relativistic Doppler effect" implies that changes in a mass's movement correspond to changes in its spatial frequency, thereby linking momentum to spatial frequency <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

Applying the [[general_uncertainty_principle_in_nonquantum_contexts_like_sound_waves_and_doppler_radar | general Fourier trade-off]] to particles:
*   If a particle is described as a wave packet concentrated in space (meaning its position is well-defined) <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>, its Fourier transform (which represents its momentum) must be spread out <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   Conversely, if a particle's momentum is well-defined (its momentum wave is concentrated) <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>, then its position wave must be spread out <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

Unlike the Doppler radar case, where the ambiguity arises from measurement, in quantum mechanics, the particle *is* the wave <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. Therefore, the spread in position and momentum is fundamental to the particle itself, not an artifact of imperfect measurement techniques <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

### "Unsharpness Relation" and Probability

The Heisenberg uncertainty principle is often misinterpreted as solely a statement about unknowability or randomness <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. However, it is fundamentally a trade-off between how concentrated a wave and its frequency representation can be, applied to the premise that matter is a wave <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

The German term for the principle, which translates more directly to "unsharpness relation," better captures the Fourier trade-off without implying limitations on what can be known <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.

In quantum mechanics, when a particle's wave is concentrated in a region of space, it means there is a higher probability of finding the particle in that region, making its location more certain <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. But because this concentration implies a spread-out Fourier transform, the momentum wave will also be spread out, meaning there is no narrow range of momenta the particle has a high probability of occupying <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. The core fascination of the Heisenberg uncertainty principle lies in the fact that position and momentum have the same underlying mathematical relationship as sound and frequency <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.