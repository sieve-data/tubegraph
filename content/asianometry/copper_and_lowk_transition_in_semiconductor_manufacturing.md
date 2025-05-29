---
title: Copper and LowK transition in semiconductor manufacturing
videoId: XHrQ-Pmvwao
---

From: [[asianometry]] <br/> 
Interconnects are wires that transmit electrical signals between transistors and other circuit elements within an integrated circuit (IC) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. They are crucial because even a billion transistors on an IC are useless if they cannot be connected <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

For over 30 years, interconnects and their insulating layers were primarily made from aluminium and silicon dioxide, respectively <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. However, by the late 1990s, new materials became technically necessary <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This shift, the transition to copper/Low-K interconnects, was one of the [[technological_advancements_in_semiconductor_manufacturing | semiconductor industry's major transitions]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Metallization
The process of laying down these metal interconnects is called "metallization" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. It is a "back end of the line" (BEOL) process, performed after the transistors (the "front end of the line") are created on the silicon wafer <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

During metallization, layers of fine metal wiring, known as "metal layers," are placed on top of the transistors <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. These metal layers are separated by insulating dielectric material layers, technically termed "intermetal dielectric layers" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Holes, called "vias," are cut into the intermetal dielectric layers to connect multiple metal layers <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Modern advanced ICs are not flat but are complex, intricately interconnected multi-layered structures, similar to Hong Kong's old Kowloon Walled City <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## RC Delay
A critical issue in interconnect performance is RC delay, which stands for resistance-capacitance <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Resistance:** All wires have resistance, which impedes electron flow, degrading the signal and losing energy <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Resistance is proportional to wire length and depends on the material; thicker, shorter, and wider wires have less resistance <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Capacitance:** This refers to an object's ability to store charge <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Because wires are physically close with insulating dielectric layers between them, the setup mimics a capacitor, storing unwanted charge <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Higher capacitance slows down signal propagation <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

RC delay is the extra time an electric signal takes to travel through an interconnect <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. A longer RC delay means signals propagate slower throughout the chip <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. An analogy is filling a bucket of water: resistance is how fast water goes in, capacitance is the bucket's size, and RC delay is the time it takes to fill <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Types of Interconnects
A microchip contains several types of interconnects:
*   **Local Interconnects:** These are the lowest layers of metal wires, connecting adjacent elements, akin to small neighborhood roads <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. They are thinner and closer together <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Common materials include poly-silicon, tungsten, or aluminium <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Global Interconnects:** Located higher on the chip, these are larger, longer connections spanning significant chip portions, like city avenues or highways <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. They also deliver clock signals and power <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. To minimize resistance over long distances, they are made as thick as possible using low-resistivity metals <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Medium-Distance Interconnects:** Layers between global and local, with names like semi-global or intermodule interconnects <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

## Logic versus Memory
Logic chips typically have more metal layers (sometimes 10-15) than memory chips (3-5 layers) <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. Memory chips have a repetitive, dense structure requiring fewer interconnects <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a> and can have bumpy structures like trench capacitors <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Logic chips are more irregular with less device density, but require more interconnects for proper connections <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Historical Materials: Aluminium and Silicon Dioxide
Initially, silicon dioxide was used for the intermetal dielectric layer and aluminium for interconnects, especially global ones <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Both materials were easy to work with in manufacturing <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Silicon dioxide could be easily laid down using chemical vapor deposition (CVD) <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Aluminium has the fourth lowest resistance (after silver, copper, and gold) <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a> and worked well with silicon dioxide <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

The traditional manufacturing process involved depositing a thick layer of aluminium on silicon dioxide, then using lithography to pattern it, and finally etching away unwanted parts <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Subsequent layers involved depositing another intermetal dielectric layer and polishing it flat <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. A key benefit was that aluminium reacted with silicon dioxide to create a protective alumina layer, preventing aluminium atom diffusion <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This process was effective for the first 30 years of semiconductor technology <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## The Need for Change: Getting Denser
As chips became denser, with smaller transistors and more interconnects, the traditional scaling methods faced [[challenges_in_semiconductor_manufacturing | challenges]] <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Shrinking Interconnects:** Reducing interconnect size (e.g., pitch) increased electrical resistance, leading to more RC delay and slower chips <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   **Taller Wires:** Making wires relatively taller was a response, but this created a step-like structure difficult to manufacture, especially at nanometer scales <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Increased Capacitance:** Denser wires led to more unwanted capacitance, increasing RC delay <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **More Metal Layers:** Adding more metal layers increased the complexity of the manufacturing process, leading to more chances for errors, worse yields, and reduced economic viability <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### The Big Problem
Initially, RC delay was less significant than delays from circuit devices <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. However, as chips grew more complicated, RC delay became a major factor in chip speed <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. By the mid-1990s, it was clear that progress could not continue with the existing materials <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. For example, interconnect pitches significantly shrank <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. The 250-nanometer node (1996) used aluminium, but projections for the 100-nanometer node showed that transmitting a signal through a 1-millimeter interconnect would take six times longer than through an equivalent transistor <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## The Solution: Copper & Low-K
To address the RC delay issue, scientists opted to replace the interconnect system's materials <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>:
1.  **Copper for Interconnects:** Replacing aluminium with copper was an obvious choice, as copper lines have 35% less resistance <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
2.  **Low-K Dielectric for Insulation:** To reduce unwanted capacitance, the insulating dielectric layer material was changed from silicon dioxide to a "low-K dielectric" <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. This new material needed a dielectric constant (k-value) lower than silicon dioxide's 3.9 <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

Together, a copper and low-K solution could potentially cut RC delay time by a factor of four, allowing for fewer metal layers and thinner wires <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

### IBM's Big Announcement
In September 1997, IBM surprised the semiconductor world by announcing their successful production of copper interconnects, a project code-named "red aluminium" they had worked on for 15 years <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. The achievement, which involved a dedicated team working tirelessly, culminated in an iconic image of six layers of copper interconnects <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. IBM planned mass production by early 1998, with the first chips for Apple Computer's Power Macs <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

### Copper Problems
IBM's announcement was significant because copper presented serious manufacturing [[challenges_in_semiconductor_manufacturing | challenges]] <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>:
*   **Copper Poisoning:** Copper atoms can rapidly diffuse into silicon or silicon dioxide, accumulating and degrading chip performance, leading to "copper poisoning" <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. This necessitates a "diffusion barrier" (often made from tantalum) to block copper from entering the silicon <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   **Inability to Etch:** Unlike aluminium, copper does not have a suitable etchant <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. This meant the traditional deposit-and-etch method could not be used <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

### Damascene Method
To overcome the etching problem, IBM reversed the traditional sequence, adopting the "damascene" method <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. Named after an ancient metal inlay technique from Damascus <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>, this complex process involves:
1.  Laying down the intermetal dielectric layer <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
2.  Using lithography to transfer interconnect patterns (trenches and vias) onto the dielectric <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
3.  Etching the pattern into the dielectric layer <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.
4.  Applying a diffusion barrier (e.g., tantalum) <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
5.  Filling the trench with copper, often using electroplating for "super-filling" or "bottoms-up growth" <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
6.  Sanding off excess copper and applying a capping layer to prevent diffusion <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

### The Copper Road
IBM's breakthrough was built on cumulative [[technological_advancements_in_semiconductor_manufacturing | technological advancements]] <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>:
*   **Diffusion Barriers:** Research on tantalum and tantalum nitride as good diffusion barriers began in the late 1980s <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.
*   **Damascene Method:** IBM invented this method around 1985 <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.
*   **Electroplating/Super-filling:** The concept of "super-filling" or "bottoms-up growth" using electroplating to fill trenches without defects was discovered by a small IBM group in 1989 <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.
*   **Multi-level Copper Wires:** By 1993, an IBM team combined diffusion barriers, damascene, and electroplating to produce multi-level copper wires <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **Dual Damascene:** This method, re-engineered by Dan Edelstein's IBM team, produced both trenches and vias simultaneously, passing internal requirements in 1995 and leading to high-volume production commitment <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

### Bringing it to the Fab
Implementing copper in a high-volume manufacturing environment presented further [[challenges_in_semiconductor_manufacturing | challenges]] <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>:
*   **Contamination Control:** Due to copper's ability to poison silicon, tools on copper lines (lithography, metrology) had to be isolated from the rest of the fab, a difficult task in facilities that share tools <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.
*   **Waste Disposal:** Copper easily dissolves in water and is toxic, requiring new waste disposal technologies <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

### Rumblings and Rapid Catch-up
Despite IBM's secrecy, other companies rapidly caught up <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>. The industry realized the deficiencies of aluminium by 1989, and copper was an obvious alternative <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a>. Hints from IBM's publications and changes in PowerPC design rules tipped off competitors <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.
*   Motorola started copper work in 1990 <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.
*   AMD began in 1995 <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
*   AT&T (Bell Labs) developed their copper interconnect stack independently <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
*   Intel, surprisingly, didn't start their copper program until 1997, despite their researchers publishing on copper electroplating in 1989 <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.

Research was accelerated through consortia like Sematech, which coordinated public-private partnerships and directed R&D funds to universities, making findings public and allowing companies to hire trained grad students <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.

### The 180 Nanometers Node
The 180-nanometer node, scheduled for high-volume production in 1999, was a major inflection point <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>. It brought significant changes:
*   **Copper Interconnects:** Implementation of copper interconnects <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.
*   **Feature Size Reduction:** A 30% reduction in feature size, as per Moore's Law <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.
*   **New Lithography Tools:** Adoption of new 193-nanometer DUV excimer laser lithography tools <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
*   **300mm Wafer Delay:** The transition to 300-millimeter wafers was pushed back to the 130-nanometer node due to the existing complexities <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

In 1998, IBM launched the 180nm generation with the PowerPC 750CX, seeing chip speeds increase from 300 to 400 MHz <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>. Motorola followed, releasing a 220nm half-node in late 1998 with PowerPC G4 chips used in Apple's laptops <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

Not all companies adopted copper at the 180nm node <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>. Intel, for example, did not implement copper interconnects in their 180nm process <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>. This was due to their late start on copper and the need for a process that could scale rapidly to massive quantities (112,000 200mm wafers per month by 2000), which was constrained by the limited availability of copper tools from suppliers <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>. Intel delayed copper until their 130nm node in November 2000, and even then, only six of seven layers were copper <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>.

### TSMC and UMC
Across the Pacific, Taiwanese foundries [[comparison_of_semiconductor_manufacturing_strategies_between_companies | TSMC and UMC]] started behind their American counterparts, not seriously considering copper until 1997 <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>. UMC was rapidly catching up to TSMC in market share and capacity by the end of 1999 <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.

UMC joined an IBM-sponsored research consortium (likely Semiconductor Research Corporation) to leverage IBM's patents and collective research on copper interconnects <a class="yt-timestamp" data-t="00:25:18">[00:25:18]</a>. TSMC, under Morris Chang and Dr. Chiang Shang-yi, chose to develop its copper implementation independently, with a team of six elite scientists <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. Both approaches yielded results. By 1999, both UMC and TSMC began shipping 180nm chips to fabless customers with the top two metal layers made of copper, although this lagged behind IBM's chips, which had six of seven copper layers <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>.

## The Low-K Problem
While copper addressed increasing wire resistance, the [[challenges_in_semiconductor_manufacturing | semiconductor industry]] struggled to find a suitable low-K material for the intermetal dielectric layers to cut down unwanted capacitance <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>. The issue was not just material engineering, but knowing *what* to engineer, as materials kept falling apart or failing reliability metrics <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>.

The industry attempted low-K materials three times:
1.  **250nm node:** Fluorinated Silicon Glass (FSG), a silicon dioxide doped with fluorine, with a K-value of ~3.5 (vs. 3.9 for traditional SiO2), applied with CVD <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.
2.  **180nm node:** Hydrogen silsesquioxane (HSQ) with a lower K-value of ~2.8, applied using a "spin-on" technique <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>. Spin-on involves spinning the wafer and pouring the dielectric for an even layer <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>. HSQ failed to scale in high-volume production because the spin-on method combined with high fab temperatures stressed the HSQ layer, causing distortion <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>. TSMC and Texas Instruments faced significant production delays due to this <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>.

### The Legendary 130 Nanometer Node
The 130-nanometer node (following a minor 150nm node by TSMC), was anticipated to complete the copper interconnect transition and introduce a "true" low-K dielectric <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>.
*   **IBM's SiLK:** In April 2000, IBM announced adopting SiLK, a proprietary new low-K material from Dow Chemical, applied with the spin-on technique <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>. SiLK had a K-value of 2.6 (potentially 2.2) and was expected to meet needs until the 65nm node <a class="yt-timestamp" data-t="00:30:23">[00:30:23]</a>.
*   **Applied Materials' Black Diamond:** Texas Instruments and TSMC favored "Black Diamond" from Applied Materials, which had a K-value of ~2.8 but was applied using chemical vapor deposition (CVD) <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>. Dr. Chiang of TSMC personally swore off the spin-on technique due to past failures <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>.
*   **Intel's Choice:** Intel opted to stick with the older, second-generation FSG technique, again due to their immense capacity needs <a class="yt-timestamp" data-t="00:31:44">[00:31:44]</a>.

Ultimately, the SiLK + spin-on setup failed. IBM and UMC's customers failed to ship products with it, leading to significant financial and strategic costs <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>. Xilinx publicly announced delays in their FPGAs specifically due to SiLK <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. IBM eventually switched to CVD as well <a class="yt-timestamp" data-t="00:33:24">[00:33:24]</a>.

On October 2001, TSMC became the first to ship 130nm chips with both copper interconnects and low-K dielectric (using Black Diamond) <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>. They also offered an alternate FSG dielectric version for customers like Nvidia <a class="yt-timestamp" data-t="00:32:16">[00:32:16]</a>. Yields for products like Nvidia's NV30 started low but reached over 70% by late 2002 <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>. By the end of 2001, UMC abandoned SiLK for a Novellus Systems CVD process <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>.

## Conclusion
TSMC's successful implementation of the 130-nanometer node, especially with the appropriate low-K dielectric, distinguished the company from its competitors <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>. Their R&D team, "the Six R&D Horsemen," received the 2003 Outstanding Scientific and Technological Worker Award <a class="yt-timestamp" data-t="00:34:10">[00:34:10]</a>. This achievement transformed TSMC's image from a simple factory to a formidable force in the [[semiconductor industry | industry's]] R&D landscape <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.