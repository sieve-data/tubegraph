---
title: Design and Preparation of Sheet Metal Enclosures
videoId: RopgrECLSJc
---

From: [[dgelbart]] <br/> 

This guide outlines the complete process of constructing a sheet metal enclosure, from initial design conversion and cutting to bending, hardware insertion, and final finishing.

## Initial Setup and Cutting

The first step in creating an enclosure involves preparing the design and cutting the raw material <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

### Design Conversion
Assuming the design is already complete, it can be downloaded as an .ORD or .DXF file and then converted to a v5 file format for the machine <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

### Material Preparation
Once the file is ready, the material is clamped down <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Key parameters must be entered into the machine, including:
*   Material thickness <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Setting the height: typically set high, then brought to touch the material, and finally adjusted half a millimeter above the material for cutting <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

### Cutting Process
The [[utilizing_waterjet_cutting_for_electronic_enclosure_precision | cutting]] process then begins <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Post-Cutting Cleanup and Repair

After the material is cut, it's essential to clean up the part and correct any errors.

### Edge Finishing
*   Break sharp edges: This protects fingers and ensures that components lay flat <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Cuts, especially patterns, can be rough <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Repairing Mistakes with Spot Welding
Mistakes like extra or misplaced holes/cuts do not require scrapping the part <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. They can be repaired using [[prototyping_and_temporary_welding_techniques | spot welding]] <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Technique:** Place a slightly oversized piece of material above the defect and melt it into the hole with the spot welder <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   For slots, cut a strip slightly wider than the slot (e.g., by 0.5 or 1 millimeter) <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   Use a fairly high setting (e.g., "number 8") for larger areas to ensure melting over a big area <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   The plug doesn't need to be round; a square plug slightly larger than the hole works as the high current will melt and flow, overfilling the hole <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   After welding, cut off excess material and touch up corners <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. For perfection, the top surface can be sanded <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Bending the Enclosure

[[bending_order_and_techniques_for_enclosure_assembly | Bending]] is a critical stage that requires careful planning to ensure correct dimensions and avoid machine interference <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Critical Considerations
1.  **Order of Bends:**
    *   Determine the correct [[bending_order_and_techniques_for_enclosure_assembly | bending order]] because some parts can only be bent in a specific sequence; otherwise, the machine's dies may interfere <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. For example, edges might need to be bent up first to allow the die to fit for subsequent bends <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
2.  **Part Orientation:**
    *   Unless the part is symmetrical, ensure the correct side is oriented for bending to avoid creating a mirror image mistake <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. This is a common error that requires significant straightening <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
3.  **Tooling Selection:**
    *   Consider the available [[customization_and_tooling_for_precision_bending | tooling]] for bending <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. The length of the bent edges dictates the required tool size to fit between previously bent sections <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Segmentation of tooling can be used for longer bends <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. A small gap in the tooling will not significantly affect the bend quality <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Inserting Hardware and Reinforcement

Before completing all bends, it's often easier to insert hardware like rivet nuts or threaded inserts <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

### Captive Hardware
*   Install rivet nuts or threaded inserts while the part is still flat for easier access <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   [[techniques_for_constructing_enclosures_and_flexures | Captive hardware]] is crucial in electronic assembly to prevent screws from falling and shorting circuit boards <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
*   For standard round head studs, [[utilizing_waterjet_cutting_for_electronic_enclosure_precision | waterjet]] cut holes to allow the head to be felt for precise placement <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>.
*   Nuts and studs require longer spot welding duration due to their larger area <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.
*   Remember that spot welding cannot be done after painting, as paint acts as an insulator <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.

### Braces for Squareness
To ensure the enclosure maintains a perfect right angle, especially with larger parts, it's beneficial to add spot-welded braces <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.
*   Weld braces on one side first <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.
*   Bend the enclosure against a square and then weld the other side of each brace to fix it in place <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

## Designing and Fitting the Cover

Creating a well-fitting cover requires accounting for material thickness and bend radius <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

### Test Strip Method
*   Cut a test strip of the same width as the cover <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
*   Use CAD programs (e.g., SolidWorks sheet metal option) to calculate initial bend positions <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   Perform a test bend on the strip and adjust the numbers based on how it fits <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. This saves material compared to bending the full cover multiple times <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   If the fit is too tight, adjust measurements (e.g., reduce by 1mm on each side) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   If the enclosure's base bends are not exactly 90 degrees, gently push them down to ensure the cover fits perfectly without gaps <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Always use a protective material (e.g., a sweater) when pressing sheet metal to avoid dents <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.

