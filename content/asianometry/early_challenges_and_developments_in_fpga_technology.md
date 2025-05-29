---
title: Early challenges and developments in FPGA technology
videoId: m-8G1Yixb34
---

From: [[asianometry]] <br/> 

A [[Differences between FPGA PAL PLA and ASIC | Field Programmable Gate Array (FPGA)]] is an integrated circuit that can be reprogrammed after manufacture to emulate a digital circuit <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. FPGAs are useful for prototyping new functionalities before mass production or for serving rare use cases that would not be economical for a custom chip <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While not the first to offer this capability, FPGAs have become the most commercially successful reprogrammable chips <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Precursors to FPGAs: Early Programmable Logic

For decades, engineers sought ways to create chips that could be reprogrammed post-manufacture <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Before FPGAs, two primary options existed for prototyping and testing logic functions on hardware:
*   **Transistor-Transistor Logic (TTL) Chips**: These involved plugging transistors into a printed circuit board, but were limited by board size and power consumption <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Application-Specific Integrated Circuits (ASICs)**: These were custom-built chips, incurring substantial upfront costs for photo masks and months of fabrication time. Mistakes in design were very costly as they could not be easily edited <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. ASICs were only economically viable for very large-scale use cases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

As integrated circuits became more widely adopted after the 1960s, the need for field programmability became more compelling <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Programmable Read-Only Memories (PROMs)
The first integrated circuits capable of implementing a programmable logic function were PROMs <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. In 1970, Harris Semiconductor introduced PROMs that could be programmed to implement arrays of programmable logic gates (an AND set and an OR set) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. These PROMs supported combinational (time-independent) logic, where outputs depend purely on inputs, unlike sequential logic functions that require external memory (like a rolling sum) <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Any combinational logic function can be expressed using AND and OR gates <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

Harris's PROMs had fixed AND gates and programmable OR gates, achieved using fusible nichrome metal links that were burned to program them, making them one-time use only <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This method made programming challenging due to the permanence of changes <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. However, using PROMs for programmable logic was inefficient due to unnecessary memory cells <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Programmable Logic Arrays (PLAs)
In 1975, Signetics (later part of NXP Semiconductors) introduced the Programmable Logic Array (PLA) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. PLAs allowed both the AND set and OR set of logic gates to be programmable, enabling a wider range of logic functions <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. However, this flexibility came at a significant cost: PLAs required a much larger chip, costing about $25 each in 1975 ($140 today), and still relied on burning fuse connections, making errors costly <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Despite their advantages, PLAs did not gain significant market traction <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Programmable Array Logic (PALs)
In 1977, John Birkner and H.D. Tua of Monolithic Memories modified the PLA to create the Programmable Array Logic (PAL) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. PALs traded some of the PLA's configurability for better performance and cost <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. They kept the AND set programmable but made the OR set fixed <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

A key improvement was the inclusion of sequential logic circuits, such as flip-flops, through the use of macrocells <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Flip-flops can store a single bit of information and use it in output calculations, making PALs more practical for everyday computer circuits that mix combinational and sequential logic <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

By the early 1980s, new technologies emerged allowing these circuits to be truly reprogrammable, often using ultraviolet light to erase the chip, eliminating the need for fuses <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. These small field-programmable devices (PROMs, PLAs, PALs) were categorized as Simple Programmable Logic Devices (SPLDs) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. PALs achieved some success, being widely produced by memory makers who found their structure similar to core products, and Monolithic Memories made them easy to use <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Emergence of Complex Programmable Logic Devices (CPLDs)

In 1980, engineers from Intel, Signetics, and Intersil founded Altera, a design consulting company <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Their experience with [[Differences between FPGA PAL PLA and ASIC | ASIC]] chipmakers led them to develop their own field-programmable hardware <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. In July 1984, Altera released the EP300, an SPLD made with a CMOS EEPROM process that was erasable and programmable <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

