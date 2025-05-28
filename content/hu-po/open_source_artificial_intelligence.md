---
title: Open source artificial intelligence
videoId: Ii_7-wsTjLo
---

From: [[hu-po]] <br/> 

Open source artificial intelligence (AI) models, such as DeepSeek, are a significant area of development, even if the topic can sometimes feel "done to death" due to the rapid pace of discussion and releases <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The growth in [[open_source_contributions_to_ai_development | open source contributions to AI development]] is evident, with communities actively replicating and building upon new innovations <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.

## DeepSeek's Approach and Impact

DeepSeek is an example of an AI model that has generated considerable discussion, particularly concerning its training methods and efficiency. The DeepSeek Math paper is highlighted as a leading resource for understanding the project's "unified paradigm and the explanations" <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Distillation and Data Usage
A common point of contention around models like DeepSeek involves [[synthetic_training_data_for_ai | synthetic training data for AI]] and distillation, where one model learns from the outputs of another <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. This process is not seen as cheating or theft, as "everyone distills from each other" and "humanity is just one giant distillation process" <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. For instance, even OpenAI has been noted to have trained on publicly available data like YouTube, similar to how DeepSeek might have distilled from OpenAI's models <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. Distillation involves a smaller model learning to mimic the outputs of a larger, more intelligent model, either by copying final answers or, more efficiently, by using the larger model's "logits" (exact probabilities for each token) <a class="yt-timestamp" data-t="01:14:03">[01:14:03]</a>. This process can make smaller models surprisingly capable, indicating that such models have the inherent capacity for intelligence if their weights are set correctly <a class="yt-timestamp" data-t="01:21:01">[01:21:01]</a>.

### GRPO Algorithm for Efficiency
DeepSeek's success is partly attributed to its use of the **GRPO (Group-Reward Proximal Policy Optimization)** algorithm, a variant of the well-known PPO (Proximal Policy Optimization) <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

Key innovations in GRPO:
*   **Multiple Observations**: Unlike PPO, which samples a single observation, GRPO samples a "group" of observations (multiple completions) from the policy, allowing for a more robust advantage estimation <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Elimination of Value Network**: GRPO avoids the need for a separate value network, which typically adds "substantial memory and computational burden" <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. Instead, it uses a "group reward score" based on multiple samples, akin to a Monte Carlo estimate of the value function <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>. This contrasts with older reinforcement learning (RL) paradigms (like those used in PPO from 2015), which leveraged learned value functions, influenced by approaches like Generative Adversarial Networks (GANs) <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.
*   **Outcome vs. Process Supervision**: DeepSeek's paper surprisingly found "process reward is unsuccessful" <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>, concluding that outcome supervision (reward at the end of output) was more effective for them than process supervision (feedback at every step), which contradicts some prior research <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>. This highlights that "different results" can occur in AI research, and one should "don't over index on any one individual result" <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>.

### Engineering and Data Over Algorithms
The speaker emphasizes that the advancements in AI are often driven more by data and engineering effort than by a single "magic algorithm" <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. DeepSeek's 40x cost reduction is attributed to an accumulation of many small optimizations and "little tricks," rather than solely the elimination of the value model <a class="yt-timestamp" data-t="01:08:38">[01:08:38]</a>.

A notable engineering feat by DeepSeek was their ability to optimize GPU code at a low level, including using NVIDIA's PTX Assembly Language. They effectively turned h800 chips into h100s by programming "specifically to manage cross-chip communications" <a class="yt-timestamp" data-t="01:00:32">[01:00:32]</a>, showcasing exceptional engineering talent.

## Open Source Implementations and Challenges
Hugging Face, a champion of [[opensource_ai_and_its_implications | open source AI and its implications]], has undertaken the "Open R1" project to openly reproduce DeepSeek R1 <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>. This implementation primarily uses TRL (Transformer Reinforcement Learning), a library maintained by Hugging Face <a class="yt-timestamp" data-t="00:26:54">[00:26:54]</a>.

