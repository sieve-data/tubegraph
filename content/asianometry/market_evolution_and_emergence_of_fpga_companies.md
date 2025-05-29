---
title: Market evolution and emergence of FPGA companies
videoId: m-8G1Yixb34
---

From: [[asianometry]] <br/> 

A field programmable gate array (FPGA) is an integrated circuit that can be reprogrammed after manufacture to emulate a digital circuit <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While not the first with this capability, FPGAs are the most commercially successful <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Early Programmable Logic Devices (Pre-FPGA)

For decades, engineers sought ways to create reprogrammable chips <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Before programmable chips, designers largely had two options for prototyping logic functions on hardware:
1.  **TTL Chips:** Using transistors plugged into a printed circuit board, limited by board size and power consumption <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  **Custom Built Chips (ASICs):** Substantial upfront costs, including paying for a photo mask and waiting months for fabrication, making design errors very costly <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. These are now called [[history_of_chip_design_and_evolution_of_electronic_design_automation | Application Specific Integrated Circuits]] (ASICs) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

As integrated circuits became more widely adopted after the 1960s, field programmability became a compelling need <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Programmable Read-Only Memories (PROMs)

The first integrated circuits capable of implementing a programmable logic function were [[comparison_between_fpgas_and_other_programmable_devices_like_proms_and_plas | Programmable Read-Only Memories]] (PROMs) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. In 1970, Harris Semiconductor introduced PROMs that could be programmed to implement an array of programmable logic gates, specifically an AND set and an OR set <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. These PROMs targeted combinational logic functions, where outputs depend purely on inputs <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

Harris's PROM product had fixed AND gates and programmable OR gates <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Programming was done by burning fusible metal links made of nichrome, making them one-time use only <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Harris performed pioneering work in fabricating these burnable fuses <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. However, using PROMs for programmable logic was inefficient as they didn't require all the memory cells <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Programmable Logic Arrays (PLAs)

In 1975, Signetics (later part of NXP Semiconductors) introduced the [[comparison_between_fpgas_and_other_programmable_devices_like_proms_and_plas | Programmable Logic Array]] (PLA) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. With the PLA, both the AND set and OR set of logic gates were made programmable, allowing for a wider range of logic functions <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This flexibility came at a significant cost, as PLAs required a much larger chip, costing about $25 each in 1975 ($140 USD today) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Programming still involved burning fuse connections, making errors costly <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Despite their advantages, PLAs did not widely catch on <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Programmable Array Logic (PALs)

In 1977, John Birkner and H.D. Tua of Monolithic Memories modified the PLA to create the [[comparison_between_fpgas_and_other_programmable_devices_like_proms_and_plas | Programmable Array Logic]] (PAL) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The PAL traded some configurability for better performance and cost <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. It kept the programmable AND set but made the OR set of logic gates fixed <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. PALs also included sequential logic circuits using macro cells, such as flip-flops, making them more practical for everyday use <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

By the early 1980s, new [[technological_advancements_that_impacted_fpga_development | technologies]] emerged allowing these circuits to be reprogrammed, for instance, by flashing ultraviolet light through a window to erase them, eliminating the need for fuses <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. These small field-programmable devices (PLAs, PALs) were categorized as Simple Programmable Logic Devices (SPLDs) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. PALs saw some success and were widely produced, as memory makers found them similar enough to their core products <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Emergence of Altera and Complex Programmable Logic Devices (CPLDs)

In 1980, engineers from Intel, Signetics, and Intersil founded Source 3, a design consulting company <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Their experience with ASIC chip makers led them to create their own field-programmable hardware <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. They raised $750,000 from a VC and founded Altera in February 1984 <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

