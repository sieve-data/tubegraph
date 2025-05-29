---
title: Design Philosophy and Aesthetics
videoId: MtxA20Q-Uss
---

From: [[dgelbart]] <br/> 

## Strength vs. Stiffness

In classical mechanical engineering, concerns often revolve around strength, such as when building bridges, steel cables, or airplanes <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. However, in the design of instruments and machine tools, **stiffness** is the primary concern <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

For instance:
*   A microscope frame might support one ton, yet in use, it only holds a glass slide <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Its heavy construction ensures it remains completely stiff even when touched <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   A lathe bed, made of cast iron, could easily support 10 tons, but the workpiece is only 10 kg <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. It is overdesigned because stiffness, not strength, dictates its dimensions <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   Measurement tools, like squares, must be extremely stiff to prevent deflection during measurement, even if they bear no significant force <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

There is a significant difference between strength and stiffness <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. A demonstration shows that a bar cut in two and held with rubber bands can be stiffer than a solid aluminum bar <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   A solid bar deflected 12 microns under a load <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   The cut bar, despite having strength limited to that of a rubber band, deflected only 7 microns under the same load <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   This counter-intuitive result occurs because the two pieces, when held together, behave like a single, thicker piece, which can be theoretically eight times stiffer if double the thickness <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Material Hierarchy in Design

When approaching [[materials_and_construction_methods_for_precision_machinery | designing a part]], there's a hierarchy of ease and cost for manufacturing:
1.  **Wire**: The easiest and cheapest material to work with <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
    *   Advantages for production:
        *   Zero waste, as wire comes on a spool <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
        *   Minimal finishing; corners don't need deburring, and sharp ends can be hidden <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
        *   Modern CNC machines can bend wire into any shape very cheaply without specific tooling <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. Four computer-controlled fingers can bend the wire or tube as it's fed, allowing for bends in a full 360-degree range <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. This means a complex wire piece can take shape in the air without tooling <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
2.  **[[designing_with_wire_and_sheet_metal | Sheet Metal]]**: Considered if wire isn't feasible <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
    *   Sheet metal can sometimes perform better than solid parts, particularly for adjustable and lockable components <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
    *   An adjustable monitor holder made from sheet metal can be extremely rigid when locked <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. This rigidity comes from multiplying friction across many surfaces, similar to a multi-disk clutch <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
    *   Techniques like [[designing_enclosures_using_waterjet_cutting | waterjet cutting]] are highly applicable here <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
3.  **Solid**: Used if neither wire nor sheet metal is suitable <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

## Precision and Feel in Solid Design

When designing with solid materials, consider the required accuracy and precision <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **Brute Force Precision**: If absolute, non-adjustable precision is needed, there are no shortcuts; parts may require scraping and lapping <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
*   **Adjustable Precision with "Feel"**: Sometimes, an adjustable part needs a "precision feel" rather than absolute fixed precision <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.
    *   A screw adjusted directly against a surface can feel rough due to burrs and scratching <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
    *   Inserting a ball bearing ball between the screw and the surface creates a smooth adjustment because the screw slides on a highly polished surface <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
    *   This concept applies to shafts and holes, where buying precise pins (like dowel pins or roller bearing pins) can achieve precision without machining the shaft itself <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

## Instrument vs. Machine Design

The purpose of a design dictates key choices:
*   **Instrument Design**: For devices with minimal load but high accuracy requirements <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
    *   Can use kinematic mounts, which are convenient for removal, replacement, and self-adjustment <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.
    *   Surfaces can rest on small points, requiring minimal lapping <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.
    *   Kinematic mounts rely on point contacts, which cannot carry heavy loads due to infinite pressure at contact points, leading to indentation <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
*   **Machine Design**: For devices that carry heavy loads, require huge stiffness, and potentially wear resistance <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.
    *   Cannot use kinematic mounts <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
    *   Relies on overconstrained designs or full surface bearings <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

## Product Design Considerations

For product design, especially for something that will be repeated and have a long life, several additional factors come into play, related to [[importance_of_planning_and_optimization_in_prototyping | lifetime cost]]:
*   **Maintenance**: Parts must be easily removable, and access should be proper <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.
*   **Cable Routing**: A frequently underestimated aspect is routing electrical cabling <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. All cables, plugs, and strain reliefs must be precisely laid out in the design to avoid a messy build <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.
*   **Fluid and Electrical Separation**: In systems with both hydraulics/water and electrical components (common in CNC machines), fluid tubing should always be placed below electrical wiring to prevent leaks from damaging electrical components <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. Electrical relays should be on top, and water/hydraulics on the bottom <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. Air lines can be on top <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

## Aesthetics in Design

A key rule for achieving aesthetics in design is that **if something is 100% functional, it is always beautiful** <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
*   Examples of inherently beautiful, fully functional objects include nails, hammers, and airplanes <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. Airplanes have no room for non-functional additions due to weight constraints <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
*   Conversely, cars can be ugly because not everything is functional; they often have non-functional spoilers or additions <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
*   A part designed with no extra metal, where material is removed from low-stress areas, is inherently beautiful <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>. For example, a classical bow is thinner at the ends where there's less stress; a bow that gets wider at the end would look ugly because it intuitively feels non-functional and has unneeded material <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>.

To make a design beautiful, design it to be 100% functional and remove all unneeded material <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>. Its beauty will emerge naturally <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.