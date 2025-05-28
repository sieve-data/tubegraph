---
title: Model distillation and training
videoId: Ii_7-wsTjLo
---

From: [[hu-po]] <br/> 

This article discusses [[Model training and evaluation methods | training methods]] and [[model_distillation_techniques | model distillation techniques]] used in machine learning, specifically focusing on DeepSeek models. It covers the intricacies of algorithms like PPO and GRPO, hyperparameter tuning, and the broader implications of these techniques in the AI landscape.

## DeepSeek: A Case Study in Advanced Training
DeepSeek's recent advancements have sparked significant discussion in the AI community <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. The DeepSeek math paper is highlighted for its "unified paradigm and explanations" <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Accusations against DeepSeek of "sucking the knowledge out" or copying data are dismissed, as "everyone distills from each other" <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>, and "humanity is just one giant distillation process" <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Even OpenAI's Mira Murati effectively acknowledged training on publicly available data like YouTube <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## GRPO: A Variant of PPO
DeepSeek Math utilizes a variant of PPO (Proximal Policy Optimization) called GRPO (Group Reward Proximal Policy Optimization) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. PPO is often one of the first reinforcement learning algorithms learned <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. The objective functions for GRPO and PPO are "very, very similar" <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### Key Differences between GRPO and PPO
The main differences in their objectives are:
*   **Sampling from `P(q)`:** Both sample questions (q) from a probability distribution `P(q)`, which for DeepSeek Math, represents math questions <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Multiple vs. Single Observations:** In GRPO, observations are sampled from `Pi Theta old` (the old policy) as a set of answers, averaged over 'G' observations <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. PPO, in contrast, samples only a single observation <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. This means GRPO uses multiple "green lines" (completions), while PPO uses one <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Value Function:** PPO typically employs a separate value network, often a model of comparable size to the policy model, which introduces "substantial memory and computational burden" <a class="yt-timestamp" data-t="01:5:02:59">[01:5:02:59]</a>. GRPO, however, eliminates this separate value function by using a "group reward score" derived from G times running the policy, acting as a Monte Carlo estimate of the learned value function <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. This innovation helps reduce memory and computational costs <a class="yt-timestamp" data-t="02:11:02">[02:11:02]</a>.

### Core Components Explained
*   **`Pi Theta` vs. `Pi Theta old`:** These refer to the current and old policies, respectively <a class="yt-timestamp" data-t="01:10:02">[01:10:02]</a>. The ratio of their probabilities indicates progress: if the new policy's probability of picking the right token is higher than the old, it signifies improvement <a class="yt-timestamp" data-t="01:11:02">[01:11:02]</a>.
*   **Clipping (`Min` and `Clip`):** The clip function (`1 minus Epsilon` and `1 plus Epsilon`) is used to manage extreme values in the probability ratio, preventing instability <a class="yt-timestamp" data-t="01:46:02">[01:46:02]</a>.
*   **KL Divergence (`Beta DK`):** This term (Kullback-Leibler Divergence or relative entropy) measures the distance between the current policy (`Pi Theta`) and a reference policy (`Pi ref`), often an SFT (Supervised Fine-Tuning) model <a class="yt-timestamp" data-t="01:21:02">[01:21:02]</a>. Its purpose is to prevent the policy from "drifting too far" from the reference during gradient updates <a class="yt-timestamp" data-t="01:24:02">[01:24:02]</a>.
*   **Advantage Function (`A hat I of T` and `AF of T`):** The advantage function measures the expected reward from a given state and action <a class="yt-timestamp" data-t="01:39:02">[01:39:02]</a>.
    *   **Value Function (`V`):** Takes the state (e.g., board position in Go) and outputs a single number representing the "value of that state" <a class="yt-timestamp" data-t="01:43:02">[01:43:02]</a>.
    *   **Q-Function (`Q(s,a)`):** Similar to the value function, but also takes a specific action, indicating the "expected reward" for that state-action pair <a class="yt-timestamp" data-t="01:52:02">[01:52:02]</a>.
    *   GRPO's `A hat I of T` is computed based on group reward scores <a class="yt-timestamp" data-t="01:09:02">[01:09:02]</a>, while PPO's `AF of T` uses Generalized Advantage Estimation (GAE) based on rewards and a learned value function <a class="yt-timestamp" data-t="01:13:02">[01:13:02]</a>.

