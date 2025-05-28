---
title: Explanation of bit flips and single event upsets
videoId: AaZ_RSt0KP8
---

From: [[veritasium]] <br/> 

A "bit flip" describes an instance where a binary digit (bit) in a computer's memory or register spontaneously changes its state, for example, from a 0 to a 1, or vice versa <a class="yt-timestamp" data-t="02:55:00">[02:55]</a>. When such an alteration is caused by an external, non-damaging event, it is known as a "single event upset" (SEU), a type of soft error where the device itself remains undamaged, but the data is altered <a class="yt-timestamp" data-t="03:34:00">[03:34]</a>. These invisible phenomena can lead to unexpected and counterintuitive effects in various systems, from election recounts to aircraft malfunctions.

## Case Study: The Belgian Election Anomaly

On May 18th, 2003, during an election in Belgium, a computer-based voting system in Schaerbeek reported an inexplicable result for candidate Maria Vindevogel <a class="yt-timestamp" data-t="00:44:00">[00:44]</a>. She received 4,096 more votes than was mathematically possible <a class="yt-timestamp" data-t="00:56:00">[00:56]</a>. A recount, feeding magnetic cards through machines, confirmed the original tally for all candidates except Vindevogel, whose votes were indeed 4,096 less <a class="yt-timestamp" data-t="01:09:00">[01:09]</a>.

Computer experts found no bugs in the software or hardware issues <a class="yt-timestamp" data-t="01:38:00">[01:38]</a>. The clue lay in the number 4,096, which is exactly 2 to the power of 12 <a class="yt-timestamp" data-t="02:36:00">[02:36]</a>. Computers operate using binary, where numbers are represented as strings of zeros and ones, each corresponding to a power of two <a class="yt-timestamp" data-t="02:11:00">[02:11]</a>. For Maria Vindevogel to gain 4,096 extra votes, the 13th bit in the computer's vote tally for her had to flip from a zero to a one <a class="yt-timestamp" data-t="02:55:00">[02:55]</a>.

## Historical Precedent: Intel DRAM Errors

Similar issues were reported by major computer companies starting in the 1970s <a class="yt-timestamp" data-t="03:10:00">[03:10]</a>. In 1978, Intel observed strange errors in their 16-kilobit dynamic random-access memory (DRAM), where ones would spontaneously flip to zeros <a class="yt-timestamp" data-t="03:19:00">[03:19]</a>. The cause was traced to the ceramic packaging of the chips <a class="yt-timestamp" data-t="03:33:00">[03:33]</a>. A new manufacturing plant on the Green River in Colorado was downstream from an old uranium mill, leading to radioactive atoms making their way into the ceramic material <a class="yt-timestamp" data-t="03:44:00">[03:44]</a>.

Trace amounts of uranium and thorium in the ceramic were sufficient to cause problems <a class="yt-timestamp" data-t="04:01:00">[04:01]</a>. Alpha particles emitted by these radioactive elements are energetic and ionizing, capable of creating electron-hole pairs in silicon <a class="yt-timestamp" data-t="04:14:00">[04:14]</a>. If an alpha particle struck in the right place, it could generate enough free charge carriers to accumulate electrons in a memory well, thus flipping a bit from a one to a zero <a class="yt-timestamp" data-t="04:22:00">[04:22]</a>.

This problem emerged in the 1970s because chip components had miniaturized to a point where a single alpha particle could produce enough charge to flip a bit <a class="yt-timestamp" data-t="04:59:00">[04:59]</a>. Following Intel's findings, chip manufacturers became more careful to avoid radioactive materials in their microchips and packaging <a class="yt-timestamp" data-t="05:18:00">[05:18]</a>.

## The Invisible Phenomenon: Cosmic Rays

The bit flip in the Belgian election computer was not caused by natural radioactivity within the machine itself, but rather by cosmic rays <a class="yt-timestamp" data-t="09:52:00">[09:52]</a>.

### Discovery of Cosmic Rays

