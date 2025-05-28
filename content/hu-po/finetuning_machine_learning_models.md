---
title: finetuning machine learning models
videoId: nTdJEQLday0
---

From: [[hu-po]] <br/> 

[[Finetuning and Training Curriculums in AI Models | Finetuning]] is the process of taking a machine learning or deep learning model that has been trained for a long time on one dataset and then training it for a little bit longer on a different dataset <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This process falls within the broader sphere of [[Training and finetuning processes for AI models | training machine learning models]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Purpose of Finetuning
While the original training data and model size account for approximately 99% of a large language model's (LLM) intelligence <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, [[finetuning language models for specific tasks | finetuning]] is used for specific tasks such as:
*   AI safety <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>
*   Ensuring the LLM output is specifically desired for certain tasks <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>

It's noted that [[Pretraining and finetuning in AI models | finetuning]] is not strictly required and may even potentially hurt large language models in some cases, similar to "catastrophic forgetting" in transfer learning, where a model fine-tuned on new data might perform worse on its original task <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Reinforcement Learning from Human Feedback (RLHF)
RLHF is a technique that has become popular, particularly because OpenAI stated they use it to [[finetuning language models for specific tasks | fine-tune]] their ChatGPT models <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It is considered a competitive alternative to existing [[Finetuning pretrained models with minimal additional parameters | fine-tuning approaches]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. RLHF is more about the "human feedback" part and the dataset chosen for fine-tuning, rather than the specific reinforcement learning (RL) implementation <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Core Concepts of RL
Reinforcement learning predates deep learning and is built upon the concept of a Markov decision process <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This framework describes the world as a set of states where agents take actions, produce more states, and receive rewards for successful completion of tasks <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Three Steps of RLHF
Training a language model with RLHF involves three key steps:

1.  **Fine-tune a Pre-trained LLM on Instructions and Human Demonstrations** <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>:
    *   This initial [[finetuning language models for specific tasks | fine-tuning]] uses a much smaller, very clean dataset of human feedback <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
    *   A prompt is sampled, and a human "labeler" demonstrates the desired output behavior <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
    *   This data is used to fine-tune the base LLM (e.g., GPT-3.5) with supervised learning <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

2.  **Collect Human-Annotated Data and Train a Reward Model** <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>:
    *   A prompt and several model outputs are sampled <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
    *   A human labeler ranks these outputs based on appropriateness, providing the learning signal for the reward model <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
    *   The reward model, often another LLM or deep neural network, approximates a "value function" <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. It predicts the reward for any given state (human prompt) and action (LLM answer) <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This reward is typically a number between 0 and 1, indicating how appropriate the answer is <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

3.  **Fine-tune the LLM from Step 1 with the Reward Model using RL** <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>:
    *   Once the reward model is trained, it's used to "self-supervise" and push gradients into the LLM <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
    *   This involves optimizing the policy (the LLM's action-selection strategy) against the reward model using algorithms like Proximal Policy Optimization (PPO) <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
    *   PPO is a common and relatively easy-to-implement RL algorithm <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
    *   The model generates an output for a new prompt, the reward model calculates a score for that output, and this score is used to push gradients back into the PPO model to refine its answer selection <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

The overall goal is for human labelers to shape the distribution of what constitutes good answers, and then a value function estimates this distribution, and an RL (PPO) model picks answers based on the reward model <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. This process involves three main "function approximators": the reward model, the supervised policy (likely a deep learning model), and the LLM itself <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

## Technical Aspects and Optimization in Finetuning
[[Technical aspects of AI model training and finetuning | Finetuning]] involves actively modifying the parameters of the large language model by pushing gradients into it <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. This is distinct from in-context learning or prompt engineering, where no model parameters are changed <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Model Size and Memory
*   Large Language Models (LLMs) like ChatGPT, Google's Palm, and Meta's Llama have billions of parameters <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   GPUs (graphics cards) are essential for training and running these models, and they have varying amounts of memory <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Larger models require more GPU memory <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   A 24-gigabyte GPU is considered a consumer-grade GPU, often costing over a thousand dollars, while A100s used in research are significantly more powerful <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Data Precision and [[quantization and optimization in machine learning | Quantization]]
*   Parameters in machine learning models are numbers stored at different levels of precision (d-type) <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
    *   `float32`: uses 32 bits per number, common for full precision <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.
    *   `float16`: uses 16 bits per number, halving memory usage <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.
    *   `int8`: uses 8 bits per number <a class="yt-timestamp" data-t="00:29:16">[00:29:16]</a>.
    *   4-bit: actively being researched to store parameters in just four bits <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   [[finetuning with quantized models | Quantization]] reduces memory requirements but can lead to [[Performance and efficiency in machine learning models | performance degradation]] due to reduced precision <a class="yt-timestamp" data-t="00:36:45">[00:36:45]</a>.
*   **8-bit Matrix Multiplication**: A technique that performs matrix multiplications using a mix of `float16` for "outlier" hidden states and `int8` for "non-outlier" parts to mitigate performance degradation while saving memory <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.

### Parallelism and Distributed Training
[[Training and finetuning processes for AI models | Training at scale]] can be challenging due to fitting the model and optimizer on available GPU devices <a class="yt-timestamp" data-t="00:28:39">[00:28:39]</a>. Techniques include:
*   **Data Parallelism**: The same model is replicated across several machines, and each instance is fed a different batch of data <a class="yt-timestamp" data-t="00:32:25">[00:32:25]</a>.
*   **Model Parallelism (Pipeline and Tensor Parallelism)**: The model itself is distributed across many machines <a class="yt-timestamp" data-t="00:32:38">[00:32:38]</a>.
    *   *Pipeline Parallelism* splits the model layer-wise <a class="yt-timestamp" data-t="00:32:45">[00:32:45]</a>.
    *   *Tensor Parallelism* splits tensors and operations across GPUs <a class="yt-timestamp" data-t="00:32:48">[00:32:48]</a>.
*   **Sharding**: The process of dividing a large blob of data (like model weights) into smaller chunks to be sent to different machines <a class="yt-timestamp" data-t="00:33:23">[00:33:23]</a>.
*   **Fused Kernels**: Optimizing mathematical concepts in model architecture by combining multiple operations into a single GPU-executable kernel for speed improvements <a class="yt-timestamp" data-t="00:35:36">[00:35:36]</a>.

### Low-Rank Adaptation (LoRA) / Parameter-Efficient Fine-Tuning (PEFT)
A paper called LoRA demonstrated that [[Finetuning pretrained models with minimal additional parameters | fine-tuning]] can be done by "freezing" the pre-trained weights and creating low-rank versions of specific attention matrices (query and value layers) <a class="yt-timestamp" data-t="00:39:39">[00:39:39]</a>.
*   **Freezing weights**: Preventing gradients from changing the values of a large portion of the model's original weights <a class="yt-timestamp" data-t="00:40:28">[00:40:28]</a>.
*   **Adapter layers**: Instead of updating all 20 billion weights, only a small portion of "trainable weights" (the adapters) are changed <a class="yt-timestamp" data-t="00:48:27">[00:48:27]</a>. These low-rank matrices have significantly fewer parameters than the original model, enabling [[finetuning language models for specific tasks | fine-tuning]] with less GPU memory <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.
*   This approach also allows for easier sharing of fine-tuned models, as only the small adapter weights need to be distributed <a class="yt-timestamp" data-t="00:49:04">[00:49:04]</a>.

## Tools and Libraries
*   **TRL and PEFT**: Python modules for [[finetuning language models for specific tasks | fine-tuning]] and RLHF, aiming to make LLM [[finetuning language models for specific tasks | fine-tuning]] with reinforcement learning more accessible <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Hugging Face Accelerate**: Leveraged by TRL for distributed PPO <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
*   **Weights & Biases**: A platform useful for experiment tracking and creating living reports or model dashboards <a class="yt-timestamp" data-t="00:56:26">[00:56:26]</a>.

## Challenges and Considerations
*   **Hardware Requirements**: While techniques like [[finetuning with quantized models | 8-bit precision]] and LoRA can reduce memory, [[Training and finetuning processes for AI models | finetuning]] large models still often requires powerful GPUs (e.g., A100s with 80GB memory) rather than typical consumer GPUs <a class="yt-timestamp" data-t="00:53:15">[00:53:15]</a>.
*   **Open Source vs. Proprietary**: While open-source RL frameworks exist, companies like OpenAI, Google, and Meta are expected to develop their own libraries and tooling for RLHF, potentially overshadowing smaller bespoke libraries <a class="yt-timestamp" data-t="00:59:11">[00:59:11]</a>.
*   **Legal Uncertainty**: Using leaked models like Llama for commercial products can be legally ambiguous, as they may be intended for research purposes only <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
*   **Complexity of Distributed Training**: Applying model and data parallelism is complex, requiring a deep understanding of hardware and potential bottlenecks <a class="yt-timestamp" data-t="00:33:44">[00:33:44]</a>.
*   **Training Speed**: Improving [[Performance and efficiency in machine learning models | training speed]] often involves trade-offs and introduces additional complexity (e.g., adjusting learning rate, batch size, or optimizers) <a class="yt-timestamp" data-t="00:58:29">[00:58:29]</a>.