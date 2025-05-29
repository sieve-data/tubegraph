---
title: Feynmans explanation of electromagnetic waves
videoId: KTzGBJPuJwM
---

From: [[3blue1brown]] <br/> 

The phenomenon of light separating into colors when passing through a prism is one of the most recognized physics experiments <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While often depicted iconically, such as on Pink Floyd's "Dark Side of the Moon" album cover, some artistic choices contradict the actual physics, like showing white light inside the prism or discrete colors <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Isaac Newton's original experiments with prisms demonstrated that sunlight contains a continuous spectrum of colors <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## The Standard Explanation

A common explanation for how prisms work, often taught in high school physics, posits that when light enters a medium like glass, it slows down <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The crests of the light wave, which travel at the speed of light `c` in a vacuum, move slower inside the glass <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. The ratio between the speed of light in a vacuum and its speed inside a medium is called the index of refraction <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

If a light beam enters the glass at an angle, this slowdown causes it to bend, or refract <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This bending can be visualized by imagining a tank moving from a fast region (concrete) into a slower region (mud) at an angle; one tread hits the slow region first, causing the tank to steer <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Snell's Law quantitatively describes this bending, stating that the sine of the angle of incidence divided by the light's speed is constant, meaning slower light bends more <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

The key to prism function in this explanation is that the amount light slows down depends on its frequency <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. For instance, high-frequency blue light slows down more aggressively than low-frequency red light <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. White light, which is a [[Fourier series and sine waves | sum of a bunch of clean sine waves]] corresponding to pure spectral colors, experiences different refraction amounts for each component, leading to the iconic separation into a rainbow <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Limitations of the Standard Explanation

While accurate, the standard explanation doesn't delve into *why* light slows down, *what* "slowing down" truly means for a wave, or *why* the slowdown depends on color <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. For a deeper understanding, one needs to discover these facts rather than merely accept them <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Feynman's Approach to Understanding Prisms

Richard Feynman's lectures offer a more fundamental explanation, focusing on the interactions of light with individual charges within a material <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### The Phase Kick and Apparent Slowdown

Feynman's approach involves considering the material (e.g., glass) as distinct layers perpendicular to the light's direction <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. A single layer interacts with the light wave by "kicking back" its phase <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

Phase is a term in wave terminology that describes the horizontal shift of a wave function (e.g., in `sin(x + constant)`) <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. If a light wave hits a layer of glass, the function describing it after the interaction has an extra constant added to its input, shifting its phase <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

When multiple layers of glass each apply a small phase kick, the cumulative effect on the wave is a "squishing together" of its wavelength <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. As this process is smoothed out by considering a continuum of infinitesimally thin layers, the resulting wave is indistinguishable from one that is simply traveling slower while maintaining the same frequency but with a scrunched-up wavelength <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Thus, the question of why light slows down becomes why a single layer causes a phase kick <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

### Fundamentals of Light and Interactions

[[understanding_light_as_electromagnetic_waves | Light is a wave in the electromagnetic field]] <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. Specifically, an oscillating (wiggling) charged particle produces propagating ripples in the electric field that travel at the speed `c`, the speed of causality <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. These ripples can, in turn, cause other charged particles to wiggle <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. The specific force law describing this phenomenon can be derived from [[Maxwells equations and vector calculus | Maxwell's equations]] <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

When multiple charges oscillate, their effects on the electric field [[polarization and superposition in quantum mechanics | superimpose]] <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. A plane of charges wiggling in sync produces a concentrated beam of light perpendicular to that plane due to constructive interference <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

### Second-Order Waves and Phase Shift Explained

When an incoming light beam enters a material, it causes the charges (e.g., electrons, ions) within that material to wiggle in response <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. These wiggling charges, in turn, produce their own "second-order" light waves at the same frequency, propagating in both directions perpendicular to the layer <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. The overall electric field is the sum of the initial incoming light wave and this second-order wave <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. While some light is reflected back <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>, the focus for refraction is on the wave propagating forward.

Adding two waves of the same frequency can be visualized using rotating vectors:
*   Each wave corresponds to the y-component of a rotating vector, where the vector's length is the wave's amplitude and its initial angle is the wave's phase <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
*   The sum of the two waves corresponds to the sum of these rotating vectors (tip to tail) <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   If the second wave's phase is exactly 90 degrees behind the first, and the second wave is much smaller, the resulting wave is almost identical to the first but shifted back in phase by a tiny amount <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. The magnitude of this phase shift depends on the amplitude of the second wave <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

The crucial insight is that the second-order wave produced by the wiggling charges in a material layer is exactly a quarter of a cycle (90 degrees) behind the phase of the incoming light wave <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. This phase relationship is why adding them together results in a phase shift to the overall wave <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

### Why Phase Shift (and Slowdown) Depends on Color: The Driven Harmonic Oscillator

To understand why the index of refraction depends on color, one must understand how much the charges wiggle in response to an incoming light wave <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. This requires modeling each charged particle in the material as if it's bound to an equilibrium position by a spring <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. This "linear restoring force" (force proportional to displacement) is a good approximation for small displacements <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.

If undisturbed, such a particle would undergo simple harmonic motion with a specific "resonant angular frequency" (`omega_r = sqrt(k/m)`, where `k` is the spring constant and `m` is mass) <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.

When an incoming light wave acts as an external force on these charges, it causes them to oscillate <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>. This is analogous to pushing a child on a swing <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. In the steady state, the charges oscillate at the same frequency as the light wave (`omega_l`), but the amplitude of their oscillation is critical <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

The amplitude of the charge's oscillation is inversely proportional to the difference between the square of the resonant frequency (`omega_r^2`) and the square of the light frequency (`omega_l^2`) <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
*   If `omega_l` is very close to `omega_r`, the oscillations grow very large (resonance) <a class="yt-timestamp" data-t="00:24:39">[00:24:39]</a>, similar to the Millennium Bridge oscillating due to crowd steps matching its resonant frequency <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.
*   If `omega_l` is much smaller than `omega_r`, the oscillations are much more modest <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.

Therefore, the size of the charge's wiggle depends on the frequency (color) of the incoming light <a class="yt-timestamp" data-t="00:26:14">[00:26:14]</a>. The more the charges wiggle, the stronger the second-order wave they produce, leading to a bigger phase shift of the overall light wave <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>. Since multiple phase shifts cause the apparent slowdown of light, the amount of slowdown ultimately depends on the light's frequency <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>. This is the fundamental reason why prisms separate light by color <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.

### Additional Considerations

An important detail is the inclusion of a "drag force" term in the model of the harmonic oscillator, which depends on the charge's velocity <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a>. This term accounts for the absorption of energy from the light wave by the material, explaining why some materials absorb light rather than merely transmitting it <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.

For more in-depth details, the Feynman lectures on the matter are highly recommended <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>. Other related topics include how the index of refraction can be less than one, why slowing implies bending, and the concept of light slowing down in a medium in terms of information transfer via wave packets <a class="yt-timestamp" data-t="00:27:42">[00:27:42]</a>.