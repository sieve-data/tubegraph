---
title: Finetuning machine learning models
videoId: nTdJEQLday0
---

From: [[hu-po]] <br/> 

## What is Finetuning?
[[Finetuning large language models | Finetuning]] is the process of taking a machine learning or deep learning model that has been trained for a long time on a large dataset and then training it for a little bit longer on a different, often smaller, dataset <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. This process falls within the broader sphere of training machine learning models <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

In contrast to [[finetuning_large_language_models | finetuning]], techniques like in-context learning or prompt engineering do not modify any of the model's parameters <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. When [[finetuning_large_language_models | finetuning]], gradients are actively pushed into the model, thereby changing its parameters <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### Finetuning with Reinforcement Learning from Human Feedback (RLHF)
RLHF is a technique that became popular after OpenAI stated they use it to [[finetuning_large_language_models | fine-tune]] their ChatGPT models <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. It aims to make [[finetuning_large_language_models | large language model finetuning]] more accessible <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. While the original training data and model size contribute most to an LLM's intelligence <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, RLHF is primarily used for AI safety and to ensure the output of LLMs aligns with specific desired tasks <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

The process of training a language model with RLHF involves three key steps <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>:
1.  **Fine-tune a pre-trained LLM:** This involves [[finetuning_large_language_models | finetuning]] the model on a smaller, cleaner dataset of human instructions and demonstrations <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
2.  **Collect human annotated data and train a reward model:** A separate model (often another LLM) is trained to predict the reward for any given state and action (e.g., how "good" an LLM's answer is to a human prompt) <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Human labelers rank model outputs to provide this learning signal <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
3.  **Fine-tune the LLM using the reward model and data with Reinforcement Learning (RL):** The LLM is further [[finetuning_large_language_models | fine-tuned]] using the reward model, typically with algorithms like Proximal Policy Optimization (PPO) <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>, <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. This step allows the model to "self-supervise" and improve its outputs based on the predicted rewards <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

A potential downside of RLHF, similar to [[selfimproving_machine_learning_models | transfer learning]], is the problem of "catastrophic forgetting," where [[finetuning_large_language_models | fine-tuning]] on specific human feedback datasets might reduce a model's ability to generalize <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

## Efficiency Considerations and [[techniques_for_efficient_model_finetuning | Techniques for Efficient Model FineTuning]]
[[techniques_for_efficient_model_finetuning | Finetuning large language models]] presents significant challenges, primarily related to fitting the model and its optimizer states on available GPU memory <a class="yt-timestamp" data-t="00:28:40">[00:28:40]</a>.

### Hardware Requirements
The memory required by a model depends on its size (number of parameters) and the precision (data type) of its parameters <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. For example, a 20-billion parameter model requires 80 gigabytes (GB) in float32 precision, 40 GB in float16, and 20 GB in int8 <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>. Consumer GPUs typically do not have 80 GB of memory <a class="yt-timestamp" data-t="00:45:15">[00:45:15]</a>.

### Scaling Strategies
Training at scale is challenging, but various parallelism techniques help distribute the computational load <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>:
*   **Data Parallelism:** The same model is replicated across multiple machines, and each instance processes a different batch of training data <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>, <a class="yt-timestamp" data-t="00:32:25">[00:32:25]</a>.
*   **Model Parallelism (Pipeline and Tensor Parallelism):** The model itself is distributed across multiple machines. Pipeline parallelism splits the model layer-wise, while tensor parallelism splits operations within layers across GPUs <a class="yt-timestamp" data-t="00:30:47">[00:30:47]</a>, <a class="yt-timestamp" data-t="00:32:36">[00:32:36]</a>. Sharding, the process of dividing a large blob of data into smaller ones, is often used to share model weights across devices <a class="yt-timestamp" data-t="00:33:23">[00:33:23]</a>.

Other [[techniques_for_efficient_model_finetuning | techniques for efficient model finetuning]] include:
*   **Fused Kernels:** Combining multiple mathematical operations into a single GPU kernel for better performance <a class="yt-timestamp" data-t="00:34:45">[00:34:45]</a>.
*   **8-bit Matrix Multiplication:** Introduced in the "LLM.int8()" paper, this method aims to solve performance degradation issues when quantizing large models <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>. It intelligently performs parts of the matrix multiplication in float16 and other, non-outlier parts in int8 <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.
*   **Low-Rank Adaptation (LoRA) / Parameter-Efficient Finetuning (PEFT):** This technique, demonstrated in the "LoRA: Low-Rank Adaptation of Large Language Models" paper, allows [[finetuning_large_language_models | fine-tuning]] by freezing most of the pre-trained weights and only training smaller, "low-rank" versions of specific attention matrices (query and value layers) <a class="yt-timestamp" data-t="00:39:39">[00:39:39]</a>, <a class="yt-timestamp" data-t="00:47:41">[00:47:41]</a>. These low-rank matrices have significantly fewer parameters, drastically reducing memory requirements <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>, <a class="yt-timestamp" data-t="00:48:57">[00:48:57]</a>. Libraries like PEFT support the creation and [[finetuning_large_language_models | fine-tuning]] of these adapter layers <a class="yt-timestamp" data-t="00:43:24">[00:43:24]</a>.

## Tools and Libraries
Several libraries facilitate [[finetuning_large_language_models | large language model finetuning]]:
*   **HuggingFace:** Provides a platform for accessing and training models <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   **TRL:** A library designed to simplify the RL step in [[finetuning_large_language_models | RLHF finetuning]], making it more accessible for custom datasets <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. It uses Accelerate from Hugging Face for distributed training <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **PEFT:** A Hugging Face library specifically for parameter-efficient [[finetuning_large_language_models | fine-tuning]], supporting adapter layers <a class="yt-timestamp" data-t="00:43:24">[00:43:24]</a>.
*   **Weights & Biases:** A company that offers tools for experiment tracking and creating dynamic reports for machine learning projects <a class="yt-timestamp" data-t="00:56:20">[00:56:20]</a>.

## Example Finetuning Process
An example of [[finetuning_large_language_models | fine-tuning]] a 20-billion parameter GPT Neo X model on a single 24 GB GPU involves <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>, <a class="yt-timestamp" data-t="00:52:59">[00:52:59]</a>:
1.  Loading the active model in 8-bit precision to fit it into memory <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>.
2.  Adding extra trainable parameters (low-rank adapters) <a class="yt-timestamp" data-t="00:47:41">[00:47:41]</a>.
3.  [[Finetuning_large_language_models | Fine-tuning]] the low-rank adapter on a frozen 8-bit model for text generation on a dataset like IMDb <a class="yt-timestamp" data-t="00:51:37">[00:51:37]</a>. The IMDb dataset contains movie reviews, often used for sentiment analysis tasks <a class="yt-timestamp" data-t="00:52:05">[00:52:05]</a>.
4.  Merging the adapted layers into the base model's weights <a class="yt-timestamp" data-t="00:52:22">[00:52:22]</a>.
5.  Using a pre-trained sentiment classifier (like an IMDb sentiment classifier) to provide rewards for the RL algorithm <a class="yt-timestamp" data-t="00:55:08">[00:55:08]</a>.

While the example suggests a 24 GB consumer GPU is possible, the full training rounds were actually undertaken on an NVIDIA A100 GPU (80 GB of memory), an enterprise-grade GPU typically found in cloud environments <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>, <a class="yt-timestamp" data-t="00:53:15">[00:53:15]</a>, <a class="yt-timestamp" data-t="00:53:42">[00:53:42]</a>. Training often involves multiple "epochs," meaning the model has been trained on the entire dataset multiple times <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>.

The future of [[finetuning_large_language_models | finetuning]] large language models will likely see major companies like Google and Microsoft developing their own integrated tools and libraries, potentially rendering smaller, specialized libraries less critical <a class="yt-timestamp" data-t="00:59:08">[00:59:08]</a>.