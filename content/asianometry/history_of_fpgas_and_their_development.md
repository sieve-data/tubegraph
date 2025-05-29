---
title: History of FPGAs and their development
videoId: m-8G1Yixb34
---

From: [[asianometry]] <br/> 

A Field Programmable Gate Array (FPGA) <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> is an integrated circuit that can be reprogrammed after manufacture to emulate a digital circuit <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. These devices are useful for prototyping new functionalities before mass production <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> or for serving niche use cases that are not economically viable for custom chips <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. While FPGAs were not the first devices with this reprogrammable capability, they have become the most commercially successful <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Early Programmable Logic

For decades, the industry sought ways to create chips that could be reprogrammed after manufacturing <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. In the early days of chip design, engineers had limited options for prototyping and testing logic functions on hardware <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>:

*   **TTL Chips**: These involved plugging transistors into a printed circuit board, but were limited by board size and power consumption <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Custom-Built Chips (ASICs)**: Getting a chip built to order, known today as an Application-Specific Integrated Circuit (ASIC) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, involved substantial upfront costs for photo masks and months of fabrication time <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. Mistakes in design were costly as they couldn't be easily edited <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This path only made economic sense for very large use cases <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

As integrated circuits became more widely adopted after the 1960s, the need for field programmability became more compelling <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## The First Programmable Integrated Circuits

The first integrated circuits capable of implementing a programmable logic function were [[comparison_between_fpgas_and_other_programmable_devices_like_proms_and_plas | Programmable Read-Only Memories (PROMs)]] <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Programmable Read-Only Memory (PROM)

In 1970, Harris Semiconductor introduced PROMs that could be programmed to implement an array of programmable logic gates, specifically an AND set and an OR set <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. These PROMs targeted combinational logic functions, where outputs are purely dependent on inputs <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Any combinational logic function can be expressed using a combination of OR and AND gates <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

Harris's PROM product had fixed AND gates, but the OR gates were programmable using fusible metal links made of nichrome <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Users programmed them by "burning" these switches, making them one-time use <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Harris did pioneering work in the fabrication of these burnable fuses <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. However, using PROMs for programmable logic was inefficient due to the excess memory cells <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### Programmable Logic Array (PLA)

In 1975, Signetics (later part of NXP Semiconductors) introduced the [[comparison_between_fpgas_and_other_programmable_devices_like_proms_and_plas | Programmable Logic Array (PLA)]] <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. With PLAs, both the AND set and OR set of logic gates were programmable <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>, allowing for a wider range of logic functions <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This flexibility came at a significant cost, as PLAs required a much larger chip, costing about $25 in 1975 (around $140 today) <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. Like PROMs, programming involved burning fuse connections, making errors costly <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Despite their advantages, PLAs did not gain significant market traction <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Programmable Array Logic (PAL)

In 1977, John Birkner and H.D. Chua of Monolithic Memories modified the PLA to create the [[comparison_between_fpgas_and_other_programmable_devices_like_proms_and_plas | Programmable Array Logic (PAL)]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The PLA's high configurability was seen as a drawback <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>, so the PAL sacrificed some configurability for improved performance and cost <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. It retained a programmable AND set but made the OR set of logic gates fixed <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

A key improvement in PAL design was the inclusion of sequential logic circuits through macrocells <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Practical computer circuits use a mix of combinational and sequential logic (where the output depends on past states, like a rolling sum) <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. PAL designers added sequential logic devices like flip-flops to the output end <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. A flip-flop can store a single bit of information and use it in calculations <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>, making PALs more practical for everyday use <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

By the early 1980s, new [[technological_advancements_that_impacted_fpga_development | technologies]] emerged for reprogramming these circuits, such as using ultraviolet light flashed through a window to erase them, eliminating the need for fuses <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. These small field programmable devices—PROMs, PLAs, and PALs—are categorized as Simple Programmable Logic Devices (SPLDs) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. PALs achieved some success and were widely produced, as memory makers found them similar enough to their core products <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## The Rise of Altera and CPLDs

In 1980, engineers from Intel, Signetics, and Intersil founded a design consulting company called Source III, specializing in helping companies work with silicon suppliers <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Their experience with ASIC chipmakers inspired them to create their own field programmable hardware <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. They raised $750,000 in venture capital and founded Altera <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

Altera's first product, released in July 1984, was the EP300, a simple programmable logic device made with a CMOS EEPROM process <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. It was erasable and programmable for various needs <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. The main problem with the PAL architecture was its lack of scalability; growing the AND set of gates proportionally decreased performance <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. To better leverage [[technological_advancements_that_impacted_fpga_development | classical scaling]], Altera pioneered the **Complex Programmable Logic Device (CPLD)** <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. CPLDs connected a bunch of smaller PALs with crossbar connections, making them much more scalable <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Altera's use of CMOS, which was not available in the United States at the time, required them to work with Ricoh in Japan <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Altera's success heralded the beginning of the fabless design model that now drives the American semiconductor industry <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

## The Birth of the FPGA: Xilinx

While Altera's CPLD was a step forward, another company truly evolved the concept to what we know today <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. In the mid-1980s, Ross Freeman, an engineer at Zilog, had an idea that as [[technological_advancements_that_impacted_fpga_development | Moore's Law]] continued, transistors would become so cheap that a single piece of silicon could meet diverse needs <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