After Henri Becquerel's discovery of radioactivity in 1896, scientists sought to measure it <a class="yt-timestamp" data-t="05:38:00">[05:38]</a>. In 1910, Theodore Wolf used a gold leaf electrometer atop the Eiffel Tower, expecting less radiation higher up <a class="yt-timestamp" data-t="06:16:00">[06:16]</a>. Instead, he found only a slight decrease <a class="yt-timestamp" data-t="06:31:00">[06:31]</a>. In 1911, Austrian physicist Victor Hess took the experiment further with balloon flights <a class="yt-timestamp" data-t="06:37:00">[06:37]</a>. His initial flights showed no fundamental change in radiation up to 1,100 meters <a class="yt-timestamp" data-t="06:49:00">[06:49]</a>. However, in 1912, seven flights reaching 5,200 meters revealed a remarkable increase in radiation with altitude <a class="yt-timestamp" data-t="06:58:00">[06:58]</a>. At maximum height, the radiation level was several times greater than on the ground <a class="yt-timestamp" data-t="07:18:00">[07:18]</a>.

Hess also conducted a flight during a solar eclipse, finding that the radiation readings were unaffected by the sun's partial coverage <a class="yt-timestamp" data-t="07:32:00">[07:32]</a>. This led him to conclude that the radiation was not primarily emanating from the sun, but from space <a class="yt-timestamp" data-t="07:49:00">[07:49]</a>. Victor Hess had discovered [[Historical context and secrecy of the Dzhanibekov effect | cosmic rays]] <a class="yt-timestamp" data-t="08:01:00">[08:01]</a>. He shared the Nobel Prize in Physics in 1936 for this discovery <a class="yt-timestamp" data-t="11:14:00">[11:14]</a>.

### Nature and Origin

Today, [[Historical context and secrecy of the Dzhanibekov effect | cosmic rays]] are known to be high-energy particles, not electromagnetic rays <a class="yt-timestamp" data-t="08:10:00">[08:10]</a>. Approximately 90% are protons, 9% are helium nuclei, and 1% are heavier nuclei <a class="yt-timestamp" data-t="08:16:00">[08:16]</a>.
*   **Solar Cosmic Rays**: Some originate from the sun, but these have comparatively low energy <a class="yt-timestamp" data-t="08:23:00">[08:23]</a>.
*   **High-Energy Cosmic Rays**: Moving near the speed of light, these come from exploding stars (supernovae) within and beyond our galaxy <a class="yt-timestamp" data-t="08:28:00">[08:28]</a>. The highest energy particles are believed to originate from black holes, including supermassive black holes at galactic centers <a class="yt-timestamp" data-t="08:39:00">[08:39]</a>.

Pinpointing their exact origin is challenging because, as charged particles, they are deflected by magnetic fields in space, allowing them to traverse the universe for billions of years <a class="yt-timestamp" data-t="08:47:00">[08:47]</a>. An example of their immense energy is the "OMG particle," detected on October 15th, 1991, which was a single subatomic particle with the kinetic energy of a baseball traveling 100 kilometers per hour (51 joules) <a class="yt-timestamp" data-t="09:01:00">[09:01]</a>.

### Cosmic Ray Showers

Primary [[Historical context and secrecy of the Dzhanibekov effect | cosmic rays]] do not reach Earth's surface directly <a class="yt-timestamp" data-t="09:20:00">[09:20]</a>. Instead, they collide with air molecules about 25 kilometers above the ground, creating new particles such as pions <a class="yt-timestamp" data-t="09:24:00">[09:24]</a>. These particles further collide and decay into other particles like neutrons, protons, muons, electrons, positrons, and photons, in a cascade that streams towards the Earth <a class="yt-timestamp" data-t="09:31:00">[09:31]</a>. It is one of these secondary particles that investigators suspect struck a transistor in the Belgian election computer, causing the bit flip <a class="yt-timestamp" data-t="09:52:00">[09:52]</a>.

