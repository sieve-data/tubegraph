---
title: Challenges and innovations in integrated circuit interconnects
videoId: XHrQ-Pmvwao
---

From: [[asianometry]] <br/> 

Integrated circuits (ICs) rely on intricate networks of wires, known as interconnects, to transmit electrical signals between billions of transistors and other circuit elements [00:00:09]. Just as roads connect houses in a neighborhood, interconnects are essential for the functionality of a chip [00:00:02]. For over 30 years, these interconnects were primarily made from aluminum, with silicon dioxide serving as the insulating layer [00:00:27]. However, by the late 1990s, the semiconductor industry faced a critical need for new materials and processes to continue its progress [00:00:35]. This technical imperative led to a major transition: the adoption of copper and Low-K dielectric interconnects [00:00:51].

## Metallization
The process of laying down these metal interconnects is called "metallization" [00:01:20]. This is considered a "back end of the line" (BEOL) process, performed after the transistors are fabricated on the silicon wafer in the "front end of the line" (FEOL) [00:01:27]. During metallization, layers of fine metal wiring, known as “metal layers,” are deposited on top of the transistors [00:01:41]. These metal layers are separated by insulating dielectric material layers, technically termed "intermetal dielectric layers" [00:01:56]. To connect multiple metal layers, holes called "vias" are cut into the intermetal dielectric layers [00:02:10]. Modern advanced ICs are complex, multi-layered structures, reminiscent of Hong Kong's old Kowloon Walled City, with layers intricately jumbled and interconnected [00:02:25].

## RC Delay
A fundamental challenge in interconnect design is [[emerging_trends_and_challenges_in_chip_design | RC delay]] [00:02:45]. "RC" stands for resistance-capacitance [00:02:48].
*   **Resistance:** All wires possess resistance, which impedes electron flow, degrades signals, and leads to energy loss [00:02:53]. A wire's resistance depends on its material and is proportional to its length; thus, thicker, shorter, and wider wires have less resistance [00:03:03].
*   **Capacitance:** This refers to an object's ability to store charge [00:03:13]. Due to the close proximity of wires and the insulating dielectric layers between them, the entire setup mimics a capacitor, storing unwanted charge [00:03:18]. This unwanted capacitance slows down the interconnect's ability to carry signals [00:03:34].

Combined, resistance and capacitance create [[emerging_trends_and_challenges_in_chip_design | RC delay]], which is the extra time an electrical signal takes to travel through an interconnect [00:03:40]. A longer [[emerging_trends_and_challenges_in_chip_design | RC delay]] means signals propagate more slowly throughout the chip [00:03:52].

## Types of Interconnects
A single microchip contains several types of interconnects:
*   **Local Interconnects:** These are the lowest layers of metal wires, connecting local "blocks" of adjacent elements [00:04:13]. They are thinner and closer to each other, acting like small roads [00:04:33]. They need to be more heat-resistant due to their proximity to the transistor layer and are commonly made from poly-silicon, tungsten, or aluminum [00:04:41].
*   **Global Interconnects:** Located higher on the chip, these are larger, longer connections that span significant portions of the chip, akin to city avenues or highways [00:04:53]. They are used for delivering critical signals like clock signals for synchronization and power [00:05:09]. To minimize resistance over long distances, they are made as thick as possible and use low-resistivity metals [00:05:21].
*   **Medium-Distance Interconnects:** Layers between global and local interconnects, sometimes called semi-global or intermodule interconnects [00:05:34].

Logic chips generally feature more metal layers (sometimes 10-15) than memory chips (3-5) [00:05:48]. Memory chips have a repetitive, dense structure requiring fewer interconnects and may have bumpy structures like trench capacitors [00:05:57]. Logic chips are more irregular and prioritize correct connections, necessitating more interconnects and layers [00:06:13].

## Early Materials: Aluminum and Silicon Dioxide
Initially, silicon dioxide served as the intermetal dielectric layer, and aluminum was used for the interconnects, especially the global ones [00:06:28]. The primary reason for their adoption was their ease of manufacturing [00:06:37]. Silicon dioxide could be easily laid down in thick layers using chemical vapor deposition [00:06:45]. Aluminum, while having higher resistance than silver, copper, and gold, worked well with silicon dioxide in manufacturing [00:06:54].

The manufacturing process involved depositing a thick layer of aluminum on silicon dioxide, using lithography to transfer the interconnect pattern, and then etching away unwanted parts [00:07:06]. For multiple layers, another intermetal dielectric layer would be deposited and polished for a smooth surface [00:07:28]. Aluminum and silicon dioxide formed a protective aluminum oxide (alumina) layer at their interface, preventing aluminum atoms from diffusing into the silicon dioxide [00:07:42]. This process worked effectively for the first three decades of semiconductor technology [00:08:00].

