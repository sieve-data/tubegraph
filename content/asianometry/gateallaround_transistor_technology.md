---
title: GateAllAround Transistor technology
videoId: 5RPFfPtgw7g
---

From: [[asianometry]] <br/> 

TSMC's N2 process node is one of its most ambitious, with plans for three new N2 fabs in Hsinchu, Kaohsiung, and Taichung mentioned in their 4Q2023 earnings call <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. A key feature of this N2 process is a special type of transistor <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. After the semiconductor industry transitioned from planar transistors to 3D FinFETs in 2011 <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>, TSMC is now joining Samsung and Intel in another significant shift <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. This involves the vertically-stacked, gate-all-around, nanosheet/nanowire metal-oxide-semiconductor field-effect transistor (GAAFET) <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Beginnings: Understanding the Transistor

At its most basic, a transistor is an actively controlled switch <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

It consists of:
*   **Source and Drain**: These are created by doping regions of silicon with a dopant element implanted using an ion beam, a process called ion implantation <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Gate and Gate Oxide**: Located between the source and drain, they sit on top of the channel and control it through "capacitive coupling" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Channel**: The path between the source and drain <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

When the gate receives a specific voltage, known as the "threshold voltage," it "turns on" or "opens" <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This allows the flow of electrons or electron holes from the source to the drain along the channel <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This control of a material's ability to conduct such particles is called the "field effect" <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The semiconductor material conducts only part of the time, hence "semi" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. When combined, a transistor using the "field effect" with a metal gate and gate oxide (metal oxide) forms a "metal oxide semiconductor field effect transistor," or MOSFET <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. While some early gates were made from metal, many modern gates use polycrystalline silicon <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

While the MOSFET is the most common design, other types of transistors exist, such as bipolar junction transistors (BJTs), named for their three regions of alternatively doped silicon or germanium <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. In an integrated circuit (IC), transistors are used to design logic gates and other blocks like memories, for instance, SRAM <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## [[Short channel effects in transistors | Short Channel Effects]]

Ideally, a transistor would switch instantly, with zero current flow when the gate is closed and no resistance when open <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. However, as the original planar MOSFETs were shrunk over decades, they began to suffer from "[[Short channel effects in transistors | short-channel effects]]" <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

These effects manifest in two primary forms:
1.  **Threshold Voltage Roll-off**: When the channel length decreased, the threshold voltage (the voltage at which the gate opens) was no longer constant but decreased or "rolled off" <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. This exacerbates "sub-threshold leakage," a residual current that flows even when the gate's voltage is below the threshold, like a dripping faucet <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
2.  **Drain-Induced Barrier Lowering (DIBL)**: This occurs when the source and drain are so close that electrons from the source can diffuse into the drain, even "burrowing under the gate" <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. DIBL leads to a tiny parasitic current flow, causing the transistor to consume power even in "standby" mode <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

Multiplying these two effects across billions of transistors results in a significant power consumption problem <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Going Multigate

[[Short channel effects in transistors | Short channel effects]] arise from interference caused by electric fields emanating from the source and drain <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The traditional planar gate controls the channel from only one side, but as transistors shrunk, the source and drain's electric fields began encroaching horizontally, "stealing" control from the gate <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

For years, the industry managed to mitigate [[Short channel effects in transistors | short channel effects]] by lowering voltage, heavily doping the channel, or reducing source and drain depths <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. Another significant advancement was replacing the silicon dioxide gate oxide with a material having a higher dielectric constant (High-K), which strengthened the gate's capacitance and its electric field over the channel <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. Notably, Intel used High-K dielectrics like hafnium oxide in 2007 for their High-K metal gate, which paved the way for advanced atomic layer deposition techniques <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

However, these methods eventually reached their limits, necessitating an entirely new structure to regain control of the channel <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. In 1984, Japanese researchers Sekigawa and Hayashi proposed "multi-gate" transistors, specifically a "double-gate MOS" transistor or XMOS <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

This led to the development of the [[Evolution from FinFET to GAAFET | FinFET]], which significantly intensifies the gate's control by wrapping it around the channel (the "fin") on three sides <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Intel produced the first commercial [[Evolution from FinFET to GAAFET | FinFET]] devices in 2011 at the 22-nanometer process node, with TSMC and Samsung following a few years later in 2013 <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## Gate All Around (GAAFET)

The GAAFET builds upon the [[Evolution from FinFET to GAAFET | FinFET]] concept by wrapping the gate *entirely* around the channel <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. The term "gate all around" first appeared in a 1990 paper by Jean Pierre Colinge, M. H. Gao, A. Romano, and others <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. It describes a class of transistor structures where the gates completely surround the channel, rather than just on three sides <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

Within the GAAFET category, there are two main sub-categories: **Nanowires** and **Nanosheets** <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. These names describe the shape of the channel; nanowire channels are rounder than nanosheets <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. While nanowires' smaller channels offer greater gate control over electron flow, they also impede flow when the gate is open <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This often necessitates stacking nanowires, but only to a certain extent to avoid interference with interconnect layers built above them <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

