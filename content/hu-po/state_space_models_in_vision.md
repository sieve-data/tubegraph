---
title: State space models in vision
videoId: RtHDu6kFPb8
---

From: [[hu-po]] <br/> 

State space models (SSMs), particularly those known as Mamba, are emerging as an alternative to traditional deep learning architectures like Transformers and Convolutional Neural Networks (CNNs) in [[computer_vision_deep_dive | computer vision]] tasks <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Originating in the language modeling space for sequence-to-sequence tasks, Mamba models are now being applied to [[vision_language_models | vision language models]] due to their efficiency advantages <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>, <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Architectural Overview

Mamba models are designed to efficiently process long sequences, a critical feature for high-resolution images <a class="yt-timestamp" data-t="02:04:05">[02:04:05]</a>. Unlike [[state_space_models_vs_attentionbased_models | attention-based models]] (Transformers), which suffer from quadratic complexity with respect to input sequence length, SSMs scale linearly <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>, <a class="yt-timestamp" data-t="01:19:16">[01:19:16]</a>. This linear scaling allows for processing larger images with less GPU memory and faster inference speeds <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>, making them attractive for edge computing and real-time applications <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

### State Space Model (SSM) Fundamentals
SSMs, specifically their discrete versions like S4 and Mamba, model a system by mapping an input sequence to an output sequence through a compressed hidden state <a class="yt-timestamp" data-t="00:59:49">[00:59:49]</a>. This hidden state acts as a bottleneck, limiting the information passed between tokens, which reduces computational overhead <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>. The core equations involve transforming continuous parameters (A, B, C) into discrete versions using methods like zero-order hold, which aligns the model with the discrete nature of input signals (e.g., image pixels) <a class="yt-timestamp" data-t="01:01:11">[01:01:11]</a>, <a class="yt-timestamp" data-t="01:02:40">[01:02:40]</a>.

The key to Mamba's efficiency is its selective scan mechanism, where matrices B, C, and Delta are derived from the input data, providing contextual awareness and dynamic weights <a class="yt-timestamp" data-t="01:04:25">[01:04:25]</a>.

## Comparison with Existing Architectures

### Vision Transformers (ViTs)
ViTs excel in "fitting capabilities" and visual modeling due to their global receptive fields and dynamic weights <a class="yt-timestamp" data-t="01:37:53">[01:37:53]</a>. Their self-attention mechanism allows every patch to potentially interact with every other patch <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>. However, this comes at the cost of quadratic computational complexity, making them memory-intensive for high-resolution images <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>, <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. ViTs typically flatten images into 1D sequences of patches, sometimes introducing a directional bias <a class="yt-timestamp" data-t="01:48:57">[01:48:57]</a>.

### Convolutional Neural Networks (CNNs)
CNNs offer remarkable scalability with linear complexity concerning image resolution <a class="yt-timestamp" data-t="01:24:20">[01:24:20]</a>. They use kernels that convolve across an image, building abstract representations through hierarchical layers <a class="yt-timestamp" data-t="01:08:26">[01:08:26]</a>. A limitation of CNNs is their local receptive field, meaning that higher-level parts of the network primarily consider information from a limited, local subset of the image <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.

### Mamba's Position
Mamba aims to combine the best of both: linear complexity like CNNs while retaining a global receptive field akin to ViTs <a class="yt-timestamp" data-t="01:53:50">[01:53:50]</a>. This is achieved by converting non-causal 2D visual data into ordered patch sequences, then processing them to ensure each element integrates information from all other locations without the quadratic cost <a class="yt-timestamp" data-t="01:54:19">[01:54:19]</a>.

## Prominent Mamba-based Vision Architectures

Two papers published in January 2024 highlight the rapid development in this field:

### 1. Vamba (Visual Mamba)
*   **Developers**: University of Chinese Academy of Sciences (UCAS), Huawei Inc., and Pen Lab <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Key Feature**: **Cross-Scan Module (CSM)** <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>. To overcome the "direction-sensitive issue" (the bias from flattening 2D images into 1D sequences), Vamba's CSM adopts a four-way scanning strategy (e.g., left-to-right, right-to-left, top-to-down, bottom-to-up) <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>. This ensures a global receptive field by accumulating a hidden state traversing in four different directions <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>.
*   **Architecture**: Vamba blocks perform an initial linear embedding, split the output into two flows, one of which passes through a 3x3 depthwise convolutional kernel followed by a SiLU activation function <a class="yt-timestamp" data-t="01:17:40">[01:17:40]</a>. They explicitly *refrain* from using position embeddings, believing the causal nature of their scanning makes them unnecessary <a class="yt-timestamp" data-t="01:20:06">[01:20:06]</a>. They also discard the MLP (multi-layer perceptron) block commonly found in ViTs, making their blocks "shallower" <a class="yt-timestamp" data-t="01:21:05">[01:21:05]</a>.

