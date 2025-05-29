---
title: Fourier transforms and their role in frequency analysis
videoId: MBnnXbOM5S4
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_fourier_transform | Fourier transform]] is a mathematical construct relevant for analyzing frequencies within a signal <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. It provides a way to view any signal not in terms of its intensity at each point in time, but rather in terms of the strength of various frequencies present within it <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## How the Fourier Transform Works

The main idea behind the [[introduction_to_fourier_transform | Fourier Transform]] involves "winding" a signal around a circle <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This is conceptualized by imagining a rotating vector whose length is determined by the height of the signal's graph at each point in time <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

When the "winding frequency" (the rate at which the graph is wound around the circle) matches the signal's dominant frequency, all the peaks of the signal align on one side of the circle and all the valleys on another, causing the "weight" of the graph to be off-center <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

The [[introduction_to_fourier_transform | Fourier Transform]] measures how well a signal correlates with a given pure frequency <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. The position of the center of mass of this wound-up graph encodes the strength of that frequency in the original signal <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

*   The distance between the center of mass and the origin captures the strength of that frequency <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   The angle of that center of mass off the horizontal corresponds to the phase of the given frequency <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

The output of the [[introduction_to_fourier_transform | Fourier Transform]] is a new function whose input is the winding frequency and whose output is the center of mass, often thought of as a complex number <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. A spike in the [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier Transform]]'s output at a specific frequency indicates that this is the dominant frequency of the signal <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. The spread around this spike indicates that pure sine waves near that dominant frequency also correlate well with the signal <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

## The Frequency-Duration Trade-off (Uncertainty Principle)

The relationship between how long a signal persists and how sharply its frequency content is defined is a key aspect of the general uncertainty principle, which applies to various wave phenomena beyond quantum mechanics <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This core idea involves the interplay between frequency and duration <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Intuitive Examples

*   **Flashing Turn Signals:** Observing flashing turn signals for a short time provides low confidence about their exact frequency, as they could fall out of sync later <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. A longer observation period increases confidence that their frequencies are the same <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This trade-off between observation duration and frequency certainty is an example of the general uncertainty principle <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Musical Note:** The shorter a musical note lasts, the less certain one can be about its exact frequency <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. A very short sound, like a clap or shockwave, has no discernible pitch <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Conversely, a more definite frequency requires a longer duration signal <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Fourier Transform Perspective

A short signal correlates highly with a wider range of frequencies, while a signal correlating strongly with only a narrow range of frequencies must last for a longer time <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

*   **Long-Duration Signal:** If a signal persists over a long period, when the winding frequency is even slightly different from its dominant frequency, the signal goes on long enough to wrap itself around the circle and balance out <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This results in a super sharp drop-off in the magnitude of the [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier Transform]] as the frequency shifts away from the dominant one, indicating a narrow, concentrated peak in the frequency domain <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Short-Duration Signal:** If a signal is localized to a short period of time, adjusting the winding frequency away from its dominant frequency means the signal doesn't have as much time to balance itself out around the circle <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This results in a much broader peak around the dominant frequency in the [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier Transform]] plot <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

In summary:
> A signal concentrated in time must have a spread out [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier Transform]], meaning it correlates with a wide range of frequencies <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Conversely, a signal with a concentrated [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier Transform]] (meaning a narrow range of frequencies) has to be spread out in time <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. This is the general uncertainty principle, a trade-off where one cannot have crisp delineation for both time and frequency <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

### Application in Doppler Radar

[[applications_of_fourier_transform | Applications of Fourier Transform]] extend to areas like Doppler radar <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. In radar, a radio wave pulse is sent out, and the time it takes for the echo to return helps deduce the distance of objects <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. The [[applications_of_fourier_transform | Doppler effect]] allows for deductions about the velocities of objects by analyzing the frequency shift of the echo <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. A higher frequency echo indicates an object moving towards the source <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

The [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier Transform]] of the original signal reveals its constituent frequencies <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. For a short pulse, its [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier Transform]] is necessarily spread out <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. The Doppler-shifted echo will have a similar [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier Transform]] plot, but shifted up in frequency <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. The size of this shift indicates the object's speed <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

In Doppler radar, the time of the echo signal corresponds to an object's position, and the frequency of the echo signal corresponds to its velocity <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This creates a dilemma:
*   **Precise Position:** To know the precise position of objects, a very quick, short pulse is needed <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. However, a short pulse's [[fourier_transforms_and_their_applications_in_integral_evaluation | Fourier Transform]] is necessarily more spread out <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. This means Doppler-shifted echoes from multiple objects, while separated in time, are more likely to overlap in frequency space, making velocity determination ambiguous <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
*   **Precise Velocity:** To get a clear view of velocities, an echo that occupies a very small amount of frequency space is needed <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. For a signal to be concentrated in frequency space, it necessarily has to be spread out in time <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This spread-out echo from multiple objects can overlap, making their distinct locations ambiguous <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

This demonstrates the inherent trade-off: the more certain one is about the positions of objects, the less certain one can be about their velocities, and vice-versa <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.