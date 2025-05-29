---
title: Complex numbers and Fourier Transform
videoId: spUNpyF58BY
---

From: [[3blue1brown]] <br/> 

The [[introduction_to_fourier_transform | Fourier transform]] is a super important mathematical idea primarily used for decomposing frequencies from signals, such as sound <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Initially, one might consider a simpler approach, an "almost Fourier transform," which involves wrapping a signal's intensity-vs-time graph around a circle and tracking the x-coordinate of its center of mass <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This process creates a plot showing spikes at frequencies present in the original signal <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. However, this only tells half the story <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

## The Role of Complex Numbers

When dealing with a two-dimensional entity like the center of mass of the wound-up graph, it is elegant and typical in [[complex_numbers_in_mathematics | mathematics]] to think of it in the [[complex_numbers_in_mathematics | complex plane]] <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. This means the center of mass is a [[complex_numbers_in_mathematics | complex number]] with both a real and an imaginary part <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

[[complex_numbers_in_mathematics | Complex numbers]] are particularly well-suited for describing things involving winding and rotation <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

### Euler's Formula and Rotation
[[complex_numbers_and_imaginary_exponents | Euler's formula]] (e to the `i` times a number) describes a point on a unit circle, reached by walking that number of units counter-clockwise starting from the right <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

To describe rotation at a specific rate, for example, 1 cycle per second, one can use the expression:
$$ e^{2\pi i t} $$
where `t` is the time passed <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. To represent different frequencies `f`, the time `t` in the exponent is multiplied by `f` <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. In the context of [[introduction_to_fourier_transform | Fourier transforms]], the convention is to think about clockwise rotation, which means adding a negative sign into the exponent <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>:
$$ e^{-2\pi i f t} $$

## Building the Fourier Transform Formula

To describe the winding of a graph, a signal intensity vs. time function `g(t)` (like a cosine wave) is multiplied by the exponential expression <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. This multiplication means the rotating [[complex_numbers_in_mathematics | complex number]] is scaled up or down according to the value of `g(t)`, effectively drawing the wound-up graph <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

The next step is to track the center of mass of this wound-up graph <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. This can be approximated by sampling many points from the original signal, finding where they end up on the wound-up graph, and then taking the average of these complex numbers <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

### The Integral Component
In the limit of sampling more points closer together, this average becomes an integral of the function divided by the size of the time interval being observed <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. The integral of a [[complex_numbers_in_mathematics | complex-valued function]] can be interpreted as the center of mass of the wound-up graph <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.

## The Actual Fourier Transform

The "actual" [[introduction_to_fourier_transform | Fourier transform]] differs from the "almost Fourier transform" by not dividing by the time interval <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. It is simply the integral part of this expression <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. This means the result is scaled up by the duration of the original graph segment <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

This scaling has the physical effect that if a certain frequency persists for a long time, the magnitude of the [[introduction_to_fourier_transform | Fourier transform]] at that frequency is scaled up proportionally <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.

The [[introduction_to_fourier_transform | Fourier transform]] of an intensity vs. time function, `g(t)`, results in a new function, commonly denoted as `g-hat` ($\hat{g}$), which takes a frequency `f` (the winding frequency) as input <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. The output of this function is a [[complex_numbers_in_mathematics | complex number]], representing a point in the 2D plane that corresponds to the strength of a given frequency in the original signal <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. While a plot of the [[introduction_to_fourier_transform | Fourier transform]] might show only the real component (x-coordinate), the imaginary component can also be graphed for a fuller description <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.

The formula for the [[introduction_to_fourier_transform | Fourier transform]] is:
$$ \hat{g}(f) = \int g(t) e^{-2\pi i f t} dt $$
Understanding how [[complex_numbers_and_imaginary_exponents | exponentials correspond to rotation]], how multiplying by `g(t)` draws a wound-up graph, and how an integral of a [[complex_numbers_in_mathematics | complex-valued function]] relates to a center of mass, reveals the rich intuitive meaning behind this seemingly daunting formula <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

In theory, the integral bounds for the [[introduction_to_fourier_transform | Fourier transform]] are often from negative infinity to infinity, considering the limit as the time interval grows <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.

The [[introduction_to_fourier_transform | Fourier transform]] extends to many areas beyond just extracting frequencies from signals <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>, demonstrating its wide [[mathematical_principles_of_fourier_transform | application]].