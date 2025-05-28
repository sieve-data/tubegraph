---
title: Performance and implications of quantized language models
videoId: YEm4tuo2HPA
---

From: [[hu-po]] <br/> 

## Introduction to Quantization

[[quantization_for_large_language_models | Quantization]] is a process used in machine learning to reduce the precision of numbers representing a model's parameters, thereby decreasing memory usage and increasing computational speed during inference <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. Any number on a computer is represented by a certain amount of bits, and the precision depends on the number of storage places used <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>. For example, a Floating Point 16 (FP16 or Bfloat16) uses 16 bits, while Integer 4 (Int 4) uses 4 bits <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.

The core idea behind [[quantization_in_large_language_models | quantization]] is to store model parameters (weights) in lower bit formats (e.g., from 16 bits to 4 bits), significantly reducing the memory footprint <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a> and making models smaller and faster <a class="yt-timestamp" data-t="00:50:28">[00:50:28]</a>. This is particularly useful for deploying models on resource-limited devices like mobile phones <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

## Quantization Techniques and Their Impact

Various [[advancements_in_model_efficiency_through_quantization | quantization]] techniques exist, each with its own tricks <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. Some of these include:
*   RTN (Round to Nearest) <a class="yt-timestamp" data-t="00:51:37">[00:51:37]</a>
*   AWQ (Activation-aware Weight Quantization) <a class="yt-timestamp" data-t="00:51:37">[00:51:37]</a>
*   SmoothQuant <a class="yt-timestamp" data-t="00:51:37">[00:51:37]</a>
*   BiLLM (Binarized Large Language Models) <a class="yt-timestamp" data-t="00:51:42">[00:51:42]</a>
*   PTQ (Post-Training Quantization) <a class="yt-timestamp" data-t="00:51:42">[00:51:42]</a> <a class="yt-timestamp" data-t="01:11:14">[01:11:14]</a>
*   QLoRA <a class="yt-timestamp" data-t="00:51:44">[00:51:44]</a>
*   IRQ-LoRA <a class="yt-timestamp" data-t="00:51:44">[00:51:44]</a>
*   LoRA-FT (LoRA Fine-Tuning Quantization) <a class="yt-timestamp" data-t="00:51:46">[00:51:46]</a> <a class="yt-timestamp" data-t="01:11:17">[01:11:17]</a>

### Performance Degradation

When a model is quantized, it generally loses some information due to the reduced precision, which can lead to performance degradation <a class="yt-timestamp" data-t="00:52:26">[00:52:26]</a>. For example, a Llama 3 model quantized down to [[2bit_quantization_for_machine_learning_models | 2 bits]] saw its performance score drop from 68 (for 16-bit) to 34 <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>. While a 4-bit quantization might only result in a small drop (e.g., from 68 to 64), ultra-low bit widths like 2 bits can cause a significant performance loss <a class="yt-timestamp" data-t="00:52:51">[00:52:51]</a> <a class="yt-timestamp" data-t="01:10:33">[01:10:33]</a>.

### Compensating with Fine-tuning

Historically, techniques like LoRA fine-tuning could compensate for performance loss after quantization <a class="yt-timestamp" data-t="01:15:37">[01:15:37]</a>. In Llama 1 and Llama 2, a heavily quantized model (e.g., 4-bit) could, with LoRA fine-tuning, surpass the performance of its original 16-bit floating point counterpart <a class="yt-timestamp" data-t="01:17:42">[01:17:42]</a>.

However, this phenomenon has changed with Llama 3. Despite the use of [[finetuning_with_quantized_models | finetuning with quantized models]] (LoRA-FT), a quantized Llama 3 model cannot reach the performance of the original 16-bit Llama 3 <a class="yt-timestamp" data-t="01:18:10">[01:18:10]</a>. This suggests that Llama 3, due to its massive pre-training on 15 trillion tokens, is more "fragile" to quantization <a class="yt-timestamp" data-t="01:18:19">[01:18:19]</a> <a class="yt-timestamp" data-t="01:19:39">[01:19:39]</a>. Older models (Llama 1 and 2) might have been "undertrained" or had "too much capacity" for their datasets, making them more robust to such "surgeries" like pruning or quantization <a class="yt-timestamp" data-t="01:19:51">[01:19:51]</a>.

## Case Studies

### Microsoft's F3 Model

Microsoft's F3 Mini model, a 3.8 billion parameter model, is trained on 3.3 trillion tokens <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>. It is designed for local deployment on devices like the iPhone 14 <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>. To achieve this, F3 is quantized to 4 bits, reducing its memory footprint to approximately 1.8 GB <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a> and allowing it to generate around 12 tokens per second <a class="yt-timestamp" data-t="00:50:37">[00:50:37]</a>.

### Llama 3 Quantization Study

A paper titled "How Good Are Low Bit Quantized Llama 3 Models: An Empirical Study" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>, published shortly after the Llama 3 release, evaluated 10 existing [[quantization_for_large_language_models | post-training quantization]] and LoRA fine-tuning methods <a class="yt-timestamp" data-t="01:10:17">[01:10:17]</a>. The study revealed that while Llama 3 still outperforms Llama 1 and 2 after quantization, it suffers "non-negligent degradation" in performance, especially at ultra-low bit widths <a class="yt-timestamp" data-t="01:10:31">[01:10:31]</a>. This contrasts with previous Llama versions where quantization combined with LoRA-FT could yield better results than the full-precision model <a class="yt-timestamp" data-t="01:17:34">[01:17:34]</a>.

## Implications for GPU Hardware

The effectiveness of [[quantization_for_large_language_models | quantization]] has significant implications for GPU hardware design <a class="yt-timestamp" data-t="01:23:06">[01:23:06]</a>.
*   **Bifurcation Theory:** If [[quantization_in_large_language_models | quantization]] works very well (i.e., models can be heavily quantized without significant performance loss), it could lead to a bifurcation of the GPU market:
    *   **Inference GPUs:** Designed specifically for extremely small data types (e.g., 2-bit), optimized for speed and [[impact_of_quantization_on_memory_usage_and_power_consumption | memory usage]], like Groq's chips <a class="yt-timestamp" data-t="01:23:51">[01:23:51]</a>.
    *   **Training GPUs:** Designed to support higher precision data types (e.g., 16-bit or 8-bit) necessary for training, like Nvidia's H100s <a class="yt-timestamp" data-t="01:23:36">[01:23:36]</a>. In this scenario, Nvidia could lose market share in the inference space <a class="yt-timestamp" data-t="01:26:05">[01:26:05]</a>.
*   **Unified GPU Market:** If quantization doesn't work as well, and future models like Llama 4 or Llama 5 remain sensitive to quantization, then inference might continue to be performed at 16-bit precision <a class="yt-timestamp" data-t="01:24:51">[01:24:51]</a>. In this case, there would be less need for specialized inference GPUs, allowing Nvidia, whose GPUs are designed for higher precision, to continue dominating the market <a class="yt-timestamp" data-t="01:25:01">[01:25:01]</a> <a class="yt-timestamp" data-t="01:25:46">[01:25:46]</a>.

The future of the GPU market and the role of [[efficiency_of_large_language_models | quantization]] remain turbulent and yet to be determined <a class="yt-timestamp" data-t="01:25:05">[01:25:05]</a>.