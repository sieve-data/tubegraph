---
title: Advantages and disadvantages of the casting to sinter method
videoId: kLgPW2672s4
---

From: [[dgelbart]] <br/> 

The "Cast to Sinter" method is a process for 3D printing metal and ceramic objects with high resolution and excellent surface finish <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Developed by Rapidia, this method leverages the capabilities of high-resolution resin plastic printers (SLA machines) to convert plastic parts into metal or ceramic components <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Rapidia has made the intellectual property for this process publicly available, aiming to sell more furnaces <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>.

## Advantages of the Cast to Sinter Method

*   **Superior Resolution and Surface Finish** The method produces the highest resolution and best surface finish compared to other metal 3D printing techniques <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. It can reproduce fine details, including micron-level details, thin walls with high aspect ratios, cross holes, and cross threads <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Parts produced are shiny and smooth, allowing for a mirror finish with a short electropolish <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Material Versatility** This process works for any metal or ceramic material that can be [[sintering_process_in_metal_3d_printing | sintered]] <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. Examples include stainless steel, alumina, zirconia, and tungsten carbide <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>.
*   **Cost-Effectiveness**
    *   **Ceramics:** For ceramic parts, a less expensive sintering furnace (around $4,000) can be used, as ceramics can be [[sintering_process_in_metal_3d_printing | sintered]] in air <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>. The total system cost for ceramics can be under $10,000 <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>. This offers a [[advantages_and_disadvantages_of_machinable_ceramics | high-performance, high-resolution 3D system for ceramics]] at a low cost <a class="yt-timestamp" data-t="00:27:49">[00:27:49]</a>.
    *   **General Part Cost:** The cost per part is primarily the cost of the metal powder, plus minimal electricity and gas for the furnace <a class="yt-timestamp" data-t="00:37:36">[00:37:36]</a>. Metal powder is generally cheaper when purchased in its raw form compared to filaments or bound metal slurries <a class="yt-timestamp" data-t="00:38:02">[00:38:02]</a>. Molds are inexpensive and reusable <a class="yt-timestamp" data-t="00:37:44">[00:37:44]</a>.
*   **Small Quantity and Exotic Material Production** The method is well-suited for very small quantities and exotic materials like platinum or gold, as only a small amount of powder needs to be mixed <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>.
*   **Reproducibility of Molds** Dozens of silicone molds can be made and filled simultaneously <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>. Molds are reusable every two hours once frozen parts are removed, allowing for faster production than traditional printing if many molds are used <a class="yt-timestamp" data-t="00:36:37">[00:36:37]</a>.

## Disadvantages of the Cast to Sinter Method

*   **Manual Steps and Delays** The process involves numerous manual steps and significant delays, such as waiting for silicone molds to cure, parts to freeze, and then 20 hours for drying <a class="yt-timestamp" data-t="00:34:08">[00:34:08]</a>. This contrasts with more automated 3D printing methods <a class="yt-timestamp" data-t="00:33:43">[00:33:43]</a>.
*   **Distortion** Parts produced using this method generally experience more distortion compared to parts made with regular 3D printing <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>. This is due to the slow settling of metal particles to the bottom, creating a density gradient <a class="yt-timestamp" data-t="00:34:37">[00:34:37]</a>. While rotationally symmetric parts might have minimal out-of-round distortion (30-50 microns), parts with overhangs can experience up to 1% distortion (hundreds of microns) <a class="yt-timestamp" data-t="00:34:56">[00:34:56]</a>.
*   **Shape Limitations** The method cannot produce shapes that are difficult or impossible to cast, such as hollow shapes or infills <a class="yt-timestamp" data-t="00:36:01">[00:36:01]</a>. Supports must also be cast for parts with overhangs <a class="yt-timestamp" data-t="00:35:25">[00:35:25]</a>.

## Process Steps

The [[prototyping_techniques_for_creating_castinglike_structures | "Cast to Sinter" method]] involves several distinct stages:

1.  **SLA Model Creation**
    *   Start with a plastic model created using an SLA (resin) printer <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. These printers are known for making super high-resolution parts at low cost <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
    *   The SLA model must be scaled up by approximately 19% to account for shrinkage during the [[sintering_process_in_metal_3d_printing | sintering process]] <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
    *   Spray paint the SLA model with any paint or varnish to prevent the photopolymer resin from inhibiting the polymerization of the silicone rubber mold <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

