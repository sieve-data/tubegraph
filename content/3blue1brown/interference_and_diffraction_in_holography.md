---
title: Interference and diffraction in holography
videoId: EmKQsSDlaa4
---

From: [[3blue1brown]] <br/> 

A hologram is a special type of recording on film that creates the illusion of looking through a window into a three-dimensional (3D) scene, where you can move your head and observe light interacting with objects in different ways [00:00:03]. Unlike an ordinary photograph, which records a scene from a single viewing angle [00:01:14], a hologram stores an entire continuum of differing perspectives and every optical detail from all viewing angles on a two-dimensional piece of film [00:01:18].

The underlying principle of holography, discovered by [[history_of_holography_and_dennis_gabors_contributions | Dennis Gabor]] in 1947, relies on capturing and recreating the full state of the light field around a scene [00:02:03], which includes both the amplitude and the phase of light waves [00:05:49].

## Recording a Hologram: Capturing Phase Through Interference

Ordinary photography, such as that from a pinhole camera, limits exposure to a single viewing angle and records only the amplitude (intensity) of light, losing information about the phase [00:04:14]. The exposure of film is proportional to the square of the amplitude of the light wave, meaning that a phase shift of half a wavelength makes no difference to the exposure [00:06:17].

To record the phase of light, [[how_holograms_are_recorded_and_reconstructed | holography]] uses a technique involving the [[how_holograms_are_recorded_and_reconstructed | interference]] of two coherent light beams [00:06:36]:
1.  **Object Wave**: Light that bounces off the scene and hits the film [00:08:18].
2.  **Reference Wave**: A second beam of light with the same frequency that does not interact with the scene but also hits the film [00:07:03].

When these two waves intersect at the film, they interfere with each other [00:07:09]. If the object wave is in sync with the [[how_holograms_are_recorded_and_reconstructed | reference wave]], they [[how_holograms_are_recorded_and_reconstructed | constructively interfere]], producing a wave with greater amplitude and strong film exposure [00:07:12]. If they are out of phase, they [[how_holograms_are_recorded_and_reconstructed | destructively interfere]], resulting in low amplitude and less exposure [00:07:23]. This process makes the film's exposure highly sensitive to phase shifts in the object wave [00:07:30].

For this interference to work, all light must have the same frequency, which necessitates the use of a laser [00:08:01]. A common setup involves splitting a laser beam, with one half forming the object wave and the other half forming the [[how_holograms_are_recorded_and_reconstructed | reference wave]] [00:08:15]. The resulting exposure pattern on the film is an "extremely subtle" [[how_holograms_are_recorded_and_reconstructed | interference]] pattern, which looks nothing like the original objects when magnified [00:09:12]. This pattern is also incredibly sensitive to tiny movements, with shifts comparable to the wavelength of light (a few hundred nanometers) able to completely change the pattern [00:09:35].

## Reconstruction of a Hologram: The Role of Diffraction

The magic of holography lies in its [[how_holograms_are_recorded_and_reconstructed | reconstruction]]: if the exposed film is illuminated *only* by the [[how_holograms_are_recorded_and_reconstructed | reference wave]], it produces a complete recreation of the original object wave, even without the physical objects present [00:10:28].

### Simplest Case: A Single Point Object

To understand this, consider the simplest hologram: that of a single point floating in 3D space [00:12:00]. The object wave from this point radiates radially [00:12:08]. If the [[how_holograms_are_recorded_and_reconstructed | reference wave]] is modeled as a plane wave perpendicular to the film [00:13:44], the [[how_holograms_are_recorded_and_reconstructed | interference]] pattern on the film consists of concentric rings [00:15:18]. This pattern is known as a **Fresnel zone plate** [00:15:47].
*   The center of the rings corresponds to the xy-coordinates of the point [00:16:16].
*   The spacing between the rings (fringes) uniquely determines the z-coordinate (distance from the object to the film) [00:16:19]. The fringes are closer together farther from the center [00:15:39].

### Diffraction Grating Mini-Lesson

The reconstruction relies on the phenomenon of [[how_holograms_are_recorded_and_reconstructed | diffraction]]. When a light wave shines onto a wall with many thin, evenly spaced slits (a diffraction grating) [00:17:16], the light passing through them creates a complex pattern on the other side [00:17:26].
*   Each slit acts as a point source of light [00:17:52].
*   With multiple slits, the waves from each slit interfere, producing bright spots where they [[how_holograms_are_recorded_and_reconstructed | constructively interfere]] and dark spots where they [[how_holograms_are_recorded_and_reconstructed | destructively interfere]] [00:18:41].
*   When observed from a distance, the light forms distinct beams, not just a blurred mess [00:20:36].
*   The angle (θ) of these distinct beams relative to the center is governed by the **diffraction equation**:
    $$d \sin \theta = n \lambda$$
    where `d` is the spacing between the slits, `λ` (lambda) is the wavelength of the light, and `n` is an integer representing the "order" of the beam (e.g., 1 for the first order beam) [00:22:53].
