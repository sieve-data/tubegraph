---
title: Overview of ASMLs Extreme Ultraviolet Lithography
videoId: en7hhFJBrAI
---

From: [[asianometry]] <br/> 

Currently, [[Extreme Ultraviolet Lithography Technology | Extreme Ultraviolet Lithography]] (EUVL) is operational, utilizing dozens of $150 million machines to create patterns nanometers wide <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The industry has worked for decades on this complex technology, but the development continues <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. [[ASMLs role in semiconductor manufacturing | ASML]] is already developing the next generation of [[Extreme Ultraviolet Lithography Technology | EUV]], known as High [[future_developments_in_euv_systems_by_asml | NA EUV]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This $300 million machine is designed to surpass regular [[Extreme Ultraviolet Lithography Technology | EUV]] in performance <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Current Challenges with EUV

While [[Extreme Ultraviolet Lithography Technology | EUV]] technically functions, significant commercial challenges persist, primarily related to throughput – the number of wafers a single machine can produce <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

*   **Throughput Limitations**: TSMC's leading-edge N5 process requires 14 to 15 [[Extreme Ultraviolet Lithography Technology | EUV]] layers <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. [[Extreme Ultraviolet Lithography Technology | EUV]] machines are slower than older lithography machines, necessitating more units to maintain wafer output <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. In 2020, TSMC acquired 50% of [[ASMLs role in semiconductor manufacturing | ASML's]] installed [[Extreme Ultraviolet Lithography Technology | EUV]] base by the second half of the year <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **High Costs**: Each N5 wafer is estimated to cost nearly $17,000, which is a theoretical 80% price increase <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Reducing this cost requires higher wafer output, which in turn demands faster throughput <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Increased EUV Layers for Newer Nodes**: TSMC's next node, N3, uses 20 to 25 [[Extreme Ultraviolet Lithography Technology | EUV]] layers, compared to N5's 14-15 layers <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This increases the risk of further throughput decline, hindering the ability to achieve economies of scale <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Multiple Patterning**: To improve feature density for N3, foundries like TSMC may resort to multiple patterning, where additional exposures are used <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. While this can enable finer features (e.g., cutting a 13nm wide noodle with a 26nm mold through careful repositioning for a second pass) <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>, it doubles or triples the processing time per layer <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This makes already slow [[Extreme Ultraviolet Lithography Technology | EUV]] decidedly uneconomical <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

The more economical solution is to acquire [[Extreme Ultraviolet Lithography Technology | EUV]] machines that perform lithography better and faster <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## Introducing High NA EUV

The solution to these challenges is High [[future_developments_in_euv_systems_by_asml | NA EUV]] <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. "NA" stands for Numerical Aperture, a dimensionless number that measures how much light an optical system can collect and focus <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

According to Rayleigh's formula, resolution is equal to `k1 * light wavelength / NA` <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. To improve resolution, one must shrink `k1` or the wavelength, or increase the NA <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

*   `k1` is near its physical limit <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   The first generation of [[Extreme Ultraviolet Lithography Technology | EUV]] already reduced the wavelength to 13.5 nanometers, making further reductions difficult <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   Therefore, the primary remaining factor to improve is the NA by re-engineering the optics to collect and focus more [[Extreme Ultraviolet Lithography Technology | EUV]] light <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

