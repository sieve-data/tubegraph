---
title: Benefits of brazing in prototype building
videoId: Vpt0gdbI4-8
---

From: [[dgelbart]] <br/> 

When constructing [[introduction_to_building_prototypes | prototypes]], particularly three-dimensional, rigid, heavy, and machinable structures, traditional methods like milling from a solid block can be expensive in terms of material and machine time <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. While machining near-net shapes (castings, forgings, or bent parts) offers advantages <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, castings are a tedious process in a research and development (R&D) environment, requiring patterns that are not easily made at home <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. An effective alternative is to build structures from segments by brazing <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Brazing vs. Welding
While industrial production often uses weldments, [[brazing_versus_welding | brazing]] has distinct advantages over welding for prototyping <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>:
*   **Skill Requirement**: Brazing requires less skill than welding <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Distortion**: Welding causes heavy distortion due to weld bead shrinkage, even with careful technique <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Brazing minimizes this issue.
*   **Dissimilar Metals**: Welding is not suitable for joining very dissimilar metals <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. For instance, you cannot weld steel and brass together <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Brazing allows each segment to be made from a different material, optimizing for specific needs like having a steel machine part with a brass boss for bearings or machining <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>, <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Prototype Assembly Process
Parts are typically cut using a water jet <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. To ensure accurate assembly, parts can be registered using tabs <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a> or small finger-like cutouts for square holes to align components <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Temporary Joining Techniques
Before brazing, parts must be temporarily secured in place. Common [[prototyping_and_temporary_welding_techniques | temporary welding techniques]] include:
*   **[[laser_welding_advantages | Laser welding advantages]]**: A laser welder is a versatile machine that can weld in hard-to-reach places as long as the spot is visible under a microscope <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. It can weld dissimilar metals because the pulse is so fast that oxidation or other issues don't have time to occur <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, even without an inert atmosphere <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. This allows for combinations like aluminum to steel, or silver to lead <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Dowel Pins**: Simple dowel pins can be used to hold parts in place <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **[[spot_welding_and_repairing_errors_in_metal_prototypes | Spot Welding]]**: Parts can also be temporarily secured using a spot welder <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Brazing Materials and Application
Brazing is performed by placing small pieces of brazing wire, typically a silver-copper alloy, and flux <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Flux is essential as it dissolves oxides and protects the metal from further oxidation, allowing the braze material to wet the metal <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

Common types of flux include:
*   **White Flux**: Primarily borax, commonly used for non-ferrous metals and also suitable for iron <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Black Flux**: Likely a fluoride salt, more aggressive and used for stainless steel and harder-to-braze materials <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

The brazing wire is the most expensive component, while fluxes are inexpensive <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. To apply, flux is spread as a paste into the corners where a fillet is desired, with excess wiped away to prevent surface defects from the flux attacking the metal at high temperatures <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>, <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. Small pieces of brazing wire are then laid at the corners, ideally half-buried in the flux, to create a sufficient fillet <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>, <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

For vertical joints, where the wire might fall off, tricks include placing more material on top hoping it will flow down, drilling a hole and inserting slugs of brazing wire and flux, or brazing in multiple steps if parts are securely pinned <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. However, it's generally better to complete the braze in one go, ensuring all gaps are filled with flux to prevent oxidation <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. Gaps should ideally be between zero and half a millimeter for good capillary action <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Brazing foil can be used for larger areas <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Oven Heating
The assembled part is placed in an oven, typically heated to about 750°C <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. The temperature should be 50-100°C above the braze alloy's melting point (e.g., 680°C melting point, set to 750°C) to ensure full melting and proper flow, but not excessively high to avoid unnecessary oxidation <a class="yt-timestamp" data-t="00:09:57">[00:10:00]</a>. After reaching temperature, the part should remain in the oven for about an hour per kilo of weight to ensure even heat absorption and equalization <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Once done, the oven is turned off, and the part is left to cool naturally to about 500°C before handling <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

## Finishing and Performance
After cooling, the brazed assembly is sandblasted <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. The result is an assembly that resembles a casting, but with the added benefit of each part potentially being made from a different metal, such as incorporating stainless steel or hardened inserts <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. The brazing creates a nice fillet due to good wetting <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. For a perfect finish, the fillets can be lightly sanded <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

### Strength and Versatility
Brazed assemblies are comparable in strength to castings and can even be stronger <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
*   **Comparison to [[comparison_of_brazed_assemblies_and_cast_iron | Cast Iron]]**: Cast iron, often used for machinery, is weaker than steel and can easily shatter when impacted <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>, <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. This inherent weakness is why cast machinery is often very heavy <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   **Brazed Assembly Strength**: A brazed "casting" made from steel can be bent significantly without breaking the joint, demonstrating much higher strength than cast iron against both regular stress and hammering <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>, <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

<div class="callout">
    Beyond its aesthetic appeal, brazing offers a versatile and strong method for creating complex metal prototypes with multiple materials, outperforming traditional casting in both material choice and durability.
</div>