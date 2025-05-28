---
title: Large Language Models LLMs and scaling
videoId: nTdJEQLday0
---

From: [[hu-po]] <br/> 

[[LLM Large Language Models development | Large Language Models (LLMs)]] are a type of machine learning model that power popular AI tools like ChatGPT, Google's Palm, and Meta's LLaMA <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. These models vary in size, often measured by their number of parameters <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. For instance, a 20 billion parameter model is discussed in the context of [[finetuning_large_language_models | fine-tuning]] <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.

## Memory Requirements and GPU Usage

[[Large Language Models LLMs and scaling | Scaling]] [[LLM Large Language Models development | LLMs]] for training and inference requires significant memory, primarily on Graphics Processing Units (GPUs) <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.
*   **GPU Memory** The larger the model, the more memory is needed on the GPU to fit it <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
    *   A 24 gigabyte GPU is considered high-end consumer hardware, typically costing over a thousand dollars <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.
    *   [[large_language_models_in_machine_learning_research | Machine learning research]] often utilizes GPUs like the A100s, which are significantly more powerful and expensive than consumer-grade options <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.
    *   A 10 billion parameter model in full (float32) precision would require up to 40 gigabytes of GPU memory <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>. A 20 billion parameter model in float32 would take 80 gigabytes <a class="yt-timestamp" data-t="45:01:00">[45:01:00]</a>.

## Precision and Quantization

The amount of GPU memory a single parameter takes depends on its precision (d-type), commonly float32 <a class="yt-timestamp" data-t="28:46:00">[28:46:00]</a>.
*   **Float32 (Full Precision)** Requires 32 bits per number, meaning each billion parameters costs 4 gigabytes <a class="yt-timestamp" data-t="29:01:00">[29:01:00]</a>, <a class="yt-timestamp" data-t="29:21:00">[29:21:00]</a>. A 20 billion parameter model would require 80 gigabytes <a class="yt-timestamp" data-t="45:01:00">[45:01:00]</a>.
*   **Float16 (Half Precision)** Uses 16 bits per number, effectively halving memory requirements. A 20 billion parameter model would fit into 40 gigabytes <a class="yt-timestamp" data-t="45:19:00">[45:19:00]</a>, <a class="yt-timestamp" data-t="29:06:00">[29:06:00]</a>.
*   **Int8 and 4-bit Quantization** More recently, exotic precisions like int8 (8 bits) and even 4-bit are supported, significantly reducing memory <a class="yt-timestamp" data-t="29:13:00">[29:13:00]</a>, <a class="yt-timestamp" data-t="17:22:00">[17:22:00]</a>.
    *   A 20 billion parameter model in int8 could fit in 20 gigabytes <a class="yt-timestamp" data-t="45:28:00">[45:28:00]</a>.
    *   Using 4-bit data types would bring it down to 10 gigabytes, making it accessible to a broader range of consumer GPUs <a class="yt-timestamp" data-t="45:49:00">[45:49:00]</a>.
    *   **Performance Degradation** Quantization can lead to performance degradation because it reduces the precision of the model's parameters <a class="yt-timestamp" data-t="36:41:00">[36:41:00]</a>.
    *   **8-bit Matrix Multiplication** Techniques like this, introduced in the "LLM in 8-bit" paper, aim to mitigate performance degradation by performing matrix multiplications in stages: outlier hidden states in float16 and non-outlier parts in int8 <a class="yt-timestamp" data-t="37:57:00">[37:57:00]</a>, <a class="yt-timestamp" data-t="38:24:00">[38:24:00]</a>. This intelligent use of different data types helps save memory and improve model size on a single GPU <a class="yt-timestamp" data-t="39:15:00">[39:15:00]</a>.

## Optimizers

Optimizers are crucial for [[Large Language Models and Optimization | Large Language Models and Optimization]]. AdamW is a very popular and common optimizer used in model training <a class="yt-timestamp" data-t="39:38:00">[39:38:00]</a>.

## Distributed Training and Parallelism

[[Large Language Models LLMs and scaling | Scaling]] [[LLM Large Language Models development | LLM]] training often involves parallelizing the process across multiple machines <a class="yt-timestamp" data-t="30:01:00">[30:01:00]</a>.
*   **Data Parallelism** The most straightforward strategy, where the same model is replicated on several machines, and each instance is fed a different batch of data <a class="yt-timestamp" data-t="31:10:00">[31:10:00]</a>, <a class="yt-timestamp" data-t="32:25:00">[32:25:00]</a>.
*   **Model Parallelism** Involves splitting the model itself across multiple computers, with each compute node calculating only a portion of the gradients for a specific part of the model <a class="yt-timestamp" data-t="30:45:00">[30:45:00]</a>, <a class="yt-timestamp" data-t="31:06:00">[31:06:00]</a>.
    *   **Pipeline Parallelism** Splits the model layer-wise <a class="yt-timestamp" data-t="32:42:00">[32:42:00]</a>.
    *   **Tensor Parallelism** Splits tensor operations across GPUs <a class="yt-timestamp" data-t="32:45:00">[32:45:00]</a>.
*   **Sharding** The process of taking one large blob of data (like model weights) and turning it into smaller blobs to be sent to different machines <a class="yt-timestamp" data-t="33:23:00">[33:23:00]</a>.
*   Implementing these parallel strategies and defining communication protocols is non-trivial and often requires a deep understanding of the specific hardware being used <a class="yt-timestamp" data-t="33:36:00">[33:36:00]</a>. Hardware like Nvidia GPUs, Google's TPUs, and Tesla's Dojo chips all have different bottlenecks and characteristics that influence optimal distribution strategies <a class="yt-timestamp" data-t="34:03:00">[34:03:00]</a>.
*   **Fused Kernels** Optimizing mathematical concepts into GPU-executable code (kernels) and fusing multiple operations into a single kernel can significantly increase speed <a class="yt-timestamp" data-t="34:47:00">[34:47:00]</a>.

