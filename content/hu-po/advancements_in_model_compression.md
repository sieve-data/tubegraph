---
title: Advancements in Model Compression
videoId: HcE3I_iCvoI
---

From: [[hu-po]] <br/> 

Recent research highlights significant advancements in making AI models, particularly Transformers, smaller and more efficient without sacrificing performance. This progress is crucial for reducing deployment costs, increasing inference speed, and making powerful AI more accessible on diverse hardware <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. These advancements stem from two primary areas: identifying and reducing redundancy within model architectures, and optimizing data precision through quantization.

## Architectural Redundancy and Pruning

Transformer models, while powerful, contain significant architectural redundancies that can be exploited for compression. Studies have empirically investigated which components of a Transformer are most critical to performance <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### What Matters in Transformers: Not All Attention is Needed

A paper from the University of Maryland, released in October 2024, explored redundancy across Transformer modules, including blocks, Multi-Layer Perceptrons (MLPs), and attention layers <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The researchers conducted an "ablation study" by dropping (deleting) different parts of trained Transformers to observe the impact on performance <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

Key findings include:
*   **Block Removal**: Removing entire Transformer blocks leads to significant performance degradation <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **MLP Layers**: Dropping MLP (feed-forward network) layers negatively affects performance <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Attention Layers**: A large portion of attention layers exhibit excessively high similarity and can be pruned without degrading performance <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Llama 2 70B, for example, achieved a 50% speedup with only a 3% performance drop by pruning half of its attention layers <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. This indicates a high degree of redundancy in these layers <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Layer Importance**: The first and last layers of MLP and attention modules tend to be more important than the middle layers <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>. This suggests an "hourglass" shape for optimal pruning, where early and late layers are retained, but middle layers are heavily pruned <a class="yt-timestamp" data-t="00:30:28">[00:30:28]</a>.
*   **Methodology**: Redundant layers are identified using cosine similarity scores, dropping layers that show high similarity in their features <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

The presence of redundancy in Transformers might also explain their powerful generality; multiple paths for information flow make them robust <a class="yt-timestamp" data-t="00:39:31">[00:39:31]</a>. This phenomenon is reminiscent of dropout regularization techniques, which promote redundant information encoding for robustness <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.

### PyramidDrop: Visual Redundancy Reduction

The "PyramidDrop" paper, published in October 2024, focuses on [[recent_advancements_in_multimodal_model_architectures | Vision-Language Models (VLMs)]] (also called LVLMs or MMLMs) <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. It reveals that while visual tokens in shallow layers are necessary, token redundancy progressively increases in deeper layers of the model <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.

Images inherently contain substantial spatial redundancy, which, when converted into a sequence of tokens for a Transformer, leads to excessive and unnecessary computation <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>. For example, many "sky tokens" in an image result in wasted attention calculations between redundant elements <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>. This problem is compounded by the quadratic increase in image tokens with higher resolution, leading to a "double quadratic curse" <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>.

PyramidDrop addresses this by dividing the Visual Transformer (ViT) into stages and progressively dropping image tokens at the end of each stage based on a predefined ratio <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. This creates a pyramid-like structure where sparsity increases with layer depth <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. This approach yields significant benefits for LLaVA-NeXT:
*   40% reduction in training time <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   55% acceleration in inference FLOPs (floating point operations) <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   Crucially, performance often remains comparable or can even improve after dropping tokens <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>, challenging the "scale is all you need" paradigm <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.

## Quantization for Efficient Inference

Beyond architectural pruning, [[advancements_in_model_efficiency_through_quantization | quantization]] is a key technique for [[energy_and_compute_optimization_in_ai_models | optimizing energy and compute]] in AI models.

### One-bit AI Infra Part 1.1: Fast and Lossless BitNet b 1.58 Inference on CPUs

A Microsoft Research paper, "One-bit AI Infra Part 1.1," demonstrates how to achieve fast and lossless inference of ternary (1.58-bit) BitNet LLMs on CPUs <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>. This involves reducing the precision of model weights from full-precision (e.g., 16 or 32-bit floats) to much smaller, rounded values like -1, 0, or 1 <a class="yt-timestamp" data-t="00:53:20">[00:53:20]</a>.

Benefits of this approach:
*   **Memory and Bandwidth Savings**: Storing weights with fewer bits (e.g., 2 bits instead of 32) significantly reduces memory footprint and data transfer requirements <a class="yt-timestamp" data-t="00:53:57">[00:53:57]</a>.
*   **Accelerated Matrix Multiplication**: Specialized kernels (i2s, tl1, tl2) are designed for very fast and efficient matrix multiplications on CPUs <a class="yt-timestamp" data-t="00:52:13">[00:52:13]</a>. When weights are quantized to -1, 0, or 1, calculations can be simplified or replaced with lookup tables, where pre-calculated results for common operations are stored and retrieved instead of computed on the fly <a class="yt-timestamp" data-t="00:55:08">[00:55:08]</a>.
*   **Significant Speedups**: This results in up to a 6x speedup on x86 CPUs and a 5x speedup on ARM CPUs <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>.
*   **Performance Retention/Gain**: Similar to pruning, quantization can sometimes lead to an improvement in model performance, alongside significant speedups <a class="yt-timestamp" data-t="01:07:11">[01:07:11]</a>.
*   **Energy Efficiency**: Reducing computation directly translates to reduced energy consumption, which is critical given the increasing energy demands of large AI models <a class="yt-timestamp" data-t="01:08:50">[01:08:50]</a>.
*   **Portability**: Post-training quantization (PTQ) methods allow models to be optimized for specific use cases or private datasets without requiring access to the original training data, enhancing privacy and enabling on-device optimization <a class="yt-timestamp" data-t="01:05:09">[01:05:09]</a>.

## [[Implications of AI model scaling and convergence | Implications of AI Model Scaling and Convergence]]

These advancements in model compression and efficiency are not isolated; they stack to create a multiplicative effect on performance gains <a class="yt-timestamp" data-t="00:57:49">[00:57:49]</a>. The combination of architectural pruning and low-bit quantization suggests a future where incredibly powerful AI models can run on very small and inexpensive hardware. This has profound implications:

*   **Democratization of AI**: The ability to run advanced AI (potentially even [[selfimprovement_in_ai_models | AGI]]) on devices like cell phones or Raspberry Pis dramatically lowers the barrier to entry, making AI ubiquitous and difficult to control centrally <a class="yt-timestamp" data-t="01:29:47">[01:29:47]</a>.
*   **Leveraging Existing Infrastructure**: Efficient models can run on existing CPU-heavy data centers, reducing the need for massive investments in new GPU infrastructure <a class="yt-timestamp" data-t="01:28:44">[01:28:44]</a>.
*   **Challenging "Scale is All You Need"**: The consistent observation that smaller, pruned, or quantized models can match or even surpass the performance of larger, unoptimized counterparts directly challenges the notion that intelligence solely derives from model size <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.

This shift towards "tiny Transformers" suggests a future where powerful AI is not confined to massive data centers but is distributed and accessible on a wide range of devices.