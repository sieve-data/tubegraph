---
title: Spot Welding and Repairing Errors in Metal Prototypes
videoId: RopgrECLSJc
---

From: [[dgelbart]] <br/> 

Creating a metal prototype involves several precise steps, from initial design and cutting to bending, welding, and finishing. This guide outlines the complete process, including how to efficiently [[spot_welding_basics_and_setup | spot weld]] and repair errors that may occur during fabrication <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Initial Part Preparation

After designing and cutting the material (e.g., from an A or D file converted to DXF or OV5 format) <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, the material is clamped, and its thickness and height are set for processing <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

Once the initial cutting is complete <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>, the first step is to break any sharp edges to protect fingers and ensure parts lay flat <a class="yt-timestamp" data-t="01:21:51">[01:21:51]</a>. Cut patterns can often leave rough edges that require cleaning <a class="yt-timestamp" data-t="01:37:11">[01:37:11]</a>.

## [[prototyping_and_temporary_welding_techniques | Repairing Errors with Spot Welding]]

Mistakes such as an extra or misplaced hole or cut can occur during the fabrication process <a class="yt-timestamp" data-t="02:01:28">[02:01:28]</a>. Instead of scrapping the part, these errors can be fixed using a [[spot_welding_basics_and_setup | spot welder]] <a class="yt-timestamp" data-t="02:08:29">[02:08:29]</a>.

The technique involves placing a slightly oversized piece of metal over the defect and melting it into the hole with the [[spot_welding_basics_and_setup | spot welder]] <a class="yt-timestamp" data-t="02:14:31">[02:14:31]</a>. For larger slots, a strip of metal slightly wider than the slot (by about half a millimeter or a millimeter) can be used <a class="yt-timestamp" data-t="02:31:07">[02:31:07]</a>. A high setting (e.g., number eight) is typically used for melting over a larger area <a class="yt-timestamp" data-t="02:39:10">[02:39:10]</a>.

After melting, the excess material is cut off and the corner is touched up <a class="yt-timestamp" data-t="03:06:21">[03:06:21]</a>. The plug does not have to be round; a square plug slightly larger than the hole can be used, as the high current will melt and flow the metal, always overfilling the hole so excess can be sanded off <a class="yt-timestamp" data-t="03:31:03">[03:31:03]</a>. The process completely melts and fills the hole <a class="yt-timestamp" data-t="03:57:04">[03:57:04]</a>.

## Bending the Part

Bending is a critical step, and two main considerations are vital:
1.  **Order of Bends:** The sequence of bends must be carefully thought through, as some parts can only be bent in a specific order to avoid interference with the machine <a class="yt-timestamp" data-t="04:09:20">[04:09:20]</a>. For instance, outer edges may need to be bent up before inner bends can be made, ensuring the die fits <a class="yt-timestamp" data-t="04:19:15">[04:19:15]</a>.
2.  **Orientation:** Unless the part is symmetric, determining the correct bending side is crucial to avoid creating a mirror image, which would require extensive straightening <a class="yt-timestamp" data-t="04:51:24">[04:51:24]</a>.

Tooling also plays a role in the bending order. Consider which tools fit best between already bent sections <a class="yt-timestamp" data-t="06:03:07">[06:03:07]</a>. While slight gaps in tooling can still result in a nice bend, optimal results are achieved by spreading the tools as much as possible for accuracy <a class="yt-timestamp" data-t="07:51:25">[07:51:25]</a>.

## Adding Inserts and Hardware

It is often much easier to [[spot_welding_basics_and_setup | spot weld]] nuts or threaded inserts into the part *before* completing all the bends, even if it's possible to do it afterward <a class="yt-timestamp" data-t="10:00:27">[10:00:27]</a>. Nuts and studs require a longer welding duration than a simple weld due to their larger area <a class="yt-timestamp" data-t="23:05:07">[23:05:07]</a>.

The use of [[advanced_spot_welding_applications | captive hardware]] (like threaded nuts and studs welded directly into the part) is highly important in electronic assembly <a class="yt-timestamp" data-t="24:28:13">[24:28:13]</a>. It significantly reduces the chances of screws falling and shorting out circuit boards <a class="yt-timestamp" data-t="24:34:39">[24:34:39]</a>.

## Fitting the Cover and Design Considerations

When bending a cover to fit perfectly, factors like material thickness and bend radius are complex <a class="yt-timestamp" data-t="11:26:01">[11:26:01]</a>. A simpler approach is to cut a test strip of the same material <a class="yt-timestamp" data-t="11:40:24">[11:40:24]</a>. Use calculations from CAD programs (e.g., SolidWorks sheet metal option) as a starting point <a class="yt-timestamp" data-t="11:48:02">[11:48:02]</a>, then perform a test bend and adjust the numbers until the fit is correct <a class="yt-timestamp" data-t="12:03:13">[12:03:13]</a>. This prevents wasting the entire cover <a class="yt-timestamp" data-t="12:06:07">[12:06:07]</a>.

For aesthetic and functional reasons, always recess the cover by a couple of millimeters from the end of the main part <a class="yt-timestamp" data-t="14:34:04">[14:34:04]</a>. This ensures the rounded edge of the bend is visible, preventing sharp edges that can cause injury or lead to paint chipping <a class="yt-timestamp" data-t="14:41:03">[14:41:03]</a>.

### Waterjet Design Advantages

