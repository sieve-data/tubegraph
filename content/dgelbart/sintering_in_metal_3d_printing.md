---
title: Sintering in metal 3D printing
videoId: nyYcomX7Lus
---

From: [[dgelbart]] <br/> 

[[Metal 3D printing process | Metal 3D printing]] is considered more important than plastic 3D printing for production applications in the long run <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. While methods like injection molding offer low-cost, high-volume, and high-quality production for plastics <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, similar mass production methods for high-performance metal parts (like steel, stainless steel, or special alloys) are often costly and time-consuming <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>, <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This includes [[challenges_and_limitations_of_metal_3d_printing | CNC machining]], investment casting, and forging <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

[[Advantages of metal 3d printing | Metal 3D printing]] offers a pathway not just for prototyping but also for producing complex parts, with costs projected to decrease over time <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## When Sintering Excels

[[Applications of metal 3d printing | Metal 3D printing]] offers significant benefits, especially when a part contains substantial internal features or structures <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. Simple parts without internal structures can often be produced faster and cheaper using traditional [[designing_with_wire_sheet_metal_and_solid_materials | CNC machining]] from a metal plate <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

For parts with internal cavities, undercuts, or complex passages that are difficult or impossible to reach with conventional tools, metal 3D printing is often more efficient <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. Investment casting, while capable of producing such parts, can take a month or more, involving extensive tooling and a multi-day process of applying ceramic layers, drying, burning out wax, and pouring metal <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. In contrast, metal 3D printing can produce complex parts with internal complexity, like miniature manifolds, much faster (e.g., one to two days for a tray of 100 parts) <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

Additionally, metal 3D printing is advantageous for very thin-walled parts, which are time-consuming to [[designing_with_wire_sheet_metal_and_solid_materials | CNC machine]] due to grip issues and slow cuts <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Thicker parts, conversely, take longer to 3D print as they require more material deposition <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This preference for internal complexity and hollow spaces makes parts faster to 3D print, while making them slower or impossible to machine <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

## Materials for Sintering

Stainless alloys are popular for sintering because their cost in powdered form is comparable to plain steel, and the printing and sintering times remain consistent regardless of the alloy's hardness <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. This allows for the [[use_of_different_materials_for_castinglike_assemblies | use of exotic alloys]] that might otherwise be harder to machine <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

## The Sintering Process

Sintering is a process where metal powder, shaped and lightly held together by a binder or pressure, is heated to a temperature below its melting point but high enough to metallurgically bond the individual particles <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>, <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This process densifies the part and increases its strength <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. For sintering to occur within a reasonable time, the temperature must be very close to the melting point (e.g., 20-50 degrees below) <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

Despite the metal becoming very soft (like play-doh) at these temperatures, the part amazingly shrinks uniformly in all directions with a predictable ratio, typically achieving accuracies within a fraction of 1% <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>, <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>, <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>, <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>. This uniform shrinkage occurs regardless of the complexity of the shape <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>. The shrinkage (e.g., 17-20%) is necessary because the air gaps between the metal powder particles disappear as the metal fuses together <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

### Historical Context of Sintering

Sintering is an ancient process <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>:
*   Ceramics, made from clay, undergo sintering in a kiln, a tradition dating back 25,000 years <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   Metal sintering is thousands of years old <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. The Iron Pillar of Delhi, made about 1,500 years ago, is believed to be the largest sintered object ever made (seven meters tall, six tons) <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   Historically, sintering allowed objects to be made from metals with high melting points (like platinum) when furnaces capable of reaching casting temperatures were unavailable <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. Ancient Inca jewelry from platinum and gold, and many steel objects, were produced by sintering <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

### Two Main Metal 3D Printing Approaches

There are two primary approaches for 3D printing metal objects with internal complexity:

1.  **Sintering-based Methods**:
    *   **Catalyzed Deposition of Powder**: Metal powder is mixed with a plastic or liquid binder to create a paste or filament, which is then deposited layer by layer <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>, <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
    *   **Binder Jetting**: A layer of metal powder is laid down, and a binder is selectively applied where the metal is desired <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. Unbound powder is brushed off <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
    *   In both cases, the resulting "green part" (e.g., a gear printed with an FDM-type printer for metal paste) is fragile (like chalk) <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>, but holds its shape until it is heated in a sintering furnace <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. The furnace then fuses the metal particles, resulting in a solid, scaled-down replica <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.

2.  **Laser/Energy-based Methods (e.g., Direct Metal Laser Sintering (DMLS) / Selective Laser Melting (SLM))**:
    *   Powder is placed everywhere layer by layer, but energy (typically from a fiber-optic laser) is used to selectively melt the powder only where the solid part is desired <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>, <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>, <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. Although often called "selective laser sintering" (SLS), the process is more accurately described as "selective laser melting" (SLM) because the short dwell time of the laser beam requires melting rather than just sintering for particle fusion <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.
    *   These systems are expensive (around $1 million for installation) and require extensive post-processing <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>, <a class="yt-timestamp" data-t="00:44:46">[00:44:46]</a>.
    *   Parts often need support structures during printing to counteract warping caused by rapid cooling and shrinking of molten layers, similar to [[spot_welding_and_repairing_errors_in_metal_prototypes | welding]] <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.
    *   Post-processing involves heat treatment in a controlled atmosphere furnace to relieve stresses and prevent oxidation, followed by removal of supports, often using wire EDM or traditional methods like belt sanders <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.
    *   These systems are typically housed in special, explosion-proof installations due to the explosive nature of some metal powders, making them suitable for large production facilities (e.g., medical, aerospace) rather than small R&D labs <a class="yt-timestamp" data-t="00:26:43">[00:26:43]</a>.

