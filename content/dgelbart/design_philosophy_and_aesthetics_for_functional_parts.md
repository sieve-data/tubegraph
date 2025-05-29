---
title: Design philosophy and aesthetics for functional parts
videoId: MtxA20Q-Uss
---

From: [[dgelbart]] <br/> 

Designing a part involves several considerations, ranging from fundamental mechanical properties to material selection, assembly, and even aesthetic appeal <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. The approach to design often depends on the application, whether it's for an instrument or a heavy-duty machine <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

## Core Design Principles

### [[strength_versus_stiffness_in_mechanical_design | Strength Versus Stiffness]]
In classical mechanical engineering, concerns often revolve around strength, such as in bridges or steel cables <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. However, for instruments and machine tools, [[strength_versus_stiffness_in_mechanical_design | stiffness]] is the primary concern <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

*   **Examples:**
    *   A microscope frame might support a ton, but its heavy design is for [[strength_versus_stiffness_in_mechanical_design | stiffness]] when touched, despite only supporting a glass slide <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
    *   A lathe bed, made of cast iron, can support 10 tons, but its workpiece is only 10 kg; it's overdesigned for [[strength_versus_stiffness_in_mechanical_design | stiffness]], not strength <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
    *   A square, which takes no force, must be very stiff to prevent deflection during measurement <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

*   **Demonstration:** A solid aluminum bar deflects 12 microns under load <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. A bar cut in two and held together with rubber bands, surprisingly, deflects only 7 microns under the same load, making it much stiffer <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This is because the center section, acting as a solid piece, is effectively twice as thick and thus eight times stiffer theoretically <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Material Hierarchy
When designing a part, there's a hierarchy of ease and cost in manufacturing <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.

1.  **Wire:** The easiest and cheapest material to work with <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
    *   **Advantages:** Zero waste, as wire comes on a spool <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. Minimal finishing required, as only the cut end needs deburring <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. Modern CNC machines can bend wire into complex shapes very cheaply without specialized tooling <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
    *   **Example:** A wire bottle cap mechanism <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.

2.  **Sheet Metal:** The next consideration if wire isn't suitable <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
    *   **Advantages:** Can achieve designs more rigid than machined solid forms, especially with multiple contact surfaces that multiply friction, similar to a multi-disk clutch <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. Techniques like water jet cutting are well-suited for sheet metal <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
    *   **Example:** An easily adjustable and lockable monitor holder <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

3.  **Solid Materials:** Used when wire or sheet metal are not viable <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
    *   Requires consideration of accuracy and precision, determining if [[strength_versus_stiffness_in_mechanical_design | strength]] or [[strength_versus_stiffness_in_mechanical_design | stiffness]] is the goal <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

### Precision and Adjustability
For solid parts, distinguish between brute-force precision and designs that leverage adjustability for a "precision feel" <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.

*   **Achieving Precision Feel:**
    *   If an adjustment screw feels rough due to its end scratching the surface <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>, placing a ball bearing between the screw and the surface makes the adjustment feel completely smooth <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
    *   Use precise off-the-shelf components like dowel pins or roller bearing pins for shafts and holes, rather than machining the entire part to high precision <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
    *   Inserting a perfect surface into a rougher assembly can achieve a smooth feel without machining everything to precision <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

## Application-Specific Design

### Instrument vs. Machine Design
The design approach differs significantly for instruments (low load, high accuracy) versus machines (heavy load, high [[strength_versus_stiffness_in_mechanical_design | stiffness]], wear resistance) <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.

*   **Instruments:** Can use kinematic mounts, which are convenient, self-adjusting, and allow surfaces to rest on very small contact points, reducing lapping <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>. However, point contacts cannot carry heavy loads due to infinite pressure <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
*   **Machines:** Often rely on overconstrained designs or full surface bearings, as kinematic mounts would indent under heavy loads <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

## Practical Product Design Considerations

For products that will be repeated or have a long lifetime, consider maintenance and accessibility <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.

*   **Cabling and Tubing:** Always account for electrical cabling pathways in the design <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. If using both hydraulics/water and electrical systems, position all water or hydraulic tubing below electrical wiring to prevent damage from leaks <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.
*   **Component Mounting (Example: Pulleys and Bearings):**
    *   **Set Screws:** File flats on shafts when using set screws to prevent denting and allow for easier removal <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. For higher torque, cross-drill with a pin <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
    *   **Flexure-Based Clamping:** A better system involves a split piece that squeezes around the shaft when a screw is tightened; this distributes load and doesn't mark the shaft <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. This can be machined with a water jet <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
    *   **Bearings:**
        *   Single bearings have inherent play <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. Bearings are designed to work in preloaded pairs to eliminate play <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
        *   Preloading can be achieved by squeezing two bearings against a sleeve on the shaft within a housing <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
        *   Spring washers or wave washers can be used to provide preload if housing accuracy is a concern, as they allow some flex <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
        *   For thin sheet metal housings, beef up the wall with additional plates (e.g., water jet cut) to hold the bearing <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
        *   Achieve alignment using self-aligning welded nuts and Flathead screws with a taper (for low precision) <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. For high precision, line-bore (drill through both pieces at once) or bore with a long tool after assembly <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
        *   For shafts within a bore, use a snap ring in a groove to stop the bearing <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
        *   Alternatively, pre-bore plates and align them after assembly, potentially epoxying them in place (less stable if knocked) <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. The easiest is to use two pieces with a bored step that prevents bearing movement <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
        *   A good supplier for cheap, high-quality bearings is vxbearings.com <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. The 8mm ID by 22mm OD bearing (used in skateboards) is an outstanding value, costing about 25 cents even at high quality due to huge supply <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. Be cautious of "abex 7" branding, which might refer to a company name rather than ABEC 7 quality <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
        *   For loose fits, a drop of Loctite can take up the gap and set overnight <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. To remove a Loctited part, heat it to about 150°C (300°F) to soften it <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

## Aesthetics in Design
Aesthetic appeal is important for products and personal gratification <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.

*   **Functionality Equals Beauty:** A functional design is inherently beautiful <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. Ugly designs often result from non-functional additions <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
    *   **Examples:** Nails and hammers are generally not considered ugly because they are 100% functional, unlike many cars with non-functional spoilers <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. Airplanes are beautiful because there's no room for extra weight or non-functional elements <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
*   **Material Efficiency:** A part designed without extra material (i.e., material removed from low-stress areas) is always beautiful <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
    *   **Example:** A classical bow is thinner at the ends where there's less stress; a bow that got wider at the ends would look ugly because it intuitively feels non-functional <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>.

The guiding principle for aesthetics is to design for 100% functionality and remove all unnecessary material <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>.