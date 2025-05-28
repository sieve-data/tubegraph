---
title: Vision Transformers vs Convolutional Networks
videoId: KSZiJ4k28b4
---

From: [[hu-po]] <br/> 

The field of computer vision is currently undergoing a paradigm shift, moving away from specialized architectures like Convolutional Networks (ConvNets) towards more generalized, foundational models, particularly those built on [[Vision Transformers and their applications | Vision Transformers]] (ViTs) <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## The Rise of Vision Transformers

Historically, ConvNets were the dominant architecture for various computer vision tasks, including segmentation, classification, and bounding box detection <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. However, the landscape is changing, and the supremacy of [[Vision Transformers and their applications | Vision Transformers]] is evident <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. It is increasingly rare to see ConvNets used as encoders in cutting-edge models <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

Instead, large, task-agnostic [[Vision Transformers and their applications | Vision Transformers]] are becoming the backbone for foundational computer vision models <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. These models aim to produce "all-purpose visual features" that are useful for a wide variety of tasks without the need for fine-tuning <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Architectural Characteristics of Vision Transformers

[[Vision Transformers and their applications | ViTs]] operate by cutting an input image into smaller "patches" <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>, often a 4x4 grid resulting in 16 patches <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>. Each of these patches is then processed to generate "visual tokens," which are essentially embeddings for different parts of the image <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>.

A key feature of [[Vision Transformers and their applications | ViTs]] is their use of a "class token," from which features are extracted <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>. Furthermore, [[Vision Transformers and their applications | ViTs]] allow for the examination of "patch level features" – the features corresponding to these individual image patches <a class="yt-timestamp" data-t="01:31:51">[01:31:51]</a>.

### Challenges with Transformers

One significant challenge with [[Comparison to Transformers and RNNs | Transformers]] is their high memory consumption <a class="yt-timestamp" data-t="00:41:30">[00:41:30]</a>. This is due to the self-attention mechanism, which involves multiplying every vector by every other vector, leading to memory requirements that grow quadratically with the sequence length <a class="yt-timestamp" data-t="00:41:06">[00:41:06]</a>. To mitigate this, techniques like "flash attention" are implemented to improve memory usage and speed in self-attention layers <a class="yt-timestamp" data-t="00:41:46">[00:41:46]</a>.

Another consideration in [[Vision Transformers and their applications | ViT]] architecture design is hardware specificity. Hyperparameters, such as the embedding dimension, are often chosen to maximize computational efficiency on particular hardware (e.g., NVIDIA A100 GPUs), rather than solely for performance <a class="yt-timestamp" data-t="00:43:02">[00:43:02]</a>.

### Emergent Capabilities

A notable aspect of large [[Vision Transformers and their applications | Vision Transformers]] trained on vast datasets is their emergent capabilities. These models can learn to:
*   Separate the main object from the background <a class="yt-timestamp" data-t="01:44:19">[01:44:19]</a>.
*   Identify and match specific parts of objects (e.g., the head of an animal, the wing of a plane matching the wing of a bird), demonstrating an implicit understanding of object parts and scene geometry <a class="yt-timestamp" data-t="01:47:17">[01:47:17]</a>, <a class="yt-timestamp" data-t="01:47:50">[01:47:50]</a>.
*   Exhibit robustness to variations in style, pose, and scale, even on tiny objects within a large image <a class="yt-timestamp" data-t="01:48:24">[01:48:24]</a>.

This emergent intelligence is a key characteristic of foundational models, akin to instruction emergence in large language models <a class="yt-timestamp" data-t="01:55:12">[01:55:12]</a>.