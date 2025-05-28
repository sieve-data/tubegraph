---
title: Open Source Deep Seek and Deep Reinforcement Learning
videoId: Ii_7-wsTjLo
---

From: [[hu-po]] <br/> 

Deep Seek is an open-source model that has gained attention in the field of [[ai_and_reinforcement_learning | AI and Reinforcement Learning]], particularly for its mathematical and coding capabilities <a class="yt-timestamp" data-t="02:34:37">[02:34:37]</a>. Its release has sparked discussions about the importance of algorithms, data, and engineering effort in [[stateoftheart_in_reinforcement_learning | state-of-the-art]] AI development <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>, <a class="yt-timestamp" data-t="18:40:42">[18:40:42]</a>.

## Deep Seek Math and GRPO

Deep Seek's success in mathematics is largely attributed to its use of the **Group-Reward Proximal Policy Optimization (GRPO)** algorithm, a variant of the widely known Proximal Policy Optimization (PPO) <a class="yt-timestamp" data-t="06:08:10">[06:08:10]</a>.

### GRPO vs. PPO: Key Differences

While GRPO and PPO share very similar objectives, several distinctions set GRPO apart <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>:

*   **Observation Sampling**: In PPO, a single observation (`o`) is sampled <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>. GRPO, however, samples a *group* of `G` observations (`o_i`) from the policy <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>. This means that for each question, GRPO generates multiple possible answers or "completions" <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>.
*   **Policy Ratio**: Both algorithms use a ratio of the current policy (`Pi Theta`) to an old policy (`Pi Theta old`) to determine if progress is being made <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>. If the new policy has a higher probability of picking the correct token, progress is indicated <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>. A clipping function is applied to this ratio to prevent extreme values <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.
*   **KL Divergence**: A Beta-weighted Kullback-Leibler (KL) Divergence term is included to prevent the policy from drifting too far from a reference policy (P_ref), often an SFT model <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>, <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>. This ensures that while the policy updates, it doesn't "scramble" itself too much <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>.
*   **Advantage Function**:
    *   In PPO, the advantage function (`A_f`) is typically computed using **Generalized Advantage Estimation (GAE)**, which relies on rewards and a *learned value function* (`V(s)`) <a class="yt-timestamp" data-t="19:35:00">[19:35:00]</a>. This value function is often another [[deep_learning_and_neural_networks | neural network]] of comparable size to the policy model, introducing substantial memory and computational burden <a class="yt-timestamp" data-t="19:48:00">[19:48:48]</a>. The historical context for this approach dates back to 2015 with the rise of Generative Adversarial Networks (GANs), where a discriminator model (similar to a value network) complemented a generator (policy network) <a class="yt-timestamp" data-t="21:40:00">[21:40:00]</a>.
    *   GRPO's innovation, however, is to compute the advantage (`A_hat`) based on **group reward scores**, effectively removing the need for a separate value network <a class="yt-timestamp" data-t="20:36:00">[20:36:00]</a>, <a class="yt-timestamp" data-t="20:46:00">[20:46:00]</a>. This is likened to a Monte Carlo estimate of the value function <a class="yt-timestamp" data-t="20:55:00">[20:55:00]</a>. While this reduces computational overhead by eliminating a second network, it requires running the policy multiple times to sample the group of observations <a class="yt-timestamp" data-t="20:09:00">[20:09:00]</a>.

## Conflicting Research on Supervision

Deep Seek's findings on outcome supervision versus process supervision contradict previous research.

> [!NOTE] Outcome vs. Process Supervision
> Outcome supervision provides a reward only at the end of the output, while process supervision provides feedback at every step <a class="yt-timestamp" data-t="24:08:00">[24:08:00]</a>.

Ilya's paper, "Let's Verify Step by Step," concluded that process supervision was more effective <a class="yt-timestamp" data-t="24:21:00">[24:21:00]</a>. Deep Seek, however, found process reward to be "unsuccessful" due to challenges in explicit fine-grained step definition, annotation, and increased training pipeline complexity <a class="yt-timestamp" data-t="24:54:00">[24:54:00]</a>. This highlights that results can differ across studies, and no single algorithm or technique is universally superior <a class="yt-timestamp" data-t="25:16:00">[25:16:00]</a>. The speaker emphasizes that the algorithms are not the primary driver of progress, but rather the data and engineering effort <a class="yt-timestamp" data-t="18:40:42">[18:40:42]</a>.

