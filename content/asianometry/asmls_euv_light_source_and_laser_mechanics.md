---
title: ASMLs EUV Light Source and Laser Mechanics
videoId: 5Ge2RcvDlgw
---

From: [[asianometry]] <br/> 

After over 20 years of development, [[overview_of_asmls_extreme_ultraviolet_lithography | Extreme Ultraviolet Lithography (EUV)]] has become a commercial reality, with multi-million dollar machines from [[asmls_role_in_semiconductor_manufacturing | ASML]] using EUV light to create incredibly small patterns in wafers <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Central to this technology is a powerful EUV light source within [[overview_of_asml_lithography_machines | ASML]]'s $150 million lithography machine <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This system relies on lasers firing pulses at tin droplets to generate powerful 13.5 nanometer wavelength light for microprocessors <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

This video primarily focuses on the [[ASML]] subsidiary Cymer's approach to EUV <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Gigaphoton, a Komatsu subsidiary, also works on generating UV light with a unique method <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Evolution to EUV Lithography

Historically, the semiconductor industry used 193 nanometer wavelength light for etching chips <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Engineers extended its usefulness through techniques like immersion lithography, which involves shooting light through ultra-pure water to focus more sharply <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, and double patterning, using additional exposures to improve feature density <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. However, the industry eventually needed to transition from 193 nanometer light <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. EUV light, at 13.5 nanometers, became the target wavelength for the next generation of chip manufacturing <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### Requirements for EUV Light Source

Scientists and engineers identified two critical requirements for the next-generation EUV light source:

1.  **High Conversion Efficiency**: The source must generate sufficient 13.5 nanometer EUV light <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This light needs to be emitted in the correct direction, backwards towards the light collector optics, to be gathered and sent through the rest of the optical system <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. It also needs to do this relatively efficiently to avoid excessive energy consumption <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
2.  **Debris Mitigation**: Firing lasers at targets creates a lot of debris <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. This debris can contaminate critical optical systems, degrading performance and increasing cost of ownership <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. A method to mitigate this debris was essential <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

These two requirements, simple to explain, proved incredibly difficult to overcome <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Early Experiments with EUV Sources

The journey for EUV lasers began in 1986, when Japanese researcher Hiro Kinoshita experimented with X-rays to etch transistors, achieving 500 nanometer half-pitch patterns <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. Bell Labs followed in 1990 with a 50 nanometer half-pitch print <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. These early experiments used synchrotron radiation, a type of particle accelerator <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

Industrialists initially envisioned linking one synchrotron to multiple lithography tools <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. However, researchers quickly found synchrotrons impractical because they emitted UV light over too broad a field of view, meaning not enough light would enter the collector mirror <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>, failing the first major requirement <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

Additionally, the target resolution for EUV kept shifting; it was originally planned for the 100 nanometer node, then 70 nanometer, then 50 nanometer, and further delayed <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This had cascading effects on the design, requiring changes to the [[technical_and_engineering_aspects_of_high_na_euv | EUV optics]] system crafted by Carl Zeiss <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. To increase print resolution, Zeiss had to add more mirrors, but each mirror only reflects around 70% of EUV light <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This meant [[ASML]] needed a much stronger, more brilliant point of plasma light, capable of at least 250 watts, to be competitive with existing 193 nanometer laser technology <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

### Laser Produced Plasma (LPP) Research

Researchers explored Laser Produced Plasma (LPP), where a laser points at a target to create plasma that emits the required UV light <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The main concern was debris <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Initial target materials included lithium, tin, and xenon <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

*   **Xenon**: Initially promising, using rare xenon gas (in gaseous or ice form) with YAG lasers <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Scientists at Sandia Laboratory suppressed xenon ice particles from reaching optics using a gas jet, but the plasma emitted high-energy ions that still degraded the optics <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. Xenon had a fundamental roadblock: very low conversion efficiency (less than one percent), limiting it to tens of watts of EUV light <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Tin**: Tin plasma emits a lot of UV light in the required wavelength <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. However, early experiments with tin plates had terrible conversion efficiency and generated significant tin debris <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. A tin layer just 1.2 nanometers thick can cause a 20% decline in collector efficiency and a 10% decline in total tool output <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### The Turn to Tin Plasma and Droplets

