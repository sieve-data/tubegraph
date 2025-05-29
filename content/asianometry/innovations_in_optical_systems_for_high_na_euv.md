---
title: Innovations in Optical Systems for High NA EUV
videoId: en7hhFJBrAI
---

From: [[asianometry]] <br/> 

Extreme Ultraviolet (EUV) lithography is a critical technology in modern semiconductor manufacturing, enabling the creation of intricate patterns just nanometers wide. Currently, foundries utilize dozens of 150 million dollar EUV machines for their processes <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. However, the industry is already looking ahead to the next generation: [[High Numerical Aperture EUV Machines | High NA EUV]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This advanced system, developed by [[ASML and highvolume EUV systems | ASML]] and its partners, aims to overcome existing limitations and push the boundaries of nanolithography even further <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## The Need for High NA EUV

While current EUV technology technically works, it faces substantial [[Challenges in developing commercial EUV systems | commercial challenges]], particularly regarding throughput – the number of wafers a single machine can produce over time <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. For instance, TSMC's leading-edge N5 process requires 14 to 15 EUV layers <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Since EUV machines are slower than older lithography systems, more machines are needed to maintain wafer output <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. By the second half of 2020, TSMC had acquired 50% of the installed EUV base to address this <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

Despite these efforts, each N5 wafer is estimated to cost around $17,000, leading to a significant price jump <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. To reduce costs, faster throughput is necessary <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. TSMC's N3 node uses even more EUV layers (20-25 compared to N5's 14-15), posing a risk of further throughput decline and hindering economies of scale <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

Current EUV machines often resort to a technique called **multiple patterning** to improve feature density <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This involves using another exposure pass to achieve finer features, such as cutting a 13-nanometer wide "noodle" with a 26-nanometer mold by making a second, carefully positioned pass <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. However, multiple patterning doubles or even triples the time to process a single layer, making EUV decidedly uneconomical <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Since [[Challenges in manufacturing EUV lithography machines | ASML is already selling current EUV machines as fast as they can make them]] <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>, the more economical alternative is to develop EUV machines that perform lithography better and faster <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. This is the core objective of High NA EUV <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## The Role of Numerical Aperture (NA)

The "NA" in High NA stands for Numerical Aperture, a dimensionless number that measures how much light an optical system can collect and focus <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. The fundamental principle for improving resolution in lithography is described by **Rayleigh's formula**:

> Resolution = k1 × light wavelength / NA <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>

To improve resolution, one must either shrink the k1 factor, reduce the light wavelength, or increase the NA <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   The k1 factor has a physical limit that is nearly reached <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   The first generation of EUV already brought the light wavelength down to its current 13.5 nanometers, making further significant reductions challenging <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

Therefore, the last major factor remaining is to increase the NA by re-engineering the optics to collect and focus more EUV light <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

ASML's most advanced current EUV machine, the NXE 3600D, has an NA of 0.33, which translates to a 26-nanometer pitch and meets TSMC's N5 process requirements (28-nanometer pitch) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This machine can churn out about 160 wafers per hour <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

The first High NA EUV machine from ASML, the EXE 5000, will increase the NA from 0.33 to 0.55 <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This translates to a 16-nanometer pitch, representing a 67% improvement <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. This increased NA is the preferred method for the N3 process <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Beyond smaller pitches, High NA EUV also promises higher resolution, leading to fewer defects and thus more good wafers produced <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. If successful, High NA EUV could replace layers previously done with costly and slow multi-patterning, justifying its significant investment <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Engineering Challenges in Optics

Developing [[High Numerical Aperture EUV Machines | High NA EUV]] involves two major [[Challenges in developing commercial EUV systems | challenges]]: the optics and the photoresist <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. The optics, particularly the Starlith 5000 system from Zeiss, present complex engineering hurdles <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

Current EUV systems (like the Starlith 3000 series) consist of collector optics, aperture illumination optics, a mask (reticle), and projection optics before hitting the wafer <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. To achieve a higher NA, the Starlith 5000 must be redesigned to allow light at more angles to hit the wafer <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### Mirror Redesign

