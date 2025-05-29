---
title: The role of electronic design automation in chip design
videoId: uSchEDY6y20
---

From: [[acquiredfm]] <br/> 

Electronic Design Automation (EDA) is the specialized software that chip designers use to create semiconductors <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Synopsys is a leading company in this field, alongside Cadence Design Systems <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Often likened to productivity software like Microsoft Excel or Figma for chip designers, EDA manages the immense complexity of chip design <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Its capabilities make entirely new types of chips possible that would be unachievable without it <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. EDA is considered essential infrastructure behind the [[AI era | AI era]] and the ongoing [[semiconductor innovation | semiconductor innovation]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Without EDA and the [[challenges_in_semiconductor_manufacturing_and_technology_optimization | incredible optimizations]] its software performs, [[AI applications | AI applications]] would not be possible <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. In a full-circle development, Synopsys now even uses [[impact_of_ai_in_electronic_design_automation | AI to design the software that designs chips]] <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## From Computer-Aided Design to Electronic Design Automation

Before the advent of EDA, chip design was a highly manual process, often involving paper or schematic entry systems <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. The early focus was on managing functional and physical layers <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

### The Birth of Synthesis

Art De Geus, the founding CEO of Synopsys, describes the mid-1980s as a period when General Electric (GE) was involved in semiconductors <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. While at GE, De Geus and his team developed innovative design tools, including one focused on "synthesis" <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Synthesis involved automatically generating circuits, initially with a program called Socrates <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This was a rebellious idea at the time <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

GE's eventual exit from the semiconductor field due to an industry downturn in 1985 led to the accidental spin-out of Synopsys <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The small team, with GE's support, took their synthesis technology to form an independent company <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

Early synthesis tools were able to make circuits significantly smaller (fewer gates) and faster (shorter critical path) compared to manual designs <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. This capability was revolutionary, as prior "computer-aided design" (CAD) tools merely aided designers, whereas synthesis actively "created something" <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. This shift marked the transformation from CAD to [[the_history_and_evolution_of_synopsys | Electronic Design Automation (EDA)]] <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

### The "License to Kill"

A key differentiator of EDA was its ability to change a circuit for the better <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. Previously, if a tool altered a design, it was assumed to have introduced bugs <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. This capability, dubbed "license to kill" by Synopsys, meant designers had to trust the software to intervene and improve their work <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

### Integration of AI and Machine Learning

Synopsys began integrating [[impact_of_ai_in_electronic_design_automation | AI]] into its synthesis and place and route tools in 2018 <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>. Initially, users showed resistance, wanting to understand every change made by the AI <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. However, because the [[impact_of_ai_in_electronic_design_automation | AI]] consistently delivered better results, it is now widely accepted and used in production by dozens of customers <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.

EDA software focuses on optimization problems, specifically for placing and routing billions of transistors within a small area to achieve desired performance, power, and area targets <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. The fundamental difference between EDA's [[impact_of_ai_in_electronic_design_automation | AI]] and other generative AI applications is the requirement for absolute correctness in functionality, with zero tolerance for error <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>. This absolute correctness is crucial because the cost of manufacturing a chip with a bug is immense <a class="yt-timestamp" data-t="00:18:55">[00:18:55]</a>.

## EDA's Role in Modern Semiconductor Industry

### Enabling Moore's Law

[[The evolution of the semiconductor industry and the rise of the fabless model | Moore's Law]] has been a driving force, and EDA plays a critical role in its continuation <a class="yt-timestamp" data-t="00:29:53">[00:29:53]</a>. It's not a natural law but rather relies on continuous innovation from companies like Synopsys <a class="yt-timestamp" data-t="00:29:27">[00:29:27]</a>. Synopsys estimates it has contributed about a "10 million x" increase in productivity <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>. The continuous push for better performance requires constant innovation and close collaboration with customers <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>.

### Collaboration with Foundries: Design Technology Co-Optimization (DTCO)

The relationship between EDA companies and foundries has evolved significantly <a class="yt-timestamp" data-t="00:36:28">[00:36:28]</a>. Historically, foundries provided "enablement" inputs for EDA products <a class="yt-timestamp" data-t="00:36:34">[00:36:34]</a>. However, in the last six to seven years, it has become impossible to design advanced chips without deep collaboration <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>. Synopsys engineers now sit with hundreds of engineers at foundries like TSMC, Samsung, Intel, and GF during process development <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. This close partnership, known as Design Technology Co-Optimization (DTCO), ensures that designs are aligned with manufacturing capabilities and that the physical limitations are understood and managed <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.

### Systemic Complexity and Multi-Die Architectures (SyMoore)

As [[technology_choices_and_advances_in_semiconductors | chip design]] pushes the boundaries of physics, new challenges arise, such as thermal issues, warpage, and cracking when billions of transistors are jammed together <a class="yt-timestamp" data-t="00:38:47">[00:38:47]</a>. This has led to a shift from focusing solely on single-chip density to "systemic complexity" <a class="yt-timestamp" data-t="00:37:52">[00:37:52]</a>.

One major innovation to achieve higher performance is [[technology_choices_and_advances_in_semiconductors | multi-die architectures]] and advanced packaging <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a>. Instead of larger single chips, functionality is split across multiple dies brought very close together, often on an interposer <a class="yt-timestamp" data-t="00:42:57">[00:42:57]</a>. The key enabler for this is dramatically improved "connectivity" between these dies, allowing for high bandwidth and low energy transfer of data <a class="yt-timestamp" data-t="00:43:28">[00:43:28]</a>. Nvidia's Blackwell chip, for example, uses a silicon interposer to connect two dies <a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>.

This new era, dubbed "SyMoore" by Synopsys, combines systemic complexity with the ambition of Moore's Law, focusing on multiplying performance through architectural innovation rather than just linear additions in transistor count <a class="yt-timestamp" data-t="00:44:57">[00:44:57]</a>. It's about optimizing the entire system, from software down to the transistor level <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>.

### Economic Decisions in Chip Design

Beyond technical feasibility, chip design decisions are increasingly driven by economics, referred to as "techonomics" <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. Factors like the cost of manufacturing a chip for a specific application (e.g., a phone versus a data center AI chip) influence architectural choices, such as how far to push angstrom-scale manufacturing versus multi-die architectures <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>.

### Expansion to System Companies

The importance of silicon has grown such that many non-semiconductor companies now design their own chips <a class="yt-timestamp" data-t="00:59:01">[00:59:01]</a>. Fifteen years ago, nearly 100% of Synopsys's revenue came from semiconductor companies; today, 45% comes from "system companies" – end-market OEMs like automotive manufacturers who are developing or architecting their own electronics <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>. This shift is driven by a "market pull" for specialized computing solutions and a recognition that custom silicon is key to competitive advantage in the [[AI era | AI era]] <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>.

## The Future of EDA: Simulation and Multiphysics

Synopsys's acquisition of Ansys, a leader in simulation and analysis, underscores the future direction of EDA <a class="yt-timestamp" data-t="01:04:11">[01:04:11]</a>. This strategic move addresses two critical areas:

1.  **Deep Core Business**: To tackle the challenges of advancing [[the_future_of_semiconductor_design_and_simulation | Moore's Law]], future chip design requires addressing not only electronics but also deep physics, including thermal and structural analysis <a class="yt-timestamp" data-t="01:04:08">[01:04:08]</a>. Ansys's expertise complements Synopsys's in this area.
2.  **System-Level Design**: As system companies increasingly design complex products with integrated electronics and mechanical components (e.g., cars), there's a need for "multiphysics" simulation <a class="yt-timestamp" data-t="01:04:34">[01:04:34]</a>. This enables the creation of digital twins of entire systems, allowing for comprehensive simulation upfront, reducing the need for expensive and time-consuming physical testing <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>.

The ability to accurately simulate complex physical interactions is becoming paramount. [[The future of semiconductor design and simulation | Simulation]] is further accelerated by compute advancements and [[impact_of_ai_in_electronic_design_automation | AI techniques]], opening doors for even more applications <a class="yt-timestamp" data-t="01:08:41">[01:08:41]</a>.

## Synopsys's Unique Position and Culture

Synopsys's success is attributed to its "cumulative learning" over decades, fostered by a culture of trust and collaboration <a class="yt-timestamp" data-t="00:56:58">[00:56:58]</a>. The company benefits from having long-serving employees who accumulate vast knowledge, continuously rejuvenating itself with new talent and approaches <a class="yt-timestamp" data-t="01:09:32">[01:09:32]</a>. A consistent passion for innovation drives the company, with engineers tackling the "most complex things known for humankind" <a class="yt-timestamp" data-t="01:11:23">[01:11:23]</a>. This blend of experience, continuous learning, and a relentless pursuit of future possibilities, often described as "only the paranoia survive," defines Synopsys <a class="yt-timestamp" data-t="01:10:06">[01:10:06]</a>.

The company also recognizes its growing societal responsibility as a central player in the global technology ecosystem, acknowledging the broader implications of its work on geopolitics and climate change <a class="yt-timestamp" data-t="01:12:40">[01:12:40]</a>. As leaders, they believe in using their understanding to act responsibly, embodying the principle: "they who have the brains to understand should have the courage to act" <a class="yt-timestamp" data-t="01:14:22">[01:14:22]</a>.