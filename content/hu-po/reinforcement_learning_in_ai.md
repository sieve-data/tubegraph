---
title: Reinforcement learning in AI
videoId: Ii_7-wsTjLo
---

From: [[hu-po]] <br/> 

This article explores [[reinforcement_learning_and_q_learning_in_ai | Reinforcement Learning (RL)]], focusing on its application in DeepSeek's models, specifically the Group Reward Proximal Policy Optimization (GRPO) algorithm. It delves into the technical differences between GRPO and PPO, the broader implications of [[reinforcement_learning_concepts_applied_to_ai_agents | RL]] in AI development, and the ongoing debate about the importance of algorithms versus data and engineering.

## DeepSeek and GRPO: An Overview
DeepSeek, a prominent AI model, has garnered attention for its mathematical capabilities, largely attributed to its use of a variant of PPO called GRPO <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. While the speaker acknowledges being "a little bit slow to the punch" in covering DeepSeek, given the abundance of existing content, the focus here is on the underlying [[reinforcement_learning_concepts_applied_to_ai_agents | RL]] techniques <a class="yt-timestamp" data-t="02:52:50">[02:52:50]</a>.

## Fundamentals of Reinforcement Learning
At its core, [[reinforcement_learning_and_q_learning_in_ai | Reinforcement Learning]] involves an agent (policy, neural net, or robot) interacting with an environment <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>. The environment provides a reward signal, which is then used to generate a gradient update, refining the agent's policy <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.

### On-Policy vs. Off-Policy RL
*   **On-policy [[reinforcement_learning_and_q_learning_in_ai | RL]]:** The gradient update is directly applied to the policy that generated the interaction and observations <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>.
*   **Off-policy [[reinforcement_learning_and_q_learning_in_ai | RL]]:** Experiences from the agent's interaction with the environment are stored in a replay buffer <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>. Policy updates can then sample from this buffer, meaning the gradient update might use examples from a policy that is no longer the current one <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>. This can lead to complications, as a greater "distance" between the policy that collected the experience and the policy receiving the update can cause issues <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>. PPO and GRPO utilize both the current policy ($\Pi_\theta$) and an old policy ($\Pi_{\theta_{old}}$) in their objectives <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.

### Deep Dive into PPO and GRPO
Both PPO and GRPO aim to maximize an objective function, which are very similar in structure <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>.

#### Objective Functions
The objective functions for GRPO and PPO share common elements:
*   **Sampling from P(Q):** Both methods sample questions (Q) from a probability distribution of all possible questions <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>.
*   **Ratio of Current to Old Policy:** A core component is the ratio $\Pi_\theta / \Pi_{\theta_{old}}$, which represents the probability of the current policy picking a token compared to the old policy <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. A ratio greater than one indicates the new policy is making progress by increasing its probability of picking the right token <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>.
*   **Clipping:** To prevent extreme values, this ratio is clipped between `1 - Epsilon` and `1 + Epsilon`, then the minimum of the original and clipped value is taken <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.

#### KL Divergence
A `beta * KL Divergence` term is included to prevent the policy from drifting too far from a reference policy ($\Pi_{ref}$), which in the DeepSeek paper is an SFT (Supervised Fine-Tuning) model <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>. This term acts as a regularization to ensure stability during gradient updates <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>. A large beta value means the KL divergence is highly penalized, forcing the policy to stay close to the reference <a class="yt-timestamp" data-t="41:52:00">[41:52:00]</a>.

#### Advantage, Q, and Value Functions
These functions are central to [[reinforcement_learning_and_q_learning_in_ai | Reinforcement Learning]] for evaluating states and actions:
*   **Policy Network ($\Pi_\theta$):** Consumes the current state (e.g., a Go board) and produces a probability distribution over possible actions (e.g., moves) <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>.
*   **Value Function (V(s)):** Takes in the state and outputs a single number representing the "value" or goodness of that state <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.
*   **Q-Function (Q(s, a)):** Similar to the value function, but it also considers a specific action, indicating the expected reward if that action is taken in that state <a class="yt-timestamp" data-t="15:16:00">[15:16:00]</a>. It's often broken down as the immediate reward plus the discounted value of the next state <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>.
*   **Advantage Function (A(s, a)):** Represents how much better a specific action is compared to the average value of that state <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>. The objective of the algorithm is to maximize the expected reward <a class="yt-timestamp" data-t="17:18:00">[17:18:00]</a>.

