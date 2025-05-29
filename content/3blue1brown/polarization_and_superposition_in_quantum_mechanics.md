---
title: Polarization and superposition in quantum mechanics
videoId: MzRCDLre1b4
---

From: [[3blue1brown]] <br/> 

To understand quantum mechanics deeply, it is essential to grasp the mathematical description of waves and their behavior, particularly the [[relationship_between_classical_and_quantum_waves | relationship between the energy in a purely classical wave and the probabilities that govern quantum behavior]] <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Many core ideas in quantum mechanics, such as describing states as superpositions with various amplitudes and phases, originate from classical wave contexts without involving "quantum weirdness" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This classical foundation helps in appreciating what is truly unique in quantum mechanics, namely restrictions on energy levels, measurement behavior, and quantum entanglement (though entanglement is not covered in this video) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Classical Waves and Light

The starting point for quantum mechanics, and a natural place to begin learning, is light <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Electromagnetic Fields and Waves

In the late 1800s, light was understood as waves in the electromagnetic field <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Electric Field:** A vector field where each point in space has an arrow indicating the direction and strength of the field <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. A charged particle in this field experiences a force in the direction of the arrow, proportional to the arrow's length and the particle's charge <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Magnetic Field:** Another vector field where the arrow's physical meaning relates to the force on a moving charged particle <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This force is perpendicular to both the particle's motion and the magnetic field direction, and its strength is proportional to the particle's charge, velocity, and the magnetic field's strength <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

