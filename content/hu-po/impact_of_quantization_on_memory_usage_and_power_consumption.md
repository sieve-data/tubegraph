---
title: Impact of quantization on memory usage and power consumption
videoId: 6wEVz0wkhCM
---

From: [[hu-po]] <br/> 

[[quantization and optimization in machine learning | Quantization]] is a fundamental concept in machine learning that involves reducing the precision of the numerical values (weights and activations) within a neural network <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. Conceptually, it's akin to compressing an image, where a 24-bit per pixel image can be reduced to 8 bits per pixel (appearing slightly grainier) or even 1 bit per pixel (resulting in a black and white image) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The goal is to use less information to represent the model while maintaining acceptable performance <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

## Reasons for Quantization

The primary motivations for quantizing machine learning models include:

### Reduced Memory Usage
The most immediate and significant benefit of [[quantization in large language models | quantization in large language models]] is the drastic reduction in memory requirements <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. When data type precision is lowered, less memory is needed to store the model's parameters <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. For instance, attempting to load a large model like CodeLlama34B onto typical consumer GPUs often fails due to insufficient memory <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. By quantizing a model from 32-bit precision down to 16, 8, or even 2 bits, the total memory required can be substantially reduced <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This enables larger models to fit into the memory of more accessible hardware, such as a single GPU with 48 gigabytes of memory <a class="yt-timestamp" data-t="00:53:51">[00:53:51]</a>.

### Lower Power Consumption
A less obvious but important benefit of quantization is the reduction in power consumption during inference <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Smaller neural networks, due to their reduced data precision and memory footprint, inherently require less power for computations <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. While not always a critical factor for individual use, the cumulative energy reduction becomes significant when considering widespread AI usage, such as millions of users constantly interacting with AI companions <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. In such scenarios, the energy savings from quantization are "not negligible" <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Other Efficiencies
Beyond memory and power, [[Quantization for large language models | quantization]] also leads to improved latency (faster computation as less data needs to be fetched) and reduces the required silicon area on chips <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. These factors collectively contribute to more efficient model deployment and operation.

## Advancements in 2-bit Quantization

The paper "QUIP: [[2bit quantization for machine learning models | 2-bit Quantization]] of Large Language Models with Guarantees" (July 2023 pre-print) introduces a method that achieves viable [[performance_and_implications_of_quantized_language_models | 2-bit quantization]] for large language models (LLMs) with minimal loss in accuracy <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>, <a class="yt-timestamp" data-t="01:53:50">[01:53:50]</a>. This is a significant leap beyond previous [[quantization_techniques_for_transformers | quantization techniques]] like QLoRA, which focused on 4-bit quantization <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>, <a class="yt-timestamp" data-t="00:46:57">[00:46:57]</a>.

QUIP employs a two-step process:
1.  **Adaptive Rounding:** Minimizes a quadratic proxy objective, which is a Taylor series approximation of the loss landscape for a specific layer <a class="yt-timestamp" data-t="01:50:03">[01:50:03]</a>, <a class="yt-timestamp" data-t="01:52:50">[01:52:50]</a>. This process determines whether to round a weight up or down more intelligently than simple "round to nearest" methods <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.
2.  **Incoherence Pre- and Post-processing:** Ensures that the weight and Hessian matrices are "incoherent" (non-correlated) by multiplying them with random orthogonal matrices <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>, <a class="yt-timestamp" data-t="01:50:24">[01:50:24]</a>. This "scrambling" of the matrices disrupts any existing relationships between them, which the paper theoretically and empirically demonstrates to be crucial for achieving high compression rates <a class="yt-timestamp" data-t="01:49:51">[01:49:51]</a>, <a class="yt-timestamp" data-t="01:51:15">[01:51:15]</a>.

## Quantization Performance and Model Size

Experiments using the QUIP method on OPT models (up to 30 billion parameters) showed remarkable results:
*   **2-bit Viability:** QUIP achieves viable 2-bit [[advancements_in_model_efficiency_through_quantization | quantization]] for LLMs, outperforming other baselines like OptQ <a class="yt-timestamp" data-t="00:51:30">[00:51:30]</a>.
*   **Scalability:** For larger models, the difference in performance (measured by perplexity or accuracy) between 2-bit quantized models and full 16-bit precision models becomes surprisingly small <a class="yt-timestamp" data-t="00:51:38">[00:51:38]</a>, <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>. This suggests that larger models might be inherently more robust to quantization <a class="yt-timestamp" data-t="00:51:55">[00:51:55]</a>, <a class="yt-timestamp" data-t="01:55:02">[01:55:02]</a>.
*   **Theoretical Guarantees:** Unlike many empirical machine learning algorithms, QUIP provides theoretical analysis guaranteeing its optimality within a class of adaptive rounding methods for LLM-sized models <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>, <a class="yt-timestamp" data-t="01:21:56">[01:21:56]</a>.

This observation hints at a potential future where even larger models (e.g., trillion-parameter models) could be quantized down to just one bit per weight, making them more accessible and dramatically reducing inference costs for major AI services like OpenAI <a class="yt-timestamp" data-t="01:56:39">[01:56:39]</a>, <a class="yt-timestamp" data-t="01:13:14">[01:13:14]</a>. This could be due to the intelligence of very large models residing more in their overall connectivity patterns rather than the precise values of individual weights <a class="yt-timestamp" data-t="01:55:52">[01:55:52]</a>.