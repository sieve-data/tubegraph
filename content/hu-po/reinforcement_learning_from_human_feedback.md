---
title: reinforcement learning from human feedback
videoId: nTdJEQLday0
---

From: [[hu-po]] <br/> 

Reinforcement Learning from Human Feedback (RLHF) is a technique that has become very popular, especially since [[ai_and_reinforcement_learning | OpenAI]] stated they use it to fine-tune their [[ai_and_reinforcement_learning | ChatGPT]] models <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This method makes fine-tuning Large Language Models (LLMs) with [[ai_and_reinforcement_learning | reinforcement learning]] more accessible <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Purpose and Application
RLHF is primarily used to ensure that the output of LLMs aligns with desired human behavior and safety guidelines <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. It helps make LLM outputs specifically what is wanted for certain tasks <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. However, it's noted that 99% of an LLM's intelligence comes from its original pre-training on simple tasks like next token prediction, not from RLHF <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

## The Three Steps of RLHF
Training a language model with RLHF involves three main steps <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>:

### Step 1: Supervised Fine-tuning
This step involves fine-tuning a pre-trained LLM on a specific domain or corpus of instructions and human demonstrations <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. This human feedback constitutes a much smaller dataset compared to the original pre-training data <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. A prompt is sampled from a prompt dataset, and a human labeler demonstrates the desired output behavior <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This data is used to fine-tune the LLM (e.g., GPT-3.5) with supervised learning <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. The prompt dataset needs to be very clean, likely created in-house rather than from user data <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

### Step 2: Reward Model Training
In this step, a human-annotated dataset is collected to train a reward model <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. This reward model is essentially a value function <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. A prompt and several model outputs are sampled <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. A human labeler then ranks these outputs, providing a learning signal for the reward model <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. The reward model predicts the reward (e.g., a number between 0 and 1) for any given state (human prompt) and action (LLM answer), indicating how appropriate the answer is <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Step 3: Policy Optimization with RL
Finally, the LLM from Step 1 is fine-tuned further with the reward model and the data set using [[ai_and_reinforcement_learning | reinforcement learning]] <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This is often done using the Proximal Policy Optimization (PPO) algorithm <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. The reward model continuously pushes gradients into the LLM, enabling it to choose the best answers based on the distribution shaped by human labelers <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

## Underlying Concepts

### [[ai_and_reinforcement_learning | Reinforcement Learning]] (General)
[[ai_and_reinforcement_learning | Reinforcement learning]] is a type of [[applications_in_machine_learning_and_reinforcement_learning | machine learning]] that predates deep learning <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. It is built upon the idea of a [[reinforcement_learning_and_selfplay_in_ai_development | Markov Decision Process]] <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>, where an environment rewards an agent for successfully completing tasks <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### [[reinforcement_learning_and_selfplay_in_ai_development | Markov Decision Process (MDP)]]
The [[reinforcement_learning_and_selfplay_in_ai_development | Markov Decision Process]] describes the world as a set of states where agents take actions that produce more states <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. There is also observability of these states <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Value Function / Reward Model
In [[ai_and_reinforcement_learning | reinforcement learning]], a component (often a deep neural network) approximates the value function, which predicts the reward for any given state and action within the environment <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. The reward model in RLHF serves this purpose, determining the "goodness" of LLM answers <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### Proximal Policy Optimization (PPO)
PPO is a common and relatively straightforward [[ai_and_reinforcement_learning | reinforcement learning]] algorithm, often the first one to try <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. It is widely available in open-source [[ai_and_reinforcement_learning | reinforcement learning]] libraries like OpenAI Gym and RL Baselines <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. In RLHF, PPO optimizes the language model's policy based on the rewards provided by the reward model <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

## RLHF and Large Language Models (LLMs)

### Role of Pre-training vs. RLHF
The vast majority (99%) of an LLM's intelligence comes from its initial, massive pre-training, typically on simple tasks like next token prediction <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. RLHF primarily focuses on "AI safety" and aligning the LLM's output with specific desired behaviors <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### Potential Downsides
It's suspected that RLHF could potentially harm LLMs, similar to how transfer learning can lead to "catastrophic forgetting" <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. By fine-tuning on human feedback datasets, a model's ability to generalize might be reduced <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>, potentially decreasing performance on benchmarks unrelated to answering questions <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

## Technical Considerations and Scaling

