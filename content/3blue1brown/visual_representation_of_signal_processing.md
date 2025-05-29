---
title: Visual representation of signal processing
videoId: spUNpyF58BY
---

From: [[3blue1brown]] <br/> 

The **Fourier transform** is an animated approach to understanding a crucial mathematical idea related to signal processing <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This concept allows for the decomposition of frequencies from sound signals <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Its utility extends beyond sound and frequency, appearing in various areas of mathematics and physics <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Decomposing Frequencies from Sound

Sound, such as a pure A note at 440 beats per second, causes air pressure to oscillate in a wave <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. When multiple notes are played simultaneously, the resulting pressure vs. time graph is a sum of the individual waves, leading to a more complicated, non-pure sine wave <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. A microphone records only this final sum of air pressure over time <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. The central challenge is to decompose such a signal back into its constituent pure frequencies <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>, which is likened to "unmixing multiple paint colors" <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

The strategy involves building a "mathematical machine" that treats signals with specific frequencies differently from others <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## The Winding Machine Concept

### Wrapping the Graph Around a Circle

To analyze a signal, such as a pure signal with 3 beats per second over a finite interval (e.g., 0 to 4.5 seconds) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>, the key idea is to "wrap it up around a circle" <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This is done by imagining a rotating vector whose length at any given time is equal to the height of the signal's graph at that time <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. High points on the graph correspond to a greater distance from the origin, while low points are closer <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

There are two frequencies at play:
1.  **Signal frequency**: How often the signal goes up and down (e.g., 3 times per second) <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
2.  **Winding frequency**: The rate at which the graph is wrapped around the circle (e.g., half a rotation per second) <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This winding frequency can be adjusted <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, and it determines the appearance of the wound-up graph <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

When the winding frequency matches the signal's frequency (e.g., 3 beats per second), a special alignment occurs: all high points of the graph appear on one side of the circle (e.g., the right), and all low points appear on the opposite side (e.g., the left) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Tracking the Center of Mass

To leverage this alignment, one can imagine the wound-up graph as a metal wire with mass and track its **center of mass** <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.
*   For most winding frequencies, peaks and valleys are spread out, keeping the center of mass close to the origin <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   However, when the winding frequency equals the signal's frequency, the peaks align, causing the center of mass to be unusually far from the origin in a specific direction (e.g., to the right) <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

By plotting the x-coordinate of this center of mass against different winding frequencies, a peak or "spike" appears at the signal's frequency <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a> <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. A spike around zero frequency in this plot indicates that the original cosine wave was shifted up <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### The "Almost Fourier Transform"

This plot of winding frequency vs. center of mass (specifically its x-coordinate) is referred to as the "almost Fourier transform" <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. This "machine" effectively picks out the frequency of a signal <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

A crucial property of this machine is its **linearity**: if you take two signals, apply the almost Fourier transform to each individually, and then add the results, you get the same outcome as if you first added the signals and then applied the transform <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. Since the transform of a pure frequency is near zero everywhere except for a spike at that frequency, adding two pure frequencies results in a transform graph with peaks above each of those input frequencies <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This allows the machine to "unmix the mixed bucket of paint" by pulling out original frequencies from jumbled sums <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

### Application: Sound Editing

This concept is highly useful in practical applications like sound editing <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. For example, to filter out an annoying high pitch from a recording:
1.  The signal, initially represented as varying intensities over time, is transformed into frequencies <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
2.  Applying the Fourier transform reveals the annoying high pitch as a distinct spike at a high frequency <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
3.  Filtering it out involves "smushing the spike down" <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
4.  An **inverse Fourier transform** can then convert this modified frequency representation back into a time-based signal, producing the sound without the unwanted frequency <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Applying the Fourier transform to the Fourier transform returns something close to the original function <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

## The Full Fourier Transform

### Complex Numbers and Euler's Formula

The "almost Fourier transform" only considers the x-coordinate of the center of mass <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. Since the wound-up graph exists in two dimensions, it also has a y-coordinate <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. In mathematics, it is often more elegant to represent two-dimensional concepts using the **complex plane** <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. The center of mass then becomes a complex number with both a real (x) and an imaginary (y) part <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

Complex numbers are particularly suitable for describing rotation and winding <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. **Euler's formula** (e.g., $e^{i\theta}$) famously describes points on a unit circle when walking a certain number of units counterclockwise <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. To describe rotation at a specific rate (e.g., 1 cycle per second), the expression $e^{2\pi i t}$ is used, where $t$ is time <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. For a different frequency $f$, the expression becomes $e^{2\pi i f t}$ <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

For the Fourier transform, the convention is to think of rotation in the clockwise direction, so a negative sign is added to the exponent: $e^{-2\pi i f t}$ <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

### The Fourier Transform Formula

When this exponential expression is multiplied by the signal intensity function, $g(t)$, (i.e., $g(t) \cdot e^{-2\pi i f t}$), it means the rotating complex number's length is scaled by the signal's value <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This combined expression elegantly encapsulates the idea of winding a graph around a circle with a variable frequency $f$ <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

To track the center of mass of this wound-up graph, one would traditionally sample many points, find where they land on the wound-up graph, and then average them (summing as complex numbers and dividing by the number of points) <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. In the limit, as more points are sampled closer together, this sum becomes an **integral** <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

The **actual Fourier transform** differs from the "almost Fourier transform" by *not* dividing by the time interval <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. It is simply the integral part of this expression <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. This means the result is the center of mass scaled up by the duration of the original graph <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. This scaling has the effect that if a certain frequency persists for a long time, the magnitude of the Fourier transform at that frequency is proportionally scaled up <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.

The Fourier transform of an intensity vs. time function, $g(t)$, is a new function, commonly denoted as $\hat{g}(f)$ (g-hat) <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. This new function takes a frequency $f$ as input <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a> and outputs a complex number <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>, representing the strength of that frequency in the original signal <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>. The visual plot of the Fourier transform typically shows only the real component (x-coordinate) of this complex output <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.

### Final Formula and Intuitive Meaning

The full formula for the Fourier transform is:

```
F(f) = ∫ g(t) * e^(-2πi f t) dt
```
Where:
*   $g(t)$ is the original signal (intensity vs. time).
*   $f$ is the winding frequency.
*   $t$ is time.
*   $e^{-2\pi i f t}$ represents the complex number that rotates clockwise.
*   The integral (∫) over time represents summing up scaled rotating vectors to find their total displacement, or "center of mass" <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

Although this formula may appear daunting out of context <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>, its components correspond to:
*   Exponentials relating to rotation <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.
*   Multiplication by $g(t)$ drawing a wound-up version of the graph <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   The integral of a complex-valued function being interpreted as a center of mass <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

In practice, for applications like sound editing, the integral is calculated over a finite time interval <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. However, the theoretical definition often uses bounds from negative infinity to infinity, considering the limit as the time interval grows <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.

The Fourier transform extends to many areas of mathematics beyond just extracting frequencies from signals, such as [[visualizing mathematical operations using vector fields | visualizing mathematical operations using vector fields]] or [[visualizing mathematical concepts | visualizing mathematical concepts]] more broadly <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>.