---
title: Extreme Ultraviolet Lithography and its Challenges
videoId: en7hhFJBrAI
---

From: [[asianometry]] <br/> 

Extreme Ultraviolet (EUV) lithography is a crucial technology in modern semiconductor manufacturing, enabling the creation of intricate patterns just nanometers wide <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Currently, dozens of [[challenges_in_manufacturing_euv_lithography_machines | EUV machines]], each costing $150 million, are in use <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The semiconductor industry has invested decades of effort into this complex technology <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

Despite its impressive functionality <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, significant commercial challenges remain, primarily concerning throughput – the number of wafers a single machine can produce over time <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Current Commercial Challenges

*   **Throughput Limitations:** EUV machines are slower than older lithography equipment <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. For instance, TSMC's N5 process incorporates 14 to 15 EUV layers <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. To maintain production volume, more machines are required <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. By late 2020, TSMC owned 50% of the installed EUV base <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **High Manufacturing Costs:** The cost of an N5 wafer is estimated by industry analysts to be around $17,000, representing a theoretical 80% price increase <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. To reduce this cost, faster throughput is necessary <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Increasing EUV Layers in Newer Nodes:** TSMC's next full-step node, N3, utilizes even more EUV layers, ranging from 20 to 25, compared to N5's 14 to 15 <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This increases the risk of further throughput decline <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Multiple Patterning:** To improve feature density, particularly for nodes like N3, semiconductor foundries may resort to multiple patterning <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This technique involves multiple exposures to achieve smaller features (e.g., cutting a 13nm wide noodle with a 26nm mold by making a second pass) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. However, it can double or triple the processing time for a single layer <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>, making EUV decidedly uneconomical <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## High Numerical Aperture (High NA) EUV

The more economical alternative to buying more standard EUV machines is to acquire EUV machines that perform lithography better and faster <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This is the purpose of High NA EUV <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

*   **Numerical Aperture (NA):** NA is a dimensionless number that quantifies how much light an optical system can collect and focus <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Rayleigh's Formula:** Resolution is equal to k1 multiplied by light wavelength, divided by NA <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. To improve resolution, one must either shrink k1, reduce the wavelength, or increase the NA <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Since k1 is nearing its physical limit and the 13.5nm wavelength is already established for EUV <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>, increasing the NA by re-engineering the optics is the remaining major factor <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Capabilities of High NA EUV

[[asml_and_the_commercialization_of_euv_lithography | ASML]]'s most advanced current EUV machine, the NXE 3600D, has an NA of 0.33, resulting in a 26nm pitch <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. This meets TSMC's N5 process requirements for a 28nm pitch and can produce about 160 wafers per hour <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

[[asml_and_the_commercialization_of_euv_lithography | ASML]]'s first High NA EUV machine, the EXE 5000, is designed to increase the NA from 0.33 to 0.55 <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

*   **Improved Pitch:** This NA increase translates to a 16nm pitch <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>, a 67% improvement <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>, making it the preferred method for the N3 process <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Higher Resolution and Fewer Defects:** High NA EUV can print at a much higher resolution, leading to fewer defects and more good wafers per day <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Replacing Multi-patterning:** If effective, High NA EUV could replace layers previously done with multi-patterning at lower wavelengths, as it can achieve the desired results in a single pass <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

## [[engineering_challenges_of_the_euv_light_source | Engineering Challenges]] of High NA EUV

The [[challenges_in_developing_commercial_euv_systems | development of commercial EUV systems]], particularly High NA EUV, faces two primary engineering challenges: optics and photoresist <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Optics

[[asml_and_the_commercialization_of_euv_lithography | ASML]] works with Carl Zeiss on the Starlith 5000 optics system <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. To achieve a higher NA, the system must be redesigned to allow light at more angles to hit the wafer <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

*   **Mirror Design:** The old 0.33 NA systems had a thinner light cone at Mirror 6 (M6), directly above the wafer <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Increasing to 0.55 NA means making this cone thicker <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   **M5/M6 Interference:** The thicker M6 light cone creates interference with the Mirror 5 (M5) just before it, leading to significant imaging errors <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This is due to multi-layer mirrors, with 50 EUV reflecting layers, being limited to reflecting light at very specific angles (around 13 degrees) <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
    *   **Solutions: Obscurations:** Zeiss engineered a solution by drilling oval-shaped holes, called obscurations, into the mirrors <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. These reduce the angular spread on the mirrors and significantly increase the transmission of the optics <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Reticle/Mask Stage:** Similar challenges arise at the reticle (mask) stage, which contains the chip design pattern <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. A higher NA at the wafer stage requires a higher NA at the mask stage <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
    *   **Magnification Factor:** The NXE 30300B EUV machine has an NA of 0.33 and a magnification factor of 4x <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>, projecting a 132mm x 104mm reticle area onto a 33mm x 26mm wafer area <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. Increasing the NA makes the light cones bigger, causing them to overlap by one degree <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
    *   **Challenges of Reflection Angle:** Raising the EUV light reflection angle (e.g., from 6 to 9 degrees) is not feasible due to mask shadowing effects <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
    *   **Solution: Increased Magnification:** The magnification factor was increased from 4x to 8x <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. While this solved the fatter cone and mask shadow issues, it reduced the projected wafer area to a quarter of its size (16.5mm x 13mm) <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. This is economically unacceptable for customers <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
    *   **Anamorphic Imaging:** [[asml_and_the_commercialization_of_euv_lithography | ASML]] and Zeiss adopted anamorphic imaging, a technology borrowed from the movie industry <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. This allows different magnification factors on the X and Y axes <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. By applying the 8x magnification only along the Y-axis, the system can project a 16.5mm x 26mm field <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>, which is half-size but "just barely acceptable" <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

### [[challenges_in_euv_photoresist_and_metrology | Photoresist]]

The photoresist, applied to the substrate before EUV exposure <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>, also presents a challenge. A higher NA necessitates a thinner resist layer to reduce the risk of pattern collapse or line collapse <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

*   **Pattern Collapse:** If the resist is too thick, lines might be too close together after exposure. During the washing and drying process, surface tension can distort the design, causing lines to fall over or peel off <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Resist Thickness Requirement:** Ideally, the resist layer should be at least 50% thicker than the pitch. For a 16nm pitch, this means a 20nm thick resist <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. Companies, including [[asml_and_the_commercialization_of_euv_lithography | ASML]] with partners like imec, PSI, and CXRO, are experimenting with new resists <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### Other Engineering Challenges

Additional [[challenges_in_manufacturing_euv_lithography_machines | engineering challenges]] for High NA EUV include:

*   Making bigger mirrors <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
*   Mask frame layout <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
*   Pellicle <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
*   [[challenges_in_euv_photoresist_and_metrology | Metrology System]]: This system of sensors and programs checks progress and quality <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. Inspecting features less than 20 nanometers wide is challenging <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. [[asml_and_the_commercialization_of_euv_lithography | ASML]] is exploring e-beam inspection techniques, but this is not yet finalized <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

## Development and Cost

The EXE 5000 machine remains in [[development_of_uv_and_euv_lithography_technology | development]] <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. The first machines are expected to be delivered to customers in late 2022 <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. An improved version, the EXE 5200, is anticipated by 2024 or 2025, with an expected throughput of 220 wafers per hour <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

The EXE 5000 will be massive, comparable in size to a crouched T-Rex <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Its price tag will be equally immense, topping $300 million per machine <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>. This engineering marvel must justify its monstrous price through its performance and economic benefits <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.