*   A narrower slit spacing (`d`) results in a larger angle (`θ`) for the diffracted beams [00:23:49].
*   Different wavelengths (`λ`) will diffract at different angles, which is why white light passing through a diffraction grating separates into a rainbow [00:24:52].

### Reconstructing the Point Hologram

The key insight is that a small region of the Fresnel zone plate created by the point object acts like a diffraction grating when the [[how_holograms_are_recorded_and_reconstructed | reference wave]] is shone through it [00:26:38].
*   The spacing of the fringes in the zone plate (`D`) at a given point, multiplied by the sine of the angle (`θ'`) between the line from that point to the original object and the perpendicular to the film, is equal to the wavelength of the light: `D sin θ' = λ` [00:26:17].
*   Since the exposed film acts as a diffraction grating with local spacing `D`, one of its diffracted beams will satisfy the diffraction equation `D sin θ = λ` [00:26:42].
*   This means that one of the diffracted beams (a "first order beam") from each point on the film exactly matches the angle of the light that would have come from the original object point if it were still there [00:26:56].

Therefore, for an observer, every point of the film emits a beam that aligns with the position of the original object [00:27:24]. As the observer moves their head, the apparent bright spot on the glass moves with them, creating the illusion of a floating point of light behind the glass [00:27:46].

## Holographic Artifacts and Nuances

During reconstruction, a hologram doesn't just produce the desired object wave [00:28:54]:
*   **Zeroth Order Beam**: A scaled copy of the [[how_holograms_are_recorded_and_reconstructed | reference wave]] that appears as a bright glow behind the film [00:29:01].
*   **Conjugate Image**: A third wave component that appears as a focused, reflected, and often warped version of the original object on the opposite side of the film from the intended reconstruction [00:29:19]. In early holography, this "muddying" effect was a significant challenge for [[history_of_holography_and_dennis_gabors_contributions | Dennis Gabor]] [00:29:57].
*   **Angling the Reference Beam**: By shining the [[how_holograms_are_recorded_and_reconstructed | reference beam]] at an angle during recording and reconstruction, these extraneous beams (zeroth order and conjugate image) can be spatially separated from the desired reconstructed object wave, allowing for a clean view [00:30:07].

Furthermore, for a complex scene, the [[how_holograms_are_recorded_and_reconstructed | interference]] pattern becomes extremely intricate, resembling random noise [00:32:28]. To faithfully record the very narrow fringe spacing, especially for light viewed from sharp angles, the holographic film must have extremely high resolution—many thousands of lines per millimeter, significantly more than standard film [00:33:31].

## Formal Explanation Using Complex Numbers (Technical Appendix)

The complete power of [[what_is_a_hologram | holography]] is best understood through a more formal mathematical framework involving complex numbers [00:35:39].

The combined wave shining on the film during recording can be represented as the sum of the [[how_holograms_are_recorded_and_reconstructed | reference wave]] `R` and the object wave `O`, both as complex values [00:38:46]. The exposure pattern, or opacity, of the film is proportional to the square of the amplitude of this combined wave, which can be expressed as `(R + O) * (R + O)*`, where `*` denotes the complex conjugate [00:38:56].

During [[how_holograms_are_recorded_and_reconstructed | reconstruction]], when only the [[how_holograms_are_recorded_and_reconstructed | reference wave]] `R` shines through the exposed film, the light wave immediately on the other side can be approximated as `R * (1 - Opacity)`. Substituting the expression for opacity and expanding the terms, the resulting wave can be seen to contain three main components [00:41:00]:
1.  A scaled copy of the [[how_holograms_are_recorded_and_reconstructed | reference wave]] itself: `(some real number) * R` [00:42:35]. This corresponds to the zeroth order beam [00:42:48].
2.  A scaled copy of the object wave: `(some real number) * O` [00:42:58]. This is the desired reconstructed image, containing all the complex optical properties of the original scene [00:43:08].
3.  A term involving the complex conjugate of the object wave: `(some real number) * O*` [00:43:31]. This represents the [[how_holograms_are_recorded_and_reconstructed | conjugate image]] [00:43:37].

This algebraic derivation demonstrates that a copy of the object wave `O` is intrinsically reproduced beyond the film, regardless of the object's complexity or the [[how_holograms_are_recorded_and_reconstructed | reference wave's]] shape, as long as the same [[how_holograms_are_recorded_and_reconstructed | reference wave]] (or a close approximation) is used for reconstruction [00:44:10]. The ability to store a 3D scene on a 2D film is possible because light obeys laws where its state in 3D space is sufficiently constrained by its value on a 2D boundary [00:45:50].

This understanding of [[how_holograms_are_recorded_and_reconstructed | interference]] and [[how_holograms_are_recorded_and_reconstructed | diffraction]] is fundamental to [[what_is_a_hologram | holography]] and has broader significance, particularly in [[applications_and_significance_of_holography | interferometry]], which uses wave [[how_holograms_are_recorded_and_reconstructed | interference]] to measure extremely tiny distances [00:37:21].