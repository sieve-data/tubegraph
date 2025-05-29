---
title: Engineering challenges of the EUV light source
videoId: 5Ge2RcvDlgw
---

From: [[asianometry]] <br/> 

Extreme Ultraviolet (EUV) lithography has become a commercial reality after more than 20 years of development <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Machines from ASML, costing multi-millions of dollars, use EUV light to create incredibly small patterns on wafers <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. At the core of ASML's $150 million lithography machine is an amazing system: the [[euv_light_source_development_and_laserproduced_plasma | EUV light source]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This system utilizes lasers firing pulses at tin droplets to generate the powerful 13.5 nanometer wavelength light essential for modern microprocessors <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Key Developers
This article primarily focuses on the [[euv_light_source_development_and_laserproduced_plasma | EUV approach]] taken by Kymer, an ASML subsidiary <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Another semiconductor laser company, Gigaphoton (a subsidiary of Komatsu), is also working on reliably generating UV light with its own unique method <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Historical Context and Initial Requirements
For a long time, the semiconductor industry used 193 nanometer wavelength light for etching <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Techniques like immersion lithography (shooting light through ultra-pure water) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a> and double patterning (using additional exposures to improve feature density) extended its usefulness <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. However, the industry eventually needed to transition to EUV light at 13.5 nanometers <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Scientists and engineers identified two fundamental requirements for the next-generation [[euv_light_source_development_and_laserproduced_plasma | EUV light source]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>:
1.  **High Conversion Efficiency**: The source needed to generate enough EUV light at 13.5 nanometers and emit it in the correct direction (backwards towards the light collector optics) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This generation had to be relatively efficient <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
2.  **Debris Mitigation**: Firing lasers at targets creates a lot of debris, which can contaminate the critical optic system and dampen its performance <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. A way had to be found to mitigate this debris to meet cost-of-ownership requirements <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

These two major issues, while simple to explain, proved incredibly difficult to overcome <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Early Experiments with [[euv_light_source_development_and_laserproduced_plasma | EUV Light Sources]]
The story of the [[euv_light_source_development_and_laserproduced_plasma | EUV laser]] began in 1986 when Japanese researcher Hiro Kinoshita experimented with x-rays to etch transistors, successfully printing 500 nanometer half-pitch patterns <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. Bell Labs later achieved a 50 nanometer half-pitch print in 1990 <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. These early experiments used synchrotron radiation, a form of radiation emitted by particle accelerators <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Industrialists envisioned linking one synchrotron to multiple lithography tools <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

However, researchers quickly realized that synchrotrons were impractical due to their broad field of view, meaning not enough EUV light would go into the collector mirror, failing the first major requirement <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

### Shifting Goalposts and Optics Challenges
Initially, EUV was planned for the 100 nanometer node, but it was successively pushed to the 70 nanometer, then 50 nanometer node, and further as [[challenges_in_developing_commercial_euv_systems | delays piled up]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This had cascading effects on the entire design, particularly the [[innovations_in_optical_systems_for_high_na_euv | EUV optics system]] crafted by Carl Zeiss <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. To increase print resolution, Zeiss had to add more mirrors <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Each mirror reflects at most about 70 percent of EUV light, with the rest absorbed <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. These factors necessitated a stronger, more brilliant point of plasma light, capable of at least 250 watts, to be competitive with existing 193 nanometer laser technology <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## Evolution of Laser Produced Plasma (LPP)
Researchers experimented with [[euv_light_source_development_and_laserproduced_plasma | Laser Produced Plasma (LPP)]], where a laser strikes a target to create plasma that emits UV light <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The main concern was debris from the target contaminating the optics <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

They narrowed down target materials to lithium, tin, and xenon <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### Xenon Challenges
Xenon gas (in gaseous or ice form) with YAG lasers initially seemed promising <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. Early experiments involved firing 1-kilowatt YAG lasers at a xenon jet at 10,000 cycles per second <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Sandia Laboratory scientists managed to suppress xenon ice particles from reaching the optics using a gas jet, but the xenon ice plasma emitted high-energy ions that still degraded the optics <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

In 2002, industry leaders debated the future of the xenon laser option and concluded it lacked a promising technical future due to its fundamental roadblock: low conversion efficiency (less than one percent), limiting it to only several tens of watts of EUV light <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

### Tin Challenges and Breakthroughs
Tin plasma emits a lot of UV light at the required wavelength, but early attempts with a tin plate had terrible conversion efficiency <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. Furthermore, tin notoriously generates a lot of tin debris; a layer of just 1.2 nanometers thick can cause a 20% decline in collector efficiency <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

Despite these issues, the industry made a massive turn towards tin plasma <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>, believing that with enough engineering, the debris nightmare could be overcome, as there was no fundamental physics issue ahead <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

### The Two-Pulse Laser System with Tin Droplets
The low spectral efficiency (ratio of 13.5 nm light to energy input) of tin plates was a major issue, as the plasma created was too opaque <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. A new shape was proposed to increase spectral efficiency: a concave shape instead of flat <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. Firing a laser onto this shape would create 13.5 nanometer light with much greater intensity, improving overall spectral and conversion efficiency <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

To address the debris problem, the target needed to be as small as possible. This led to experimenting with tin droplets instead of plates or wires <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. The solution involved a two-shot laser system hitting falling tin droplets 100,000 times a second <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>:

1.  **Pre-pulse**: A low-energy laser pulse hits the tin droplet, creating strong pressure waves that reshape it from a sphere into a concave sheet <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. Precision is crucial to avoid tilting the sheet incorrectly or reflecting the main shot back at the laser <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
2.  **Main pulse**: A powerful blast from an amplified carbon dioxide laser (operating at 10 micrometer wavelength) hits the pre-shaped droplet, transforming it into an acorn shape and vaporizing it <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This creates a dense plasma, hotter and denser than lightning, which emits the desired 13.5 nanometer light <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

The addition of the pre-pulse in 2016, combined with more powerful CO2 lasers, drastically scaled up ASML and Kymer's [[euv_light_source_development_and_laserproduced_plasma | EUV light source]] power from 10 watts to over 200 watts <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

### Machine Components and Operation
The EUV light source machine consists of several main components <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>:
*   **High-powered CO2 laser**: Includes a master oscillator and power amplifier (MOPA) <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. It needs to reach over 20 kilowatts and is typically installed under the fab cleanroom floor due to its size <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Beam transport system**: Handles laser focusing and beam positioning <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Vacuum vessel**: Filled with low-pressure hydrogen gas, it houses the droplet generator, metrology modules, and the [[innovations_in_optical_systems_for_high_na_euv | EUV collector mirror]] <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. The collector mirror has a hole for the laser to fire through <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
*   **Droplet generator**: Shoots 30 micrometer wide tin droplets into the vessel at 50 kilohertz (50,000 cycles a second) at 80 meters per second (288 km/h) <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. This high speed creates a large separation (about 1.6 millimeters) between droplets, preventing plasma interference <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

The resulting final conversion efficiency from this setup is six percent, a significant improvement from the one percent seen with YAG lasers <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. This allowed ASML's [[extreme_ultraviolet_lithography_and_its_challenges | EUV machines]] to reach the stable 250-watt power level needed for 125 wafers per hour operation, with a pathway towards 450 watts in the future <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

### Debris Mitigation for Collector Optics
The bilayer collector mirror faces threats from both tin debris particles and high-energy ions and neutrals from the plasma <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. To ensure the collector optics survive over 100 billion pulses or 30,000 hours throughout its lifetime <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>, Zeiss and ASML decided to pump hydrogen into the vacuum chamber as a buffer gas <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. The hydrogen gas cools the plasma, blocks a percentage of tin ions, and etches tin layers from the mirror surface <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

## Engineering Philosophy: Theory-Driven Design
The development of EUV lasers differed significantly from previous lithography technologies like 193 nanometer argon fluoride lasers <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. For the latter, basic technologies were already developed, and the industry could largely rely on trial and error <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. However, with EUV, such empirical methods were insufficient <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

Overcoming the thorny energy efficiency and debris mitigation issues required a deep understanding of physics and fundamental dynamics <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. Engineers first calculated the exact opacity, temperature, droplet size, ion density, and emission duration years in advance, then built a machine to achieve these specifications in real life <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>, representing a "modern day moon landing" <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.