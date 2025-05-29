---
title: Light refraction and the refractive index
videoId: KTzGBJPuJwM
---

From: [[3blue1brown]] <br/> 

Refraction is a widely recognized physics phenomenon, notably illustrated by a prism separating white light into a spectrum of colors <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While common in pop culture, the underlying physics is often misunderstood <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Standard Explanation of Refraction

The typical high school explanation for light refraction states that when light enters a medium like glass, it slows down <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This means the crests of the light wave travel slower inside the glass than in a vacuum <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. The ratio between the speed of light in a vacuum and its speed inside a medium is called the **index of refraction** for that medium <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

If a beam of light enters a medium at an angle, this slowdown causes it to bend, or refract <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. An analogy often used is a tank moving from concrete (fast) into mud (slow); if it enters at an angle, one tread slows first, causing the tank to steer until both treads are in the mud and it continues straight, but slower <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Snell's Law

[[snells_law | Snell's law]] quantifies how much light bends <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. It states that if you draw a line perpendicular to the boundary between two mediums, the sine of the angle between that perpendicular line and the light beam, divided by the speed of light in that medium, is constant <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This means slower light results in a lower angle, allowing for the calculation of refraction <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Dispersion in Prisms

A key aspect of prisms is that the amount light slows down depends on its frequency <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. For example, blue light (higher frequency) slows down more aggressively than red light (lower frequency) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

White light, such as sunlight, is not a single sine wave but can be expressed as a sum of many clean sine waves, each corresponding to a pure spectral color <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. When white light enters a prism, its different frequency components refract by slightly different amounts, leading to the iconic separation into rainbow colors <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## Limitations of the Standard Explanation

While the standard explanation is not wrong, it doesn't fully explain *why* light slows down, *what* "slowing down" precisely means, or why the slowdown depends on the light's color <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. A deeper understanding requires explaining these facts rather than taking them as given <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## Deeper Explanation: Feynman's Perspective

A more comprehensive explanation comes from [[feynmans_explanation_of_light_phenomena | Feynman's lectures]], which involves examining the interaction of individual wiggling charges within the material and the light waves they produce <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This approach clarifies why the effect depends on color <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### The "Phase Kick" Concept

Consider a material like glass as a stack of distinct layers perpendicular to the light's direction <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. When light interacts with a single layer, it effectively "kicks back" the phase of the wave <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

#### Wave Terminology Review
*   **Amplitude**: Affects how high the wave oscillates <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Angular Frequency (ω)**: Describes how rapidly a wave oscillates over time (2π times the frequency) <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   **Wave Number**: Describes how rapidly a wave oscillates over space <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   **Phase**: A constant added inside the sine function that slides the wave left or right <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

A phase kick means an extra term is added to the input of the sine function describing the wave <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. If many layers each apply a small phase kick, the cumulative effect is identical to a wave traveling slower, with a scrunched-up wavelength but the same frequency <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Thus, understanding the index of refraction boils down to understanding why a single layer causes a phase kick and how strong that kick is <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Light and Charge Interactions

Light is a wave in the electromagnetic field, represented by an electric field vector at each point in space <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
When a charged particle wiggles, it creates propagating ripples in the electric field that travel at the speed of causality, `c` <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. These ripples, when they reach another charged particle, cause it to wiggle, generating its own propagations <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

Crucially, the net effect on the electric field from multiple oscillating charges is the sum of their individual effects <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. A plane of charges wiggling in sync produces a concentrated beam of light perpendicular to the plane due to constructive interference <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

### Interaction with Material Layers

When a light beam enters a material, it causes charges (e.g., electrons, ions) within the material to wiggle in response <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. Each wiggling layer produces its own "second-order" light wave at the same frequency, propagating in both directions <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. The overall electric field is the sum of the initial incoming wave and this second-order wave <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. The light reflected back is on the left side of the layer, but for transmission, we focus on what happens to the right <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.

Adding the second-order oscillation to the incoming light results in a wave that is almost identical to the incoming light but shifted back in phase by a small amount <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. This phase shift is what ultimately explains the index of refraction <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.

#### Adding Waves with Rotating Vectors

To understand how two waves sum to cause a phase shift, consider representing each sine wave as the y-component of a rotating vector <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. The vector's length corresponds to the wave's amplitude, and its initial angle corresponds to its phase <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
If the waves have the same frequency, their sum can be found by adding their corresponding vectors tip to tail <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. The length and angle of the resulting vector sum give the amplitude and phase of the combined wave <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

A crucial insight is that if a second wave's phase is exactly 90 degrees behind the first (a quarter cycle out of sync) and it's much smaller than the first, the resulting combined wave is almost identical to the initial wave but is shifted back in phase by a tiny bit <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. The magnitude of this phase shift depends on the amplitude of the second wave <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. In the context of light in a material, the second-order wave from charge oscillations is indeed a quarter-cycle behind the incoming light, leading to the phase shift <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

## Driven Harmonic Oscillator Model

To understand why the index of refraction depends on color, one must understand how much the charges in the material wiggle in response to the incoming light wave <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. This involves modeling each charge as a [[wave_behavior_in_materials_and_phase_shift | harmonic oscillator]] bound to an equilibrium position by a spring-like force <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. This "linear restoring force" is proportional to the displacement from equilibrium (Hooke's Law) <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

In the absence of external forces, such a system undergoes simple harmonic motion, a sine wave, with a **resonant angular frequency** (ωr) given by the square root of k/m (spring constant/mass) <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>, <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. A stronger "spring" (larger k) or smaller mass (m) leads to faster oscillation <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.

When a light beam shines on the material, it acts as an external oscillating force on these charges, with an angular frequency of the light, ωL <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. This is analogous to pushing a child on a swing with a cyclic force <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. In this "steady state," the charge oscillates at the same frequency as the incoming light <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.

The amplitude of this driven oscillation is key <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. It is proportional to the strength of the incoming light wave and the charge of the particle <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>. The most significant factor is the denominator, which involves the difference between the square of the resonant frequency (ωr) and the square of the light frequency (ωL) <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.

*   If the light frequency (ωL) is very close to the resonant frequency (ωr), the oscillations grow very large (resonance) <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>, similar to the [[millennium_bridge_london_oscillations | Millennium Bridge]] or pushing a swing at its natural frequency <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.
*   If the light frequency (ωL) is much smaller than the resonant frequency (ωr), the amplitude of motion is much more modest <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.

This means that the larger the difference between the light frequency and the resonant frequency, the smaller the oscillation of the charge <a class="yt-timestamp" data-t="00:25:44">[00:25:44]</a>.

## Conclusion: How Prisms Work

As light shines into a material, the size of the induced wiggles in its charges depends on the light's frequency due to this denominator term <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>. The more the charges wiggle, the stronger the second-order wave they produce <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>. A stronger second-order wave causes a bigger shift to the phase of the overall light wave <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>. Since accumulated phase shifts are what cause the apparent slowdown of light, this explains why the amount light slows down (its index of refraction) depends on its frequency, or color <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>. This fundamental interaction explains why prisms work and why light separates into colors <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.

### Omitted Details

A more complete model of the harmonic oscillator should include a "drag force" term dependent on the charge's velocity <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a>. This term accounts for the absorption of energy from the light wave by the material, explaining why some materials absorb or reflect light rather than allowing it to pass through <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.

### Further Questions

The concept of the index of refraction also raises questions such as how it can be less than one (implying apparent speeds greater than `c` for wave crests, but not information) and birefringence, where a material has two different indices of refraction <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>, <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>, <a class="yt-timestamp" data-t="00:27:42">[00:27:42]</a>. The topic also relates to the idea of light slowing down in a medium in terms of sending information via a wave packet, rather than just the steady-state crests of a pure sine wave <a class="yt-timestamp" data-t="00:27:57">[00:27:57]</a>.