## Getting Denser: The Interconnect Problem
As chips became denser with smaller transistors, the number of interconnects increased [00:08:11]. Designers scaled interconnect systems by shrinking their size (e.g., pitch, the distance between wires) [00:08:21]. However, this increased electrical resistance, leading to more [[emerging_trends_and_challenges_in_chip_design | RC delay]] [00:08:33]. Engineers responded by making wires relatively taller, but this step-like structure presented [[challenges_in_semiconductor_manufacturing | manufacturing challenges]] at nanometer scale [00:08:42]. Denser wire clusters also led to more unwanted capacitance, further increasing [[emerging_trends_and_challenges_in_chip_design | RC delay]] [00:09:03]. Adding more metal layers introduced [[challenges_in_semiconductor_manufacturing | process challenges]], as each layer required deposition, lithography, and etching, increasing the risk of defects and reducing yield [00:09:12].

Initially, [[emerging_trends_and_challenges_in_chip_design | RC delay]] was less significant than delays from the circuit devices themselves [00:09:42]. However, as chips grew more complex, [[emerging_trends_and_challenges_in_chip_design | RC delay]] became a dominant factor in chip speed by the mid-1990s [00:09:53]. By 1994, interconnect pitches on global layers had shrunk significantly from 20 micrometers in 1978 to 1.8 micrometers [00:10:08]. Projections for the 100-nanometer process node (a few years away) indicated that transmitting a signal through a 1-millimeter interconnect would take six times longer than through an equivalent-sized transistor [00:10:45]. This bottleneck necessitated a fundamental change [00:10:03].

## The Solution: Copper and Low-K Dielectrics
To mitigate the [[emerging_trends_and_challenges_in_chip_design | RC delay]] issue, scientists proposed replacing the interconnect system's materials [00:11:04].
1.  **Copper Interconnects:** Switching from aluminum to copper for interconnects was an obvious choice, as copper lines have 35% less resistance than aluminum counterparts [00:11:13].
2.  **Low-K Dielectrics:** To reduce unwanted capacitance, the insulating dielectric layer material needed to be changed from silicon dioxide (k-value of 3.9) to a material with a lower "dielectric constant" or "k-value" [00:11:26]. These new materials were termed "low-K dielectrics" [00:11:44].

Combining copper and low-K dielectrics allowed manufacturers to use fewer metal layers and thinner wires, potentially reducing [[emerging_trends_and_challenges_in_chip_design | RC delay]] by a factor of four [00:11:57].

## IBM's Big Announcement and Copper Challenges
In September 1997, IBM stunned the semiconductor world by announcing its successful production of copper interconnects [00:12:08]. Their 15-year "red aluminum" project involved a secret team of engineers working exhaustively [00:12:16]. This achievement, marked by a famous image of six layers of copper interconnects, positioned IBM to mass-produce copper-wired wafers by early 1998 [00:12:47].

IBM's breakthrough was significant because copper presented serious [[challenges_in_semiconductor_manufacturing | manufacturing problems]] [00:13:09]:
*   **Copper Poisoning:** Unlike aluminum, copper atoms can quickly diffuse into silicon or silicon dioxide, accumulating and degrading chip performance, a phenomenon known as "copper poisoning" [00:13:20]. This necessitates a "diffusion barrier" to block copper from entering the silicon [00:13:34]. Materials like tantalum or tantalum nitride are commonly used for this barrier, requiring specific properties like adhesion, corrosion resistance, and even deposition [00:13:43].
*   **Inability to Etch:** Copper lacks a suitable etchant, meaning it cannot be deposited and then etched away like aluminum [00:13:59].

### The Damascene Method
To overcome the etching problem, IBM reversed the traditional manufacturing sequence, developing the "damascene method" [00:14:13]:
1.  An intermetal dielectric layer is laid down [00:14:21].
2.  Lithography is used to transfer interconnect patterns (trenches and vias) onto the dielectric [00:14:26].
3.  The pattern is etched into the dielectric layer [00:14:33].
4.  A diffusion barrier (e.g., tantalum) is applied to protect against copper diffusion [00:14:38].
5.  The trenches are filled with copper, typically using electroplating, a process IBM pioneered [00:14:49].
6.  Excess copper is sanded off [00:15:03].
7.  A capping layer is applied to prevent copper diffusion [00:15:08].

Named after ancient metal inlay techniques from Damascus, this complex and counter-intuitive process was a key innovation [00:15:14].

