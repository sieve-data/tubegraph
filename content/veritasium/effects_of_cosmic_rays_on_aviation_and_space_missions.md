---
title: Effects of cosmic rays on aviation and space missions
videoId: AaZ_RSt0KP8
---

From: [[veritasium]] <br/> 

[[cosmic_rays_and_their_impact_on_computers | Cosmic rays]] are an invisible phenomenon that permeates the universe, capable of causing unexpected events ranging from election recounts to aircraft malfunctions <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. These high-energy particles from space pose significant challenges for aviation and space missions due to their ability to alter electronic systems and expose humans to [[radiation_exposure_during_space_travel | radiation]].

## Understanding Cosmic Rays

[[cosmic_rays_and_their_impact_on_computers | Cosmic rays]] are not electromagnetic rays but high-energy particles, primarily composed of protons (around 90%), helium nuclei (9%), and heavier nuclei (1%) <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.

They originate from various sources:
*   **The Sun**: Emits relatively low-energy [[cosmic_rays_and_their_impact_on_computers | cosmic rays]] <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>.
*   **Exploding Stars (Supernovae)**: Produce high-energy [[cosmic_rays_and_their_impact_on_computers | cosmic rays]] moving close to the speed of light within and beyond our galaxy <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
*   **Black Holes**: The highest energy particles are believed to emanate from black holes, including supermassive black holes at galactic centers <a class="yt-timestamp" data-t="08:39:00">[08:39:00]</a>.

It is challenging to pinpoint the exact origin of [[cosmic_rays_and_their_impact_on_computers | cosmic rays]] because their charged nature causes them to be deflected by magnetic fields in space, allowing them to traverse the universe for billions of years <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>. An extreme example is the "OMG particle" detected in 1991, a single subatomic particle with an energy of 51 joules, equivalent to a baseball traveling 100 kilometers per hour <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.

### Interaction with Earth's Atmosphere
Primary [[cosmic_rays_and_their_impact_on_computers | cosmic rays]] do not typically reach Earth's surface <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>. Instead, they collide with air molecules approximately 25 kilometers above the ground, creating a cascade of new particles like pions, which then decay into neutrons, protons, muons, electrons, positrons, and photons <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>. These secondary particles form a shower streaming towards Earth <a class="yt-timestamp" data-t="09:45:00">[09:45:00]</a>.

### The Heliosphere's Protection
The solar system is protected from interstellar [[cosmic_rays_and_their_impact_on_computers | radiation]] by the heliosphere, a protective bubble maintained by particles from the sun and solar wind <a class="yt-timestamp" data-t="20:33:00">[20:33:00]</a>. This bubble helps deflect and slow down [[cosmic_rays_and_their_impact_on_computers | cosmic rays]] <a class="yt-timestamp" data-t="20:44:00">[20:44:00]</a>. The sun's 11-year activity cycle causes this protection to fluctuate, resulting in a lower flux of [[cosmic_rays_and_their_impact_on_computers | cosmic rays]] on Earth when the sun is active <a class="yt-timestamp" data-t="20:52:00">[20:52:00]</a>.

## Impact on Aviation

The increasing altitude significantly increases [[radiation_exposure_during_space_travel | radiation]] from [[cosmic_rays_and_their_impact_on_computers | cosmic rays]] <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>:
*   **18,000 feet**: 0.5 microsieverts per hour <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>
*   **23,000 feet**: Up to 1 microsievert per hour <a class="yt-timestamp" data-t="14:48:00">[14:48:00]</a>
*   **33,000 feet**: Over 2 microsieverts per hour <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>
*   **Higher altitudes and towards the poles**: Over 3 microsieverts per hour <a class="yt-timestamp" data-t="14:54:00">[14:54:00]</a>

At cruising altitude, the chance of a "single event upset" (SEU) increases by 10 to 30 times <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>. A SEU is a "soft error" where a bit flips (e.g., from a zero to a one) without damaging the device <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>. This type of error, often caused by neutrons from cosmic ray showers <a class="yt-timestamp" data-t="13:27:00">[13:27:00]</a>, is not critical for personal laptops but can be catastrophic in flight computers <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>.

