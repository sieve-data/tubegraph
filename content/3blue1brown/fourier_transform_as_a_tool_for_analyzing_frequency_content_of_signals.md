---
title: Fourier transform as a tool for analyzing frequency content of signals
videoId: MBnnXbOM5S4
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_fourier_transform | Fourier Transform]] is a mathematical construct primarily used for analyzing the frequency content of signals <a class="yt-timestamp" data-t="02:32">[02:32]</a>, allowing a signal to be viewed not by its intensity over time, but by the strength of its various frequencies <a class="yt-timestamp" data-t="02:55">[02:55]</a>.

## How the Fourier Transform Works

The core idea behind the [[introduction_to_fourier_transform | Fourier Transform]] involves winding a signal around a circle <a class="yt-timestamp" data-t="03:05">[03:05]</a>. This is visualized by imagining a rotating vector whose length is determined by the height of the signal's graph at each point in time <a class="yt-timestamp" data-t="03:10">[03:10]</a>. The frequency at which the graph is wound around the circle is the "winding frequency" <a class="yt-timestamp" data-t="03:22">[03:22]</a>.

For most winding frequencies, the signal's values tend to average out over the circle <a class="yt-timestamp" data-t="03:27">[03:27]</a>. However, when the winding frequency matches the signal's dominant frequency (e.g., 5 cycles per second), the peaks of the signal align on one side of the circle and the valleys on the opposite side, causing the "weight" of the graph to be off-center <a class="yt-timestamp" data-t="03:42">[03:42]</a>.

The [[introduction_to_fourier_transform | Fourier Transform]] measures how well a signal correlates with a given pure frequency <a class="yt-timestamp" data-t="04:31">[04:31]</a>. It does this by tracking the center of mass of the wound-up graph for each winding frequency <a class="yt-timestamp" data-t="04:02">[04:02]</a>.

The output of the [[introduction_to_fourier_transform | Fourier Transform]] is a new function <a class="yt-timestamp" data-t="04:42">[04:42]</a>:
*   Its input is the winding frequency <a class="yt-timestamp" data-t="04:42">[04:42]</a>.
*   Its output is the center of mass, thought of as a [[complex_numbers_and_fourier_transform | complex number]] <a class="yt-timestamp" data-t="04:46">[04:46]</a>.
    *   The distance between the center of mass and the origin captures the *strength* or *magnitude* of that frequency in the original signal <a class="yt-timestamp" data-t="04:16">[04:16]</a>.
    *   The angle of that center of mass off the horizontal corresponds to the *phase* of the given frequency <a class="yt-timestamp" data-t="04:24">[04:24]</a>.

When the [[introduction_to_fourier_transform | Fourier Transform]] is plotted, a spike above a particular winding frequency (e.g., 5 beats per second) indicates that this is the dominant frequency of the signal <a class="yt-timestamp" data-t="05:16">[05:16]</a>. If the spike is spread out around that dominant frequency, it indicates that pure sine waves near that frequency also correlate well with the signal <a class="yt-timestamp" data-t="05:26">[05:26]</a>.

## Fourier Transform and Signal Duration

The [[introduction_to_fourier_transform | Fourier Transform]] illustrates a trade-off between a signal's duration and the certainty of its frequency content:
*   **Long-duration signals**: If a signal persists over a long period, even a slight difference in winding frequency from the signal's actual frequency will cause the signal to balance itself out when wound around the circle <a class="yt-timestamp" data-t="05:58">[05:58]</a>. This results in a "super sharp drop-off" in the magnitude of the [[introduction_to_fourier_transform | Fourier Transform]] as the frequency shifts away from the dominant one, indicating a very narrow and certain frequency <a class="yt-timestamp" data-t="06:09">[06:09]</a>.
*   **Short-duration signals**: If a signal is localized to a short period of time, it does not have enough time to balance itself out around the circle when the winding frequency is adjusted slightly <a class="yt-timestamp" data-t="06:26">[06:26]</a>. This leads to a much broader peak in the frequency plot, meaning the signal correlates highly with a wider range of frequencies <a class="yt-timestamp" data-t="06:42">[06:42]</a>.

This relationship demonstrates a general uncertainty principle:
> "A signal concentrated in time must have a spread out [[introduction_to_fourier_transform | Fourier Transform]], meaning it correlates with a wide range of frequencies, and a signal with a concentrated [[introduction_to_fourier_transform | Fourier Transform]] has to be spread out in time." <a class="yt-timestamp" data-t="06:51">[06:51]</a>

This concept applies to various wave phenomena, including:
*   **Musical Notes**: A shorter note makes its exact frequency less certain, while a more definite frequency requires a longer duration signal <a class="yt-timestamp" data-t="01:51">[01:51]</a>. For instance, the pitch of a clap or shockwave cannot be determined, even by someone with perfect pitch <a class="yt-timestamp" data-t="01:57">[01:57]</a>.
*   **Doppler Radar**: In radar, a long pulse allows for a more precise determination of an object's velocity (due to a concentrated frequency representation via the Doppler effect), but it makes the object's position ambiguous <a class="yt-timestamp" data-t="09:02">[09:02]</a>. Conversely, a short pulse gives precise position but results in a spread-out frequency representation, making velocity determination ambiguous <a class="yt-timestamp" data-t="09:24">[09:24]</a>. This analogy is close to the quantum mechanical [[Heisenberg uncertainty principle|Heisenberg uncertainty principle]] <a class="yt-timestamp" data-t="08:37">[08:37]</a>.