---
title: General uncertainty principle in nonquantum contexts like sound waves and Doppler radar
videoId: MBnnXbOM5S4
---

From: [[3blue1brown]] <br/> 

The [[heisenberg_uncertainty_principle_and_its_relation_to_frequency_and_duration | Heisenberg uncertainty principle]], often associated with quantum mechanics, states that the more precisely one knows a particle's position, the less certain one can be of its momentum, and vice versa <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This principle is not exclusive to the quantum realm; it is a specific instance of a more general trade-off that appears in various everyday, non-quantum situations involving waves <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Core Idea: Frequency and Duration Interplay

At its heart, the general uncertainty principle deals with the relationship between frequency and duration <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. An intuitive understanding of this principle can be seen in common scenarios:

*   **Turn Signals**: If two car turn signals flash in sync for a few seconds, you might assume they have the same frequency <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. However, this short observation provides low confidence, as they could fall out of sync over a longer period <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Observing them in sync for a full minute, however, would significantly increase your confidence that their frequencies are identical <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Certainty about frequency requires an observation spread out over time <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Musical Notes**: The shorter a musical note lasts, the less certain one can be about its exact frequency <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. For instance, it's impossible to determine the pitch of a brief sound like a clap or a shockwave <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Conversely, a more definite frequency necessitates a longer-duration signal <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Correlation with Frequency Range

More accurately, a short signal correlates highly with a wider range of frequencies <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Conversely, a signal that correlates strongly with only a narrow range of frequencies must persist for a longer time <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This concept is clarified through the [[relationship_between_classical_and_quantum_waves | Fourier transform]].

## The Fourier Transform and Uncertainty

The [[relationship_between_classical_and_quantum_waves | Fourier transform]] is a mathematical tool that converts a signal from its intensity over time into the strength of various frequencies within it <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. It helps analyze how well a signal correlates with a given pure frequency <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

Consider a signal playing 5 beats per second over 2 seconds <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The Fourier transform shows a spike at 5 beats per second, indicating the dominant frequency <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. The spread around this peak indicates that frequencies near 5 beats per second also correlate well with the signal <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

The key to the uncertainty principle lies in how this frequency spread changes with signal duration:

*   **Long-Duration Signal**: If a signal persists for a long time, even a slight difference in the winding frequency (for the transform) causes the signal to average out around the circle, leading to a sharp drop-off in the transform's magnitude <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This results in a very narrow, sharp peak in the frequency plot <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Short-Duration Signal**: If a signal is localized to a short period, it doesn't have enough time to balance itself out around the circle when the winding frequency is adjusted <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This results in a much broader peak around the dominant frequency in the Fourier plot <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

In summary, a signal concentrated in time must have a spread-out Fourier transform, meaning it correlates with a wide range of frequencies <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Conversely, a signal with a concentrated Fourier transform must be spread out in time <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. This is the general uncertainty principle expressed mathematically.

## Application in [[doppler_effect_and_its_application_in_radar_technology | Doppler Radar]]

The general uncertainty principle has tangible implications in [[doppler_effect_and_its_application_in_radar_technology | Doppler radar]] technology. Radar operates by sending out radio wave pulses that reflect off objects, with the echo's return time indicating distance <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. The [[doppler_effect_and_its_application_in_radar_technology | Doppler effect]] allows for velocity deductions: if an object moves towards the radar, the echoed wave's frequency increases, and the magnitude of this frequency shift indicates the object's speed <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

In this context, the time and frequency of the echo signal correspond to the position and velocity of the measured object, respectively <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This analogy closely mirrors the [[heisenberg_uncertainty_principle_and_its_relation_to_frequency_and_duration | Heisenberg uncertainty principle]] in quantum mechanics <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

A radar operator faces a dilemma:
*   **Precise Position, Ambiguous Velocity**: Sending a short, quick pulse confined to a small amount of time yields a more precise understanding of object distances <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. However, the Fourier transform of such a short pulse is necessarily more spread out in frequency <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. This means [[doppler_effect_and_its_application_in_radar_technology | Doppler-shifted]] echoes from objects with various velocities are more likely to overlap in frequency space, making it ambiguous to determine individual velocities <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
*   **Precise Velocity, Ambiguous Position**: To achieve a sharp, clean view of velocities, the echo signal needs to occupy a very small amount of frequency space <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. But for a signal to be concentrated in frequency space, it must necessarily be spread out in time <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. If the echo is spread out over a long period, echoes from multiple objects in the field can overlap, making their locations ambiguous <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

This illustrates the Fourier trade-off: crisp delineation for both position and velocity (or time and frequency) is impossible <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

## Connection to the Quantum Case

The general uncertainty principle, as observed in sound waves and radar, provides a foundation for understanding the [[heisenberg_uncertainty_principle_and_its_relation_to_frequency_and_duration | Heisenberg uncertainty principle]] in quantum mechanics. The core idea is that if particles behave as waves, then the same trade-off between concentration in space (position) and concentration in spatial frequency (momentum) applies <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. Unlike the radar case where waves measure an object, in quantum mechanics, "the particle *is* the wave" <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. Thus, the spread in position and momentum is fundamental to the particle's nature, not just an artifact of measurement <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. The German term for the [[heisenberg_uncertainty_principle_and_its_relation_to_frequency_and_duration | principle]], "unsharpness relation," better captures this fundamental Fourier trade-off at play <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.