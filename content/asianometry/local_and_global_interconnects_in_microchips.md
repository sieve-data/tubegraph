---
title: Local and global interconnects in microchips
videoId: XHrQ-Pmvwao
---

From: [[asianometry]] <br/> 

Interconnects serve as the crucial "roads and sidewalks" of an integrated circuit (IC), transmitting electrical signals between billions of transistors and other circuit elements <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Without them, transistors are useless <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Metallization
The process of laying down these metal interconnects is known as "metallization" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This is a "back end of the line" process, performed after the transistors have been created on the silicon wafer in the "front end of the line" <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

During metallization, layers of fine metal wiring, called "metal layers," are deposited on top of the transistors <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These metal layers are separated by insulating dielectric material layers, technically termed "intermetal dielectric layers" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Holes, known as "vias," are cut into these dielectric layers to connect multiple metal layers <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Modern advanced ICs are complex, multi-layered structures, intricately interconnected <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## [[RC delay and its impact on chip performance | RC Delay]]
A significant challenge for interconnects is [[RC delay and its impact on chip performance | RC delay]], which stands for resistance-capacitance <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Resistance**: All wires possess resistance, which impedes electron flow, degrades signals, and leads to energy loss <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. A wire's resistance depends on its material and is proportional to its length; thicker, shorter, and wider wires have less resistance <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Capacitance**: Wires store charge due to their close proximity and the insulating dielectric layers between them, mimicking a capacitor <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This unwanted capacitance slows down the interconnect's ability to carry signals <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

[[RC delay and its impact on chip performance | RC delay]] is the extra time an electric signal takes to travel through an interconnect <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The longer the [[RC delay and its impact on chip performance | RC delay]], the slower signals propagate across the chip <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Initially, [[RC delay and its impact on chip performance | RC delay]] was less significant than device delays, but as chips grew more complex, it became a major factor in chip speed <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. By the mid-1990s, it was clear that existing methods could not sustain progress <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

## Types of Interconnects
A single microchip contains several types of interconnects:

### Local Interconnects
These are the lowest layers of metal wires, connecting local blocks of adjacent circuit elements, much like small roads <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. They are typically thinner and placed closer together <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Being close to the transistor layer, they need to be more heat-resistant <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Common materials for local interconnects include poly-silicon, tungsten, or aluminium <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Global Interconnects
Located higher up on the chip, these are larger, longer connections that span significant portions of the chip, akin to city avenues or highways <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. They also deliver vital signals such as clock synchronization and power <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. To cover large distances with minimal resistance, global interconnects are made as thick as possible and use low-resistivity metals <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

Medium-distance metal layers, sometimes called semi-global or intermodule interconnects, exist between global and local layers <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

## Logic versus Memory Chips
Logic chips tend to have more metal layers (sometimes 10-15) than memory chips (perhaps 3-5) <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. This is because memory chips have a repetitive, dense structure requiring fewer interconnects, and their bumpy structure (e.g., trench capacitors) can make additional layers challenging <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Logic chips are more irregular with lower device density, necessitating more interconnects for proper connection <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Historical Materials: Aluminium and Silicon Dioxide
For over 30 years, interconnects were primarily made from aluminium, with silicon dioxide serving as the insulating intermetal dielectric layer <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Ease of Manufacturing**: Both materials were easy to work with <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Silicon dioxide could be laid down thickly using chemical vapor deposition (CVD) <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Aluminium, the fourth lowest in resistance (after silver, copper, and gold), worked well with silicon dioxide <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Traditional Process**: A layer of silicon dioxide was laid, followed by a thick layer of aluminium <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Lithography transferred the pattern, and unwanted aluminium was etched away <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. For subsequent layers, another intermetal dielectric layer was deposited and polished <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   **Protective Alumina**: When aluminium was laid on silicon dioxide, they reacted to form aluminium oxide (alumina), which acted as a protective sheath, preventing aluminium atoms from diffusing into the silicon dioxide <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This process worked well for decades <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## The Problem of Getting Denser
As chips became denser with smaller, more numerous transistors, the interconnect system had to scale <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Shrinking Interconnects**: Shrinking interconnect size, such as pitch (distance between parallel wires), increased electrical resistance, leading to more [[RC delay and its impact on chip performance | RC delay]] <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   **Taller Wires**: Engineers tried making wires relatively taller, but this created difficult step-like structures for manufacturing, hindering coating and etching processes <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Increased Capacitance**: Denser wire clusters led to more unwanted capacitance, further increasing [[RC delay and its impact on chip performance | RC delay]] <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **More Metal Layers**: Adding more metal layers introduced process challenges, increasing the chances of errors and negatively impacting manufacturing yield and economic viability <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

By the mid-1990s, with interconnect pitches on global layers reaching 1.8 micrometers, it became evident that the delay from interconnects would soon far exceed that of transistors, necessitating a fundamental change <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

## The Solution: [[copper_lowk_interconnect_transition | Copper & Low-K]]
To combat the growing [[RC delay and its impact on chip performance | RC delay]], scientists decided to replace the interconnect system's materials <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

### Copper Interconnects
Aluminium interconnects were replaced with copper <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. Copper lines have 35% less resistance than aluminium counterparts <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

IBM publicly announced their successful production of copper interconnects in September 1997, after 15 years of secret development <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. They aimed for mass production by early 1998 <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

