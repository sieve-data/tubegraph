---
title: Resistancecapacitance delay and its impact on chip performance
videoId: XHrQ-Pmvwao
---

From: [[asianometry]] <br/> 

An integrated circuit (IC) requires interconnects, which are wires used to transmit electrical signals between transistors and other circuit elements <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Historically, for over 30 years, these interconnects were made from aluminium, with insulating layers of silicon dioxide <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. By the late 1990s, however, it became technically necessary to adopt new materials <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This transition, which saw the industry move to copper and low-K interconnects, represented a significant shift in semiconductor manufacturing <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Metallization

The process of laying down these metal interconnects is known as "metallization" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. As a "back end of the line" process, metallization occurs after transistors are fabricated on the silicon wafer in the "front end of the line" <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

During metallization, layers of fine metal wiring, called "metal layers," are deposited on top of the transistors <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These metal layers are separated by insulating dielectric materials, technically known as "intermetal dielectric layers" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. To connect multiple metal layers, holes called "vias" are cut into the intermetal dielectric layers <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Modern advanced ICs are described as intricate, layered structures, similar to Hong Kong's old Kowloon Walled City, rather than flat landscapes <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## RC Delay

A critical challenge in interconnect performance is "RC delay," which stands for resistance-capacitance <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Resistance
All wires possess resistance, which impedes the flow of electrons, degrading the electrical signal and leading to energy loss <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. A wire's resistance is determined by its material and is directly proportional to its length <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Consequently, thicker, shorter, and wider wires exhibit less resistance <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

### Capacitance
Capacitance refers to an object's ability to store an electrical charge <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. In integrated circuits, the close proximity of wires, separated by insulating dielectric layers, causes the entire setup to store charge, mimicking a real-life capacitor <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This unwanted capacitance slows down the interconnect's ability to carry signals <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Impact of RC Delay
RC delay is the additional time an electric signal takes to travel through an interconnect <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. A longer RC delay results in slower signal propagation across the chip <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. An analogy for RC delay is filling a bucket of water, where resistance represents the rate of water inflow and capacitance represents the bucket's size; the time to fill the bucket is the RC delay <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Types of Interconnects

A single microchip contains several types of interconnects:

### Local Interconnects
The lowest layers of metal wires, placed directly on top of the transistors, are called "local interconnects" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. These connect local "blocks" of adjacent elements, akin to small neighborhood roads <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. They can be made thinner and placed closer together as they cover shorter distances <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Due to their proximity to the transistor layer, they also require higher heat resistance <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Common materials for local interconnects include poly-silicon, tungsten, or aluminium <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Global Interconnects
Higher up on the chip are "global interconnect" layers, which are larger, longer connections spanning significant portions of the chip, comparable to city avenues or highways <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. These interconnects also deliver essential signals like clock synchronization and power <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. To cover large distances with minimal resistance, they are made as thick as possible and utilize low-resistivity metals <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

Between global and local layers, there are medium-distance metal layers known by various names such as semi-global interconnects or intermodule interconnects <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Logic versus Memory Chips
[[chip_design_process_and_techniques | Logic chips]] typically have more metal layers (sometimes 10-15) than [[chip_design_process_and_techniques | memory chips]] (perhaps 3-5) <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. This is because memory has a repetitive, dense structure requiring fewer interconnects and may feature bumpy structures like trench capacitors <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Logic chips, being more irregular with less device density, demand more interconnects to ensure proper connections <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Historical Materials: Aluminium and Silicon Dioxide

Initially, silicon dioxide was used for the intermetal dielectric layer and aluminium for the interconnects, especially global ones <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. These materials were chosen due to their ease of manufacturing <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Silicon dioxide could be easily deposited as a thick layer using chemical vapor deposition (CVD) <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Aluminium, being the fourth lowest in resistance after silver, copper, and gold, also worked well with silicon dioxide in manufacturing <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

The process involved laying down a silicon dioxide layer, then a thick aluminium layer, which was patterned using lithography, and finally, unwanted parts were etched away <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. For multiple layers, another intermetal dielectric layer was deposited and polished flat <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. The interaction between aluminium and silicon dioxide created a protective aluminium oxide (alumina) layer, preventing aluminium atoms from diffusing into the silicon dioxide <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This process worked effectively for the first 30 years of semiconductor technology <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Challenges of Denser Chips

As chips became more dense and transistors smaller, more interconnects were needed <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Semiconductor designers attempted to scale the interconnect system by shrinking their size, for instance, reducing the pitch (distance between parallel wires) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. However, this increased the electrical resistance of the wires, leading to more RC delay and slowing down the chip <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

Engineers responded by making wires relatively taller, but this step-like structure proved difficult for manufacturing, especially at nanometer scales, leading to issues with coating and etching <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. Denser clusters of wires also increased unwanted capacitance, further contributing to RC delay <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Adding more metal layers introduced process challenges, increased chances of defects, and reduced yield, making chip production less economically viable <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## The Growing Problem of RC Delay