## Hugging Face's Open R1 and Replication Challenges

Hugging Face, a champion of [[open_source_ai_models_and_accessibility | open-source AI]], released Open R1 as a reproduction of Deep Seek R1 <a class="yt-timestamp" data-t="26:31:00">[26:31:00]</a>. Open R1 leverages TRL (Transformer Reinforcement Learning), a library maintained by Hugging Face <a class="yt-timestamp" data-t="26:52:00">[26:52:00]</a>.

### Experiment Setup

The speaker attempted to replicate Deep Seek's GRPO training using Open R1, specifically on the `grpo.py` script <a class="yt-timestamp" data-t="27:39:00">[27:39:00]</a>.

*   **Base Model**: Qwen 7B, distilled from Deep Seek R1 <a class="yt-timestamp" data-t="31:14:00">[31:14:00]</a>. This process, known as knowledge distillation, involves a smaller model mimicking a larger, more intelligent model's outputs <a class="yt-timestamp" data-t="31:29:00">[31:29:00]</a>, <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>.
*   **Data Set**: AIMO Num Math dataset, originally 70,000 examples <a class="yt-timestamp" data-t="32:31:00">[32:31:00]</a>. To reduce costs for experimentation, the dataset size was cut down to approximately 2,000 examples <a class="yt-timestamp" data-t="34:08:00">[34:08:00]</a>.
*   **Hyperparameters**: The experiment involved sweeping different values for `beta` (controlling KL divergence importance), `temperature` (influencing randomness of model outputs), and `learning rate` <a class="yt-timestamp" data-t="28:12:00">[28:12:00]</a>.

> [!INFO] Deep Seek's Precision
> Deep Seek utilized a custom `f8 E4 M3` floating-point precision, a "hardcore hack" that allows for much lower precision computations and faster training compared to standard `bf16` or `fp32` <a class="yt-timestamp" data-t="32:03:00">[32:03:00]</a>, <a class="yt-timestamp" data-t="1:22:51">[1:22:51]</a>.

### Cost and Scale Limitations

Replicating the full Deep Seek training run is prohibitively expensive for individuals. An 8x H100 node costs approximately $24 per hour, and a full run on 70,000 data points would take 56 hours, totaling $1,300 per run <a class="yt-timestamp" data-t="33:51:00">[33:51:00]</a>. By reducing the dataset size, the speaker managed to complete a run in 42 minutes for $16 <a class="yt-timestamp" data-t="34:15:00">[34:15:00]</a>.

> [!NOTE] Hyperparameter Tuning on Smaller Models
> Large-scale AI labs often tune hyperparameters on smaller models or datasets before transferring them to full-sized models, as running full experiments for every hyperparameter combination would be prohibitively expensive <a class="yt-timestamp" data-t="37:53:00">[37:53:00]</a>.

The small-scale experiment, while confirming expected relationships between hyperparameters and metrics like KL divergence or reward standard deviation, was a tiny fraction of the actual training (e.g., 40 global steps vs. 8,000 in the paper) <a class="yt-timestamp" data-t="35:56:00">[35:56:00]</a>. Moreover, the evaluation was done on a hold-out set from the same distribution, not a separate benchmark, limiting the real-world applicability of the results <a class="yt-timestamp" data-t="36:46:00">[36:46:00]</a>.

### "Dependency Hell" and GPU Capacity

Attempts to pull in updates from Hugging Face's Open R1 repository led to "dependency hell" <a class="yt-timestamp" data-t="45:47:00">[45:47:00]</a>. The repository introduced new optimizations (e.g., dedicating one GPU for faster inference using vLLM and others for training) <a class="yt-timestamp" data-t="44:11:00">[44:11:00]</a>, but these required specific Cuda versions (12.1 vs. available 12.4) <a class="yt-timestamp" data-t="45:58:00">[45:58:00]</a>. The speaker ultimately abandoned the replication due to the time-consuming and unrewarding nature of debugging Cuda dependency mismatches and a lack of H100 GPU capacity in the cloud <a class="yt-timestamp" data-t="46:40:00">[46:40:00]</a>.

## Broader Implications of Deep Seek's Success

### The Rise of Finance Firms in AI

