---
title: Complex plane and winding frequency
videoId: spUNpyF58BY
---

From: [[3blue1brown]] <br/> 
## Complex Plane and Winding Frequency

The core concept of the Fourier transform involves an "animated approach" to thinking about signals by wrapping them around a circle <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This process introduces the idea of a "winding frequency" <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.

### Winding a Signal Graph

To understand the Fourier transform, a signal (e.g., air pressure over time for sound <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>) is visualized by taking its graph and "wrapping it up around a circle" <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

This is concretely imagined by:
*   **Rotating Vector**: A small rotating vector whose length at any point in time is equal to the height of the signal graph for that time <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. High points on the graph correspond to a greater distance from the origin, while low points are closer to the origin <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
*   **Winding Frequency**: There are two distinct frequencies at play: the frequency of the signal itself (how many times it goes up and down per second) and the "winding frequency" with which the graph is wrapped around the circle (how many rotations per second) <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. This winding frequency can be adjusted, determining the shape of the wound-up graph <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

### Center of Mass and Frequency Detection

A key insight arises when the winding frequency matches the signal's frequency <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. For example, if a signal has 3 beats per second, and it's wound at 3 cycles per second, all high points of the graph will align on one side of the circle (e.g., the right), and all low points on the opposite side (e.g., the left) <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

To quantify this, the concept of the "center of mass" of the wound-up graph is introduced <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
*   For most winding frequencies, the peaks and valleys are spaced out, causing the center of mass to remain close to the origin <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.
*   When the winding frequency aligns with the signal's frequency, the center of mass is unusually far from the origin, creating a "spike" in its position (e.g., to the right) <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.
*   Tracking the x-coordinate of this center of mass as the winding frequency changes reveals these spikes, indicating the presence of specific frequencies in the original signal <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.

### The [[complex_plane_and_exponential_functions | Complex Plane]] and Fourier Transform

To fully capture the two-dimensional nature of the center of mass of the wound-up graph, it is elegant to think of it as existing in the [[complex_numbers_and_2d_plane_transformations | complex plane]] <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>. The center of mass then becomes a [[complex_numbers_and_2d_plane_transformations | complex number]] with both a real (x-coordinate) and an imaginary (y-coordinate) part <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>.

[[complex_numbers_and_2d_plane_transformations | Complex numbers]] are particularly well-suited for describing winding and rotation <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>.
*   **Euler's Formula**: [[complex_plane_and_exponential_functions | Euler's formula]] ($e^{i\theta} = \cos\theta + i\sin\theta$) states that $e$ raised to some number times $i$ lands on a point obtained by walking that number of units around a unit circle counterclockwise from the right <a class="yt-timestamp" data-t="12:32:00">[12:32:00]</a>.
*   **Rotating Vector Representation**: To describe rotation at a specific rate, for example, 1 cycle per second, one can use the expression $e^{2\pi i t}$ (where `t` is time) <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>. To represent a winding frequency `f`, this becomes $e^{2\pi i f t}$ <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.
*   **Clockwise Convention**: In the context of Fourier transforms, the convention is to think about rotating in the clockwise direction, which introduces a negative sign in the exponent: $e^{-2\pi i f t}$ <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>.

### Formalizing the Winding Machine

The process of winding the graph is elegantly encapsulated by multiplying the signal function, `g(t)` (describing intensity vs. time), by the complex exponential: $g(t) \cdot e^{-2\pi i f t}$ <a class="yt-timestamp" data-t="14:04:00">[14:04:00]</a>. This means the rotating complex number is scaled by the signal's value, effectively drawing the wound-up graph <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>.

To track the center of mass of this wound-up graph, one would conceptually average the complex numbers representing points on the graph <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>. In the limit of continuous sampling, this average becomes an integral <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>:

$$ \frac{1}{T} \int g(t) \cdot e^{-2\pi i f t} dt $$
Where `T` is the size of the time interval <a class="yt-timestamp" data-t="15:21:00">[15:21:00]</a>. This entire expression represents the center of mass of the wound-up graph <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.

The actual Fourier transform, denoted as $\hat{g}(f)$, is defined by omitting the division by the time interval `T`:

$$ \hat{g}(f) = \int g(t) \cdot e^{-2\pi i f t} dt $$
This means the Fourier transform is essentially the center of mass scaled up by the duration of the signal <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>. A longer-persisting frequency results in a larger magnitude for the Fourier transform at that frequency <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>.

The output of the Fourier transform is a complex number, corresponding to a point in the 2D [[complex_numbers_and_2d_plane_transformations | complex plane]], which indicates the "strength" of a given frequency in the original signal <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>. While visualizations often plot only the real (x-coordinate) component, the imaginary (y-coordinate) component also provides a fuller description <a class="yt-timestamp" data-t="17:46:00">[17:46:00]</a>.

The integral bounds are typically from negative infinity to infinity in theoretical contexts, considering the limit as the time interval grows <a class="yt-timestamp" data-t="18:36:00">[18:36:00]</a>.