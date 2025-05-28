---
title: Unexpected glitches in voting systems
videoId: AaZ_RSt0KP8
---

From: [[veritasium]] <br/> 

On May 18th, 2003, voters in Belgium participated in an election where voting was primarily conducted on computers, a practice the Belgians had been experimenting with for over a decade [00:00:22]. The system included a backup, where each voter's selection was saved both to the computer and a magnetic card, which was then dropped into a box for redundancy [00:00:29].

## The Schaerbeek Vote Anomaly

During the tabulation of votes late on election night, officials discovered a significant problem with the results from Schaerbeek, a municipality in central Brussels [00:00:44]. Maria Vindevogel, a relatively unknown candidate, appeared to have received more votes than was mathematically possible, a fact identified due to the preferential voting system in place [00:00:54].

A recount was triggered using the magnetic cards [00:01:05]. After several hours, the recount was completed, and while most candidates' vote totals remained the same, Maria Vindevogel's recounted number of votes was exactly 4,096 less than her original tally [00:01:17]. This meant her initial count had been inflated by over 4,000 votes [00:01:33].

## Investigation and the "Bit Flip" Explanation

Computer experts were called in to investigate, running extensive tests on the software and combing through the code, but they found no bugs [00:01:38]. They also tested the hardware of the computer that made the initial erroneous tally repeatedly, but could not replicate the error, and the hardware appeared to be in perfect working order [00:01:46].

The clue to the mystery lay in the number 4,096 [00:02:04]. Computers operate using binary, where strings of zeros and ones correspond to powers of two [00:02:11]. For Maria Vindevogel's vote count, a string of bits represented her votes, incrementing by one for each vote received [00:02:17]. The number 4,096 is exactly 2 to the power of 12, which corresponds to the 13th bit in binary [00:02:40]. Therefore, for Maria Vindevogel to receive an extra 4,096 votes, the 13th bit in her vote count had to have flipped from a zero to a one [00:02:48].

This phenomenon is known as a [[bit_flips_in_electronic_systems | single event upset]], a type of soft error where a bit changes without damaging the device [00:04:34].

## Historical Precedent: Radioactive Packaging

Belgian investigators discovered that [[bit_flips_in_electronic_systems | similar issues]] had been reported by large computer companies starting in the 1970s [00:03:12]. In 1978, Intel observed strange errors in their 16 kilobit dynamic random access memory (DRAM), where ones would spontaneously flip to zeros [00:03:19].

The problem was traced to the ceramic packaging of the chip [00:03:33]. A new manufacturing plant on the Green River in Colorado was built downstream from an old uranium mill [00:03:41]. Radioactive atoms, specifically trace amounts of uranium and thorium, made their way into the river and subsequently into the ceramic packaging for Intel's microchips [00:03:52].

Alpha particles emitted by these radioactive elements were energetic enough to create electron-hole pairs in the silicon [00:04:14]. If an alpha particle struck in the right place, it could generate enough charge carriers to cause electrons to accumulate in the memory well, effectively flipping a bit from one to zero [00:04:22]. This issue became apparent in the 1970s because chip components had miniaturized to the point where a single alpha particle could produce enough charge to flip a bit [00:05:01]. Following these findings, chip manufacturers became more cautious about avoiding radioactive materials in their microchip production and packaging [00:05:18].

## Cosmic Rays: The Unseen Culprit

Since the bit flip in the Belgium election was not caused by natural radioactivity in the computer itself [00:05:31], investigators suspected another source: cosmic rays.

Cosmic rays are high-energy radiation from space, discovered by Victor Hess in 1912 through balloon flights measuring radiation at increasing altitudes [00:07:04]. While some low-energy cosmic rays originate from the sun, high-energy cosmic rays, which move close to the speed of light, come from exploding stars (supernovae) and supermassive black holes in distant galaxies [0008:23]. As charged particles, they are deflected by magnetic fields in space, making their precise origin hard to pinpoint [00:08:49].

