---
title: Applications in machine learning and reinforcement learning
videoId: LuF4NGezcxo
---

From: [[hu-po]] <br/> 

[[ai_and_reinforcement_learning | Reinforcement learning]] (RL) is a prominent field within [[ai_and_reinforcement_learning | machine learning]] where models, often neural networks, learn to make decisions by interacting with an environment to maximize a reward signal <a class="yt-timestamp" data-t="01:10:09">[01:10:09]</a>. This approach is frequently observed in [[ai_and_reinforcement_learning | machine learning]] papers, particularly those focused on [[ai_and_reinforcement_learning | reinforcement learning]] <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>.

## Reinforcement Learning Fundamentals

In [[ai_and_reinforcement_learning | reinforcement learning]], models are referred to as "policies" <a class="yt-timestamp" data-t="01:06:57">[01:06:57]</a>. These policies are typically neural networks with parameters (e.g., "Theta" for a [[large_language_models_and_their_applications | Large Language Model]] like Llama 70B, meaning 70 billion numbers) <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>. The policy consumes an input (e.g., a sequence of tokens) and outputs a probability distribution over possible next actions or tokens <a class="yt-timestamp" data-t="01:05:14">[01:05:14]</a>.

A core concept in [[ai_and_reinforcement_learning | reinforcement learning]] is the reward function <a class="yt-timestamp" data-t="01:10:11">[01:10:11]</a>. The goal of an RL algorithm is to maximize this reward function <a class="yt-timestamp" data-t="01:10:12">[01:10:12]</a>. Reward signals typically originate from the environment <a class="yt-timestamp" data-t="01:10:12">[01:10:12]</a>. For example, in games like Go or chess, winning the game yields a high reward for all actions leading to that win, while losing results in a low reward for preceding actions <a class="yt-timestamp" data-t="01:10:12">[01:10:12]</a>.

This concept extends to domains like math and coding problems <a class="yt-timestamp" data-t="01:10:12">[01:10:12]</a>. A [[large_language_models_and_their_applications | language model]] generates sequences of tokens that represent problem-solving steps <a class="yt-timestamp" data-t="01:21:50">[01:21:50]</a>. The final answer can be verified as correct or incorrect, providing a reward signal <a class="yt-timestamp" data-t="01:15:58">[01:15:58]</a>. This allows the model to explore different solution paths ("traces") and learn which ones lead to correct answers <a class="yt-timestamp" data-t="01:16:10">[01:16:10]</a>.

### KL Divergence (Relative Entropy) as a Regularizer

[[discussion_on_reinforcement_learning_and_ai | Relative entropy]], also known as KL Divergence, is a statistical distance metric between two probability distributions <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>. It measures how inefficient it is to assume one distribution (Q) when the true distribution is another (P) <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. The concept of relative entropy comes from [[discussion_on_reinforcement_learning_and_ai | information theory]] and is related to entropy and cross-entropy <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a>.

In [[ai_and_reinforcement_learning | reinforcement learning]], KL Divergence is frequently incorporated into the loss function as a regularizer <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Its primary purpose is to prevent the policy (neural network) from "drifting too far" from a reference policy during iterative training <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. By adding a small, weighted KL term to the loss, it penalizes significant changes in the policy's output distribution <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This ensures that while the policy optimizes for reward, it doesn't drastically alter its behavior in each training step <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

The formula for KL Divergence (P from Q) is:
$DKL(P || Q) = \sum_{x \in X} P(x) \log\left(\frac{P(x)}{Q(x)}\right)$ <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
For continuous distributions, the sum is replaced by an integral <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
It's important to note that KL Divergence is not symmetric, meaning order matters (DKL(P || Q) is not equal to DKL(Q || P)) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

Numerical stability issues are common when implementing KL Divergence, especially when probabilities are zero or very small <a class="yt-timestamp" data-t="00:38:41">[00:38:41]</a>. This can lead to division by zero or logarithms of zero <a class="yt-timestamp" data-t="00:38:47">[00:38:47]</a>. To mitigate this, operations are often performed in logarithmic scale, which converts multiplications to additions and helps with numerical stability <a class="yt-timestamp" data-t="00:43:24">[00:43:24]</a>.

### Specific Applications in Large Language Models