### Cover Recess for Aesthetics and Durability
*   Always recess the cover a couple of millimeters from the end of the enclosure <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.
*   This allows the rounded edge of the bend to be exposed, avoiding a sharp edge <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
*   Sharp edges are problematic because paint will always chip from them, making the enclosure look ugly <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Recessing ensures any impact hits the more durable rounded corner <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   It's a good practice to bias the cover to be slightly too tight initially <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

## Optimizing Design with Waterjet Capabilities

[[designing_with_wire_sheet_metal_and_solid_materials | Designing]] for waterjet cutting allows for precise features that enhance functionality and ease of assembly.

### Advanced Features
*   **Keyed Holes:** For toggle switches or other components with anti-rotation features, cut corresponding keys into the holes <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>. Similarly, for power cords, cut double-D shaped holes to match common connectors <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   **Knockouts:** If uncertain about future hole requirements, cut knockouts – incomplete holes with tabs holding the plug in place <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. These can be easily punched out later, especially after the box is assembled <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.
*   **Integrated Brackets/Clamps:** Plan and cut all small internal brackets, cable clamps, or 'L' brackets from the same sheet during the initial waterjet process <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. This ensures they get painted together and fit perfectly <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

### Precision and Distortion Considerations
*   **Hole Registration:** Holes cut in a single plane by a waterjet are perfectly registered (accurate to about 0.1mm) <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. However, registration is lost across bend lines because it depends on the squareness of the bend and material deformation <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.
*   **Holes Near Bends:** Avoid placing holes too close to bend lines <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>. If an edge is too narrow (e.g., 3mm instead of 10mm) near a bend, it will twist and distort <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>. Round holes are particularly susceptible to distortion if they touch a bend line <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.
*   **Recommended Distance:** Ideally, keep any openings at least 10mm away from a bend line <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>. For openings, a minimum of 15mm to the bend line is recommended to avoid distortion <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.

## Painting Preparation and Application

After all fabrication is complete, the enclosure is prepared for [[painting_and_finishing_techniques_for_metal_enclosures | painting]] and then coated.

### Surface Preparation (Sandblasting)
*   The first step is sandblasting the entire enclosure to prepare the surface for [[best_practices_for_painting_metal_surfaces | painting]] <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>.

### Masking and Hanging
*   **Masking:** Any areas where paint is undesirable (e.g., studs, threads) must be masked using silicon rubber tubes or Kapton tape, which can withstand high temperatures <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>. Nuts generally don't need masking as threads will be cleaned out later <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>.
*   **Hangers:** Create hangers to suspend the part for painting and curing <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
    *   Hang the part in a way that the hanger's signature is invisible on the finished product <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>.
    *   Hangers cannot be reused for powder coating after they themselves are coated, as they are essential for grounding <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.

### Powder Coating Process
*   **Application:** Apply powder coat, adjusting voltage for different areas <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>.
    *   Reduce voltage (e.g., 15 kilovolts) for inside corners to minimize electrostatic shielding <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>.
    *   For other areas, 20 to 50 kilovolts is generally acceptable <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.
    *   In a proper [[workshop_layout_and_design | enclosure]], the part would hang on a rotating shaft to ensure even coating <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.
*   **Curing:**
    *   The nominal procedure involves placing the part in an oven for 5 minutes at 235°C (approximately 380°F) until the paint flows <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>.
    *   Then, drop the temperature to 190°C (less than 350°F) and leave for another 15 minutes, making a total cycle of 20 minutes <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>.
    *   Alternatively, leaving it at 230-235°C for the full 20 minutes is acceptable, though white paint may yellow slightly to a light beige, which can be aesthetically pleasing <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
    *   The extended curing time after flowing is crucial for chemical crosslinking, which gives the paint its hardness, especially for epoxy coatings <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.
    *   If the powder is accidentally touched, it can be oversprayed with more powder and re-cured <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.

## Final Assembly

After cooling, the final steps involve removing protective coverings and preparing for component installation.

### Post-Paint Cleanup
*   Remove silicone rubber or Kapton tape protectors from threads <a class="yt-timestamp" data-t="00:31:41">[00:31:41]</a>. These materials are essential to prevent fusion during curing <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>.
*   Clean threads: Go over all threads with a tap to clear any paint or welding debris <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

### Assembly with Keyholes and Slots
*   When [[techniques_for_constructing_enclosures_and_flexures | designing with keyholes and slots]], covers can be slid on and off without removing screws, significantly speeding up assembly and maintenance <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. This approach extends the lifespan of R&D work by reducing time spent on repetitive screw removal <a class="yt-timestamp" data-t="00:33:12">[00:33:12]</a>.