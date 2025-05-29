---
title: EUV light source development and laserproduced plasma
videoId: 5Ge2RcvDlgw
---

From: [[asianometry]] <br/> 

[[Development of UV and EUV lithography technology | Extreme ultraviolet (EUV) lithography]] has become a commercial reality after over 20 years of development <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Multi-million dollar machines from ASML utilize [[Development of UV and EUV lithography technology | EUV light]] to create minuscule patterns in wafers <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. At the core of ASML's $150 million lithography machine is an advanced [[EUV light source development and laserproduced plasma | EUV light source]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This system involves lasers firing pulses at tin droplets to generate powerful 13.5 nanometer wavelength light, essential for modern microprocessors <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

While this article primarily focuses on the [[EUV light source development and laserproduced plasma | EUV]] approach adopted by Kymer, an ASML subsidiary <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>, it's worth noting that another semiconductor laser company, Gigaphoton (a Komatsu subsidiary), is also pursuing its own unique method for generating [[Development of UV and EUV lithography technology | UV light]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Historical Context and Industry Efforts in EUV Advancement

Semiconductor firms periodically collaborate to determine the next generation of chip etching technology, coordinating R&D and cooperating despite their rivalry <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. For a long time, the industry used 193 nanometer wavelength light for etching <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Engineers extended its lifespan through techniques like immersion lithography, which involved shooting light through ultra-pure water to achieve sharper focus and smaller features <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, and double patterning, using additional exposures to improve feature density <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. Ultimately, a move to [[Development of UV and EUV lithography technology | EUV light]] at 13.5 nanometers became necessary <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Core Requirements for EUV Light Sources

Scientists and engineers identified two critical requirements for the next-generation [[EUV light source development and laserproduced plasma | EUV light source]] <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>:

1.  **High Conversion Efficiency**: The source needed to generate sufficient [[Development of UV and EUV lithography technology | EUV light]] at the correct 13.5 nanometer wavelength <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This light also had to be emitted backwards, towards the collector optics, and do so relatively efficiently <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
2.  **Debris Mitigation**: Firing lasers at targets generates significant debris, which can contaminate and degrade the critical optic system <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. A solution was needed to mitigate this debris to meet cost-of-ownership requirements <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

These two requirements, simple to state, proved incredibly difficult to overcome <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## Early EUV Laser Development

The story of the [[EUV light source development and laserproduced plasma | EUV laser]] began in 1986 when Japanese researcher Hiro Kunoshita started experimenting with new wavelengths, essentially X-rays, to etch transistors <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. His work achieved 500 nanometer half-pitch patterns <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>, followed by Bell Labs with a 50 nanometer half-pitch print in 1990 <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

Early experiments utilized synchrotron radiation, a type of particle accelerator <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. While industrialists envisioned linking one synchrotron to multiple lithography tools <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, researchers quickly deemed them impractical because they emitted [[Development of UV and EUV lithography technology | UV light]] over too broad a field of view, failing the first requirement of directing enough light into the collector mirror <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Evolving Demands and Optic Systems

The target resolution for [[Development of UV and EUV lithography technology | EUV]] continually shifted, from the 100 nanometer node to 70 nm, then 50 nm, and even further due to delays <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This had cascading effects on the entire design, particularly the [[Innovations in Optical Systems for High NA EUV | EUV optics system]] meticulously crafted by German optics maker Carl Zeiss <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

To increase print resolution, Zeiss had to add more mirrors to the projection and illumination systems <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Each mirror, even when perfectly made, can only reflect around 70 percent of the [[Development of UV and EUV lithography technology | EUV light]] that hits it, with the rest absorbed <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. These factors combined meant ASML needed a much stronger, more brilliant point of plasma light, capable of at least 250 watts, to compete with existing 193 nanometer laser technology <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## Laser Produced Plasma (LPP) Research

Researchers explored Laser Produced Plasma (LPP), where a laser points at a target (e.g., gold plate or wire) to create plasma, which then emits [[Development of UV and EUV lithography technology | UV light]] at the required wavelength <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The primary concern with LPP was debris contamination of the optic system <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

Initial targets investigated included lithium, tin, and xenon <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### Xenon as a Target

Xenon gas, in either gaseous or ice form, seemed promising initially, used with YAG lasers (yttrium aluminum garnet lasers powered by a crystal) <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Early experiments involved firing one-kilowatt YAG lasers at a xenon jet at 10,000 cycles per second <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Scientists at Sandia Laboratory managed to suppress xenon ice particles from reaching the optics using a gas jet <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. However, xenon ice plasma also emitted high-energy ions that still degraded the optics <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. A major roadblock was xenon's low conversion efficiency, less than one percent, preventing it from generating more than several tens of watts of [[Development of UV and EUV lithography technology | EUV light]] <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

### Challenges with Tin as a Target

