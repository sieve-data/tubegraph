---
title: Maxwells equations and electromagnetic waves
videoId: MzRCDLre1b4
---

From: [[3blue1brown]] <br/> 

Light is a fundamental starting point for understanding quantum mechanics <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. A deep understanding of waves and their mathematical description is essential for learning quantum mechanics <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Many core concepts in quantum mechanics, such as describing states as superpositions with various amplitudes and phases, originate from classical wave phenomena <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Studying the pre-quantum understanding of light helps lay relevant foundations for wave mechanics <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Classical Understanding of Light in the 19th Century

By the late 1800s, light was understood as waves in the [[electromagnetic_waves_and_charged_particles | electromagnetic field]] <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### The Electromagnetic Field
*   **Electric Field**: A vector field where every point in space has an arrow indicating the direction and strength of the field <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. If a charged particle is placed in this field, it experiences a force in the direction of the arrow, proportional to the arrow's length and the particle's charge <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Magnetic Field**: Another vector field <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. When a charged particle moves through a magnetic field, it experiences a force perpendicular to both its direction of motion and the magnetic field's direction <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. The strength of this force is proportional to the particle's charge, its velocity, and the length of the magnetic field arrow <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Maxwell's Equations
The culmination of 19th-century physics understanding of these fields came with [[maxwells_equations_and_vector_calculus | Maxwell's equations]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. These equations describe how the electric and magnetic fields can cause changes to each other <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   [[maxwells_equations_and_vector_calculus | Maxwell's equations]] indicate that when electric field arrows form a loop around a region, the magnetic field increases inside that region perpendicular to the loop's plane <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   Symmetrically, a loop in the magnetic field corresponds to a change in the electric field within it, perpendicular to the loop's plane <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   This mutual interplay, where changes in one field cause changes in neighboring regions of the other, leads to propagating waves <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. In these waves, the electric and magnetic fields oscillate perpendicular to each other and to the direction of propagation <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   This phenomenon is what "electromagnetic radiation" refers to, including radio waves and visible light <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. The understanding that light is an [[electromagnetic_waves_and_charged_particles | electromagnetic wave]] was surprising in Maxwell's time <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

## Mathematical Description of Classical Waves

Waves can be described mathematically, and concepts from this classical description are core to quantum mechanics <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Wave Components
*   **Polarization**: Describes the oscillation direction of the electric field <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. For example, if the electric field oscillates horizontally, the light is horizontally polarized <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   A horizontally polarized wave can be described using a cosine function of frequency `f` and time `t`, with an amplitude `a` and a phase shift `phi` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
    *   Vertical polarization similarly uses a cosine function for the vertical component <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Amplitude**: Represents the strength or maximum displacement of the wave <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Phase Shift**: Tells where the wave is in its cycle at time `t=0` <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### Superposition of Waves
In a vacuum, [[maxwells_equations_and_vector_calculus | Maxwell's equations]] are linear [[differential_equations_in_physics | differential equations]] <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. This means that if two distinct waves are solutions to these equations, their sum is also a valid wave <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This new wave is called a [[polarization_and_superposition_in_quantum_mechanics | superposition]] of the first two <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   [[polarization_and_superposition_in_quantum_mechanics | Superposition]] essentially means sum, or weighted sum, including amplitudes and phase shifts <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   If horizontal and vertical components are out of phase, their superposition can trace out an ellipse <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. When phases are 90 degrees out of sync and amplitudes are equal, this results in circularly polarized light <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   The phase is crucial because it affects how waves add together <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Basis
Waves can be described with respect to different directions, known as a "basis" <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. For example, a wave can be a [[polarization_and_superposition_in_quantum_mechanics | superposition]] of horizontal and vertical components, or diagonal and anti-diagonal components <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. The choice of basis depends on the context, such as analyzing light passing through a polarizing filter <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

### Energy of Classical Waves
Classically, the energy of a wave is proportional to the square of its amplitude <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. If a wave is described as a superposition of horizontal (Ax) and vertical (Ay) components, its energy density is proportional to Ax² + Ay² <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. This aligns with the Pythagorean theorem <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. Classically, this energy can be continuously dialed up or down by changing the wave's amplitude <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

## Transition to Quantum Mechanics and Photons

Experiments in the late 19th and early 20th centuries revealed that the energy of [[electromagnetic_waves_and_charged_particles | electromagnetic waves]] actually comes in discrete amounts, not continuously <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   The energy is always an integer multiple of a specific constant (Planck's constant, `h`) times the wave's frequency (`f`) <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This means energy is traded in integer multiples of `hf` <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
*   There is a minimal non-zero energy level for waves of a given frequency, `hf` <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. An [[electromagnetic_waves_and_charged_particles | electromagnetic wave]] with this minimal energy is called a "photon" <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   This quantization of energy in free space is unusual for waves, which typically show such discrete energy levels (harmonics) only when constrained (e.g., in pipes or instrument strings) <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

### [[relationship_between_classical_and_quantum_waves | Relationship between Classical and Quantum Waves]]
The mathematical description used for classical [[electromagnetic_waves_and_charged_particles | electromagnetic waves]] carries over to describing a photon <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
*   A photon's [[polarization_and_superposition_in_quantum_mechanics | polarization]], such as 45-degree diagonal, can still be described as a [[polarization_and_superposition_in_quantum_mechanics | superposition]] of horizontal and vertical states, each with an amplitude and phase <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   However, the interpretation of this [[polarization_and_superposition_in_quantum_mechanics | superposition]] differs <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. Since a photon cannot have "half" its energy <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>, the components of its superposition (e.g., with amplitudes like 1/√2 for horizontal and vertical) cannot exist in isolation <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   When a diagonally polarized photon interacts with a vertically oriented polarizing filter, it either passes through entirely or is absorbed entirely, with an apparent randomness <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. This measurement "forces" the photon to change its [[polarization_and_superposition_in_quantum_mechanics | polarization]] to align with the filter's direction if it passes <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. This is analogous to wave function collapse <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

### Probabilistic Interpretation of Amplitudes
The squares of the amplitudes of each component in a quantum superposition, at the minimal non-zero energy level, tell you the probabilities that a given photon will be found to have all of its energy in one direction or not <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. For example, if a photon has amplitudes of 0.38 for horizontal and 0.92 for vertical (where 0.38² + 0.92² ≈ 1), passing it through a vertical filter means it will pass 85% of the time (0.92²) and be blocked 15% of the time (0.38²) <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

### Complex Numbers in Quantum Mechanics
In quantum mechanics, the components of a superposition are often given using a single complex number, which conveniently encodes both the amplitude and the phase with a single value <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. The use of complex numbers in quantum mechanics is a direct result of its underlying wavy nature and the need to encapsulate amplitude and phase for each direction <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

### Generalization
Photons are one example of a quantum phenomenon, initially understood as a wave due to [[maxwells_equations_and_vector_calculus | Maxwell's equations]], and later as individual particles or quanta <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. Similarly, particles like electrons, initially understood as discrete packets, were discovered to be governed by wavy quantum mechanics <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.

Quantum mechanical states are generally described as a [[polarization_and_superposition_in_quantum_mechanics | superposition]] of multiple base states, with choice in basis <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. Each component has an amplitude and phase, often encoded as a single complex number, due to the wave nature of these objects <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>. The choice of measurement determines a set of base states, and the probability of measuring a particle in one of these states is proportional to the squares of the amplitudes of these numbers <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.