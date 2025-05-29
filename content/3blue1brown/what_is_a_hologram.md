---
title: What is a hologram
videoId: EmKQsSDlaa4
---

From: [[3blue1brown]] <br/> 

A hologram is a special kind of recording taken on film that gives the illusion of looking through a window into a three-dimensional recorded scene [00:01:54]. When viewed, a hologram allows an observer to move their head and see the light play off the objects in different ways, as if a real 3D scene is present [00:00:03]. This is an illusion; in reality, only an empty table and a diverging laser beam shining on a piece of film are necessary to create this effect [00:00:17].

Unlike an ordinary photograph, which records a scene from a single viewing angle, a hologram makes available an entire continuum of differing perspectives [00:01:14]. Every optical detail from all these viewing angles is stored on a two-dimensional piece of film [00:01:35].

## [[history_of_holography_and_dennis_gabors_contributions | History of Holography]]

The principle behind holography was discovered by [[history_of_holography_and_dennis_gabors_contributions | Dennis Gabor]] in 1947 while he was working on methods for electron microscopy [00:02:03]. The fundamental insight reportedly came to him while watching a tennis match [00:02:11]. However, it wasn't until decades later, with the invention of lasers, that [[history_of_holography_and_dennis_gabors_contributions | holography]] became practical [00:02:15]. In 1971, Gabor won the Nobel Prize for his discovery [00:02:18].

## Types of Holograms

The simplest type of hologram, where the scene is visible only when illuminated with a laser from behind, is called a **transmission hologram** [00:02:25]. More advanced variants exist, such as the **white light reflection hologram**, which can be illuminated using ordinary light reflecting off of it [00:02:40].

## [[how_holograms_are_recorded_and_reconstructed | How Holograms Are Recorded]]

The goal of recording a hologram is to recreate the entire light field around a scene [00:04:24]. A light field is an incredibly complicated, undulating electromagnetic field surrounding objects, with specifics dependent on the optical properties of the objects and their illumination [00:04:37].

### Contrast with Ordinary Photography

Traditional photography, like with a pinhole camera, limits the exposure to a single viewing angle, causing a significant loss of information about the light field [00:04:14]. A hologram, however, aims to capture all the information from all possible viewing angles [000:04:19].

### Recording Phase Information

A key difference in [[how_holograms_are_recorded_and_reconstructed | holography]] is the recording of the light's **phase**, not just its amplitude (which determines exposure in ordinary photography) [00:05:49]. To record the phase, a second beam of light with the same frequency, called the **reference wave**, is shined onto the film alongside the light from the scene (the **object wave**) [00:07:03].

When these two waves [[interference_and_diffraction_in_holography | interfere]], the exposure pattern on the film becomes sensitive to phase shifts [00:07:30]. Where the object wave and reference wave are in sync, they constructively [[interference_and_diffraction_in_holography | interfere]], resulting in high exposure [00:07:12]. Where they are out of phase, they destructively [[interference_and_diffraction_in_holography | interfere]], leading to low exposure [00:07:23].

### The Setup

To achieve this, lasers are used because they produce light of a single frequency [00:08:08]. A laser beam is typically passed through a beam splitter; one half becomes the object wave, bouncing off the scene and hitting the film, while the other half becomes the reference wave, hitting the film directly without interacting with the scene [00:08:15]. These two waves then [[interference_and_diffraction_in_holography | interfere]] at the film's plane [00:08:32].

The resulting exposure pattern on the film looks nothing like the original objects; instead, it's a rapidly oscillating pattern of fringes [00:09:19]. This pattern is extremely sensitive to tiny movements [00:09:35]. A shift in object position by just a few hundred nanometers (comparable to the light's wavelength) can completely change the pattern [00:09:42]. This sensitivity requires a meditative stillness during the recording process, which can take several minutes [00:09:53].

### Film Resolution

For the holographic process to work, the film must have extremely high resolution [00:33:31]. While standard Polaroid film resolves around 10 lines per millimeter and microfilm over 100, holographic film can resolve many thousands of lines per millimeter [00:33:37]. This high resolution is necessary to faithfully record the very narrow spacing between interference fringes [00:33:58].

## [[how_holograms_are_recorded_and_reconstructed | How Holograms Are Reconstructed]]

The "magic" of [[how_holograms_are_recorded_and_reconstructed | holography]] occurs during reconstruction: if all objects are removed from the scene and only the reference beam is shined onto the exposed film, the light produced beyond the glass includes a complete recreation of the original object wave [00:10:28]. This recreation of light appears as if the scene were still present and the object beam were still shining [00:10:42].

### The Single Point Example: Fresnel Zone Plate

To understand reconstruction, consider the simplest object: a single point floating in 3D space [00:12:00]. When recorded, the radial wave from this point interferes with a plane reference wave (coming in perpendicular to the film) [00:13:31]. The resulting exposure pattern on the film is a series of concentric rings, known as a **Fresnel zone plate** [00:15:18]. The spacing of these rings encodes the 3D coordinates of the point; the center gives the XY coordinates, and the ring spacing determines the Z coordinate [00:16:16].