#### Key Differences between PPO and GRPO
*   **Multiple Observations in GRPO:** Unlike PPO, which samples a single observation (o), GRPO samples a group (G) of observations from the old policy <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>.
*   **Elimination of Separate Value Model in GRPO:** PPO typically employs a separate value network, often a model comparable in size to the policy model, which adds significant memory and computational burden <a class="yt-timestamp" data-t="19:46:00">[19:46:00]</a>. GRPO innovates by calculating the advantage based on a "group reward score" from the multiple sampled observations, effectively acting as a Monte Carlo estimate of the value function and thus eliminating the need for a separate value network <a class="yt-timestamp" data-t="20:33:00">[20:33:00]</a>. This means GRPO doesn't require two different networks to run simultaneously <a class="yt-timestamp" data-t="23:03:00">[23:03:00]</a>.

## Outcome vs. Process Supervision in RL
DeepSeek's research showed different results regarding supervision types compared to earlier works, like a paper from Google (with John Shulman of OpenAI/Anthropic also listed as an author):
*   **Outcome Supervision:** Provides a single reward at the very end of the output <a class="yt-timestamp" data-t="24:11:00">[24:11:00]</a>.
*   **Process Supervision:** Provides feedback (reward) at every intermediate step <a class="yt-timestamp" data-t="24:32:00">[24:32:00]</a>.

While earlier research concluded that process supervision was superior, DeepSeek found process reward to be "unsuccessful," citing difficulties in defining fine-grained steps, issues with automated annotations, and additional training resources needed for reward models <a class="yt-timestamp" data-t="24:54:00">[24:54:00]</a>. This highlights that results can differ across studies, suggesting no single definitive approach in [[challenges_and_techniques_in_reinforcement_learning | RL]] <a class="yt-timestamp" data-t="25:16:00">[25:16:00]</a>.

## The Role of Algorithms vs. Data in RL Success
The speaker strongly argues that the success of models like DeepSeek is not solely due to the specific algorithm (GRPO) but rather a combination of superior data and significant engineering effort <a class="yt-timestamp" data-t="18:40:00">[18:40:00]</a>. This aligns with the historical pattern in AI where different algorithms (e.g., CNNs vs. Vision Transformers) constantly battle for supremacy, with no single one being universally "better" <a class="yt-timestamp" data-t="18:08:00">[18:08:00]</a>. The market tends to over-index on algorithms, while the real gains often come from data and engineering <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>.

## Practical Experimentation with GRPO
The speaker attempted to replicate parts of DeepSeek's [[reinforcement_learning_and_selfplay_in_ai_development | RL]] training using Hugging Face's Open RLHF project, which aims for an open reproduction of DeepSeek RL <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>. The experiment focused on fine-tuning a `Qwen 7B` model on the `AIMO Num Math` dataset using GRPO <a class="yt-timestamp" data-t="32:48:00">[32:48:00]</a>.

### Hyperparameter Tuning
The experiment involved sweeping different hyperparameters for GRPO:
*   **Beta:** Controls the importance of the KL Divergence term <a class="yt-timestamp" data-t="28:40:00">[28:40:00]</a>. A low beta allows for greater divergence from the reference policy, leading to increased KL Divergence <a class="yt-timestamp" data-t="41:29:00">[41:29:00]</a>.
*   **Temperature:** Influences the randomness of the neural net's outputs <a class="yt-timestamp" data-t="29:23:00">[29:23:00]</a>. Higher temperatures lead to more diverse (random) outputs, which in GRPO results in more varied observations and a higher reward standard deviation <a class="yt-timestamp" data-t="30:26:00">[30:26:00]</a>.
*   **Learning Rate:** Determines the step size in traversing the loss landscape during gradient updates <a class="yt-timestamp" data-t="42:26:00">[42:26:26]</a>. A learning rate that is too high can lead to large gradient norms and a drop in reward <a class="yt-timestamp" data-t="42:32:00">[42:32:00]</a>.