KL Divergence is extensively used in [[ai_and_reinforcement_learning | reinforcement learning]] for [[large_language_models_and_their_applications | Large Language Models]] (LLMs):

*   **DeepSeek R1 Paper**: This paper introduces GRPO (Generalized Reinforcement Learning with Policy Optimization), where a KL term is included in the optimization objective <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. The KL Divergence is calculated between the current policy ($\Pi_{Theta}$) and a reference policy ($\Pi_{reference}$), which helps regularize the policy's updates <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
    *   DeepSeek R1, an autoregressive [[large_language_models_and_their_applications | Large Language Model]], samples different completions, evaluates their rewards and advantages, and uses this signal to push gradients into the LLM <a class="yt-timestamp" data-t="00:26:20">[00:26:20]</a>. The KL Divergence acts on the outputs of the policy and the reference policy <a class="yt-timestamp" data-t="00:26:39">[00:26:39]</a>.
*   **Kim K 1.5**: This Chinese startup also used [[ai_and_reinforcement_learning | RL]] to iteratively improve their model, employing a KL Divergence between the current policy ($\Pi_{Theta}$) and a previous policy ($\Pi_{Theta}I$) <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This is often between two neural networks, one being a slightly newer version of the other <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

### RL Training Paradigms: Online vs. Offline

In [[ai_and_reinforcement_learning | reinforcement learning]], a key distinction is made between online and offline RL <a class="yt-timestamp" data-t="01:17:11">[01:17:11]</a>.

*   **Online RL**: In this paradigm, gradients are pushed directly into the neural network (policy) that generated the current experience <a class="yt-timestamp" data-t="01:17:21">[01:17:21]</a>. This means the policy being updated is the same one that collected the data.
*   **Offline RL**: Here, a large dataset of experiences is collected, often by policies that are different from the one currently being trained <a class="yt-timestamp" data-t="01:17:29">[01:17:29]</a>. This allows for leveraging vast amounts of pre-recorded data. In distributed RL systems, the policy used for experience collection quickly becomes "old" as the main policy updates <a class="yt-timestamp" data-t="01:18:03">[01:18:03]</a>. The KL Divergence acts as a regularizer in off-policy methods to ensure the updated policy doesn't deviate too much from the policy that generated the data, preventing "drifting too far" and over-optimizing for a specific iteration's experience <a class="yt-timestamp" data-t="01:18:48">[01:18:48]</a>.

### The Role of Reward Models and Replay Buffers

Reward models (RM) are central to many [[ai_and_reinforcement_learning | reinforcement learning]] applications <a class="yt-timestamp" data-t="01:14:31">[01:14:31]</a>. They evaluate the quality of the policy's outputs based on defined criteria (e.g., correctness of a math solution) <a class="yt-timestamp" data-t="01:15:58">[01:15:58]</a>.

A "replay buffer" is a storage mechanism for collecting "experience" (data, such as completed games or problem-solving traces) generated by the policy <a class="yt-timestamp" data-t="01:20:23">[01:20:23]</a>. When training, a subset of this collected experience is sampled from the replay buffer and used to calculate gradients for updating the policy <a class="yt-timestamp" data-t="01:20:41">[01:20:41]</a>.

### Self-Learning and Exploration

The process where models generate their own data (e.g., trying out different paths down a "tree of knowledge" in problem-solving) and then use an environmental reward signal to determine which of those traces are best to train the model is a form of [[reinforcement_learning_and_selfplay_in_ai_development | self-learning]] <a class="yt-timestamp" data-t="01:23:50">[01:23:50]</a>. For tasks like math and code, the ability to label these explorations as "good" or "bad" facilitates continuous experience collection and policy improvement <a class="yt-timestamp" data-t="01:24:06">[01:24:06]</a>. This iterative process allows the model to explore more effectively and improve its performance <a class="yt-timestamp" data-t="01:24:17">[01:24:17]</a>. This paradigm, utilizing [[ai_and_reinforcement_learning | reinforcement learning]] for exploring the "tree of knowledge," is less compute-heavy than traditional pre-training approaches that involve feeding massive amounts of training data into a model <a class="yt-timestamp" data-t="01:35:31">[01:35:31]</a>.