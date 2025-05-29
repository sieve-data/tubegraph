---
title: Challenges and benefits of GAAFET over FinFET
videoId: 5RPFfPtgw7g
---

From: [[asianometry]] <br/> 

TSMC's upcoming N2 process node marks an ambitious shift in semiconductor manufacturing, featuring a new transistor technology [00:00:02]. This N2 process will incorporate the vertically-stacked, gate-all-around, nanosheet/nanowire metal-oxide-semiconductor field-effect transistor, known as [[gateallaround_gaafet_transistor_technology | GAAFET]] [00:00:21, 00:00:39, 00:00:42]. This transition follows the industry's previous move from planar transistors to 3D FinFETs in 2011 [00:00:26, 00:00:32].

## Transistor Basics and Short Channel Effects

A transistor fundamentally functions as an actively controlled switch [01:02]. It consists of a source and a drain, created by doping regions of silicon through ion implantation [01:07, 01:10, 01:15]. Between the source and drain, the gate and gate oxide control the channel via "capacitive coupling" [01:18, 01:22, 01:24]. When the gate voltage reaches a specific "threshold voltage," the transistor turns "on," allowing electrons or electron holes to flow from source to drain along the channel [01:28, 01:30, 01:35, 01:37]. This control mechanism is termed the "field effect," leading to the name Field Effect Transistor (FET) [01:42, 01:55]. Most commonly, this is a Metal-Oxide-Semiconductor Field-Effect Transistor, or MOSFET [02:15, 02:20].

However, as the size of the original planar MOSFET shrunk, "short-channel effects" began to impede performance [03:24, 03:27]. These effects manifest in two primary ways:

1.  **Threshold Voltage Roll-off**: When the channel shortens, the threshold voltage, which was once constant, decreases ("rolls off") [03:42, 03:43, 03:48, 03:54]. This exacerbates "sub-threshold leakage," where a residual current flows even when the gate voltage is below the threshold, leading to unwanted power consumption [04:00, 04:04, 04:07, 04:11, 04:16].
2.  **Drain-Induced Barrier Lowering (DIBL)**: When the source and drain are too close, electrons can diffuse from the source to the drain, sometimes "burrowing under the gate" [04:25, 04:28, 04:32, 04:37]. This results in a tiny parasitic current flow, causing the transistor to consume power even on standby [04:43, 04:46].

These short-channel effects, multiplied across billions of transistors in an integrated circuit (IC), lead to significant power consumption issues [04:52, 04:55].

## From Planar to FinFET

Short-channel effects arise from the electric fields of the source and drain encroaching horizontally into the channel, diminishing the gate's control [05:01, 05:04, 05:07, 05:12, 05:17, 05:22, 05:26]. Initially, the industry managed these effects by lowering voltage, heavily doping the channel, or reducing source/drain depths [05:42, 05:46, 05:50]. A significant step was replacing the gate oxide with high-K dielectrics, such as hafnium oxide used by Intel in 2007, which strengthened the gate's capacitance and its electric field [05:55, 06:00, 06:06, 06:12, 06:19].

However, these methods reached their limits, necessitating an entirely new transistor structure [06:27, 06:31]. The concept of "multi-gate" transistors was proposed by Sekigawa and Hayashi in 1984 [06:37, 06:40]. This led to the development of the FinFET, which enhances gate control by wrapping the gate around the channel (the "fin") on three sides [06:56, 07:00]. Intel was the first to commercially produce FinFET devices in 2011 at the 22-nanometer node, with TSMC and Samsung following in 2013 [07:06, 07:10, 07:15].

## GAAFET: The Next Iteration

The [[gateallaround_gaafet_transistor_technology | GAAFET]] is an evolution of the FinFET, where the gate completely encloses the channel [07:29]. The term "gate all around" first appeared in a 1990 paper [07:35, 07:39]. [[gateallaround_gaafet_transistor_technology | GAAFET]] refers to a class of transistors whose gates fully surround the channel [07:45, 07:48, 07:54].

Within the [[gateallaround_gaafet_transistor_technology | GAAFET]] category, there are two main sub-categories based on channel shape: Nanowires and Nanosheets [07:57, 08:04]. Nanowire channels are rounder, while nanosheets are flatter [08:04]. While nanowires offer greater gate control due to smaller channels, they can impede electron flow when the gate is open [08:15, 08:21, 08:25]. This often necessitates stacking multiple nanowires, though too many stacks can interfere with interconnect layers above [08:30, 08:35].

## Fabricating a [[gateallaround_gaafet_transistor_technology | GAAFET]]

The fabrication process for FinFETs largely built upon that of planar transistors, with the key new step being the creation of dense, regular fins using double-patterning lithography [08:42, 08:47, 08:54, 09:00]. The [[gateallaround_gaafet_transistor_technology | GAAFET]] process flow further evolves from the FinFET's [09:29, 09:35].