When designing for waterjet cutting, leverage its capabilities:
*   **Keyholes:** Cut keyholes for components like toggle switches, ensuring proper alignment and preventing rotation <a class="yt-timestamp" data-t="18:16:11">[18:16:11]</a>.
*   **Double D-shaped Holes:** For circular components that require anti-rotation features, cut double D-shaped holes instead of plain round ones <a class="yt-timestamp" data-t="18:40:08">[18:40:08]</a>.
*   **Knockouts:** Include knockouts (partially cut holes with holding tabs) for optional future openings. These are easier to punch out later, especially after assembly <a class="yt-timestamp" data-t="19:01:21">[19:01:21]</a>.
*   **Integrated Brackets:** Design and cut any small internal brackets, cable clamps, or 'L' brackets from the same sheet as the main part. This ensures consistent material, finishes, and fits <a class="yt-timestamp" data-t="19:40:08">[19:40:08]</a>.

### Waterjet Design Considerations

*   **Hole Registration:** Holes cut in a single plane will be perfectly registered (accurate to about 0.1 mm) <a class="yt-timestamp" data-t="20:21:05">[20:21:05]</a>. However, registration is lost across bend lines due to bending inaccuracies and material deformation <a class="yt-timestamp" data-t="20:36:09">[20:36:09]</a>. Design to minimize holes across bend lines where high accuracy is needed <a class="yt-timestamp" data-t="21:10:04">[21:10:04]</a>.
*   **Proximity to Bend Lines:** Avoid placing holes or openings very close to bend lines <a class="yt-timestamp" data-t="21:35:05">[21:35:05]</a>. Round holes, in particular, will distort out of shape if too near a bend <a class="yt-timestamp" data-t="21:55:00">[21:55:00]</a>. Aim to keep openings at least 10-15 mm away from bend lines to prevent distortion <a class="yt-timestamp" data-t="22:22:04">[22:22:04]</a>.

## Finishing and Painting

After all welding and bending are complete, prepare the part for painting:
1.  **Sandblasting:** [[sandblasting | Sandblasting]] prepares the surface for paint <a class="yt-timestamp" data-t="25:08:04">[25:08:04]</a>.
2.  **Masking:** Any areas where paint is not desired (e.g., threads, specific studs) should be covered with silicon rubber caps or Kapton tape, which can withstand high temperatures <a class="yt-timestamp" data-t="25:35:07">[25:35:07]</a>.
3.  **Hanging:** Use hangers to suspend the part, ensuring the hangers' contact points are in invisible areas <a class="yt-timestamp" data-t="26:02:18">[26:02:18]</a>. Hangers are typically single-use for [[advanced_welding_and_coating_processes | powder coating]] as they must provide grounding <a class="yt-timestamp" data-t="26:31:07">[26:31:07]</a>.

### [[advanced_welding_and_coating_processes | Powder Coating]] Process

*   **Baking Procedure:** A nominal procedure is to bake in an oven for about 5 minutes at 235°C (380°F) until the paint flows, then drop the temperature to 190°C (less than 350°F) for another 15 minutes, for a total cycle of 20 minutes <a class="yt-timestamp" data-t="27:09:07">[27:09:07]</a>. Leaving it at 230-235°C for the whole 20 minutes can cause the paint to yellow slightly, resulting in a light beige <a class="yt-timestamp" data-t="27:37:05">[27:37:05]</a>.
*   **Crosslinking:** The paint needs to crosslink during baking for hardness, especially for epoxy paints <a class="yt-timestamp" data-t="28:07:07">[28:07:07]</a>. Incomplete baking will result in soft paint <a class="yt-timestamp" data-t="28:19:07">[28:19:07]</a>.
*   **Application:** For inside corners, reduce voltage (e.g., 15 kilovolts) to minimize electrostatic shielding and ensure even coating <a class="yt-timestamp" data-t="28:29:07">[28:29:07]</a>. For other areas, 20-50 kilovolts is generally acceptable <a class="yt-timestamp" data-t="29:00:26">[29:00:26]</a>. A proper non-metal enclosure for powder coating would attract powder only to the workpiece, reducing overspray <a class="yt-timestamp" data-t="29:22:31">[29:22:31]</a>.
*   **Defect Repair:** If the powder is touched or a defect occurs before baking, simply overspray with more powder and re-bake <a class="yt-timestamp" data-t="30:46:17">[30:46:17]</a>. Paint cannot be [[spot_welding_basics_and_setup | spot welded]] after curing as it acts as an insulator <a class="yt-timestamp" data-t="22:34:57">[22:34:57]</a>.

## Final Assembly

Once the part cools down after baking <a class="yt-timestamp" data-t="31:39:27">[31:39:27]</a>:
1.  **Remove Protectors:** Take off the silicone rubber or Kapton tape protectors from masked areas <a class="yt-timestamp" data-t="31:44:03">[31:44:03]</a>.
2.  **Clean Threads:** Clean any threads, which may be dirty from welding and painting, using a tap <a class="yt-timestamp" data-t="32:03:00">[32:03:00]</a>.
3.  **Assemble:** Install mounting screws and fit the cover <a class="yt-timestamp" data-t="32:37:05">[32:37:05]</a>.

Designing with keyholes, slots, and [[advanced_spot_welding_applications | captive hardware]] significantly reduces assembly time by allowing parts to slide off without removing screws, effectively extending the lifespan of an R&D engineer <a class="yt-timestamp" data-t="33:04:12">[33:04:12]</a>.