## Efficient [[finetuning_large_language_models | Fine-tuning]] with PEFT and LoRA

[[Large Language Models LLMs and scaling | Scaling]] fine-tuning can be done more efficiently using techniques that reduce memory requirements.
*   **Low-Rank Adaptation (LoRA)** This technique allows [[finetuning_large_language_models | fine-tuning]] [[LLM Large Language Models development | LLMs]] by freezing most of the pre-trained weights and only creating low-rank versions of the query and value layer attention matrices, which have significantly fewer parameters <a class="yt-timestamp" data-t="39:41:00">[39:41:00]</a>.
    *   "Freezing" weights means preventing gradients from changing their values, often applied to the bulk of the model, allowing only a small "top" portion to be fine-tuned <a class="yt-timestamp" data-t="39:55:00">[39:55:00]</a>.
*   **Parameter-Efficient Fine-Tuning (PEFT)** A Hugging Face library designed to support the creation and [[finetuning_large_language_models | fine-tuning]] of adapter layers on [[LLM Large Language Models development | LLMs]], leveraging techniques like LoRA <a class="yt-timestamp" data-t="43:26:00">[43:26:00]</a>.
    *   PEFT allows loading a model in 8-bit precision by simply adding `load_in_8bit=True` when calling the `from_pretrained` method <a class="yt-timestamp" data-t="46:09:00">[46:09:00]</a>.
    *   It also enables the use of the same model to get both reference and active logits for PPO (Proximal Policy Optimization) without needing two copies of the model, by disabling adapters <a class="yt-timestamp" data-t="50:45:00">[50:45:00]</a>.

## Reinforcement Learning with Human Feedback (RLHF)

RLHF is a technique that has gained popularity, particularly with OpenAI's use of it to [[finetuning_large_language_models | fine-tune]] their ChatGPT models <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   While [[LLM Large Language Models development | LLMs]] combined with RLHF seem to be the next go-to approach for building powerful AI systems like ChatGPT, the primary intelligence of an [[LLM Large Language Models development | LLM]] comes from its original pre-training on vast datasets <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>, <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.
*   RLHF is more about [[large_language_models_and_optimization | AI safety]] and ensuring the [[LLM Large Language Models development | LLM]]'s output aligns with specific desired outcomes <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
*   There is speculation that RLHF could potentially hurt [[LLM Large Language Models development | LLM]] performance on tasks unrelated to the fine-tuning objectives, similar to catastrophic forgetting in transfer learning <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.

### Three Steps of RLHF Training
1.  **Fine-tune a pre-trained [[LLM Large Language Models development | LLM]] with supervised learning:** This involves using a relatively smaller, clean dataset of instructions and human demonstrations (human feedback) to fine-tune the model <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>, <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>.
2.  **Collect human annotated data and train a reward model:** Human labelers rank various [[LLM Large Language Models development | LLM]] outputs given a prompt, providing a learning signal for a reward model (or value function). This model predicts how "good" an [[LLM Large Language Models development | LLM]]'s answer is, given a human prompt <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>, <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>, <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.
3.  **Fine-tune the [[LLM Large Language Models development | LLM]] from Step 1 with the reward model using Reinforcement Learning (RL):** The reward model is used to continuously push gradients into the [[LLM Large Language Models development | LLM]], updating its parameters <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>, <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.
    *   **PPO (Proximal Policy Optimization)** A common and relatively easy-to-implement [[large_language_models_and_optimization | reinforcement learning algorithm]] that is often tried first <a class="yt-timestamp" data-t="12:07:00">[12:07:00]</a>, <a class="yt-timestamp" data-t="12:49:00">[12:49:00]</a>.
    *   In an RLHF setup, there can be three different function approximators: the reward model, the supervised policy (often a deep learning model), and the actual [[LLM Large Language Models development | large language model]] <a class="yt-timestamp" data-t="14:58:00">[14:58:00]</a>.

### TRL Library
TRL is a library designed to make the RL step for [[LLM Large Language Models development | LLM]] [[finetuning_large_language_models | fine-tuning]] easier and more accessible, specifically enabling the use of PPO in a distributed manner <a class="yt-timestamp" data-t="17:40:00">[17:40:00]</a>, <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>. It appears to implement PPO internally rather than relying on external [[large_language_models_and_optimization | reinforcement learning libraries]] like OpenAI Gym or RL Baselines, which offer a wider array of algorithms <a class="yt-timestamp" data-t="19:23:00">[19:23:00]</a>.

## Future Outlook

While techniques like PEFT and 8-bit multiplication make [[LLM Large Language Models development | LLM]] [[finetuning_large_language_models | fine-tuning]] more accessible, particularly on consumer GPUs like a 24 GB Nvidia 4090, large-scale training often still relies on enterprise-grade hardware like the A100 (80GB memory) <a class="yt-timestamp" data-t="52:59:00">[52:59:00]</a>, <a class="yt-timestamp" data-t="53:15:00">[53:15:00]</a>, <a class="yt-timestamp" data-t="53:42:00">[53:42:00]</a>. The complexity of multi-GPU scaling and optimizing training speed remains a challenge, with various trade-offs involved <a class="yt-timestamp" data-t="57:35:00">[57:35:00]</a>, <a class="yt-timestamp" data-t="58:29:00">[58:29:00]</a>. It is expected that major companies like Google and Microsoft will develop their own robust tooling for RLHF and related processes <a class="yt-timestamp" data-t="59:08:00">[59:08:00]</a>.