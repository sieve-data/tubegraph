---
title: Understanding light as electromagnetic waves
videoId: MzRCDLre1b4
---

From: [[3blue1brown]] <br/> 

To deeply learn [[quantum_mechanics_basics_for_beginners | quantum mechanics]], it is essential to understand waves and their mathematical description <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Many ideas from [[quantum_mechanics_basics_for_beginners | quantum mechanics]], such as describing states as superpositions with various amplitudes and phases, emerge from classical wave concepts without involving quantum weirdness <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.

## Classical Understanding of Light

The late 1800s understanding of light describes it as waves in the electromagnetic field <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.

### Electric and Magnetic Fields
*   **Electric field**: A vector field where each point in space has an arrow indicating the direction and strength of the field <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>. If a charged particle is in this space, a force acts on it in the direction of the arrow, proportional to the arrow's length and the particle's charge <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.
*   **Magnetic field**: Another vector field where, for a charged particle moving through it, a force acts perpendicular to both its motion and the magnetic field's direction <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. The force's strength is proportional to the particle's charge, velocity, and the magnetic field arrow's length <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>. An example is a wire with current next to a magnet, which is pushed or pulled by the magnetic field <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

### Maxwell's Equations and Electromagnetic Waves
Maxwell's equations, a culmination of 19th-century physics, describe how electric and magnetic fields interact and cause changes in each other <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.
*   When electric field arrows form a loop, the magnetic field increases perpendicular to the loop's plane within that region <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.
*   Symmetrically, a loop in the magnetic field corresponds to a change in the electric field perpendicular to the loop's plane <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
This mutual interplay results in propagating waves where electric and magnetic fields oscillate perpendicularly to each other and to the direction of propagation <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. This phenomenon is known as electromagnetic radiation, encompassing radio waves and visible light <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. The discovery that light is a propagating wave of these interacting fields was surprising in Maxwell's time <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

## Mathematical Description of Classical Waves

Ideas crucial to [[quantum_mechanics_basics_for_beginners | quantum mechanics]], such as superposition, amplitudes, and phases, arise naturally in the context of classical waves <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.

### Wave Components and Polarization
Consider a wave directed out of the screen, focusing only on the oscillating electric field in the xy-plane <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.
*   **Horizontally polarized light**: The electric field oscillates horizontally, meaning its y-component is zero <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>. The x-component can be described as $A \cos(2\pi ft + \phi)$ <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.
    *   `f` represents the frequency, indicating how many cycles the cosine function completes per unit time <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>.
    *   `$\phi$` is the phase shift, indicating the vector's position in its cycle at time t=0 <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.
    *   `A` is the amplitude, which scales the wave's maximum oscillation <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.
    *   These components can be separated using kets: $| \text{horizontal} \rangle$ for the unit vector in the horizontal direction and $| \text{vertical} \rangle$ for the unit vector in the vertical direction <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>.
*   **Vertically polarized light**: The electric field oscillates purely in the up-and-down direction, with a zero horizontal component <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

### Superposition and Basis
*   **Superposition**: If two distinct waves solve Maxwell's equations in a vacuum, their sum also forms a valid wave <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>. This is because Maxwell's equations in a vacuum are linear equations <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>. Adding these vectors tip to tail at all points in space and time creates a new valid solution, called a superposition <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.
*   **Phase differences**: If horizontal and vertical components are out of phase, their sum can trace out an ellipse <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>. When phases are exactly 90 degrees out of sync and amplitudes are equal, it results in [[polarization_and_superposition_in_quantum_mechanics | circularly polarized light]] <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. The phase is important as it affects how waves add together <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.
*   **Basis**: Waves can be described with respect to different directions, such as horizontal/vertical or diagonal/anti-diagonal <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. This choice of directions is called a basis <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.
    *   For example, [[polarization_and_superposition_in_quantum_mechanics | vertically polarized light]] can be a superposition of diagonal and anti-diagonal directions if they are in phase and have the same magnitude <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>.
    *   Polarizing filters absorb energy from electromagnetic oscillations in specific directions <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>. A vertically oriented polarizer absorbs horizontal energy, allowing only the vertical component of the original wave to pass through <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>. The choice of basis depends on the specific interaction with light, such as passing through a filter <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.

## Transition to Quantum Mechanics: Quantization of Light

Classically, the energy of a wave is proportional to the square of its amplitude <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>. If a wave is a superposition of a horizontal component with amplitude $A_x$ and a vertical component with amplitude $A_y$, its energy density is proportional to $A_x^2 + A_y^2$, aligning with the Pythagorean theorem <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>. Classically, this energy could be continuously varied by changing the wave's amplitude <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>.

