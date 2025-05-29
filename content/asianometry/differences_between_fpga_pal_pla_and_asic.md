---
title: Differences between FPGA PAL PLA and ASIC
videoId: m-8G1Yixb34
---

From: [[asianometry]] <br/> 
A Field Programmable Gate Array (FPGA) is an integrated circuit that can be reprogrammed after manufacture to emulate a digital circuit <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. FPGAs are useful for prototyping new functionalities before mass production or for serving rare use cases that are not economical for a custom chip <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While not the first with this capability, FPGAs are the most commercially successful <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The [[history_and_evolution_of_field_programmable_gate_arrays_fpga | history of FPGAs]] involves a blend of technological advancements and business developments <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Early Challenges in Chip Design <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>

Decades ago, if someone wanted to prototype and test a logic function on hardware, they had two main options:
*   **TTL Chips:** These were transistors plugged into a printed circuit board <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The limitation was the board's size and power consumption <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Custom-Built Chips (ASICs):** Getting a chip built to order, known today as an [[chip_design_process_and_techniques | Application Specific Integrated Circuit]] (ASIC) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, involved substantial upfront costs like paying for a photo mask and waiting months for fabrication <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Mistakes in the design were costly and couldn't be easily fixed <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This path was only economically sensible for very large use cases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

As integrated circuits became more widely adopted after the 1960s, the need for field programmability became more compelling <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Programmable Read-Only Memories (PROMs) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>

The first integrated circuits capable of implementing a programmable logic function were PROMs <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. In 1970, Harris Semiconductor introduced PROMs that could be programmed to implement an array of programmable logic gates, specifically an AND set and an OR set <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. These PROMs targeted combinational (time-independent) logic functions, where outputs depend purely on inputs <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Any combinational logic function can be expressed using a combination of OR and AND gates <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

Harris's PROM product had fixed AND gates, while the OR gates were programmable using fusible metal links made of nichrome <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Users programmed them by burning these switches, making them one-time use only and challenging to program <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Using PROMs for programmable logic was not efficient due to the unnecessary memory cells <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Programmable Logic Arrays (PLAs) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>

In 1975, Signetics (later part of NXP Semiconductors) introduced the Programmable Logic Array (PLA) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. With the PLA, both the AND set and OR set of logic gates were made programmable <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This allowed for a wider range of logic functions, but at a significant cost, as PLAs required a much larger chip <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. In 1975, each part cost about $25, or approximately $140 today <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. Like PROMs, PLAs were programmed by burning fuse connections, making errors costly <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Despite their advantages, PLAs did not gain widespread adoption <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

## Programmable Array Logic (PALs) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>

In 1977, John Birkner and H.D. Tua of Monolithic Memories modified the PLA to create the Programmable Array Logic (PAL) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The PLA had been "too configurable for its own good" <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, so the PAL traded some configurability for better performance and cost <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. It kept the AND set programmable but made the OR set of logic gates fixed <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

A key modification in PAL design was the inclusion of sequential logic circuits using macro cells <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Practical computer circuits use a mix of combinational and sequential logic <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. PAL designers added sequential logic devices like flip-flops to the output end <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. Flip-flops store a single bit of information and can use it in output calculations <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This made PALs more practical for everyday consumer usage <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

In the early 1980s, new technologies emerged to make these circuits more reprogrammable, such as using ultraviolet light through a window to erase them, eliminating the need for fuses <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. These small field programmable devices (PLAs, PALs) are categorized as Simple Programmable Logic Devices (SPLDs) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

PALs achieved some success and were widely manufactured, particularly by memory makers due to their structural similarity to memory chips <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Monolithic Memories also made them easy to learn <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

## The Rise of Complex Programmable Logic Devices (CPLDs) and FPGAs <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>