[[maxwells_equations_and_electromagnetic_waves | Maxwell's equations]] culminated the 19th-century understanding of these fields <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. These equations describe how changes in one field can cause changes in the other <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. A key consequence is the propagation of waves where electric and magnetic fields oscillate perpendicularly to each other and to the direction of propagation <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This phenomenon is known as electromagnetic radiation, encompassing radio waves and visible light <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Describing Waves: Amplitudes, Phases, and Superposition

Classical wave descriptions lay the groundwork for quantum mechanics, introducing concepts like superposition, amplitudes, and phases <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

*   **Polarization:** Refers to the direction of oscillation of the electric field <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
    *   **Horizontally Polarized Light:** The electric field oscillates horizontally <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Its x-component can be described as `a * cos(2πft + φ)`, where `a` is the amplitude, `f` is the frequency, `t` is time, and `φ` is the phase shift <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   **Vertically Polarized Light:** The electric field oscillates purely in the up and down direction <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

*   **Superposition:** If two distinct waves satisfy [[maxwells_equations_and_electromagnetic_waves | Maxwell's equations]], their sum also forms a valid wave, at least in a vacuum <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This is due to the linearity of Maxwell's equations in a vacuum <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
    *   By adding horizontal and vertical components, various polarization states can be created. If components are in phase, the result is a diagonal oscillation <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
    *   If components are out of phase, the sum can trace out an ellipse <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
    *   **Circularly Polarized Light:** Occurs when components are 90 degrees out of sync with equal amplitudes <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. The phase of each component significantly affects how waves add together <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Basis and Polarizing Filters

The choice of directions to describe waves is called a **basis** <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. For example, waves can be described as a superposition of horizontal and vertical directions, or diagonal and anti-diagonal directions <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. The most convenient basis depends on the application <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

**Polarizing filters** absorb energy from electromagnetic oscillations in a specific direction <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Classically, a vertically oriented polarizer would absorb all energy from horizontal waves <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. If light passes through such a filter, what remains is the vertical component of the original wave <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

Classically, the energy of a wave is proportional to the square of its amplitude <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. If a wave is a superposition of components, its energy density is proportional to the sum of the squares of the amplitudes of its components (e.g., Ax² + Ay²), which aligns with the Pythagorean theorem <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. This implies that wave energy can be continuously adjusted <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

## Quantum Mechanics: Discrete Energy and Photons

However, late 19th and early 20th-century physicists observed that energy appears in [[discrete_energy_levels_and_photons | discrete amounts]] <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. The energy of an electromagnetic wave is an integer multiple of Planck's constant (`h`) times its frequency (`f`), i.e., `E = nhf` <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This means there is a minimal non-zero energy level for waves of a given frequency, `hf` <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

A **photon** is an electromagnetic wave with this minimal possible energy <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. The phenomenon of discrete energy levels is common in constrained waves (like harmonics in pipes or strings) but is peculiar for electromagnetic waves in free space <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

## Quantum Interpretation of Polarization and Superposition

The mathematical framework used to describe classical electromagnetic waves also applies to a photon <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. A photon, for instance, can have a 45-degree diagonal polarization, which can be described as a superposition of horizontal and vertical states, each with an amplitude and phase <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

### Probabilistic Interpretation

The interpretation of this superposition differs fundamentally in quantum mechanics. Classically, a diagonally polarized photon with amplitude `A` would have horizontal and vertical components with amplitudes `Ax` and `Ay`, where `A² = Ax² + Ay²` <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. This would imply half the energy in the horizontal component and half in the vertical component if `Ax = Ay = A / sqrt(2)` <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

However, waves of this frequency cannot have half the energy of a photon, as energy comes in discrete, indivisible chunks <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. Thus, the individual components with imagined amplitudes (e.g., `1/√2`) cannot exist in isolation <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

When a diagonally polarized photon is directed at a vertically oriented polarizing filter:
*   Classically, half its energy in the horizontal direction would be absorbed <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   Quantically, because energy comes in discrete [[discrete_energy_levels_and_photons | photon]] packets, the photon either passes through with all its energy or is absorbed entirely <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
*   Experimentally, about half the time the photon passes through entirely, and about half the time it is absorbed entirely, seemingly at random <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   If it passes through, its polarization is forced to align with the filter's direction <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

This phenomenon is analogous to [[schrodingers_cat_setup | Schrödinger's cat]] <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>: a superposition of states "collapses" into one definite state upon measurement, where the act of measurement forces the object to interact with an observer in a way where each state would behave differently <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

### The Three-Filter Experiment

A compelling demonstration involves multiple polarizing filters:
1.  **Two filters:** When two polarizing filters are rotated 90 degrees off from each other, light is completely blocked <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>. Photons passing the first (e.g., vertical) filter have 0% chance of passing a horizontally oriented filter <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
2.  **Three filters:** Inserting a third filter oriented at a 45-degree angle *between* the first two filters *lets more light through* <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
    *   50% of the photons passing the vertical filter will also pass through the diagonal filter <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
    *   Once they pass the diagonal filter, they are changed to have purely diagonal polarization <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.
    *   From this diagonal state, they have a 50-50 chance of passing through the final filter oriented at 90 degrees <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.
    *   Result: 25% of the original photons pass through all three filters (0.50 * 0.50 = 0.25) <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.

This outcome demonstrates that the middle filter forces the photons to change their states, a concept not explainable classically <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

### Amplitudes as Probabilities

For a photon whose polarization is 22.5 degrees off the direction of a filter:
*   Its horizontal component would have an amplitude of `sin(22.5°) ≈ 0.38` <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.
*   Its vertical component would have an amplitude of `cos(22.5°) ≈ 0.92` <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.
*   Classically, the horizontal component might be thought of as having energy proportional to `0.38² ≈ 0.15`, and the vertical to `0.92² ≈ 0.85` <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. Passing through a vertical filter would mean 15% of its energy is absorbed horizontally <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   Quantum mechanically, because light energy comes in discrete quanta, 85% of the time the photon passes through entirely, and 15% of the time it gets completely blocked <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.

The wave equations themselves do not change <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. A photon is still described as a superposition of oscillating components with amplitude and phase, often encoded using a single complex number <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>. The key difference is that while classically the squares of amplitudes indicate energy distribution, in quantum mechanics, the squares of those amplitudes tell you the *probabilities* that a photon will be found to have all of its energy in one direction or not <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. This also applies to circularly polarized photons and corresponding filters <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.

## Conclusion

Photons represent a quantum phenomenon where initial understanding was wave-based ([[maxwells_equations_and_electromagnetic_waves | Maxwell's equations]]), evolving to individual particles or quanta <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. Conversely, particles like electrons, initially understood as discrete packets, were later discovered to be governed by similar [[wave_nature_of_particles_and_de_broglies_hypothesis | wavy quantum mechanics]] <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.

In quantum mechanics, states are generally described as a superposition of multiple base states, the choice of which depends on the basis chosen <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. Each component of this superposition has an amplitude and a phase, often encoded as a single complex number, stemming from the underlying wave nature of these objects <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>. The chosen method of measurement determines a set of base states, and the probability of measuring a particle in one of these states is proportional to the squares of the amplitudes of these numbers <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.

The initial understanding of light as a wave, then as [[discrete_energy_levels_and_photons | discrete units]], paved the way for modern quantum mechanics, where the "weirdness" lies in the fact that waves come in discrete units, and particles are governed by wave equations <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>. This connection is further explored in topics such as [[bells_inequalities_in_quantum_mechanics | Bell's inequalities]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.