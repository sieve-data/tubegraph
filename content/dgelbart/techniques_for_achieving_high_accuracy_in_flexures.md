---
title: Techniques for achieving high accuracy in flexures
videoId: PaypcVFPs48
---

From: [[dgelbart]] <br/> 

Flexures are mechanical components that achieve motion through the elastic deformation of a material, rather than through traditional joints or bearings. When designing and fabricating flexures, especially for high-precision applications, specific [[high_precision_machining_techniques | techniques]] are employed to ensure accuracy in their movement and stability.

## Principles of Accurate Flexure Design
The accuracy of a flexure, particularly its ability to follow a straight line or maintain a fixed pivot point, depends on precise design and fabrication.

*   **Linear Motion Decoupling** For multi-stage flexures or those requiring precise linear motion, "wiggle bars" are used. These bars eliminate the effect of rotation around a pivot, effectively decoupling linear motion from rotational components <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. This ensures that the desired linear motion is maintained without unintended angular displacement <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
*   **Symmetry** A critical design principle for achieving perfectly straight-line motion in flexures is symmetry. If a design is symmetric, its movement inherently follows a straight line because there's no reason for it to deviate one way or the other <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.
*   **Stiffness in Undesired Directions** High accuracy flexures are designed to have high stiffness in all planes except the desired direction of motion. For example, a linear flexure will have high stiffness in lateral and rotational planes to prevent buckling or stretching, ensuring motion is confined to the intended axis <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>, <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>, <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.
*   **Exact Matching of Pivots** The linearity and smooth movement of a flexure depend on the exact matching of all its pivot points, or elastic pivots <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. For multi-spring designs, such as those made of [[materials_used_for_flexures_and_their_properties | Nitinol]], the "springs" must be precisely matched in both length and stiffness to ensure straight-line travel <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>, <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a>.

## Fabrication for High Accuracy
While a water jet allows for easy and rapid fabrication of [[types_of_flexures_and_their_design | flexures]] from a single block of material <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>, achieving very [[high_accuracy_in_machining | high accuracy]] requires additional steps:

*   **Pre-drilling and Reaming Holes** For flexures requiring straightness of travel in the range of one micron, a water jet alone is not accurate enough <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. It is essential to pre-drill and ream the critical holes <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. The water jet can then be aligned to one of these precisely drilled holes to make all other cuts <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>. This method can achieve a range of about 2 mm travel following a straight line to one micron <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
*   **Controlled Assembly for Composite Flexures** When working with materials like [[materials_used_for_flexures_and_their_properties | Nitinol]], which cannot be spot welded, individual pieces are trapped between stainless steel components. To ensure consistent spacing and alignment, a jig (a piece of metal acting as a spacer) should be inserted during welding, then removed, to maintain identical spacing everywhere <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.
*   **Avoiding Stress Concentrations** Any sharp transition in the design can lead to stress concentration problems <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>. For instance, when connecting flexible materials, edges should be bent around to prevent sharp transitions <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.

## Post-Assembly Correction
Even after careful fabrication, flexures can sometimes be adjusted to achieve ultimate straightness:

*   **Spring Modification** If a flexure is found to not travel in a perfectly straight line, the springs can be modified after assembly. This can involve grinding them slightly or clamping something onto them to change the stiffness of the pivot point <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>. Many flexures are corrected post-assembly if extreme straightness is required <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>.

## Materials for Stability
The choice of [[materials_used_for_flexures_and_their_properties | material]] is crucial for the stability and accuracy of a flexure, especially concerning temperature:

*   **Temperature Sensitivity** Aluminum, while commonly used for tutorial flexures, is very temperature sensitive, with a coefficient of thermal expansion of approximately 22-23 PPM per degree Celsius <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. Even radiated heat from a hand can cause a drift of 100 nanometers <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
*   **Stable Materials** For high stability, flexures should be cut from materials like Invar, quartz, or other materials that exhibit very stable properties with temperature <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
*   **High Elastic Range Materials** Materials such as [[materials_used_for_flexures_and_their_properties | Nitinol]] (nickel-titanium alloy) are ideal for flexures requiring larger travel, as they have an elastic range approximately ten times that of steel <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.

## Testing and Measurement for Accuracy
[[testing_and_measurement_for_flexure_systems | Testing and measurement]] are essential to verify the accuracy of flexure movement:

*   **Capacitance Gauge** A capacitance gauge can measure the position of a linear stage, allowing for precise observation of movement down to 10 nanometers per division without backlash <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>, <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>, <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
*   **Laser Pointer Method** A simple method to test straightness involves mounting a laser pointer on the moving part of the flexure and observing the laser spot on a wall across the room. A 1 milliradian error over 10 meters will result in a visible 10 mm deviation on the wall, allowing for measurement down to 50 microradians <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.
*   **Autocollimator** For more precise measurement of angular motion, an autocollimator can be used. By placing a mirror on the flexure's moving part, an autocollimator can measure sub-arcsecond deviations <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>. Deviation from linearity is always accompanied by angular motion, making angular measurement an effective way to determine straightness by integration <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.