### Observing Cosmic Rays

In 1911, Charles Wilson perfected the cloud chamber, an enclosure containing supersaturated water or alcohol vapor <a class="yt-timestamp" data-t="10:10:00">[10:10]</a>. When a [[Historical context and secrecy of the Dzhanibekov effect | cosmic ray]] passes through, it ionizes the gas, causing vapor to condense into tiny droplets, revealing the particle's path <a class="yt-timestamp" data-t="10:22:00">[10:22]</a>. Using this technology:
*   In 1932, Carl Anderson identified the anti-electron, or positron, the first confirmed sighting of anti-matter <a class="yt-timestamp" data-t="10:40:00">[10:40]</a>.
*   Four years later, he discovered the muon, also in [[Historical context and secrecy of the Dzhanibekov effect | cosmic rays]] <a class="yt-timestamp" data-t="11:01:00">[11:01]</a>.
Anderson was awarded the Nobel Prize in Physics for his discovery of the positron <a class="yt-timestamp" data-t="11:07:00">[11:07]</a>.

## Real-World Impacts of Bit Flips

Bit flips triggered by [[Historical context and secrecy of the Dzhanibekov effect | cosmic rays]] occur constantly <a class="yt-timestamp" data-t="12:45:00">[12:45]</a>. In 1996, IBM estimated that one bit flip occurs per month for every 256 megabytes of RAM <a class="yt-timestamp" data-t="13:19:00">[13:19]</a>, with neutrons from [[Historical context and secrecy of the Dzhanibekov effect | cosmic ray]] showers being the main culprit <a class="yt-timestamp" data-t="13:27:00">[13:27]</a>.

### Computer Malfunctions
*   **Blue Screen of Death**: A "blue screen of death" error on a computer might actually be caused by a neutron strike from a [[Historical context and secrecy of the Dzhanibekov effect | cosmic ray]] <a class="yt-timestamp" data-t="12:57:00">[12:57]</a>.
*   **Speedrunning Glitch**: In 2013, during a Super Mario 64 speedrun, a player experienced an inexplicable "up warp" to a higher platform <a class="yt-timestamp" data-t="11:32:00">[11:32]</a>. This glitch, unreplicated after six years despite a $1,000 bounty, is best explained by a [[Historical context and secrecy of the Dzhanibekov effect | cosmic ray]] flipping a single bit in Mario's height coordinate <a class="yt-timestamp" data-t="12:08:00">[12:08]</a>.
*   **Supercomputer Crashes**: [[Historical context and secrecy of the Dzhanibekov effect | Cosmic rays]] have caused crashes in supercomputers, particularly at higher elevations <a class="yt-timestamp" data-t="14:14:00">[14:14]</a>. Los Alamos National Labs, located at 2,200 meters above sea level, frequently deals with neutron-induced supercomputer crashes, requiring frequent auto-saves and the installation of neutron detectors <a class="yt-timestamp" data-t="14:21:00">[14:21]</a>.

### Aviation Incidents
At cruising altitude, the radiation from [[Historical context and secrecy of the Dzhanibekov effect | cosmic rays]] increases significantly, leading to a 10 to 30 times higher chance of a single event upset <a class="yt-timestamp" data-t="14:36:00">[14:36]</a>.
*   **Airbus A330 Incident (October 7th, 2008)**: An Airbus A330 flying from Singapore to Perth suddenly pitched down, diving 200 meters in 20 seconds, injuring 119 people <a class="yt-timestamp" data-t="15:12:00">[15:12]</a>. The investigation pointed to a fault in the air data inertial reference unit (ADIRU), which supplies critical flight data <a class="yt-timestamp" data-t="15:57:00">[15:57]</a>. A bit flip in the first eight bits of a 32-bit binary word meant altitude information was mislabeled as angle of attack <a class="yt-timestamp" data-t="16:24:00">[16:24]</a>. The plane then sharply nosed down to correct what it incorrectly perceived as a stall <a class="yt-timestamp" data-t="16:41:00">[16:41]</a>. The single event effect from a high-energy atmospheric particle was considered the most likely triggering event, especially since the 1992-built aircraft had no specific regulatory requirements for resilience to such effects <a class="yt-timestamp" data-t="17:05:00">[17:05]</a>.

