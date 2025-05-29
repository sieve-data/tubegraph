---
title: Role of Electronic Design Automation EDA in Chip Design
videoId: uSchEDY6y20
---

From: [[acquiredfm]] <br/> 

Electronic Design Automation (EDA) is a crucial field that provides the software tools necessary for chip designers to create and optimize integrated circuits <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Synopsys is an $80 billion company that makes this software, operating as one of the two major players, alongside Cadence Design Systems <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. EDA can be thought of as productivity software for chip designers, akin to Microsoft Excel or Figma for that profession <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The complexity of modern chip design is largely handled by EDA software, making entirely new types of chips possible <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

EDA serves as essential infrastructure for the [[AI and Machine Learning in EDA | AI era]] and the current semiconductor innovation <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Without EDA and the software's incredible optimizations for chip designers, [[AI and Machine Learning in EDA | AI applications]] would not be possible <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Synopsys even uses [[AI and Machine Learning in EDA | AI]] to design the software itself <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Genesis of Synopsys and EDA

Art de Geus, the founding CEO of Synopsys, is a pioneer in the [[development_and_impact_of_the_semiconductor_industry | semiconductor industry]] <a class="yt-timestamp" data-t="01:29:10">[01:29:10]</a>. He founded the company 37 years ago, evolving it into an essential part of the [[the_technological_ecosystem_in_the_semiconductor_industry | semiconductor value chain and ecosystem]] <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. Synopsys was born out of a spin-out from General Electric (GE) in the mid-1980s, a period marked by the worst downturn in semiconductor history <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>. GE had developed innovative design tools, including "synthesis," which became the foundation for Synopsys <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. The spin-out, involving seven people, was supported by GE financially and with technology, a rare successful corporate venture <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.

### Pre-EDA Chip Design

Before synthesis and EDA software, chip design involved manual processes. Designers would typically work at a functional level, choosing gates to implement complex digital math functions <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>. This was often done on paper or with schematic entry tools <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. The primary metrics for "goodness" were the number of gates (fewer being better) and speed, determined by the longest path through the design <a class="yt-timestamp" data-t="10:05:00">[10:05:05]</a>.

### The Innovation of Synthesis

Synthesis allowed for the automatic design of circuits, which was revolutionary <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. Synopsys's early program, "Socrates," demonstrated astounding results, creating circuits that were 30% smaller (fewer gates) and 30% faster than manual designs in a matter of hours <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>. This marked a shift from "computer-aided design" (CAD), where the computer merely helped human designers, to "electronic design automation" (EDA), where software actively created and optimized designs <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>.

Initially, there was a "lack of trust" from engineers who wanted to understand every change made by the software, similar to the initial resistance to [[AI and Machine Learning in EDA | AI tools]] <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>. However, the superior outcomes led to widespread adoption <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>.

> "We're the only ones that have license to kill. Because license to kill means we can actually change a circuit and that was completely taboo before, if a tool did that, means they had put some bugs in it." <a class="yt-timestamp" data-t="17:10:00">[17:10:00]</a>

## EDA's Role in Moore's Law and Semiconductor Innovation

EDA is fundamental to sustaining Moore's Law. It's not a natural law but a continuous achievement driven by companies like Synopsys <a class="yt-timestamp" data-t="29:27:00">[29:27:00]</a>. Staying on this exponential curve requires constant innovation and collaboration with leading chip designers and foundries <a class="yt-timestamp" data-t="31:08:00">[31:08:00]</a>.

Synopsys works closely with customers, who provide critical feedback that drives continuous improvement <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>. This collaborative model, where customers become "parents of the tool," has been key to Synopsys's success and ability to stay at the state-of-the-art <a class="yt-timestamp" data-t="15:47:00">[15:47:00]</a>.

## Addressing Advanced Challenges and Systemic Complexity

The [[development_and_impact_of_the_semiconductor_industry | semiconductor industry]] has faced increasing [[challenges_and_successes_within_the_semiconductor_market | complexities]] in chip design:

