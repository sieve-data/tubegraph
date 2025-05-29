---
title: Technical and engineering aspects of high NA EUV
videoId: en7hhFJBrAI
---

From: [[asianometry]] <br/> 

Currently, [[euv_lithography_technology_and_its_challenges | Extreme Ultraviolet (EUV) lithography]] is a working technology, with companies utilizing dozens of $150 million machines to create patterns nanometers wide <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, there are still substantial commercial [[challenges_in_developing_euv_systems | challenges]] despite decades of industry effort <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The most significant problem is throughput, or how many wafers a single machine can produce over time <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

For instance, TSMC's n5 process requires 14 to 15 EUV layers <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Since EUV machines are slower than older technologies, more machines are needed to maintain wafer output <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. By the second half of 2020, TSMC had acquired 50% of the installed EUV base <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This approach is costly, with each n5 wafer estimated to cost as much as a car, or nearly $17,000, representing an 80% price jump <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. To reduce costs, faster throughput is essential <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

TSMC's n3 node uses even more EUV layers, about 20 to 25, compared to n5's 14 to 15 <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This risks further throughput decline and makes it harder to achieve economies of scale <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Additionally, TSMC may have to use multiple patterning for n3, which involves multiple exposures to improve feature density <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. While this can achieve finer patterns, it doubles or triples the processing time for a single layer, making [[euv_lithography_technology_and_its_challenges | EUV]] decidedly uneconomical <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

The more economical alternative is to use EUV machines that perform lithography better and faster <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This is where [[challenges_and_potential_of_high_na_euv_technology | High NA EUV]] comes in <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## High NA EUV and Rayleigh's Formula

High NA EUV refers to an increased numerical aperture (NA), a dimensionless number measuring how much light an optic system can collect and focus <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. According to Rayleigh's formula, resolution equals k1 times light wavelength divided by NA <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Improving resolution requires shrinking k1, reducing the wavelength, or increasing the NA <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

*   **k1 Factor**: K1 has a physical limit that is nearly reached <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Wavelength**: The first generation of EUV already brought the light wavelength down to its current 13.5 nanometers, making further significant reductions unlikely soon <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Numerical Aperture (NA)**: Therefore, raising the NA by re-engineering the optics to collect and focus more EUV light is the remaining major factor <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

ASML's most advanced current EUV machine, the NXE 3600D, has an NA of 0.33, translating to a 26-nanometer pitch, which meets TSMC's n5 process requirements (28-nanometer pitch) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This machine can produce about 160 wafers per hour <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

ASML's first [[challenges_and_potential_of_high_na_euv_technology | High NA EUV]] machine, the EXE 5000, will increase the NA from 0.33 to 0.55, resulting in a 16-nanometer pitch <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This is a 67% improvement and the preferred method for the n3 process <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. Beyond smaller pitches, [[challenges_and_potential_of_high_na_euv_technology | High NA EUV]] can print at much higher resolution, reducing defects and increasing the yield of good wafers <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. If successful, it could replace layers previously done with multi-patterning, saving significant time and justifying its use <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

## Engineering Challenges

Two major [[challenges_in_developing_euv_systems | challenges]] associated with [[challenges_and_potential_of_high_na_euv_technology | High NA EUV]] are the optics and the photoresist <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Optics

The optics system, specifically the Zeiss StarLight 5000, must be redesigned to allow light at more angles to hit the wafer, thus achieving a higher NA <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

The older 0.33 NA systems had a thinner light cone at Mirror 6 (M6), which is right above the wafer <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Increasing the NA to 0.55 means making this cone thicker <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This creates a significant challenge with Mirror 5 (M5), the mirror directly before M6 <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

Multi-layer mirrors, with their 50 EUV reflecting layers, are limited to reflecting at very specific angles (about 13 degrees) <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. This requires the M5 mirror to be positioned very close to the M6 light cone <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. In a high NA setup, the two light cones would interfere, causing significant imaging errors <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

**Solution: Obscurations**
Zeiss's solution was to drill oval-shaped holes, called "obscurations," into the mirrors <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. These holes reduce the angular spread on the mirrors and significantly increase the transmission of the optics <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### Mask/Reticle Challenges

A similar effect occurs at the reticle or mask stage <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The mask contains the chip design pattern <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. A key design requirement for [[challenges_and_potential_of_high_na_euv_technology | High NA EUV]] is that the mask size cannot change due to the millions of dollars it costs to redesign <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

To achieve a high NA at the wafer stage, a high NA is also required at the mask stage, as the two are mathematically linked <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. The Twinscan NXE 30300B, an EUV-enabled machine, has an NA of 0.33 and a magnification factor of 4 times <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. It projects a 132mm by 104mm reticle area onto a 33mm by 26mm wafer area <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. When increasing the NA, the two light cones at the mask also become bigger and overlap <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

Raising the EUV light reflection angle (e.g., from 6 to 9 degrees) is not feasible as it creates undesirable mask shadowing effects <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

**Solution: Increased Magnification (and Anamorphic Imaging)**
The alternative was to change the magnification factor, increasing it from 4 times to 8 times <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. This achieved the higher NA without fatter cones or compromising mask shadows <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

However, magnifying something reduces the light area at the end <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. The 33mm by 26mm wafer area shrinks to a quarter of its original size: 16.5mm by 13mm <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. This smaller area is economically unacceptable for customers, as it would make the EUV machine four times slower <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

**Solution: Anamorphic Imaging**
To address this, Zeiss and ASML adopted anamorphic imaging, a technique borrowed from the movie industry <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. Magnification factors can exist independently on both the x and y axes <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. By applying the 8x magnification along only the y-axis (not the x-axis), the system can project a 16.5mm by 26mm field, which is half the original size but barely acceptable <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

### Resist Challenges

The photoresist, applied on top of the substrate before EUV exposure, also presents [[challenges_in_developing_euv_systems | challenges]] <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. A higher NA necessitates a thinner resist layer to lower the risk of pattern or line collapse <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. If the resist is too thick, lines after EUV exposure will be too close together <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. During drying after washing, the surface tension of water can distort the design, causing lines to fall over or peel off if they don't dry simultaneously <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. Ideally, the resist layer should be at least 50% thicker than the pitch, meaning a 20-nanometer thick resist for a 16-nanometer pitch <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

Companies, including ASML in partnership with IMEC, PSI, and CXRO, are actively experimenting with new resist materials to find suitable candidates <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. As of the video's creation, this is still an ongoing development <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

### Other Engineering Challenges

Other [[challenges_in_developing_euv_systems | engineering challenges]] for [[challenges_and_potential_of_high_na_euv_technology | High NA EUV]] include <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>:
*   Making bigger mirrors <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
*   The mask frame layout <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.
*   The pellicle <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   The metrology system: This system of sensors and programs checks progress and quality <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. Inspecting features less than 20 nanometers wide is challenging <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. ASML is exploring e-beam inspection techniques, but this is yet to be finalized <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

## Development and Cost

[[future_developments_in_euv_systems_by_asml | ASML]]'s High NA EUV machine, the EXE 5000, remains in development <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. The first machines were expected to be delivered to customers in late 2022 <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. An improved version, the EXE 5200, is anticipated by 2024 or 2025, with an expected throughput of 220 wafers per hour <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

The EXE 5000 will be massive, comparable in size to a crouched T-Rex <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. It will also come with a colossal price tag, topping $300 million per machine <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. While an engineering marvel, its monstrous price requires justification <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.