Primary cosmic rays do not reach Earth's surface directly. Instead, they collide with air molecules about 25 kilometers above the ground, creating a cascade of secondary particles like neutrons, protons, muons, electrons, positrons, and photons [00:09:24]. It is one of these secondary particles that investigators suspect struck a transistor in the Belgium computer, causing the 13th bit to flip and giving Maria Vindevogel her 4,096 extra votes [00:09:52].

## Impact and Mitigation of Bit Flips

[[Bit_flips_in_electronic_systems | Cosmic rays]] are constantly triggering bit flips [00:12:45]. For instance, a "blue screen of death" error on a computer might actually be caused by a neutron strike [00:12:57]. In 1996, IBM estimated that for every 256 megabytes of RAM, one bit flip occurs per month, with neutrons from cosmic ray showers being the main culprit [00:13:19].

While the Toyota unintended acceleration recalls were largely attributed to sticky pedals, floor mats, and driver error rather than cosmic rays [00:14:02], cosmic rays have been implicated in crashes of supercomputers, especially at higher elevations [00:14:14]. Los Alamos National Labs, located 2200 meters above sea level, frequently deals with neutron-induced supercomputer crashes and employs frequent auto-saves and neutron detectors [00:14:21].

The risk of [[bit_flips_in_electronic_systems | single event upsets]] increases significantly at higher altitudes, such as cruising altitude in a plane, where the chance of a bit flip can increase by 10 to 30 times [00:14:59]. This is a concern for critical systems like flight computers.

### Aviation Incident

On October 7th, 2008, an Airbus A330 flying from Singapore to Perth experienced a sudden pitch down, diving 200 meters in 20 seconds, causing injuries to 119 people on board [00:15:12]. The investigation identified a fault with the first air data inertial reference unit (ADIRU), which supplies critical flight data like airspeed, angle of attack, and altitude [00:16:00]. The data is transmitted as a 32-bit binary word [00:16:13]. It is believed that a bit flip in the first eight bits, which identify the type of information, caused altitude information to be mislabeled as angle of attack [00:16:26]. This led the plane to sharply nose down to correct a perceived stall, triggering alarms for both overspeed and stall simultaneously [00:16:34].

Investigators ruled out software bugs, hardware failures, environmental factors, and electromagnetic interference as likely causes [00:16:51]. The remaining potential trigger was a [[bit_flips_in_electronic_systems | single event effect]] resulting from a high-energy atmospheric particle striking an integrated circuit [00:17:07]. A challenge in investigating such events is that they are soft errors and leave no trace [00:17:16]. Notably, the Airbus A330 was built in 1992, before specific regulatory or manufacturer requirements for airborne systems to be resilient to single event effects were in place [00:17:24].

### Protection Measures

Modern computer chips employ various methods to be resilient against bit flips, such as error correction code (ECC) memory [00:13:07]. However, bit flips cannot be entirely prevented [00:13:16].

For critical space missions, extensive measures are taken. The Space Shuttle, for instance, had four computers simultaneously running identical software for navigation and control, allowing the other three to overrule a single soft error [00:17:34]. This system also allowed tracking of bit flip frequency, revealing 161 separate bit flips on one five-day mission (STS 48) [00:17:50].

The computer on the Mars Perseverance Rover, launched in 2020, uses a 20-year-old PowerPC from 2001 [00:19:28]. Despite its age, it is radiation-hardened, meaning its design, materials, circuits, and software are built to withstand 40 times the radiation of an ordinary computer [00:19:41]. This technology has been used on over a dozen space missions since 2005 [00:19:52]. Testing for radiation hardening involves subjecting processors to particle beams to induce "blue screens of death" and then designing solutions to prevent them, as a spacecraft in such a state is often unrecoverable [00:20:01].

The heliosphere, a protective bubble formed by particles streaming from the sun and solar wind, helps deflect and slow down cosmic rays from interstellar space, protecting the solar system from ionizing radiation [00:20:33]. The sun's 11-year activity cycle causes this protection to fluctuate, with cosmic ray flux on Earth being lower when the sun is active [00:20:52].

Even in human perception, astronauts in space have reported seeing flashes of light with their eyes closed, which are believed to be heavy cosmic ray particles passing through the eyeball or optic nerve [00:18:08].