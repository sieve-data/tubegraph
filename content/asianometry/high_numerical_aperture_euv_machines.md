---
title: High Numerical Aperture EUV Machines
videoId: en7hhFJBrAI
---

From: [[asianometry]] <br/> 

[[development_of_uv_and_euv_lithography_technology | Extreme Ultraviolet (EUV) lithography]] is currently a working technology, with boundaries using dozens of $150 million machines to create patterns nanometers wide <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite decades of industry effort, there's no time to rest as [[asml_and_highvolume_euv_systems | ASML]] is already developing the next generation: High NA EUV <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This $300 million machine is designed to be superior to existing EUV systems <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Current EUV Challenges

While EUV technology technically works, it faces [[challenges_in_developing_commercial_euv_systems | substantial commercial challenges]] <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. The primary issue is throughput – the number of wafers a single machine can produce over time <a class="yt-timestamp" data-t="01:10:49">[01:10:49]</a>.

Current EUV machines are slower than older lithography systems <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>. For example, TSMC's leading-edge N5 process uses about 14 to 15 EUV layers <a class="yt-timestamp" data-t="01:21:40">[01:21:40]</a>. To maintain production volume, companies like TSMC have had to acquire more machines <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. By the second half of 2020, TSMC owned 50% of the installed EUV base <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. However, this increases costs; an N5 wafer is estimated to cost as much as a car, nearly $17,000, representing an 80% price jump <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. To reduce this cost, faster throughput is essential <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

TSMC's next node, N3, uses even more EUV layers (20-25 compared to N5's 14-15), risking further throughput decline and impacting economies of scale <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. This also makes [[impact_of_euv_technology_on_semiconductor_fabrication | multiple patterning]] likely necessary for N3 <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. Multiple patterning involves using an additional exposure to improve feature density, effectively doubling or tripling processing time for a single layer, making EUV decidedly uneconomical <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

Since [[asml_and_highvolume_euv_systems | ASML]] is already selling existing EUV machines as fast as they can make them, the more economical solution is to develop EUV machines that perform lithography better and faster <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>. This is the core purpose of High NA EUV <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.

## The Role of Numerical Aperture (NA)

NA stands for Numerical Aperture, a dimensionless number quantifying how much light an optical system can collect and focus <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. Improving resolution in lithography is governed by Rayleigh's formula: Resolution = k1 × light wavelength / NA <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. To improve resolution, one must either shrink k1 or the wavelength, or increase the NA <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.

*   **k1**: Already near its physical limit <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.
*   **Wavelength**: The first generation of EUV already reduced the wavelength to its current 13.5 nanometers, and pushing this further is not desirable in the short term <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
*   **NA**: The remaining major factor is to increase the NA by re-engineering the optics to collect and focus more EUV light <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.

## High NA EUV Specifications and Benefits

