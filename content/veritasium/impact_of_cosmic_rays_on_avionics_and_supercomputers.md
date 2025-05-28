---
title: Impact of cosmic rays on avionics and supercomputers
videoId: AaZ_RSt0KP8
---

From: [[veritasium]] <br/> 

[[cosmic_rays_and_their_effects_on_electronic_devices | Cosmic rays]], an invisible phenomenon permeating the universe, can cause unexpected malfunctions in electronic devices, leading to incidents ranging from election recounts to aircraft plunges <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. These high-energy particles can flip bits in computer memory, leading to what are known as "soft errors" <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

## Unintended Electronic Malfunctions

In 2003, a Belgian election recount was triggered in Schaerbeek, a municipality in central Brussels <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. A little-known candidate, Maria Vindevogel, received 4,096 more votes than mathematically possible <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Investigations found no software bugs or hardware faults <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. The number 4,096 is exactly 2 to the power of 12, or the 13th bit in binary <a class="yt-timestamp" data="00:02:40">[00:02:40]</a>. This suggested that the 13th bit representing Vindevogel's vote tally had flipped from a zero to a one <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Investigators suspected a particle from a [[cosmic_rays_and_their_effects_on_electronic_devices | cosmic ray]] shower struck a transistor in the computer, causing the bit flip <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

Similar issues were reported by major computer companies starting in the 1970s <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. In 1978, Intel found that [[radioactivity_in_everyday_objects_and_environments | natural radioactivity]] from trace amounts of uranium and thorium in the ceramic packaging of their DRAM chips caused bits to spontaneously flip <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Alpha particles emitted by these elements were energetic enough to create electron-hole pairs in silicon, accumulating electrons and flipping a bit from one to zero <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. This issue became prominent as chip components miniaturized to the point where a single alpha particle could produce enough charge to flip a bit <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

Today, chip manufacturers are more careful to avoid radioactive materials <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. While not caused by natural radioactivity in the computer itself, the Belgian election incident is consistent with a [[cosmic_rays_and_their_effects_on_electronic_devices | cosmic ray]] interaction <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

## Discovery of Cosmic Rays

The existence of [[historical_discoveries_about_cosmic_rays | cosmic rays]] was first suggested by Theodore Wolf in 1910, who observed that [[types_and_effects_of_ionizing_radiation | radiation]] levels did not decrease as expected at the top of the Eiffel Tower <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. Austrian physicist Victor Hess confirmed this in 1911-1912 by conducting balloon flights up to 5,200 meters, where he found [[types_and_effects_of_ionizing_radiation | radiation]] levels several times greater than on the ground, concluding the [[types_and_effects_of_ionizing_radiation | radiation]] came from the sky, not Earth <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Hess also found that a solar eclipse had no effect on the [[types_and_effects_of_ionizing_radiation | radiation]] levels, suggesting it did not emanate from the sun <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

Today, we know [[cosmic_rays_and_their_effects_on_electronic_devices | cosmic rays]] are not electromagnetic rays but particles: about 90% protons, 9% helium nuclei, and 1% heavier nuclei <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. High-energy [[cosmic_rays_and_their_effects_on_electronic_devices | cosmic rays]] originate from exploding stars (supernovae) in our galaxy and others, and the highest energy particles are thought to come from black holes <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. These primary [[cosmic_rays_and_their_effects_on_electronic_devices | cosmic rays]] collide with air molecules about 25 kilometers above the ground, creating a cascade of secondary particles like neutrons, protons, muons, electrons, positrons, and photons that stream towards Earth <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

## [[cosmic_rays_and_their_effects_on_electronic_devices | Cosmic Rays]] and Terrestrial Systems