Tin plasma effectively emits [[Development of UV and EUV lithography technology | UV light]] at the required wavelength <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. However, firing lasers at a tin plate resulted in terrible conversion efficiency <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, and it notoriously generated a lot of tin debris <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. A tin layer just 1.2 nanometers thick could cause a 20% decline in collector efficiency and a 10% decline in total tool output <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. Despite these issues, some companies began experimenting with firing lasers at tin droplets instead of plates, yielding good results <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

## Industry Shifts to Tin Plasma

In 2002, leading minds in the industry met in Dallas. They concluded that the xenon laser option had a fundamental roadblock due to its low conversion efficiency <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. While the tin option presented a "debris nightmare," they believed it could be overcome with sufficient [[Engineering challenges of the EUV light source | engineering]] as there was no fundamental physics issue ahead <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. Thus, the industry made a significant shift towards tin plasma <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

The original tin plate target had poor conversion efficiency due to low spectral efficiency—the ratio of 13.5 nanometer light to the energy input <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. The plasma formed on a tin plate was too opaque, blocking the desired wavelength from reaching the mirror <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. To increase spectral efficiency, a new, more concave shape for the target was proposed <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. Firing a laser onto this shape created 13.5 nanometer light with much greater intensity <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

Separately, the issue of debris and fast ions from large tin plates or wires led to the idea of using the smallest possible target: tin droplets <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

## The Dual-Laser Droplet System

To address both challenges (concave shape for efficiency and small size for debris mitigation), a "wicked" two-shot, two-laser solution was developed <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>:

1.  **Pre-pulse Laser**: A low-energy laser pulse hits the tin droplet first <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. This "pre-pulse" creates strong pressure waves that reshape the spherical tin droplet into a concave sheet <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Precise targeting is crucial; an inaccurate hit can tilt the sheet incorrectly, interfering with or reflecting the second shot back at the laser <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
2.  **Main Pulse Laser**: The second shot is a more powerful blast from an amplified carbon dioxide laser operating at a 10 micrometer wavelength <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This remakes the droplet into an acorn shape and vaporizes it, creating a dense plasma from the liquid tin <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. This plasma emits the desired 13.5 nanometer light <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. This plasma is hotter and denser than lightning-created plasma <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

The introduction of the pre-pulse laser in 2016, combined with more powerful CO2 lasers, allowed ASML and Kymer to drastically scale [[EUV light source development and laserproduced plasma | EUV light source]] power levels from 10 watts to over 200 watts <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. Researchers globally studied and modeled the physics and dynamics of the tin droplet under these laser strikes <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

## Components of the EUV Light Source Machine

The [[EUV light source development and laserproduced plasma | EUV light source]] machine consists of several key components <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>:

*   **High-powered CO2 Laser**: Includes a master oscillator and a power amplifier (together known as MOPA) <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. This laser is so large (requiring over 20 kilowatts of power) that it's often installed beneath the fab clean room floor <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Beam Transport System**: Manages the laser's focusing and beam positioning <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Vacuum Vessel**: Filled with low-pressure hydrogen gas <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. It houses:
    *   **Droplet Generator**: Shoots tin droplets into the vessel at a high rate of 50 kilohertz (50,000 cycles per second) <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. The droplets are shot at 80 meters per second (288 km/h) to maintain a large separation (1.6 millimeters) between each 30 micrometer droplet, preventing plasma interference <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
    *   **Metrology Modules**: Monitor system performance <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
    *   **EUV Collector Mirror**: An ellipsoid-shaped mirror with a hole in the middle for the laser to fire through <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. This mirror collects the [[Development of UV and EUV lithography technology | EUV light]] and directs it to the rest of the optic system <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

### Performance and Debris Mitigation

This setup achieves a final conversion efficiency of six percent <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>, a massive improvement from the initial one percent seen with YAG lasers <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. This enabled ASML's [[Development of UV and EUV lithography technology | EUV machines]] to reach the stable 250-watt power level needed for 125 wafers per hour operation <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>, with a pathway towards 450 watts in the future <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

To ensure the collector optics survive over 100 billion pulses or 30,000 hours of operation, facing threats from tin debris, high-energy ions, and neutrals from the plasma <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>, Zeiss and ASML decided to pump hydrogen into the vacuum chamber as a buffer gas <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. The hydrogen gas cools the plasma, blocks a percentage of tin ions, and etches tin layers from the mirror surface <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

## Engineering Philosophy: Edison vs. Tesla

The development of [[Development of UV and EUV lithography technology | EUV lasers]] contrasts sharply with earlier lithography methods, like argon fluoride lasers for 193 nanometer light <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>. With earlier technologies, the basic principles were already established, and the semiconductor industry largely relied on trial and error to refine what worked <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

In contrast, [[Development of UV and EUV lithography technology | EUV]] development required a deep understanding of physics and fundamental dynamics <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. Engineers first calculated precise parameters like opacity, temperature, droplet size, ion density, and emission duration years in advance, then built a machine to achieve these theoretical requirements in real life <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. This approach highlights the difference between empirical trial-and-error (likened to Edison's method) and a theoretical, calculation-driven approach (likened to Tesla's method) <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>, <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.