Altera's first product, released in July 1984, was the EP300, a simple programmable logic device made with a CMOS EEPROM process, which was erasable and programmable <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. The main issue with PALs was that their structure didn't scale well with [[technological_advancements_that_impacted_fpga_development | Moore's Law]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. To leverage classical shrinking, Altera pioneered the **Complex Programmable Logic Device** (CPLD) <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. CPLDs connected smaller PALs with crossbar connections for greater scalability <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Altera's choice to use CMOS was significant, requiring them to go to Ricoh in Japan as CMOS wasn't available in the U.S. at the time <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Altera's success heralded the beginning of the [[global_semiconductor_supply_chain_dynamics | fabless design model]] <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## Xilinx and the First FPGA

In the mid-1980s, Ross Freeman, an engineer at Zylog, conceived an idea that transistors would eventually become cheap enough to create a universal piece of silicon <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. He recruited Zylog co-workers and founded Xilinx in February 1984 (original name Logica was taken) <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. They partnered with Seiko Corporation to produce their new chip, offering Seiko a way to keep their fabs busy and granting exclusive resale rights in Japan <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

Bill Carter was hired to design the product, facing the challenge of working with only Ross Freeman's loose patent application and Seiko's 2.5 micrometer CMOS process, which he had no prior experience with <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. The chip was expected to be very large, and Seiko's engineers doubted it would yield well <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

### The XC2064: The First FPGA

The team created the Xilinx XC2064, the first FPGA <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. Unlike PALs, which relied on a large AND gate set that slowed down as it grew, FPGAs removed the AND set entirely <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. Instead, FPGAs featured an array of configurable logic blocks (CLBs) connected by programmable switches <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Device inputs and outputs were placed around the device <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. Each CLB contained a pair of lookup tables, which mapped inputs to outputs to implement arbitrary logic functions <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. The interconnects between logic blocks were also programmable, allowing for arbitrary signal paths <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

The first Xilinx FPGAs required external memory to store programming when power was off; Actel later invented anti-fuse technology a few years later to help with this <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This design was a radical departure from PROMs, PLAs, and PALs, which had a family resemblance to memory chips <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

The XC2064 was a large chip for its time, with 85,000 transistors arranged into 64 CLBs and 58 input/output blocks, translating to less than a thousand gates <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. When taped out in 1985, its size strained Seiko's manufacturing capabilities <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. Of the first 25 wafers received from Seiko, only one worked, allowing Carter to program an inverter and confirm its functionality <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

### Early Challenges for FPGAs

The first FPGA competed against Monolithic Memories' PAL devices, and while customers initially grouped them together, FPGAs were fundamentally different <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
*   **Cost:** FPGAs cost hundreds of dollars due to their large die size and extremely low yields, while PALs were much cheaper <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.
*   **Ease of Use:** FPGAs were harder to use due to their newness <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Xilinx introduced their own [[history_of_chip_design_and_evolution_of_electronic_design_automation | Electronic Design Automation]] (EDA) software, which was complicated and hard to use, and performance was difficult to predict <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. In contrast, PALs were easier to understand, with simple, widely available third-party EDA software <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

## Market Takeoff and Differentiation

Despite these early shortcomings, FPGAs eventually thrived due to a fortuitous intersection of technology and business opportunity <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

### Technological Advancements
[[Technological advancements that impacted FPGA development | Moore's Law]] and maturing lithography technologies allowed for incredible classical scaling <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. Since FPGAs could scale unlike PALs, they were the first to benefit from crashing transistor costs <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. Crucially, a new process called chemical mechanical polishing drastically lowered the costs of making FPGA interconnects <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. This enabled FPGAs to exponentially grow their lookup table counts and interconnect wire lengths, making them faster and more powerful <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

### Business Opportunity and Fabless Model
The early 1990s saw the rise of independent foundries <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. Altera and Xilinx were early pioneers in the [[global_semiconductor_supply_chain_dynamics | fabless startup model]], allowing design groups to develop ideas and approach foundries for fabrication without needing their own manufacturing capabilities <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. Foundries, in turn, found that FPGAs, with their large dies, were excellent for honing and mastering their processes <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>. The FPGA market blossomed with new startups, many of which eventually closed or exited the business, but their optimizations and features were often absorbed by Xilinx and Altera through IP and patent acquisitions <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.

### Software as a Differentiator
Another significant differentiation was software <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>. While PAL EDA software was easy to use and widely available through third parties, this consumer-friendly situation had a downside: PAL manufacturers didn't control their software, limiting their hardware capabilities to what third-party EDA vendors supported <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. This led to PAL makers producing similar hardware, crashing the market to the lowest common denominator <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

FPGAs, however, controlled their own EDA, allowing companies like Xilinx and Altera to dictate their future by crafting software to enable more features and add automation for increased productivity <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

## Consolidation and Modern Applications

Xilinx and Altera continued to hold the majority share of the multi-billion dollar FPGA industry <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. However, both companies are no longer independent:
*   Intel acquired Altera in 2015 for about $16.7 billion <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.
*   AMD acquired Xilinx for an estimated $50 billion, closing in 2022 <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.

Today, FPGAs are widely used across various industries <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. As ASICs become increasingly expensive to design and fabricate, FPGAs have filled a valuable market gap, particularly in the [[applications_of_fpgas_in_various_industries | aerospace, military, and telecom spaces]] <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. They continue to gain new functionalities, expanding into areas like [[ai_accelerator_hardware_market_and_its_growth | AI processing]] and data centers <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. The success and "Swiss army knife" functionality of FPGAs reflect the semiconductor industry's innovative power <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.