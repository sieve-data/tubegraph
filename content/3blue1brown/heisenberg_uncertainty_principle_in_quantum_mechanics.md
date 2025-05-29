---
title: Heisenberg uncertainty principle in quantum mechanics
videoId: MBnnXbOM5S4
---

From: [[3blue1brown]] <br/> 

The Heisenberg Uncertainty Principle, a cornerstone of [[Quantum mechanics basics for beginners | quantum mechanics]], states that the more precisely one knows a particle's position, the less certain one can be of its momentum, and vice versa <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This concept, while often perceived as strange or unique to the quantum realm, is actually a specific instance of a more general trade-off observed in various wave phenomena <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The General Uncertainty Trade-off

The core idea behind the uncertainty principle lies in the interplay between frequency and duration <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This trade-off can be understood intuitively with everyday examples involving waves:

*   **Turn Signals**: If two car turn signals flash in sync for a few seconds, they might appear to have the same frequency. However, over a longer duration, they might fall out of sync, revealing different frequencies <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. A short observation yields low confidence in their exact frequencies, whereas a longer observation provides greater certainty <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Musical Notes**: A shorter musical note makes it less certain to determine its exact frequency <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. For instance, it's impossible to determine the pitch of a clap or shockwave <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Conversely, a more definite frequency requires a longer signal duration <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

More accurately, a short signal correlates highly with a wider range of frequencies, while a signal correlating strongly with only a narrow range of frequencies must last for a longer time <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This is the essence of the general uncertainty principle <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### The Role of Fourier Transform

The [[General uncertainty trade off and its applications to sound waves | Fourier Transform]] is a crucial mathematical construct for analyzing frequencies <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. It allows viewing a signal not by its intensity over time, but by the strength of various frequencies within it <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

The process involves "winding" a signal around a circle, where a rotating vector's length is determined by the signal's height over time <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. When the "winding frequency" matches the signal's dominant frequency, the signal's peaks align on one side of the circle and valleys on the other, causing the "center of mass" of the wound-up graph to be off-center <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. The position of this center of mass encodes the strength and phase of that frequency in the original signal <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

The Fourier transform output is a function whose input is the winding frequency and whose output is this center of mass (as a complex number) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. A sharp spike in the Fourier transform indicates a dominant frequency, while a spread around that frequency indicates that nearby pure sine waves also correlate well with the signal <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

The key to the uncertainty principle lies in how this spread changes with signal duration:
*   **Long Duration Signal**: If a signal persists for a long time, even a slight difference in winding frequency from the dominant frequency causes the signal to balance out around the circle. This results in a super sharp drop-off in the Fourier transform's magnitude, indicating a very narrow range of frequencies <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Short Duration Signal**: If a signal is localized to a short period, it doesn't have enough time to balance out when the winding frequency is adjusted. This means the winding frequency must be significantly different from the dominant frequency for the signal to balance out again. On the frequency plot, this corresponds to a much broader peak <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

In summary, a signal concentrated in time necessarily has a spread-out Fourier transform (correlates with a wide range of frequencies), and a signal with a concentrated Fourier transform must be spread out in time <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. This is the general uncertainty principle phrased mathematically.

## Doppler Radar Analogy

Doppler radar provides a tangible example of this trade-off. Radar works by sending out radio wave pulses, and the time it takes for an echo to return indicates the object's distance <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. The Doppler effect allows deduction of an object's velocity: a reflected pulse from an object moving towards the source will have a slightly higher frequency <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

The Fourier transform of the original signal reveals its constituent frequencies, and the Doppler-shifted echo's Fourier transform will show a similar plot shifted to a higher frequency <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. The size of this frequency shift allows deduction of the object's speed <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

Crucially, in this context, the time of the echo signal corresponds to the object's position, and the frequency of the echo signal corresponds to its velocity <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This makes Doppler radar closely analogous to the [[Quantum mechanics basics for beginners | Heisenberg Uncertainty Principle]] <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

