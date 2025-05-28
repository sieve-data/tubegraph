---
title: Radiation hardening in space missions and electronics
videoId: AaZ_RSt0KP8
---

From: [[veritasium]] <br/> 

## The Unseen Threat: Bit Flips

An invisible phenomenon that permeates the universe, cosmic rays, can cause unpredictable issues in electronic devices, from plummeting planes to election recounts and video game glitches <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These "soft errors" involve a bit spontaneously flipping from a zero to a one, or vice versa, without permanently damaging the device <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### Early Discoveries of Bit Flips

In 1978, Intel reported strange errors in their 16 kilobit dynamic random access memory (DRAM), where "ones" would spontaneously flip to "zeros" <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. The cause was traced to the ceramic packaging of the chip, which contained trace amounts of uranium and thorium <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Alpha particles emitted by these radioactive elements could create electron-hole pairs in the silicone, causing electrons to accumulate and flip a bit <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. This problem was identified in the 1970s as chip components were miniaturized to a point where a single alpha particle could produce enough charge to flip a bit <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. This discovery led chip manufacturers to be more cautious about avoiding radioactive materials in their products <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

### Cosmic Rays: The Primary Culprit

[[cosmic_rays_and_their_effects_on_electronic_devices | Cosmic rays]] are high-energy particles from space, primarily protons (90%), helium nuclei (9%), and heavier nuclei (1%) <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. While some originate from the sun, the highest energy cosmic rays come from exploding stars (supernovae) in our galaxy and others, and even from supermassive black holes at the centers of galaxies <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

When these primary cosmic rays strike air molecules about 25 kilometers above Earth's surface, they create a cascade of new particles, including neutrons, protons, muons, electrons, positrons, and photons, which then stream towards the ground <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

### Impact on Electronics on Earth

Even on Earth's surface, these secondary particles can cause bit flips. For example:
*   **Belgian Election (2003)**: A cosmic ray is suspected of striking a transistor in a voting computer, flipping the 13th bit and incorrectly adding 4,096 votes to a candidate's tally <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Super Mario 64 Speedrun (2013)**: A user experienced an "up warp" glitch, which is best explained by a cosmic ray flipping a single bit in Mario's height coordinate, causing him to instantly move to a higher platform <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
*   **General Computer Failures**: Cosmic rays are constantly triggering bit flips, and a "blue screen of death" might actually be caused by a neutron from a cosmic ray shower <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. In 1996, IBM estimated one bit flip per month for every 256 megabytes of RAM <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.
*   **Supercomputers**: [[impact_of_cosmic_rays_on_avionics_and_supercomputers | Cosmic rays and their effects on electronic devices]] have caused crashes in supercomputers, particularly at higher elevations like Los Alamos National Labs (2200 meters above sea level), where neutron-induced crashes are a constant concern <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

### Increased Risk in Aerospace and Space

The risk of single event upsets increases significantly at higher altitudes. At cruising altitude in a plane, the chance of a bit flip increases by 10 to 30 times <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.

*   **Airbus A330 Incident (2008)**: An Airbus A330 experienced two sudden dives during a flight from Singapore to Perth. Investigation suggested a bit flip in the first air data inertial reference unit (ADIRU), which mislabeled altitude data as angle-of-attack information <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. This incident highlighted the lack of specific regulatory or aircraft manufacturer requirements for airborne systems to be resilient to single event effects at the time the aircraft was built in 1992 <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

Beyond Earth's protective atmosphere, the problem intensifies. Astronauts in space have reported seeing flashes of light with their eyes closed, which are believed to be heavy particles or bursts of energy from [[radiation_exposure_during_space_travel | radiation exposure during space travel]] passing through their eyeballs or optic nerves <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

### Radiation Hardening: Solutions for Spacecraft

For missions to other planets, protecting electronics is critical, as a single bit flip in a critical function, like thrusters, could lead to mission loss <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.

[[applications_in_aerospace_and_space_technology | Radiation hardening]] is a set of design, material, circuit, and software techniques used to make electronics more resilient to radiation.

*   **Redundancy**: The Space Shuttle, for example, had four computers simultaneously running identical software for navigation and control. If one computer experienced a soft error, the other three would overrule it <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. On one five-day mission (STS 48), 161 separate bit flips were recorded <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
*   **Specialized Hardware**: The computer on the Perseverance Rover, which landed on Mars, is a 20-year-old PowerPC launched in 2001. While it only has 256 megabytes of RAM and two gigabytes of flash storage, it is radiation-hardened, meaning its design and components are built to withstand 40 times the radiation of an ordinary computer <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. This specific computer has been used on over a dozen space missions since 2005 <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.
*   **Testing**: Radiation hardening involves rigorously testing processors by exposing them to particle beams to generate "blue screens of death" and then figuring out how to prevent them. A spacecraft that enters such a mode is typically unrecoverable <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

### Natural Protection and Long-Term Effects

The heliosphere, a protective bubble maintained by particles streaming from the sun and the solar wind, helps deflect and slow down cosmic rays from interstellar space, shielding the solar system from ionizing radiation <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>. This protection fluctuates with the sun's 11-year activity cycle <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.

Beyond electronics, cosmic rays may have played a significant role in the history of our planet by flipping bits in the genetic codes of living organisms, potentially contributing to the variation on which natural selection acts <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.