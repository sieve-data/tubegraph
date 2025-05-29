---
title: History and evolution of Field Programmable Gate Arrays FPGA
videoId: m-8G1Yixb34
---

From: [[asianometry]] <br/> 

A Field Programmable Gate Array (FPGA) is an integrated circuit designed to be reprogrammed after manufacture to emulate a digital circuit <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. FPGAs are valuable for prototyping new functionalities before mass production or for serving niche use cases that wouldn't be economical for a custom chip <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While not the first to offer this capability, FPGAs are the most commercially successful reprogrammable chips <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Early Challenges in Prototyping Digital Circuits

Before the advent of FPGAs, engineers had limited options for prototyping and testing logic functions on hardware:
*   **TTL Chips**: Transistor-transistor logic chips could be plugged into a printed circuit board <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. However, this approach was limited by board size and power consumption <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Custom Chips (ASICs)**: Getting a chip built to order, known today as an [[differences_between_fpga_pal_pla_and_asic | Application-Specific Integrated Circuit (ASIC)]], involved substantial upfront costs for a photo mask and months of fabrication time <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Mistakes in the design meant re-doing the entire costly and time-consuming process <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This path was only economically viable for very large-scale use cases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

As integrated circuits became more widely adopted after the 1960s, the need for field programmability grew more compelling <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Evolution of Programmable Logic Devices

### Programmable Read-Only Memories (PROMs)

The first integrated circuits capable of implementing a programmable logic function were Programmable Read-Only Memories (PROMs) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. In 1970, Harris Semiconductor introduced PROMs that could be programmed to implement an array of programmable logic gates, specifically an AND set and an OR set <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

These devices targeted "combinational logic," where outputs depend purely on current inputs <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>, unlike "sequential logic" which requires memory of previous states <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Any combinational logic function can be expressed using AND and OR gates <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

Harris's PROM product had fixed AND gates and programmable OR gates <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Programming involved burning fusible metal links made of nichrome, making them one-time use only <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Harris did pioneering work in fabricating these burnable fuses <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. However, using PROMs for programmable logic was inefficient due to unnecessary memory cells <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Programmable Logic Arrays (PLAs)

In 1975, Signetics (later part of NXP Semiconductors) introduced the Programmable Logic Array (PLA) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. The PLA improved upon PROMs by making *both* the AND set and OR set of logic gates programmable <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This allowed for implementing a wider range of logic functions <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, but at a significant cost due to a larger chip size <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. A PLA part cost about $25 in 1975, equivalent to about $140 USD today <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. Errors were still costly as programming involved burning fuse connections <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Despite their advantages, PLAs did not gain significant market traction <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Programmable Array Logic (PALs)

In 1977, John Birkner and H.D. Chua of Monolithic Memories modified the PLA to create the Programmable Array Logic (PAL) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The PLA had been "too configurable," making it difficult to use <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. The PAL traded some configurability for better performance and cost <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. It kept the programmable AND set but made the OR set of logic gates fixed <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

A crucial modification in PAL design was the inclusion of sequential logic circuits through macro cells <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Practical computer circuits use a mix of combinational and sequential logic <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. PAL designers added sequential logic devices like flip-flops, which can store a single bit of information <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This made PALs more practical for everyday consumer usage <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

By the early 1980s, new technologies emerged allowing these circuits to be reprogrammable, for instance, using ultraviolet light through a window to erase them, eliminating the need for fuses <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. These small field programmable devices (PLAs, PALs, etc.) were categorized as Simple Programmable Logic Devices (SPLDs) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. PALs achieved some success and were widely produced, often by memory makers who found them similar enough to their core products <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

### Altera and Complex Programmable Logic Devices (CPLDs)

In 1980, engineers from Intel, Signetics, and Intersil founded Source 3, a design consulting company specializing in helping companies work with silicon suppliers <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Their experience with [[differences_between_fpga_pal_pla_and_asic | ASIC]] chip makers led them to pursue their own field programmable hardware <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. They raised $750,000 from a VC and founded Altera, releasing their first product, the EP300, in July 1984 <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. This SPLD was made with a CMOS EEPROM process, making it erasable and reprogrammable <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