## Sintering-Type Metal 3D Printing Systems

A common example of a sintering-based system, such as the Ropadia 3D metal printer, leverages technology similar to FDM plastic printers <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.

### System Components and Operation

*   **Printer**: Very similar to a plastic FDM filament printer, but fed by cartridges of metal paste (e.g., 5 kg each) <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>. One cartridge typically holds the main metal paste, while another holds a support or separation layer material <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>. A hydraulic system pushes the paste at high pressure (e.g., 250 psi) through a metering valve in the printhead <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>.
*   **Automated Sintering Furnace**: This is the second key component <a class="yt-timestamp" data-t="00:29:58">[00:29:58]</a>. It requires a tank of gas, typically 3% hydrogen with 97% argon, which is non-flammable and allows for office use <a class="yt-timestamp" data-t="00:30:07">[00:30:07]</a>.
*   **Process**: Parts are printed onto a surface like aluminum foil <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>. After printing, the "green part" is placed on a tray inside the furnace <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>. The furnace ramps up to high temperatures (e.g., 1740°C for 17-4 stainless steel) for several hours, followed by a long cooling period (e.g., a total cycle of 22-24 hours) <a class="yt-timestamp" data-t="00:34:05">[00:34:05]</a>. The system is locked for safety until it cools sufficiently <a class="yt-timestamp" data-t="00:34:28">[00:34:28]</a>.

### Support Structures and Bonding

*   Support is needed for printing parts with overhangs or internal structures <a class="yt-timestamp" data-t="00:35:26">[00:35:26]</a>.
*   Some support materials are water-soluble <a class="yt-timestamp" data-t="00:37:38">[00:37:38]</a>, allowing complex internal structures to be printed without physical support <a class="yt-timestamp" data-t="00:37:30">[00:37:30]</a>. By wetting the edges of printed green parts, they can be bonded together to form enclosed objects, as the paste's binding is water-based <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>. This eliminates the need for printing internal supports, saving time and simplifying the process <a class="yt-timestamp" data-t="00:38:35">[00:38:35]</a>.
*   This method also allows for combining [[use_of_different_materials_for_castinglike_assemblies | machined parts with 3D printed parts]] into a single piece by using printing paste as an adhesive and then re-sintering <a class="yt-timestamp" data-t="00:39:02">[00:39:02]</a>.
*   Unlike some other systems that require honeycomb-like infill structures, sintering-based systems using water-based paste often don't need infill, as the small amount of binder evaporates during sintering, allowing for 100% solid parts <a class="yt-timestamp" data-t="00:39:53">[00:39:53]</a>.

### Advantages of Sintering-based Systems

*   **Simplicity and Low Cost**: These systems are significantly less expensive than laser systems (e.g., under $200,000 for a complete installation compared to $1 million) <a class="yt-timestamp" data-t="00:41:24">[00:41:24]</a>. They do not require extensive backroom equipment like EDM machines or long finishing operations <a class="yt-timestamp" data-t="00:41:52">[00:41:52]</a>.
*   **Office Friendly**: No solvents, no special power requirements, and the gas used is non-flammable <a class="yt-timestamp" data-t="00:41:58">[00:41:58]</a>. They only require a small vent to the outside for fumes from evaporating support material <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>.
*   **Material Efficiency**: Many cases do not require a base or metal support, reducing wasted metal <a class="yt-timestamp" data-t="00:36:48">[00:36:48]</a>.
*   **Faster Post-Processing Time**: The total time to get a finished object is often faster than laser systems because the post-processing is minimal <a class="yt-timestamp" data-t="00:45:13">[00:45:13]</a>.

### Disadvantages of Sintering-based Systems

*   **Size Limitation**: The primary limitation is object size. Due to the softness of the green part at sintering temperatures, objects larger than roughly a shoebox (e.g., a complex differential gearbox) may sag or distort <a class="yt-timestamp" data-t="00:42:10">[00:42:10]</a>.
*   **Limited Material Choice**: Currently, there are fewer metal and ceramic material options available compared to laser systems <a class="yt-timestamp" data-t="00:43:32">[00:43:32]</a>.

### Market Segments

These two types of metal 3D printing cater to distinct markets <a class="yt-timestamp" data-t="00:45:25">[00:45:25]</a>:
*   **Laser/SLS/SLM Systems**: Best for high-net-value parts in sectors like aerospace and medical, which require large objects and a wider range of materials (e.g., titanium) <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>.
*   **Sintering-based Systems (FDM, Binder Jetting)**: More suited for R&D, prototyping, educational use, and small-batch production <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>. Binder jetting systems typically offer a middle ground in price and speed between FDM-sintering and laser systems <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.