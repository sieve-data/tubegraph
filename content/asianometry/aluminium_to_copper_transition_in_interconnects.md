---
title: Aluminium to copper transition in interconnects
videoId: XHrQ-Pmvwao
---

From: [[asianometry]] <br/> 

Integrated circuits (ICs) rely on [[local_and_global_interconnects_in_microchips | interconnects]], which are wires transmitting electrical signals between transistors and other circuit elements <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. For over 30 years, these interconnects and their insulating layers were made from aluminium and silicon dioxide, respectively <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. However, by the late 1990s, new materials became technically necessary <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This significant [[generational_shifts_in_semiconductor_manufacturing | technology transition]] created opportunities for companies like [[us_technology_transfer_concerns_with_tsmc | TSMC]] to gain a lead <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This article examines the semiconductor industry's major [[copper_lowk_interconnect_transition | transition to copper/Low-K interconnects]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Metallization

The process of laying down these metal interconnects is called "metallization" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. As a "back end of the line" process, metallization occurs after transistors are created on the silicon wafer in the "front end of the line" <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Layers of fine metal wiring, known as "metal layers," are placed on top of the transistors <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. These metal layers are separated by insulating dielectric materials called "intermetal dielectric layers" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Holes, known as "vias," are cut into these dielectric layers to connect multiple metal layers <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

Modern integrated circuits are complex, with many layers intricately interconnected, resembling Hong Kong's old Kowloon Walled City rather than a flat landscape <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## RC Delay

A critical challenge in interconnect design is RC delay, which stands for resistance-capacitance <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Resistance** impedes electron flow through wires, degrading signals and losing energy <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. It depends on material and is proportional to length; thicker, shorter, and wider wires have less resistance <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Capacitance** refers to an object's ability to store charge <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Because wires are physically close with insulating dielectric layers between them, the setup acts like a capacitor, storing unwanted charge that slows down signal propagation <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

RC delay is the extra time for an electric signal to travel through an interconnect <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The longer the RC delay, the slower signals propagate throughout the chip <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. An analogy is filling a bucket of water: resistance is how fast water goes in, and capacitance is the bucket's size; RC delay is the time it takes to fill the bucket <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Types of Interconnects

A single microchip features several types of interconnects <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>:

### Local Interconnects
The lowest metal layers placed on top of transistors are [[local_and_global_interconnects_in_microchips | local interconnects]] <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. They connect adjacent elements, similar to small roads in a neighborhood <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. These can be thinner and closer due to shorter distances, but must be more heat-resistant due to proximity to the transistor layer <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Common materials include poly-silicon, tungsten, or aluminium <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Global Interconnects
Higher up are [[local_and_global_interconnects_in_microchips | global interconnect]] layers, which are larger, longer connections spanning significant chip portions, akin to city avenues or highways <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. These also deliver essential signals like clock synchronization and power <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. To cover long distances with minimal resistance, they are made as thick as possible using low-resistivity metals <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Medium-distance layers, often called semi-global or intermodule interconnects, exist between local and global layers <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

## Logic versus Memory
Logic chips generally have more metal layers (sometimes 10-15) than memory chips (3-5) <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. Memory chips have a repetitive, dense structure requiring fewer interconnects and often feature bumpy structures like trench capacitors <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Logic chips are more irregular with less device density, prioritizing precise connections, thus requiring more interconnects <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Materials (Old)
Initially, silicon dioxide was used for the intermetal dielectric layer and aluminium for interconnects, especially global ones <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Both materials were chosen for their ease of manufacturing <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Silicon dioxide could be easily laid down using chemical vapor deposition (CVD) <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Aluminium, having the fourth-lowest resistance after silver, copper, and gold, also worked well with silicon dioxide <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

