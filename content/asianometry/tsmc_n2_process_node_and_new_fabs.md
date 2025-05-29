---
title: TSMC N2 process node and new fabs
videoId: 5RPFfPtgw7g
---

From: [[asianometry]] <br/> 

TSMC's upcoming [[smics_7nm_process_and_n2_node | N2 process node]] is one of its most ambitious developments yet <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. During their 4Q2023 earnings call, TSMC announced plans for three new N2 fabs in Hsinchu, Kaohsiung, and Taichung <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Beyond the significant number of new fabrication plants, the N2 process incorporates a special type of transistor <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Transistor Basics

A transistor is fundamentally an actively controlled switch <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. It consists of a source and a drain, created by doping regions of silicon through ion implantation <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Between these, a gate and a gate oxide sit atop a channel, controlling it via capacitive coupling <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. When the gate receives a specific voltage (threshold voltage), it turns "on," allowing electrons or electron holes to flow from the source to the drain along the channel <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This control, known as the "field effect," gives the semiconductor material its name—it conducts only part of the time <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

The most common transistor design is the metal-oxide-semiconductor field-effect transistor, or MOSFET <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Early gates were made from metal, though many modern gates use polycrystalline silicon <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Transistors are used in integrated circuits (ICs) to design logic gates and memory blocks, such as SRAM <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Short Channel Effects

Ideally, a transistor switches instantly, with zero current flow when off and no resistance when on <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. However, after decades of shrinking the original planar MOSFETs, the industry encountered "short-channel effects" <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

These effects manifest in two main ways:
*   **Threshold Voltage Roll-Off** When channels shorten, the threshold voltage (the voltage at which the gate opens) decreases, rather than remaining constant <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This exacerbates "sub-threshold leakage," a residual current that flows even when the gate's voltage is below the threshold, leading to wasted power <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Drain-Induced Barrier Lowering (DIBL)** With the source and drain positioned extremely close, electrons can "burrow" under the gate from the source to the drain <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. DIBL results in a tiny parasitic current, causing the transistor to consume power even when in standby mode <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

Multiplying these effects across billions of transistors creates a significant power consumption problem <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

Short channel effects arise from the electric fields of the source and drain horizontally encroaching into the channel, diminishing the gate's control <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. While methods like lowering voltage, heavy channel doping, and using high-K dielectrics (like Intel's hafnium oxide in 2007) helped mitigate these issues for a time, a new structural design became necessary <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

## Going Multigate: From FinFET to Gate-All-Around (GAAFET)

The concept of "multi-gate" transistors was first proposed in 1984 by Sekigawa and Hayashi <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This led to the FinFET, which enhances gate control by wrapping the gate around the channel (the "fin") on three sides <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. [[generational_shifts_in_semiconductor_manufacturing | Intel]] introduced the first commercial FinFET devices in 2011 at the 22-nanometer node, with TSMC and [[comparative_strategies_of_semiconductor_companies_like_tsmc_samsung_and_intel | Samsung]] following in 2013 with their 16nm and 14nm nodes, respectively <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

The Gate-All-Around FET (GAAFET) evolves the FinFET concept by completely surrounding the channel with the gate <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. First described in a 1990 paper, GAAFETs represent a class of structures where gates fully encompass the channel <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. Within the GAAFET category, two main sub-categories exist: Nanowires and Nanosheets, distinguished by the shape of their channels <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. While nanowires offer greater gate control due to smaller channels, they can impede electron flow when the gate is open, often requiring vertical stacking <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### Fabricating a GAAFET

The fabrication process for GAAFETs builds upon that of FinFETs, reflecting the semiconductor industry's evolutionary nature <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. Key steps include:
1.  **Epitaxy** Several layers of silicon and silicon-germanium are added atop the silicon substrate, forming a "super-lattice" <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
2.  **Fin Creation** These layers are then cut to produce a "Fin," similar to FinFETs, with careful attention to preventing deformations and maintaining a high aspect ratio (tall and skinny) <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
3.  **Shallow Trench Isolation (STI)** Trenches are patterned, dug, and filled with oxide around the transistor to prevent electrical cross-talk and create well-defined fins <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
4.  **Sacrificial Layer Removal** The silicon-germanium layers are etched away, leaving the silicon layers suspended between the source and drain <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This technique is borrowed from MEMS (Micro-Electro-Mechanical Systems) fabrication <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
5.  **Atomic Layer Deposition (ALD)** To build the gate and gate oxide, ALD is used to precisely surround the exposed channel wires with one-atom-thick layers of metals or chemicals <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. The main challenge is correctly aligning the gate material <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

## Gains from GAAFET Technology

The transition to GAAFETs offers significant advantages:
*   **Power Efficiency** A 2020 study found that a nanosheet GAAFET draws 20-35% less power than a FinFET when turned off, depending on device dimensions <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
*   **Speed** Gains in speed are around 10% at constant power <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
*   **Density** Density improvements are approximately 15%, varying with the IC's mix of transistor types (analog, digital, SRAM) <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

These power gains are particularly appealing for chip designers in mobile and AI processing applications, where power constraints and high compute demands are critical <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. TSMC management noted "a much higher level of customer interest and engagement at N2 as compared with N3 at a similar stage," indicating strong market demand for GAAFETs, especially for AI accelerator chips <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

## Race to the Gate

TSMC has largely dominated the FinFET era for over a decade <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. In an effort to gain market share, [[comparative_strategies_of_semiconductor_companies_like_tsmc_samsung_and_intel | Samsung]] and [[comparative_strategies_of_semiconductor_companies_like_tsmc_samsung_and_intel | Intel]] have moved ahead with GAAFET adoption <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

[[comparative_strategies_of_semiconductor_companies_like_tsmc_samsung_and_intel | Samsung]] has been researching GAAFETs since at least 2003 <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. They began offering their first GAAFET process, SF3E, in mid-2022, primarily for crypto miner chips, followed by their second-generation SF3 node in 2023 <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. [[comparative_strategies_of_semiconductor_companies_like_tsmc_samsung_and_intel | Intel]]'s GAAFET offering, "RibbonFET," will debut with their 20A process node in mid-2024, with the highly anticipated 18A node to follow <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

[[comparative_strategies_of_semiconductor_companies_like_tsmc_samsung_and_intel | Intel]]'s 20A and 18A GAAFET processes also feature a "Backside Power" innovation, which relocates power lines beneath the silicon substrate to open up additional space <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. TSMC's N2 will not incorporate backside power until its second-generation processes (N2P and N2X) about a year later, which many observers see as a significant advantage for [[comparative_strategies_of_semiconductor_companies_like_tsmc_samsung_and_intel | Intel]] <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

The FinFET-to-GAAFET transition is seen by industry watchers as a potential turning point in foundry [[competition_between_tsmc_and_samsung | competition]] <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. However, the close similarities in process flows between FinFET and GAAFET suggest that proficiency in the former will aid success in the latter <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

## The Future of Transistors

While planar transistors dominated for 50 years and FinFETs for about ten, the lifespan of the GAAFET on the leading edge is yet to be determined <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. Research institutes like imec in Belgium are already exploring next-generation transistor structures beyond GAAFET nanosheets and nanowires <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.

Promising designs include:
*   **Forksheet** An evolutionary step from the GAAFET, it involves vertically stacked sheets with a dividing wall, offering higher gate control <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   **Complementary FET (CFET)** This design folds nanosheets or fins on top of each other, creating a true 3D transistor <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

While these advanced designs are not yet close to production, they demonstrate the semiconductor industry's continuous drive for innovation <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. For now, the focus remains on N2 and its related processes, expected to arrive in 2025 <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.