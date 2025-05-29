---
title: Evolution of Moores Law and advanced chip design
videoId: uSchEDY6y20
---

From: [[acquiredfm]] <br/> 

The semiconductor industry, fundamental to the modern technological landscape, has seen remarkable growth and complexity, driven significantly by the principles and aspirations of [[The role of technology choices and Moores Law in semiconductor advancement | Moore's Law]]. Companies like Synopsys, an $80 billion entity specializing in electronic design automation (EDA) software, have been crucial in enabling this advancement <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. EDA software is considered essential infrastructure behind the AI era and all current semiconductor innovation <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Early Days of Chip Design and Synopsys

In the mid-1980s, when Synopsys was founded, the semiconductor industry experienced its worst downturn <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. At the time, chip design was often done manually, with functional designs drawn on paper or using schematic entry tools <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. The focus was on minimizing the number of gates to reduce area, with circuit speed determined by the longest path through the design <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

Art de Geus, Synopsys's founding CEO, accidentally developed an innovative design tool called Socrates at General Electric (GE), which automated the creation of denser circuits using multiplexers <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. This program yielded "astoundingly good results" compared to manual design, making GE quickly known for its synthesis work <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Synthesis, the process of automatically designing circuits, transformed the field from "computer aided design" (CAD) to "electronic design automation" (EDA) <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. Unlike CAD tools that merely aided designers, synthesis tools could actively change circuits, a capability initially met with skepticism but ultimately leading to significant improvements in size and speed <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

Synopsys spun out of GE with support and a transaction on technology valued at the equivalent of a million dollars <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. Early customers, impressed by the ability to make circuits 30% smaller and faster in a few hours, became collaborators, providing crucial feedback that helped refine the tools <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

## Moores Law and the [[The evolution of the semiconductor industry | Semiconductor Industry]]

[[Modern Approaches to Moores Law | Moore's Law]], initially an observation of exponential growth in transistor density, became a driving force and a self-fulfilling prophecy for the semiconductor industry <a class="yt-timestamp" data-t="00:29:43">[00:29:43]</a>. Synopsys has contributed about "10 million X in productivity" to this exponential advancement <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>.

The evolution of the semiconductor industry also saw a shift from Integrated Device Manufacturers (IDMs) – companies with their own fabs – to a focus on "fabless design" and specialized foundries like [[Semiconductor Industry and TSMC | TSMC]] <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. TSMC, founded three months after Synopsys, exemplifies this industry transformation <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.

## Increasing Complexity and Collaboration

Modern chip design faces [[Challenges and strategic decisions in the semiconductor industry | increasing complexity]]. Early chip design software capacity limited the size of designs an engineer could undertake <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. Over time, optimization priorities evolved from primarily performance to including power and area <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

The introduction of AI in synthesis and place-and-route in 2018 initially met resistance from users who wanted to understand every AI change, despite better results <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. However, AI is now well-accepted for its role in "massive optimization problems" involving billions of transistors, where human optimization is impossible <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. The key constraint in EDA is "absolute correctness in functionality," as errors in manufacturing are extremely costly <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.

Synopsys's role has become "mission critical" to the success of companies like Nvidia <a class="yt-timestamp" data-t="00:27:05">[00:27:05]</a>. This requires constant innovation to stay ahead of customer aspirations for bigger and better products <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>. A crucial aspect of this advancement is the collaboration between Synopsys, chip designers, and foundries (like TSMC, Samsung, Intel, and GF) <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>. This partnership has evolved from mere "enablement" (adapting existing foundry inputs) to deep "process development" collaboration, where Synopsys engineers work with foundries during technology development to ensure that physics and design align <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. This "Design Technology Co-Optimization" (DTCO) ensures that designs can be manufactured and that manufacturing processes support advanced designs <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.

The industry is now "bumping up against the edges of physics" <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>. Miniaturization to angstrom levels brings challenges like heat generation, warpage, and cracking when billions of transistors are jammed together <a class="yt-timestamp" data-t="00:38:47">[00:38:47]</a>.

## Addressing Future Performance: Beyond Moore's Law

To achieve greater performance gains (4x, 8x, 16x), two main strategies are emerging:
1.  **Specialized Hardware**: Developing hardware specifically for certain workloads, moving beyond general-purpose processors. The GPU, initially for pixels, is an example of such a specialized accelerator <a class="yt-timestamp" data-t="00:41:21">[00:41:21]</a>. This is seen in "software-defined architectures" where high-level functional requirements drive hardware design <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>.
2.  **Advanced Packaging and Multi-Die Architectures**: Splitting functionality across multiple chips (dies) and bringing them "really close together" <a class="yt-timestamp" data-t="00:42:57">[00:42:57]</a>. The key enabler for this is "connectivity," significantly improving bandwidth and reducing energy consumption for inter-chip communication <a class="yt-timestamp" data-t="00:43:28">[00:43:28]</a>. Nvidia's Blackwell chip, using a silicon interposer between two dies, is a prime example <a class="yt-timestamp" data-t="00:43:54">[00:43:54]</a>. These multi-die systems can include processors and stacked memories <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>.

This new era is termed "Symore" – "systemic complexity with a [[Modern Approaches to Moores Law | Moore's Law]] exponential ambition" <a class="yt-timestamp" data-t="00:44:57">[00:44:57]</a>. It signifies a shift from focusing on single-chip density to optimizing entire systems to achieve [[Modern Approaches to Moores Law | Moore's Law]]-like outcomes <a class="yt-timestamp" data-t="00:45:27">[00:45:27]</a>. Power reduction, for instance, is more effectively achieved at the software layer than at the transistor level <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>. This involves multi-dimensional optimization across architectural, physical, and economic factors <a class="yt-timestamp" data-t="00:49:48">[00:49:48]</a>. The cost implications, such as a $15,000 chip for a phone, drive the need for strategic trade-offs between angstrom-level scaling and multi-die architectures <a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>.

## Future of Semiconductor Manufacturing and Design

EUV (Extreme Ultraviolet) lithography still has "a lot of mileage" for future advancements, with new generations of machines continually emerging <a class="yt-timestamp" data-t="00:53:55">[00:53:55]</a>. The industry has a history of engineers "working around science" to overcome perceived physical limits, as seen with the introduction of finFET transistors <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>.

The industry is now driven by an "end market pull" in addition to a "technology push" <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>. Big Data and AI applications demand customized silicon, leading many system companies to design their own chips <a class="yt-timestamp" data-t="00:59:01">[00:59:01]</a>. For example, 45% of Synopsys's revenue now comes from system companies, such as automotive OEMs, who may not sell chips but architect their electronics and use Synopsys software for virtualization <a class="yt-timestamp" data-t="01:02:16">[01:02:16]</a>.

To further expand its capabilities, Synopsys announced the acquisition of Ansys in January, a leader in multiphysics simulation and analysis <a class="yt-timestamp" data-t="01:04:22">[01:04:22]</a>. This acquisition addresses two key areas:
1.  **Deep Core Business**: Integrating Ansys's expertise in thermal and structural simulation to tackle the deep physics challenges at the silicon level <a class="yt-timestamp" data-t="01:04:02">[01:04:02]</a>.
2.  **System-Level Design**: Enabling system companies (like automotive OEMs) to create digital twins of entire products, simulating the interaction between electronics, mechanics, and other physics early in the design process <a class="yt-timestamp" data-t="01:04:31">[01:04:31]</a>.

This aims to provide a "design solution from Silicon to system," recognizing that physical testing will become impractical and that simulation, enhanced by accelerated compute and AI, will play a crucial role in future product development <a class="yt-timestamp" data-t="01:07:50">[01:07:50]</a>.

## Synopsys Culture and Societal Role

The continued success of Synopsys is rooted in its culture, which emphasizes continuous innovation and a commitment to tackling the most complex problems <a class="yt-timestamp" data-t="01:11:02">[01:11:02]</a>. The company values long-term employees alongside continuous rejuvenation through new talent and learning <a class="yt-timestamp" data-t="01:09:34">[01:09:34]</a>. Synopsys's leadership has navigated increasing [[Collaborative innovation in the semiconductor industry | systemic complexity]] and globalization, recognizing the importance of trust and collaboration in the ecosystem <a class="yt-timestamp" data-t="00:56:52">[00:56:52]</a>.

As the industry faces challenges like increased energy utilization, climate change, and geopolitical tensions, companies like Synopsys are increasingly expected to take on a broader societal responsibility, acting as "value centers of gravity" beyond their technological contributions <a class="yt-timestamp" data-t="01:13:07">[01:13:07]</a>.