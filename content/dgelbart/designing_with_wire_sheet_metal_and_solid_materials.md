---
title: Designing with wire sheet metal and solid materials
videoId: MtxA20Q-Uss
---

From: [[dgelbart]] <br/> 

When approaching the design of mechanical parts, a key consideration is the choice of material and form factor, following a hierarchy of ease and cost: wire, then sheet metal, then solid materials <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. This approach considers not only the raw material cost but also manufacturing efficiency and precision requirements, aligning with an [[overview_of_materials_for_prototype_building | overview of materials for prototype building]].

## Wire Design

Wire is generally the easiest and cheapest material to work with for both one-off designs and production <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. An example of effective wire design is a wire bottle cap, which latches and opens beautifully <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.

### Advantages of Wire
*   **Zero Waste:** Wire comes on a spool, resulting in virtually no material waste during manufacturing <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
*   **Minimal Finishing:** Wire parts require minimal finishing like deburring, as the main body is smooth; only sharp ends might need to be hidden by smart bending <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Cost-Effective Production:** Modern CNC machines can bend wire into virtually any shape very cheaply <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. These machines feed wire from a bushing, and computer-controlled fingers bend it in a full circle, allowing complex shapes to form without special tooling <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. This relates to [[techniques_for_bending_metal | techniques for bending metal]].

## Sheet Metal Design

If a design cannot be achieved with wire, the next consideration is sheet metal <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>. Sheet metal can sometimes offer advantages over solid materials, especially when designing for adjustability and strong locking mechanisms <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. The [[design_and_preparation_of_sheet_metal_enclosures | design and preparation of sheet metal enclosures]] often utilizes these principles.

### Advantages of Sheet Metal
*   **Multi-Surface Locking:** A good example is an adjustable monitor holder, which can be made from sheet metal <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. When locked, it becomes very rigid, often more so than a machined solid lock, because it utilizes many surfaces <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. The total friction is multiplied by the number of surfaces, similar to a multi-disk clutch <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>. This allows a very small hinge to achieve immense locking power <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.
*   **Versatile Fabrication:** Techniques like water jet cutting are highly suitable for sheet metal fabrication <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## Solid Material Design

When wire or sheet metal are not suitable, designs must be built from solid material <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. When working with solid materials, attention shifts to accuracy and precision <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

### Strength vs. Stiffness
A fundamental distinction in mechanical engineering is between strength and stiffness <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
*   **Strength** is a primary concern for structures like bridges or steel cables <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   **Stiffness** is paramount in instruments and machine tools <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. For example, a microscope frame, while only supporting a glass slide, is made heavy to be completely stiff and prevent flexing when touched <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Similarly, a lathe bed is significantly overdesigned in terms of strength (e.g., supporting 10 tons for a 10 kg workpiece) because stiffness, not strength, determines its dimensions for precision <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Even tools like a machinist's square, which bear no force, must be very stiff to prevent deflection during measurement <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

A demonstration comparing a solid aluminum bar to a bar cut in two and held by rubber bands reveals a surprising aspect of stiffness <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. While the strength of the rubber-banded bar is limited, its stiffness can be significantly higher <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Under an equal load, the solid bar deflected 12 microns, while the cut bar with rubber bands deflected only 7 microns <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. This is because the central section of the cut bar, if the pieces don't separate, behaves like a solid piece twice as thick, making it theoretically eight times stiffer <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Achieving Precision and Adjustability
*   **Adjustable vs. Brute Force Precision:** Consider if parts need to be precisely adjustable or if brute force precision (lapping, scraping) is required <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
*   **Improving Feel of Adjustment:** To give a rough adjustment a smooth, precise feel, insert a ball from a ball bearing between the adjusting screw and the surface <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. This allows a rough screw end to slide on a very smooth surface, making the overall adjustment feel precise <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
*   **Using Pre-fabricated Precision Parts:** Instead of machining shafts to precision, use precise pins like dowel pins or roller bearing pins <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   **Bearing Mounting:** Bearings inherently have play <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. They are designed to work in pre-loaded pairs to eliminate this play <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Preloading can be achieved by pushing bearings against each other using a sleeve on a shaft, or by using spring or wave washers <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. Wave washers, with their wavy shape, allow for some flex, making preload less critical <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
    *   For thin sheet metal housings that cannot hold bearings, beef up the wall with additional water jet cut plates permanently mounted with screws <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   Alignment can be achieved with self-aligning welded nuts and tapered flathead screws that pull into position (for low precision) <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. For high precision, "line boring" is necessary: drilling or boring through both pieces at once after assembly <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Bearings can be secured with snap rings in grooves <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
    *   For loose fits, Loctite can fill the gap and provide a strong bond, hardening overnight <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. To remove, heat the part to 150°C <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
    *   **Bearing Sourcing:** VXB Bearings is a good supplier <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. The 8mm ID by 22mm OD bearing is an exceptionally good value (around 25 cents for high quality) due to its widespread use in skateboards <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. Be cautious of "abex 7" branded bearings, which might be a company name, not an ABEC 7 quality rating <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

### Instrument vs. Machine Design
A critical distinction in solid material design is whether the part is for an instrument or a machine <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   **Instrument Design:** Instruments typically have no significant load and require high accuracy <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. Techniques like kinematic mounts (point contacts) are convenient, allowing parts to be easily removed, replaced, and self-adjusted <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.
*   **Machine Design:** Machines carry heavy loads and require huge stiffness and wear resistance <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. Kinematic mounts are unsuitable because point contacts cannot carry heavy loads without deforming due to infinite pressure <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. Machine tools rely on over-constrained designs or full-surface bearings <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

### Production Considerations for Solid Designs
When designing for a product that will be repeated, consider lifetime cost and maintenance <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>.
*   **Cable Management:** Always plan the routing of electrical cables, plugs, and strain reliefs in the design, as underestimating this can lead to a messy build <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>.
*   **Fluid and Electrical Separation:** If a system involves both hydraulics/water and electrical components, always place fluid tubing below electrical wiring to prevent leaks from damaging electrical parts <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

## Design Philosophy and Aesthetics

Beyond functionality, [[design_philosophy_and_aesthetics_for_functional_parts | design philosophy and aesthetics for functional parts]] are important, especially for products <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.

### Functionality as Beauty
A key rule of design aesthetics states that if something is 100% functional, it is always beautiful <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
*   Examples: A nail or hammer is rarely considered ugly because their form is purely dictated by their function <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. Airplanes are generally beautiful because there's no room for non-functional additions <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.
*   Conversely, items like cars can be ugly because they often include non-functional spoilers or additions <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
*   A part designed with no extra metal, where material is only present where stress is highest, will always be beautiful <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>. For instance, a classical bow is thinner at the ends where stress is less <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>; a bow that got wider at the ends would look intuitively ugly because it would appear to have unneeded extra material <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.
*   To achieve aesthetic beauty, design for 100% functionality and remove all unneeded material <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.