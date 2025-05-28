---
title: DeepSeek and computational efficiency
videoId: Ii_7-wsTjLo
---

From: [[hu-po]] <br/> 

DeepSeek has gained significant attention for its advancements in artificial intelligence, particularly in achieving high performance with notable computational efficiency. This efficiency stems from a combination of algorithmic innovations, such as the use of Grouped Proximal Policy Optimization (GRPO), and meticulous engineering efforts, including low-level hardware optimizations <a class="yt-timestamp" data-t="01:17:40">[01:17:40]</a>.

## GRPO: A Key to Efficiency

DeepSeek's approach to achieving high performance, particularly in mathematical reasoning, heavily relies on a variant of Proximal Policy Optimization (PPO) called Grouped Proximal Policy Optimization (GRPO) <a class="yt-timestamp" data-t="06:10:19">[06:10:19]</a>.

### PPO vs. GRPO

The core difference between PPO and GRPO lies in how they handle observations and value estimation <a class="yt-timestamp" data-t="07:01:02">[07:01:02]</a>.
*   **PPO:** Samples a single observation (`o`) and uses a value function (`V(s)`) to estimate the expected reward from a given state <a class="yt-timestamp" data-t="07:48:49">[07:48:49]</a> <a class="yt-timestamp" data-t="19:33:57">[19:33:57]</a>.
*   **GRPO:** Samples *multiple* observations (`G` of them) from the old policy (`Pi Theta old`). Instead of relying on a separate learned value function, GRPO computes the advantage function based on a group reward score, effectively performing a Monte Carlo estimate of the value function <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a> <a class="yt-timestamp" data-t="20:33:00">[20:33:00]</a> <a class="yt-timestamp" data-t="20:55:00">[20:55:00]</a>.

### The Advantage Function and Value Network

In reinforcement learning, the advantage function (`A(s,a)`) measures how much better an action (`a`) is at a given state (`s`) compared to the average expected value of that state <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>. PPO typically employs a separate value network to compute this, which is often another neural network of comparable size to the policy model <a class="yt-timestamp" data-t="19:48:00">[19:48:00]</a>. This separate network introduces a "substantial memory and computational burden" <a class="yt-timestamp" data-t="19:53:00">[19:53:00]</a> <a class="yt-timestamp" data-t="20:21:00">[20:21:00]</a>.

GRPO's key innovation is removing this value network <a class="yt-timestamp" data-t="20:36:00">[20:36:00]</a>. By sampling multiple outputs and analyzing their rewards, GRPO approximates the value function, thus reducing the [[ai_algorithms_and_computational_constraints | computational constraints]] and memory requirements associated with running two distinct networks <a class="yt-timestamp" data-t="20:55:00">[20:55:00]</a> <a class="yt-timestamp" data-t="21:10:00">[21:10:00]</a>.

### Historical Context and Instability

The use of a learned value function in PPO, developed around 2015, was influenced by the contemporary advancements in Generative Adversarial Networks (GANs). The architecture of GANs, with a generator and a discriminator, mirrored the policy network and value network in reinforcement learning <a class="yt-timestamp" data-t="21:51:00">[21:51:00]</a>. However, this dual-network setup in GANs and PPO led to training instabilities, as balancing the two networks could be challenging <a class="yt-timestamp" data-t="22:45:00">[22:45:46]</a>. GRPO bypasses this by eliminating the need for a separate value network, potentially offering more stable and efficient training <a class="yt-timestamp" data-t="22:56:00">[22:56:00]</a>.

## Beyond the Algorithm: DeepSeek's Engineering Prowess

While GRPO is a significant algorithmic contribution, DeepSeek's overall [[compute_efficiency_in_language_models | compute efficiency in language models]] is attributed to an accumulation of many "little tricks" and a strong engineering focus <a class="yt-timestamp" data-t="01:08:41">[01:08:41]</a> <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

### Precision and Custom Hardware Optimization

DeepSeek has demonstrated "hardcore hacks" related to numerical precision, notably using a custom `f8 E4 M3` tensor type, allowing models to run at much lower precision <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>. Reducing data types, such as from `fp32` to `fp8`, significantly increases computational throughput (e.g., from 67 TeraFLOPS to 4,000 TeraFLOPS for fp8), enabling faster training <a class="yt-timestamp" data-t="01:22:57">[01:22:57]</a>.

Furthermore, DeepSeek engineers showcased exceptional low-level programming skills, even writing better GPU code using Nvidia's PTX Assembly Language than Nvidia's own engineers <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a> <a class="yt-timestamp" data-t="01:00:32">[01:00:32]</a>. They were able to optimize H800 chips, which typically have nerfed interconnect bandwidth compared to H100s, by directly programming the processing units to manage cross-chip communications, effectively turning H800s into H100s for their specific needs <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a> <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a>. This allowed them to overcome hardware limitations imposed by export controls <a class="yt-timestamp" data-t="01:01:22">[01:01:22]</a>.

### Data-Centric Approach

A key philosophy underpinning DeepSeek's success, and AI development in general, is that the algorithm itself is often less important than the quality of the data and the engineering effort <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a> <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. The iterative nature of AI development, where different models and techniques might show conflicting results, suggests that focusing on data and robust engineering yields more consistent progress <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a> <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>.

## Implications for AI Development

DeepSeek's achievements have several significant implications for the broader field of AI.

### Process vs. Outcome Supervision

DeepSeek's findings challenge previous conclusions regarding process versus outcome supervision in reinforcement learning <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. While some earlier research suggested that process supervision (providing feedback at every step) was superior, DeepSeek found that process reward was "unsuccessful," citing challenges in explicit definition, retraining reward models, and pipeline complication <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>. This highlights the variability of results in AI research and the importance of not "over-indexing on any one individual result" <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>.

### Robotics and Simulation

The success of reinforcement learning with "long-horizon generated data" (e.g., self-play in Go, simulated math problems) suggests a shift away from reliance on "imitation learning from teleoperation data" <a class="yt-timestamp" data-t="00:55:31">[00:55:31]</a>. For robotics, this implies that training models extensively in simulation, rather than through real-world teleoperation, might be the more effective path forward <a class="yt-timestamp" data-t="00:56:27">[00:56:27]</a> <a class="yt-timestamp" data-t="00:57:01">[00:57:01]</a>. This approach mirrors how superhuman Go performance was achieved entirely in simulation <a class="yt-timestamp" data-t="00:56:55">[00:56:55]</a>.

### Cost Savings and Accessibility

DeepSeek's ability to achieve significant performance with greater efficiency means that powerful models can potentially be developed at a lower cost <a class="yt-timestamp" data-t="01:08:41">[01:08:41]</a>. This could make advanced AI development more accessible, even if it still involves substantial financial investment (e.g., a full GRPO run on a large dataset and powerful GPUs could cost over $1,300) <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>. The open-sourcing of DeepSeek's methods, such as Hugging Face's Open R1 reproduction, allows other companies and researchers to leverage these innovations, accelerating progress across the field <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a> <a class="yt-timestamp" data-t="01:28:44">[01:28:44]</a>.