The main challenge with PALs was their architecture did not scale with [[Impact of Moores Law on FPGA growth and capabilities | Moore's Law]] <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. As the AND set of gates grew, performance slowed significantly because the number of transistors within the set increased much faster than the number of inputs and outputs <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. To leverage classical shrinking more effectively, Altera pioneered the **Complex Programmable Logic Device (CPLD)** <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. CPLDs consisted of multiple smaller PALs connected by crossbar connections, making them much more scalable <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Altera's choice to use CMOS technology was also significant, requiring them to work with Ricoh in Japan as CMOS was not readily available in the U.S. at the time <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Altera's success heralded the beginning of the [[Industry shifts and acquisitions in the FPGA market | fabless design model]] <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## The Birth of the FPGA: Xilinx XC2064

In the mid-1980s, Ross Freeman, an engineer at Zilog, envisioned a future where [[Impact of Moores Law on FPGA growth and capabilities | Moore's Law]] would make transistors so inexpensive that a single piece of silicon could meet a wide range of needs <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. He founded Xilinx in February 1984 with former Zilog colleagues to realize this vision <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

Xilinx partnered with Seiko Corporation to produce their new chip, pitching it as a way for Seiko to keep their fabs busy and offering exclusive resale rights in Japan <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Bill Carter was hired to design the product, facing a massive [[Chip design process and techniques | challenge]]: his only guidance was Ross Freeman's loose patent application, and he had no experience with Seiko's CMOS 2.5-micrometer process <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Carter had to learn on the fly while communicating with a Japanese-speaking fab <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

The chip was designed to be very large, a concern for Seiko's engineers who had never made anything of that size, raising fears of low yields for the young startup <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Despite repeated advice to "create something simple," Carter's design was elegant in its simplicity: the **Xilinx XC2064, the first FPGA** <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### FPGA Architecture and Initial Challenges
Unlike PALs, which relied on large AND gate arrays that slowed down as they grew, the FPGA removed the AND set entirely <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. Instead, the FPGA utilized an array of configurable logic blocks (CLBs) connected by programmable switches <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Device inputs and outputs were placed around the device <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. Each CLB contained a pair of lookup tables (like an array of outputs mapped to inputs) to implement arbitrary logic functions <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. The interconnects between logic blocks were also programmable, allowing arbitrary paths for logic flow <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

The first Xilinx FPGAs required external memory to store programming when power was off; Actel later invented anti-fuse technology a few years later to address this <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This was a radical departure from PALs and PLAs, which descended from memory chips <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

The XC2064 was a large chip for its time, with approximately 85,000 transistors arranged into 64 CLBs and 58 input/output blocks, translating to less than a thousand gates <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. Its sheer size strained Seiko's manufacturing capabilities <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. Of the first 25 wafers from Seiko, only one worked <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. Carter successfully programmed an inverter into that single working wafer, marking the first functional FPGA <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### Initial Disadvantages of FPGAs

Early FPGAs faced significant disadvantages compared to PALs:
*   **High Cost**: Due to their large die size and extremely low yields, the first FPGAs cost hundreds of dollars, while PALs were much cheaper <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. PALs were cheaper partly because their structure was similar to memory, allowing memory makers to churn them out <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   **Difficulty of Use**: The newness of the FPGA made it harder to use. Xilinx introduced its own Electronic Design Automation (EDA) software to help fit designs, but it was complicated and difficult to use, and performance was hard to predict <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. In contrast, PAL EDA software was simple, widely available from third parties, and easy to pick up <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

## How FPGAs Overcame Challenges and Thrived

Despite these early shortcomings, FPGAs gained traction and eventually thrived due to several factors:

### Technological Advancements
*   **[[Impact of Moores Law on FPGA growth and capabilities | Moore's Law]]**: The FPGA's architecture scaled well with [[Impact of Moores Law on FPGA growth and capabilities | Moore's Law]], unlike PALs <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. As transistor costs plummeted, FPGAs were uniquely positioned to benefit <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   **[[Challenges and innovations in integrated circuit interconnects | Chemical Mechanical Polishing (CMP)]]**: This new process drastically lowered the costs of making the complex interconnects necessary for FPGAs <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. This allowed FPGAs to exponentially grow their lookup table counts and interconnect wire lengths, making them faster and more powerful <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

### Business Opportunities and Industry Shifts
*   **Rise of Independent Foundries**: The early 1990s saw the rise of independent foundries, enabling the [[Industry shifts and acquisitions in the FPGA market | fabless startup model]] pioneered by Altera and Xilinx <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. This allowed design groups to focus on innovation without needing their own semiconductor manufacturing capabilities <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. Foundries, in turn, found that large-die FPGAs were excellent for honing their processes <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **Market Growth and Consolidation**: The FPGA market blossomed with new startups, which, though many failed, contributed optimizations and features that were eventually absorbed by Xilinx and Altera through [[Industry shifts and acquisitions in the FPGA market | IP and patent acquisitions]] <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.

### Software Control
*   **FPGA Control over EDA Software**: Unlike PAL manufacturers who relied on third-party EDA vendors and thus lacked control over their hardware's capabilities, FPGA companies (like Xilinx and Altera) developed and controlled their own EDA software <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>. This allowed them to dictate their future, crafting software to enable more features and automation, leading to greater productivity <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. The PAL market, without this control, converged to similar hardware and a race to the bottom <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

## Current Status
Xilinx and Altera continued to hold a majority share of the multi-billion dollar FPGA industry <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. However, they are no longer independent: Intel acquired Altera in 2015 for approximately $16.7 billion, and AMD acquired Xilinx for an estimated $50 billion, closing in 2022 <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

Today, [[history_and_evolution_of_field_programmable_gate_arrays_fpga | FPGAs]] are widely used across various industries, filling a valuable gap as [[Differences between FPGA PAL PLA and ASIC | ASICs]] become increasingly expensive to design and fabricate <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. They are particularly prevalent in aerospace, military, and telecom, and are gaining new functionalities in areas like AI processing and data centers <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. The FPGA's "Swiss Army knife" functionality and success exemplify the semiconductor industry's innovative power <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.