Attempting to run a replication experiment comes with significant challenges:
*   **High GPU Costs**: Running large-scale AI experiments on powerful GPUs like h100s is prohibitively expensive for individuals, with costs easily reaching thousands of dollars per run <a class="yt-timestamp" data-t="00:33:45">[00:33:45]</a>.
*   **Limited Resources for Individuals**: Even with reduced dataset sizes, personal experiments are often "the tiniest first initial part of a small model" compared to massive training runs, making it difficult to prove anything substantial <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. However, tuning hyperparameters on smaller models and then transferring them to full-size models is a common industry practice <a class="yt-timestamp" data-t="00:37:54">[00:37:54]</a>.
*   **Dependency Hell**: Maintaining compatible versions of NVIDIA drivers, CUDA, PyTorch, and specialized libraries like vLLM can lead to frustrating and time-consuming "dependency mismatch issues," where debugging feels like a "waste of an entire day" <a class="yt-timestamp" data-t="00:46:36">[00:46:36]</a>.
*   **Cloud GPU Capacity**: Even if one can afford it, demand for high-end GPUs can lead to capacity shortages from cloud providers <a class="yt-timestamp" data-t="00:47:33">[00:47:33]</a>.

Despite these hurdles, open-sourcing these models is vital as it allows the entire field to "move faster," benefiting all developers and accelerating progress up the "reinforcement learning S-curve" <a class="yt-timestamp" data-t="01:28:41">[01:28:41]</a>.

## Implications for AI Development and Future Trends

### The Rise of Reasoning Models
DeepSeek's work highlights the emergence of "reasoning models" that are encouraged to "think long" by generating multiple tokens or steps in their output before providing a final answer. This approach, similar to "chain of thought" prompting, often leads to more accurate results, particularly in complex tasks like math <a class="yt-timestamp" data-t="01:26:59">[01:26:59]</a>.

### Reinforcement Learning and Simulation
The speaker believes that **reinforcement learning with long-horizon generated data** will surpass imitation learning from teleoperation data <a class="yt-timestamp" data-t="00:55:31">[00:55:31]</a>. This suggests a future where AI models, particularly in robotics, will be trained predominantly in "ginormous" simulations rather than relying on human teleoperation data, leading to more robust and generalized behaviors <a class="yt-timestamp" data-t="00:56:27">[00:56:27]</a>. The success of AlphaGo, which achieved superhuman Go performance entirely through simulation without ever playing on a real board, serves as a precedent <a class="yt-timestamp" data-t="00:56:52">[00:56:52]</a>. This shift suggests that AI development will increasingly leverage [[synthetic_training_data_for_ai | synthetic training data for AI]] generated by the models themselves within simulated environments <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

### Generalization and Transfer of Knowledge
There is an expectation that superhuman performance in domains like math and coding, where reward signals can be easily verified by the environment, will lead to "superhuman performance" in other disciplines like philosophy due to the transfer of general reasoning capabilities <a class="yt-timestamp" data-t="01:32:05">[01:32:05]</a>.

### Decentralized AI Training
The future of AI training might involve **decentralized systems**, similar to how Bitcoin operates. This would leverage the collective compute power of "every single cell phone in the world and every single computer in the world" to form massive, distributed clusters, potentially leading to the "best model in the world" <a class="yt-timestamp" data-t="01:41:44">[01:41:44]</a>. Such decentralized training could even be managed by AI agent corporations that operate without human intervention <a class="yt-timestamp" data-t="01:46:40">[01:46:40]</a>.

### The Bigger Picture
Ultimately, the competition between nations or corporations in AI is a "human game" <a class="yt-timestamp" data-t="00:53:09">[00:53:09]</a>. The true "third wave" is the eventual emergence of AI itself, which will eventually be in control <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>. The faster the field moves forward through [[open_source_contributions_to_ai_development | open source contributions to AI development]], the sooner humanity can reach a future where AI solves major problems like cancer, leading to an "immortal life" <a class="yt-timestamp" data-t="01:29:04">[01:29:04]</a>.