### Diffraction Grating Effect

When the reference wave is shined through this Fresnel zone plate pattern during reconstruction, each small region of the film acts like a [[interference_and_diffraction_in_holography | diffraction grating]] [00:16:42]. A [[interference_and_diffraction_in_holography | diffraction grating]] is a wall with evenly spaced slits that cause light to split into distinct beams [00:17:16]. The angle of these diffracted beams depends on the spacing of the slits and the wavelength of the light, as described by the equation `d sin(θ) = λ` (where `d` is slit spacing, `θ` is angle, and `λ` is wavelength) [00:22:21].

For the Fresnel zone plate, the spacing between its fringes (`D`) multiplied by the sine of the angle (`θ'`) from the object point to a point on the film equals the wavelength of the light (`λ`) [00:26:17]. When the reference wave illuminates the film, one of the resulting diffracted beams (a "first order" beam) satisfies the same angle relationship as the line connecting the film point to where the object was during recording [00:26:56].

### Recreating the Illusion

Because every point on the film emits a beam that matches what would have come from the original object, an observer moving their head sees a bright spot that shifts in just such a way as to create the illusion of a floating point of light behind the glass [00:27:36].

### Conjugate Image and Other Beams

When reconstructing a hologram, three main components of light emerge:
1.  **Zeroth order beam**: A scaled copy of the reference wave, appearing as a bright glow [00:28:07].
2.  **Object wave**: A scaled copy of the wave emanating from the object [00:29:08]. This is the desired reconstructed image [00:29:13].
3.  **Conjugate image**: A third wave that appears as a reflected, warped version of the original scene on the opposite side of the film [00:29:21].

In early [[history_of_holography_and_dennis_gabors_contributions | holography]], the conjugate image caused clarity issues [00:30:00]. This can be solved by shining the reference beam in at an angle during recording, which separates the reconstructed object wave from the conjugate image artifact [00:30:07].

## Mathematical Explanation (Complex Numbers)

A more formal explanation of [[how_holograms_are_recorded_and_reconstructed | holography]] involves treating light waves as the real component of rotating complex numbers [00:39:31]. This allows for elegant encoding of both the phase and amplitude of a wave [00:39:44].

If the sum of the reference wave (R) and object wave (O) is `R + O`, the film's exposure is proportional to the square of its amplitude: `|R + O|^2` [00:38:46]. During reconstruction, when only the reference wave `R` shines through the exposed film, the resulting wave on the other side can be expressed algebraically.

> [!INFO]
> The exposure of the film is proportional to `(R + O)(R + O)*`, where `*` denotes the complex conjugate [00:40:01].
> When the reference wave `R` shines through this, the output wave `W` is approximately `R * (R + O)(R + O)*` [00:41:00].
>
> Expanding this gives terms:
> - `R * R R*` (which is `|R|^2 R`): A scaled copy of the reference wave (zeroth order beam) [00:42:35].
> - `R * R O*`
> - `R * O R*` (which is `|R|^2 O`): A scaled copy of the object wave (the reconstructed image) [00:42:58].
> - `R * O O*` (which is `|O|^2 R`)
>
> The key term `|R|^2 O` represents the scaled copy of the original object wave, demonstrating how the hologram perfectly recreates the scene [00:42:58]. The term `R * R O*` (or `|R|^2 O*`) corresponds to the conjugate image [00:43:31].

This algebraic approach demonstrates that a copy of the object wave is produced on the plane immediately after the film, regardless of the object wave's complexity [00:44:10].

## [[applications_and_significance_of_holography | Applications and Significance of Holography]]

[[applications_and_significance_of_holography | Holography]] extends beyond simple transmission holograms. More advanced techniques include:
*   **White light reflection holograms**: Reproducing scenes with ordinary white light [00:36:06].
*   **Dynamic holograms**: Showing changes in a scene over time as the hologram is viewed from different angles [00:36:14].
*   **Computer-generated holograms**: Producing holograms from 3D computer graphics models [00:36:21].

The significance of [[applications_and_significance_of_holography | holography]] extends beyond art. For instance, the phenomenon of dark stripes appearing on an object when its hologram is superimposed shows how tiny shifts in position affect light [[interference_and_diffraction_in_holography | interference]] [00:37:09]. This principle is used in **interferometry**, a technique that uses wave [[interference_and_diffraction_in_holography | interference]] to measure extremely tiny distances [00:37:21]. Broadly, the ability to record and reproduce an entire wavefront is a useful tool for various scientific experiments [00:37:32].

[[history_of_holography_and_dennis_gabors_contributions | Dennis Gabor]] himself described his discovery as "an exercise in serendipity, the art of looking for something and finding something else" [00:38:00].