However, late 19th and early 20th-century physicists observed that energy appears in discrete amounts <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>. The energy of electromagnetic waves always comes as an integer multiple of a constant (Planck's constant, `h`) times the wave's frequency (`f`), i.e., $E = nhf$ <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>. This means there's a minimal non-zero energy level for waves of a given frequency, `hf`, which cannot be made smaller without eliminating the wave entirely <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>. This concept of discrete energy units, called harmonics, is common in constrained waves (like in pipes or instrument strings) but is weird for electromagnetic waves in free space <a class="yt-timestamp" data-t="12:39:00">[12:39:00]</a>. An electromagnetic wave with this minimal possible energy is called a photon <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>.

## Quantum Interpretation

The mathematical description used for classical electromagnetic waves also applies to describing a photon <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>. A photon with a 45-degree diagonal [[polarization_and_superposition_in_quantum_mechanics | polarization]] can be described as a superposition of horizontal and vertical states, each with an amplitude and phase <a class="yt-timestamp" data-t="13:03:00">[13:03:00]</a>. This is consistent with what is seen in [[quantum_mechanics_basics_for_beginners | quantum mechanics]] <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a>.

### Amplitudes and Probabilities
Unlike classical waves where amplitude squares relate to energy, in [[quantum_mechanics_basics_for_beginners | quantum mechanics]], the squares of amplitudes in a superposition indicate probabilities <a class="yt-timestamp" data-t="13:26:00">[13:26:00]</a>.
*   If a diagonally polarized photon has an amplitude of 1 unit, its horizontal and vertical components would each have hypothetical amplitudes of $\sqrt{1/2}$ <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.
*   However, a wave of this frequency cannot have half the energy of a photon, as energy comes in indivisible chunks <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>.
*   When a diagonally polarized photon is shot at a vertically oriented polarizing filter, classically, half its energy would be absorbed <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>. However, due to quantized energy packets, the photon either passes through entirely or is absorbed entirely <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>. Approximately half the time, the photon passes through, and half the time it is absorbed, appearing random <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>.
*   If a photon passes through, its polarization is changed to align with the filter's direction <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>. This is analogous to [[polarization_and_superposition_in_quantum_mechanics | Schrödinger's cat]], where a superposition collapses to one state upon measurement <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>.

### The Three-Filter Experiment
This phenomenon can be observed by setting up three polarizing filters <a class="yt-timestamp" data-t="15:40:00">[15:40:00]</a>:
1.  Two filters rotated 90 degrees from each other block light completely because photons passing the first (e.g., vertical) have a 0% chance of passing a horizontally oriented filter <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>.
2.  Inserting a third filter oriented at a 45-degree angle between the first two allows more light to pass through <a class="yt-timestamp" data-t="16:10:00">[16:10:00]</a>.
    *   50% of photons passing the vertical filter will also pass the diagonal filter <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>.
    *   Once they pass, their polarization changes to purely diagonal <a class="yt-timestamp" data-t="16:23:00">[16:23:00]</a>.
    *   In this diagonal state, they have a 50-50 chance of passing the final 90-degree filter <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>.
    *   As a result, 25% of the original photons pass through all three filters <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a>. This demonstrates that the middle filter forces photons to change their states <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>.

Consider a photon whose [[polarization_and_superposition_in_quantum_mechanics | polarization]] is 22.5 degrees off the direction of a filter <a class="yt-timestamp" data-t="17:06:00">[17:06:00]</a>.
*   Classically, if the wave has an amplitude of 1, its horizontal component would have an amplitude of $\sin(22.5^\circ) \approx 0.38$, and its vertical component would have an amplitude of $\cos(22.5^\circ) \approx 0.92$ <a class="yt-timestamp" data-t="17:20:00">[17:20:00]</a>.
*   Classically, passing it through a vertical filter would mean 15% of its energy (proportional to $0.38^2$) is absorbed in the horizontal direction <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>.
*   However, due to the discrete nature of light quanta, what is observed is that 85% of the time the photon passes through entirely (proportional to $0.92^2$), and 15% of the time it is completely blocked <a class="yt-timestamp" data-t="18:07:00">[18:07:00]</a>.

The wave equations for photons remain the same; a photon is described as a superposition of oscillating components with phase and amplitude, often encoded using a single complex number <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>. The key difference is that the squares of the amplitudes of each component tell you the *probabilities* that a photon will be found to have all its energy in one direction <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>. Photons can also be [[polarization_and_superposition_in_quantum_mechanics | circularly polarized]], and filters exist that let through photons polarized circularly (e.g., clockwise), with probabilities determined by the square of the amplitude of the desired component <a class="yt-timestamp" data-t="18:58:00">[18:58:00]</a>.

## Conclusion

Photons are just one quantum phenomenon, where light was initially understood as a wave via Maxwell's equations and then as individual particles or quanta, leading to the name [[quantum_mechanics_basics_for_beginners | quantum mechanics]] <a class="yt-timestamp" data-t="19:32:00">[19:32:00]</a>. Conversely, particles like electrons, initially understood as discrete packets, were found to be governed by similar wavy [[quantum_mechanics_basics_for_beginners | quantum mechanics]] <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>.

In [[quantum_mechanics_basics_for_begginers | quantum mechanical]] states, far beyond the photon polarization example:
*   States are described as superpositions of multiple base states <a class="yt-timestamp" data-t="19:52:00">[19:52:00]</a>.
*   The superposition depends on the chosen basis <a class="yt-timestamp" data-t="19:56:00">[19:56:00]</a>.
*   Each component has an amplitude and a phase, often encoded as a complex number <a class="yt-timestamp" data-t="20:03:00">[20:03:00]</a>. The need for phase arises from the wave nature of these objects <a class="yt-timestamp" data-t="20:07:00">[20:07:00]</a>.
*   The choice of how to measure these objects determines a set of base states <a class="yt-timestamp" data-t="20:14:00">[20:14:00]</a>.
*   The probability of measuring a particle in one of these base states is proportional to the squares of the amplitudes <a class="yt-timestamp" data-t="20:17:00">[20:17:00]</a>.

If the wavy nature of electrons and other particles had been discovered first, the field might have been called "harmonic mechanics" because the weirdness would not be that waves come in discrete units, but that particles are governed by wave equations <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>.