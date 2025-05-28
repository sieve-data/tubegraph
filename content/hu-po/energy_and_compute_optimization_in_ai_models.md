---
title: Energy and Compute Optimization in AI Models
videoId: HcE3I_iCvoI
---

From: [[hu-po]] <br/> 

AI models, particularly Transformers, are becoming increasingly powerful and capable, but simultaneously, significant advancements are being made to reduce their size and computational demands. This ongoing development aims to make these models more accessible and efficient for deployment and inference, potentially democratizing advanced AI capabilities <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## Redundancy in Transformer Architectures

Recent research highlights a significant amount of redundancy within Transformer models, which can be leveraged for [[optimization_methods_in_machine_learning | optimization]].

### Identifying Redundancy

An empirical study, "What matters in Transformers: Not all attention is needed" (University of Maryland, October 17, 2024), investigates redundancy across different modules:
*   **Blocks:** The repeated elements within a Transformer architecture <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
*   **MLP (Multi-Layer Perceptron) / Feed-Forward Networks:** Components within each block with full connectivity <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a> <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>.
*   **Attention Layers:** The mechanism that calculates relationships between tokens in a sequence <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

The study uses cosine similarity to determine which layers or parts of layers are redundant and can be dropped without significantly degrading [[performance_and_efficiency_in_machine_learning_models | performance]] <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a> <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. The intuition is that if features are highly similar, some can be removed <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

### Pruning Strategies and Impacts

*   **Block Removal:** Removing entire blocks leads to significant [[performance_and_efficiency_in_machine_learning_models | performance]] degradation <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **MLP Layer Dropping:** Negatively affects [[performance_and_efficiency_in_machine_learning_models | performance]] when dropped separately <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Attention Layer Dropping:** A large portion of attention layers exhibit excessively high similarity and can be pruned without degrading [[performance_and_efficiency_in_machine_learning_models | performance]] <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. Llama 2 70B, for instance, achieved a 50% speed-up with only a 3% [[performance_and_efficiency_in_machine_learning_models | performance]] drop by pruning half of its attention layers <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Joint Layer Dropping:** Allows for even more aggressive dropping of both attention and MLP layers <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

Transformer-based language models are considered to have redundant architectures, leading to inefficiencies in deployment costs and resource demands <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. Making them smaller saves money, allows faster execution, and enables parallel processing to serve more users <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

### Layer Importance

Studies show that the importance of MLP and attention layers is not uniform across the model's depth <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>:
*   **MLP Layers:** The first and last layers are very important, while middle layers are less critical <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.
*   **Attention Layers:** Similar to MLPs, attention layers at the beginning and end tend to be more important, though the very last attention layers might be the least important <a class="yt-timestamp" data-t="00:26:43">[00:26:43]</a>.
*   **Overall Pattern:** There's a pattern where early layers are important, then redundancy increases in middle layers, and the very last layer becomes important again <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>. This "hourglass" or "up and then down" pattern applies regardless of whether full blocks, MLPs, or attention layers are dropped <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>.

## Vision Models and Token Reduction

The "Pyramid Drop" paper (Shanghai AI Laboratory, USC, and CK, October 22, 2024) extends the concept of redundancy to visual language models (VLMs) <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>.

*   **Visual Redundancy:** Images exhibit substantial spatial redundancy <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>. When images are converted into sequences of tokens for Transformers, much of this information is redundant (e.g., "Sky token, Sky token..." <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>).
*   **Quadratic Curse:** The number of image tokens increases quadratically with resolution, exacerbating the quadratic computational cost of Transformer attention mechanisms <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>.
*   **Pyramid Drop Strategy:** This method cuts the visual Transformer (ViT) into stages and drops a portion of image tokens at the end of each stage based on a predefined ratio <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.
    *   **Layer Sensitivity:** Dropping tokens in shallow layers of the model is more sensitive, while deeper layers show progressively increasing token redundancy <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a> <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>. More aggressive dropping occurs in deeper layers <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.
    *   **Results:** Pyramid Drop achieved a 40% [[training_and_finetuning_processes_for_ai_models | training]] time acceleration and 55% inference FLOP acceleration for the LLaVA-Next model <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>. In some cases, performance was even slightly improved, rather than just reduced <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a> <a class="yt-timestamp" data-t="00:35:16">[00:35:16]</a>.

### Emergent Behavior and "Registers"

The effectiveness of dropping tokens in vision models reveals an emergent behavior where Transformers learn to "sneak" information into seemingly unrelated or less important tokens, similar to "ViT registers" <a class="yt-timestamp" data-t="00:42:48">[00:42:48]</a>. This happens because the model finds more robust paths for information flow when core spatial tokens might be redundant or pruned <a class="yt-timestamp" data-t="00:43:11">[00:43:11]</a>. This phenomenon can also contribute to the robustness and redundancy observed in Transformers, potentially explaining their broad applicability across modalities <a class="yt-timestamp" data-t="00:39:18">[00:39:18]</a>.