Despite early challenges, companies began experimenting with firing lasers at tin droplets instead of tin plates, yielding good results <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. In 2002, industry leaders debated the future of xenon and tin. They realized xenon's fundamental physics issue (low conversion efficiency) was insurmountable, while tin's debris issue, though a "nightmare," could potentially be overcome with enough engineering <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. Thus, the industry made a massive turn towards tin plasma <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

The low conversion efficiency of tin plates stemmed from low "spectral efficiency" – the ratio of 13.5 nanometer light generated compared to the energy input <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. The plasma from a tin plate was too opaque, blocking the desired wavelength from reaching the mirror <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. A new shape was proposed: a concave target instead of a flat one, to increase spectral efficiency and light intensity <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

To address the debris problem, the target needed to be as small as possible, leading to the use of tin droplets <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### The Two-Shot Laser System

Engineers devised a "wicked" solution to achieve both a small, concave shape and high conversion efficiency: two laser shots hitting a falling tin droplet <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>, 100,000 times a second <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

1.  **Pre-pulse**: A low-energy laser pulse hits the tin droplet first <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. This creates strong pressure waves that reshape the spherical tin droplet into a concave sheet <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Precise aiming is crucial; a tilted sheet can misdirect the second shot or reflect it back, damaging the laser machine <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
2.  **Main Pulse**: The second shot comes from an amplified carbon dioxide (CO2) laser operating at a 10 micrometer wavelength <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This more powerful blast remakes the droplet into an acorn shape and vaporizes it, creating dense plasma <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. This plasma then emits the desired 13.5 nanometer light <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>. This plasma is hotter and denser than lightning-generated plasma, though not as hot as the sun's core <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

The pre-pulsed laser was a critical ingredient <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. Systems installed as recently as 2010 struggled to exceed 10 watts of UV power <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. Adding the pre-pulse in 2016, combined with more powerful CO2 lasers, allowed [[ASML]] and Cymer to drastically scale up EUV light source power levels from 10 watts to over 200 watts <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

### Machine Components

The EUV light source machine has several main components:
*   **High-powered CO2 Laser**: This includes a master oscillator and a power amplifier (together referred to as MOPA) <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. It needs to reach over 20 kilowatts of power and is often installed under the fab clean room floor due to its size <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Beam Transport System**: Manages the laser's focusing and beam positioning <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Vacuum Vessel**: Filled with low-pressure hydrogen gas, it houses the droplet generator, metrology modules, and the EUV collector mirror <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   **Droplet Generator**: Shoots 30 micrometer wide tin droplets into the vessel at a rate of 50 kilohertz (50,000 cycles per second) at 80 meters per second (288 km/h) <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. This high speed ensures sufficient separation (about 1.6 millimeters) between droplets to prevent interference between plasma plumes <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
*   **Metrology Modules**: Monitor performance within the system <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
*   **[[overview_of_asml_lithography_machines | EUV Collector Mirror]]**: An ellipsoid-shaped mirror with a hole in the middle for the laser to fire through <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. It collects the light and directs it towards the rest of the optical system <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

### Results and Debris Mitigation

This setup achieved a final conversion efficiency of six percent <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>, a massive improvement from the one percent of early YAG laser experiments <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. This breakthrough allowed [[ASML]]'s EUV machines to consistently reach the stable 250 watt power level needed for 125 wafers per hour operation <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. There is even a pathway toward 450 watts in the [[future_developments_in_euv_systems_by_asml | future]] <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

To protect the collector optics from tin debris particles and high-energy ions, Zeiss and [[ASML]] decided to pump hydrogen gas into the vacuum chamber as a buffer <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. The hydrogen gas cools the plasma, blocks a percentage of tin ions, and etches layers of tin from the mirror surface, ensuring the mirror can survive over 100 billion pulses (30,000 hours) throughout its lifetime <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

## A Triumph of Physics-Based Engineering

The development of the EUV laser stands in contrast to previous lithography advancements. While Argon Fluoride lasers for 193 nanometer lithography involved extensive trial and error <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>, EUV required a deep understanding of physics and fundamental dynamics <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. Engineers first calculated exact opacity, temperature, droplet size, ion density, and emission duration years in advance, then built a machine to achieve these specifications in reality <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. This approach highlights a shift from empirical methods to a more theoretical, physics-driven engineering philosophy in semiconductor manufacturing <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.