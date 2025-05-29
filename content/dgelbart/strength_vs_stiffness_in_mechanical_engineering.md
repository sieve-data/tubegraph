---
title: Strength vs Stiffness in Mechanical Engineering
videoId: MtxA20Q-Uss
---

From: [[dgelbart]] <br/> 

In mechanical engineering, it is crucial to understand the distinction between strength and stiffness <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. While both are important properties, their prioritization depends heavily on the application.

## Strength vs. Stiffness: Core Differences

*   **Strength** refers to a material's ability to withstand an applied load without failure or permanent deformation <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
*   **Stiffness** refers to a material's resistance to elastic deformation under an applied load <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Applications Prioritizing Strength
Classical mechanical engineering often prioritizes strength <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Examples include:
*   Bridges <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>
*   Steel cables <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>
*   Airplanes <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>

### Applications Prioritizing Stiffness
In instruments and machine tools, stiffness is the primary concern <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Microscopes**: A microscope frame, though supporting only a [[unique_properties_of_glass_in_engineering_applications | glass]] slide, is designed to support a ton to ensure it remains completely stiff when touched and does not flex <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **Lathe Beds**: The bed of a lathe, typically made of [[comparing_the_strength_and_aesthetic_of_brazed_assemblies_to_traditional_cast_iron | cast iron]], can support 10 tons, far exceeding the 10 kg weight of a typical workpiece. This overdesign is for stiffness, which determines its dimension, not strength <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Measurement Tools**: Tools used for checking squareness must be exceptionally stiff to prevent deflection during measurement, even if they bear no significant force <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Stiffness Demonstration

To illustrate the critical difference, a demonstration compares the stiffness of a solid [[properties_and_uses_of_different_metals_particularly_stainless_steel | aluminum]] bar with an identical bar cut in two and held together by rubber bands <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Setup
1.  One end of the bar is rounded to prevent rocking <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
2.  The bar is rested on three points to eliminate play <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
3.  A gauge is set to zero after preloading the bar <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
4.  A block of steel is used as a load <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### Test Results
*   **Solid Bar**: Under load, the solid bar showed a deflection of 12 microns <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Cut Bar with Rubber Band**: The cut bar, reassembled with rubber bands, showed a deflection of 7 microns <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

### Surprising Conclusion
The bar held together by a rubber band was significantly stiffer than the solid bar, nearly twice as stiff <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

#### Explanation
This counterintuitive result occurs because as long as the two pieces of the cut bar do not separate, the section where they are joined acts as a solid piece <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. This joined section effectively doubles the thickness at that point, making it theoretically eight times stiffer than the original bar due to its increased cross-section <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Therefore, despite having no strength beyond that of the rubber band, its stiffness is remarkably high <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Design Philosophy and Considerations
The distinction between strength and stiffness also influences broader design choices.

### Precision vs. Feel
*   **High Precision**: For high-precision applications requiring brute-force accuracy, parts often need to be carefully machined, lapped, or scraped <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. This often involves [[techniques_for_measuring_and_ensuring_precision_in_mechanical_parts | line boring]] or precision boring after assembly <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   **Adjustable Precision with Feel**: For applications where absolute position is adjustable, but a "precision feel" is desired, simple solutions can be effective <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. For example, placing a ball bearing between an adjusting screw and a surface makes the adjustment feel smooth, as the screw's rough end slides on the ball's smooth surface <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. The use of precise standard parts like dowel pins or roller bearing pins can also provide precision without complex machining <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

### Instrument vs. Machine Tool Design
*   **Instrument Design**: Instruments, which typically bear no significant load but require high accuracy, can utilize [[materials_and_construction_methods_for_precision_machinery | kinematic mounts]] <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>. These mounts are convenient for easy removal and replacement and self-adjusting features <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>. They rely on minimal contact points, which reduces the need for extensive lapping <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
*   **Machine Tool Design**: Machine tools, which carry heavy loads and demand immense stiffness, cannot use kinematic mounts <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. Kinematic mounts inherently create point contacts, leading to infinite pressure and potential indentation under heavy loads <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. Machine tool design relies on overconstrained designs or full surface bearings to distribute loads effectively <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.