### Fine-tuning Process
Fine-tuning involves taking a pre-trained [[applications_in_machine_learning_and_reinforcement_learning | machine learning]] or deep learning model and training it for a longer period on a different dataset <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. When fine-tuning, gradients are pushed into the large language model, modifying its parameters <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. This differs from in-context learning or prompt engineering, where model parameters are not changed <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### GPU Memory and Precision
Large LLMs, such as those with 20 billion parameters, require substantial GPU memory <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. In full float32 precision, a billion parameters cost 4 GB of GPU memory <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>. For a 20-billion-parameter model, this would be 80 GB <a class="yt-timestamp" data-t="00:45:01">[00:45:01]</a>. To reduce memory usage, lower precision data types like float16 (half memory), int8 (quarter memory), and even 4-bit numbers (eighth memory) are used <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. A 20-billion-parameter model in int8 precision would fit in 20 GB of memory <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>. Efficient 8-bit matrix multiplication helps mitigate performance degradation when quantizing large models by performing outlier computations in float16 and non-outlier parts in int8 <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>.

### Parallelism Strategies
Training LLMs at scale often involves distributing the workload across multiple GPUs <a class="yt-timestamp" data-t="00:28:39">[00:28:39]</a>. Common strategies include:
*   **Data Parallelism:** The same model is replicated on several machines, each processing a different batch of data <a class="yt-timestamp" data-t="00:30:07">[00:30:07]</a>.
*   **Model Parallelism:** The model itself is split across multiple machines, with each compute node calculating only a part of the model <a class="yt-timestamp" data-t="00:30:45">[00:30:45]</a>. This can be further divided into:
    *   **Pipeline Parallelism:** The model is split layer-wise <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>.
    *   **Tensor Parallelism:** Tensors or operations within a layer are split across GPUs <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>.
These strategies, often combined, require a deep understanding of hardware and can be very complicated to implement <a class="yt-timestamp" data-t="00:33:44">[00:33:44]</a>.

### Low-Rank Adaptation (LoRA) and Parameter-Efficient Fine-Tuning (PEFT)
LoRA, introduced in 2021, allows fine-tuning large language models by freezing most of the pre-trained weights and instead creating low-rank versions of specific matrices (like query and value layers in attention mechanisms) <a class="yt-timestamp" data-t="00:39:39">[00:39:39]</a>. These low-rank matrices have far fewer parameters, drastically reducing memory requirements and allowing fine-tuning with less GPU memory <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>. Hugging Face's PEFT library supports the creation and fine-tuning of these adapter layers <a class="yt-timestamp" data-t="00:43:24">[00:43:24]</a>. These adapters can be saved and loaded separately, so users don't need to download the entire base model again <a class="yt-timestamp" data-t="00:49:04">[00:49:04]</a>.

### Handling Reference Models
In RLHF, it's common to have two copies of the model: an "active" model and a "reference" model. The reference model helps prevent the active model from deviating too much from its original behavior <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. Using techniques like LoRA adapters, the same model can serve as both active and reference, dynamically enabling or disabling the adapter layers to obtain their respective "logits" (outputs representing probability distributions over actions) <a class="yt-timestamp" data-t="00:49:56">[00:49:56]</a>. This avoids the need for two full copies of the model, saving memory <a class="yt-timestamp" data-t="00:50:45">[00:50:45]</a>.

## Tools and Libraries
*   **Hugging Face:** A platform for [[ai_and_reinforcement_learning | machine learning]] models and tools <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>.
*   **TRL (Transformer Reinforcement Learning):** A library from Hugging Face designed to make [[ai_and_reinforcement_learning | RL]] steps for LLM fine-tuning easier <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **PEFT (Parameter-Efficient Fine-Tuning):** A Hugging Face library supporting adapter layers for LLMs <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Accelerate:** A Hugging Face library that helps with distributed training <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
*   **OpenAI Gym / RL Baselines:** Open-source [[ai_and_reinforcement_learning | reinforcement learning]] libraries that implement various [[ai_and_reinforcement_learning | RL]] algorithms, including PPO <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.
*   **BitsAndBytes:** A library used for 8-bit quantization <a class="yt-timestamp" data-t="00:57:05">[00:57:05]</a>.
*   **Weights & Biases:** A platform for experiment tracking and creating living reports/dashboards for [[applications_in_machine_learning_and_reinforcement_learning | machine learning]] projects <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>.

## Future Outlook
While current tools make RLHF more accessible, scaling these techniques to multi-GPU settings remains a significant challenge <a class="yt-timestamp" data-t="00:57:35">[00:57:35]</a>. It's anticipated that major players like [[ai_and_reinforcement_learning | OpenAI]] (via Microsoft), Google, and Meta will develop their own comprehensive libraries and tooling for specific [[taskspecific_agent_loops_and_reinforcement_learning | applications in machine learning and reinforcement learning]] <a class="yt-timestamp" data-t="00:59:08">[00:59:08]</a>. Improving training speed is another key area for future [[stateoftheart_in_reinforcement_learning | development in reinforcement learning and AI]] <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>.