---
title: How prisms work
videoId: KTzGBJPuJwM
---

From: [[3blue1brown]] <br/> 

A prism separating white light into a rainbow is one of the most widely recognized physics experiments, famously featured on an iconic album cover <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While visually striking, the album art contains physics inaccuracies, such as depicting white light *inside* the prism or showing discrete colors instead of a continuous spectrum <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Standard Explanation

The common high school physics explanation for how a prism works is as follows:
*   When light enters a medium like glass, it slows down <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The ratio between the speed of light in a vacuum and its speed within the medium is called the [[snells_law_and_light_refraction | index of refraction]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   If a light beam enters the medium at an angle, this slowdown causes it to bend, or refract <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This can be visualized with an analogy of a tank moving from concrete (fast) into mud (slow) at an angle, causing it to steer <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   The exact amount of bending is described by [[snells_law_and_light_refraction | Snell's Law]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This law states that the sine of the angle of incidence divided by the speed of light in the medium is a constant, meaning slower light results in a lower angle <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   In a prism, the amount that light slows down depends on its frequency (color) <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. For example, blue light (higher frequency) slows down more aggressively than red light (lower frequency) <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   White light from the sun is a complex signal that can be expressed as a sum of many pure sine waves, each corresponding to a pure spectral color <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   When white light enters a prism, its different color components are refracted by slightly different amounts, leading to the iconic separation into rainbow colors <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

While this explanation is not incorrect, it treats key concepts like light slowing down and its dependence on color as given facts, rather than derived principles <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## A Deeper Dive: The Feynman Lectures Approach

A more fundamental understanding, inspired by the Feynman Lectures, involves considering the interaction of light with individual charges within the material <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### The Phase Kickback

Imagine the material, like glass, as a series of distinct layers perpendicular to the light's direction <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. A single layer causes a "kickback" to the phase of the light wave <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

#### Wave Terminology
*   **Amplitude:** Affects how high the wave oscillates <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Angular Frequency (ω):** Affects how rapidly the wave oscillates over time <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Wave Number (k):** Affects how rapidly the wave oscillates over space <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Phase (φ):** A constant added inside the sine function that slides the wave left or right <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

When a layer "kicks back" the phase, it adds a small constant to the input of the sine function describing the wave <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. As many successive layers apply these small phase kicks, the wave effectively gets "squished together," which is indistinguishable from a wave traveling slower with a scrunched wavelength <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Light as Electromagnetic Waves and Wiggling Charges

Light is a wave in the electromagnetic field <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. The electric field describes the force applied to a hypothetical charge at any point in space <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
*   [[visualizing_transformations_in_three_dimensions | Wiggling charges]] generate propagating ripples (light) in the electric field, traveling at the speed of causality, 'c' <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   These ripples cause other charges to wiggle, generating their own propagations <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   When multiple charges oscillate in sync, their effects constructively interfere perpendicular to their plane, forming a concentrated beam of light <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

When light enters a material, it causes charges (electrons, ions) within that material to wiggle in response <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. Each wiggling layer produces its own "second-order" light wave <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. The overall electric field is the sum of the initial incoming wave and these second-order waves <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. (Light reflected back to the left of the layer is ignored for this discussion <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.)

#### Adding Waves with Phasor Diagrams
Adding two sine waves of the same frequency can be visualized by representing them as rotating vectors (phasors) <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
*   The length of the vector corresponds to the wave's amplitude <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
*   The initial angle of the vector corresponds to the wave's phase <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   The sum of the waves is found by adding their vectors tip-to-tail <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

Crucially, if the second-order wave is small and its phase is exactly 90 degrees (a quarter cycle) behind the incoming wave, the resulting sum wave is almost identical to the initial wave, but shifted back in phase by a tiny amount <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. The strength of this phase shift depends on the amplitude of the second-order wave <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

### The Driven Harmonic Oscillator

To understand why the [[snells_law_and_light_refraction | index of refraction]] depends on color, we need to know how strongly the charges wiggle in response to incoming light <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
*   Each charge in the material can be modeled as being bound to an equilibrium position by a spring-like force (a linear restoring force), obeying Hooke's Law (force proportional to displacement) <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.
*   Without external force, this produces simple harmonic motion with a specific "resonant angular frequency" (ω_r) of $\sqrt{k/m}$, where 'k' is the spring constant and 'm' is the mass <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. A stronger spring or lighter mass increases the resonant frequency <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.

When an incoming light wave (an external oscillating force with angular frequency ω_L) acts on these charges, it's like pushing a child on a swing <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. After an initial startup period, the charge oscillates sinusoidally at the same frequency as the light (ω_L), but its amplitude (how much it wiggles) is determined by a specific formula <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>.

The amplitude of the charge's oscillation is inversely proportional to the difference between the square of the resonant frequency (ω_r) and the square of the light frequency (ω_L) <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
*   If ω_L is very close to ω_r, the oscillations grow very large (resonance), similar to the Millennium Bridge swaying due to pedestrian steps <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a>.
*   If ω_L is much smaller than ω_r, the oscillations are much more modest <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.

Therefore, the size of the charge's wiggle depends on the frequency (color) of the incoming light <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>. A larger wiggle creates a stronger second-order wave, which in turn causes a bigger shift to the phase of the overall light wave <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>. Since a series of phase shifts causes the apparent slowdown of light, this ultimately explains why the amount of slowdown (and thus refraction) depends on the light's frequency <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>. This is the fundamental reason why prisms separate light by color <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.

> [!NOTE] Further details, such as the exact reason for the 90-degree phase lag of the second-order wave and the effect of drag force (accounting for light absorption), are more complex and can be found in resources like the Feynman lectures <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>. Some materials can also have an [[snells_law_and_light_refraction | index of refraction]] less than 1, or even multiple indices (birefringence) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.