To create a [[gateallaround_gaafet_transistor_technology | GAAFET]]:
1.  **Epitaxy**: Several layers of silicon and silicon germanium are deposited on the silicon substrate, forming a "super-lattice" [09:35, 09:40, 09:47].
2.  **Fin Creation**: These layers are cut to produce a "Fin" structure similar to that of a FinFET, requiring careful attention to maintain high aspect ratios and prevent deformations [09:47, 09:51, 09:56, 10:02, 10:07].
3.  **Shallow Trench Isolation (STI)**: Trenches are patterned, etched, and filled with oxide to prevent electrical cross-talk and define the fins [10:12, 10:17, 10:23].
4.  **Sacrificial Layer Etching**: The silicon-germanium layers are etched away, leaving the silicon channels suspended between the source and drain. This technique is borrowed from MEMS (Micro-Electro-Mechanical Systems) [10:27, 10:31, 10:36].
5.  **Gate Formation**: Atomic layer deposition (ALD) is used to precisely surround the exposed channel wires with the gate and gate oxide, one atomic layer at a time [10:43, 10:45, 10:49, 10:55]. A major challenge is correctly aligning the gate material around the channel [11:00, 11:03]. The rest of the gate is then built, similar to FinFETs and planar transistors [11:07].

## Benefits of [[gateallaround_gaafet_transistor_technology | GAAFET]] over FinFET

The transition to [[gateallaround_gaafet_transistor_technology | GAAFET]] offers significant advantages, particularly in power efficiency [11:13, 11:17, 11:20]:
*   **Power Draw**: A 2020 study found that a nanosheet [[gateallaround_gaafet_transistor_technology | GAAFET]] consumes 20-35% less power than a FinFET when turned off, depending on dimensions [11:20, 11:25, 11:29].
*   **Speed**: Gains in speed are about 10% at constant power [11:35, 11:39].
*   **Density**: Density improvements are approximately 15%, varying with the IC's mix of transistor types (analog, digital, SRAM) [11:39, 11:43].

These power gains are particularly appealing for chip designers focusing on mobile and AI processing applications, given the power constraints in mobile devices and the massive computational needs of modern AI [11:51, 11:55, 12:00]. This is reflected in TSMC's observation of "a much higher level of customer interest and engagement at N2 as compared with N3 at a similar stage" [12:05, 12:11]. [[gateallaround_gaafet_transistor_technology | GAAFET]]s are expected to significantly advance AI accelerator chips [12:17].

## Race to the Gate

TSMC's dominance during the 10+ years of the FinFET era has prompted Samsung and Intel to accelerate their adoption of [[gateallaround_gaafet_transistor_technology | GAAFET]] technology in an attempt to gain market share [12:24, 12:28, 12:33].

*   **Samsung**: Samsung has been researching [[gateallaround_gaafet_transistor_technology | GAAFET]] since at least 2003 [12:38, 12:42]. They began offering their first [[gateallaround_gaafet_transistor_technology | GAAFET]] process, SF3E, in mid-2022, primarily shipping crypto miner chips rather than major digital logic products [12:49, 12:55, 13:00]. Their second-generation [[gateallaround_gaafet_transistor_technology | GAAFET]] node, SF3, was released later in 2023 [13:07, 13:12].
*   **Intel**: Intel's [[gateallaround_gaafet_transistor_technology | GAAFET]] offering is named "RibbonFET" or "Nanoribbon" [13:17]. Their first process node to use it, 20A, is scheduled for mid-2024, followed by 18A, which is anticipated to restore Intel's leadership position [13:22, 13:25, 13:30]. Intel's 20A and 18A [[gateallaround_gaafet_transistor_technology | GAAFET]] processes also include "Backside Power," which moves power lines underneath the silicon substrate to open up additional space [13:36, 13:41, 13:44]. TSMC's N2 will not incorporate backside power until its second generation, N2P and N2X, about a year later [13:49, 13:54], which many see as a significant advantage for Intel [13:54].

The [[gateallaround_gaafet_transistor_technology | FinFET-to-GAAFET]] transition is widely viewed as a potential turning point in foundry competition, with the first to achieve volume production often gaining a significant lead [14:02, 14:04, 14:08]. However, the close similarities in process flows between FinFET and [[gateallaround_gaafet_transistor_technology | GAAFET]] suggest that expertise in the former will aid in the latter [14:13, 14:18].

## Future Innovations

While the planar transistor architecture lasted 50 years and the FinFET about ten years at the leading edge, the duration of the [[gateallaround_gaafet_transistor_technology | GAAFET]]'s dominance remains to be seen [14:26, 14:30, 14:33]. Research and development continues beyond [[gateallaround_gaafet_transistor_technology | GAAFET]] [14:33, 14:38].

The semiconductor R&D institute imec is exploring [[future_innovations_beyond_gaafet | other transistor structures]] beyond current nanosheet or nanowire [[gateallaround_gaafet_transistor_technology | GAAFET]]s [14:38, 14:42, 14:46]. Promising designs include:
*   **Forksheet**: This design involves a bundle of vertically stacked sheets with a wall dividing them [14:51, 14:57]. It's an evolutionary step from [[gateallaround_gaafet_transistor_technology | GAAFET]], offering higher gate control [15:02].
*   **Complementary FET (CFET)**: This concept involves folding nanosheets or fins on top of one another to create a true 3D transistor [15:09, 15:14].

Though these advanced structures are not yet in production, the ongoing research demonstrates a continuous drive for future advancements in the semiconductor industry [15:21, 15:25].