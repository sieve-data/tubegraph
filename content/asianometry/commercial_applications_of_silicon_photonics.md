---
title: Commercial Applications of Silicon Photonics
videoId: 29aTqLvRia8
---

From: [[asianometry]] <br/> 

[[introduction_to_silicon_photonics | Silicon Photonics]] is a technology that applies modern nanoscale CMOS processes to the optical realm <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. It focuses on technologies that transmit and manipulate light in the form of light particles or photons <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>. This field is closely related to optical data transmission <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

## Evolution of Data Transmission
Historically, networking companies used electrical signals sent through copper wire <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. However, electrons in copper wires interact with other atoms, causing slowdowns and heat generation <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. By the 1990s, the increasing data traffic network demands became a significant challenge <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.

A revolution occurred in long-distance communications when companies switched to using light sent via optical fiber <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. Light moves through optical fiber at the speed of light, enabling super high frequencies and thus higher data volume transmissions <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. Engineers further advanced this by sending multiple signals through the same fiber using different, non-interfering light wavelengths <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. Today, optical fiber technologies dominate long-distance communication, with over 2 billion kilometers deployed globally <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.

## Core Components of a Photonic System
Researchers aim to incorporate a complete photonic system onto a single monolithic silicon chip <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. Such a system would ideally have five components:
1.  **Light Source:** Typically a laser <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.
2.  **Routes and Pathways:** Passive structures to manipulate light (bend, guide, filter, couple, split, combine) within the integrated chip <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.
3.  **Modulator:** Converts digital electronic signals into digital optical signals <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.
4.  **Photo Detector:** Converts digital optical signals into digital electronic signals <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. A component that can do both is called a transceiver <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
5.  **Traditional CMOS Electronics:** Support functions like encoding and decoding data <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>.

## [[challenges_in_silicon_photonics_development | Challenges]] and Workarounds
[[introduction_to_silicon_photonics | Silicon Photonics]] faces two major [[challenges_in_silicon_photonics_development | challenges]] for a fully integrated pure silicon device:
*   **Light Emission:** Crystalline [[evolution_and_uses_of_silicon_wafer_in_technology | silicon]] has an indirect band gap, preventing it from naturally emitting light or "lasing" <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. While modifications like boron implantation have created silicon-based LEDs, commercial silicon-based lasers are still not yet available <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.
*   **Modulation:** [[evolution_and_uses_of_silicon_wafer_in_technology | Silicon]]'s crystal structure does not exhibit the Pockels effect, which allows an electric field to control light's speed <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>. This means it cannot directly convert digital electrical signals into digital light signals efficiently <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

To overcome the light source issue, engineers have adopted workarounds:
*   Using an external laser positioned outside the chip <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>.
*   Bonding a pre-made laser from a different material (e.g., indium phosphide) onto the silicon, known as hybrid integration <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. Most commercial [[introduction_to_silicon_photonics | silicon photonics]] providers currently use one of these two methods <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>.

Significant progress has been made in silicon modulators since the 1980s and 1990s, particularly in shrinking device size and speeding up throughput <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>. In 2004, Intel announced the first high-speed silicon-based optical modulator with over 1 GHz bandwidth <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>. By 2012, Intel unveiled its first fully integrated CMOS [[introduction_to_silicon_photonics | silicon photonics]] transceiver, fabricated with a 90-nanometer process <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

## Commercial Opportunities

### Data Centers
The [[introduction_to_silicon_photonics | silicon photonics]] industry found its first major commercialization opportunity within data centers <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>. Hyperscalers (e.g., Alibaba, AWS, Google, Microsoft) build immense data centers with immense data traffic between servers <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>.
*   **Transceivers:** These products convert between digital optical and digital electrical signals <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. Traditionally, transceivers are separate units plugged into switch gear <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>.
*   **Integration:** With [[introduction_to_silicon_photonics | silicon photonics]], transceiver functionality can be integrated directly onto the chip, replacing legacy components <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>. This integration saves on cost, power, and labor, while also addressing bandwidth bottlenecks <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.
*   **Market Impact:** Companies like Intel, Cisco, and Macom sell millions of these units annually <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>. [[introduction_to_silicon_photonics | Photonic components]] are expected to continue taking market share from legacy optics and copper wire <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>.

