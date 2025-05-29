---
title: Comparison between RISC and CISC architectures
videoId: Y8guMe665RE
---

From: [[acquiredfm]] <br/> 

The world of CPUs is fundamentally shaped by two primary instruction set architectures: Complex Instruction Set Computer (CISC) and Reduced Instruction Set Computer (RISC) <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. Understanding their origins, characteristics, and historical trajectories is key to comprehending the evolution of computing.

## What is a CPU?
A CPU (Central Processing Unit) is described as the "digital brain of every modern electronic device" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. It is responsible for running complex software, operating systems, and applications found in devices ranging from televisions and thermostats to cars and phones <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a> <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

## Complex Instruction Set Computer (CISC)
CISC architectures, such as the x86 or Motorola 68000, were characterized by having "lots and lots and lots of instructions" <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a> <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.

### Characteristics of CISC:
*   **Complex Instructions:** A single instruction in CISC could perform multiple operations across several clock cycles <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. This means transistors run more than they "probably should" <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>, leading to higher power consumption <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Software Reliance & "Baggage":** Early software was written to rely on these complex instructions, meaning later architectures had to carry forward this "baggage" for compatibility <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a> <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   **Inefficient Code:** Compilers, which translate higher-level programming languages (like Fortran, Pascal, C, C++) into lower-level instructions, would utilize these heavy instructions, resulting in "heavier and more inefficient code" <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a> <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   **Larger Memory Footprints:** CISC designs generally required larger memory footprints for programs <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

### CISC Dominance in the PC Era:
Despite RISC's perceived advantages, CISC, specifically the x86 architecture, dominated the PC era <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a> <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. This was largely due to IBM's decision in 1981 to use an Intel 8086 processor and Microsoft's DOS for their IBM PC <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a> <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. This "open" platform allowed for clones and fostered an ecosystem where software (e.g., Lotus 1-2-3, later Windows) was optimized for x86 <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a> <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. The principle that "a CPU is only as good as the software that's written on it" was critical <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

## Reduced Instruction Set Computer (RISC)
RISC architectures were conceived by professors at the University of California, Berkeley, and focused on "simple movements" or instructions <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a> <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. Early RISC processors included MIPS <a class="yt-timestamp" data-t="00:12:58">[00:12:58]</a>.

### Characteristics of RISC:
*   **Simple Instructions:** Examples include basic operations like "add" or "subtract" <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>. Each instruction is designed to run in a single clock cycle <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Efficiency and Lower Power:** Simpler instructions, when combined efficiently, lead to lower power consumption <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a> <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. This was a key advantage, especially when running off a battery <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a> <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Smaller Memory Footprint:** RISC machines could fit programs into smaller memory footprints, which was beneficial when memory was expensive <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

### [[history_and_evolution_of_arm_architecture | ARM]]'s Rise as a RISC Architecture:
[[history_and_evolution_of_arm_architecture | ARM]] was founded in the early 1990s and utilized a RISC-based approach <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>. Its initial success was in portable devices due to its low-power design, stemming from its work on the Apple Newton PDA <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a> <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

[[history_and_evolution_of_arm_architecture | ARM]]'s business model focused on licensing its designs and instruction set architecture (ISA) <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>. This "shared success model" involved a modest upfront licensing fee and royalties on shipped products <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>. This contrasted with vertically integrated chip companies of the time <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>.

Key milestones for [[history_and_evolution_of_arm_architecture | ARM]]:
*   **Mobile Phones:** [[history_and_evolution_of_arm_architecture | ARM]] became the de facto standard in mobile phones, starting with Texas Instruments' baseband chips for Nokia's 2G GSM phones in the mid-1990s <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a> <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.
*   **iPod:** The first iPod, released in the early 2000s, was based on [[history_and_evolution_of_arm_architecture | ARM]] <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>.
*   **iPhone and Android:** The decision to use [[history_and_evolution_of_arm_architecture | ARM]] as the processor inside the iPhone, despite Intel's x86 Atom being considered, was a "key design win" <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a> <a class="yt-timestamp" data-t="00:35:15">[00:35:15]</a>. This was followed by the adoption of [[history_and_evolution_of_arm_architecture | ARM]] by the Android ecosystem (Samsung, MediaTek, Qualcomm) <a class="yt-timestamp" data-t="00:36:22">[00:36:22]</a>.
*   **Software Compatibility:** [[history_and_evolution_of_arm_architecture | ARM]] strictly maintains its ISA, not allowing custom instructions that could break software compatibility <a class="yt-timestamp" data-t="00:42:25">[00:42:25]</a>. This ensures that software developers can write programs that run broadly across [[history_and_evolution_of_arm_architecture | ARM]]-based devices <a class="yt-timestamp" data-t="00:42:19">[00:42:19]</a>.

