---
title: Historical context and industry efforts in EUV advancement
videoId: 5Ge2RcvDlgw
---

From: [[asianometry]] <br/> 

After more than 20 years of [[development_of_uv_and_euv_lithography_technology | development]], extreme ultraviolet (EUV) lithography has become a commercial reality <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Multi-million dollar machines from [[ASML and the commercialization of EUV lithography | ASML]] now utilize EUV light to create incredibly small patterns on wafers <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. At the heart of [[ASML and the commercialization of EUV lithography | ASML]]'s $150 million lithography machine is an amazing system: the EUV light source <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This system involves lasers firing pulses at tin droplets to generate powerful 13.5 nanometer wavelength light for microprocessors <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

While this article primarily focuses on the EUV approach taken by Kymer, an [[ASML and the commercialization of EUV lithography | ASML]] subsidiary, it's worth noting that Gigaphoton, a Komatsu subsidiary, is also working on reliably generating UV light with its own unique methods <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Industry Collaboration and the Evolution of Lithography

The semiconductor industry, despite rivalries, has a history of collaboration among its top firms to decide on and coordinate research and development for etching the next generation of chips <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

For a long time, the industry used 193 nanometer wavelength light for etching <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Engineers continuously found ways to extend its usefulness, such as:
*   **Immersion Lithography** <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>: Shooting light through ultra-pure water to focus more sharply and etch smaller features <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Double Patterning** <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>: Using additional exposures to improve feature density <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

Despite these advancements, the industry ultimately needed to move beyond 193 nanometer technology, and EUV light, at 13.5 nanometers, became the solution <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Core Requirements for EUV Light Source

Scientists and engineers identified two critical requirements for the next-generation EUV light source, moving far beyond simple light bulbs <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>:

1.  **High Conversion Efficiency**: The source needed to generate sufficient 13.5 nanometer EUV light, emitted in the correct direction (backwards towards the light collector optics) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This had to be done relatively efficiently without an obscene amount of energy input <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
2.  **Debris Mitigation**: Firing lasers at targets creates significant debris, which can contaminate the critical optic system and degrade performance <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. A method had to be found to mitigate this debris to meet cost of ownership requirements <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

While these issues are simple to explain, they proved incredibly difficult to overcome <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## Early EUV Experiments and Challenges with Synchrotron Radiation

The journey of the EUV laser began in 1986 when Japanese researcher Hiro Kunoshita started experimenting with new wavelengths (essentially x-rays) to etch transistors onto silicon <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. His work achieved 500 nanometer half-pitch patterns <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Bell Labs followed in 1990 with a 50 nanometer half-pitch print <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

These early experiments utilized synchrotron radiation, a type of particle accelerator that continuously circulates a beam and emits radiation <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Industrialists initially envisioned linking one synchrotron to multiple lithography tools <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. However, researchers quickly realized this light source was impractical for the industry <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. The primary issue was that the synchrotron emitted UV light over too broad a field of view, preventing enough light from entering the collector mirror, thus failing the first big requirement for efficiency <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

Simultaneously, the target resolution for EUV advanced. Originally slated for the 100 nanometer node, it was later pushed to 70 nanometers, then 50 nanometers, with further delays accumulating <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This had cascading effects on the entire design, particularly for the [[innovations_in_optical_systems_for_high_na_euv | EUV optics system]] meticulously crafted by German optics maker Carl Zeiss <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. To increase print resolution, Zeiss had to add more mirrors into the projection and illumination optic systems <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Each mirror, even when perfectly made, only reflects about 70 percent of EUV light, absorbing the rest <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. These factors combined meant [[ASML and the commercialization of EUV lithography | ASML]] needed a stronger, more brilliant point of plasma light, capable of at least 250 watts, to be competitive with existing 193 nanometer laser technology <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## Evolution of Laser Produced Plasma (LPP) Targets

For a long time, researchers experimented with Laser Produced Plasma (LPP), where a laser is pointed at a target (e.g., gold plate or wire) to create plasma, which then emits UV light in the required wavelength <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The primary concern was debris from the target contaminating the optic system <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

Researchers narrowed down potential targets to lithium, tin, and xenon <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

### Xenon as a Target
Initially, rare xenon gas (in gaseous or ice form) combined with YAG lasers (yttrium aluminum garnet) seemed most promising <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. Early experiments involved firing one kilowatt YAG lasers at a xenon jet at 10,000 cycles per second <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Scientists at Sandia Laboratory managed to suppress xenon ice particles from reaching the optics using a gas jet <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. However, the xenon ice plasma also emitted high-energy ions that degraded the optics, a problem no one knew how to solve <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### Tin as a Target
Tin plasma certainly emitted a lot of UV light in the required wavelength <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. However, the conversion efficiency from firing lasers at a tin plate was terrible <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Furthermore, using tin as an EUV light source notoriously generated significant tin debris <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. A mere 1.2 nanometer thick tin layer could cause a 20% decline in collector efficiency and a 10% decline in total tool output <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. Consequently, tin initially did not seem to hold much promise <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