A significant problem with PALs was their structure did not scale well with [[impact_of_moores_law_on_fpga_growth_and_capabilities | Moore's Law]] <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. Simply growing the AND set of gates led to disproportionately slower performance because the number of transistors grew much faster than the number of inputs and outputs <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

In 1980, engineers from Intel, Signetics, and Intersil founded Altera <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Their experience with ASIC chip makers led them to create their own field programmable hardware <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. Altera's first product in July 1984 was the EP300, a simple programmable logic device made with a CMOS EEPROM process that was erasable and programmable <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

To leverage classical shrinking enabled by [[impact_of_moores_law_on_fpga_growth_and_capabilities | Moore's Law]], Altera pioneered the **Complex Programmable Logic Device (CPLD)** <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. CPLDs connect smaller PALs with crossbar connections for better scalability <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Altera's choice of CMOS technology, which required going to Ricoh in Japan at the time, was also impactful and heralded the beginning of the fabless design model <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### The First FPGA: Xilinx XC2064 <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>

In the mid-1980s, Ross Freeman, an engineer at Zilog, envisioned that with continued [[impact_of_moores_law_on_fpga_growth_and_capabilities | Moore's Law]], transistors would become cheap enough to create a piece of silicon meeting everyone's needs <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. He founded Xilinx, which officially opened in February 1984 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Xilinx partnered with Seiko Corporation for manufacturing <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

Bill Carter, the designer, faced significant challenges:
*   Limited design guidance beyond Freeman's patent application <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   Working with Seiko's 2.5 micrometer CMOS process, which Carter had no prior experience with <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   The chip's unprecedented size, raising concerns about yield <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

The result was the Xilinx XC2064, the first FPGA <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

#### Architectural Differences between FPGAs and PALs:
*   **PALs:** Consist of an AND set and an OR set, plus macro cells <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. The core problem was that scaling the AND set made it slower due to disproportionate growth in transistors versus inputs/outputs <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   **FPGAs:** The FPGA solution removed the AND set of gates entirely <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. Instead, FPGAs have an array of **configurable logic blocks (CLBs)** connected by programmable switches <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Device inputs and outputs are placed around the device <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
    *   Inside each CLB is a pair of **lookup tables (LUTs)**, which are arrays of outputs mapped to inputs <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. LUTs enable the FPGA to implement arbitrary logic functions <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
    *   Function results can be routed to other logics like flip-flops <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
    *   The interconnects between logic blocks are also programmable, allowing arbitrary paths where one block's output can become another's input <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

Early Xilinx FPGAs required external memory to store programming when power was off <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>; later, Actel invented anti-fuse technology to help with this <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This architecture was a radical departure from PALs and PLAs, which descended from memory chips <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

The XC2064 was a large chip for its time, with approximately 85,000 transistors, 64 configurable logic blocks, and 58 input/output blocks <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. Its size strained Seiko's manufacturing capabilities, with only one out of 25 initial wafers working <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

## FPGA vs. PAL: Early Market Dynamics <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>

Despite appearing to do similar things, FPGAs and PALs had significant differences:
*   **Cost:** The first FPGAs cost hundreds of dollars due to large die size and low yields, while PALs were much cheaper <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. PALs benefited from being structurally similar to memory, allowing memory makers to easily add them to their product lines <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   **Ease of Use:** The newness of FPGAs made them harder to use <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Xilinx introduced its own Electronic Design Automation (EDA) software, which was complicated and hard to use, and performance was difficult to predict <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. PALs, conversely, had simpler EDA software widely available through third parties, making them easier to pick up <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

### Why FPGAs Thrived <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>

Despite early shortcomings, FPGAs eventually thrived due to several factors:
*   **[[impact_of_moores_law_on_fpga_growth_and_capabilities | Moore's Law]]:** The FPGA launch coincided with maturing lithography technologies that rapidly scaled transistor density <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. FPGAs, unlike PALs, were designed to scale, so they benefited directly from crashing transistor costs <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
*   **Chemical Mechanical Polishing (CMP):** This new process drastically lowered the costs of making the necessary interconnects for FPGAs <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. This allowed FPGAs to exponentially grow their lookup table counts and interconnect wire lengths <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
*   **Rise of Independent Foundries:** The early 1990s saw the rise of independent foundries, a model pioneered by Altera and Xilinx <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. This allowed design companies to focus on innovation without needing their own manufacturing <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. Foundries also found FPGAs useful for honing and mastering their processes due to their large dies <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **[[industry_shifts_and_acquisitions_in_the_fpga_market | Software Control]]:** While PAL EDA software was consumer-friendly and widely available, it meant PAL manufacturers didn't control the software, limiting their hardware capabilities to what third-party EDA vendors supported <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. This led to similar hardware and market competition based on the lowest common denominator <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. In contrast, FPGA companies controlled their own EDA software, allowing them to dictate their future, enable more features, and add automation for productivity <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

Xilinx and Altera continue to hold a majority share of the multi-billion dollar FPGA industry <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. Altera was acquired by Intel in 2015 for approximately $16.7 billion <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>, and AMD acquired Xilinx for an estimated $50 billion, closing in 2022 <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.

Today, FPGAs are widely used across various industries, filling a valuable gap as ASICs become increasingly expensive to design and fabricate <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>. They are particularly prevalent in aerospace, military, and telecom, and are gaining new functionalities in areas like AI processing and data centers <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.