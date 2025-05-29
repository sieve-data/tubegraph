---
title: Quantum mechanics basics for beginners
videoId: MzRCDLre1b4
---

From: [[3blue1brown]] <br/> 

This article aims to provide foundational understanding for anyone interested in learning [[schrodingers_equation_and_quantum_mechanics | quantum mechanics]] more deeply <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. While [[schrodingers_equation_and_quantum_mechanics | quantum mechanics]] is a vast field <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>, understanding the fundamental concepts of waves and their mathematical description is crucial <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Many ideas from [[schrodingers_equation_and_quantum_mechanics | quantum mechanics]], such as describing states as [[polarization_and_superposition_in_quantum_mechanics | superpositions]] with various amplitudes and phases, emerge from the context of classical waves <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Light: The Starting Point

A natural starting point for [[schrodingers_equation_and_quantum_mechanics | quantum mechanics]], mirroring its historical development, is the study of light <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The pre-[[schrodingers_equation_and_quantum_mechanics | quantum]] understanding of light sets up many relevant wave mechanics <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Classical Description of Light

In the late 1800s, light was understood as waves in the electromagnetic field <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

#### Electric and Magnetic Fields
*   The **electric field** is a vector field where every point in space has an arrow indicating the direction and strength of the field <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. A charged particle in this field experiences a force in the direction of the arrow, proportional to the arrow's length and the particle's charge <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   The **magnetic field** is another vector field <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. When a charged particle moves through it, there's a force perpendicular to both its motion and the magnetic field's direction <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. The strength of this force is proportional to the particle's charge, velocity, and the magnetic field's arrow length <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