### Sensors and Lidar
Besides data centers, [[introduction_to_silicon_photonics | silicon photonics]] has potential in sensor and lidar markets <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>.
*   **Lidar (Light Detection and Ranging):** Uses light to acquire a 3D picture of an environment, similar to radar but with higher resolutions due to smaller optical light waves <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>. It is crucial for autonomous driving <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>.
*   **Current Lidar Issues:** Traditional lidar setups are expensive (up to $70,000 per system) and bulky <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>.
*   **[[introduction_to_silicon_photonics | Silicon Photonics]] Solution:** A [[introduction_to_silicon_photonics | silicon photonics]]-based lidar system can integrate many discrete optical components onto a single chip, drastically reducing costs and size <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>.
*   **Key Players:** Intel subsidiary Mobileye has presented a small lidar system-on-chip with integrated lasers <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>. Other notable companies include Point Cloud, Aeva, Voyant Photonics, and Analog Photonics <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>.

## Production and Market Dynamics
[[introduction_to_silicon_photonics | Silicon photonics]] products typically use [[silicon_wafer_manufacturing_process_and_challenges | silicon-on-insulator (SOI) wafers]], which have special layers (like silicon dioxide) that help confine light due to contrasting refractive indices <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>. This necessitates a slightly different fabrication process, often a few years behind the leading edge of [[advancements_in_semiconductor_technology | semiconductor technology]] <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.

*   **Foundries:** This makes it a specialty node, offering opportunities for foundries not competing at the leading edge <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>. GlobalFoundries is considered a market leader in this space, having acquired relevant IP from IBM <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>. Intel has also been an R&D pioneer <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>. TSMC has historically offered less in this area, but their current strategy seems focused on integration schemes that allow [[introduction_to_silicon_photonics | silicon photonics]] chiplets to work seamlessly with traditional [[advancements_in_semiconductor_technology | semiconductors]] <a class="yt-timestamp" data-t="12:28:00">[12:28:00]</a>.

Despite its promise, the current market volume for [[introduction_to_silicon_photonics | silicon photonics]] remains a [[challenges_in_silicon_photonics_development | challenge]]. For example, the transceiver market is estimated to sell 50-75 million units annually, requiring only about 40-60,000 200mm SOI wafers for the entire industry <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>. This volume is less than a month's production for a typical mega-fab, making it a smaller focus for large foundries like TSMC <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>.

## [[future_potential_of_silicon_photonics_technology | Future Potential]]
The long-standing dream since the 1970s is to replace copper wiring on chips with optical fiber to create a [[introduction_to_silicon_photonics | silicon photonics]] microprocessor that could disrupt traditional [[advancements_in_semiconductor_technology | semiconductors]] <a class="yt-timestamp" data-t="13:45:00">[13:45:00]</a>.
*   **Scalability [[challenges_in_silicon_photonics_development | Challenge]]:** However, [[photonics components]] cannot be made smaller than the wavelengths of the light they carry (around one micrometer) <a class="yt-timestamp" data-t="14:00:00">[14:00:00]</a>. In contrast, leading-edge transistors are now only a few nanometers large <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>. At the 7-nanometer node, a single square micrometer can house over a hundred transistors <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>. This high opportunity cost pushes the industry away from highly integrated [[introduction_to_silicon_photonics | silicon photonics]] monoliths towards packaging solutions that pair [[photonics]] and traditional chiplets together <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>.

Despite the [[challenges_in_silicon_photonics_development | challenges]], [[introduction_to_silicon_photonics | silicon photonics]] remains a technology with significant [[future_potential_of_silicon_photonics_technology | future potential]] <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>. The key is to find a commercial market large and valuable enough to fulfill this potential <a class="yt-timestamp" data-t="15:27:00">[15:27:00]</a>.