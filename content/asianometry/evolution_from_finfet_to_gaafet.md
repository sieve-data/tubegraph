---
title: Evolution from FinFET to GAAFET
videoId: 5RPFfPtgw7g
---

From: [[asianometry]] <br/> 

TSMC's upcoming N2 process node is considered one of its most ambitious endeavors, with plans for three new N2 fabs in Hsinchu, Kaohsiung, and Taichung mentioned during their 4Q2023 earnings call <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. A key aspect of this N2 process involves a significant change to the transistors themselves <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

In 2011, the semiconductor industry made a major [[generational_shifts_in_semiconductor_manufacturing | generational shift]] from planar transistors to 3D FinFETs <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Over ten years later, TSMC is joining Samsung and Intel in another such transition <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, moving towards vertically-stacked, [[gateallaround_transistor_technology | gate-all-around]] nanosheet/nanowire metal-oxide-semiconductor field-effect transistors <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Beginnings: Understanding the Transistor
A transistor, at its most fundamental, acts as an actively controlled switch <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. It consists of a source and a drain, created by doping regions of silicon through ion implantation <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Between these two, a gate and its gate oxide sit atop a channel, controlling it via "capacitive coupling" <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

When the gate receives a specific "threshold voltage," it "opens" or "turns on," allowing electrons or electron holes to flow from the source to the drain along the channel <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This control over a material's conductivity is termed the "field effect," which lends the "Field Effect Transistor" its name <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Semiconductor materials conduct only part of the time, hence "semi" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

Early gates were made of metal, though today many are made from polycrystalline silicon <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The combination of the metal gate and gate oxide gives us "metal oxide," leading to the full name "metal oxide semiconductor field effect transistor," or MOSFET <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. While MOSFETs are the most common, other designs exist, such as bipolar junction transistors <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Transistors are integral to designing logic gates and memory blocks, like SRAM, within integrated circuits (ICs) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Short Channel Effects
Ideally, a transistor would switch instantly, with zero current flow when closed and no resistance when open <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. However, after decades of shrinking the planar MOSFET, "short-channel effects" began to emerge <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

These effects manifest in two primary forms:
1.  **Threshold Voltage Roll-Off**: When the channel length decreased, the threshold voltage, which was once constant, started to decrease or "roll off" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This exacerbates "sub-threshold leakage," a residual current that flows even when the gate's voltage is below the threshold, leading to wasted power <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
2.  **Drain-Induced Barrier Lowering (DIBL)**: When the source and drain are too close, electrons from the source can diffuse into the drain, even burrowing under the gate <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. DIBL results in a tiny parasitic current, causing the transistor to consume power even when on standby <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

Multiplying these effects across billions of transistors leads to significant power consumption problems <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Going Multigate: From Planar to FinFET
Short channel effects stem from the electric fields of the source and drain encroaching horizontally into the channel, interfering with the gate's control <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The planar gate, only touching the channel on one side, projects its electric field downwards, but this control is weakened by the proximity of the source and drain <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

For years, the industry tried to mitigate these effects by lowering voltage, heavily doping the channel, or reducing source/drain depths <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. Another significant step was replacing the silicon dioxide gate oxide with a high-K dielectric (high dielectric constant material), which strengthens the gate's capacitance and makes its electric field more dominant <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. Intel famously used High-K dielectrics like hafnium oxide in 2007, paving the way for [[advancements_in_semiconductor_technology | advanced atomic layer deposition techniques]] <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

However, these methods reached their limits, necessitating an entirely new structure to regain control of the channel <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. This led to the concept of "multi-gate" transistors, proposed in 1984 by Japanese researchers Sekigawa and Hayashi <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. They introduced a "double-gate MOS" or XMOS transistor <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

This concept evolved into the **FinFET**, which enhances gate control by wrapping the gate around the channel (the "fin") on three sides <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Intel was the first to commercially produce FinFET devices in 2011 at the 22-nanometer process node, with TSMC and Samsung following a few years later in 2013 with their 16 nm and 14 nm nodes, respectively <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## [[gateallaround_transistor_technology | Gate All Around]] (GAAFET)
The [[gateallaround_transistor_technology | Gate-All-Around FET]] (GAAFET) builds upon the FinFET concept by wrapping the gate entirely around the channel <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. The term "gate all around" first appeared in a 1990 paper by Jean Pierre Colinge and others <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. It describes a class of transistors where the gate completely encircles the channel, rather than just three sides <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