#### Maxwell's Equations and Electromagnetic Waves
[[the_classical_and_quantum_description_of_light | Maxwell's equations]], a culmination of 19th-century physics, describe how these two fields interact <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. They show that changes in one field cause changes in the other <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. For example, a loop in the electric field corresponds to an increasing magnetic field, and vice versa <a class="yt-timestamp" data-t="00:02:48">[00:03:08]</a>. This mutual interplay leads to propagating waves where the electric and magnetic fields oscillate perpendicular to each other and to the direction of propagation <a class="yt-timestamp" data-t="00:03:18">[00:03:30]</a>. This phenomenon is known as electromagnetic radiation, encompassing radio waves and visible light <a class="yt-timestamp" data-t="00:03:35">[00:03:41]</a>.

### Mathematical Description of Classical Waves

Ideas central to [[schrodingers_equation_and_quantum_mechanics | quantum mechanics]], like [[polarization_and_superposition_in_quantum_mechanics | superposition]], amplitudes, and phases, arise in the context of classical waves with clear motivation <a class="yt-timestamp" data-t="00:04:13">[00:04:21]</a>.

*   **Polarization**: Light waves can be characterized by their [[polarization_and_superposition_in_quantum_mechanics | polarization]], which describes the direction of the oscillating electric field <a class="yt-timestamp" data-t="00:04:43">[00:04:49]</a>. For instance, horizontally polarized light means the electric field oscillates horizontally <a class="yt-timestamp" data-t="00:04:43">[00:04:49]</a>.
*   **Mathematical Representation**: An oscillating electric field can be described by a cosine function <a class="yt-timestamp" data-t="00:04:53">[00:04:58]</a>:
    *   `A * cos(2πft + φ)`
    *   `A` is the **amplitude**, representing the maximum strength of the oscillation <a class="yt-timestamp" data-t="00:05:38">[00:05:44]</a>.
    *   `f` is the **frequency**, determining how many cycles occur per unit time <a class="yt-timestamp" data-t="00:04:58">[00:05:03]</a>.
    *   `t` is time.
    *   `φ` (phi) is the **phase shift**, indicating the wave's position in its cycle at time t=0 <a class="yt-timestamp" data-t="00:05:24">[00:05:28]</a>.
*   **Kets**: In quantum mechanics, column vectors describing components are often replaced by "kets" (e.g., `|horizontal⟩` for horizontal direction, `|vertical⟩` for vertical direction) <a class="yt-timestamp" data-t="00:05:48">[00:06:00]</a>.
*   **Superposition**: If two distinct waves satisfy [[the_classical_and_quantum_description_of_light | Maxwell's equations]] (in a vacuum), their sum also forms a valid wave <a class="yt-timestamp" data-t="00:06:23">[00:06:29]</a>. This is because [[the_classical_and_quantum_description_of_light | Maxwell's equations]] in a vacuum are linear <a class="yt-timestamp" data-t="00:06:48">[00:06:53]</a>. This new wave is called a [[polarization_and_superposition_in_quantum_mechanics | superposition]] of the original two <a class="yt-timestamp" data-t="00:07:16">[00:07:20]</a>.
    *   The resulting [[polarization_and_superposition_in_quantum_mechanics | superposition]] depends not only on the amplitudes of the components but also on their relative phases <a class="yt-timestamp" data-t="00:07:39">[00:08:04]</a>. For example, if horizontal and vertical components are 90 degrees out of phase with equal amplitudes, the result is circularly polarized light <a class="yt-timestamp" data-t="00:07:50">[00:07:54]</a>.
*   **Basis**: Waves can be described with respect to different sets of orthogonal directions, called a basis (e.g., horizontal/vertical or diagonal/anti-diagonal) <a class="yt-timestamp" data-t="00:08:21">[00:08:50]</a>. The choice of basis depends on the context, such as analyzing light passing through a polarizing filter <a class="yt-timestamp" data-t="00:08:50">[00:09:25]</a>.
*   **Energy in Classical Waves**: Classically, the energy of a wave is proportional to the square of its amplitude <a class="yt-timestamp" data-t="00:10:51">[00:10:54]</a>. For a wave described as a [[polarization_and_superposition_in_quantum_mechanics | superposition]] of horizontal (Ax) and vertical (Ay) components, its energy density is proportional to Ax² + Ay² (Pythagorean theorem) <a class="yt-timestamp" data-t="00:11:01">[00:11:11]</a>. In classical physics, this energy can be continuously adjusted <a class="yt-timestamp" data-t="00:11:31">[00:11:34]</a>.

## Transition to Quantum Mechanics

At the turn of the 20th century, physicists discovered that energy does not come continuously, but in discrete amounts <a class="yt-timestamp" data-t="00:11:38">[00:11:42]</a>.

*   **Quantization of Energy**: The energy of an electromagnetic wave always comes as an integer multiple of a specific constant (Planck's constant, `h`) times its frequency (`f`) <a class="yt-timestamp" data-t="00:11:46">[00:11:54]</a>.
    *   `E = nhf` (where `n` is an integer).
*   This means there is a minimal non-zero energy level for waves of a given frequency, `hf` <a class="yt-timestamp" data-t="00:12:09">[00:12:12]</a>. An electromagnetic wave cannot be made smaller than this minimal energy without being eliminated entirely <a class="yt-timestamp" data-t="00:12:15">[00:12:22]</a>.
*   An electromagnetic wave with this minimal possible energy is called a **photon** <a class="yt-timestamp" data-t="00:12:51">[00:12:56]</a>.
*   While energy quantization is common in constrained waves (like harmonics in pipes or instrument strings), its occurrence in electromagnetic waves in free space was unexpected <a class="yt-timestamp" data-t="00:12:39">[00:12:49]</a>.

## Quantum Superposition and Measurement

The mathematical description used for classical electromagnetic waves (amplitude, phase, [[polarization_and_superposition_in_quantum_mechanics | superposition]]) carries over to describing a photon <a class="yt-timestamp" data-t="00:12:56">[00:13:03]</a>. However, the interpretation differs significantly.

*   **Interpretation of Amplitudes**: Classically, the square of an amplitude indicates energy <a class="yt-timestamp" data-t="00:13:52">[00:13:56]</a>. In [[schrodingers_equation_and_quantum_mechanics | quantum mechanics]], since photons cannot be subdivided, the squares of the amplitudes tell you the **probabilities** that a given photon will be found to have all of its energy in one direction or another upon measurement <a class="yt-timestamp" data-t="00:18:46">[00:18:55]</a>.
    *   For example, a diagonally polarized photon can be described as a [[polarization_and_superposition_in_quantum_mechanics | superposition]] of horizontal and vertical states, each with an amplitude of `1/√2` <a class="yt-timestamp" data-t="00:13:06">[00:13:14]</a>. The square of this amplitude `(1/√2)² = 1/2` implies a 50% chance of being measured as horizontal and a 50% chance of being measured as vertical <a class="yt-timestamp" data-t="00:14:31">[00:14:35]</a>.
*   **Complex Numbers**: In [[schroder_s_equation_and_quantum_mechanics | quantum mechanics]], these components are often represented using [[complex_numbers_as_a_foundation_for_understanding_quaternions | complex numbers]] <a class="yt-timestamp" data-t="00:10:09">[00:10:15]</a>. This is a convenient mathematical way to encode both an amplitude and a phase with a single value <a class="yt-timestamp" data-t="00:10:18">[00:10:21]</a>.
*   **Measurement and Collapse**: When a photon in a [[polarization_and_superposition_in_quantum_mechanics | superposition]] state interacts with an observer (e.g., a polarizing filter), it is "forced to make a decision" <a class="yt-timestamp" data-t="00:15:05">[00:15:09]</a>. It will either pass through entirely (if its [[polarization_and_superposition_in_quantum_mechanics | polarization]] aligns with the filter) or be absorbed entirely <a class="yt-timestamp" data-t="00:14:48">[00:14:52]</a>. This process changes its state to align with the measured outcome, an analogy to the classic [[schrodingers_equation_and_quantum_mechanics | Schrodinger's cat]] setup, where a [[polarization_and_superposition_in_quantum_mechanics | superposition]] "collapses" into a definite state upon measurement <a class="yt-timestamp" data-t="00:15:14">[00:15:36]</a>.

> [!example]- Polarizing Filters Experiment
> If two polarizing filters are oriented 90 degrees apart, they block all light <a class="yt-timestamp" data-t="00:15:46">[00:15:55]</a>. However, inserting a third filter oriented at 45 degrees between them allows more light to pass through <a class="yt-timestamp" data-t="00:16:10">[00:16:15]</a>. This occurs because photons passing the first filter become polarized along its direction. When they encounter the 45-degree filter, they are forced to change their state, with 50% passing through and adopting the diagonal polarization <a class="yt-timestamp" data-t="00:16:18">[00:16:26]</a>. These diagonally polarized photons then have a 50% chance of passing the final 90-degree filter <a class="yt-timestamp" data-t="00:16:30">[00:16:35]</a>, resulting in 25% of the original light passing through all three <a class="yt-timestamp" data-t="00:16:44">[00:16:49]</a>. This demonstrates how the middle filter forces photons to change their states, a phenomenon not explainable classically <a class="yt-timestamp" data-t="00:16:49">[00:16:55]</a>. This phenomenon is related to [[bells_inequalities_in_quantum_mechanics | Bell's inequalities]] <a class="yt-timestamp" data-t="00:17:03">[00:17:06]</a>.

## Generalization of Quantum Concepts

The concepts observed with photons apply more broadly:
*   [[waveparticle_duality_and_de_broglie_hypothesis | Wave-particle duality]]: Many things traditionally considered discrete particles (like electrons) are governed by similar wavy [[schrodingers_equation_and_quantum_mechanics | quantum mechanics]] <a class="yt-timestamp" data-t="00:19:42">[00:19:52]</a>.
*   **Quantum States**: [[schrodingers_equation_and_quantum_mechanics | Quantum mechanical]] states are described as [[polarization_and_superposition_in_quantum_mechanics | superpositions]] of multiple base states <a class="yt-timestamp" data-t="00:19:56">[00:20:00]</a>, with the choice of basis depending on the context <a class="yt-timestamp" data-t="00:20:00">[00:20:03]</a>.
*   **Amplitude and Phase**: Each component in this [[polarization_and_superposition_in_quantum_mechanics | superposition]] has an amplitude and a phase, often encoded as a single [[complex_numbers_as_a_foundation_for_understanding_quaternions | complex number]] <a class="yt-timestamp" data-t="00:20:03">[00:20:07]</a>. The necessity of including phase arises from the underlying wave nature of these objects <a class="yt-timestamp" data-t="00:20:07">[00:20:10]</a>.
*   **Measurement Probabilities**: The probability of measuring a particle in one of its base states is proportional to the squares of the amplitudes of these numbers <a class="yt-timestamp" data-t="00:20:14">[00:20:25]</a>.

The "weirdness" of [[schrodingers_equation_and_quantum_mechanics | quantum mechanics]] is not that waves come in discrete units, but that particles are governed by wave equations <a class="yt-timestamp" data-t="00:20:33">[00:20:36]</a>.