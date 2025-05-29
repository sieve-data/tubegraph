---
title: TSMCs N2 process node and new fab locations
videoId: 5RPFfPtgw7g
---

From: [[asianometry]] <br/> 

[[tsmcs_technological_advancements | TSMC's N2 process node]] is one of the company's most ambitious undertakings <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. In their 4Q2023 earnings call, TSMC announced plans for three new N2 fabrication facilities (fabs) <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. These new fabs are slated for Hsinchu, Kaohsiung, and Taichung <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Assuming these are built, this represents a significant expansion for [[tsmcs_global_expansion_strategy | TSMC's global expansion strategy]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>, potentially having an [[impact_of_tsmcs_expansion_on_taiwan | impact on Taiwan]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Beyond the physical expansion, the N2 process is also notable for a special characteristic of its transistors <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Shift to Gate-All-Around Transistors

The N2 process will incorporate vertically-stacked, gate-all-around, nanosheet/nanowire metal-oxide-semiconductor field-effect transistors (MOSFETs) <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This marks a significant technological transition in semiconductor manufacturing.

### What is a Transistor?
A transistor is essentially an actively controlled switch <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. It has a source and a drain, created by doping regions of silicon using ion implantation <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Between the source and drain are the gate and gate oxide, which control the flow of electrons or electron holes along a channel through "capacitive coupling" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. When the gate receives a specific voltage (threshold voltage), it turns "on," allowing current to flow <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This control of a material's conductivity is known as the "field effect," giving the semiconductor its name <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. A transistor using the field effect is thus called a Field Effect Transistor, and with a metal gate and oxide, it becomes a MOSFET <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### Short Channel Effects and the Need for New Structures
For decades, the size of planar MOSFETs was shrunk <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. However, this shrinking led to "short-channel effects" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, primarily:
*   **Threshold Voltage Roll-Off**: The threshold voltage, which should be constant, began to decrease as the channel shortened <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This exacerbates "sub-threshold leakage," a residual current that flows even when the transistor is supposed to be off, leading to power waste <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Drain-Induced Barrier Lowering (DIBL)**: The source and drain become so close that electrons can diffuse directly into the drain, even when the transistor is on standby, causing parasitic current flow <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

These effects lead to significant power consumption issues when multiplied across billions of transistors in an integrated circuit (IC) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

To combat these issues, the industry made adjustments like lowering voltage, heavy channel doping, and reducing source/drain depths <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. A major improvement was replacing silicon dioxide gate oxides with "High-K" dielectrics (like hafnium oxide used by Intel in 2007) to strengthen the gate's control <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. However, these methods eventually ran their course, necessitating an entirely new transistor structure <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### From Planar to FinFET to GAAFET
The solution involved "multi-gate" transistors, first proposed in 1984 <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   **FinFET**: The FinFET intensifies the gate's control by wrapping it around the channel (the "fin") on three sides <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Intel introduced the first commercial FinFETs in 2011 at the 22-nanometer node <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. [[impact_on_tsmc_and_samsung | TSMC and Samsung]] followed in 2013 with their 16nm and 14nm nodes, respectively <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. [[impact_on_tsmc_and_samsung | TSMC]] has largely dominated the FinFET era <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

*   **Gate-All-Around FET (GAAFET)**: The GAAFET evolves the FinFET concept by completely wrapping the gate around the channel <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This class of transistors includes "nanowires" and "nanosheets," named for the shape of their channels <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. While nanowires offer more gate control due to smaller channels, they also impede electron flow when open, often requiring stacking <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Fabricating a GAAFET
The fabrication process for GAAFETs evolves from that of FinFETs <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. Key steps include:
1.  **Epitaxial Deposition**: Adding layers of silicon and silicon germanium on the substrate, creating a "super-lattice" <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
2.  **Fin Creation**: Cutting through these layers to produce a fin, similar to a FinFET <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
3.  **Shallow Trench Isolation**: Patterning and filling trenches with oxide to prevent electrical cross-talk and define fins <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
4.  **Silicon-Germanium Etch**: Etching away the silicon-germanium layers, leaving silicon layers suspended between the source and drain <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This utilizes "sacrificial layers" similar to MEMS technology <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
5.  **Gate and Gate Oxide Formation**: Using atomic layer deposition (ALD), the gate material is precisely aligned and applied around the exposed channel wires, one atom thick layer at a time <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

## Gains from GAAFETs in N2
The transition to GAAFETs in [[tsmcs_technological_advancements | TSMC's N2 process node]] offers significant benefits <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>:
*   **Power Efficiency**: A 2020 study found that a nanosheet GAAFET draws 20-35% less power than a FinFET when turned off <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This is particularly appealing for mobile and AI processing applications where power is a critical constraint <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Speed**: Gains in speed are around 10% at constant power <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
*   **Density**: Density improvements are about 15%, depending on the IC's mix of transistors <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

TSMC management has observed "a much higher level of customer interest and engagement at N2 as compared with N3 at a similar stage" <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>, indicating strong demand for these power-efficient transistors.

## Race to the Gate
The FinFET-to-GAAFET transition is seen as a potential turning point in foundry competition <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   [[impact_on_tsmc_and_samsung | Samsung]] has been a leader in the drive into GAAFET, researching it since at least 2003 <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. They began offering their SF3E GAAFET process in mid-2022, primarily shipping crypto miner chips <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. Their second-generation GAAFET node, SF3, was released in late 2023 <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   Intel's GAAFET offering, named "RibbonFET," will first appear in their 20A process node, scheduled for mid-2024, followed by 18A <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. Intel's 20A and 18A processes also include "Backside Power," which moves power lines underneath the silicon substrate to open up additional space <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. [[tsmcs_technological_advancements | TSMC's N2]] will not incorporate backside power until its second-generation N2P and N2X processes, about a year later <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>, which many view as a major advantage for Intel <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

The close similarities in process flows between FinFET and GAAFET suggest that expertise in the former will aid success in the latter <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

## Future of Transistors
While the planar transistor lasted 50 years and the FinFET about ten years as leading-edge architectures <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>, the duration of the GAAFET's prominence is yet to be determined <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. Research institutes like imec are already exploring future transistor designs:
*   **Forkshet**: An evolutionary step from GAAFETs, featuring vertically stacked sheets with a wall through the middle, offering higher gate control <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   **Complementary FET (CFET)**: A true 3D transistor where nanosheets or fins are folded on top of one another <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

These advanced structures are still in the R&D phase <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. For now, the focus is on [[tsmcs_technological_advancements | TSMC's N2]] and its variants, expected to arrive in 2025 <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.