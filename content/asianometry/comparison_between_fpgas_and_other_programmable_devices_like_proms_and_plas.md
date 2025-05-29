---
title: Comparison between FPGAs and other programmable devices like PROMs and PLAs
videoId: m-8G1Yixb34
---

From: [[asianometry]] <br/> 

A Field-Programmable Gate Array (FPGA) is an integrated circuit that can be reprogrammed after manufacture to emulate a digital circuit <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. FPGAs are useful for prototyping new functionalities before mass production or for serving rare use cases that are not economical for a custom chip <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While not the first to offer this capability, FPGAs are the most commercially successful reprogrammable integrated circuit <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Early Programmable Logic Devices (PLDs)

Before FPGAs, prototyping and testing logic functions on hardware largely involved two options:
*   **TTL Chips**: Transistors plugged into a printed circuit board, limited by board size and power consumption <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Built-to-Order Chips (ASICs)**: Application-Specific Integrated Circuits, which involved substantial upfront costs for photo masks and months of fabrication time <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Mistakes in design were costly and irreversible <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. ASICs were only economically viable for very large use cases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

As integrated circuits became more widely adopted after the 1960s, the need for field programmability grew <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Programmable Read-Only Memories (PROMs)

The first integrated circuits capable of implementing a programmable logic function were Programmable Read-Only Memories (PROMs) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   In 1970, Harris Semiconductor introduced PROMs that could be programmed to implement an array of programmable logic gates, specifically an AND set and an OR set <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   The inputs first went into the AND set, whose outputs then fed into the OR set before being outputted <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This configuration allowed for implementing combinational (time-independent) logic functions <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   Harris's PROM product shipped with fixed AND gates and programmable OR gates <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Programming Method**: These PROMs were programmed by "burning" fusible metal links made of nichrome, making them one-time use devices <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Limitation**: Using PROMs for programmable logic was inefficient as it required more memory cells than necessary <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Programmable Logic Arrays (PLAs)

In 1975, Signetics (later part of NXP Semiconductors) introduced the Programmable Logic Array (PLA) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Key Difference**: Unlike PROMs, with the PLA, *both* the AND set and OR set of logic gates were made programmable <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Advantage**: This allowed users to implement a wider range of logic functions <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Disadvantage**: The PLA required a far larger chip, raising the overall cost. In 1975, each part cost about $25, equivalent to $140 today <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Programming still involved burning fuses, making errors costly <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Market Adoption**: Despite their advantages, PLAs never widely caught on due to their high cost and complexity <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Programmable Array Logic (PALs)

In 1977, engineers John Birkner and H.D. Tua of Monolithic Memories modified the PLA to create the Programmable Array Logic (PAL) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Design Trade-off**: The PLA was considered "too configurable" <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. The PAL traded away some configurability to gain better performance and cost <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   **Architecture**: It kept the programmable AND set but made the OR set of logic gates fixed <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Key Improvement**: The PAL design also included sequential logic circuits through the use of macro cells, such as flip-flops <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Flip-flops store a single bit of information and enable the output to depend on external items or previous states, making PALs more practical for real-world computer circuits <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Reprogrammability**: In the early 1980s, new [[technological_advancements_that_impacted_fpga_development | technologies emerged]] that allowed these circuits to be reprogrammed, for instance, by flashing ultraviolet light through a window to erase them, removing the need for fuses <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **Market Success**: PALs saw some success and were widely made. Memory makers found them similar enough to their core products to add to their repertoire <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. Monolithic Memories also made them easy for users to learn <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   These smaller, early field-programmable devices like PLAs and PALs are categorized as Simple Programmable Logic Devices (SPLDs) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## The Emergence of FPGAs

### Complex Programmable Logic Devices (CPLDs) by Altera

In 1980, engineers from Intel, Signetics, and Intersil founded a design consulting company called Source 3, which later became Altera <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Their experiences with ASIC chipmakers led them to try making their own field-programmable hardware <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **First Product**: Altera's first product, released in July 1984, was the EP300, an SPLD made with a CMOS EEPROM process, which was erasable and programmable <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Scaling Problem**: The core problem with the PAL's structure was that it didn't scale well with [[technological_advancements_that_impacted_fpga_development | Moore's Law]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. As the AND set of gates got bigger, it became slower because the number of transistors grew much faster than the number of inputs and outputs <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   **CPLD Solution**: To better leverage shrinking transistor sizes, Altera pioneered the Complex Programmable Logic Device (CPLD) <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This involved connecting a bunch of smaller PALs with crossbar connections, making them much more scalable <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   Altera's use of CMOS, which was not readily available in the US at the time, led them to Ricoh in Japan for fabrication. This success heralded the beginning of the [[market_evolution_and_emergence_of_fpga_companies | fabless design model]] <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

### Xilinx and the First FPGA