The fundamental problem with the PAL architecture was its inability to scale with [[impact_of_moores_law_on_fpga_growth_and_capabilities | Moore's Law]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Simply growing the AND set of gates didn't yield proportionally better performance; it became too large and slowed down <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. To address this, Altera pioneered the Complex Programmable Logic Device (CPLD) <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. CPLDs took a collection of smaller PALs and connected them with crossbar connections, making them much more scalable <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Altera's choice to use CMOS technology was also significant, requiring them to go to Ricoh in Japan as CMOS was not readily available in the US at the time <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Altera's success heralded the beginning of the fabless design model that now drives the American semiconductor industry <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## The Birth of the FPGA

In the mid-1980s, Ross Freeman, an engineer at Zilog, envisioned a future where [[impact_of_moores_law_on_fpga_growth_and_capabilities | Moore's Law]] would make transistors so cheap that it would be possible to create a single piece of silicon to meet everyone's needs <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. He recruited Zilog co-workers and founded Xilinx in February 1984 <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

Xilinx leveraged a connection with Seiko Corporation, the digital watchmaker, to produce their new chip, pitching it as a way to keep Seiko's fabs busy and offering exclusive resale rights in Japan <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Bill Carter, a young designer, was hired to design the product with only Ross Freeman's patent application as guidance <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Carter also had to learn Seiko's CMOS 2.5-micrometer process on the fly while communicating with a Japanese-speaking fab <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This chip was going to be very large, straining Seiko's capabilities and raising concerns about yield <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Despite being told to create something simple, what they produced was elegant in its simplicity: the Xilinx XC2064, the first FPGA <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Key Innovations of the FPGA Architecture

The core problem with the PAL's architecture was that its AND set of gates became slower as it got bigger, because the number of transistors grew much faster than the number of inputs and outputs <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. The FPGA's solution was to remove the AND set of gates entirely <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

Instead, the FPGA introduced:
*   An array of **configurable logic blocks (CLBs)** connected by programmable switches <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   Device inputs and outputs placed all around the device <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   Inside each CLB, a pair of **lookup tables** (LUTs), which are essentially arrays of outputs mapped to inputs <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. LUTs enable the FPGA to implement arbitrary logic functions <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
*   The function result could be routed to other logics like flip-flops <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
*   **Programmable interconnects** between logic blocks, allowing arbitrary paths so one block's output could become another's input <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

Early Xilinx FPGAs required external memory to store programming when power was off <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. A few years later, Actel invented anti-fuse technology to address this <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This architecture was a radical departure from PROMs, PLAs, and PALs, which had a "family resemblance" to memory chips <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

The XC2064 was a large chip for its time, with approximately 85,000 transistors arranged into 64 configurable logic blocks and 58 input/output blocks, translating to less than a thousand gates <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. Its sheer size strained Seiko's manufacturing ability <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. From the first batch of 25 wafers, only one (the 11th) worked, allowing Carter to successfully program an inverter, marking the first functional FPGA <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

## Early Challenges and FPGA's Rise to Viability

Initially, the FPGA faced significant disadvantages compared to PAL devices:
*   **Higher Cost**: The first FPGAs cost hundreds of dollars due to their large die size and extremely low yields, whereas PALs were much cheaper <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. PALs were cheaper partly because their memory-like structure allowed memory makers to easily add them to their product lines <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   **Difficulty of Use**: The novelty of FPGAs made them harder to use <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Xilinx introduced its own Electronic Design Automation (EDA) software, which was complicated and hard to use, and FPGA performance was difficult to predict <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. In contrast, PALs had simpler EDA software widely available from third parties <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

Despite these [[early_challenges_and_developments_in_fpga_technology | early challenges and disadvantages]], the FPGA eventually thrived due to a fortuitous intersection of technology and business opportunities <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

### Factors Driving FPGA Success

1.  **[[impact_of_moores_law_on_fpga_growth_and_capabilities | Moore's Law]] and Classical Scaling**: Maturing lithography technologies allowed for incredible speeds in classical scaling <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. FPGAs, with their inherently scalable architecture, were able to benefit dramatically as transistor costs plummeted, unlike PALs which could not scale effectively <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
2.  **Chemical Mechanical Polishing (CMP)**: This new process significantly lowered the costs of making the complex interconnects necessary for FPGAs <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. This allowed FPGAs to exponentially grow their lookup table counts and interconnect wire lengths <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
3.  **Rise of Independent Foundries**: The early 1990s saw the emergence of independent foundries <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. Altera and Xilinx were pioneers in the fabless startup model, allowing design teams to focus on innovation without needing to own manufacturing facilities <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. Foundries, in turn, found that large-die FPGAs were excellent for honing and mastering their processes <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. This period saw a blossoming of new FPGA startups, many of whose optimizations and features were later absorbed by Xilinx and Altera <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
4.  **Control over EDA Software**: While PAL manufacturers relied on third-party EDA vendors, which led to a race to the bottom as all PALs became similar <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>, FPGA companies like Xilinx and Altera controlled their own EDA <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. This allowed them to dictate their future, craft software to enable more features, and add automation for increased productivity <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

## Industry Consolidation and Modern Applications

Xilinx and Altera continued to hold the majority share of the multi-billion dollar FPGA industry <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. However, these two companies are no longer independent <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. [[industry_shifts_and_acquisitions_in_the_fpga_market | Intel]] acquired Altera in 2015 for about $16.7 billion <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>, and [[industry_shifts_and_acquisitions_in_the_fpga_market | AMD]] acquired Xilinx for an estimated $50 billion, with the deal closing in 2022 <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.

Today, FPGAs are widely used across various industries <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. As [[differences_between_fpga_pal_pla_and_asic | ASICs]] become increasingly expensive to design and fabricate, FPGAs have filled a valuable market gap, particularly in aerospace, military, and telecom <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. They continue to gain new functionalities and expand into areas like [[evolution_of_ai_hardware_and_gpus | AI processing]] and data centers <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. The FPGA's "Swiss Army knife" functionality and success stand as a unique Silicon Valley story, reflecting the industry's innovative power <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.