The process involved depositing a thick layer of aluminium on silicon dioxide, then using lithography to pattern and etch away unwanted parts <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Subsequent layers required depositing more intermetal dielectric and polishing for a smooth surface <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. Aluminium and silicon dioxide were compatible because they reacted to form aluminium oxide (alumina) at their interface, which acted as a protective sheath preventing aluminium atoms from diffusing into the silicon dioxide <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This process worked well for 30 years <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Getting Denser
As chips became denser with smaller transistors, the interconnect system scaled in two ways <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>:
1.  **Shrinking interconnects**: Reducing the distance between parallel wires (pitch) increased electrical resistance, leading to more RC delay <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
2.  **Taller wires**: Engineers made wires relatively taller to compensate for increased resistance, but this created difficult-to-manufacture step-like structures and increased unwanted capacitance, further contributing to RC delay <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
Adding more metal layers also posed challenges, increasing the likelihood of manufacturing defects and worsening yields, making chips less economically viable <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### The Big Problem
Initially, RC delay was negligible compared to delays from circuit devices <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. However, as chips grew more complex, RC delay became a significant factor in chip speed <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. By the mid-1990s, it was clear the existing approach was unsustainable <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. For example, in 1978, the interconnect pitch for the second metal layer (M2) was 20 micrometers <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. By 1994, global layer pitches, which were supposed to be the widest, were 1.8 micrometers <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. Although aluminium interconnects were used for one more generation (the 250 nanometer node ramping up in 1996), the end was near <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. Looking ahead to the 100 nanometer node, signal transmission through a 1-millimeter interconnect would take six times longer than through an equivalent transistor <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.

## Copper & Low-K

To address the RC delay issue, scientists decided to replace the interconnect system's materials <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>:
1.  **Copper for Interconnects**: Switching from aluminium to copper was an obvious choice, as copper lines have 35% less resistance <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
2.  **Low-K Dielectric**: Unwanted capacitance could be reduced by replacing silicon dioxide (k-value 3.9) with a new insulating dielectric material that carries less charge <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. This material needed a lower "dielectric constant" or "k-value," hence it was called "low-K dielectric" <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

Together, a copper and low-K solution could allow manufacturers to use fewer metal layers and thinner wires, potentially cutting RC delay time by a factor of four <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

## IBM's Big Announcement
In September 1997, IBM announced they had successfully produced copper interconnects after 15 years of secret work on the "red aluminium" project <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. Engineers worked tirelessly, driven by a deep sense of motivation <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. The achievement was capped by a famous image of six layers of copper interconnects <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. IBM planned to mass-produce copper-wired wafers by early 1998, with the first chips going to Apple Computer for their Power Macs <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

## Copper Problems
IBM's announcement was significant because copper presented serious manufacturing problems compared to the aluminium-silicon friendly pairing <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

First, copper atoms can quickly diffuse into silicon or silicon dioxide, accumulating like mercury and hurting chip performance—a phenomenon known as "copper poisoning" <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. Semiconductor manufacturers must produce a "diffusion barrier" (usually from tantalum or its compounds) to block copper from entering the silicon <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. This barrier must adhere to both copper and low-K insulation layers, resist corrosion, and be easily and evenly deposited <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

Second, copper cannot be etched in the same way as aluminium <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. This meant the traditional sequence of depositing a metal layer and then etching away unwanted parts was not possible <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

## Damascene
IBM reversed the traditional manufacturing sequence, adopting the "damascene method" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>:
1.  Lay down the intermetal dielectric layer <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
2.  Use lithography to transfer interconnect patterns (trenches and vias) onto the dielectric <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
3.  Etch the pattern into the dielectric layer <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.
4.  Apply the diffusion barrier (tantalum-based) <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
5.  Fill the trenches with copper, typically using electroplating for "super-filling" or "bottoms-up growth" <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
6.  Sand off excess copper and apply a capping layer to prevent diffusion <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

This complex, unintuitive process, named after the ancient metal inlay techniques from Damascus, is critical for copper integration <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

## The Copper Road (Technological Advancements)
IBM's breakthrough was built on cumulative [[technological_advancements_in_cable_design | technological advancements]] <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>:
*   **Diffusion Barriers**: Research on tantalum and tantalum nitride as diffusion barriers began in the late 1980s and early 1990s <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.
*   **Damascene Method**: IBM invented the damascene method around 1985 <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
*   **Copper Filling**: The biggest challenge was filling trenches with copper without defects using traditional methods like sputtering or CVD <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. In 1989, a group discovered "super-filling" or "bottoms-up growth" using electroplating, which filled the trench from the bottom up like a liquid <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.
*   **Multi-level Copper Wires**: In 1993, an IBM team combined diffusion barriers, damascene, and electroplating to produce multi-level copper wires <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **Dual Damascene**: The initial damascene method wasn't economically viable due to throughput and yield issues <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. In 1995, an IBM team led by Dan Edelstein re-engineered the process to "dual damascene," which produced both trenches and vias simultaneously <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. This new recipe passed internal requirements, leading to the 1997 announcement after two more years of development <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.

