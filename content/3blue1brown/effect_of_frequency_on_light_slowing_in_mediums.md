---
title: Effect of frequency on light slowing in mediums
videoId: KTzGBJPuJwM
---

From: [[3blue1brown]] <br/> 

The phenomenon of light slowing down in a medium, particularly how it affects different colors (frequencies) of light, is central to understanding how prisms work <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While widely recognized, the standard explanation often lacks the depth needed for a complete understanding <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Standard Explanation of Light Refraction

In a typical high school physics class, the explanation for light's behavior in a medium like glass goes as follows:
*   When light enters a medium, its wave crests slow down compared to their speed in a vacuum (c) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   The ratio between the speed of light in a vacuum and its speed inside a medium is called the [[light_refraction_and_the_refractive_index|index of refraction]] for that medium <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   If a beam of light enters glass at an angle, this slowdown causes it to bend, or refract <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This bending can be visualized with an analogy of a tank moving from concrete into mud at an angle <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   Snell's law quantifies this bending, stating that the sine of the angle of incidence divided by the speed of light is constant, meaning slower light bends more <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Frequency Dependence and Prisms
The key to understanding prisms within this standard view is that the specific amount light slows down depends on its frequency <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. For instance, blue light (higher frequency) slows down more aggressively than red light (lower frequency) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Since white light is a continuous spectrum of colors (a sum of many pure sine waves), each component refracts by a slightly different amount, leading to the iconic separation of colors <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

While this explanation is not incorrect, it presents these facts—why light slows down, and why the slowdown depends on color—as given, rather than derived <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

## A Deeper Explanation: Feynman's Approach

A more satisfying explanation, inspired by [[Feynmans explanation of light phenomena|Feynman's lectures]], delves into the interactions between light and individual charges within the material <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### The "Phase Kick" Concept
Instead of directly asking why light slows down, a better question is why its interaction with a single layer of glass causes a "kickback" to the phase of the wave <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

Waves have properties like amplitude, angular frequency/wavenumber, and phase <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. A "phase kickback" means a small constant is added to the input of the sine function describing the wave, effectively sliding the wave left or right <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. When a light wave passes through many such infinitesimal layers, each applying a tiny phase kick, the cumulative effect is identical to the wave simply traveling slower, with its wavelength "scrunched up," while maintaining the same frequency <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Light and Interacting Charges
Light is a wave in the electromagnetic field, where oscillating charged particles produce propagating ripples (light) traveling at the speed of causality, c <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. These ripples, upon reaching other charged particles, cause them to wiggle, which in turn generates their own propagations <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. The net effect of multiple oscillating charges is the sum of their individual effects <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. A plane of charges wiggling in sync can produce a concentrated beam of light perpendicular to that plane <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

When a light beam enters a material like glass, it causes the charges (electrons, ions) within the material to wiggle in response <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. This wiggling produces its own "second-order" light wave at the same frequency, propagating in both directions <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. The overall electric field is the sum of the initial incoming wave and this second-order wave <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

#### Adding Waves with Rotating Vectors
Adding two sine waves with the same frequency can be visualized by representing each wave as the y-component of a rotating vector <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. The amplitude corresponds to the vector's length, and the phase corresponds to its initial angle <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. The sum of the two waves is represented by the vector sum of these rotating vectors <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

Crucially, if the second wave's phase is exactly 90 degrees behind the first wave's phase, and if the second wave is much smaller than the first, their sum results in a wave that is almost identical to the initial wave but is shifted back in phase by a tiny bit <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. The size of this phase shift depends on the amplitude of the second wave <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. In the case of light interacting with a material, the second-order wave produced by the wiggling charges is indeed a quarter cycle behind the incoming light wave, leading to this phase shift <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

### The Driven Harmonic Oscillator

To understand why the [[light_refraction_and_the_refractive_index|index of refraction]] depends on color (frequency), we must determine how much the charges wiggle in response to the incoming light wave <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.

*   **Modeling Charges**: Each charged particle in the material can be modeled as if it's bound to an equilibrium position by a spring, exhibiting a linear restoring force <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.
*   **Resonant Frequency**: Such an oscillator, if disturbed, will naturally oscillate at a specific angular frequency, called its resonant frequency (ωr), determined by the "spring constant" (k) and the mass (m) of the particle (ωr = sqrt(k/m)) <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>. Stronger springs or lighter masses lead to faster oscillations <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.
*   **External Driving Force**: The incoming light wave acts as an external, oscillating force on these charges <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. The frequency of this force (ωl, the light's angular frequency) is generally distinct from the material's resonant frequency <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.
*   **Amplitude Dependence on Frequency**: In the steady state, the charges will oscillate at the same frequency as the incoming light, but the amplitude of their oscillation depends on the difference between the light's frequency (ωl) and the resonant frequency (ωr) of the material's charges <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>. The amplitude of oscillation is inversely proportional to the difference between the square of the resonant frequency and the square of the light frequency <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
    *   If ωl is very close to ωr, the oscillations grow very large, a phenomenon known as resonance <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>.
    *   If ωl is much smaller or much larger than ωr, the amplitude of oscillation is significantly more modest <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.

Therefore, the larger the difference between the light's frequency and the material's resonant frequency, the smaller the oscillation of the charge <a class="yt-timestamp" data-t="00:25:44">[00:25:44]</a>.

## Conclusion

The amount of wiggling of the charges dictates the strength of the second-order wave they produce <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>. A stronger second-order wave causes a larger phase shift to the overall light wave <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>. Since a series of phase shifts is what makes light appear to slow down, this means that the amount light slows down ultimately depends on its frequency (color) <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>. This comprehensive explanation of the driven harmonic oscillator is the true reason why prisms separate light by color <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.

### Further Considerations
While this explanation provides a solid foundation, some details are omitted, such as the inclusion of a "drag force" term depending on the charge's velocity. This term is crucial for explaining why some materials absorb light instead of merely transmitting it, accounting for energy absorption from the light wave <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a>.
Additional complexities include understanding how the [[light_refraction_and_the_refractive_index|index of refraction]] can be less than 1 (implying apparent speeds faster than c, but not violating causality for information transfer) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>, and the concept of birefringence where a material has multiple refractive indices <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. The distinction between the speed of wave crests and the speed of information ([[wave behavior in materials and phase shift|wave packets]]) is also a related area of study <a class="yt-timestamp" data-t="00:27:57">[00:27:57]</a>.