## Quantization and Hardware Optimization

"One-bit AI Infra Part 1.1: Fast and Lossless BitNet b 1.58 Inference on CPUs" (Microsoft Research, October 21, 2024) explores [[quantization_and_optimization_in_machine_learning | quantization and optimization]] methods at the hardware level <a class="yt-timestamp" data-t="00:46:58">[00:46:58]</a>.

*   **Low-Precision Weights:** This approach involves representing model weights with very low precision, such as 1-bit or effectively 1.58 bits, instead of full precision (16 or 32 bits) <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a> <a class="yt-timestamp" data-t="01:04:10">[01:04:10]</a>. This drastically reduces memory usage and bandwidth requirements <a class="yt-timestamp" data-t="00:53:51">[00:53:51]</a>.
*   **Specialized Kernels:** The paper introduces custom kernels (algorithms) for CPUs to support fast and lossless inference of these low-precision models <a class="yt-timestamp" data-t="00:55:02">[00:55:02]</a>.
    *   **i2s kernel:** Transforms full-precision weights into 2-bit values <a class="yt-timestamp" data-t="00:52:29">[00:52:29]</a>.
    *   **tl1 and tl2 kernels:** Utilize lookup tables (LUTs) to perform matrix multiplications. If weights are limited to a few discrete values (e.g., -1, 0, 1), the result of multiplications can be pre-calculated and stored in a table, avoiding real-time computation <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>. Lookup tables are highly effective for functions expensive to compute but inexpensive to cache <a class="yt-timestamp" data-t="00:55:47">[00:55:47]</a>.
*   **Performance Gains:** This method achieves up to a 6x speed-up on x86 CPUs and 5x speed-up on ARM CPUs <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>. Similar to pruning, this [[quantization_and_optimization_in_machine_learning | quantization]] often results in negligible or even improved [[performance_and_efficiency_in_machine_learning_models | performance]] <a class="yt-timestamp" data-t="01:04:53">[01:04:53]</a> <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>.
*   **Post-[[training_and_finetuning_processes_for_ai_models | Training]] Quantization (PTQ):** Allows models to be quantized to retain [[performance_and_efficiency_in_machine_learning_models | performance]] on specific use cases or private datasets without needing access to the original [[training_and_finetuning_processes_for_ai_models | training]] data <a class="yt-timestamp" data-t="01:05:09">[01:05:09]</a>.

## Combined Impact and Future Implications

These [[optimization_methods_in_machine_learning | optimization methods]] — redundancy reduction in architecture and low-precision [[quantization_and_optimization_in_machine_learning | quantization]] at the hardware level — can be stacked, leading to compounded improvements <a class="yt-timestamp" data-t="00:57:39">[00:57:39]</a>.

*   **Reduced Costs and Energy:** Smaller models and faster inference directly translate to lower [[training_and_finetuning_processes_for_ai_models | training]] and inference costs, as well as reduced energy consumption <a class="yt-timestamp" data-t="01:08:50">[01:08:50]</a>. High energy consumption of AI models is a growing concern, with models like ChatGPT consuming substantial electricity daily <a class="yt-timestamp" data-t="01:12:42">[01:12:42]</a>.
*   **Democratization of AI:** The ability to run powerful AI models efficiently on less powerful or older hardware, including CPUs and edge devices like cell phones, signifies a major shift <a class="yt-timestamp" data-t="01:02:27">[01:02:27]</a> <a class="yt-timestamp" data-t="01:28:31">[01:28:31]</a>. This potentially eliminates the need for massive GPU data centers for all AI applications, allowing existing CPU infrastructure to be repurposed <a class="yt-timestamp" data-t="01:28:44">[01:28:44]</a>.
*   **Ubiquitous AI:** If advanced AI can run on low-cost, widely available devices, it becomes nearly impossible to control or restrict its spread, leading to a highly decentralized and pervasive AI ecosystem <a class="yt-timestamp" data-t="01:29:45">[01:29:45]</a>. This would mean that powerful AI (even approaching [[selfimprovement_in_ai_models | AGI]]) could be accessible to almost anyone <a class="yt-timestamp" data-t="01:29:45">[01:29:45]</a>.

> "If you can run super Intelligence on a Raspberry Pi, there is no way to control that <a class="yt-timestamp" data-t="01:29:47">[01:29:47]</a>. It's going to it's going to spread almost immediately everywhere and you're never going to be able to control it <a class="yt-timestamp" data-t="01:29:53">[01:29:53]</a>."