Freeman recruited Zilog co-workers to join his new startup, originally named Logica (but already taken), and officially opened as Xilinx in February 1984 <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. They leveraged a connection with Seiko Corporation, the digital watchmaker, to produce their new chip, pitching it as a way for Seiko to keep their fabs busy in exchange for exclusive resale rights in Japan <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

Bill Carter, a young designer hired by Xilinx, faced immense challenges <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. His only design guidance was Ross Freeman's loose patent application <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Seiko's fab used a 2.5-micrometer CMOS process unfamiliar to Carter, who had to learn it while communicating with a Japanese-speaking fab across the Pacific <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. The chip was also going to be very large, with Seiko's engineers expressing concerns about yield <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Carter was repeatedly advised to create something simple to ensure it could be fabricated <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### The XC2064: The First FPGA

The result of this effort was the **Xilinx XC2064**, the first FPGA <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. The core problem with PALs was that their AND gate sets became slower as they grew larger, because the number of transistors grew much faster than the number of inputs and outputs <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

The FPGA's solution was radical: it removed the AND set of gates entirely <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. Instead, the FPGA featured an array of **Configurable Logic Blocks (CLBs)** connected by programmable switches <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, with device inputs and outputs placed around the perimeter <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. Each CLB contained a pair of lookup tables, which are essentially arrays of outputs mapped to inputs, allowing the FPGA to implement arbitrary logic functions <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. The interconnects between logic blocks were also programmable, allowing for arbitrary paths and connections <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

Early Xilinx FPGAs required external memory to store programming when power was off <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>; it was a few years later that Actel invented anti-fuse technology to address this <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This was a significant departure from PALs and PLAs, which had a family resemblance to memory chips <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

The XC2064 was a large chip, with about 85,000 transistors arranged into 64 CLBs and 58 input/output blocks, translating to less than a thousand gates <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. When the chip was first taped out in 1985, its sheer size strained Seiko's manufacturing capabilities <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. Of the first 25 wafers received, only one worked <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. Carter successfully programmed an inverter into that single working wafer, marking the creation of the first FPGA <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### Early Challenges for FPGAs

Initially, customers often grouped the XC2064 with Monolithic Memories' PAL devices, as they appeared to perform similar functions <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. However, the FPGA had significant differences:

*   **Cost**: The FPGA cost hundreds of dollars due to its large die and extremely low yields, while PALs were much cheaper <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>. PALs were cheaper partly because their structure was similar to memory, allowing memory makers to churn them out <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   **Ease of Use**: The FPGA's newness made it harder to use <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Xilinx introduced its own [[history_of_chip_design_and_evolution_of_electronic_design_automation | Electronic Design Automation (EDA)]] software to assist with design fitting, but it was complicated and performance was hard to predict <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. In contrast, PALs were easier to understand, with simple, widely available third-party EDA software <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

## FPGA's Path to Dominance

Despite its early shortcomings, the FPGA eventually thrived in the market, thanks to a fortuitous intersection of [[technological_advancements_that_impacted_fpga_development | technology]] and business opportunity <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

### Technological Advancements

*   **[[technological_advancements_that_impacted_fpga_development | Moore's Law]] and Scaling**: Maturing lithography [[technological_advancements_that_impacted_fpga_development | technologies]] ramped up classical scaling, allowing more transistors on a die <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. FPGAs, unlike PALs, were designed to scale, allowing them to benefit greatly as transistor costs crashed <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
*   **Chemical Mechanical Polishing (CMP)**: This new process drastically lowered the costs of making the complex interconnects required by FPGAs <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. As a result, FPGAs began to grow their lookup table counts and interconnect wire lengths exponentially, becoming faster and more powerful <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

### Business Opportunities

*   **Rise of Independent Foundries**: The early 1990s saw the rise of independent foundries <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. Altera and Xilinx were pioneers in the fabless startup model, allowing design groups to raise money and approach a foundry without needing semiconductor manufacturing expertise <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. Foundries, in turn, found that FPGAs with their large dies were excellent for honing and mastering their processes <a class="yt="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **Market Expansion**: The FPGA market blossomed with new startups, many of which eventually failed but introduced optimizations and features that Xilinx and Altera absorbed into their IP and patents <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.

### Software Differentiation

While PAL EDA software was user-friendly and widely available from third parties <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>, this posed a long-term detriment. PAL manufacturers did not control their software, limiting their agency over hardware capabilities and leading to similar hardware offerings and market commoditization <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. In contrast, FPGA companies controlled their own EDA, much like Nvidia controlling its drivers <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. This allowed FPGA companies to dictate their future, crafting software to enable more features and automation <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

## Modern FPGA Landscape

Today, Xilinx and Altera continue to hold the majority share of the multi-billion dollar FPGA industry <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>, though they are no longer independent:

*   Intel acquired Altera in 2015 for about $16.7 billion <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.
*   AMD acquired Xilinx for an estimated $50 billion, with the deal closing in 2022 <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.

FPGAs are now widely used across a [[applications_of_fpgas_in_various_industries | variety of industries]] <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. As ASICs become increasingly expensive to design and fabricate, FPGAs fill a valuable gap, particularly in aerospace, military, and telecom sectors <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>. They continue to gain new functionalities, expanding into areas like AI processing and data centers <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. The FPGA's "Swiss Army knife" functionality and success stand as a unique testament to the semiconductor industry's innovative power <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.