Single event upsets (SEUs) are a type of soft error where a bit changes without damaging the device <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. These are constantly occurring:
*   **Video Games**: In 2013, during a Super Mario 64 speedrun, a player experienced an inexplicable "up warp" to a higher platform <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. The best explanation is a [[cosmic_rays_and_their_effects_on_electronic_devices | cosmic ray]] caused a bit flip in Mario's height coordinate, leading to the effect <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
*   **Operating Systems**: A "blue screen of death" in an operating system can potentially be caused by a neutron, a product of [[cosmic_rays_and_their_effects_on_electronic_devices | cosmic ray]] showers <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **General Computing**: In 1996, IBM estimated that for each 256 megabytes of RAM, one bit flip occurs per month, with neutrons being the main culprit <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

While [[cosmic_rays_and_their_effects_on_electronic_devices | cosmic rays]] were initially speculated to be the cause of Toyota's unintended acceleration recalls starting in 2009, a NASA investigation identified sticky accelerator pedals, poorly fitted floor mats, and driver error as the main causes <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

### Impact on Supercomputers

[[cosmic_rays_and_their_effects_on_electronic_devices | Cosmic rays]] have caused crashes of supercomputers, especially at higher elevations <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. Los Alamos National Labs, located 2200 meters above sea level, frequently deals with neutron-induced supercomputer crashes <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. To mitigate this, their software auto-saves frequently, and neutron detectors have been installed throughout the facility <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

### Impact on Avionics

At cruising altitude in a plane, the [[radiation_exposure_during_space_travel | radiation]] from [[cosmic_rays_and_their_effects_on_electronic_devices | cosmic rays]] increases significantly:
*   0.5 microsieverts per hour at 18,000 feet <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>
*   1 microsievert per hour at 23,000 feet <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>
*   Over 2 microsieverts per hour at 33,000 feet <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>
*   Over 3 microsieverts per hour at even higher altitudes and towards the poles <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>

This increases the chance of a single event upset by 10 to 30 times at cruising altitude <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

On October 7, 2008, an Airbus A330 flying from Singapore to Perth suddenly pitched down, diving 200 meters in 20 seconds <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. 119 people were injured <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>. The fault was traced to the first Air Data Inertial Reference Unit (ADIRU), which supplies critical flight data <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. A bit flip in the first eight bits of a 32-bit binary word meant altitude information was mislabeled as angle of attack information <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. The plane then sharply nosed down to correct what it thought was a stall <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. While other possibilities were ruled out, investigators concluded that a single event effect from a high-energy atmospheric particle striking an integrated circuit was a potential triggering event <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. The Airbus A330 was built in 1992, before specific regulatory requirements for airborne systems to be resilient to single event effects <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>.

## Mitigation in Space and Aerospace

For critical [[applications_in_aerospace_and_space_technology | aerospace and space technology]], [[radiation_hardening_in_space_missions_and_electronics | radiation hardening]] is employed to protect electronics:
*   **Space Shuttle**: Redundancy was built into the space shuttle's navigation and control systems, with four computers simultaneously running identical software <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. If one computer had a soft error, the other three would overrule it <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. On one five-day mission (STS 48), 161 separate bit flips were tracked <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
*   **Mars Rovers**: The computer on the Perseverance Rover, launched in 2001, is a 20-year-old PowerPC with 256 megabytes of RAM and two gigabytes of flash storage <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. It is [[radiation_hardening_in_space_missions_and_electronics | radiation hardened]], meaning its design, materials, circuits, and software are built to withstand 40 times the [[types_and_effects_of_ionizing_radiation | radiation]] of an ordinary computer <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. This technology has been used on over a dozen space missions since 2005 <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.
*   **Testing**: Engineers test radiation-hardened processors by exposing them to particle beams on Earth and observing "blue screens of death" to understand failure modes and prevent them in space, where an unrecoverable crash would mean mission loss <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

The sun's 11-year activity cycle creates a protective bubble (the heliosphere) that helps deflect and slow [[cosmic_rays_and_their_effects_on_electronic_devices | cosmic rays]] from interstellar space, but this protection fluctuates, with lower [[cosmic_rays_and_their_effects_on_electronic_devices | cosmic ray]] flux on Earth when the sun is active <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.