Initially, RC delay was not a significant concern because it was smaller than delays from the circuit devices themselves <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. However, as chips became more complex, RC delay emerged as a major contributor to a chip's overall speed <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. By the mid-1990s, it was clear that the existing approach was unsustainable <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

For example, in 1978, the interconnect pitch for the second metal layer (M2) was about 20 micrometers <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. By 1994, the pitches on the widest global layers had shrunk to 1.8 micrometers <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. Although aluminium interconnect technology was pushed for one more generation (the 250 nanometer node ramping up in 1996), projections for the 100 nanometer process node showed that transmitting a signal through a 1-millimeter interconnect would take six times longer than through an equivalent-sized transistor <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## The Solution: Copper and Low-K Dielectrics

To address the RC delay issue, scientists proposed replacing the interconnect system's materials <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

1.  **Copper Interconnects:** The low-resistivity metal in the interconnects was changed from aluminium to copper <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. Copper lines offer 35% less resistance than their aluminium counterparts, making it an obvious choice <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

2.  **Low-K Dielectrics:** Unwanted capacitance could be reduced by replacing silicon dioxide in the insulating dielectric layer with a material that stores less charge <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. A substance's ability to store charge is measured by its "dielectric constant" or "k-value" <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. The new material needed a k-value lower than silicon dioxide's (3.9) and was thus called a "low-K dielectric" <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

The combination of copper and low-K dielectrics allowed manufacturers to use fewer metal layers and thinner wires, potentially reducing RC delay time by a factor of four <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

## IBM's Breakthrough and the Challenges of Copper

In September 1997, IBM announced its successful production of copper interconnects, a result of 15 years of secret development on a project code-named "red aluminium" <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. This achievement, symbolized by an image of six layers of copper interconnects, was set to be mass-produced by early 1998, with the first chips going to Apple Computer for their Power Macs <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

IBM's announcement was significant because copper presented serious manufacturing problems:
*   **Copper Poisoning:** Copper atoms can diffuse into silicon or silicon dioxide, accumulating and degrading chip performance, a phenomenon known as "copper poisoning" <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. Manufacturers had to create a "diffusion barrier," typically made from tantalum or tantalum nitride, to block copper from entering the silicon <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. This barrier needed to adhere to both copper and low-K insulation, resist corrosion, and be easily and evenly deposited <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Inability to Etch:** Unlike aluminium, copper cannot be easily etched using suitable etchants <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

### The Damascene Method
To overcome the etching problem, IBM reversed the traditional manufacturing sequence with the "damascene method" (named after ancient metal inlay techniques) <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

1.  An intermetal dielectric layer is laid down <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
2.  Lithography is used to transfer interconnect patterns (trenches and vias) onto the dielectric <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
3.  The pattern is etched into the dielectric layer <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.
4.  A diffusion barrier (e.g., tantalum compound) is applied <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
5.  The trenches are filled with copper using electroplating, an electrochemical deposition process that achieves "super-filling" or "bottoms-up growth" by filling from the bottom up, avoiding seams or voids <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
6.  Excess copper is sanded off <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
7.  A capping layer is applied to prevent copper diffusion <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

This complex and unintuitive process was critical for copper implementation <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.

## The Copper Road: Evolution and Adoption

The adoption of copper interconnects was a culmination of several advancements:
*   **Diffusion Barriers:** Research on tantalum and tantalum nitride as diffusion barriers began in the late 1980s and progressed into the early 1990s <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.
*   **Damascene Method:** IBM invented this method around 1985 <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
*   **Super-filling:** The "super-filling" or "bottoms-up growth" idea for filling trenches and vias using electroplating was discovered in 1989 <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

In 1993, an IBM team combined these elements to produce multi-level copper wires, marking the first indication that copper could replace aluminium <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. However, this initial method was not economically viable due to throughput and yield issues <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. A re-engineered "dual damascene" methodology, developed by another IBM team led by Dan Edelstein, simultaneously produced trenches and vias, passing internal requirements in 1995 and leading to the public announcement two years later <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

### Bringing it to the Fab
Implementing copper in high-volume fabrication plants (fabs) posed additional challenges for IBM's foundry, which had faced cost-cuts <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>. Due to copper's ability to "poison" silicon and cause defects, tools on copper lines needed to be isolated, a difficult task in fabs sharing tools <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>. Furthermore, copper's toxicity when dissolved in water necessitated new waste disposal technologies <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

### Industry Catch-up
Despite IBM's perceived lead, Motorola announced its own copper interconnect production just two weeks after IBM's 1997 announcement <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. While IBM was the sole company researching copper before 1989, the industry recognized aluminium's deficiencies afterward <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. Other companies, sensing IBM's work through published papers and design rule changes, began their own copper programs <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>. Motorola started in 1990 via its alliance with IBM, AMD in 1995, and AT&T (Bell Labs) around the same time, independently developing their copper stack <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. Surprisingly, Intel did not start its copper program until 1997, despite its own researchers publishing on copper electroplating in 1989 <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.

Much of this rapid catch-up was facilitated by increased public research, particularly through Sematech, an R&D consortium that coordinated public-private partnerships and funded university studies on copper technology, releasing findings into the public domain and supplying talent to semiconductor companies <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.