## On-Policy vs. Off-Policy Reinforcement Learning
Reinforcement learning involves an agent (policy/neural net) interacting with an environment to receive rewards, which are used to update the policy via gradient updates <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
*   **On-policy:** The gradient update is applied to the *same* policy that generated the observations <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Off-policy:** Experience is stored in a replay buffer, and samples are drawn from it. This means gradient updates can be applied using examples collected by a *different* (older) policy <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. The greater the "distance" between the policy that collected the data and the policy being updated, the more complications arise <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

## Training and Implementation Details
### Hugging Face's Open R1 Reproduction
Hugging Face created Open R1, an open-source reproduction of DeepSeek R1, primarily using the TRL (Transformer Reinforcement Learning) library <a class="yt-timestamp" data-t="02:30:02">[02:30:02]</a>. The focus was on the GRPO step, where a base model (e.g., Qwen 7B) is fine-tuned using GRPO <a class="yt-timestamp" data-t="02:49:02">[02:49:02]</a>.

### Hyperparameter Tuning
Experiments were conducted to compare the importance of `beta` (KL Divergence weight), `temperature` (randomness of output), and `learning rate` hyperparameters <a class="yt-timestamp" data-t="02:50:02">[02:50:02]</a>.
*   **Beta:** A large `beta` makes KL Divergence very important, keeping the policy close to the reference, while a small `beta` allows more deviation <a class="yt-timestamp" data-t="02:42:02">[02:42:02]</a>. Lower beta values resulted in increased KL Divergence <a class="yt-timestamp" data-t="02:41:02">[02:41:02]</a>.
*   **Temperature:** A high temperature increases randomness in token predictions, leading to higher KL Divergence and larger reward standard deviations <a class="yt-timestamp" data-t="02:53:02">[02:53:02]</a>. Conversely, a low temperature leads to more greedy sampling <a class="yt-timestamp" data-t="03:00:02">[03:00:02]</a>.
*   **Learning Rate:** A very high learning rate can cause a "huge gradient norm," leading to a sudden drop in reward, as the model ends up in a "weird part of the Loss landscape" <a class="yt-timestamp" data-t="03:22:02">[03:22:02]</a>.

### Data and Model Scaling
*   The `numath_ti` dataset (70,000 examples) was used <a class="yt-timestamp" data-t="03:31:02">[03:31:02]</a>. Running a full GRPO training on an 8x H100 node would cost approximately $1,300 and take 56 hours <a class="yt-timestamp" data-t="03:52:02">[03:52:02]</a>.
*   To manage costs, the dataset size was reduced to around 2,000 examples, cutting the run time to 42 minutes and cost to $16 <a class="yt-timestamp" data-t="03:08:02">[03:08:02]</a>.
*   Hyperparameter tuning is often done on smaller models and then "zero-shot transfer[red]" to full-size models, saving significant computational resources <a class="yt-timestamp" data-t="03:53:02">[03:53:02]</a>.

### Hardware and Optimization
DeepSeek's success is partly attributed to their engineers' ability to write "better GPU code than the engineers at Nvidia" using Nvidia's PTX Assembly Language <a class="yt-timestamp" data-t="05:09:02">[05:09:02]</a>. They effectively turned h800 chips (nerfed H100s in terms of interconnect) into H100-like performance by programming 20 of 132 processing units to manage cross-chip communications, bypassing Cuda <a class="yt-timestamp" data-t="01:00:32">[01:00:32]</a>. This low-level optimization is "impossible to do in Cuda" <a class="yt-timestamp" data-t="01:00:44">[01:00:44]</a>.