### The Copper Road: Cumulative Advancements
IBM's announcement was built on a series of [[technological_advancements_in_semiconductor_manufacturing | cumulative technological advancements]]:
*   **Diffusion Barriers:** Research on tantalum and tantalum nitride as effective diffusion barriers began in the late 1980s and continued into the early 1990s [00:15:43].
*   **Damascene Invention:** IBM invented the damascene method around 1985 [00:15:55].
*   **Copper Filling Breakthrough:** The biggest hurdle was filling the trenches and vias with copper without defects [00:16:05]. Traditional methods like sputtering, physical vapor deposition, and chemical vapor deposition led to seams or voids [00:16:11]. In 1989, a small group at IBM discovered "super-filling" or "bottoms-up growth" using electroplating, which allowed trenches to be filled uniformly from the bottom [00:16:34].
*   **Multi-level Copper Wires:** By 1993, an IBM team combined diffusion barriers, damascene, and electroplating to produce multi-level copper wires, demonstrating copper's viability [00:16:49].
*   **Dual Damascene:** The initial damascene method was not economically viable due to throughput and yield issues, especially with vias [00:17:04]. In 1995, another IBM team led by Dan Edelstein re-engineered the process, developing a "dual damascene" methodology that produced both trenches and vias simultaneously [00:17:16]. This new recipe met internal requirements, leading to the 1997 announcement [00:17:31].

## Bringing Copper to the Fab
Implementing copper at high volume presented significant [[challenges_in_semiconductor_manufacturing | manufacturing challenges]] for IBM's foundry [00:17:42]:
*   **Isolation:** Due to copper's toxicity to silicon, tools used for copper lines (lithography, metrology) had to be isolated from the rest of the fab, a difficult task given that many fabs shared tools [00:17:58].
*   **Waste Disposal:** Copper easily dissolves in water and is toxic, requiring new waste disposal technologies in the fab [00:18:15].

## Industry Catch-up
Despite IBM's initial lead, other companies quickly caught up [00:18:28]. While IBM was the sole investigator of copper interconnects before 1989, the industry recognized the deficiencies of aluminum after that point, and copper became an obvious replacement [00:18:49]. Subtle cues from IBM's published papers hinted at their copper work, prompting other companies to initiate their own programs [00:19:06].

*   **Motorola:** Started copper work in 1990, guessing IBM's progress through changes in PowerPC design rules from their alliance [00:19:18]. They announced their own copper interconnects just two weeks after IBM in October 1997 [00:18:38].
*   **AMD & AT&T (Bell Labs):** Began copper work around 1995, with AT&T developing its stack independently [00:19:36].
*   **Intel:** Surprisingly, Intel did not start its copper program until 1997, despite its researchers having published on copper electroplating in 1989 [00:19:51].

Much of the rapid catch-up was facilitated by increased public research, often coordinated through consortia like Sematech, which directed R&D funds to universities [00:20:16]. Findings were released into the public domain, and semiconductor companies hired graduates from these research teams [00:20:33]. While IBM guarded details of its copper fill process, the rest of the industry rapidly closed the gap [00:20:45].

## The 180 Nanometer Node Transition
The 180-nanometer node, scheduled for high-volume production in 1999, represented a major technological shift, bringing several [[technological_advancements_in_semiconductor_manufacturing | technical changes]] simultaneously [00:20:57]:
*   **Copper Interconnects:** Implementation of copper wiring.
*   **Feature Size Reduction:** Another 30% reduction in feature size, adhering to Moore's Law [00:21:15].
*   **New Lithography Tools:** Introduction of 193-nanometer DUV excimer laser lithography tools [00:21:22].
*   **300mm Wafer Transition:** The planned transition to 300-millimeter wafers was pushed back to the 130-nanometer node due to the complexity of the other concurrent changes [00:21:34].

In 1998, IBM kicked off the 180-nanometer generation with the PowerPC 750CX, boosting chip speeds from 300 to 400 MHz due to copper interconnects [00:21:49]. Motorola followed closely, releasing a 220-nanometer "half node" in late 1998, with PowerPC G4 chips powering Apple's laptops [00:22:06].

The semiconductor [[challenges_in the_semiconductor_industry | manufacturing industry]] at the time was more fragmented, with many players adopting their own variants of the 180-nanometer "generation" [00:22:28]. Intel's 180-nanometer process, for instance, did not use copper interconnects [00:22:45]. This was due to their late start with copper and their massive capacity needs for PC CPUs (112,000 200-millimeter wafers per month by 2000), for which there weren't enough copper tools available [00:22:56]. Intel would not implement copper until the 130-nanometer node in November 2000, and even then, only six of seven layers were copper [00:23:17].

### TSMC and UMC's Copper Journey
Taiwanese foundries TSMC and UMC, initially far behind American companies, had no serious experience with copper until 1997 [00:23:29]. Both faced a steep learning curve [00:23:41]. TSMC had struggled with its 250-nanometer process, allowing UMC to rapidly catch up in market share and capacity by 1999 [00:23:46].