[[asml_and_highvolume_euv_systems | ASML's]] most advanced current EUV machine, the NXE 3600D, has an NA of 0.33, translating to a 26-nanometer pitch, which meets TSMC's N5 process requirements (28-nanometer pitch) <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>. It can produce about 160 wafers per hour <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.

[[asml_and_highvolume_euv_systems | ASML's]] first High NA EUV machine, the EXE 5000, will increase the NA from 0.33 to 0.55 <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>. This translates to a 16-nanometer pitch, a 67% improvement, and is the preferred method for the N3 process <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>.

Beyond smaller pitch, High NA EUV can print at a much higher resolution, resulting in fewer defects and more good wafers per day <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. If successful, High NA EUV could replace layers previously done with multiple patterning, performing the task in one pass instead of two or three <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>. Such savings would justify its high cost <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.

## Engineering Challenges

Two major [[challenges_in_manufacturing_euv_lithography_machines | engineering challenges]] are associated with High NA EUV: optics and resist <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>.

### Optics

The Starlift 5000 optics system from Zeiss is central to High NA EUV <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.
To achieve a higher NA, the system must be redesigned to allow light at more angles to hit the wafer <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>.

*   **Mirror Challenges**:
    *   Older 0.33 NA systems had a thinner light cone at Mirror 6 (M6), just above the wafer <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.
    *   Increasing NA to 0.55 means making this light cone thicker <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.
    *   Because multi-layer mirrors (with ~50 EUV reflecting layers) are limited to reflecting at specific angles (~13 degrees), the Mirror 5 (M5) must be positioned very close to the M6 light cone <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.
    *   This proximity causes the two light cones to interfere, leading to significant imaging errors <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>.
    *   The solution involves drilling oval-shaped holes, termed "obscurations," into the mirrors. These reduce angular spread and significantly increase the transmission of optics <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
    *   These mirrors are massive, a meter wide, with picometer accuracy; if scaled to Earth size, the largest aberration would be a human hair's diameter <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.

*   **Mask/Reticle Challenges**:
    *   The mask, which contains the chip design pattern, is essentially a grating in front of a mirror <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.
    *   Redesigning a mask costs millions of dollars, so a key requirement for High NA EUV is that the mask size cannot change <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.
    *   Achieving high NA at the wafer stage requires high NA at the mask stage <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.
    *   Current systems (like the Twinscan NXE 3300B) have a 0.33 NA and a 4x magnification factor, reflecting EUV light at 6 degrees <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>. This projects a 132x104 mm reticle area onto a 33x26 mm wafer area <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.
    *   Increasing the NA causes the light cones to overlap by one degree <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.
    *   Raising the EUV light reflection angle (e.g., from 6 to 9 degrees) is not feasible due to mask shadowing effects <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.
    *   The solution involved changing the magnification factor from 4x to 8x <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>. This achieves the higher NA without fatter cones or compromising mask shadows <a class="yt-timestamp" data-t="10:13:00">[10:13:00]</a>.
    *   However, magnifying by 8x shrinks the light area at the wafer end to a quarter of its original size (16.5x13 mm) <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>. This is economically unacceptable for customers, as it would make the EUV machine four times slower <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>.
    *   Making a larger mask (e.g., 12 inches) is not feasible as the machine cannot handle it <a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a>.
    *   The ultimate solution, developed by Zeiss and [[asml_and_highvolume_euv_systems | ASML]] since 2014, is [[innovations_in_optical_systems_for_high_na_euv | anamorphic imaging]] <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>. This technology, borrowed from the movie industry, allows magnification factors to exist independently on the x and y axes <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>. By only applying the 8x magnification along the y-axis, the system can project a 16.5x26 mm field, which is half the size but "just barely acceptable" <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>.

### Resist

The photoresist is applied to the substrate before EUV exposure <a class="yt-timestamp" data-t="12:08:00">[12:08:00]</a>. For High NA EUV, the resist needs to be thinner to reduce the risk of pattern or line collapse <a class="yt-timestamp" data-t="12:25:00">[12:25:00]</a>. If the resist is too thick, lines can be too close and may fall over or peel off during the washing and drying process due to surface tension <a class="yt-timestamp" data-t="12:34:00">[12:34:00]</a>. The goal is a resist layer at least 50% thicker than the pitch; for a 16-nanometer pitch, this means a 20-nanometer thick resist <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>. Companies like [[asml_and_highvolume_euv_systems | ASML]], IMEC, PSI, and CXRO are actively working on finding a suitable new resist candidate <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>.

### Other Engineering Challenges

Additional challenges include:
*   Making bigger mirrors <a class="yt-timestamp" data-t="13:21:00">[13:21:00]</a>.
*   The mask frame layout <a class="yt-timestamp" data-t="13:24:00">[13:24:00]</a>.
*   The pellicle <a class="yt-timestamp" data-t="13:26:00">[13:26:00]</a>.
*   The [[metrology_in_euv_lithography | metrology system]] (sensors and programs for quality control) <a class="yt-timestamp" data-t="13:29:00">[13:29:00]</a>. Inspecting features less than 20 nanometers wide is particularly challenging, and [[asml_and_highvolume_euv_systems | ASML]] is exploring e-beam inspection techniques <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>.

## Development and Cost

The EXE 5000 machine remains in development <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>. The first machines were expected to be delivered to customers in late 2022 <a class="yt-timestamp" data-t="14:00:00">[14:00:00]</a>. An improved version, the EXE 5200, is anticipated in 2024 or 2025, with an expected throughput of 220 wafers per hour <a class="yt-timestamp" data-t="14:09:00">[14:09:00]</a>.

The EXE 5000 will be massive, comparable in size to a crouched T-Rex <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>. Its price tag is expected to top $300 million each <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>. While an engineering marvel, its monstrous price requires significant justification <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>.