## Industry's Pivotal Shift: From Xenon to Tin

In 2002, leading minds in the industry convened in Dallas to discuss the future <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. They debated the xenon laser option and concluded it offered an unpromising technical future <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Xenon's fundamental roadblock was its low conversion efficiency (less than one percent), preventing it from generating more than several tens of watts of EUV light <a class="yt-timestamp" data-t="00:08:57">[00:09:02]</a>.

While the tin option posed a "debris nightmare" on the [[challenges_in_developing_commercial_euv_systems | development roadmap]], engineers believed it could be overcome without a fundamental physics issue <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. Thus, the industry made a massive turn, embarking on a journey towards tin plasma <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

## Innovations in Tin Plasma Generation

The original tin target material was a plate, which resulted in a very low spectral efficiency (around 1%) due to the plasma's high opacity blocking 13.5 nanometer wavelength light from reaching the mirror <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

To increase spectral efficiency, a new, more concave shape for the target was proposed <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. Firing a laser onto this shape would create 13.5 nanometer light with far greater intensity, improving overall spectral and conversion efficiency <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

Concurrently, the issue of debris from a large tin plate or wire target remained <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. The solution was to make the target as small as possible: tin droplets, which companies had already begun experimenting with <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

Engineers combined the need for a small, concave shape with debris reduction into a "wicked" double solution involving two laser shots hitting a falling tin droplet <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>:

1.  **Pre-pulse**: A low-energy laser pulse hits the tin droplet, creating strong pressure waves that reshape it from a sphere into a concave sheet <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. Precise timing is crucial, as an incorrect hit can tilt the sheet, interfering with the second shot or reflecting it back to the laser machine <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
2.  **Main Pulse**: A more powerful blast from an amplified carbon dioxide laser (10 micrometer wavelength) remakes the droplet into an acorn shape and vaporizes it, creating dense plasma <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This plasma emits the desired 13.5 nanometer light <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

The pre-pulsed laser was a critical ingredient <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. Systems installed as recently as 2010 struggled to exceed 10 watts of UV power <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. Adding the pre-pulse in 2016, along with more powerful CO2 lasers, allowed [[ASML and the commercialization of EUV lithography | ASML]] and Kymer to drastically increase EUV light source power from 10 watts to over 200 watts <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

### The EUV Machine's Components

The EUV machine itself is relatively simple, consisting of a few main components <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>:
*   **High-powered CO2 laser**: Includes a master oscillator and power amplifier (MOPA) <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. This large component often needs to be installed under the fab cleanroom floor due to its size <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   **Beam transport system**: Handles laser focusing and positioning <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Vacuum vessel**: Filled with low-pressure hydrogen gas, it houses the droplet generator, metrology modules, and the EUV collector mirror <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. The collector mirror has a hole for the laser to fire through <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
*   **Droplet generator**: Shoots 30 micrometer wide tin droplets into the vessel at 50 kilohertz (50,000 cycles per second) and a speed of 80 meters per second (288 km/h) <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. This high speed ensures a large separation space between droplets, preventing plasma interference <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

This setup achieves a final conversion efficiency of six percent, a massive improvement from the initial one percent observed with YAG lasers <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. This breakthrough enabled [[ASML and the commercialization of EUV lithography | ASML]]'s EUV machines to consistently reach the 250 watt power level required for 125 wafers per hour operation, with a future pathway towards 450 watts <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

### Addressing Debris with Hydrogen Buffer Gas

When the industry shifted to tin, a major [[challenges_in_manufacturing_euv_lithography_machines | challenge]] was ensuring the collector optics could survive over 100 billion pulses (30,000 hours) throughout its lifetime, as the bilayer collector mirror was vulnerable to tin debris particles, high-energy ions, and neutrals from the plasma <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

Carl Zeiss and [[ASML and the commercialization of EUV lithography | ASML]] ultimately decided to pump hydrogen into the vacuum chamber as a buffer gas <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. The hydrogen gas cools the plasma, blocks a percentage of tin ions, and etches layers of tin from the mirror surface <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

## Engineering Philosophy: Edison vs. Tesla

The [[development_of_uv_and_euv_lithography_technology | development]] of EUV lithography, particularly its laser, represents a shift from empirical trial-and-error methods to a deep understanding of physics and fundamental dynamics <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

As Nikola Tesla commented on Thomas Edison's empirical method, it was "inefficient in the extreme" and relied on "persistent trials and experiments often performed at random," with "a little theory and calculation" saving "ninety percent of labor" <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. This contrasts the development of argon fluoride lasers for 193 nanometer lithography, where basic technologies were already developed, and the industry could "grind through the many variations in a trial and error manner" <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

For EUV, such trial and error was not feasible <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. To overcome the thorny energy efficiency and debris mitigation issues while meeting commercial requirements, a deep understanding of the physics and its fundamental dynamics was necessary <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. Researchers first calculated the exact opacity, temperature, droplet size, ion density, and emission duration years in advance, then built a machine to achieve it in real life <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. This scientific approach has been compared to the modern-day moon landing <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.