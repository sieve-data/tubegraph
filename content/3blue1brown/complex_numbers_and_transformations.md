---
title: Complex numbers and transformations
videoId: mvmuCPvRoWQ
---

From: [[3blue1brown]] <br/> 

[[introduction_to_complex_numbers | Complex numbers]] can be conceptualized in terms of transformations or actions on a plane, particularly through the lens of [[conceptualizing_complex_numbers | group theory]] <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>. This perspective views numbers not just as static values, but as dynamic operations that alter a mathematical object.

## Additive Group of Complex Numbers

One way to think of [[complex_numbers_in_mathematics | numbers]] as a group involves addition <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>. Consider all possible sliding actions on the complex plane <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>. Each complex number can be associated with a unique sliding action that moves the point at zero to that number's location <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>.

*   **Imaginary Numbers:** Numbers like `i`, `2i`, `3i` on the vertical line are associated with purely vertical sliding motions <a class="yt-timestamp" data-t="08:19:00">[08:19:00]</a>.
*   **General Complex Numbers:** A number like `3 + 2i` is associated with a diagonal sliding action that drags zero to that point <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>. This action is equivalent to a slide of 3 units to the right followed by a slide of 2 units vertically <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>.
*   **Composition:** Composing two sliding actions (applying one after the other) results in an overall slide that corresponds to the addition of the [[complex_numbers_in_discrete_math | complex numbers]] associated with the individual slides <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>. For example, a slide by `3 + 2i` followed by a slide by `1 - 3i` results in a slide equivalent to `(3+1) + (2-3)i` <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.
*   **Group Name:** This collection of all sliding actions on the complex plane is called the "additive group of complex numbers" <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>.
*   **Action Breakdown:** Any action in this group can be broken down into a purely real number action (horizontal slide) and a purely vertical slide (specific to [[complex_numbers_in_discrete_math | complex numbers]]) <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>.

## Multiplicative Group of Complex Numbers

Another way to think of [[complex_numbers_in_mathematics | numbers]] as a group involves multiplication <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>. Consider actions on the complex plane that stretch or squish it while keeping the origin (zero) fixed <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>.

*   **Real Numbers:** On the real number line, these actions correspond to stretching or squishing. For instance, stretching by a factor of 3 takes the point at 1 to 3 <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. Applying a stretch by 3 then a stretch by 2 results in a stretch by 6, demonstrating how multiplication relates to composing these actions <a class="yt-timestamp" data-t="11:21:00">[11:21:00]</a>.
*   **Complex Numbers:** Extending this to the complex plane, the group of actions includes not only stretching and squishing but also rotational components <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>.
    *   **The Imaginary Unit `i`:** The action associated with `i` (dragging the point at 1 to `i`) is a 90-degree rotation <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>. Applying this action twice (`i * i`) results in a 180-degree rotation, which is the action associated with -1 <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>. This gives a geometric interpretation for `i^2 = -1` <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>.
    *   **General Complex Numbers:** Any multiplicative action (associated with a [[complex_numbers_in_mathematics | complex number]]) can be broken down into a combination of a stretch/squish and a pure rotation <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>. Pure rotations are associated with points on the unit circle (a circle with radius 1 centered at the origin) <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.
*   **Action Breakdown:** Similar to the additive group, actions here can be broken down into a purely real number action (stretch/squish) and a pure rotation (specific to [[complex_numbers_in_discrete_math | complex numbers]]) <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>.

## Exponentiation as a Transformation

[[complex_numbers_and_imaginary_exponents | Exponentiation]] can be understood as a function that maps actions from the additive group to actions in the multiplicative group <a class="yt-timestamp" data-t="16:54:00">[16:54:00]</a>. This means:

*   **Inputs as Slides:** The input to an exponential function (e.g., `x` in `e^x`) can be thought of as a sliding action <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>.
*   **Outputs as Stretch-Rotate Actions:** The output of the function can be thought of as a stretching/squishing/rotating action <a class="yt-timestamp" data-t="17:08:00">[17:08:00]</a>.
*   **Preserving Structure (Homomorphism):** The key property of exponentiation (`b^(x+y) = b^x * b^y`) implies that adding inputs (composing sliding actions) corresponds to multiplying outputs (composing stretch-rotate actions) <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>. Such functions that preserve the group structure are called homomorphisms <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>.
*   **Mapping Complex Numbers:**
    *   Purely horizontal slides (real number inputs) map to pure stretching or squishing actions (positive real number outputs) <a class="yt-timestamp" data-t="18:40:00">[18:40:00]</a>.
    *   Purely vertical slides (inputs along the imaginary axis, multiples of `i`) map directly into pure rotations (outputs on the unit circle) <a class="yt-timestamp" data-t="18:53:00">[18:53:00]</a>.
*   **The Special Nature of *e***: For the exponential function `e^x`, a vertical slide of one unit (corresponding to the input `i`) maps to a rotation of exactly one radian <a class="yt-timestamp" data-t="20:15:00">[20:15:00]</a>. This ensures that a vertical slide of `π` units (input `πi`) maps to a rotation of exactly `π` radians (180 degrees), which is the multiplicative action associated with the number -1 <a class="yt-timestamp" data-t="20:39:00">[20:39:00]</a>. This provides a vivid interpretation of Euler's formula, `e^(πi) = -1` <a class="yt-timestamp" data-t="20:51:00">[20:51:00]</a>.

This perspective highlights that exponentials map additive actions perpendicular to the real number line (vertical slides) into multiplicative actions perpendicular to the real number stretching actions (pure rotations) <a class="yt-timestamp" data-t="21:45:00">[21:45:00]</a>.

## Visualizing the `e^x` Transformation

The function `e^x` can be visualized as a [[understanding_complex_functions_and_their_transformations | transformation of the complex plane]] <a class="yt-timestamp" data-t="22:21:00">[22:21:00]</a>:

1.  **Rolling to a Cylinder:** Imagine rolling the complex plane into a cylinder, where all vertical lines wrap into circles <a class="yt-timestamp" data-t="23:51:00">[23:51:00]</a>.
2.  **Mapping to the Plane:** Then, this cylinder is "smooshed" onto the plane around zero. Each of the original vertical lines corresponds to one of the resulting concentric circles, which are spaced out exponentially <a class="yt-timestamp" data-t="23:57:00">[23:57:00]</a>.