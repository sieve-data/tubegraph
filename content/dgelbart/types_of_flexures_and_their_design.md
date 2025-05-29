---
title: Types of flexures and their design
videoId: PaypcVFPs48
---

From: [[dgelbart]] <br/> 

Flexures are mechanical components that achieve motion through the elastic deformation of a material, often cut from a single piece. They are particularly easy to manufacture, especially with tools like a water jet, which facilitates working with sheet metal <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Classical Linear Motion Flexure Stage

A classic flexure design often consists of a large block cut out to accommodate a linear stage, which can also incorporate a reduction lever to achieve a desired range of motion <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

**Design Components:**
*   **Reduction Lever:** A common configuration involves multi-stage reduction, such as a 5:1 reduction lever followed by a 3:1 lever, yielding a total 15:1 reduction <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Pivot:** These designs utilize elastic pivots <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Wiggle Bar:** This component is crucial in multi-stage flexures to eliminate the effect of rotation around a pivot, ensuring that linear motion is decoupled from rotational motion and transferred correctly to the next stage <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Micromet Screw:** Used in conjunction with a lever for fine adjustment <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

**Manufacturing and Accuracy:**
The entire flexure is typically cut from a single piece of material using a water jet <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. For very high accuracy, the holes for the elastic pivots should be pre-drilled and reamed, as the water jet itself may not be precise enough to achieve micron-level straightness of travel <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Aligning the water jet to these pre-drilled holes ensures the precise matching of all pivot points, which is critical for linear motion <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This method can achieve a travel range of about 2 mm with a straight line accuracy of one micron <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

**Materials for Stability:**
While aluminum is often used for tutorial or prototype flexures, it is highly temperature-sensitive (around 22-23 PPM per degree Celsius) <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. For stability, especially at nanometer precision, materials like [[materials_used_for_flexures_and_their_properties | Invar]], quartz, or other dimensionally stable materials are preferred <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Radiated heat from a hand can cause an aluminum flexure to drift by 100 nanometers <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

**Testing and Performance:**
A capacitance gauge can measure the position of the linear stage, demonstrating movement precision down to 10 nanometers per division without backlash <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Small Parallel Arm Flexure

Small flexures can be made, with arms as narrow as 3-4 mm being the limit for reliable cutting on a water jet <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Material:** [[materials_used_for_flexures_and_their_properties | Type 25 beryllium copper]] is very flexible and suitable for this design <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Assembly:** Nuts can be inserted into [[techniques_for_constructing_enclosures_and_flexures | water jet cut slots]], minimizing the need for machining or tapping <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Nitinol Linear Motion Flexure

Flexures are limited by the elastic range of their material <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. While steel has an elastic range of about 1%, [[materials_used_for_flexures_and_their_properties | Nitinol]] offers an elastic range approximately 10 times greater <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. While cutting a whole block from Nitinol is expensive, a sheet metal design can effectively utilize its properties <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

**Motion Characteristics:**
This type of flexure consists of a base, a moving part, and side bars that move half the distance of the moving part <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. It moves in a perfectly straight line due to its symmetric design <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. It exhibits high stiffness in planes perpendicular to the motion, as the strips would need to buckle or stretch, and also high stiffness against rotational motion <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. The only "soft" direction is the intended linear motion <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. A Nitinol flexure can achieve a significant travel, for instance, 20 mm <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

**Construction Techniques for Nitinol:**
*   Nitinol cannot be spot welded <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Instead, each piece is trapped between two smaller pieces of stainless steel <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   Edges are bent around to avoid sharp transitions and stress concentrations, which are critical for longevity <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   [[techniques_for_constructing_enclosures_and_flexures | Jigs]] (e.g., a metal spacer) are used during welding to ensure uniform spacing between the flexure elements, which is vital for straight travel <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. The straightness of travel depends on precisely matching the length and stiffness of the "springs" (flexing strips) <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

**Post-Assembly Correction:**
If a flexure does not travel in a perfectly straight line, it can be corrected by modifying the springs, such as grinding them or clamping something onto them to change the pivot point's stiffness <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

## Cross Hinge Flexure (Flex Pivot)

This is a common type of flexure used when a pivot is needed that does not require a full circular rotation <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Design:** It consists of two strips, one going one way and the other perpendicular to it <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Behavior:** For small angles, it behaves as if there were a true pivot point, meaning the center of rotation remains fixed <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Material:** Made of [[materials_used_for_flexures_and_their_properties | Nitinol]], it can bend up to 90 degrees <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

## Advantages of Flexures Over Traditional Methods

Flexures offer significant benefits compared to traditional slides and bearing-based mechanisms:
*   **No Lubrication:** Suitable for dirty environments, eliminating the need for maintenance <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **No Wear:** Designed correctly, flexures can have infinite life as there are no rubbing surfaces <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **No Backlash:** Unlike traditional stages that require preload and can develop looseness with wear, flexures inherently prevent play or looseness <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Cost-Effectiveness:** If a water jet is available, flexures can be made from scrap metal, effectively making them "free" and allowing for easy incorporation into designs as [[unique_machine_components_and_design | integral flexures]] <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

## Design for Infinite Life

For [[strength_versus_stiffness_in_mechanical_design | infinite life]] in flexures, it is crucial not to use the full elastic range of the material <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   **Elastic Range:** The deformation limit beyond which a material will permanently deform <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **Rule of Thumb:** To ensure infinite life, one should generally not exceed two-thirds of the elastic range, and ideally, stay below half of it <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. The exact percentage depends on the specific metal <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

## Testing and Measurement for Flexure Systems

[[testing_and_measurement_for_flexure_systems | Testing and measurement]] are crucial for achieving high accuracy in flexures.
*   **Laser Pointer Method:** A simple method to test straightness involves mounting a laser pointer on the moving part and observing the laser spot on a wall across the room (e.g., 10 meters away) <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. A 1 milliradian error will result in a 10 mm deviation on the wall, allowing for measurement down to 50 microradians by visual inspection <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Autocollimator:** For more precise measurements, an autocollimator can be used <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. By looking at the reflection from a mirror placed on the flexure, an autocollimator can measure sub-arcsecond angular motions <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Since a deviation from linearity is accompanied by an angular motion, measuring the angular motion and integrating it can determine the deviation from straightness <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.