### The 180 Nanometer Node
The 180 nanometer node (also known as 0.18 microns), scheduled for high-volume production in 1999, was a major transition point <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. It involved:
1.  Copper interconnects <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>.
2.  A 30% reduction in feature size, following Moore's Law <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.
3.  The introduction of new 193-nanometer DUV excimer laser lithography tools <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
The 300 millimeter wafer transition, initially planned for this node, was delayed to the 130 nanometer node due to the existing complexities <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

IBM launched the 180 nanometer generation in 1998 with the PowerPC 750CX, whose copper interconnects boosted speeds from 300 to 400 MHz <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>. Motorola followed closely with a 220 nanometer node in late 1998, producing the PowerPC G4 chips for Apple's PowerBook G4 and iBook G4 laptops <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. The semiconductor manufacturing industry had more players then, each adopting their own variants of the 180 nanometer "generation" <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. Notably, Intel's 180 nanometer process did not use copper interconnects, partly due to their late start and the need to scale production rapidly for their PC CPU monopoly, which faced insufficient copper tool supply <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. Intel implemented copper interconnects only in November 2000 with the 130 nanometer node, with only six of seven layers made from copper <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.

## The Low-K Problem

While copper addressed wire resistance, the industry faced a persistent challenge in finding a suitable low-K material for the intermetal dielectric layers to reduce unwanted capacitance <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>. The problem was that materials often fell apart or failed reliability metrics, unlike copper, which was a known [[emerging_trends_and_challenges_in_chip_design | materials engineering problem]] <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>.

The industry attempted low-K dielectrics at three nodes:
1.  **250 nanometer node:** Fluorinated Silicon Glass (FSG), a fluorine-doped silicon dioxide, was used <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. FSG had a slightly lower K-value (about 3.5) than traditional silicon dioxide (3.9) and was applied via CVD <a class="yt-timestamp" data-t="00:27:43">[00:27:43]</a>.
2.  **180 nanometer node:** Hydrogen Silsesquioxane (HSQ) with a lower K-value (about 2.8) was attempted using a "spin-on" technique, where the dielectric is poured onto a rapidly spinning wafer <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>. Though it passed internal tests, HSQ failed to scale in high-volume production because the spin-on process combined with high fab temperatures caused the HSQ layer to distort <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>. This forced [[TSMC and UMC | TSMC]] and Texas Instruments to revert to FSG, causing delays <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>.

### The Legendary 130 Nanometer Node
The 130 nanometer node (following a minor 150 nanometer node by [[TSMC and UMC | TSMC]]), was expected to achieve full copper interconnects and a "true" low-K dielectric <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>.

*   **IBM, UMC, and Infineon:** In April 2000, IBM announced adopting SiLK, a proprietary low-K material from Dow Chemical, applied via the spin-on technique <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>. SiLK had a K-value of 2.6 (or possibly 2.2), projected to meet needs until the 65 nanometer node <a class="yt-timestamp" data-t="00:30:23">[00:30:23]</a>.
*   **Texas Instruments, [[TSMC and UMC | TSMC]], and Intel:** Texas Instruments favored "Black Diamond" from Applied Materials (K-value ~2.8), which required CVD, not spin-on <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>. [[TSMC and UMC | TSMC]] also chose Black Diamond, largely because Dr. Chiang Shang-yi, the VP of R&D at [[TSMC and UMC | TSMC]], vowed not to use spin-on again after the HSQ failure <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>. Intel opted to stick with the older FSG technique due to its massive capacity needs <a class="yt-timestamp" data-t="00:31:44">[00:31:44]</a>.

Ultimately, the SiLK and spin-on combination failed, with IBM and UMC's customers unable to ship products using it, incurring significant financial and strategic costs <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>.

On October 2001, [[TSMC and UMC | TSMC]] became the first to ship 130 nanometer chips with both copper interconnects and a low-K dielectric (Black Diamond), offering an alternate FSG dielectric version for customers like Nvidia <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>. Yields, initially in the teens for products like Nvidia's NV30, reached over 70% by late 2002 <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>.

In late 2001, UMC abandoned SiLK for a CVD process from Novellus Systems <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>. IBM itself switched to CVD in 2002 after a public announcement from customer Xilinx blaming SiLK for delays <a class="yt-timestamp" data-t="00:32:55">[00:32:55]</a>. Despite defending their initial SiLK choice, IBM's inability to capitalize on its breakthrough cost it dearly, leading to a loss of face <a class="yt-timestamp" data-t="00:33:24">[00:33:24]</a>.

## Conclusion

[[TSMC and UMC | TSMC]]'s successful implementation of the 130 nanometer node, with its copper interconnects and CVD-based low-K dielectric, distinguished the Taiwanese foundry from its competitors <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. Their R&D team, "the Six R&D Horsemen," received the 2003 Outstanding Scientific and Technological Worker Award <a class="yt-timestamp" data-t="00:34:10">[00:34:10]</a>. This node transformed [[TSMC and UMC | TSMC]]'s reputation from a mere factory to a recognized innovator in the semiconductor industry <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.