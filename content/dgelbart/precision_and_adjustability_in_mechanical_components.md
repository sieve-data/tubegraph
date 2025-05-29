---
title: Precision and adjustability in mechanical components
videoId: MtxA20Q-Uss
---

From: [[dgelbart]] <br/> 

In mechanical engineering, particularly for instruments and machine tools, [[Strength versus stiffness in mechanical design | stiffness]] is often a more critical design consideration than strength <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. While strength is paramount for structures like bridges or airplanes <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>, precision components demand high stiffness to prevent deflection under minimal loads <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Stiffness vs. Strength

Components in precision instruments, such as a microscope frame or a lathe bed, are significantly "overdesigned" for strength relative to the loads they carry <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. A microscope frame, capable of supporting one ton, might only hold a glass slide, but its heavy construction ensures it remains completely stiff and doesn't flex when touched <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Similarly, a cast iron lathe bed, able to support 10 tons, holds a workpiece weighing only 10 kilograms, because its stiffness, not its strength, determines dimensional accuracy <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Demonstration of Stiffness

To illustrate the difference, consider comparing a solid aluminum bar to an identical bar cut in two and held together with rubber bands <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. While the strength of the rubber-banded bar is minimal, its stiffness can be surprising <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

In a test where an equal load was applied to both:
*   The solid aluminum bar deflected 12 microns <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   The two-piece bar, held by rubber bands, deflected only 7 microns <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

This counter-intuitive result occurs because as long as the two pieces don't separate, the middle section behaves like a solid piece. Being twice as thick as the original bar, that section is theoretically eight times stiffer <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Thus, a low-strength assembly can be significantly stiffer than a solid component <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Mounting Components

### Pulleys and Shafts

When mounting pulleys or shafts, avoiding damage and ensuring reusability are key:
*   **Set Screws**: If using set screws, file flats on the shaft to prevent dents that hinder removal <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. For higher torque, cross-drilling with a pin is recommended <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Flexure-Based Clamping**: A superior method, especially if using a water jet, involves a split housing that flexes to grip the shaft <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This system distributes the load evenly and doesn't mark the shaft <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Bearings and Alignment

Bearings inherently have play <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>, as they are designed to work in preloaded pairs <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. To eliminate play in a shaft assembly, bearings must be preloaded against each other <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This can be achieved by:
*   Using a sleeve on the shaft to push bearings together from the housing <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   Inserting a spring washer or wave washer, which can be squeezed flat to provide consistent preload even if the housing isn't perfectly accurate <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

For thin sheet metal housings, beefing up the wall with additional plates (e.g., water jet cut) is necessary to contain the bearing <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. Achieving [[high accuracy in machining | high accuracy in machining]] alignment for these plates presents a challenge:
*   **Self-Aligning Fasteners**: Welded nuts with self-aligning holes and flathead screws with a taper can pull parts into position for lower precision applications <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Line Boring**: For [[high accuracy in machining | high accuracy in machining]] applications, the assembly must be line bored. This involves drilling through both pieces at once after assembly, or using a boring head with a long tool to bore both holes in a single mounting <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   **Snap Rings**: For internal steps in bored holes, a groove can be cut for a snap ring to stop the bearing <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Post-Assembly Alignment and Epoxy**: For less critical applications, pre-bored plates can be aligned after assembly and epoxied in place, though they may shift if knocked <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. Using pieces with a bored step that seats the bearing is more secure <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### Bearing Sourcing and Fit

*   **Cost-Effective Bearings**: Skateboard bearings (8mm ID x 22mm OD) are an outstanding buy due to their mass production, costing about 25 cents even at high quality levels (e.g., ABEC 5 comparable) <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. Most general-purpose bearings are sufficient for 99% of jobs <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.
*   **Fixing Loose Fits**: For loose fits between bearings and shafts or housings, a drop of Loctite can fill the gap and set overnight <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. To remove a Loctited part, heat it to about 150°C with a heat gun to soften the adhesive <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

## Design Philosophy

The hierarchy of material choice for design prioritizes ease and cost:
1.  **Wire**: The easiest and cheapest material. It generates zero waste, requires minimal finishing, and can be bent into complex shapes by [[customization_and_tooling_for_precision_bending | CNC wire bending machines]] without special tooling <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
2.  **Sheet Metal**: If wire isn't suitable, sheet metal is the next option. It excels in applications requiring adjustable and lockable mechanisms, such as a multi-disk clutch, due to the friction multiplication across multiple surfaces <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
3.  **Solid**: Machining from solid is considered when wire or sheet metal are not viable <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

## Achieving Precision and Adjustability

When designing with solid components, consider whether [[high accuracy in machining | brute force precision]] is needed or if adjustability can suffice <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.

*   **"Precision Feel"**: To achieve a smooth, precise feel without extreme manufacturing precision, insert a precision part. For example, placing a ball from a ball bearing between an adjusting screw and the surface it acts upon provides a completely smooth adjustment feel, even if one surface is rough <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
*   **Off-the-Shelf Precision**: Instead of machining shafts to high precision, use readily available precise pins like dowel pins or roller bearing pins <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

## Instrument vs. Machine Tool Design

A fundamental distinction exists between designing for instruments and machine tools:
*   **Instruments**: Typically carry no significant load but demand [[high accuracy in machining | high accuracy in machining]] <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. They can utilize kinematic mounts, which rely on point contacts <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.
*   **Machine Tools**: Must sustain heavy loads, possess immense [[Strength versus stiffness in mechanical design | stiffness]], and be wear-resistant <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. They cannot use kinematic mounts because point contacts would result in infinite pressure and indentation under load <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>. Instead, they rely on over-constrained designs or full surface bearings <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

## Product Design Considerations

For products intended for long life and production, additional factors come into play:
*   **Lifetime Cost**: Parts should be easily removable for maintenance and proper access <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>.
*   **Electrical Cabling**: Thoroughly plan cable routing, plugs, and strain relief within the design <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>. If combining hydraulics/water with electrical systems, position hydraulic tubing below electrical wiring to prevent damage from leaks <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

## Aesthetic Aspect

A design that is 100% functional is often inherently beautiful <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. Removing all unnecessary material (e.g., making a bow thinner at the ends where stress is lower) results in an intuitive and aesthetically pleasing form <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.