2.  **Silicone Rubber Mold Creation**
    *   Use a self-degassing, strong, tear-resistant silicone rubber (e.g., BVDino durometer 30A) <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
    *   Mix the silicone components 1:1 by volume or weight <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
    *   Pour the mixed silicone over the prepared SLA model in a container <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
    *   Allow to cure for a few hours, or accelerate curing in a warm place (60-80°C) for 2 hours <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   Cut the mold with a knife to remove the SLA part, marking the cut line for precise re-alignment <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Despite being soft, silicone rubber maintains its shape without distortion <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
    *   For simple parts, a one-piece mold can be made that flips inside out, avoiding cuts <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.
    *   For complex parts with many holes or channels, a more elaborate mold designed for injection under pressure with alignment bumps and air vents may be needed <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>.

3.  **Metal Slurry Preparation**
    *   Weigh the required amount of metal powder (e.g., 17-4 stainless steel, typically 10-25 micron fine powder for high resolution) based on the CAD model's weight <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
    *   Add approximately 10% of a specialized water-based binder to the metal powder <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
    *   Thoroughly mix the slurry using a bent wire in an electric drill for several minutes until it becomes smooth and pourable, like honey <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
    *   **The Binder:** The binder is critical and performs four functions <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>:
        1.  Holds the "green part" (unfired part) together for handling <a class="yt-timestamp" data-t="00:28:55">[00:28:55]</a>.
        2.  Prevents the formation of ice crystals during freezing, which would degrade part strength <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>.
        3.  Reduces the surface tension of the slurry to allow air bubbles to escape and ensure good wetting and bubble release, without significantly depressing the freezing point or weakening the frozen strength <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>.
        4.  Enhances shear thinning, meaning viscosity drops significantly under shear conditions (like vibration) for mold filling, but rapidly increases when shear stops to prevent metal particle sinking and density gradients <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>.
    *   Remove air bubbles by vibrating the mix on a vibrating table for a few minutes <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

4.  **Casting (Pouring into Mold)**
    *   Place the cut silicone mold back into its original cup or container, sealing the interface with silicone grease to prevent leaks <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
    *   Pour the metal slurry into the mold under strong vibration to ensure it fills every cavity and expels air bubbles <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
    *   If needed, prepare a "raft" (a flat plate of the same material) by pouring excess slurry onto a flat surface <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. This raft prevents the part from sticking to the furnace shelf and distorting during shrinkage <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

5.  **Freezing and Demolding**
    *   Freeze the mold containing the slurry in a freeze dryer (e.g., Harvest Right unit) at -40°C for a minimum of 2 hours <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.
    *   Once completely frozen, demold the part. The frozen slurry, being a composite material of metal powder and water, is immensely strong and can withstand brutal force without breaking delicate features or undercuts <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.

6.  **Drying (Freeze-Drying)**
    *   Place the demolded, frozen "green part" back into the freeze dryer and switch it to drying mode <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
    *   This is the longest step, taking about 20 hours to completely dry the part <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

7.  **Sintering**
    *   Place the dried part (and a piece of the raft) onto a shelf in a [[sintering_process_in_metal_3d_printing | sintering furnace]] <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>. For metals, a vacuum sintering furnace is required, which costs significantly more (over $100,000) than an air furnace used for ceramics <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
    *   Sprinkle alumina powder on the raft to prevent the part from fusing to it during [[sintering_process_in_metal_3d_printing | sintering]] <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>.
    *   Select the appropriate metal cycle on the furnace (e.g., Rapidia vacuum [[sintering_process_in_metal_3d_printing | sintering]] furnace) <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.
    *   The [[sintering_process_in_metal_3d_printing | sintering cycle]] typically takes about 12 hours <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>. This process converts the green part into solid metal with very high quality, typically 99% density, similar to other [[sintering_process_in_metal_3d_printing | sintered powder metallurgy parts]] <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>.

### Comparison to Other Metal 3D Printing Methods

While standard metal 3D printing methods allow for any complexity, their surface finish and resolution for micron-level details are often not ideal <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. The [[advantages_and_challenges_of_laser_metal_3d_printing | "Cast to Sinter" method provides superior resolution and surface finish]] but introduces more manual steps and potential distortion compared to automated metal 3D printing processes <a class="yt-timestamp" data-t="00:34:08">[00:34:08]</a>. The [[comparison_of_metal_3d_printing_and_traditional_manufacturing | cost implications and applications of this novel 3D printing method]] highlight its suitability for specialized applications rather than high-volume automated production <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>. The [[casting_processes_for_plastics_and_metals | casting nature of the process]] means it shares some limitations with traditional casting in terms of shape complexity (e.g., inability to create infills) <a class="yt-timestamp" data-t="00:36:01">[00:36:01]</a>.