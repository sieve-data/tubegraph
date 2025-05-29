---
title: Physical explanation of light slowing down
videoId: KTzGBJPuJwM
---

From: [[3blue1brown]] <br/> 

The phenomenon of light bending and separating into colors when passing through a prism is one of physics' most recognized experiments <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. While widely known, the underlying physical explanation for why light slows down in a medium, and how this relates to color, is often not deeply understood <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Standard High School Explanation

In a typical high school physics class, the explanation for light's behavior in a medium, such as glass, goes as follows:
*   When light enters a medium, it slows down <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   The crests of the light wave, which travel at 'c' (the [[huygens_and_the_speed_of_light | speed of light]]) in a vacuum, travel slower inside the glass <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.
*   The ratio between the speed of light in a vacuum and its speed inside a medium is called the [[understanding_light_as_electromagnetic_waves | index of refraction]] <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
*   If a beam of light enters a medium at an angle, this slowdown causes it to bend, or "refract" <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. This can be visualized with an analogy of a tank moving from concrete into mud: one tread hits the slower region first, causing the tank to steer <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.
*   [[snells_law_and_light_refraction | Snell's law]] mathematically specifies the amount of bending based on the angles and speeds of light <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   For prisms, the key insight is that the amount light slows down depends on its frequency (color) <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>. For instance, blue light (higher frequency) slows down more aggressively than red light (lower frequency) <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.
*   Since white light, like sunlight, is a continuous spectrum of colors (a sum of many clean sine waves corresponding to pure spectral colors) <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>, each component refracts by a slightly different amount, leading to the iconic separation into rainbow colors <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.

### Limitations
While factually correct, this standard explanation leaves several questions unanswered:
*   Why does light slow down? <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>
*   What does "slowing down" truly mean in the context of light? <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>
*   Why does the amount of slowdown depend on the color (frequency) of light? Is this a coincidence or a necessity? <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>

## Feynman's Deeper Explanation

A more satisfying explanation, notably articulated in the [[feynmans_explanation_of_electromagnetic_waves | Feynman lectures]], involves examining the interactions between light and the individual charges within a material <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

### The Phase Kick and Apparent Slowdown
Instead of simply stating that light slows down, a deeper approach considers how a material affects the *phase* of a light wave <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.

*   **Wave Terminology**:
    *   **Amplitude**: The height of a wave's oscillation <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
    *   **Angular Frequency**: How rapidly a wave oscillates over time (radians per unit time) <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>. Related to frequency by a factor of 2π <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.
    *   **Phase**: A constant added inside the sine function that shifts the wave left or right <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.

*   **Layer-by-Layer Interaction**: Imagine a material, like glass, as a stack of distinct layers perpendicular to the direction of light travel <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.
*   Each infinitesimal layer of the glass applies a tiny "kickback" to the phase of the light wave <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.
*   When a continuous medium applies many such infinitesimal phase kicks, the resulting wave is **identical to a wave simply traveling slower** and having a "scrunched up" wavelength, while maintaining the same frequency <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.
*   Therefore, the question "why does light slow down?" transforms into "why does interaction with a single layer cause a phase kickback?" and "how strong is that phase kick?" <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.

### Light as an Electromagnetic Wave and Interactions with Charges
Light is a wave in the [[the_classical_and_quantum_description_of_light | electromagnetic field]], depicted by the electric field which exerts force on charges <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.
*   When a charged particle wiggles, it creates propagating ripples in the electric field that travel at the speed 'c' (the speed of causality) <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
*   These ripples can, in turn, cause other charged particles to wiggle <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>.
*   The net effect of multiple oscillating charges on the electric field is the sum of their individual effects <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>.
*   Crucially, a plane of charges wiggling in sync produces a concentrated beam of light perpendicular to that plane, effectively creating a new sinusoidal wave <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>.

When an incoming light beam enters a material, it causes the charges (electrons, ions) within that material to wiggle in response <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>.
*   This wiggling produces its own "second-order" light wave, propagating in both directions <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>. (The backward propagation accounts for reflection, which is typically ignored in the context of light transmission through a medium <a class="yt-timestamp" data-t="12:32:00">[12:32:00]</a>.)
*   The overall electric field within the material is the sum of the initial incoming light wave and this second-order wave <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>.

### Adding Waves: The Vector Sum Analogy
To understand how these waves add, visualize them as rotating vectors:
*   A sine wave can be represented by the y-component of a rotating vector <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>. The vector's length is the wave's amplitude, and its initial angle is its phase <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>.
*   If two waves have the same frequency, their sum is found by adding their corresponding vectors tip to tail <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>. The resulting vector's length gives the amplitude of the sum wave, and its angle gives the phase <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>.
*   Crucially, if the second wave's phase is exactly **90 degrees behind** the first, and the second wave is much smaller, their sum results in a wave that is almost identical to the first but **shifted back slightly in phase** <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>. The strength of this phase shift depends on the amplitude of the second wave <a class="yt-timestamp" data-t="16:01:00">[16:01:00]</a>.
*   When the light wave interacts with a layer of material, the second-order wave produced by the wiggling charges is exactly a quarter of a cycle (90 degrees) behind the incoming light's phase <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>. This results in the observed phase shift.

### The Role of Resonant Frequency (Driven Harmonic Oscillator)
The amount of phase kick (and thus the apparent slowdown) depends on the strength of the second-order wave, which in turn depends on how much the charges in the material wiggle <a class="yt-timestamp" data-t="17:05:00">[17:05:00]</a>. This requires understanding the "driven harmonic oscillator":
*   **Modeling Charges**: Charges in a material can be modeled as if they are bound to an equilibrium position by a spring <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>. This creates a linear restoring force <a class="yt-timestamp" data-t="18:05:00">[18:05:00]</a>.
*   **Resonant Frequency (ωr)**: Without external force, such a charge oscillates with a natural or "resonant frequency" (ωr), which is proportional to the square root of the "spring constant" (k) divided by the mass (m) of the particle: ωr = √(k/m) <a class="yt-timestamp" data-t="19:54:00">[19:54:00]</a>. This frequency depends solely on the material's properties <a class="yt-timestamp" data-t="23:01:00">[23:01:00]</a>.
*   **Driven Oscillation**: When a light beam (an external oscillating force with angular frequency ωL) shines on the material, it forces the charges to wiggle <a class="yt-timestamp" data-t="20:59:00">[20:59:00]</a>.
*   In the steady state, the charges oscillate at the **same frequency as the light (ωL)**, not their resonant frequency <a class="yt-timestamp" data-t="23:07:00">[23:07:00]</a>.
*   The **amplitude** of these induced oscillations (how much the charges wiggle) is crucial <a class="yt-timestamp" data-t="23:22:00">[23:22:00]</a>. This amplitude is inversely proportional to the difference between the square of the resonant frequency and the square of the light frequency <a class="yt-timestamp" data-t="24:28:00">[24:28:00]</a>:
    *   If ωL is close to ωr, the oscillations become very large (resonance) <a class="yt-timestamp" data-t="24:36:00">[24:36:00]</a>.
    *   If ωL is far from ωr, the oscillations are much more modest <a class="yt-timestamp" data-t="25:23:00">[25:23:00]</a>.

### Conclusion: Why Prisms Work
The specific size of the charge wiggles depends on the frequency of the light (ωL) because of its relation to the material's resonant frequency (ωr) <a class="yt-timestamp" data-t="26:14:00">[26:14:00]</a>.
*   The more the charges wiggle, the larger the second-order wave they produce <a class="yt-timestamp" data-t="26:26:00">[26:26:00]</a>.
*   A larger second-order wave causes a bigger phase shift to the overall light wave <a class="yt-timestamp" data-t="26:29:00">[26:29:00]</a>.
*   Since successive phase shifts manifest as an apparent slowdown of light, the amount of slowdown ultimately depends on the light's frequency <a class="yt-timestamp" data-t="26:36:00">[26:36:00]</a>.

This detailed explanation connects the macroscopic behavior of light in a prism (separation by color) to the microscopic interactions between light waves and the charges within the material, making it clear why the index of refraction depends on color <a class="yt-timestamp" data-t="26:47:00">[26:47:00]</a>.

### Additional Considerations
*   **Damping Force**: A more complete model of the harmonic oscillator includes a damping or drag force dependent on the charge's velocity <a class="yt-timestamp" data-t="27:05:00">[27:05:00]</a>. This term accounts for energy absorption from the light wave by the material, explaining why some materials absorb or reflect light rather than simply transmitting it <a class="yt-timestamp" data-t="27:17:00">[27:17:00]</a>.
*   **Index of Refraction less than 1**: The [[understanding_light_as_electromagnetic_waves | index of refraction]] can sometimes be less than 1, implying a speed faster than 'c'. This does not violate the principle that information cannot travel faster than 'c', as the wave packet (which carries information) still respects this limit <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
*   **Birefringence**: Some materials exhibit two different indices of refraction depending on the polarization of light, causing a double image <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.