In the mid-1980s, Ross Freeman, an engineer at Zilog, envisioned making a piece of silicon that could meet everyone's needs as transistors became cheaper <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. He co-founded Xilinx in February 1984 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Fabrication Partnership**: Xilinx partnered with Seiko Corporation to produce their new chip, pitching it as a way for Seiko to keep their fabs busy <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **The XC2064**: Designed by Bill Carter under challenging conditions (limited guidance, unfamiliar CMOS 2.5 micrometer process at Seiko, communication with a Japanese-speaking fab), the Xilinx XC2064 became the first FPGA <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **FPGA Architecture vs. PALs**:
    *   The FPGA solution to PAL's scaling problem was to remove the large, slow AND set of gates altogether <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
    *   Instead, the FPGA features an array of **Configurable Logic Blocks (CLBs)** connected together with **programmable switches** <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Device inputs and outputs are placed all around the device <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
    *   Each CLB contains a pair of **lookup tables (LUTs)**, which are like arrays of outputs mapped to inputs, enabling the FPGA to implement arbitrary logic functions <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
    *   The interconnects between logic blocks are also programmable, allowing for arbitrary paths to be configured <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **Initial Programming**: Early Xilinx FPGAs required external memory to store the programming when power was off <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. A few years later, Actel invented anti-fuse [[technological_advancements_that_impacted_fpga_development | technology that helped]] with this <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Radical Change**: This architecture was a radical departure. While PALs and PLAs descended from memory chips, the FPGA looked totally different <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

## Comparison: FPGAs vs. PROMs, PLAs, and PALs

| Feature / Device | PROMs                                        | PLAs                                            | PALs (SPLDs)                                  | FPGAs                                                      |
| :--------------- | :------------------------------------------- | :---------------------------------------------- | :-------------------------------------------- | :--------------------------------------------------------- |
| **Logic Gates**  | Fixed AND, Programmable OR <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a> | Programmable AND, Programmable OR <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a> | Programmable AND, Fixed OR <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a> | Array of Configurable Logic Blocks (CLBs) with Look-Up Tables (LUTs) <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a> |
| **Programmability** | One-time (fusible links) <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a> | One-time (fusible links) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a> | Initially one-time; later reprogrammable (e.g., UV erasable) <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a> | Reprogrammable (initially external memory, later anti-fuse) <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a> |
| **Scalability**  | Poor <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>                             | Limited due to large chip size <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>   | Poor; structure didn't scale well with [[technological_advancements_that_impacted_fpga_development | Moore's Law]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a> | Excellent; designed to scale exponentially with [[technological_advancements_that_impacted_fpga_development | Moore's Law]] <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a> |
| **Sequential Logic** | No                                           | No                                              | Yes (through macro cells like flip-flops) <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a> | Yes (CLBs can incorporate flip-flops) <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a> |
| **Cost (Early)** | Moderate                                     | High <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>                           | Cheaper than PLAs; similar to memory <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a> | Very high initially due to large die and low yields <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a> |
| **Ease of Use (EDA)** | -                                            | Hard, errors costly <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>         | Easier, simple, widely available third-party EDA <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a> | Harder initially due to complex proprietary EDA <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a> |
| **Strategic Control** | -                                            | -                                               | Limited due to reliance on third-party EDA vendors <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a> | Full control over hardware and software, enabling innovation <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a> |

### FPGA Advantages and Market Evolution

Despite early challenges like higher cost and complexity, FPGAs eventually thrived <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. Several factors contributed to their success:
*   **[[technological_advancements_that_impacted_fpga_development | Moore's Law]]**: FPGAs were designed to scale effectively, benefiting greatly as transistor costs crashed and lithography technologies matured <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   **[[technological_advancements_that_impacted_fpga_development | Chemical Mechanical Polishing (CMP)]]**: This process drastically lowered the costs of making the complex interconnects required by FPGAs <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   **Rise of Independent Foundries**: The early 1990s saw the rise of independent foundries, enabling [[market_evolution_and_emergence_of_fpga_companies | fabless startup models]] like Altera and Xilinx <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. Foundries also found FPGAs useful for refining their manufacturing processes <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **EDA Software Control**: While PAL manufacturers relied on third-party EDA software, leading to commoditization <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>, FPGA companies like Xilinx and Altera controlled their own EDA <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. This allowed them to dictate their future, craft software to enable more features, and add automation for increased productivity <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.

Today, Xilinx and Altera (now part of AMD and Intel, respectively) continue to hold the majority share of the multi-billion dollar FPGA industry <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. FPGAs fill a valuable market gap as ASICs become increasingly expensive <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>, especially in the aerospace, military, and telecom spaces <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. They continue to gain new functionalities, expanding into [[applications_of_fpgas_in_various_industries | areas like AI processing and data centers]] <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.