## Model Distillation
[[model_distillation_techniques | Model distillation techniques]] involves using a larger, more capable model (teacher) to generate a dataset, which is then used to [[Finetuning machine learning models | train]] a smaller model (student) <a class="yt-timestamp" data-t="01:14:03">[01:14:03]</a>. For example, DeepSeek R1 distilled its knowledge into Qwen 7B <a class="yt-timestamp" data-t="03:16:02">[03:16:02]</a>. This process allows a smaller model to become "much more intelligent" by mimicking the teacher <a class="yt-timestamp" data-t="03:42:02">[03:42:02]</a>. Distillation can be more efficient if the logits (exact probabilities for each token) from the teacher model are available, but it can still be done with only the final word output <a class="yt-timestamp" data-t="01:16:02">[01:16:02]</a>.

## Broader Implications and Future Trends
*   **Process vs. Outcome Supervision:** DeepSeek's paper concluded that process reward (providing feedback at every step) is "unsuccessful" and complicates the training pipeline, yielding different results than some other research <a class="yt-timestamp" data-t="02:41:02">[02:41:02]</a>. This highlights that results can vary, and no single algorithm or method is universally superior <a class="yt-timestamp" data-t="02:16:02">[02:16:02]</a>.
*   **Algorithm vs. Data/Engineering:** The speaker emphasizes that the specific algorithm (like GRPO vs. PPO) is less important than the "actual data and then the engineering effort" <a class="yt-timestamp" data-t="01:42:02">[01:42:02]</a>.
*   **Finance Firms and Talent:** Finance firms like DeepSeek attract top Computer Science talent by offering high compensation, allowing them to recruit engineers who are often "better engineers than the people at at Fang" <a class="yt-timestamp" data-t="05:00:02">[05:00:02]</a>.
*   **Simulation vs. Teleoperation in Robotics:** DeepSeek's success with reinforcement learning suggests that "reinforcement learning with long Horizon generated data is going to beat out imitation learning from teleoperation data" <a class="yt-timestamp" data-t="05:31:02">[05:31:02]</a>. This implies that future robotics advancements will rely more on extensive simulation training rather than human teleoperation <a class="yt-timestamp" data-t="05:50:02">[05:50:02]</a>.
*   **Market Dynamics:** The market's reaction to DeepSeek's rise, including Nvidia's stock drop, indicates a realization that even established incumbents can be challenged by new players, mirroring the disruption of OpenAI <a class="yt-timestamp" data-t="02:55:02">[02:55:02]</a>.
*   **S-Curves and AGI:** Technological progress follows S-curves. Reinforcement learning, as demonstrated by DeepSeek, represents a new S-curve after the initial pre-[[Model training and evaluation methods | training]] phase, promising rapid advancements before eventually flattening out <a class="yt-timestamp" data-t="02:21:02">[02:21:02]</a>.
*   **Decentralized Training:** The future of AI [[Model training and evaluation methods | training]] may involve decentralized systems, leveraging the collective computational power of millions of devices, similar to Bitcoin <a class="yt-timestamp" data-t="01:41:02">[01:41:02]</a>. This could lead to models not owned by corporations but by AI agents <a class="yt-timestamp" data-t="01:46:02">[01:46:02]</a>.
*   **Reasoning Models:** DeepSeek's reasoning models show that allowing LLMs to produce longer "reasoning traces" (more tokens) before an answer significantly improves accuracy, encouraging the model to "think long" <a class="yt-timestamp" data-t="02:50:02">[02:50:02]</a>.
*   **Transfer Learning:** Superhuman performance in domains like math and coding, where reward signals can be automatically verified, is expected to transfer to other disciplines, including philosophy <a class="yt-timestamp" data-t="01:31:02">[01:31:02]</a>.