---
title: Emerging Trends in Memory and Chip Design
videoId: pE3KKUKXcTM
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The semiconductor industry, responsible for the design and manufacturing of chips, is characterized by immense complexity and specialization <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>, <a class="yt-timestamp" data-t="01:00:14">[01:00:14]</a>. This article explores emerging trends in memory and chip design, focusing on architectural advancements, the role of AI in the design process, and the critical importance of memory innovation, as discussed in a recent podcast episode. 

## The Evolving Landscape of Chip Design

Chip design is facing a multifaceted evolution, driven by the demand for more powerful and efficient processing, particularly for AI applications.

### The "Search Space" and AI's Role in Design
The design of modern chips, such as NVIDIA's Blackwell with approximately 220 billion transistors <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>, involves navigating an almost infinitely large "search space" <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>. This complexity arises from the vast number of permutations in arranging transistors and connecting them across multiple metal layers <a class="yt-timestamp" data-t="01:00:41">[01:00:41]</a>.

AI is beginning to play a role in tackling this challenge. Examples include:
*   NVIDIA's and Google's AI layout tools for arranging circuits within chip sections <a class="yt-timestamp" data-t="00:58:39">[00:58:39]</a>.
*   Reinforcement learning (RL) design techniques and various simulation tools <a class="yt-timestamp" data-t="00:58:49">[00:58:49]</a>.
These AI applications, even older RL techniques, are showing single-digit to low double-digit advantages <a class="yt-timestamp" data-t="00:59:26">[00:59:26]</a>. The introduction of generative AI could further revolutionize the industry, though data availability remains a significant hurdle <a class="yt-timestamp" data-t="00:59:38">[00:59:38]</a>. The goal is to optimize for "intelligence per picojoule" <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>.


### Architectural Innovations Beyond Process Nodes
Significant performance gains, potentially up to 100x, are possible through architectural advancements, even without further process node shrinks <a class="yt-timestamp" data-t="01:02:03">[01:02:03]</a>. A primary target for optimization is data movement, which consumes the vast majority of power on chips like the H100, rather than actual computation <a class="yt-timestamp" data-t="01:01:19">[01:01:19]</a>, <a class="yt-timestamp" data-t="01:01:35">[01:01:35]</a>. Key areas for architectural improvement include:
*   Minimizing data movement (networking and memory) <a class="yt-timestamp" data-t="01:01:39">[01:01:39]</a>, <a class="yt-timestamp" data-t="01:01:58">[01:01:58]</a>.
*   More efficient Arithmetic Logic Unit (ALU) designs <a class="yt-timestamp" data-t="01:01:26">[01:01:26]</a>.
*   Power delivery, system design, and chip-to-chip networking <a class="yt-timestamp" data-t="01:03:13">[01:03:13]</a>.

The number of people designing chips in the US has not significantly grown, but output per individual has soared due to Electronic Design Automation (EDA) tooling <a class="yt-timestamp" data-t="01:02:21">[01:02:21]</a>, <a class="yt-timestamp" data-t="01:02:32">[01:02:32]</a>. Further integration of AI into these tools presents a major opportunity <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>.

## Memory: A Critical Frontier

Memory technology is identified as a crucial area for innovation and a potential bottleneck.

### Current Limitations and Stagnation
The memory industry largely followed Moore's Law until around 2012, after which gains became very incremental <a class="yt-timestamp" data-t="02:08:06">[02:08:06]</a>. While logic density and cost continue to improve at over 10-15% CAGR, memory has seen "really bad" progress since 2012 <a class="yt-timestamp" data-t="02:08:23">[02:08:23]</a>. High Bandwidth Memory (HBM) itself exists due to limitations in traditional DRAM technology <a class="yt-timestamp" data-t="02:07:28">[02:07:28]</a>.

### Opportunities for Breakthroughs
Despite being considered a commodity, breaking through current memory limitations could "change the world" <a class="yt-timestamp" data-t="02:07:46">[02:07:46]</a>. Memory integration with accelerators is a key area of focus <a class="yt-timestamp" data-t="02:08:34">[02:08:34]</a>. However, entrepreneurship in this space is challenging due to the need for massive scale manufacturing and an industry not conducive to custom memory devices or novel materials <a class="yt-timestamp" data-t="02:08:39">[02:08:39]</a>, <a class="yt-timestamp" data-t="02:08:48">[02:08:48]</a>.

## Process Node Advancements and Economic Viability

Process node scaling remains important, though its nature and economic justification are evolving.

### Benefits of Node Shrinks
Moving to new process nodes (e.g., from 5nm to 3nm) offers benefits beyond just individual transistor power efficiency <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>. While SRAM doesn't scale well and logic scaling might be around 30%, leading to an overall power saving per transistor of about 20% <a class="yt-timestamp" data-t="00:45:28">[00:45:28]</a>, improved data locality significantly enhances power efficiency <a class="yt-timestamp" data-t="00:45:44">[00:45:44]</a>. Fitting more of a computation (like a large matrix multiplication) on a single chip reduces off-chip data movement, saving power <a class="yt-timestamp" data-t="00:45:57">[00:45:57]</a>. AI applications, in particular, benefit greatly from the power savings, higher density, and performance of new nodes <a class="yt-timestamp" data-t="00:46:05">[00:46:05]</a>.

