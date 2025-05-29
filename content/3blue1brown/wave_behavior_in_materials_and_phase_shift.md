---
title: Wave behavior in materials and phase shift
videoId: KTzGBJPuJwM
---

From: [[3blue1brown]] <br/> 

The widely recognized phenomenon of a prism separating white light into a continuous spectrum of colors is a fundamental physics experiment <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While often depicted iconically, such as on Pink Floyd's album cover, some representations contradict the underlying physics, like showing white light inside the prism or discrete colors <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Newton's original experiment highlighted that sunlight contains a continuous spectrum <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Standard Explanation of Light Refraction

A common explanation for how a prism works, often taught in high school physics, involves light slowing down when it enters a medium like glass <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. In a vacuum, light crests travel at speed `c`, but inside glass, they travel slower <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. The ratio between the speed of light in a vacuum and its speed in a medium is called the **index of refraction** <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

If a light beam enters glass at an angle, this slowdown causes it to bend, or refract <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. This can be visualized with an analogy of a tank moving from fast concrete into slower mud, where one tread hitting the mud first causes steering <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. Snell's law quantifies this bending, stating that the sine of the angle of incidence (with respect to the normal) divided by the light's speed is constant, meaning slower light bends more <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

### Frequency Dependence and Dispersion
A key aspect of prisms is that the amount light slows down depends on its frequency (or color) <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>. For example, blue light (higher frequency) slows down more than red light (lower frequency) <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>. White light from the sun is a complex sum of many pure sine waves, each corresponding to a spectral color <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. When white light enters a prism, these different frequency components refract by slightly different amounts, leading to the separation into a rainbow <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.

## Deeper Explanation: Phase Kickback and Wave Addition

While the standard explanation is not incorrect, it doesn't fully explain *why* light slows down, *what* "slowing down" truly means, or why the slowdown depends on color <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. A more satisfying explanation, as discussed in the Feynman Lectures, involves examining the interaction of light with individual [[electromagnetic_waves_and_charged_particles | charged particles]] within the material <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

### Effect of a Material Layer on Light
Consider a material like glass as a series of distinct layers perpendicular to the light's direction <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>. When a light wave interacts with one of these layers, its primary effect is to "kick back the phase" of the wave <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.

#### Wave Terminology Review
To understand this, it's helpful to review basic wave terminology:
*   **Amplitude**: The height of the wave's oscillation <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.
*   **Angular Frequency (ω)**: How rapidly a wave oscillates over time (in radians per unit time). Related to frequency by `ω = 2πf` <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.
*   **Wavenumber (k)**: How rapidly a wave oscillates over space <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.
*   **Phase (φ)**: A constant added inside the sine function that slides the wave left or right <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.

A "phase kickback" means that if the original wave is described by `sin(x)`, after hitting the layer, it's described by `sin(x + φ)`, where `φ` is a small negative constant <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.

### From Phase Kickback to Apparent Slowdown
When light passes through multiple layers of glass, each layer applies its own small phase kickback <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. As these kicks accumulate through a continuum of glass, the effect is indistinguishable from a wave that is simply traveling slower <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>. This apparent slowdown occurs while the wave oscillates at the same frequency, but its wavelength becomes "scrunched up" <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>. Therefore, the core question shifts from "why does light slow down?" to "why does a single layer cause a phase kickback, and how strong is it?" <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.

## Light as an Electromagnetic Wave

Light is a wave in the electromagnetic field, which associates each point in 3D space with a 3-dimensional vector representing the force on a hypothetical unit charge <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. Key to light's behavior is that if a [[electromagnetic_waves_and_charged_particles | charged particle]] wiggles, it creates propagating ripples in the electric field, traveling at the speed `c` (the speed of causality) <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>. These ripples, when they reach another [[electromagnetic_waves_and_charged_particles | charged particle]], cause it to wiggle, generating its own propagations <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>. This process is derivable from [[Maxwells_equations_and_electromagnetic_waves | Maxwell's equations]] <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>.

If a plane of charges oscillates in sync, their individual effects mostly cancel out except perpendicular to the plane, where they constructively interfere to form a concentrated beam of light <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>.

## Second-Order Waves and Phase Shift

When a light beam enters a material, it causes the [[electromagnetic_waves_and_charged_particles | charged particles]] (like electrons) within that material to wiggle in response <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>. This wiggling, in turn, produces its own "second-order light wave" at the same frequency, propagating in both directions perpendicular to the layer <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>. The overall electric field is the sum of the initial incoming light wave and this second-order wave <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>.

The reflections back are due to the second-order wave propagating backwards <a class="yt-timestamp" data-t="12:32:00">[12:32:00]</a>. Focusing on the forward propagation, when the second-order oscillation is added to the incoming light, the overall effect is nearly identical to the incoming light, but shifted back in phase by a small amount <a class="yt-timestamp" data-t="13:00:00">[13:00:00]</a>.

### Adding Waves with Rotating Vectors
To understand wave addition, especially when frequencies are the same, one can visualize waves as the y-component of rotating vectors <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>. The length of the vector corresponds to amplitude, and its initial rotation corresponds to phase <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>. To find the sum of two waves, one adds their corresponding vectors tip to tail <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>.