A radar operator faces a dilemma:
*   **Precise Position**: To precisely determine the distance of multiple objects, a very quick, short pulse is needed <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. However, the Fourier transform of a quick pulse is necessarily more spread out in frequency <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. This means Doppler-shifted echoes from multiple objects, despite being separated in time, are more likely to overlap in frequency space, making individual velocities ambiguous <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
*   **Precise Velocity**: To get a sharp view of velocities, an echo occupying a very small amount of frequency space is required <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. But a signal concentrated in frequency space must be spread out in time <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This leads to echoes overlapping in time, making the positions of multiple objects extremely ambiguous <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

This is the Fourier trade-off: one cannot have crisp delineation for both position (time) and velocity (frequency) <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

## The Quantum Case

The [[Quantum mechanics basics for beginners | Heisenberg Uncertainty Principle]] in [[Quantum mechanics basics for beginners | quantum mechanics]] extends this Fourier trade-off to particles. [[Waveparticle duality and de Broglie hypothesis | Louis de Broglie]], drawing from his experiences with radio waves, proposed in his 1924 PhD thesis that all matter has wave-like properties <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. He concluded that the momentum of any moving particle is proportional to the spatial frequency of its corresponding wave (how many times the wave cycles per unit distance) <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

De Broglie's reasoning for this connection between momentum and spatial frequency involved a crude comparison:
*   Imagine many weights oscillating in sync on springs, with most mass concentrated at a single point <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. This represents the energy of a particle (like E=mc²) <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
*   Due to [[applications_of_quaternions_in_threedimensional_rotations_and_quantum_mechanics | special relativity]], if this setup is viewed while moving relative to it, the weights will appear to fall out of phase <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. Events considered simultaneous in one reference frame may not be in another <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   This relativistic Doppler effect implies that if mass is energy (via E=mc²) and energy is carried as an oscillating phenomenon (like photons), then changes in how that mass moves correspond to changes in the spatial frequency of its associated wave <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

Therefore, if a particle is described as a wave packet in space, its momentum is represented by the spatial frequency, which is proportional to the Fourier transform of the spatial wave <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   If a particle's wave is very concentrated around a single point (meaning its position is certain), its Fourier transform (and thus its momentum wave) must necessarily be more spread out <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   Conversely, if the momentum wave is concentrated (momentum is certain), the spatial wave must be spread out (position is uncertain) <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

### Unsharpness, Not Unknowability

Unlike the Doppler radar case where the ambiguity arose from measuring an object with definite properties using waves, in [[Quantum mechanics basics for beginners | quantum mechanics]], "the particle *is* the wave" <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. The spread in position and momentum is not an artifact of imperfect measurement but is fundamental to the nature of the particle itself, similar to how a musical note's spread over time is fundamental to its identity <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

Many mainstream references misinterpret the Heisenberg Uncertainty Principle as a statement about "unknowability" or the universe's indeterminacy <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. However, it is fundamentally a Fourier trade-off: a statement about how concentrated a wave and its frequency representation can be, applied to the premise that matter is a wave <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

The "randomness" and "unknowability" enter at a deeper level of [[Quantum mechanics basics for beginners | quantum mechanics]] interpretation:
*   When particles are measured (e.g., detecting their position), the outcome appears probabilistic <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
*   The probability of finding a particle in a given region is proportional to the strength of its wave in that region <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
*   A wave concentrated near a point means a higher probability of finding the particle there (greater certainty of location) <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
*   Because this concentration implies a more spread-out Fourier transform, the wave describing its momentum would also be spread out. This means one cannot find a narrow range of momenta with a high probability of the particle occupying it <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.

The German word for this principle, "Unschärferelation," might be more accurately translated as the "unsharpness relation," which better captures the underlying Fourier trade-off without implying unknowability <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. The true fascination of the [[Quantum mechanics basics for beginners | Heisenberg Uncertainty Principle]] lies in the realization that position and momentum share the same relationship as sound and frequency, as if a particle's momentum is the "sheet music" describing its movement through space <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.