### Economic Challenges and AI's Role
The economic viability of continually shrinking process nodes is a growing concern <a class="yt-timestamp" data-t="00:43:16">[00:43:16]</a>. Node transitions, like 5nm and 3nm, have taken three years, and their cost is immense <a class="yt-timestamp" data-t="00:43:33">[00:43:33]</a>. Apple, a major driver, only moved half its iPhone volume to 3nm initially and continued using 5nm for a significant portion for a fourth year, questioning the mobile industry's ability to fund future nodes alone <a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>, <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>. There's a strong argument that nodes like 2nm (N2) might not be economically viable without the "humongous demand" generated by AI <a class="yt-timestamp" data-t="00:44:55">[00:44:55]</a>, <a class="yt-timestamp" data-t="00:42:18">[00:42:18]</a>. AI makes future nodes like 1nm or A16 viable by providing the necessary market demand <a class="yt-timestamp" data-t="00:43:20">[00:43:20]</a>. It is projected that AI could consume 60-80% of advanced node capacity (like 2nm, A16, A14) by 2028 <a class="yt-timestamp" data-t="01:32:36">[01:32:36]</a>, <a class="yt-timestamp" data-t="01:32:40">[01:32:40]</a>.

## Interplay Between Hardware and AI Model Architecture

Hardware constraints and design choices significantly influence the optimal architecture for AI models.

### Hardware Influencing Optimal Models
The relationship between chips and AI models is not a one-way street; hardware has a "huge influence" on optimal model architecture <a class="yt-timestamp" data-t="01:04:54">[01:04:54]</a>. An optimal model for Google's TPUs, given certain cost and compute constraints, will be architecturally different from an optimal model for NVIDIA GPUs <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>. This extends to networking decisions and data center design [[data_center_energy_requirements_and_scaling]] <a class="yt-timestamp" data-t="01:05:13">[01:05:13]</a>. Differences can manifest in:
*   Level of sparsity and use of "experts" <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>
*   Arrangement of attention mechanisms [[ai_systems_and_planning_mechanisms]] <a class="yt-timestamp" data-t="01:06:11">[01:06:11]</a>
*   Whether a model is "wide" versus "tall" (D-mod vs. number of layers) <a class="yt-timestamp" data-t="01:06:17">[01:06:17]</a>

### Divergence of Architectures
Constraints can lead to divergent architectural paths. For example, Chinese AI models, potentially using chips like the H20 with different compute-to-memory bandwidth ratios, might evolve differently [[china_and_the_uss_race_in_ai_and_superintelligence]] <a class="yt-timestamp" data-t="01:05:40">[01:05:40]</a>. China's significant investment in compute-in-memory technologies could also drive unique architectures <a class="yt-timestamp" data-t="01:06:40">[01:06:40]</a>. If NVIDIA designs chips specifically for the Chinese market, these might diverge architecturally from their main offerings <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. Huawei's Ascend 910B, for instance, is architecturally distinct from GPUs or TPUs <a class="yt-timestamp" data-t="00:37:27">[00:37:27]</a>. This divergence is also seen in research focus; for example, state space models, potentially advantageous for video, image, and audio, receive immense interest in China [[metas_advancements_in_ai_technology_and_infrastructure]] <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>, <a class="yt-timestamp" data-t="01:08:25">[01:08:25]</a>, areas where China has strong capabilities, partly due to surveillance data <a class="yt-timestamp" data-t="01:08:38">[01:08:38]</a>, <a class="yt-timestamp" data-t="01:08:45">[01:08:45]</a>.

There's a self-fulfilling prophecy where research focuses on models like transformers that run well on existing high arithmetic intensity hardware (GPUs, TPUs) <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>. A theoretically better architecture might be impractical if it cannot efficiently utilize current hardware [[role_of_compute_in_ai_development]] <a class="yt-timestamp" data-t="01:09:58">[01:09:58]</a>.

## Future Outlook: Gains and Challenges

The future of chip design and memory holds immense potential but also faces significant data and complexity challenges.
*   **100x Gains Possible:** Architectural advancements alone, focusing on minimizing data movement and optimizing compute, could yield 100x gains in efficiency <a class="yt-timestamp" data-t="01:01:58">[01:01:58]</a>, <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>.
*   **The Largest Search Space:** Semiconductor design and manufacturing represent the largest search space of any human endeavor due to their complexity [[ai_scalability_and_breakthroughs]] <a class="yt-timestamp" data-t="01:00:09">[01:00:09]</a>.
*   **Need for Cross-Layer Innovation:** The highly siloed nature of the industry, with specialized knowledge often not documented or easily transferable (akin to a master-apprentice system <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>, <a class="yt-timestamp" data-t="00:57:18">[00:57:18]</a>), means that AI cannot easily "learn" semiconductors <a class="yt-timestamp" data-t="00:57:28">[00:57:28]</a>. Breakthroughs will require stretching across abstraction layers <a class="yt-timestamp" data-t="00:58:20">[00:58:20]</a> and leveraging AI to experiment at much higher velocities <a class="yt-timestamp" data-t="00:58:31">[00:58:31]</a>.
*   **Outdated Infrastructure:** Many semiconductor fabs run on old operating systems like Windows XP for tool control, and chip design tools may use outdated CentOS versions <a class="yt-timestamp" data-t="00:57:46">[00:57:46]</a>, <a class="yt-timestamp" data-t="00:57:53">[00:57:53]</a>, indicating areas ripe for modernization, albeit carefully, given the hyper-optimized yet "broken" nature of the tech stack <a class="yt-timestamp" data-t="00:58:03">[00:58:03]</a>, <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>.

The opportunity for innovation exists at every layer of the stack, with the potential to utilize AI to make processes more efficient and unlock further advancements [[innovations_and_challenges_in_ai_hardware]] <a class="yt-timestamp" data-t="02:09:10">[02:09:10]</a>.