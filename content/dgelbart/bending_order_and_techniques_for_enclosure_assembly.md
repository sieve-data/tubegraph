---
title: Bending Order and Techniques for Enclosure Assembly
videoId: RopgrECLSJc
---

From: [[dgelbart]] <br/> 

Creating a complete enclosure from beginning to end involves careful steps, from initial design and cutting to bending, assembly, and finishing.

## Initial Steps: Cutting and Preparation

Before bending, the design is downloaded, typically in an .RD or .DXF file, and converted to an .OV5 format <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The material is clamped down, its thickness is entered, and the cutting height is set to just touch the material, then lowered by half a millimeter <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

After cutting, the first step is to break any sharp edges to protect fingers and ensure parts lie flat, especially with intricate cut patterns <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Repairing Mistakes with Spot Welding

Mistakes, such as an extra cut or a misplaced hole, can be repaired without scrapping the part <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The technique involves placing a slightly oversized piece of material over the defect and melting it into the hole with a spot welder <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. For slots, a strip slightly wider than the slot (by about half a millimeter or a millimeter) is used <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. A high setting (e.g., number eight) is recommended for larger areas <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. The melted material will overfill the hole, allowing for sanding off the excess for a clean finish <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

> [!NOTE] Painting will show any imperfections, so careful sanding of repairs is important <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Bending Order and Orientation

When applying bends, two crucial factors must be considered:

1.  **Order of Bends:** The sequence of bends is critical, as some parts can only be bent in a specific order to avoid jamming the machine <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. For example, outer edges might need to be bent up first so the die can fit between them for subsequent inner bends <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
2.  **Part Orientation:** Unless the part is perfectly symmetric, bending it from the wrong side will result in a mirror image, which is a common mistake <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Always consider the desired final orientation of the box before beginning bends <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

For a typical enclosure, the periphery (outer edges) is bent first <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. The X-position for the bend is set and double-checked, along with the orientation <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Tooling and Bend Accuracy

The choice of tooling depends on the size of the bends. When deciding whether to bend long or short lines first, consider which available tooling will fit between the already bent sections <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Segmented tooling can be used for longer bends where a single die is not available <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Even with small gaps in segmented tooling, the bend can be accurate, and a second pass can be done if needed <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. More pressure may be needed for wider strips <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

## Trial Bends for Covers

When bending a cover that needs to fit precisely, it's challenging to account for material thickness and bend radius accurately <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. The recommended [[design_and_preparation_of_sheet_metal_enclosures | technique]] is to cut a test strip of the same width as the cover <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. CAD programs like SolidWorks Sheet Metal option can calculate bend lines, but a physical test bend is crucial <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. The test strip is bent, checked against the main enclosure, and adjustments are made to the bending parameters until a perfect fit is achieved <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

> [!TIP] It's generally better to bias the cover to be slightly too tight initially, as material can be removed or adjusted, but not added <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

The cover should always be recessed a couple of millimeters from the main body's edge <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>. This ensures a rounded edge on the main body is exposed, preventing sharp edges that can cause injury or lead to paint chipping <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

## Ensuring Squareness and Adding Internal Braces

If the main enclosure isn't perfectly square after bending, it can be flexed slightly into position <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. To ensure a perfect right angle, small braces can be spot-welded inside <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>. These are initially welded on only one side, then the enclosure is squared against a reliable square, and the other side of each brace is welded <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

## Design Considerations for Waterjet Cutting and Bending

When designing parts for a waterjet:

*   **Hole Registration:** Holes on the same plane will be perfectly registered (accurate to about 0.1 mm) <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. However, registration across bend lines is less accurate due to the nature of bending and material deformation <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.
*   **Hole Placement Near Bends:** A hole placed too close to a bend line (e.g., 3mm vs. 10mm) will twist and distort instead of bending cleanly <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>. Round holes are particularly susceptible to distortion <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>. If a hole must be near a bend, consider making it a 'U' shape where the flat lines are the bend line, as flats remain flat after bending <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. It's advisable to keep openings at least 10-15mm away from bend lines <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.
*   **Component-Specific Holes:** For components like toggle switches, cut specific keyholes or double-D shaped holes to prevent rotation <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
*   **Knockouts:** Incorporate knockouts for future expansion. These are incomplete holes held by two tabs that can be easily punched out later, even after the box is assembled <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
*   **Integrated Parts:** Cut all small internal brackets, clamps for cables, or other necessary bits from the same sheet as the main enclosure <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>. This ensures they are painted consistently and fit perfectly <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.

## Hardware and Finishing Touches

Before sandblasting and painting, all studs and nuts (captive hardware) should be installed <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>. Captive hardware is crucial in electronic assemblies to prevent screws from falling and shorting circuits <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>. Holes for studs can be drilled with the waterjet to help locate the head by feel <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>. Spot welding cannot be done after painting, as paint acts as an insulator <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.

For [[painting_and_finishing_techniques_for_metal_enclosures | painting]], areas where paint is not desired (e.g., studs, threads) should be covered with silicon rubber tubes or Kapton tape, which can withstand high temperatures <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>. Hangers are used to suspend the part in the oven, designed to minimize visible marks <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>. Hangers cannot be reused after powder coating as they lose their grounding capability <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.

After baking (e.g., 20 minutes at 275°C or 380°F), the protectors are removed from the threads, and the threads are cleaned with a tap to remove any spot welding residue or paint <a class="yt-timestamp" data-t="00:31:41">[00:31:41]</a>.

> [!IMPORTANT] When designing the enclosure, consider using keyholes and slots for attaching covers instead of traditional screw holes <a class="yt-timestamp" data-t="00:33:06">[00:33:06]</a>. This allows for quick removal and attachment of covers without fully unscrewing, saving significant time in R&D <a class="yt-timestamp" data-t="00:33:16">[00:33:16]</a>.