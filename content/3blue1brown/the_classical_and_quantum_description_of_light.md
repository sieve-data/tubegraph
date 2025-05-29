---
title: The classical and quantum description of light
videoId: MzRCDLre1b4
---

From: [[3blue1brown]] <br/> 

Understanding light provides a foundational basis for learning [[quantum_mechanics_basics_for_beginners | quantum mechanics]] more deeply <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. While quantum mechanics is a vast field, examining light's description lays down essential foundations and intuitions, especially before delving into more advanced texts like the Feynman lectures <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Classical Understanding of Light

A natural starting point, where [[quantum_mechanics_basics_for_beginners | quantum mechanics]] itself began, is light <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. To grasp quantum concepts, it is crucial to understand waves and their mathematical description <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Many ideas from [[quantum_mechanics_basics_for_beginners | quantum mechanics]], such as describing states as [[polarization_and_superposition_in_quantum_mechanics | superpositions]] with various amplitudes and phases, emerge from the context of classical waves without involving "quantum weirdness" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Light as Electromagnetic Waves

In the late 1800s, light was understood as waves in the electromagnetic field <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

*   **Electric Field**: A vector field where each point in space has an arrow indicating the direction and strength of the field <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This arrow shows the direction of force on a charged particle, proportional to its length and the particle's charge <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Magnetic Field**: Another vector field where arrows indicate that a moving charged particle experiences a force perpendicular to both its motion and the field direction <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The force's strength is proportional to the particle's charge, velocity, and the arrow's length <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

