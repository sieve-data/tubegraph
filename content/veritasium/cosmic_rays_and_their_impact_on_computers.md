---
title: Cosmic rays and their impact on computers
videoId: AaZ_RSt0KP8
---

From: [[veritasium]] <br/> 

Cosmic rays are an invisible phenomenon that permeates the universe, capable of causing unexpected events from election recounts to glitches in video games and even issues in aviation <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## The Belgium Election Incident (2003)

On May 18, 2003, during an election in Belgium where voting was done on computers, an anomaly was detected in the results from Schaerbeek <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. A little-known candidate, Maria Vindevogel, received 4,096 more votes than was mathematically possible <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. A recount using magnetic cards confirmed that her original tally was indeed inflated by exactly 4,096 votes <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

Computer experts found no software bugs or hardware malfunctions that could explain this error <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. The number 4,096 is significant because it is exactly 2 to the power of 12 <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This suggests that a single bit, specifically the 13th bit in the binary representation of her vote count, flipped from a zero to a one <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This phenomenon is known as a "single event upset," a type of soft error where a bit changes without damaging the device <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## Early Discoveries of Bit Flips

Similar issues of spontaneous bit flips in computer memory were reported by major companies starting in the 1970s <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

In 1978, Intel observed strange errors in their 16-kilobit dynamic random-access memory (DRAM), where ones would spontaneously flip to zeros <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. The cause was traced to the ceramic packaging of the chips <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. A new manufacturing plant on the Green River in Colorado was downstream from an old uranium mill, leading to radioactive atoms (trace amounts of uranium and thorium) making their way into the ceramic material <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

The alpha particles emitted by these radioactive elements were energetic and [[understanding_ionizing_radiation | ionizing]] enough to create electron-hole pairs in the silicon, causing electrons to accumulate and flip a bit from a one to a zero <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This problem was identified in the 1970s because chip components had miniaturized to the point where a single alpha particle could produce enough charge to flip a bit <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. As a result, chip manufacturers became more careful to avoid radioactive materials <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

## The Discovery and Nature of Cosmic Rays

The search for a way to measure radioactivity led to observations that paved the way for the discovery of cosmic rays <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### [[history_and_discovery_of_cosmic_rays | Historical Context]]
*   **Henri Becquerel (1896):** Discovered radioactivity with uranium <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Theodore Wolf (1910):** Used a gold-leaf electrometer on the Eiffel Tower, expecting less radiation at altitude but finding only a slight decrease <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Victor Hess (1911-1912):** Conducted balloon flights up to 5,200 meters <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. He found that above one kilometer, [[background_radiation_levels_globally | radiation]] levels increased with altitude, becoming several times greater than on the ground at maximum height <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. His experiment during a solar eclipse showed the radiation was unaffected, leading him to conclude it originated from space, not the Sun <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. Hess is credited with discovering cosmic rays <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. He later shared the Nobel Prize in Physics with Carl Anderson <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

### Composition and Origin
Cosmic rays are not electromagnetic rays but particles <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>:
*   Approximately 90% are protons <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   9% are helium nuclei <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   1% are heavier nuclei <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

While some low-energy cosmic rays come from the Sun <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, high-energy cosmic rays originate from exploding stars (supernovae) in our and other galaxies <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The highest energy particles are believed to come from black holes, including supermassive black holes at galactic centers <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. Their paths are difficult to trace due to deflection by magnetic fields in space <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

One such particle, detected on October 15, 1991, dubbed the "OMG particle," had an energy of 51 joules, comparable to a baseball traveling 100 kilometers per hour <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### Cosmic Ray Showers
Primary cosmic rays do not typically reach Earth's surface <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Instead, they collide with air molecules around 25 kilometers above the ground, creating a cascade of secondary particles like pions, neutrons, protons, muons, electrons, positrons, and photons <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. These particles then stream towards Earth, forming a "shower" <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. It is one of these secondary particles that is suspected of causing the bit flip in the Belgian election computer <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

