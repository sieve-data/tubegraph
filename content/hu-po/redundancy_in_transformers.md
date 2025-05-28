---
title: Redundancy in Transformers
videoId: HcE3I_iCvoI
---

From: [[hu-po]] <br/> 

Recent research indicates that [[vision_transformers_and_their_efficiency | Transformers]] are poised to become significantly smaller in the future, with several papers demonstrating the inherent redundancy within their architectures <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>. This discovery suggests that while models are becoming smarter and more capable, they are also simultaneously becoming smaller without sacrificing too much intelligence <a class="yt-timestamp" data-t="03:48">[03:48]</a>. This contrasts a future where increased model size is the sole path to improved performance, enabling wider accessibility and reducing deployment costs <a class="yt-timestamp" data-t="04:06">[04:06]</a>.

## Identifying Redundancy in Transformer Modules

An empirical study from the University of Maryland investigated redundancy across different modules within [[vision_transformers_and_their_efficiency | Transformers]], including blocks, Multi-Layer Perceptrons (MLPs), and attention layers <a class="yt-timestamp" data-t="04:41">[04:41]</a>. The study involved "dropping out" (deleting) different parts of a trained Transformer to assess their importance <a class="yt-timestamp" data-t="05:27">[05:27]</a>.

Key findings include:
*   **Attention Layers:** A large portion of attention layers exhibit excessively high similarity and can be pruned without degrading performance <a class="yt-timestamp" data-t="06:22">[06:22]</a>. For example, Llama 2 70B achieved a 40-50% speed-up with only a 3% performance drop by pruning half of its attention layers <a class="yt-timestamp" data-t="06:33">[06:33]</a>. Dropping more than 50% of attention layers can result in performance comparable to the full model, indicating high redundancy <a class="yt-timestamp" data-t="09:09">[09:09]</a>.
*   **MLP/Feed Forward Networks (FFN):** Dropping MLP or FFN layers generally affects performance negatively, though joint dropping with attention layers can allow for more aggressive pruning <a class="yt-timestamp" data-t="09:03">[09:03]</a>.
*   **Entire Blocks:** Removing entire blocks leads to significant performance degradation <a class="yt-timestamp" data-t="08:25">[08:25]</a>. Naively removing blocks, such as 32 blocks in Llama 2, does not work well <a class="yt-timestamp" data-t="08:51">[08:51]</a>.

Redundancy is assessed using cosine similarity, where highly similar features indicate redundancy that can be removed <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. Neural networks are adept at extracting information, and redundant features are not always necessary for effective computation <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

### Layer-Specific Redundancy
The level of redundancy in a Transformer is dependent on the depth of the layer <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
*   **Early Layers (Shallow):** These layers are more critical, and dropping tokens or modules here is more sensitive <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.
*   **Middle Layers:** MLPs in the middle layers are often "kind of garbage," meaning they are less important <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>.
*   **Deeper Layers:** Token redundancy progressively increases in deeper layers of the model <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>, and image tokens in deeper layers gradually become less critical to the final results <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>.

The first and last layers of a deep neural network are often the most important parts <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. This suggests an "hourglass" or non-uniform pruning strategy is more effective than a simple linear reduction <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.

## Impact on Performance and Efficiency

The discovery of redundancy has significant implications for [[vision_transformers_and_their_efficiency | Transformer]] efficiency:

*   **Speed Up:** Pruning attention layers can lead to substantial speed-ups in inference <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>. For instance, LLaVA-NeXT saw a 40% reduction in training time and a 55% acceleration in inference FLOPs with [[vision_transformers_and_their_efficiency | Pyramid Drop]] <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>.
*   **Reduced Cost:** Smaller models cost less to train, deploy, and run in inference <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. This is crucial for a future where AI interactions will lead to thousands of inferences per person per day <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Performance Improvement:** Counter-intuitively, sometimes pruning can even *improve* performance. For example, in some benchmarks like OBQA, dropping attention layers resulted in an increase in performance <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>. This suggests that certain redundant parts might even hinder optimal function.
*   **Energy Consumption:** Reducing computational load also significantly reduces energy consumption, which is becoming a limiting factor in AI infrastructure <a class="yt-timestamp" data-t="01:08:50">[01:08:50]</a>.

## Why Redundancy Exists

The high degree of redundancy in [[vision_transformers_and_their_efficiency | Transformer]] models may be a key reason for their widespread power and success <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>.
*   **Robustness:** A redundant architecture offers multiple paths for important information to propagate, making the model more robust to perturbations or pruning <a class="yt-timestamp" data-t="00:40:14">[00:40:14]</a>.
*   **Generalization:** This redundancy could explain why [[vision_transformers_and_their_efficiency | Transformers]] work effectively across various modalities, domains, and problems <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.
*   **Implicit Regularization:** This phenomenon is conceptually similar to `Dropout` regularization, which promotes redundant information paths during training to make a network more robust to individual neuron failures <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>.

### Visual Redundancy
Images inherently exhibit substantial spatial redundancy, making them difficult to compress losslessly <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>. When images are converted into a sequence of tokens for [[vision_transformers_and_their_efficiency | Transformers]], many tokens can be redundant (e.g., multiple "sky tokens") <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>. Furthermore, the number of image tokens increases quadratically with resolution, exacerbating the "quadratic curse" of [[vision_transformers_and_their_efficiency | Transformer]] attention <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>.

Despite this, [[vision_transformers_and_their_efficiency | Vision Transformers]] (ViTs) can "sneak" information into seemingly unrelated or useless tokens (sometimes referred to as "ViT registers"). This is an emergent behavior where the model learns to pack information into redundant tokens, rather than relying solely on spatially relevant areas <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>.

## Future Implications: Tiny, Efficient Models

Combining insights from redundant architecture with advancements in [[quantization_techniques_for_transformers | quantization techniques for Transformers]] leads to powerful implications for future AI development.

For example, "one-bit" [[quantization_techniques_for_transformers | large language models]] (BitNet B 1.58) can achieve up to 6x speed-up on x86 CPUs and 5x speed-up on ARM CPUs with minimal performance loss <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>. This is achieved by transforming high-precision weights into low-bit values (e.g., -1, 0, 1), which significantly reduces memory and bandwidth usage during matrix multiplication <a class="yt-timestamp" data-t="00:52:32">[00:52:32]</a>. Using lookup tables instead of direct computation for these low-bit values further accelerates inference <a class="yt-timestamp" data-t="00:55:08">[00:55:08]</a>.

[!INFO] Synergistic Gains
The gains from architectural pruning and [[quantization_techniques_for_transformers | quantization]] are multiplicative, not additive <a class="yt-timestamp" data-t="00:57:39">[00:57:39]</a>. This means a 50% speed-up from pruning combined with a 6x speed-up from [[quantization_techniques_for_transformers | quantization]] results in drastically faster and more efficient models.

This trend implies a future where powerful AI models could run on very tiny or old hardware, such as cell phones or edge devices <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>. This widespread accessibility would lead to significant decentralization of AI capabilities, making it difficult to control its spread <a class="yt-timestamp" data-t="01:29:45">[01:29:45]</a>. The ability to utilize existing CPU data centers for model inference, rather than solely relying on expensive GPU infrastructure, also represents a huge unlock for the industry <a class="yt-timestamp" data-t="01:28:51">[01:28:51]</a>.