## Bringing it to the Fab
Implementing copper interconnects in high-volume production at IBM's chip foundry was formidable <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. Copper can poison silicon, requiring copper line tools (lithography, metrology) to be isolated within the fab, a challenge given shared tools across different lines <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. Additionally, copper dissolves in water and is toxic, necessitating new waste disposal technologies <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

## Rumblings & Rapid Catch-up
Despite IBM's announcement being seen as a 1-3 year lead <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>, Motorola announced copper interconnects just two weeks later in October 1997 <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. While IBM was the sole company investigating copper before 1989 <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>, the entire industry recognized aluminium's deficiencies after that and started working on copper <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.

Motorola began copper work in 1990, inferring IBM's progress through changes in PowerPC design rules <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. AMD started around 1995 and quickly ramped up <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. AT&T (Bell Labs) also developed their copper interconnect stack independently <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. Surprisingly, Intel did not start its copper program until 1997, despite its researchers publishing on copper electroplating in 1989 <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.

Research on copper interconnect technology increased leading up to IBM's announcement, with much work done through Sematech, an R&D consortium <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>. Public R&D funds were directed to universities, and findings were released into the public domain, allowing other companies to hire trained graduate students <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. While IBM tried to keep details of its copper fill process secret, the industry rapidly caught up <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>.

