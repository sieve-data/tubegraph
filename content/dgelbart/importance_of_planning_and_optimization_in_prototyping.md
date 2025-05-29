---
title: Importance of planning and optimization in prototyping
videoId: RopgrECLSJc
---

From: [[dgelbart]] <br/> 

Effective planning and optimization are crucial throughout the prototyping process, from initial design to final finishing. Careful consideration of each step can save time, material, and effort, ensuring a high-quality final product.

## Initial Setup and Design Files

The prototyping process begins with design files, typically downloaded in formats like OR D or DXF, which are then converted for use (e.g., to V5 format) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Before cutting, essential parameters like material thickness and height must be accurately entered and set <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Error Correction and Repair

Even with careful planning, mistakes can occur during cutting, such as an extra cut or a misplaced hole <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Instead of scrapping the part, errors can often be repaired using [[applications_of_spot_welding_in_prototyping_and_manufacturing | spot welding]] <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. The technique involves placing a slightly oversized piece of material over the defect and melting it into the hole or slot <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. For slots, a strip slightly wider than the slot is used <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. The key is to overfill the defect slightly, allowing for sanding off excess material for a smooth finish <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## Bending Operations: Critical Planning Steps

Two critical considerations for accurate bending are the order of bends and part orientation <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Order of Bends
It is essential to determine the correct sequence for bending, as some parts can only be bent in a specific order to avoid interference with the machine's tooling <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Incorrect order can make subsequent bends impossible <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Part Orientation
Unless a part is symmetrical, choosing the correct side for bending is vital to avoid creating a mirror image, which would require extensive straightening <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Tooling Selection
The available tooling influences the bending strategy <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. For example, if bending long edges first would require a specific tool length that isn't available, it might be more efficient to bend shorter edges first using a more suitable tool <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Incorporating Fasteners Before Bending
If [[applications_of_spot_welding_in_prototyping and manufacturing | spot welding]] nuts or threaded inserts, it is often much easier to do so *before* bending the part <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This ensures better access and placement, even if it's possible to do it after <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

## Fitting Covers and Tolerances

Achieving a perfect fit for covers requires careful consideration of material thickness and bend radius <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

### Test Strips
A highly effective optimization strategy is to cut and bend a test strip of the same material and width as the cover <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. While CAD programs like SolidWorks with sheet metal options can calculate bend points <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>, performing a physical test bend and adjusting measurements ensures accuracy without wasting the entire part <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

### Design for Aesthetics and Durability
To avoid sharp edges and paint chipping, covers should always be recessed a few millimeters from the main part's end <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. This ensures impacts occur on a rounded corner, preserving the finish <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. For a tighter fit, it's often beneficial to bias the cover design to be slightly too tight <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

## Waterjet Cutting Optimization

When designing for [[prototyping_using_water_jet_cutting | waterjet cutting]], several features can be incorporated to enhance functionality and ease of assembly:

*   **Keyholes for Components**: Cut specific key or double-D shapes for components like toggle switches or power cords that have anti-rotation features. This ensures proper alignment and prevents rotation <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>.
*   **Knockouts**: Incorporate partially cut holes (knockouts) that can be punched out later if needed <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>. This provides flexibility, especially after the box is assembled <a class="yt-timestamp" data-t="00:19:13">[00:19:13]</a>.
*   **Integrated Brackets**: Design and cut all small internal brackets, clamps, or 'L' brackets from the same sheet as the main part <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. This ensures consistent material, allows for simultaneous painting, and perfect fit <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

## Considerations for Hole Placement and Bending

*   **Hole Registration**: Holes in a single plane will be perfectly registered by the waterjet machine, which is accurate to about 0.1 mm <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. However, registration is lost across bend lines due to variations in bend squareness and material distortion <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>. If possible, design to avoid holes across bend lines to maintain accuracy <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
*   **Hole Proximity to Bends**: Avoid placing holes too close to bend lines <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>. Round holes, in particular, will distort and become ugly if placed too near a bend line <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>. A minimum distance of 10-15 millimeters from any opening to a bend line is recommended to prevent distortion <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.

## Fastener Integration

Captive hardware (screws, nuts, studs that remain attached to the part) is highly important in electronic assemblies to prevent components from falling and shorting out circuit boards <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>. Think ahead and integrate all necessary captive hardware during the assembly process <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. Holes can be waterjet-cut to align with the heads of standard round-head studs for easy placement <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>.

## Preparation for Painting

Before sandblasting and painting, mask any areas where paint is not desired, such as threads, using silicone rubber plugs or Kapton tape <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>. Hangers for painting should be designed to be minimally visible and provide proper electrical grounding for powder coating <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>. Hangers cannot be reused once powder-coated <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.

## Powder Coating Process

A typical powder coating process involves baking in an oven at 235°C (380°F) for about 5 minutes to allow the paint to flow, then dropping the temperature to 190°C (350°F) for another 15 minutes for crosslinking and hardness <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>. While the two-step process is ideal, leaving it at the higher temperature for the full 20 minutes can still work, though it may result in a slight yellowing or warming of the color <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. Proper crosslinking is essential for paint hardness <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>. For inside corners during spraying, reducing the voltage (e.g., to 15 kilovolts) can help the electrostatic field overcome shielding <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>. Paint cannot be [[applications_of_spot_welding_in_prototyping_and_manufacturing | spot welded]] after it has been applied, as paint acts as an insulator <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.

## Final Assembly Optimizations

After painting and cooling, remove protective coverings from threads. Go over threads with a tap to clean them from welding residue and paint <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>. For covers, designing with keyholes and slots allows for sliding them on and off without removing screws, significantly streamlining assembly and maintenance <a class="yt-timestamp" data-t="00:33:06">[00:33:06]</a>.