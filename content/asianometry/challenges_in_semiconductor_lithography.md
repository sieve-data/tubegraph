---
title: Challenges in Semiconductor Lithography
videoId: 5Ge2RcvDlgw
---

From: [[asianometry]] <br/> 

[[euv_lithography_technology_and_its_challenges | Extreme ultraviolet (EUV) lithography]] has become a commercial reality after over 20 years of development <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Multi-million dollar machines from ASML utilize EUV light to create impossibly small patterns on wafers <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The heart of ASML's $150 million lithography machine is its EUV light source <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This system involves lasers firing pulses at tin droplets to generate powerful 13.5 nanometer wavelength light for microprocessors <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Key Players in EUV Light Source Development
This article primarily focuses on the EUV approach taken by Kymer, an ASML subsidiary <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Gigaphoton, a Komatsu subsidiary, is another semiconductor laser company also working on reliably generating UV light with their own unique approach <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Evolution of Lithography Wavelengths
For a long time, the semiconductor industry used light with a 193 nanometer wavelength for etching <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Engineers extended its usefulness through techniques like:
*   **Immersion Lithography**: Shooting light through ultra-pure water to focus more sharply and etch smaller features <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Double Patterning**: Using additional exposures to improve feature density <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

Ultimately, a move to 13.5 nanometer EUV light was necessary <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Core Requirements for Next-Generation EUV Light Sources
Scientists and engineers identified two simple but challenging requirements for the next-generation EUV light source:
1.  **High Conversion Efficiency**: The source must generate enough EUV light at the correct 13.5 nanometer wavelength <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This light needs to be emitted in the right direction (backwards towards the light collector optics) and generated relatively efficiently <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
2.  **Debris Mitigation**: Firing lasers at targets creates debris that can contaminate and degrade the critical optic system <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. A method had to be found to mitigate this debris to meet cost of ownership requirements <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

These two issues, while simple to explain, were incredibly difficult to overcome <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Early EUV Experiments and Their Limitations
The EUV laser story began in 1986 with Japanese researcher Hiro Kinoshita, who experimented with X-rays to etch transistors, achieving 500 nanometer half-pitch patterns <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Bell Labs followed with a 50 nanometer half-pitch print in 1990 <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

These early experiments used **synchrotron radiation** <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. While industrialists envisioned linking one synchrotron to multiple lithography tools, researchers quickly found them impractical <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. The primary reason was that synchrotrons emitted UV light over too broad a field of view, meaning not enough light would enter the collector mirror, thus failing the first big requirement for conversion efficiency <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

## Shifting Goalposts and Increased Power Demands
EUV was initially targeted for the 100 nanometer node, requiring less powerful light sources <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. However, it was later penciled in for the 70 nanometer, then 50 nanometer nodes, and faced further delays <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. These delays had cascading effects:
*   The EUV optics system, crafted by German optics maker Carl Zeiss, had to change <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   To increase print resolution, Zeiss added more mirrors to the projection and illumination systems <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Each mirror reflects only about 70% of the EUV light, absorbing the rest <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   This meant ASML needed a stronger, more brilliant point of plasma light, capable of at least 250 watts, to be competitive with existing 193 nanometer laser technology <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. Technology needs to be appreciably better than existing solutions to be adopted <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## Challenges with Laser Produced Plasma (LPP)
Researchers experimented with Laser Produced Plasma (LPP), where a laser points at a target (e.g., gold plate or wire) to create plasma that emits UV light <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The main issue was debris <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

Researchers tried various target materials, narrowing them down to lithium, tin, and xenon <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### Xenon Plasma Challenges
Initially, rare xenon gas (in gaseous or ice form) combined with YAG lasers (yttrium aluminum garnet lasers) seemed promising <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   Scientists at Sandia Laboratory suppressed xenon ice particles from reaching the optics using a gas jet <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   However, xenon ice plasma also emitted high-energy ions that degraded the optics anyway <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   A major roadblock was its low conversion efficiency, less than one percent, preventing it from generating more than several tens of watts of EUV light <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

### Tin Plasma Challenges
Tin plasma emits a lot of UV light in the required wavelength <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   The conversion efficiency from firing lasers at a tin plate was terrible <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   Using tin as an EUV light source notoriously generates a lot of tin debris <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. A tin layer just 1.2 nanometers thick can cause a 20% decline in collector efficiency and a 10% decline in total tool output <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

## The Shift to Tin Plasma (2002)
In 2002, leading minds in Dallas debated the future of the xenon laser option, realizing it lacked a promising technical future due to its fundamental roadblock of low conversion efficiency <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
The tin option would create a debris nightmare but had no fundamental physics issue, suggesting it could be overcome with sufficient engineering <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. Thus, the industry made a massive turn towards tin plasma <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

## Overcoming Tin Plasma Challenges
### Improving Conversion Efficiency: From Plate to Concave Droplet
The original target material was a tin plate, but its conversion efficiency was low, around one percent <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. This was due to low spectral efficiency because the plasma made on a flat tin plate had too high an opacity, blocking 13.5 nanometer wavelength light from reaching the mirror <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

A new, more concave shape was proposed to increase spectral efficiency and light intensity <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

### Mitigating Debris: From Plate to Droplets
A large plate or wire of tin created too much debris and fast ions <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. To avoid this, the target needed to be as small as possible <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This led companies to experiment with tin droplets <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### The Double-Shot Laser Solution
Engineers faced the double challenge of needing a small, concave-shaped target. Their solution involved two shots from two lasers hitting a falling tin droplet, not once, but twice, 100,000 times a second <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
1.  **Pre-pulse**: A low-energy laser pulse hits the tin droplet, creating strong pressure waves that reshape it from a sphere into a concave sheet <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. Precision is crucial; an incorrect hit can tilt the sheet and reflect the second shot back at the laser machine <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
2.  **Main Pulse**: Generated by an amplified carbon dioxide laser (10 micrometer wavelength), this powerful blast reshapes the droplet into an acorn shape and vaporizes it, creating the dense plasma that emits 13.5 nanometer light <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This plasma is hotter and denser than lightning plasma <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

The pre-pulsed laser was a critical ingredient <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. Systems in 2010 struggled past 10 watts of UV power, but adding the pre-pulse in 2016, along with more powerful CO2 lasers, allowed ASML and Kymer to scale EUV light source power levels from 10 watts to over 200 watts <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

The final conversion efficiency from this setup is six percent, a massive leap from the one percent seen with earlier YAG lasers <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. This enabled ASML's EUV machines to reach the stable 250-watt power level needed for 125 wafers per hour, with a pathway towards 450 watts in the future <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

## Collector Optics Survival
The bilayer collector mirror is threatened by tin debris particles, high-energy ions, and neutrals from the plasma, needing to survive over 100 billion pulses or 30,000 hours <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. Zeiss and ASML decided to pump hydrogen into the vacuum chamber as a buffer gas <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. This hydrogen gas cools the plasma, blocks a percentage of tin ions, and etches layers of tin from the mirror surface <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

## The Approach to EUV Development
Unlike the development of argon fluoride lasers for 193 nanometer lithography, which relied on trial and error with already developed basic technologies, [[euv_lithography_technology_and_its_challenges | EUV]] required a different approach <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. For [[euv_lithography_technology_and_its_challenges | EUV]], such trial and error was not feasible <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. A deep understanding of the physics and fundamental dynamics was necessary to tackle the thorny energy efficiency and debris mitigation issues while meeting commercial requirements <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. Engineers first calculated exact parameters like opacity, temperature, droplet size, ion density, and emission duration years in advance, then built a machine to achieve it <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.