---
title: RC delay and its impact on chip performance
videoId: XHrQ-Pmvwao
---

From: [[asianometry]] <br/> 

Integrated circuits (ICs) are complex systems that rely on billions of transistors. However, these transistors are useless without proper connections to transmit electrical signals between them. These connections are known as interconnects <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While building more transistors might seem like the primary goal, managing the performance of these interconnects, particularly in terms of [[local_and_global_interconnects_in_microchips | RC delay]], became a critical challenge in the semiconductor industry <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

## Metallization: Building the Interconnects

The process of laying down these metal interconnects is called "metallization" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. It is a "back end of the line" (BEOL) process, performed after the transistors have been created on the silicon wafer in the "front end of the line" (FEOL) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

On top of the etched transistor circuitry, layers of fine metal wiring, known as "metal layers," are deposited <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These metal layers are separated by insulating dielectric materials, technically called "intermetal dielectric layers" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. To connect multiple metal layers, holes called "vias" are cut into these dielectric layers <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Modern advanced ICs are not flat, simple landscapes but rather intricate, multi-layered structures, resembling a "Kowloon Walled City" due to their jumbled and interconnected nature <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## Understanding RC Delay

A significant challenge for interconnects is [[local_and_global_interconnects_in_microchips | RC delay]], which stands for resistance-capacitance <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

*   **Resistance (R)**: All wires have resistance, which impedes the flow of electrons, degrades the signal, and loses energy <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. A wire's resistance depends on its material and is proportional to its length; thus, thicker, shorter, and wider wires have less resistance <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Capacitance (C)**: This refers to objects' ability to store charge <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Because interconnect wires are physically close to each other and separated by insulating dielectric layers, they mimic a capacitor, storing unwanted charge <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This unwanted capacitance slows down the interconnect's ability to carry signals <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

RC delay is the extra time an electrical signal takes to travel through an interconnect <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The longer the RC delay, the slower signals propagate throughout the chip <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. An analogy for RC delay is filling a bucket of water: resistance is how fast water can be poured, and capacitance is the bucket's size; the time to fill the bucket is the RC delay <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Types of Interconnects on a Microchip

A single microchip features different types of interconnects:

*   **Local Interconnects**: These are the lowest layers of metal wires, placed directly on top of transistors <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. They connect adjacent "blocks" of elements, like small roads in a neighborhood <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. They can be thinner and closer due to shorter distances but need to be more heat-resistant due to their proximity to transistors <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Common materials include poly-silicon, tungsten, or aluminium <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Global Interconnects**: Located higher up on the chip, these are larger, longer connections that span significant portions of the chip, akin to city avenues or highways <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. They also deliver critical signals like clock signals for synchronization and power <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. To cover long distances with minimal resistance, they are made as thick as possible and use low-resistivity metals <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Medium-Distance Interconnects**: Layers between global and local interconnects, with names like semi-global or intermodule interconnects <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Logic vs. Memory Chips

Logic chips generally have more metal layers (sometimes 10-15) than memory chips (3-5) <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. This is because memory has a repetitive, dense structure requiring fewer interconnects, and it can have bumpy structures like trench capacitors <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Logic chips are more irregular and require more interconnects for proper connection, despite having less device density <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## The Evolution of Materials: Aluminium & Silicon Dioxide

For over 30 years, interconnects were made from aluminium, and their insulating layers from silicon dioxide <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. These materials were favored due to their ease of manufacturing <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Silicon dioxide could be easily laid down using chemical vapor deposition (CVD) <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Aluminium, with the fourth lowest resistance behind silver, copper, and gold, also worked well with silicon dioxide <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

The traditional process involved depositing a thick layer of aluminium on silicon dioxide, using lithography to transfer the pattern, and then etching away unwanted parts <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. A protective alumina layer formed when aluminium reacted with silicon dioxide, preventing aluminium atoms from diffusing into the dielectric <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This system worked well for the first three decades of semiconductor technology <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## The Problem of Denser Chips and Increasing RC Delay

As chips became denser with smaller transistors and more interconnects, semiconductor designers scaled the interconnect system in two ways:
1.  **Shrinking Interconnect Size**: Reducing the pitch (distance between parallel wires) increased electrical resistance, leading to more RC delay <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
2.  **Making Wires Taller**: This was a response to increased resistance, but it created a difficult-to-manufacture step-like structure <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