## 180 Nanometers Node
The 180 nanometer node, scheduled for high-volume production in 1999, introduced significant technical changes <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>:
*   It incorporated copper interconnects and a 30% reduction in feature size, adhering to [[generational_shifts_in_semiconductor_manufacturing | Moore's Law]] <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.
*   New 193-nanometer DUV excimer laser lithography tools were being introduced <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
*   The transition to 300 millimeter wafers was initially planned for this node but was pushed back to the 130 nanometer node due to the other ongoing changes <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

In 1998, IBM launched the 180 nanometer generation with the PowerPC 750CX, using copper interconnects to boost chip speeds from 300 to 400 Megahertz, placing IBM in the technological lead <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>. Motorola followed closely, rolling out a 220 nanometer "half node" in late 1998 with their PowerPC G4 chips <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

At this time, the semiconductor manufacturing industry had many more players, each with their own variant of the 180 nanometer generation <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. Notably, Intel's 180 nanometer process did not use copper interconnects <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. This was due to their late start with copper and the insufficient supply of copper tools to meet their massive production needs for PC CPUs <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>. Intel only implemented copper interconnects in November 2000 with the 130 nanometer node, where only six of seven layers were copper <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.

## TSMC and UMC
Taiwanese foundries [[us_technology_transfer_concerns_with_tsmc | TSMC]] and UMC, initially far behind American companies, had not seriously considered copper until 1997 <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>. [[us_technology_transfer_concerns_with_tsmc | TSMC]] struggled with its 250 nanometer process, allowing rival UMC to rapidly gain market share and capacity by 1999 <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. UMC CEO John Hsuan confidently predicted surpassing [[us_technology_transfer_concerns_with_tsmc | TSMC]] in revenue <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>.

[[us_technology_transfer_concerns_with_tsmc | TSMC]] Chairman and CEO Morris Chang was determined to prevent this <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>. Dr. Chiang Shang-yi, appointed as VP of R&D in mid-1997, worked intensely to resolve [[us_technology_transfer_concerns_with_tsmc | TSMC]]'s issues <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>. Facing the need for copper at the 180 nanometer node, UMC joined an IBM-sponsored research consortium (Semiconductor Research Corporation) to benefit from IBM's patents <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. [[us_technology_transfer_concerns_with_tsmc | TSMC]], however, chose to go it alone, with a team of six elite scientists (including Dr. Liang Mong-song) undertaking a crash effort to develop their own copper interconnect implementation <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

Both approaches yielded results <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>. In 1999, both UMC and [[us_technology_transfer_concerns_with_tsmc | TSMC]] shipped 180-nanometer chips to fabless customers, with the top two metal layers made with copper <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>. While lagging IBM's six-of-seven copper layers, it was a significant step towards full copper integration <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>.

## The Low-K Problem
While copper addressed wire resistance, a good low-K material for intermetal dielectric layers was needed to cut unwanted capacitance <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>. The challenge was finding a low-K material that fit the process flow and met reliability metrics, as existing materials often failed <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>. Unlike copper, where the engineering problem was defined, with low-K, the required engineering solution itself was unclear <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>.

### TSMC Spins Around
The semiconductor industry attempted low-K integration three times:
1.  **250 nanometer node**: Fluorinated Silicon Glass (FSG), silicon dioxide doped with fluorine, had a slightly lower K-value (3.5 vs. 3.9) and was applied via CVD <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
2.  **180 nanometer node**: Hydrogen silsesquioxane (HSQ), with a lower K-value (2.8), was attempted using a "spin-on" technique, where the dielectric was poured onto a quickly spinning wafer <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>. Although HSQ passed internal tests, it failed to scale in high-volume production because the spin-on technique combined with high fab temperatures stressed the HSQ layer, causing distortion <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>. This was a major setback for [[us_technology_transfer_concerns_with_tsmc | TSMC]] and Texas Instruments, leading to [[us_technology_transfer_concerns_with_tsmc | TSMC]] shipping 180 nanometers late <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>.

## The Legendary 130
The 130 nanometer node (after [[us_technology_transfer_concerns_with_tsmc | TSMC]]'s minor 150nm node) was anticipated to complete the copper interconnect transition and introduce a "true" low-K dielectric <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>.

In April 2000, IBM, UMC, and Infineon announced their adoption of Dow Chemical's proprietary low-K material, SiLK, with a K-value of 2.6 (potentially 2.2), applied via spin-on <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>. This was a bold choice <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>.

However, other industry players like Texas Instruments favored "Black Diamond" from Applied Materials, with a K-value of 2.8, applied exclusively through CVD <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>. The industry split <a class="yt-timestamp" data-t="00:31:13">[00:31:13]</a>: IBM, UMC, and affiliates chose SiLK; Texas Instruments and [[us_technology_transfer_concerns_with_tsmc | TSMC]] opted for Black Diamond (Dr. Chiang Shang-yi personally vowed never to use spin-on again) <a class="yt-timestamp" data-t="00:31:27">[00:31:27]</a>; Intel stuck with the older FSG technique due to its massive capacity needs <a class="yt-timestamp" data-t="00:31:44">[00:31:44]</a>.

Ultimately, the SiLK + spin-on setup failed, with both IBM and UMC's customers unable to ship products <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.

> [00:33:32] "Quite bluntly, there were a lot of reasons to run with SiLK ... On the surface, it looked like it had the potential to have a lower dielectric constant. No one else was doing it at the time, and we just made a decision. We ran with SiLK ... Instead of throwing rocks at us, the industry should be saying 'Thanks guys, you saved us from this'"
> — Bernie Meyerson, IBM CTO (2003)

In October 2001, [[us_technology_transfer_concerns_with_tsmc | TSMC]] became the first to ship 130 nanometer chips with both copper interconnects and low-K dielectric <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>. They also offered an alternate FSG dielectric version for customers like Nvidia <a class="yt-timestamp" data-t="00:32:16">[00:32:16]</a>. Yields for products like Nvidia's NV30 initially were low but reached over 70% by late 2002 <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>. By late 2001, UMC conceded defeat, abandoning SiLK for a CVD process <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>. IBM eventually switched to CVD as well <a class="yt-timestamp" data-t="00:32:55">[00:32:55]</a>. IBM Micro's failure to capitalize on its initial breakthrough ultimately proved costly <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a>.

## Conclusion
[[us_technology_transfer_concerns_with_tsmc | TSMC]]'s successful 130-nanometer node distinguished it from competitors <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. Their R&D team, "the Six R&D Horsemen," received the 2003 Outstanding Scientific and Technological Worker Award from the Taiwanese government <a class="yt-timestamp" data-t="00:34:10">[00:34:10]</a>. This achievement transformed [[us_technology_transfer_concerns_with_tsmc | TSMC]]'s reputation from a mere factory to a formidable innovator in the industry <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.