### Challenges in Replication
Due to the high cost of running full-scale [[reinforcement_learning_and_stateoftheart_models | state-of-the-art models]] training (e.g., $1,300 per run for 56 hours on H100s) <a class="yt-timestamp" data-t="33:57:00">[33:57:00]</a>, the speaker had to reduce the dataset size significantly, leading to a "bogus mini experiment" <a class="yt-timestamp" data-t="35:31:00">[35:31:00]</a>. While the small experiment showed expected relationships between hyperparameters and metrics, it was not a true reproduction of DeepSeek's scale <a class="yt-timestamp" data-t="36:10:00">[36:10:00]</a>.

Further challenges arose when Hugging Face updated their Open RLHF repo to use `vllm` for faster inference, which introduced complex Cuda dependency mismatches <a class="yt-timestamp" data-t="45:47:00">[45:47:00]</a>. This type of debugging is deemed unproductive, leading the speaker to abandon the experiment <a class="yt-timestamp" data-t="46:58:00">[46:58:00]</a>.

## Wider Implications and Future of RL

### Robotics and Simulation
DeepSeek's success suggests that [[reinforcement_learning_with_human_feedback_rlhf | RL]] with minimal supervised data can outperform supervised fine-tuning with [[reinforcement_learning_with_human_feedback_rlhf | RLHF]] <a class="yt-timestamp" data-t="54:57:00">[54:57:00]</a>. This has significant implications for robotics:
*   The speaker believes that [[reinforcement_learning_concepts_applied_to_ai_agents | RL]] with long-horizon generated data will eventually surpass imitation learning from teleoperation data <a class="yt-timestamp" data-t="55:31:00">[55:31:00]</a>.
*   Instead of relying on human teleoperators to collect vast amounts of robot data, the future of robotics will likely involve training everything in simulation (Sim2Real), deploying magically working robots after millions of hours of simulated training <a class="yt-timestamp" data-t="56:27:00">[56:27:00]</a>.

### Decentralized Training
The speaker envisions a future where AI training is decentralized, leveraging millions of computers worldwide, similar to how Bitcoin operates <a class="yt-timestamp" data-t="01:41:40">[01:41:40]</a>. This could lead to a global, distributed model that surpasses those trained by corporations or nation-states <a class="yt-timestamp" data-t="01:41:43">[01:41:43]</a>.

### Model Distillation
DeepSeek's use of distillation, where a smaller model (Qwen 7B) is trained to mimic a larger one (DeepSeek RL 685B), demonstrates an effective way to transfer knowledge <a class="yt-timestamp" data-t="01:14:03">[01:14:03]</a>. Distillation involves using a larger model to generate a dataset (input-output pairs) and then training a smaller model on this synthetic data <a class="yt-timestamp" data-t="01:14:05">[01:14:05]</a>. This process can be very efficient, especially if logits (exact probabilities for each token) are available, but it can still work with just the final word outputs <a class="yt-timestamp" data-t="01:16:09">[01:16:09]</a>. Distillation can be seen as a form of distributed training, where models learn from each other's outputs, leading to continuous improvement <a class="yt-timestamp" data-t="01:48:42">[01:48:42]</a>.

It also suggests that smaller models inherently have the capacity for high intelligence; distillation merely provides a more effective path through the loss landscape to achieve those optimal weights <a class="yt-timestamp" data-t="01:20:50">[01:20:50]</a>.

### Continuation of Trends
*   **Precision Reduction:** The trend of reducing data types (e.g., from BF16 to FP8) will continue, allowing for faster computation and more efficient training <a class="yt-timestamp" data-t="01:22:51">[01:22:51]</a>.
*   **Reasoning Models:** AI models are moving towards longer reasoning traces (more tokens generated before an answer), as this generally leads to higher accuracy in complex tasks like math and coding <a class="yt-timestamp" data-t="01:26:09">[01:26:09]</a>. The ability to reason and solve problems in math and code is expected to generalize to other domains, including philosophy <a class="yt-timestamp" data-t="01:32:11">[01:32:11]</a>.

The speaker concludes that the open-sourcing of DeepSeek's innovations, including GRPO, will accelerate the overall progress of AI, even if it means larger companies with bigger budgets can quickly adopt and scale these techniques <a class="yt-timestamp" data-t="01:28:22">[01:28:22]</a>.