### 2. Vision Mamba (Vim)
*   **Developers**: Huazhong University of Science and Technology, Horizon Robotics, and Beijing Academy of Artificial Intelligence <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Key Feature**: **Bidirectional Mamba Blocks** <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>. This approach processes tokens with both forward (left-to-right, top-to-down) and backward (right-to-left, bottom-to-up) directions <a class="yt-timestamp" data-t="01:07:08">[01:07:08]</a>, <a class="yt-timestamp" data-t="01:07:10">[01:07:10]</a>.
*   **Architecture**: Vision Mamba integrates position embeddings into its patch tokens <a class="yt-timestamp" data-t="01:09:54">[01:09:54]</a> and uses a learnable classification token for tasks like ImageNet <a class="yt-timestamp" data-t="01:10:33">[01:10:33]</a>. Unlike Vamba, Vim includes an MLP block after its Mamba encoder <a class="yt-timestamp" data-t="01:21:39">[01:21:39]</a>.
*   **Efficiency Focus**: Horizon Robotics, being an autonomous vehicle company, is highly interested in efficient models with small compute footprints and low latency for edge computing <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Their design specifically optimizes memory I/O within the GPU by recomputing intermediate activations to reduce transfers from slower High Bandwidth Memory (HBM) to faster SRAM <a class="yt-timestamp" data-t="01:25:05">[01:25:05]</a>.

## Performance Benchmarks

Both Vamba and Vision Mamba are evaluated on standard [[computer_vision_deep_dive | computer vision]] benchmarks, making direct comparisons possible:

*   **ImageNet 1K**: Classification task <a class="yt-timestamp" data-t="00:39:10">[00:39:10]</a>.
*   **COCO**: Object detection and instance segmentation <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>.
*   **ADE20K**: Semantic segmentation (dense task, pixel-level classification) <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a>.

In head-to-head comparisons on ImageNet 1K, Vamba generally achieves slightly higher top-1 accuracy for comparable model sizes <a class="yt-timestamp" data-t="00:46:52">[00:46:52]</a>. For object detection and instance segmentation on COCO, Vamba also appears to perform better <a class="yt-timestamp" data-t="00:49:02">[00:49:02]</a>.

However, Vision Mamba's ablation study on its bidirectional design revealed that removing the bidirectional components and relying only on a forward pass did not significantly impact performance on ImageNet and ADE20K <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>. This suggests that factors like position embeddings (which Vision Mamba includes and Vamba does not) might play a more crucial role in handling directional biases <a class="yt-timestamp" data-t="01:50:52">[01:50:52]</a>.

## Advantages and Applications

The primary advantage of Mamba models is their efficiency at high resolutions <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. While ViTs struggle with quadratic memory scaling, Mamba's linear complexity allows for processing larger images without "exploding" GPU memory <a class="yt-timestamp" data-t="01:22:23">[01:22:23]</a>, <a class="yt-timestamp" data-t="01:23:03">[01:23:03]</a>.

This efficiency makes them particularly well-suited for:
*   **Autonomous Vehicles**: Where maintaining high image resolution is crucial to detect small, distant objects (e.g., road signs, other cars) and low latency is paramount for real-time decision-making <a class="yt-timestamp" data-t="01:27:06">[01:27:06]</a>, <a class="yt-timestamp" data-t="01:28:06">[01:28:06]</a>.
*   **Medical Images**: Allowing analysis of full-resolution scans without downsampling, which could cause the loss of critical details for diagnosis <a class="yt-timestamp" data-t="01:36:56">[01:36:56]</a>.
*   **Remote Sensing Images** and **Long Videos**: Applications where large input sizes are inherent and computational efficiency is highly valued <a class="yt-timestamp" data-t="01:37:18">[01:37:18]</a>, <a class="yt-timestamp" data-t="01:37:20">[01:37:20]</a>.

While Mamba models offer significant efficiency gains, it is suggested that they may not entirely usurp the dominance of Transformers in all generic [[vision_language_models_and_their_applications | vision language models and their applications]] due to the established "Transformer brand" <a class="yt-timestamp" data-t="02:29:50">[02:29:50]</a>. However, their efficiency makes them a strong contender for time-sensitive and Edge Computing applications <a class="yt-timestamp" data-t="01:29:02">[01:29:02]</a>.