The shift from 0.33 NA to 0.55 NA means making the light cone thicker at Mirror 6 (M6), which is positioned right above the wafer <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The primary challenge arises with Mirror 5 (M5), located just before M6 <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Due to the very specific reflection angles (around 13 degrees) required by multi-layer mirrors (with their 50 EUV reflecting layers), the M5 mirror must be positioned very close to the M6 light cone <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

With a thicker M6 light cone, the two light cones from M5 and M6 would interfere, causing significant imaging errors <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. The ingenious solution developed by Zeiss involves drilling oval-shaped holes, termed **obscurations**, into the mirrors <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. These obscurations reduce the angular spread on the mirrors and significantly increase the transmission of the optics <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### Mask and Magnification Redesign

A similar optical challenge occurs at the reticle or mask stage <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The mask, which contains the chip design pattern, is essentially a grating in front of a mirror <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. A key design requirement for High NA EUV is that the mask size cannot change, as redesigning a mask costs millions of dollars <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

To achieve a High NA at the wafer stage, a High NA is also required at the mask stage, as the two are mathematically linked <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. In current systems like the Twinscan NXE 30300B (0.33 NA), the reticle mirror reflects EUV light at 6 degrees, projecting a 132mm x 104mm reticle area onto a 33mm x 26mm wafer area with a 4x magnification factor <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

Increasing the NA leads to larger, overlapping light cones at the mask stage <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. While raising the EUV light reflection angle (e.g., from 6 to 9 degrees) might seem an obvious solution, it creates undesirable mask shadowing effects <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. The only other variable left to change is the magnification factor <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

Engineers increased the magnification from 4 times to 8 times <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. This achieved the higher NA without fatter cones or compromising mask shadows <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. However, magnifying something further makes the light area at the wafer end smaller <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. The 33mm x 26mm wafer area shrinks to a quarter of its original size, specifically 16.5mm x 13mm <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. This reduced area is economically unacceptable for customers, as it would make the EUV machine too slow <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

The ultimate solution implemented by Zeiss and ASML is **anamorphic imaging** <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. Borrowing technology from the movie industry, anamorphic imaging allows different magnification factors along the x and y axes <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. By applying the 8x magnification factor only along the y-axis, the system can project a 16.5mm x 26mm field – a half-size reduction that is just barely acceptable <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

## Other Challenges

While optics constitute the majority of the [[Challenges in manufacturing EUV lithography machines | technical challenges]], other areas like the photoresist and metrology also pose significant hurdles <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.

### Photoresist Challenges

A higher NA requires the photoresist to be thinner to reduce the risk of pattern collapse or line collapse <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. If the resist is too thick, lines after EUV exposure can be too close, and during the drying process, surface tension can distort the design, or lines might even fall over <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. The aim is a resist layer at least 50% thicker than the pitch; for a 16-nanometer pitch, this means a 20-nanometer thick resist <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. Companies are actively experimenting with new resists, and [[ASML and highvolume EUV systems | ASML]] is collaborating with partners like IMEC, PSI, and CXRO to find a suitable candidate <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### Metrology Challenges

[[Challenges in EUV Photoresist and Metrology | Metrology]], the system of sensors and programs that checks progress and quality, is crucial but also challenging for High NA EUV <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. Inspecting features less than 20 nanometers wide is difficult <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. [[ASML and highvolume EUV systems | ASML]] is exploring e-beam inspection techniques, but this is still being finalized <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

## Future Outlook

The [[High Numerical Aperture EUV Machines | High NA EUV]] EXE 5000 machine remains in development, with initial deliveries to customers expected in late 2022 <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. An improved version, the EXE 5200, is anticipated by 2024 or 2025, with an expected throughput of 220 wafers per hour <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. This machine will be massive, as big as a crouched T-Rex <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>, and is projected to cost over 300 million dollars each <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. The EXE 5000 represents an engineering marvel, but its monstrous price will require significant justification through its performance and economic benefits <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.