Crucially, if the phase of the second wave is exactly 90 degrees (a quarter cycle) behind the first wave, and the second wave's amplitude is very small compared to the first, then the resulting wave is almost identical to the initial wave but is shifted back in its phase by a tiny amount <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>. The size of this phase shift depends on the amplitude of the second wave <a class="yt-timestamp" data-t="16:01:00">[16:01:00]</a>. In the context of light passing through glass, the phase of the second-order wave generated by the wiggling charges is precisely a quarter of a cycle behind the incoming light wave <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.

## Driven Harmonic Oscillator Model

To determine the strength of the phase kick—and thus the [[effect_of_frequency_on_light_slowing_in_mediums | index of refraction's dependence on color]]—one must understand how much the charges in the material wiggle in response to the incoming light wave <a class="yt-timestamp" data-t="17:05:00">[17:05:00]</a>.

### Modeling Charges with Springs
Each [[electromagnetic_waves_and_charged_particles | charged particle]] in the material can be modeled as being bound to an equilibrium position by a spring <a class="yt-timestamp" data-t="17:25:00">[17:25:00]</a>. This "linear restoring force" (proportional to displacement, like Hooke's Law for springs) is a good approximation for small displacements <a class="yt-timestamp" data-t="18:05:00">[18:05:00]</a>.

A charge under such a force, without external influence, undergoes simple harmonic motion, oscillating like a sine wave <a class="yt-timestamp" data-t="18:32:00">[18:32:00]</a>. The frequency of this oscillation, called the **resonant angular frequency** (ω_r), is given by the square root of `k/m` (where `k` is the spring constant and `m` is mass) <a class="yt-timestamp" data-t="19:31:00">[19:31:00]</a>. A stronger spring (`k`) or smaller mass (`m`) leads to faster oscillation <a class="yt-timestamp" data-t="19:39:00">[19:39:00]</a>.

### External Driving Force: Light Wave
When a light beam shines on the material, it acts as an external oscillating force on these charges <a class="yt-timestamp" data-t="21:03:00">[21:03:00]</a>. This force also oscillates sinusoidally, but with a distinct angular frequency (ω_l) corresponding to the light's color <a class="yt-timestamp" data-t="21:10:00">[21:10:00]</a>.

After a short startup period, the charge will settle into a steady sinusoidal motion at the *same frequency as the light* <a class="yt-timestamp" data-t="22:37:00">[22:37:00]</a>. The critical factor is the *amplitude* of this oscillation. The amplitude of the charge's displacement is proportional to the light's strength and the charge, but it is inversely proportional to the difference between the square of the resonant frequency (ω_r²) and the square of the light's frequency (ω_l²) <a class="yt-timestamp" data-t="24:04:00">[24:04:00]</a>.

### Frequency Dependence and Prisms
This means that the amplitude of the charge's wiggle depends directly on the [[effect_of_frequency_on_light_slowing_in_mediums | frequency of the light]].
*   If the light's frequency (ω_l) is very close to the material's resonant frequency (ω_r), the oscillations will be large (resonance phenomenon) <a class="yt-timestamp" data-t="24:33:00">[24:33:00]</a>. This is analogous to pushing a child on a swing at its natural frequency <a class="yt-timestamp" data-t="24:44:00">[24:44:00]</a>.
*   If the light's frequency is significantly different from the resonant frequency, the oscillations will be much smaller <a class="yt-timestamp" data-t="25:23:00">[25:23:00]</a>.

Thus, the larger the difference between the light's frequency and the material's resonant frequency, the smaller the charge's wiggle <a class="yt-timestamp" data-t="25:44:00">[25:44:00]</a>. Consequently, a smaller wiggle produces a weaker second-order wave, leading to a smaller phase shift in the overall light wave <a class="yt-timestamp" data-t="26:26:00">[26:26:00]</a>.

This explains why the amount of apparent slowdown (and thus the index of refraction) ultimately depends on the frequency (color) of the light <a class="yt-timestamp" data-t="26:36:00">[26:36:00]</a>, providing the fundamental reason why prisms separate light by color.

### Further Considerations
While this model provides a robust explanation, some details are simplified:
*   **Damping/Drag Force**: A more complete model of the harmonic oscillator would include a term dependent on the charge's velocity (a "drag force") <a class="yt-timestamp" data-t="27:05:00">[27:05:00]</a>. This accounts for energy absorption by the material, explaining why some materials absorb or reflect light rather than allowing it to pass through <a class="yt-timestamp" data-t="27:19:00">[27:19:00]</a>.
*   **Advanced Topics**: Other phenomena like the index of refraction being less than one or birefringence (two different indices of refraction) can be explored with this framework <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
*   **Group vs. Phase Velocity**: This explanation focuses on the phase velocity of a pure sine wave. The speed at which information (like a wave packet) travels, known as group velocity, is a distinct concept <a class="yt-timestamp" data-t="28:01:00">[28:01:00]</a>.