Deep Seek's unexpected success, as a finance firm, in beating established AI labs is attributed to their ability to attract top talent. The "cream of the crop" computer science graduates, particularly from top universities like Carnegie Mellon, often choose finance firms over large tech companies due to significantly higher compensation <a class="yt-timestamp" data-t="50:41:00">[50:41:00]</a>. These "cracked quants" possess superior engineering skills, demonstrated by Deep Seek's ability to optimize GPU code directly in Nvidia's PTX Assembly Language, outperforming even Nvidia's own engineers <a class="yt-timestamp" data-t="52:03:00">[52:03:00]</a>. The 40x cost reduction claimed by Deep Seek is a result of an accumulation of such "little tricks" and optimizations <a class="yt-timestamp" data-t="1:08:41">[1:08:41]</a>.

### Reinforcement Learning in Robotics

Deep Seek's model demonstrates that [[reinforcement_learning_and_selfplay_in_ai_development | Reinforcement learning and selfplay in AI development]] with minimal supervised data can outperform supervised fine-tuning with Reinforcement Learning from Human Feedback (RLHF) <a class="yt-timestamp" data-t="54:57:00">[54:57:00]</a>. This has significant implications for [[applications_in_machine_learning_and_reinforcement_learning | applications in machine learning and reinforcement learning]], especially in robotics:

*   **Simulation vs. Teleoperation**: The speaker suggests a trend where reinforcement learning with long-horizon generated data will surpass imitation learning from teleoperation data <a class="yt-timestamp" data-t="55:31:00">[55:31:00]</a>. Many robotics companies currently rely on teleoperation (humans controlling robots to collect data) <a class="yt-timestamp" data-t="55:41:00">[55:41:00]</a>. However, Deep Seek's success, similar to AlphaGo achieving superhuman Go performance purely through simulation, indicates that future robotics companies might win by entirely simulated training, deploying robots to the real world only after millions of hours of simulation <a class="yt-timestamp" data-t="56:27:00">[56:27:00]</a>.

### Market Dynamics and Nvidia

Deep Seek's emergence has impacted market perceptions, especially regarding Nvidia. While Nvidia is a dominant force due to its ownership of hardware, simulation tools, and a full vertical solution for AI <a class="yt-timestamp" data-t="58:28:00">[58:28:00]</a>, the market's recent drop in Nvidia's stock price might reflect a realization that if a Chinese startup can challenge OpenAI, a similar disruption could occur in the GPU market <a class="yt-timestamp" data-t="1:02:55">[1:02:55]</a>.

> [!INFO] H800 vs. H100
> Deep Seek's use of H800 chips, which have the same computational performance (FLOPS) as H100s but slower interconnect bandwidth, forced them to write low-level PTX Assembly code to optimize cross-chip communication, effectively turning H800s into H100s <a class="yt-timestamp" data-t="59:13:00">[59:13:00]</a>.

### The Future: Open Source, Decentralization, and AGI

The open-sourcing of Deep Seek's innovations accelerates the overall progress of [[ai_and_reinforcement_learning | AI and Reinforcement Learning]] <a class="yt-timestamp" data-t="1:28:22">[1:28:22]</a>. While proprietary labs with larger budgets will benefit and move faster up the "reinforcement learning S-curve," this shared knowledge contributes to reaching advanced AI capabilities sooner <a class="yt-timestamp" data-t="1:28:50">[1:28:50]</a>.

The speaker advocates for a future where AI runs locally on personal computers, allowing individuals to decide what their AI does, rather than relying on API-controlled models from centralized servers <a class="yt-timestamp" data-t="1:05:06">[1:05:06]</a>. This vision extends to decentralized AI training, leveraging the computational power of millions of personal devices to create a "giant hive mind" that could eventually surpass corporate or nation-state clusters <a class="yt-timestamp" data-t="1:41:43">[1:41:43]</a>.

The development of reasoning models, which are encouraged to produce longer "thought traces" to arrive at correct answers, is a key trend <a class="yt-timestamp" data-t="1:26:50">[1:26:50]</a>. While current [[ai_and_reinforcement_learning | AI models]] excel in domains with clear reward signals like math and coding, the intuition is that these reasoning abilities will generalize to other domains like philosophy <a class="yt-timestamp" data-t="1:31:51">[1:31:51]</a>.

Further advancements include the continued reduction of data types (e.g., from FP16 to FP8), known as quantization, to enable faster and more memory-efficient training and deployment of models <a class="yt-timestamp" data-t="1:22:31">[1:22:31]</a>, which is crucial for [[efficient_deep_learning_for_autonomous_vehicles | efficient deep learning for autonomous vehicles]] and other [[applications_in_machine_learning_and_reinforcement_learning | applications]].