Denser wires also led to more unwanted capacitance, further increasing RC delay <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. While adding more metal layers could seem like a solution, it introduced process challenges and increased chances of defects, leading to lower yields and making chips less economically viable <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

Initially, RC delay was not a major concern because it was smaller than the delays from the circuit devices themselves <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. However, by the mid-1990s, as chips grew more complicated, RC delay became a significant contributor to the chip's final speed <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. By 1994, the interconnect pitches on the highest global layers (intended to be widest) had shrunk significantly <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. Looking ahead to the 100-nanometer process node, it was projected that transmitting a signal through a 1-millimeter interconnect would take six times longer than through an equivalent-sized transistor <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. This highlighted the urgent need for new materials and processes.

## The Solution: Copper & Low-K Dielectrics

To address the growing RC delay problem, scientists proposed replacing the interconnect system's materials <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>:

1.  **Copper for Interconnects**: Replacing aluminium with copper was an obvious choice, as copper lines have 35% less resistance <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
2.  **Low-K Dielectrics**: To reduce unwanted capacitance, the insulating dielectric layer material was changed from silicon dioxide (k-value 3.9) to "low-K dielectric" materials with a lower dielectric constant (k-value), such as those with k-values around 2.8 or lower <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

Together, copper and low-K solutions could potentially cut RC delay time by a factor of four, allowing for fewer metal layers and thinner wires <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

## Challenges with Copper

Despite its advantages, copper presented serious manufacturing problems:
*   **Copper Poisoning**: Copper atoms can diffuse into silicon or silicon dioxide, accumulating and hurting chip performance—a phenomenon called "copper poisoning" <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   **Diffusion Barrier**: A "diffusion barrier," typically made from tantalum, is required to block copper from entering the silicon. This barrier must adhere to both copper and low-K insulation layers, resist corrosion, and be easily and evenly deposited <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   **Inability to Etch**: Unlike aluminium, copper cannot be easily etched using suitable etchants <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

### The Damascene Method

Because copper cannot be etched in the traditional way, a reverse sequence called the **damascene method** was developed <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. This complex "add" process involves:
1.  Laying down the intermetal dielectric layer <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
2.  Using lithography to transfer interconnect patterns (trenches and vias) onto the dielectric <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
3.  Etching the pattern into the dielectric layer <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.
4.  Applying a diffusion barrier (e.g., tantalum) <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
5.  Filling the trenches with copper, typically using electroplating <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
6.  Sanding off excess copper <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
7.  Applying a capping layer on top of the copper to prevent diffusion <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

This method, named after the Middle Eastern metal inlay techniques, is highly complex and unintuitive <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

## IBM's Breakthrough and the Copper Road

IBM's internal project, code-named "red aluminium," began in the late 1980s and early 1990s <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. Key advancements included:
*   Discovery of tantalum and tantalum nitride as effective diffusion barriers <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.
*   Invention of the damascene method around 1985 <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
*   The crucial development of "super-filling" or "bottoms-up growth" using electroplating in 1989, which allowed trenches and vias to be filled with copper without defects <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

In 1993, an IBM team successfully combined diffusion barriers, damascene, and electroplating to produce multi-level copper wires <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. Although initial methods were not economically viable due to throughput and yield issues, a re-engineered "dual damascene" method by Dan Edelstein in 1995 allowed for simultaneous production of trenches and vias, meeting IBM's internal requirements <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

In September 1997, IBM shocked the semiconductor world by announcing its successful production of copper interconnects, showcasing six layers of copper <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. They planned mass production by early 1998, with the first chips going to Apple Computer for their Power Macs <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

Bringing copper to the fab presented significant challenges, including isolating copper tools to prevent "poisoning" the rest of the fab and installing new waste disposal technologies to handle toxic copper in water <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.

### Rapid Industry Catch-up

Initially, IBM seemed years ahead of competitors <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. However, just two weeks after IBM's announcement, Motorola also declared they had produced copper interconnects <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. The industry realized the deficiencies of aluminium interconnects after 1989 and began pursuing copper, often sensing IBM's progress through published papers and subtle signs <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.