### Spacecraft Operations
Protecting electronics is crucial for space missions <a class="yt-timestamp" data-t="19:12:00">[19:12]</a>.
*   **Space Shuttle**: Redundancy was built into the Space Shuttle's design, with four computers simultaneously running identical software for navigation and control <a class="yt-timestamp" data-t="17:34:00">[17:34]</a>. If one had a soft error, the others would overrule it <a class="yt-timestamp" data-t="17:44:00">[17:44]</a>. This setup also allowed tracking bit flip frequency; one five-day mission recorded 161 separate bit flips <a class="yt-timestamp" data-t="17:49:00">[17:49]</a>.
*   **Perseverance Rover**: The computer on the Perseverance Rover, which landed on Mars, is a 20-year-old PowerPC from 2001, but it is "radiation hardened" <a class="yt-timestamp" data-t="19:27:00">[19:27]</a>. Its design, materials, circuits, and software are built to withstand 40 times the radiation of an ordinary computer, having been used on over a dozen space missions since 2005 <a class="yt-timestamp" data-t="19:41:00">[19:41]</a>. This hardening aims to prevent critical function errors that could lead to mission loss <a class="yt-timestamp" data-t="19:14:00">[19:14]</a>.

### Human Perception in Space
Above the atmosphere, [[Historical context and secrecy of the Dzhanibekov effect | cosmic rays]] are so energetic that astronauts sometimes report seeing flashes of light, even with their eyes closed <a class="yt-timestamp" data-t="18:01:00">[18:01]</a>. This is believed to be heavy particles or bursts of energy from radiation passing through the eyeball or optic nerve, which the body registers as a flash <a class="yt-timestamp" data-t="18:18:00">[18:18]</a>.

### Solar Cycle and Planetary Protection
The Voyager 1 spacecraft, as it departed the solar system, showed an increase in [[Historical context and secrecy of the Dzhanibekov effect | cosmic ray]] flux <a class="yt-timestamp" data-t="20:24:00">[20:24]</a>. While the sun's particles and solar wind are a source of radiation, further out, they form a "heliosphere" that acts as a protective bubble, deflecting and slowing [[Historical context and secrecy of the Dzhanibekov effect | cosmic rays]] from interstellar space, thus shielding the solar system from ionizing radiation <a class="yt-timestamp" data-t="20:33:00">[20:33]</a>. The sun's 11-year activity cycle causes this protection to fluctuate, meaning the flux of [[Historical context and secrecy of the Dzhanibekov effect | cosmic rays]] on Earth is lower when the sun is active compared to when it's dormant <a class="yt-timestamp" data-t="20:52:00">[20:52]</a>.

In Earth's history, [[Historical context and secrecy of the Dzhanibekov effect | cosmic rays]] may have played an even larger role, potentially flipping bits in the genetic codes of living organisms, thereby providing some of the variation necessary for natural selection <a class="yt-timestamp" data-t="21:05:00">[21:05]</a>.

## Mitigating Bit Flips
Modern computer chips employ various methods to be resilient against bit flips, such as error correction code (ECC) memory <a class="yt-timestamp" data-t="13:07:00">[13:07]</a>. However, it's impossible to totally prevent bit flips from occurring <a class="yt-timestamp" data-t="13:16:00">[13:16]</a>. [[Probability theory in problem solving | Problem solving]], like protecting systems from radiation, requires diverse approaches <a class="yt-timestamp" data-t="22:02:00">[22:02]</a>. Concepts such as computer memory and algorithm fundamentals are relevant for understanding and addressing these challenges <a class="yt-timestamp" data-t="22:24:00">[22:24]</a>.