---
title: Convolutional Neural Networks and Visual Systems
videoId: -jG7S5g071Q
---

From: [[hu-po]] <br/> 

[[Deep Learning and Neural Networks | Convolutional Neural Networks]] (CNNs) are a fundamental component in [[computer_vision_deep_dive | computer vision]] models, and their architecture is deeply inspired by the biological visual system <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.

## Hierarchical Processing in Vision
The human visual system processes images in a hierarchical manner, moving from coarse to fine details <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. This multi-scale, coarse-to-fine nature suggests an inherent order for images <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.

This concept directly influenced the original design of [[applications_of_cnns_and_capsule_networks | CNNs]] <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a> <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.

### Biological Inspiration
The architecture of [[applications_of_cnns_and_capsule_networks | CNNs]] was developed by observing how the brain's visual system works <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
*   Images enter through the eye and are projected onto cells in the retina <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a> <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.
*   These signals are sent to the back of the head, where neurons in the visual cortex are arranged in layers, often denoted as V1, V2, V3, and so on <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a> <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a> <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a> <a class="yt-timestamp" data-t="00:21:35">[00:21:35]</a>.
*   Early research, for example by studying the neurons of cats, revealed that neurons in higher layers (e.g., V2) connect to patches of neurons in lower layers (e.g., V1) <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a> <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.
*   This hierarchical arrangement allows the brain to build a semantic representation of an image <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a> <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>.

### Receptive Fields
A key concept in [[applications_of_cnns_and_capsule_networks | CNNs]] is the receptive field <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.
*   Each neuron in a higher layer of a [[applications_of_cnns_and_capsule_networks | CNN]] processes information from a specific "receptive field" or a larger area of the preceding layer <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a> <a class="yt-timestamp" data-t="00:20:10">[00:20:10]</a>.
*   This hierarchical aggregation means that neurons at the top layers of a [[applications_of_cnns_and_capsule_networks | CNN]] represent concepts with a receptive field covering the entire image, but at a higher semantic level <a class="yt-timestamp" data-t="01:28:54">[01:28:54]</a> <a class="yt-timestamp" data-t="01:29:08">[01:29:08]</a>.
*   Conversely, lower layers represent more spatially restricted concepts, focusing on specific localized parts of the image <a class="yt-timestamp" data-t="01:29:14">[01:29:14]</a> <a class="yt-timestamp" data-t="01:29:18">[01:29:18]</a>.
*   This is analogous to how the human visual system processes information, where early visual areas respond to small, local features, and later areas integrate these features into more complex representations <a class="yt-timestamp" data-t="01:40:59">[01:40:59]</a>.

## Implications for Image Generation
Traditional [[transformer_architecture_in_image_processing | Transformer]] models used for image generation often flatten a 2D image into a 1D sequence using methods like a raster scan (left-to-right, top-to-down) <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a> <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a> <a class="yt-timestamp" data-t="00:42:06">[00:42:06]</a>.
*   This approach, while straightforward, introduces a "bad inductive prior" for images because it disrupts spatial locality <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a> <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>. For instance, a token's immediate neighbors (e.g., token 1 and token 2) have a stronger correlation than tokens further apart in the 1D sequence but close in 2D (e.g., token 1 and token 4) <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a> <a class="yt-timestamp" data-t="00:44:08">[00:44:08]</a>.
*   To mitigate this, approaches like rotary position embeddings (RoPE) are often used to reintroduce spatial information <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a> <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a> <a class="yt-timestamp" data-t="00:44:21">[00:44:21]</a>.

The paper "Visual Autoregressive Modeling" proposes an alternative by redefining autoregressive learning for images as "next scale prediction" <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. Instead of predicting the next token in a flattened sequence, the [[transformer_architecture_in_image_processing | Transformer]] predicts the next higher-resolution token map, conditioned on all previous (lower-resolution) ones <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a> <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.

This approach leverages the inherent multi-scale, coarse-to-fine inductive bias found in both human vision and [[applications_of_cnns_and_capsule_networks | CNNs]] <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a> <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>. This formulation allows for parallel token generation within each resolution layer, significantly improving inference speed compared to sequential raster-scan methods <a class="yt-timestamp" data-t="00:59:05">[00:59:05]</a> <a class="yt-timestamp" data-t="01:00:05">[01:00:05]</a> <a class="yt-timestamp" data-t="01:01:23">[01:01:23]</a>. It reduces the computational complexity from O(N^6) to O(N^4) <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a> <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a> <a class="yt-timestamp" data-t="01:14:31">[01:14:31]</a>.