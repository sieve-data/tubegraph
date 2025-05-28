---
title: Role of lowrank adapters Laura for efficient AI training
videoId: pov3pLFMOPY
---

From: [[hu-po]] <br/> 

[[LowRank Adaptation in Machine Learning | LowRank Adaptation]] (LoRA) is a technique that significantly reduces the memory footprint and computational requirements for fine-tuning large AI models, particularly Large Language Models (LLMs) <a class="yt-timestamp" data-t="0:06:40">[00:06:40]</a>. It enables fine-tuning of massive models on hardware that would otherwise be insufficient <a class="yt-timestamp" data-t="0:07:36">[00:07:36]</a>.

## How LoRA Works
Instead of fine-tuning the entire pre-trained model, LoRA introduces a small set of trainable parameters, known as "adapters" <a class="yt-timestamp" data-t="0:53:50">[00:53:50]</a>. The core concept is to freeze the original, large model's weights and only train these much smaller LoRA adapters <a class="yt-timestamp" data-t="0:06:55">[00:06:55]</a>.

During fine-tuning, gradients are pushed only into these LoRA parameters <a class="yt-timestamp" data-t="0:06:56">[00:06:56]</a>. The original model's weights remain fixed <a class="yt-timestamp" data-t="0:53:54">[00:53:54]</a>. The output of the LoRA adapters is then combined with the output of the original model, allowing the large model's behavior to be subtly adjusted by the small, trained LoRA weights <a class="yt-timestamp" data-t="0:57:53">[00:57:53]</a>.

## Efficiency and Performance
LoRA's primary benefit is its efficiency. It drastically reduces memory usage, making fine-tuning feasible on consumer-grade [[hardware_for_ai_training_and_deployment | GPUs]] <a class="yt-timestamp" data-t="0:07:37">[00:07:37]</a>. For example, fine-tuning a 65-billion parameter LLaMA model at 16-bit precision typically requires over 780 gigabytes (GB) of GPU memory <a class="yt-timestamp" data-t="0:17:15">[00:17:15]</a>. With quantized LoRA (Q-LoRA), this requirement can be reduced to less than 48 GB <a class="yt-timestamp" data-t="0:20:18">[00:20:18]</a>, allowing it to fit on a single 48GB GPU like an NVIDIA A6000 or L40 <a class="yt-timestamp" data-t="0:31:07">[00:31:07]</a>.

Despite this aggressive memory reduction, LoRA-based fine-tuning can preserve the full 16-bit fine-tuning task performance <a class="yt-timestamp" data-t="0:05:29">[00:05:29]</a>. This means models fine-tuned with LoRA can achieve performance comparable to models fine-tuned with traditional, memory-intensive methods <a class="yt-timestamp" data-t="0:20:25">[00:20:25]</a>. The Guanaco model, a LoRA-fine-tuned LLaMA, achieved 99.3% of ChatGPT's performance level on the Vicuna Benchmark after just 24 hours of fine-tuning on a single GPU <a class="yt-timestamp" data-t="0:08:35">[00:08:35]</a>.

## Q-LoRA: Quantization and LoRA
Q-LoRA is an advanced version of LoRA that combines it with quantization techniques for even greater memory efficiency. Key innovations in Q-LoRA include:
*   **4-bit NormalFloat (NF4):** A new 4-bit data type optimized for normally distributed weights found in neural networks <a class="yt-timestamp" data-t="0:10:31">[00:10:31]</a>. It's designed to be information-theoretically optimal for zero-mean normal distributions <a class="yt-timestamp" data-t="1:13:38">[01:13:38]</a>.
*   **Double Quantization:** This technique quantizes the quantization constants themselves, further reducing the memory footprint by approximately 0.37 bits per parameter (around 3GB for a 65B model) <a class="yt-timestamp" data-t="0:27:39">[00:27:39]</a>.
*   **Paged Optimizers:** Utilizing NVIDIA Unified Memory, paged optimizers manage memory spikes during gradient checkpointing, preventing out-of-memory errors that traditionally hinder fine-tuning of large models <a class="yt-timestamp" data-t="0:32:05">[00:32:05]</a>. These optimizers can store intermediate values in CPU RAM when GPU memory runs out, retrieving them as needed <a class="yt-timestamp" data-t="1:33:55">[01:33:55]</a>.

In Q-LoRA training, the large base model weights are stored in 4-bit NF4 precision, and the quantization constants are stored in 8-bit float (FP8) precision. During computation, these quantized weights are de-quantized to 16-bit Brain Float (BF16) for matrix multiplications, while the LoRA adapter weights themselves are typically stored and updated in BF16 precision <a class="yt-timestamp" data-t="1:37:05">[01:37:05]</a>.

## Hyperparameter Considerations
Research has shown that the most critical hyperparameter for LoRA is the *number* of LoRA adapters used, specifically applying LoRA to *all* linear Transformer block layers <a class="yt-timestamp" data-t="1:58:50">[01:58:50]</a>. This comprehensive application across layers is necessary to match full 16-bit fine-tuning performance <a class="yt-timestamp" data-t="1:59:03">[01:59:03]</a>. Conversely, other LoRA hyperparameters, such as the projection dimension (rank 'R'), do not significantly affect performance <a class="yt-timestamp" data-t="1:59:42">[01:59:42]</a>.

## [[Applications of LowRank Adaptation | Applications]] and Impact
While prominently used for LLMs, the principles of LoRA and Q-LoRA can extend to other domains. For instance, [[applications_of_lowrank_adaptation | ControlNet]], a technique for controlling diffusion models, utilizes a similar approach of freezing a pre-trained model and adding small, trainable networks on top <a class="yt-timestamp" data-t="2:15:15">[02:15:15]</a>. This suggests that [[applications_of_lowrank_adaptation | LoRA and quantization techniques]] could also be applied to vision models like stable diffusion for efficient fine-tuning <a class="yt-timestamp" data-t="2:16:03">[02:16:03]</a>.

The widespread adoption of LoRA and Q-LoRA has a profound impact on the AI community. By significantly lowering the computational barrier to fine-tuning large models, it democratizes AI research and development. Independent researchers and smaller organizations can now fine-tune state-of-the-art models on consumer-grade hardware, fostering innovation outside of large industry labs <a class="yt-timestamp" data-t="2:57:41">[02:57:41]</a>. This is considered a "huge win for the open-source community" <a class="yt-timestamp" data-t="2:57:50">[02:57:50]</a>.