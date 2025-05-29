---
title: Designing enclosures using waterjet cutting
videoId: RopgrECLSJc
---

From: [[dgelbart]] <br/> 

Creating a complete enclosure from start to finish involves several steps, from initial design and cutting to bending, hardware integration, and finishing processes like painting <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The use of a [[waterjet_cutter_usage_and_benefits | waterjet cutter]] significantly streamlines many of these steps, allowing for precision and flexibility in [[design_and_fabrication_of_enclosures | design and fabrication of enclosures]].

## Initial Design and Setup

The process begins with the design file, which can be downloaded in formats like DRD or DXF and then converted for use with the [[waterjet_cutter_usage_and_benefits | waterjet cutter]], typically to a V5 file <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Once the file is ready, the material is clamped down, and its thickness is entered into the machine <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The height of the waterjet nozzle is set by touching the material and then moving it half a millimeter above <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Post-Cutting Processing

After cutting, the part needs initial finishing:

*   **Breaking Sharp Edges** The first step is to break sharp edges to protect fingers and ensure the material lies flat, especially in areas with intricate patterns <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Repairing Mistakes with Spot Welding**
    *   Mistakes like extra or misplaced holes or cuts can be repaired using a spot welder, avoiding the need to scrap the part <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
    *   The technique involves placing a slightly oversized piece of material above the defect and melting it into the hole <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. For an extra slot, a strip slightly wider than the slot is cut and melted in <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   High current settings are used for larger areas <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. After melting, the excess material is cut off and corners touched up, or sanded for a perfect finish <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. The plug can be any shape, as the high current will flow and melt it to overfill the hole, allowing for sanding off the excess <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## Bending and Forming the Enclosure

[[bending_techniques_and_considerations_for_metal_enclosures | Bending techniques and considerations for metal enclosures]] are crucial for a successful enclosure:

*   **Order of Bends** It is critical to think through the order of bends, as some parts can only be bent in a specific sequence to avoid interference with the bending machine <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Symmetry and Mirror Images** A common mistake is bending a non-symmetric part incorrectly, resulting in a mirror image. Careful consideration of the desired final orientation is necessary <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Bending Process** Typically, the periphery is bent first <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. When deciding which sides to bend first (e.g., short or long), consider the available tooling to ensure it fits between already bent edges <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Segmentation of tooling can be used for longer bends <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Cover Fit and Test Strips** To ensure the cover fits perfectly, cut a test strip of the same width as the cover <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. CAD programs like SolidWorks Sheet Metal can calculate bend locations <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. Adjustments are made based on test bends to account for material thickness and bend radius <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   **Avoiding Sharp Edges** Always recess the cover by a couple of millimeters from the main enclosure's edge. This creates a rounded, safer edge and prevents paint from chipping off sharp corners <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   **Ensuring Squareness** Braces can be spot welded on one side, then the part adjusted against a square, and the other side of the braces welded to ensure the enclosure is perfectly square <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

## Integrating Hardware and Design Considerations

*   **Pre-Bend Hardware** Spot welding threaded inserts or nuts is much easier before final bends are made, even if the welder can accommodate bent parts <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Captive Hardware** It is highly recommended to use captive hardware (nuts, studs) in electronic assemblies to prevent screws from falling and shorting circuits <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>. Holes for standard round head studs can be drilled with the [[waterjet_cutter_usage_and_benefits | waterjet cutter]] to allow for tactile seating of the stud head <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>.
*   **Leveraging Waterjet Capabilities**
    *   **Keys and Non-Circular Holes:** Utilize the [[waterjet_cutter_usage_and_benefits | waterjet cutter]] to cut keys for toggle switches or double-D shaped holes for power inlets, accommodating components designed with anti-rotation features <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.
    *   **Knockouts:** Create knockouts (partially cut holes held by small tabs) for future additions, allowing for easy punching out of holes even after assembly <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.
    *   **Internal Brackets and Clamps:** Design and cut all necessary internal brackets, cable clamps, or L-brackets from the same sheet as the main enclosure. This ensures they are painted consistently and fit perfectly <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
*   **Hole Registration and Bend Lines**
    *   Holes on a single plane will be perfectly registered due to the [[waterjet_cutter_usage_and_benefits | waterjet cutter]]'s accuracy (around 0.1 mm) <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
    *   However, registration is lost across bend lines due to material stretch and bend squareness variability <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.
    *   Avoid placing holes very close to bend lines (e.g., less than 10-15 mm away), as this can cause distortion, especially for round holes <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>. If a hole must be near a bend, design it with a flat edge along the bend line to minimize distortion <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.

## Finishing: Sandblasting and Painting

*   **Pre-Paint Preparation** Before sandblasting and painting, mask any areas where paint is not desired (e.g., threads) using silicone rubber tubes or Kapton tape <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>. Spot welding cannot be done after painting, as paint is an insulator <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.
*   **Hanging for Painting** Use hangers that won't leave visible marks on the finished part <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>. Hangers cannot be reused for painting once powder-coated, as they need to ground the part <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.
*   **Powder Coating Process**
    *   Start by reducing voltage (e.g., 15 kilovolts) for inside corners to allow the electrostatic field to penetrate <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>.
    *   Apply paint to the rest of the surface (20-50 kilovolts) <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>. A proper enclosure for painting made of non-metal material prevents overspray onto other metal objects, ensuring powder adheres only to the workpiece <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>.
    *   For curing, typically bake in an oven at 235°C (380°F) for 5 minutes until the paint flows, then drop to 190°C (350°F) for another 15 minutes for a total of 20 minutes <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>. Leaving it at the higher temperature for the entire duration can cause white paint to yellow slightly to a light beige <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. Full curing is important for hardness through cross-linking <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.
    *   Minor defects can be oversprayed and re-baked <a class="yt-timestamp" data-t="00:30:54">[00:30:54]</a>.

## Final Assembly

After cooling, remove thread protectors <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>. Clean threads using a tap to remove any spot welding residue or paint <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>. For ease of assembly and maintenance, incorporating keyholes and slots for cover mounting is highly beneficial, allowing covers to slide off without fully removing screws <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.