However, copper presented significant manufacturing challenges:
*   **Copper Poisoning**: Copper atoms can diffuse into silicon or silicon dioxide, accumulating and degrading chip performance, a phenomenon called "copper poisoning" <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   **Diffusion Barrier**: To prevent this, a "diffusion barrier" (usually made from tantalum) must be produced to block copper from entering the silicon <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. This barrier needs specific properties: adherence to copper and low-K layers, corrosion resistance, and ease of uniform deposition <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Inability to Etch**: Unlike aluminium, copper cannot be easily etched <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

#### Damascene Method
Due to copper's etching difficulties, the industry adopted the "damascene" method, reversing the traditional sequence <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
1.  Lay down the intermetal dielectric layer <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
2.  Use lithography to transfer interconnect patterns (trenches and vias) onto the dielectric <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
3.  Etch the pattern into the dielectric layer <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.
4.  Apply the diffusion barrier (e.g., tantalum) <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
5.  Fill the trenches with copper, typically using electroplating for "super-filling" or "bottoms-up growth" to avoid defects <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
6.  Sand off excess copper and apply a capping layer to prevent diffusion <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

IBM invented the damascene method around 1985 and refined it, developing a "dual damascene" methodology by 1995 that produced both trenches and vias simultaneously <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

Bringing copper to the fab also required isolating copper tools to prevent contamination and installing new waste disposal technologies due to copper's toxicity in water <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.

### Low-K Dielectrics
The second part of the solution was to replace silicon dioxide with a "low-K dielectric" material that stores less charge, thereby cutting unwanted capacitance <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. The "dielectric constant" or "k-value" measures a substance's ability to store charge; a low-K material has a k-value lower than silicon dioxide's 3.9 <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

Together, copper and low-K solutions could potentially cut [[RC delay and its impact on chip performance | RC delay]] by a factor of four, allowing for fewer metal layers and thinner wires <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

#### The Low-K Problem
Unlike copper, finding a suitable low-K material was difficult, as materials often failed reliability metrics or process flow integration <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>. It was not just a materials engineering problem but a question of what to engineer <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>.

The industry attempted low-K integration at several nodes:
*   **250 nm node**: Fluorinated Silicon Glass (FSG), a doped silicon dioxide, was used with a slightly lower K-value of 3.5 via CVD <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
*   **180 nm node**: Hydrogen Silsesquioxane (HSQ) with a lower K-value of 2.8 was attempted using a "spin-on" technique <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>. However, it failed in high-volume production due to distortion under high fab temperatures <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>. This caused major setbacks for companies like TSMC and Texas Instruments <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>.
*   **130 nm node**: This node was expected to complete the [[copper_lowk_interconnect_transition | copper/Low-K interconnect transition]] <a class="yt-timestamp" data-t="00:29:48">[00:29:48]</a>.
    *   IBM, UMC, and Infineon adopted Dow Chemical's proprietary SiLK (K-value 2.6-2.2) via spin-on <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>.
    *   Texas Instruments and TSMC favored Applied Materials' "Black Diamond" (K-value 2.8), which required CVD <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>. TSMC's Dr. Chiang personally swore off spin-on techniques <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>.
    *   Intel initially stuck with the older FSG technique due to its massive capacity needs <a class="yt-timestamp" data-t="00:31:44">[00:31:44]</a>.

Ultimately, the SiLK + spin-on setup failed in production, leading to product delays for IBM and UMC's customers <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>. TSMC became the first to ship 130 nm chips with both copper interconnects and a Low-K dielectric in October 2001, offering an alternate FSG version to ensure customer supply <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>. UMC and IBM later switched to CVD-based low-K processes <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>.

## Industry Impact and Evolution
The industry rapidly caught up on copper interconnect technology after IBM's announcement <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>. Motorola announced their copper interconnects just two weeks after IBM <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. Companies like Motorola, AMD, and AT&T began their copper work earlier, sensing IBM's progress <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. Intel, despite early research, did not implement copper until the 130 nm node in November 2000, due to being late to copper and needing to scale manufacturing for massive quantities <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.

The 180 nm node (ramping up in 1999) was a major transition point, involving not just copper interconnects but also a 30% feature size reduction (Moore's Law) and the introduction of new 193 nm DUV excimer laser lithography tools <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. The planned 300 mm wafer transition was pushed to the 130 nm node due to these complexities <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

IBM kicked off the 180 nm generation in 1998 with the PowerPC 750CX, seeing speed increases due to copper interconnects <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>. Motorola's 220 nm node in late 1998 produced PowerPC G4 chips with copper <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. Each manufacturer had their own variant of the 180 nm generation, picking and choosing specifications <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>.

Asian foundries like TSMC and UMC, starting further behind, rapidly learned copper technology <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>. UMC joined an IBM-sponsored research consortium, benefiting from IBM's patents <a class="yt-timestamp" data-t="00:25:18">[00:25:18]</a>. TSMC, under Morris Chang and Dr. Chiang Shang-yi, opted to go it alone, developing their own copper interconnect implementation with a team of six scientists <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. By 1999, both TSMC and UMC were shipping 180 nm chips with the top two metal layers made from copper <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>.

TSMC's successful [[7nanometer chip production and technological significance | 130-nanometer]] node, which completed the copper and Low-K transition, was monumental <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. This achievement, for which their R&D team was recognized, transformed TSMC's perception from a simple factory to a formidable innovator in the semiconductor industry <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.