*   **UMC's Approach:** UMC joined an IBM-sponsored research consortium (likely the Semiconductor Research Corporation) to collectively research copper interconnects, benefiting from IBM's patents [00:25:18].
*   **TSMC's Approach:** TSMC, under CEO Morris Chang and led by Dr. Chiang Shang-yi, chose to go it alone [00:24:43]. A team of six elite scientists, including Dr. Liang Mong-song, embarked on a crash effort to develop a proprietary copper implementation [00:25:31].

Both strategies yielded results. By 1999, both UMC and TSMC began shipping 180-nanometer chips to fabless customers, with the top two metal layers made of copper [00:25:58]. While lagging behind IBM's more extensive copper integration (six of seven layers), this was a significant step toward full "copper-ization" [00:26:10].

## The Low-K Problem
While copper addressed wire resistance, the equally critical challenge was finding a suitable "low-K" material for the intermetal dielectric layers to reduce unwanted capacitance [00:26:23]. This problem proved more difficult than copper, as the industry struggled to find a material that integrated well into the process flow and met reliability metrics [00:26:56]. The difficulty with low-K was not just an [[challenges_in the_semiconductor_industry | engineering problem]], but a fundamental lack of understanding of what material properties were needed [00:27:13].

The semiconductor industry attempted low-K implementations three times:
1.  **250 Nanometer Node: Fluorinated Silicon Glass (FSG):** Silicon dioxide was doped with fluorine to create FSG, which had a slightly lower k-value (3.5 vs. 3.9) and was applied using chemical vapor deposition [00:27:37].
2.  **180 Nanometer Node: Hydrogen Silsesquioxane (HSQ) with Spin-on:** The industry tried HSQ, with a lower k-value of 2.8, applied using a "spin-on" technique [00:27:58]. This method involved quickly spinning the wafer and pouring the dielectric, seen as a cheaper way to achieve an even layer [00:28:18]. However, HSQ failed to scale in high-volume production; the combination of spin-on and high fab temperatures caused the HSQ layer to distort [00:28:34]. TSMC and Texas Instruments both faced significant setbacks, forcing TSMC to revert to FSG during production, working through holidays to recover [00:28:53].

## The Legendary 130 Nanometer Node
The 130-nanometer node, following TSMC's minor 150-nanometer node, was anticipated to fully complete the copper interconnect transition and introduce a "true" low-K dielectric [00:29:37]. The material choice for this low-K layer became a major point of contention.

*   **IBM's Bold Choice (SiLK):** In April 2000, IBM (working with UMC and Infineon) announced the adoption of Dow Chemical's proprietary low-K material, SiLK, applied using the spin-on technique [00:30:02]. SiLK boasted a k-value of 2.6 (potentially 2.2), designed to meet needs up to the 65-nanometer node [00:30:23].
*   **Alternative Path (Black Diamond):** Many in the industry, including Texas Instruments, favored "Black Diamond" from Applied Materials, which had a k-value of 2.8 [00:30:38]. The crucial difference was that Black Diamond was exclusive to chemical vapor deposition (CVD), not spin-on [00:30:55].

The industry split: IBM, UMC, and their affiliates chose SiLK, while Texas Instruments and TSMC opted for Black Diamond [00:31:13]. TSMC's Dr. Chiang personally swore off the spin-on technique after the HSQ debacle [00:31:36]. Intel, needing massive capacity, stuck with the older FSG technique for their 130nm process [00:31:44].

Ultimately, the SiLK + spin-on setup failed in high-volume production. IBM failed to ship a product with it, and UMC's customers also struggled, incurring significant financial and strategic costs [00:31:53].

On October 2001, TSMC became the first to ship 130-nanometer chips with both copper interconnects and a low-K dielectric (Black Diamond via CVD) [00:32:07]. They also offered an alternate FSG dielectric version for customers like Nvidia to ensure supply [00:32:16]. While initial yields for products like Nvidia's NV30 were low (in the teens), they reached over 70% by late 2002 [00:32:29].

By the end of 2001, UMC abandoned SiLK and switched to a Novellus Systems CVD process [00:32:40]. IBM delayed acknowledging the failure until 2002, when a major customer, Xilinx, publicly attributed delays in their FPGAs to SiLK [00:32:55]. IBM eventually switched to CVD as well, defending their initial decision by stating SiLK "looked like it had the potential to have a lower dielectric constant" [00:33:24].

## Conclusion
TSMC's successful 130-nanometer node was monumental, setting the Taiwanese giant apart [00:34:04]. The R&D team, known as "the Six R&D Horsemen," received a national award in 2003 for their achievement [00:34:10]. This node transformed TSMC's perception from a mere factory to a formidable innovator in the semiconductor industry, fundamentally changing its reputation [00:34:21]. IBM, despite its initial breakthroughs, failed to capitalize on its innovations in high-volume manufacturing, leading to a loss of market leadership in this critical transition [00:33:54].