[[Feynmans_explanation_of_electromagnetic_waves | Maxwell's equations]], a culmination of 19th-century physics, describe how these fields interact and cause changes to one another <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Specifically, a looping electric field corresponds to an increasing magnetic field, and vice versa <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This mutual interplay naturally leads to propagating waves where electric and magnetic fields oscillate perpendicularly to each other and to the direction of propagation <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This phenomenon is known as [[understanding_light_as_electromagnetic_waves | electromagnetic radiation]], encompassing radio waves and visible light <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Mathematical Description of Classical Waves

To describe waves, specific mathematical terms are used:

*   **Polarization**: Describes the direction of oscillation. For example, if the electric field oscillates horizontally, the light is horizontally polarized <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. This can be represented using kets (e.g., `|horizontal⟩` and `|vertical⟩`) as unit vectors <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Frequency (`f`)**: Determines how many cycles a wave completes per unit time <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Phase Shift (`phi`)**: Indicates the position of the wave in its cycle at time t=0 <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Amplitude (`a`)**: Represents the maximum displacement or strength of the wave <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Superposition in Classical Waves

[[polarization_and_superposition_in_quantum_mechanics | Superposition]] refers to the principle that if two distinct waves solve [[Feynmans_explanation_of_electromagnetic_waves | Maxwell's equations]], their sum also forms a valid wave, at least in a vacuum <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This linearity of [[Feynmans_explanation_of_electromagnetic_waves | Maxwell's equations]] allows for the addition of wave components <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. For example:
*   The sum of horizontal and vertical oscillations can result in a diagonally wiggling wave <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   If components are out of phase, their sum might trace an ellipse or, if 90 degrees out of sync with equal amplitudes, result in circularly polarized light <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. The phase is crucial as it affects how waves add together <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

The choice of which directions to describe waves (e.g., horizontal/vertical or diagonal/anti-diagonal) is called a **basis** <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This choice depends on the specific interaction, such as passing light through a polarizing filter, which absorbs energy from oscillations in a particular direction <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

### Classical Energy of a Wave

Classically, the energy of a wave is proportional to the square of its amplitude <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. If a wave is described as a [[polarization_and_superposition_in_quantum_mechanics | superposition]] of components (e.g., horizontal with amplitude Aₓ and vertical with Aᵧ), its energy density is proportional to Aₓ² + Aᵧ² <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. This aligns with the Pythagorean theorem, where energies of components add up <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. Classically, this energy can be continuously adjusted by changing the wave's amplitude <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

## Quantum Description of Light

### The Birth of Quanta

In the late 19th and early 20th centuries, physicists observed that energy, contrary to classical understanding, seemed to come in discrete amounts <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. For electromagnetic waves, energy is always an integer multiple of a specific constant (Planck's constant, `h`) multiplied by the wave's frequency (`f`) <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This means there's a minimal non-zero energy level for a given frequency, `hf` <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. An electromagnetic wave with this minimal energy is called a **photon** <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. This discreteness is unusual for waves in free space, though it's common for constrained waves (like harmonics in pipes) <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

### Superposition and Probability in Quantum Light

The mathematical description of classical electromagnetic waves, including [[polarization_and_superposition_in_quantum_mechanics | superposition]], amplitude, and phase, carries over to describing a photon <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. However, the interpretation differs significantly.

For a diagonally polarized photon, described as a [[polarization_and_superposition_in_quantum_mechanics | superposition]] of horizontal and vertical states, the classical idea of energy distribution (e.g., half energy in horizontal, half in vertical) is not valid because photons cannot have half their energy <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. Instead, the squares of the amplitudes of each component in the [[polarization_and_superposition_in_quantum_mechanics | superposition]] now represent the **probabilities** of observing the photon in one state or another <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.

#### Experimental Observation

If a diagonally polarized photon is shot at a vertically oriented polarizing filter <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>:
*   Classically, half its energy would be absorbed <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   Quantically, due to discrete energy packets, the photon either passes through with all its energy or is absorbed entirely <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   Experiments show that about half the time it passes, and half the time it's absorbed, appearing random <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   If it passes, the measurement forces its polarization to align with the filter's direction <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. This is analogous to [[schrodingers_equation_and_quantum_mechanics | Schrodinger's cat]], where a [[polarization_and_superposition_in_quantum_mechanics | superposition]] "collapses" into a single state upon measurement <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

An illustrative example involves polarizing filters:
1.  Two filters rotated 90 degrees apart block light completely because photons passing the first (e.g., vertically polarized) have a 0% chance of passing the second (horizontally oriented) <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
2.  Inserting a third filter at a 45-degree angle between them allows more light through <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. Fifty percent of photons passing the vertical filter will pass the diagonal one, and once they do, their polarization changes to purely diagonal <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. From this diagonal state, they then have a 50% chance of passing the 90-degree filter <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. This results in 25% of the original photons passing all three filters <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. This cannot be explained classically and demonstrates how the middle filter forces photons to change their states <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

When a photon's polarization is 22.5 degrees off a filter's direction:
*   Classically, its horizontal component (amplitude sin(22.5°) ≈ 0.38) would carry energy proportional to 0.38² ≈ 0.15 <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.
*   Quantically, this translates to an 85% probability of the photon passing entirely and a 15% probability of it being completely blocked <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.

The underlying wave equations remain the same, but the interpretation of amplitude squares shifts from energy distribution to probabilities of measurement outcomes <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. Complex numbers are often used to encode both amplitude and phase in a single value <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

## Generalization to Quantum Mechanics

These concepts extend beyond photons <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. While light was initially understood as a wave and then as individual particles (quanta), the reverse occurred for particles like electrons, which were discovered to be governed by similar wavy [[quantum_mechanics_basics_for_beginners | quantum mechanics]] <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. This phenomenon is known as [[waveparticle_duality_and_de_Broglie_hypothesis | wave-particle duality]].

In [[quantum_mechanics_basics_for_beginners | quantum mechanics]], states are described as [[polarization_and_superposition_in_quantum_mechanics | superpositions]] of multiple base states, the choice of which depends on the basis <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. Each component has an amplitude and a phase (often encoded as a complex number), and the phase is crucial due to the underlying wave nature <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>. The choice of measurement determines a set of base states, and the probability of measuring a particle in one of these states is proportional to the squares of the amplitudes of these numbers <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.

If the wavy nature of particles had been discovered first, the field might have been called "harmonic mechanics," as the "weirdness" would be that particles are governed by wave equations, not that waves come in discrete units <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. This foundational understanding of waves is key to grasping advanced quantum topics like [[bells_inequalities_in_quantum_mechanics | Bell's inequalities]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.