[[ASMLs role in semiconductor manufacturing | ASML's]] most advanced current [[Extreme Ultraviolet Lithography Technology | EUV]] machine, the NXE 3600D, has an NA of 0.33, which translates to a 26-nanometer pitch and meets TSMC's N5 process requirements (28nm pitch) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This machine can process about 160 wafers per hour <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

[[ASMLs role in semiconductor manufacturing | ASML's]] first High [[future_developments_in_euv_systems_by_asml | NA EUV]] machine, the **EXE 5000**, will increase the NA from 0.33 to 0.55 <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This translates to a 16-nanometer pitch, a 67% improvement, making it the preferred method for the N3 process <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

High [[future_developments_in_euv_systems_by_asml | NA EUV]] can print with a much smaller pitch and at a higher resolution, leading to fewer defects and more good wafers <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. It can potentially replace layers previously done with multi-patterning, as it can achieve the same results in a single pass, justifying its cost <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Technical Innovations in High NA EUV

There are two main engineering challenges for High [[future_developments_in_euv_systems_by_asml | NA EUV]]: the optics and the resist <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Optics Redesign (Zeiss Starlith 5000)

The optics system, particularly the Starlith 5000 from Zeiss, needed a redesign <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. The goal is to allow light at more angles to hit the wafer <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

*   **Thicker Light Cone**: Previous 0.33 NA systems had a thinner light cone at Mirror 6 (M6), directly above the wafer <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. To achieve 0.55 NA, this cone needs to be thicker <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Mirror 5 Challenge**: With a thicker M6 light cone, the Mirror 5 (M5), positioned just before it, presents a challenge <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Multi-layer mirrors reflect [[Extreme Ultraviolet Lithography Technology | EUV]] at specific angles (around 13 degrees), so M5 must be close to the M6 light cone <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. This setup causes the two light cones to interfere, leading to imaging errors <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Obscurations (Holes in Mirrors)**: The solution involves drilling oval-shaped "obscurations" (holes) into the mirrors <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. These reduce the angular spread on the mirrors and significantly increase the transmission of the optics <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### Addressing Mask Interference

A similar interference effect occurs at the reticle (mask), which contains the chip design pattern <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Mask redesigns cost millions, so the mask size cannot change for High [[future_developments_in_euv_systems_by_asml | NA EUV]] <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

*   **NA Link**: High NA at the wafer stage requires high NA at the mask stage <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. The Twinscan NXE 3300B has a 0.33 NA and a 4x magnification factor <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Its reticle reflects [[Extreme Ultraviolet Lithography Technology | EUV]] light at 6 degrees, projecting a 132mm x 104mm reticle area onto a 33mm x 26mm wafer area <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Light Cone Overlap**: Increasing the NA results in bigger light cones that overlap by one degree <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Raising the [[Extreme Ultraviolet Lithography Technology | EUV]] light reflection angle (e.g., from 6 to 9 degrees) is not feasible due to "mask shadowing effects" <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Magnification Factor Adjustment**: The magnification factor was increased from 4x to 8x <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. While this achieves higher NA without fatter cones or mask shadows, it shrinks the projected wafer area to a quarter of its original size (16.5mm x 13mm) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. This reduction makes the machine four times slower, which is economically unacceptable for customers <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Anamorphic Imaging**: To address the shrinking field size, [[ASMLs role in semiconductor manufacturing | ASML]] and Zeiss implemented anamorphic imaging, a technology borrowed from the movie industry <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. This allows different magnification factors for the x and y axes <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. By applying 8x magnification only along the y-axis, the system can project a 16.5mm x 26mm field, which is a more acceptable half-size <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. This solution was announced in 2014 <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

### Photoresist Challenges

The photoresist is applied on top of the substrate before [[Extreme Ultraviolet Lithography Technology | EUV]] exposure <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. A higher NA requires a thinner resist layer to reduce the risk of pattern or line collapse <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. If the resist is too thick, lines can be too close, and during drying, surface tension can distort the design or cause lines to fall over <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. The target is a resist layer at least 50% thicker than the pitch; for a 16nm pitch, this means a 20nm thick resist <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. [[ASMLs role in semiconductor manufacturing | ASML]] is collaborating with partners like imec, PSI, and CXRO to find suitable new resists, a challenge still ongoing <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### Other Engineering Hurdles

Other engineering challenges include:
*   Making bigger mirrors <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   Mask frame layout <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   Pellicle development <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   **Metrology System**: Inspecting features less than 20 nanometers wide is particularly challenging <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. [[ASMLs role in semiconductor manufacturing | ASML]] is exploring e-beam inspection techniques, but this is yet to be finalized <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

## Future Outlook and Cost

The EXE 5000 machine remains under development <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. The first machines are anticipated to reach customers in late 2022 <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. An improved version, the **EXE 5200**, is expected in 2024 or 2025, with an anticipated throughput of 220 wafers per hour <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

The EXE 5000 will be massive, comparable in size to a crouched T-Rex <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. It will also come with a colossal price tag, topping **$300 million each** <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>. This engineering marvel must justify its monstrous price tag <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.