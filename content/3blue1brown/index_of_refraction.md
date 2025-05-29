---
title: Index of refraction
videoId: KTzGBJPuJwM
---

From: [[3blue1brown]] <br/> 

The index of refraction is a fundamental concept in physics that explains how light behaves when it enters different materials <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Defining the Index of Refraction

When light enters a medium, such as glass, its wave crests travel slower than they would in a vacuum <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The specific ratio between the speed of light in a vacuum (c) and its speed inside a medium is called the index of refraction for that medium <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

The term "refraction" is used because if a beam of light enters a medium at an angle, this slowdown causes the light to bend <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

> "The way my high school physics teacher always explained this was to imagine a tank going from some region where it can travel relatively quickly, like concrete, into something slower, like mud, where if it's coming in at an angle, then as one of its treads hits the slow region first, that tread will be going slower while the other one is faster, causing the whole thing to steer a little bit, until that second tread also enters the mud, then it continues straight, just travelling a little slower." <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>

The amount of bending is precisely defined by [[snells_law_and_light_refraction | Snell's law]] <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This law states that if you draw a line perpendicular to the boundary between the media and consider the angle between that perpendicular line and the light beam, the sine of this angle divided by the speed of the light is always a constant <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This means the slower the light, the lower that angle will be, allowing for calculation of the refraction <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## How Prisms Work

The phenomenon of [[how_prisms_work | prisms separating light into colors]] is directly linked to the index of refraction <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. The specific amount that light slows down (and thus the index of refraction) depends slightly on its frequency <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. For example, blue light, which has a higher frequency, slows down more aggressively than red light, which has a lower frequency <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

White light from the sun is a composite of many pure spectral colors, each corresponding to a clean sine wave <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. When white light enters a prism, these different frequency components are refracted by slightly different amounts, causing the iconic separation into rainbow colors <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## A Deeper [[physical_explanation_of_light_slowing_down | Explanation of Light Slowing Down]]

A more profound understanding of why light slows down and why this slowdown depends on color requires delving into the interaction of light with the material's constituent charges <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Phase Kick

Imagine a material, like glass, as a series of distinct layers perpendicular to the direction of light <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. When a light wave interacts with one of these layers, it causes a "kickback" to the phase of the wave <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

The phase of a wave is a constant added inside the sine function that effectively slides the wave left or right <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. A phase kick means that the function describing the wave after hitting the layer is almost the same, but with a small extra term added to its input <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

When light passes through many such layers, each applying its own phase kick, the cumulative effect is identical to the wave simply traveling slower, with its wavelength scrunched up while maintaining the same frequency <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. Thus, the question of "why does light slow down in glass" transforms into "why does its interaction with a single layer cause a kickback to the phase of the wave?" <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### Light's Interaction with Charges

Light is an electromagnetic wave, which can be visualized as ripples in the electric field <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. When a charged particle wiggles, it produces propagating ripples in the electric field traveling at the speed of causality, *c* <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. These ripples, when they reach another charged particle, cause it to wiggle, which in turn produces its own propagations <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. A layer of synchronously wiggling charges can produce a concentrated beam of light perpendicular to that plane <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

When a light beam enters a material like glass, it causes the charges (electrons, ions) within that material to wiggle in response <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. This wiggling produces its own "second-order" light wave at the same frequency <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. The overall electric field is the sum of the initial incoming light wave and this second-order wave <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

### Adding Waves and Phase Shift

To understand how these waves sum, it's helpful to represent each sine wave as the y-component of a rotating vector <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. The vector's length corresponds to the wave's amplitude, and its initial rotation corresponds to the wave's phase <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. When two waves of the same frequency are added, their sum can be found by adding their corresponding vectors tip-to-tail <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

Crucially, if the phase of the second wave (from the wiggling charges) is exactly 90 degrees (a quarter cycle) behind the phase of the first (incoming light), and if the second wave is very small compared to the first, then the resulting wave is almost identical to the initial wave but shifted back in phase by a tiny bit <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. The size of this phase shift depends on the amplitude of the second wave <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

### Resonant Frequency and Color Dependence

The key to understanding why the index of refraction depends on color lies in how much those charges wiggle in response to the incoming light wave <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. Charges in a material can be modeled as bound to equilibrium positions by springs, behaving as simple harmonic oscillators <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. These oscillators have a [[physical_explanation_of_light_slowing_down | resonant frequency]] (ω_r), determined by the "spring constant" (k) and mass (m) of the charge (specifically, the square root of k divided by m) <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

When a light wave (an external oscillating force) acts on these charges, it's a "driven harmonic oscillator" <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. The amplitude of the charge's oscillation (how much it wiggles) is inversely related to the difference between the square of the material's resonant frequency and the square of the light's frequency (ω_L) <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.

If the light's frequency (ω_L) is very close to the material's resonant frequency (ω_r), the oscillations of the particle will grow significantly, leading to a large amplitude <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>. Conversely, if the light's frequency is much smaller or larger than the resonant frequency, the amplitude of oscillation will be more modest <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.

This means that the size of the charge's wiggle depends on the frequency (color) of the light <a class="yt-timestamp" data-t="00:26:14">[00:26:14]</a>. The more the charges wiggle, the stronger the second-order wave they produce, leading to a larger phase shift in the overall light wave <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>. Since many phase shifts cause the apparent slowdown of light, the amount of slowdown (and thus the index of refraction) ultimately depends on the light's frequency <a class="yt-timestamp" data-t="00:26:39">[00:26:39]</a>. This is the fundamental reason why [[how_prisms_work | prisms]] work <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.

### Further Considerations

While this model provides a robust explanation, some details are simplified. For instance, a more complete model of the harmonic oscillator would include a "drag force" term dependent on the charge's velocity <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a>. This term accounts for the absorption of light energy by the material, explaining why some materials are opaque rather than transparent <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.

Other complex phenomena related to the index of refraction include:
*   **Index of refraction less than one**: This can occur and seems to imply light traveling faster than *c*, but it does not violate the principle that information cannot travel faster than *c* <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Birefringence**: Some materials can have two different indices of refraction, causing a double image when viewed through them <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.