Within the broader GAAFET category, there are two main sub-categories:
*   **Nanowires**: Channels are rounder in shape <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. Their smaller channels offer greater gate control but can impede electron flow when the gate is open, necessitating vertical stacking <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Nanosheets**: Channels have a flatter, sheet-like shape <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

## Fabricating a GAAFET
The fabrication process for FinFETs largely retained similarities to planar transistors, with the main new step being the creation of dense, highly regular "fins" patterned onto the silicon substrate using double-patterning lithography <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

The GAAFET's process flow is an evolution from the FinFET's <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>:
1.  **Epitaxy**: Several layers of silicon and silicon germanium are added on top of the silicon substrate, forming a "super-lattice" <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
2.  **Fin Creation**: These layers are then cut down to produce a "Fin," similar to the FinFET's <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. Care is taken to maintain a high aspect ratio (tall and skinny) and prevent deformations <a class="yt-timestamp" data-t="00:09:56">[00:10:02]</a>.
3.  **Shallow Trench Isolation (STI)**: Trenches are patterned around the transistor using lithography, etched, and filled with oxide to prevent electrical cross-talk and define the fins <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
4.  **Sacrificial Layer Etch**: The silicon-germanium layers are etched away, leaving the silicon layers suspended between the source and drain <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This technique, drawing from MEMS, uses "sacrificial layers" to create suspended structures <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
5.  **Atomic Layer Deposition (ALD)**: Atomic layer deposition is used to precisely surround the exposed channel wires with the gate material and gate oxide, layer by layer <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. The main challenge lies in correctly aligning the gate material around the channel <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
6.  **Gate Stack Completion**: Once ALD is complete, the rest of the gate is built around the channels, similar to FinFET and planar transistors <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

## Gains of GAAFET
The transition to [[gateallaround_transistor_technology | Gate-All-Around]] transistors offers significant benefits, particularly in power efficiency <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. A 2020 study found that a nanosheet GAAFET draws 20-35% less power than a FinFET when turned off, depending on device dimensions <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

While speed and density gains are less dramatic (around 10% for speed at constant power and 15% for density, depending on the IC's mix of transistors), the power reduction is highly appealing to designers of mobile and AI processing applications <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Mobile devices benefit from constrained power, while AI devices need efficient compute for sheer scale <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This interest is reflected in TSMC management's statement that they are seeing "a much higher level of customer interest and engagement at N2 as compared with N3 at a similar stage" <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. GAAFETs are expected to significantly advance existing AI accelerator chips <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

## Race to the Gate
TSMC's dominance during the FinFET era has prompted Samsung and Intel to accelerate their adoption of [[gateallaround_transistor_technology | Gate-All-Around]] technology in an effort to gain market share <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

*   **Samsung**: Samsung has been researching GAAFETs since at least 2003 <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. They began offering their GAAFET process, SF3E, in mid-2022, primarily shipping crypto miner chips <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. Their second-generation GAAFET node, SF3, was released in late 2023 <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Intel**: Intel's GAAFET offering is named "RibbonFET" or "Nanoribbon" <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. Their first process node to use it, 20A, is slated for mid-2024, followed by 18A, which is widely anticipated to restore Intel's leadership position <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. Intel's 20A and 18A processes also include "Backside Power," which moves power lines underneath the silicon substrates to free up space <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
*   **TSMC**: TSMC's N2 process will not incorporate backside power until about a year later with its second-generation N2 processes (N2P and N2X), which many see as a significant advantage for Intel <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

The FinFET-to-GAAFET transition is seen by industry watchers as a potential turning point in foundry competition, where the first to achieve volume shipments could gain a significant lead <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. However, the close similarities in process flows between FinFET and GAAFET suggest that strong expertise in the former will aid in the latter <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

## Conclusion
While the planar transistor dominated for 50 years and the FinFET for about a decade at the leading edge, the lifespan of the GAAFET is yet to be determined <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

Looking ahead, imec, a premier R&D institute in Belgium, is exploring further transistor structures beyond GAAFET nanosheets and nanowires <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>:
*   **Forkshet**: An evolution from the GAAFET, it involves vertically stacked sheets with a dividing wall, offering higher gate control <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   **Complementary FET (CFET)**: This design folds nanosheets or fins on top of each other, creating a true 3D transistor <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

While these future designs are still in the research phase, the industry continues to look forward, with the N2 process and its brethren expected to arrive in 2025 <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.