## Fabricating a GAAFET

The fabrication process for a GAAFET evolves from that of the [[Evolution from FinFET to GAAFET | FinFET]], reflecting the semiconductor industry's evolutionary approach <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

For [[Evolution from FinFET to GAAFET | FinFETs]], key steps include:
*   Patterning dense, regular bunches of fins onto the silicon substrate using double-patterning lithography <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   Creating wells for the source and drain <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   Adding a temporary "dummy gate" to build the rest of the gate stack <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   Electrically isolating the transistor, demolishing the dummy gate, and building the real gate <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

The GAAFET process flow adds significant new steps:
1.  **Epitaxy**: Several layers of silicon and silicon-germanium are added on top of the silicon substrate, forming a "super-lattice" <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
2.  **Fin Creation**: These layers are then cut down to produce a "Fin," similar to a [[Evolution from FinFET to GAAFET | FinFET]] fin, requiring careful attention to avoid deformations and maintain a high aspect ratio (tall and skinny) <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
3.  **Shallow Trench Isolation (STI)**: Trenches are patterned around the transistor using lithography, dug with reactive ion etch, and filled with oxide to prevent electrical cross-talk and define the fins <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
4.  **Silicon-Germanium Etch**: The silicon-germanium layers are etched away, leaving the silicon layers suspended between the source and the drain <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This draws from MEMS technology's use of "sacrificial layers" <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
5.  **Atomic Layer Deposition (ALD)**: To build the gate and gate oxide, ALD is used to precisely surround the exposed channel wires <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. ALD is a method of applying layers of metals or chemicals one atom thick at a time <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
6.  **Gate Construction**: The primary challenge is correctly aligning the gate material around the channel <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Once aligned, the rest of the gate is built around the channels, similar to [[Evolution from FinFET to GAAFET | FinFET]] and planar transistors <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

## Gains from GAAFET

The transition to Gate-All-Around offers significant benefits, much like the switch from planar to [[Evolution from FinFET to GAAFET | FinFETs]] <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

Key gains include:
*   **Power Draw Reduction**: A 2020 study found that a nanosheet GAAFET draws about 20-35% less power than a [[Evolution from FinFET to GAAFET | FinFET]] when turned off <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
*   **Speed**: Approximately 10% gain in speed at constant power <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
*   **Density**: Around 15% increase in density, depending on the IC's mix of transistors <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.

These power gains are particularly appealing for chip designers in mobile and AI processing applications, where power is constrained or massive compute is needed <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This explains TSMC management's observation of "a much higher level of customer interest and engagement at N2 as compared with N3 at a similar stage" <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. GAAFETs are expected to significantly advance existing AI accelerator chips <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

## Race to the Gate

TSMC has largely dominated the decade-plus [[Evolution from FinFET to GAAFET | FinFET]] era <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. In an attempt to gain market share, Samsung and Intel have moved ahead with Gate-All-Around technology <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

*   **Samsung** has led the drive into GAAFET research since at least 2003 <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. They began offering their first GAAFET process, SF3E, in mid-2022, which shipped some products, primarily crypto miner chips <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. In late 2023, Samsung released their second-generation GAAFET node, SF3 <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Intel**'s GAAFET offering is named "RibbonFET" or "Nanoribbon" <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. Their first process node to use it is 20A, an internal node scheduled for mid-2024, followed by 18A, which is widely expected to bring Intel back to a leadership position <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. Intel's 20A and 18A processes also include "Backside Power," which moves power lines underneath the silicon substrates to open up additional space <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
*   **TSMC**'s N2 will not incorporate backside power until about a year later with their second-generation N2 processes, N2P and N2X <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>, which many see as a major advantage for Intel <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

Semiconductor industry watchers view the [[Evolution from FinFET to GAAFET | FinFET]]-to-GAAFET transition as a potential turning point in foundry competition, with the first to ship with volume winning <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. However, the close similarities in process flows between [[Evolution from FinFET to GAAFET | FinFET]] and GAAFET suggest that proficiency in the former will aid in the latter <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

## Conclusion

While the planar transistor lasted 50 years as a leading-edge architecture, the [[Evolution from FinFET to GAAFET | FinFET]] lasted about ten years <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. It is uncertain how long the GAAFET will remain at the leading edge <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

IMEC, the premier R&D institute in Belgium, is already exploring future transistor structures beyond GAAFET nanosheets or nanowires <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. Promising designs include:
*   **Forksheet**: An evolutionary step from GAAFET, featuring a bundle of vertically stacked sheets with a wall down the middle, offering higher gate control <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   **Complementary FET (CFET)**: Proposed by IMEC, where nanosheets or fins are folded on top of one another, creating a true 3D transistor <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

Although these advanced designs are not yet nearing production, they demonstrate the industry's continuous forward-looking approach <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. For now, the focus is on the N2 and its related processes, expected in 2025 <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.