## Current Landscape and Future Trends
In the present [[semiconductor industry | semiconductor industry]], only two main CPU architectures remain: x86 and [[history_and_evolution_of_arm_architecture | ARM]] <a class="yt-timestamp" data-t="00:47:13">[00:47:13]</a>.

### Factors favoring [[history_and_evolution_of_arm_architecture | ARM]]:
*   **Open Model:** [[history_and_evolution_of_arm_architecture | ARM]]'s open licensing model allows its products to be built by "any fab by any chip company," unlike x86 which is primarily built by Intel and AMD <a class="yt-timestamp" data-t="00:50:29">[00:50:29]</a>.
*   **Power Efficiency:** Power efficiency is "extremely important" in [[arms_adoption_in_data_centers_and_ai_applications | data centers]] due to massive workloads like general-purpose compute and AI models <a class="yt-timestamp" data-t="00:47:34">[00:47:34]</a>. [[history_and_evolution_of_arm_architecture | ARM]]'s low-power architecture provides a significant advantage <a class="yt-timestamp" data-t="00:47:52">[00:47:52]</a>.
*   **Customization (SOCs):** Hyperscalers like Microsoft, Google, and AWS can build custom Systems-on-Chip (SOCs) with [[history_and_evolution_of_arm_architecture | ARM]] <a class="yt-timestamp" data-t="00:51:41">[00:51:41]</a>. This allows for tailored designs with custom memory, storage, or accelerators, optimizing total cost of ownership (TCO) and driving innovation <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>. Such customization is difficult with x86 <a class="yt-timestamp" data-t="00:52:41">[00:52:41]</a>.
*   **Software Ecosystem:** A massive amount of software innovation has occurred on [[history_and_evolution_of_arm_architecture | ARM]] <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>, with over 20 million developers <a class="yt-timestamp" data-t="00:49:25">[00:49:25]</a>.
*   **AI Workloads:** [[history_and_evolution_of_arm_architecture | ARM]] is positioned to be central to AI compute, whether in [[arms_adoption_in_data_centers_and_ai_applications | data centers]], automobiles, smartphones, or wearables <a class="yt-timestamp" data-t="00:57:58">[00:57:58]</a>. The need for compute is "almost unabated" due to the benefits of AI <a class="yt-timestamp" data-t="00:57:46">[00:57:46]</a>.
*   **GPU Integration:** Accelerated computing with GPUs is seen as "fantastic for [[history_and_evolution_of_arm_architecture | ARM]]" because it indicates a need for more compute that integrates both base and accelerated components <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>. For instance, [[impact_of_cuda_and_nvidias_software_ecosystem | NVIDIA]]'s Grace Blackwell systems integrate [[history_and_evolution_of_arm_architecture | ARM]] CPUs with GPUs, offering architectural innovation not possible with x86 <a class="yt-timestamp" data-t="00:53:04">[00:53:04]</a>.
*   **Inference at the Edge:** While training primarily occurs in [[arms_adoption_in_data_centers_and_ai_applications | data centers]], inference (running AI applications) will happen on a vast number of edge devices like wearables and headsets <a class="yt-timestamp" data-t="01:01:27">[01:01:27]</a>. These devices require low-power solutions, making [[history_and_evolution_of_arm_architecture | ARM]] a natural fit <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>.

> "A CPU is only as good as the software that's written on it and how long that software survives." <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>
>
> "Once the flywheel of software gets built onto a certain architecture, it's very very difficult for a, if you're developing a new piece of hardware, to say well I'll choose one of the ones I just mentioned because there really isn't a software story around it." <a class="yt-timestamp" data-t="00:44:48">[00:44:48]</a>

The decline of investment in new CPU startups after the dot-com era meant that fewer alternative architectures emerged <a class="yt-timestamp" data-t="00:45:40">[00:45:40]</a> <a class="yt-timestamp" data-t="00:46:41">[00:46:41]</a>. This left x86 and [[history_and_evolution_of_arm_architecture | ARM]] as the dominant choices, with [[history_and_evolution_of_arm_architecture | ARM]] benefiting from its efficiency and adaptable licensing model <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.