Motorola began copper work in 1990 <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>, AMD in 1995 <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>, and AT&T (Bell Labs) also around the same time, developing their stack independently <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. Surprisingly, Intel didn't start its copper program until 1997, despite its own researchers publishing on copper electroplating in 1989 <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>. Much of this rapid catch-up was facilitated by consortiums like Sematech, which coordinated public-private R&D and disseminated findings, allowing companies to hire skilled graduate students <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.

## The 180 Nanometer Node and Beyond

The 180 nanometer (0.18 micron) node, scheduled for high volume in 1999, represented a major transition <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. It combined copper interconnects, a 30% reduction in feature size (as per Moore's Law), and the introduction of new 193-nanometer DUV excimer laser lithography tools <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. The planned 300-millimeter wafer transition was pushed back to the 130-nanometer node due to these simultaneous changes <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

IBM kicked off the 180nm generation in 1998 with the PowerPC 750CX, seeing speeds increase from 300 to 400 Megahertz due to copper interconnects <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>. Motorola followed closely with a 220nm half-node in late 1998, powering Apple's PowerPC G4 chips <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

Not all manufacturers adopted copper at 180nm. Intel's 180nm process did not use copper due to their late start and massive capacity needs (112,000 200mm wafers/month by 2000), as there weren't enough copper tools available <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. Intel finally implemented copper in November 2000 with the 130nm node, and even then, only six of seven layers were copper <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.

### The Low-K Problem: A Persistent Challenge

While copper addressed resistance, finding a suitable low-K material for capacitance reduction proved more challenging because the industry struggled to find one that fit well into the process flow and met reliability metrics <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>.

Early attempts included:
*   **250nm node**: Fluorinated Silicon Glass (FSG), a doped silicon dioxide with a k-value of ~3.5, applied with CVD <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
*   **180nm node**: Hydrogen Silsesquioxane (HSQ), with a lower k-value of ~2.8, attempted using a "spin-on" technique <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>. The HSQ spin-on technique failed to scale in high-volume production due to stress from high fab temperatures, causing distortion <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>. This led to significant delays for companies like TSMC and Texas Instruments <a class="yt-timestamp" data-t="00:29:04">[00:29:04]</a>.

### The Legendary 130 Nanometer Node

The 130nm node, after a minor 150nm node, was expected to fully implement copper interconnects and a "true" low-K dielectric <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>.

*   **IBM's SiLK**: In April 2000, IBM (with UMC and Infineon) announced adopting Dow Chemical's proprietary SiLK, applied via spin-on, with a k-value of 2.6 or even 2.2, projected to last until the 65nm node <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>.
*   **Applied Materials' Black Diamond**: Other companies, like Texas Instruments and TSMC, favored Black Diamond from Applied Materials, with a k-value of 2.8, which was applied using CVD <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>. TSMC specifically chose CVD due to negative experiences with the spin-on technique <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>. Intel continued to use the older FSG technique <a class="yt-timestamp" data-t="00:31:44">[00:31:44]</a>.

Ultimately, the SiLK + spin-on setup failed to ship products for IBM and UMC's customers, leading to significant financial and strategic costs <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.

### TSMC's Triumph

In October 2001, TSMC became the first to ship 130nm chips with both copper interconnects and a low-K dielectric (Black Diamond) <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>. They also offered an alternate FSG dielectric version for customers like Nvidia <a class="yt-timestamp" data-t="00:32:16">[00:32:16]</a>. Yields for products like Nvidia's NV30 started low but reached over 70% by late 2002 <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>.

In late 2001, UMC abandoned SiLK for a Novellus Systems CVD process, suffering from their costly choice <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>. IBM eventually switched to CVD as well, facing public criticism from customers like Xilinx for delays caused by SiLK <a class="yt-timestamp" data-t="00:32:55">[00:32:55]</a>.

## Conclusion

TSMC's successful implementation of the 130-nanometer node, especially with copper and low-K dielectrics, was monumental <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. This achievement, for which their R&D team was awarded the 2003 Outstanding Scientific and Technological Worker Award, transformed TSMC's reputation from a mere factory to a recognized innovator in the semiconductor industry <a class="yt-timestamp" data-t="00:34:10">[00:34:10]</a>. The mastery of copper and low-K technologies was crucial in mitigating [[local_and_global_interconnects_in_microchips | RC delay]] and enabling continued chip performance improvements.