### Visualizing Cosmic Rays
Charles Wilson's cloud chamber, perfected in 1911, allowed scientists to visualize the paths of cosmic rays <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. In 1932, Carl Anderson used a cloud chamber to identify the positron (anti-electron), the first confirmed sighting of anti-matter <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. Four years later, he discovered the muon, also in cosmic rays <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

## Cosmic Ray Impact on Computers

Cosmic rays are constantly triggering bit flips in computers <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Examples of Bit Flips
*   **Super Mario 64 Up-Warp:** In 2013, a speedrunner experienced an inexplicable "up-warp" glitch in Super Mario 64. The most plausible explanation is that a cosmic ray caused a single bit to flip in Mario's height coordinate, coincidentally aligning him with a higher platform <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
*   **Blue Screen of Death:** A "blue screen of death" error on a computer might actually be caused by a neutron or other particle from a cosmic ray shower <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Frequency:** In 1996, IBM estimated that for every 256 megabytes of RAM, one bit flip occurs per month <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. The main culprit for these flips at Earth's surface appears to be neutrons from cosmic ray showers <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

### Mitigating Bit Flips
Computer chips are made more resilient to bit flips using methods like Error Correction Code (ECC) memory <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. However, it's not possible to prevent them entirely <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

### [[effects_of_cosmic_rays_on_aviation_and_space_missions | Impact on Critical Systems]]
*   **Toyota Unintended Acceleration (2009):** While cosmic rays were initially speculated to be the cause of unintended acceleration in millions of Toyota vehicles, NASA's investigation concluded that sticky accelerator pedals, poorly fitted floor mats, and driver error were the primary causes <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   **Supercomputer Crashes:** Cosmic rays have caused crashes of supercomputers, especially at higher elevations <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. Los Alamos National Labs, located 2200 meters above sea level, frequently deals with neutron-induced supercomputer crashes, requiring frequent auto-saves and neutron detectors <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
*   **Aircraft Systems:** At cruising altitudes, [[radiation_exposure_in_daily_life_and_occupations | radiation]] from cosmic rays significantly increases, by 10 to 30 times, raising the chance of a single event upset <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
    *   **Airbus A330 Incident (2008):** An Airbus A330 experienced a sudden pitch-down during flight, injuring 119 people <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. Investigators concluded that a bit flip in the first air data inertial reference unit (ADIRU) likely caused altitude information to be mislabeled as angle of attack, leading the plane to try to correct a non-existent stall <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. The aircraft was built in 1992, before specific regulatory requirements for resilience to single event effects <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
*   **Spacecraft:** For missions to other planets, protecting electronics from cosmic rays is critical to prevent mission loss from a single bit flip in a critical function <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.
    *   **Space Shuttle:** Redundancy was built into the space shuttle's navigation and control systems, with four computers running identical software to overrule any soft errors <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. One five-day mission, STS 48, recorded 161 separate bit flips <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
    *   **Perseverance Rover:** The computer on the Mars Perseverance Rover, launched in 2001, is a 20-year-old PowerPC with limited memory but is "radiation hardened." Its design, materials, circuits, and software are built to withstand 40 times the [[radiation_exposure_during_space_travel | radiation]] of an ordinary computer <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. This type of computer has been used on over a dozen space missions since 2005 <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.
    *   **Astronaut Sightings:** Astronauts sometimes report seeing flashes of light with their eyes closed in space, which is believed to be heavy cosmic ray particles or bursts of energy from [[radiation_exposure_during_space_travel | radiation]] passing through their eyeballs or optic nerves <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

## Broader Implications

The heliosphere, a protective bubble formed by particles streaming from the Sun and solar wind, helps deflect and slow cosmic rays from interstellar space, shielding the solar system from [[understanding_ionizing_radiation | ionizing radiation]] <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>. This protection fluctuates with the Sun's 11-year activity cycle <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.

Cosmic rays may have played a significant role in the [[effects_on_earth_and_astronomical_bodies | history of our planet]] by flipping bits in the genetic codes of living organisms, potentially contributing to the variation upon which natural selection acts <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.

Maria Vindevogel was ultimately elected as a member of the Belgium Chamber of Representatives by people, not a particle <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>, but her story serves as a reminder of the constant, invisible influence of cosmic rays on our lives <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>.