### Case Study: Qantas Flight 72 (2008)
On October 7, 2008, an Airbus A330 flying from Singapore to Perth experienced two sudden, uncommanded dives <a class="yt-timestamp" data-t="15:12:00">[15:12:00]</a>. The first dive caused the plane to plummet 200 meters in 20 seconds, resulting in negative 0.8 Gs of acceleration, making it feel like the plane had flipped over <a class="yt-timestamp" data-t="15:19:00">[15:19:00]</a>. A second drop occurred minutes later <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>. A total of 119 people were injured, many from hitting their heads on the ceiling <a class="yt-timestamp" data-t="15:48:00">[15:48:00]</a>.

The investigation focused on the first Air Data Inertial Reference Unit (ADIRU), which provides critical data like airspeed, angle of attack, and altitude <a class="yt-timestamp" data-t="16:00:00">[16:00:00]</a>. Each piece of information is supplied as a 32-bit binary word <a class="yt-timestamp" data-t="16:10:00">[16:10:00]</a>. It was suspected that a bit flip in the first eight bits of the ADIRU's data caused altitude information to be mislabeled as angle of attack information <a class="yt-timestamp" data-t="16:24:00">[16:24:00]</a>. This led to conflicting alarms in the cockpit (over-speed and stall simultaneously) and the plane pitching down sharply to correct a perceived stall <a class="yt-timestamp" data-t="16:34:00">[16:34:00]</a>.

Investigators ruled out software bugs, corruption, hardware failure, environmental factors, and electromagnetic interference as likely causes <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>. The most probable cause was a single event effect from a high-energy atmospheric particle striking an integrated circuit in the CPU module <a class="yt-timestamp" data-t="17:05:00">[17:05:00]</a>. The Airbus A330, built in 1992, predated specific regulatory or manufacturer requirements for airborne systems to be resilient to single event effects <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>.

## Impact on Space Missions

For space missions, protecting electronics is critical because a single bit flip in a critical function, like thrusters, could lead to mission loss <a class="yt-timestamp" data-t="19:12:00">[19:12:00]</a>.

### Space Shuttle Redundancy
The Space Shuttle incorporated significant redundancy in its design <a class="yt-timestamp" data-t="17:34:00">[17:34:00]</a>. For navigation and control, four computers simultaneously ran identical software, allowing the other three to overrule any single computer experiencing a soft error <a class="yt-timestamp" data-t="17:38:00">[17:38:00]</a>. This setup also allowed tracking of bit flip frequencies; during one five-day mission (STS 48), 161 separate bit flips were recorded <a class="yt-timestamp" data-t="17:49:00">[17:49:00]</a>.

### Astronaut Experiences
Above the atmosphere, [[cosmic_rays_and_their_impact_on_computers | cosmic rays]] are so energetic that astronauts can sometimes perceive them as flashes of light even with their eyes closed <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>. These flashes are thought to be caused by heavy particles or bursts of energy from [[radiation_exposure_during_space_travel | radiation]] passing through the eyeball or optic nerve <a class="yt-timestamp" data-t="18:18:00">[18:18:00]</a>.

### Radiation Hardened Electronics
To withstand the harsh [[radiation_exposure_during_space_travel | radiation]] environment of space, electronics for missions to other planets are "radiation hardened" <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>. This means their design, materials, circuits, and software are built to withstand up to 40 times the [[radiation_exposure_during_space_travel | radiation]] of an ordinary computer <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>.

*   **Perseverance Rover**: The Mars Perseverance Rover, which landed in 2021, uses a PowerPC computer launched in 2001 <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>. This 20-year-old technology, despite having only 256 megabytes of RAM and 2 gigabytes of flash storage, is chosen because it is radiation hardened <a class="yt-timestamp" data-t="19:33:00">[19:33:00]</a>. This particular PowerPC design has been used on over a dozen space missions since 2005 <a class="yt-timestamp" data-t="19:52:00">[19:52:00]</a>.
*   **Testing**: Radiation hardening involves extensive testing, such as placing an operating system processor in a beam line to generate particles and observe "blue screens of death" <a class="yt-timestamp" data-t="19:57:00">[19:57:00]</a>. This helps engineers understand how to prevent such critical errors, as a spacecraft entering this mode is typically unrecoverable <a class="yt-timestamp" data-t="20:14:00">[20:14:00]</a>.

The Voyager 1 spacecraft, as it departed the solar system, showed an increase in the flux of [[cosmic_rays_and_their_impact_on_computers | cosmic rays]] it experienced, indicating its passage beyond the heliosphere's protective bubble <a class="yt-timestamp" data-t="20:24:00">[20:24:00]</a>.