*   **From Enablement to Co-Invention**: Historically, Synopsys received input from foundries (like [[the_role_and_impact_of_tsmc_and_semiconductors | TSMC]], Samsung, Intel, GF) for "enablement" within their products <a class="yt-timestamp" data-t="36:31:00">[36:31:00]</a>. In the last 5-6 years, this has evolved into hundreds of Synopsys engineers working directly with foundries during process technology development <a class="yt-timestamp" data-t="37:03:00">[37:03:00]</a>. This "Design Technology Co-Optimization" (DTCO) is necessary because enablement alone is no longer sufficient to push the limits of physics and manufacturing <a class="yt-timestamp" data-t="35:57:00">[35:57:00]</a>.
*   **Physics Limits**: The industry is now bumping up against the fundamental limits of physics <a class="yt-timestamp" data-t="39:25:00">[39:25:00]</a>. This includes issues like thermal generation, warpage, and cracking when billions of transistors are jammed into a small area <a class="yt-timestamp" data-t="38:47:00">[38:47:00]</a>. EDA software must account for these multi-physics effects during the design stage <a class="yt-timestamp" data-t="40:09:00">[40:09:00]</a>.
*   **Specialized Hardware**: To achieve higher performance, the industry is moving towards developing hardware for specific workloads rather than general-purpose processors <a class="yt-timestamp" data-t="40:42:00">[40:42:00]</a>. This led to the rise of specialized accelerators like GPUs <a class="yt-timestamp" data-t="41:31:00">[41:31:00]</a> and is increasingly seen in software-defined architectures <a class="yt-timestamp" data-t="42:24:00">[42:24:00]</a>.
*   **Multi-Die Architectures**: When single chips hit physical limits, the solution is to split functionality across multiple dies (chips) brought closely together <a class="yt-timestamp" data-t="42:55:00">[42:55:00]</a>. This "advanced packaging" uses interposers to connect chips (like the [[the_role_and_impact_of_tsmc_and_semiconductors | Nvidia Blackwell]] chip) <a class="yt-timestamp" data-t="43:37:00">[43:37:00]</a>. The key enabler here is improved connectivity between dies, allowing for dramatic reductions in distance and increases in bandwidth and energy efficiency <a class="yt-timestamp" data-t="43:28:00">[43:28:00]</a>. This approach contributes to what Synopsys calls "Symore" – systemic complexity with a Moore's Law exponential ambition <a class="yt-timestamp" data-t="44:57:00">[44:57:00]</a>.
*   **Economic Decisions**: Beyond technical feasibility, design choices are now heavily influenced by economics. For example, a chip that might cost $15,000 to produce may not be viable for a phone <a class="yt-timestamp" data-t="49:09:00">[49:09:00]</a>. EDA helps navigate these n-dimensional trade-offs, considering cost, performance, power, and area <a class="yt-timestamp" data-t="49:48:00">[49:48:00]</a>.

### The Role of [[AI and Machine Learning in EDA | AI and Machine Learning in EDA]]

[[AI and Machine Learning in EDA | AI and machine learning]] algorithms are increasingly used in EDA for massive optimization problems <a class="yt-timestamp" data-t="19:48:00">[19:48:00]</a>. While human designers struggled with complexity, [[AI and Machine Learning in EDA | AI]] can optimize billions of transistors for placement, routing, performance, and power <a class="yt-timestamp" data-t="19:54:00">[19:54:00]</a>.

EDA's [[AI and Machine Learning in EDA | AI]] differs from generative [[AI and Machine Learning in EDA | AI]] in that it focuses on optimization for a guaranteed outcome with "absolute correctness in functionality," given the high cost of manufacturing a faulty chip <a class="yt-timestamp" data-t="21:58:00">[21:58:00]</a>. Synopsys pioneered [[AI and Machine Learning in EDA | AI for EDA]] starting in 2017, and it is now used by dozens of customers in production <a class="yt-timestamp" data-t="20:54:00">[20:54:00]</a>.

## Expansion Beyond Semiconductors

Synopsys's customer base has expanded significantly. Fifteen years ago, almost 100% of its revenue came from [[development_and_impact_of_the_semiconductor_industry | semiconductor companies]] <a class="yt-timestamp" data-t="01:02:01">[01:02:01]</a>. Today, 45% of its $6 billion revenue comes from "system companies" – End Market OEMs that develop finished products rather than selling chips directly <a class="yt-timestamp" data-t="01:02:04">[01:02:04]</a>. This is driven by a strong incentive for more companies to design their own silicon to gain a competitive edge <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>. Even automotive OEMs that don't intend to design chips use Synopsys software to architect their car's electronics system digitally <a class="yt-timestamp" data-t="01:02:46">[01:02:46]</a>.

This shift signifies an "End Market pull" complementing the traditional "technology push," accelerating innovation <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>.

### [[Acquisition of Ansys and Future of Simulation in EDA | Acquisition of Ansys]]

In January, Synopsys announced the [[acquisition_of_ansys_and_future_of_simulation_in_eda | acquisition of Ansys]], a leader in multi-physics simulation and analysis <a class="yt-timestamp" data-t="01:03:41">[01:03:41]</a>. This acquisition serves two main purposes:

1.  **Deep in Core Business**: Addresses the challenge in Moore's Law of combining electronics with deep physics (thermal, structural) for device design on a chip <a class="yt-timestamp" data-t="01:04:02">[01:04:02]</a>.
2.  **System-Level Design**: Enables system companies (like automotive OEMs) to design and simulate entire products (e.g., a car) with a "digital twin," integrating electronics, mechanical, and other physics <a class="yt-timestamp" data-t="01:04:31">[01:04:31]</a>.

This strategic move positions Synopsys as a "design solution from Silicon to system," delivering an engineering platform for the future <a class="yt-timestamp" data-t="01:05:27">[01:05:27]</a>. Simulation is becoming increasingly critical as physical testing of complex, interconnected devices becomes too expensive and impractical <a class="yt-timestamp" data-t="01:07:50">[01:07:50]</a>. Accelerated compute and [[AI and Machine Learning in EDA | AI techniques]] further enhance simulation capabilities, opening doors for more applications <a class="yt-timestamp" data-t="01:08:32">[01:08:32]</a>.

## Enduring Principles and Future Outlook

Despite rapid technological advancements, the core passion for innovation and pushing the boundaries of what's possible remains a constant within Synopsys and the EDA industry <a class="yt-timestamp" data-t="01:11:02">[01:11:02]</a>.

However, the world has become significantly more complex, with globalization, geopolitical stress fields, and societal responsibilities becoming central to a company's role <a class="yt-timestamp" data-t="01:12:29">[01:12:29]</a>. Synopsys now faces questions about its position in a world grappling with issues like energy utilization for [[AI and Machine Learning in EDA | AI]] and climate change <a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>.