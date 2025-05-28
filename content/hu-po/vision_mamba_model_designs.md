---
title: Vision Mamba model designs
videoId: RtHDu6kFPb8
---

From: [[hu-po]] <br/> 

Vision Mamba models are a class of State Space Models (SSMs) designed as an alternative to traditional Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) for visual tasks. They aim to overcome the quadratic complexity issues of ViTs while retaining their modeling capabilities, particularly for high-resolution images <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. The term "Mamba" alludes to the fast-moving snake, highlighting the models' efficiency <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

## Core Concepts of Mamba in Vision

Mamba models, particularly in their "Vision Mamba" application, leverage State Space Models (SSMs) as their core operator <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>. SSMs process input data by maintaining a "compressed hidden state," which aggregates information from previously scanned samples <a class="yt-timestamp" data-t="00:29:48">[00:29:48]</a>. This approach aims to achieve linear computational complexity with respect to the input sequence length (or image size), unlike ViTs which suffer from quadratic complexity <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a> <a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a> <a class="yt-timestamp" data-t="01:26:21">[01:26:21]</a>.

A key challenge for applying SSMs to visual data is the "direction sensitive issue" <a class="yt-timestamp" data-t="02:02:02">[02:02:02]</a> or "position sensitivity" <a class="yt-timestamp" data-t="02:34:34">[02:34:34]</a>. Unlike text, where data flows causally in one dimension (e.g., left-to-right), images are 2D and non-causal <a class="yt-timestamp" data-t="03:07:54">[03:07:54]</a>. Simply flattening an image into a 1D sequence for an SSM would lead to restricted receptive fields <a class="yt-timestamp" data-t="03:06:01">[03:06:01]</a>. To address this, different Vision Mamba designs propose unique scanning strategies.

## V Mamba (Visual Mamba)

The V Mamba paper, developed by groups including University of Chinese Academy of Sciences (UCAS), Huawei Inc., and Pen Lab, was released on January 17, 2024 <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a> <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>.

### Key Design Elements
*   **Cross-Scan Module (CSM)**: V Mamba introduces a four-way scanning strategy to traverse the spatial domain <a class="yt-timestamp" data-t="02:03:03">[02:03:03]</a>. Instead of unidirectional patterns, it scans from all four corners across the feature map to the opposite location (e.g., left-to-right, top-to-down; right-to-left, bottom-to-up; top-to-down, left-to-right; and bottom-to-up, right-to-left) <a class="yt-timestamp" data-t="03:30:57">[03:30:57]</a>. This ensures each pixel integrates information from all other locations, achieving a global receptive field without increasing computational complexity <a class="yt-timestamp" data-t="02:04:02">[02:04:02]</a>.
*   **No Position Embeddings**: Unlike many ViTs, V Mamba refrains from using position embeddings, believing its causal nature and cross-scan module mitigate the need for explicit positional bias <a class="yt-timestamp" data-t="02:06:03">[02:06:03]</a> <a class="yt-timestamp" data-t="02:20:06">[02:20:06]</a>.
*   **No MLP Blocks**: The V Mamba design's fundamental block (VSS block) is "shallower" than a typical ViT block, as it discards the Multi-Layer Perceptron (MLP) components commonly found in Transformers <a class="yt-timestamp" data-t="02:21:05">[02:21:05]</a>.
*   **Activation Function**: Uses the SiLU activation function <a class="yt-timestamp" data-t="01:18:04">[01:18:04]</a>.

### Performance
V Mamba generally shows promising performance on [[benchmarking_vision_models | vision benchmarks]] <a class="yt-timestamp" data-t="02:03:39">[02:03:39]</a>:
*   **ImageNet-1K Classification**: Achieves higher top-1 accuracy (e.g., V Mamba-B with 75M parameters gets 83%) compared to Vision Mamba (Vim) <a class="yt-timestamp" data-t="00:46:07">[00:46:07]</a> <a class="yt-timestamp" data-t="00:46:51">[00:46:51]</a>.
*   **COCO Object Detection & Instance Segmentation**: Generally outperforms Vim, with V Mamba-T achieving an AP box of 46 (compared to Vim-T's 45.3) <a class="yt-timestamp" data-t="00:48:39">[00:48:39]</a>.
*   **ADE20K Semantic Segmentation**: Shows higher scores (e.g., V Mamba-L at 47.7 mIoU) compared to Vim <a class="yt-timestamp" data-t="00:49:14">[00:49:14]</a> <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>.

## Vision Mamba (Vim)

The Vision Mamba (Vim) paper, from groups including H. Jong University of Science and Technology, Horizon Robotics, and Beijing Academy of Artificial Intelligence, was released on January 18, 2024 <a class="yt-timestamp" data-t="00:37:35">[00:37:35]</a> <a class="yt-timestamp" data-t="00:41:02">[00:41:02]</a>. A key motivation for this group, particularly Horizon Robotics (an autonomous vehicle company), is the development of efficient vision systems with a very small compute footprint suitable for edge computing <a class="yt-timestamp" data-t="00:54:52">[00:54:52]</a> <a class="yt-timestamp" data-t="00:59:52">[00:59:52]</a>.

### Key Design Elements
*   **Bidirectional Mamba Blocks**: Vim uses bidirectional Mamba blocks, processing sequences in both forward (left-to-right, top-to-down) and backward (right-to-left, bottom-to-up) directions <a class="yt-timestamp" data-t="00:35:25">[00:35:25]</a>.
*   **Position Embeddings**: Includes position embeddings to provide explicit positional information to patch tokens <a class="yt-timestamp" data-t="01:09:54">[01:09:54]</a>.
*   **Class Token**: Utilizes a learnable classification token, similar to ViTs, to aggregate global semantic information for classification tasks <a class="yt-timestamp" data-t="01:10:33">[01:10:33]</a>.
*   **MLP Blocks**: Their encoder structure includes MLP blocks after the core Mamba operations <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>.

### Performance & Efficiency
Vim emphasizes efficiency and scalability, especially for high-resolution images <a class="yt-timestamp" data-t="02:35:05">[02:35:05]</a>:
*   **Speed**: Vim is designed to be faster than ViTs like DeiT, especially at higher resolutions, leveraging SSMs' linear complexity <a class="yt-timestamp" data-t="01:07:22">[01:07:22]</a> <a class="yt-timestamp" data-t="01:29:57">[01:29:57]</a>.
*   **Memory Efficiency**: Optimizes memory usage by minimizing data transfer between slow high-bandwidth memory (HBM) and fast SRAM within the GPU, for example, by recomputing activations instead of storing them <a class="yt-timestamp" data-t="01:23:09">[01:23:09]</a>. This is crucial for resource-constrained environments <a class="yt-timestamp" data-t="01:24:45">[01:24:45]</a>.
*   **Ablation Study**: An ablation study on Vim's bidirectional design showed that removing the backward pass or additional `conv1d` blocks resulted in only minor performance drops on ImageNet-1K and ADE20K <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a> <a class="yt-timestamp" data-t="01:13:56">[01:13:56]</a>. This suggests that the addition of position embeddings might largely negate the benefits of complex scanning directions <a class="yt-timestamp" data-t="01:50:52">[01:50:52]</a>.

## Comparison of Design Philosophies

The two models represent slightly different approaches to integrating SSMs into computer vision:

*   **Scanning Strategy**: V Mamba's more complex four-way cross-scan aims for a "purer" global receptive field without needing explicit position embeddings <a class="yt-timestamp" data-t="01:43:01">[01:43:01]</a>. Vim's bidirectional approach is simpler, relying on position embeddings for context <a class="yt-timestamp" data-t="01:09:54">[01:09:54]</a>. The ablation study in Vim suggests that extensive scanning might not be as critical if position embeddings are used <a class="yt-timestamp" data-t="01:50:52">[01:50:52]</a>.
*   **Model Depth**: V Mamba's omission of MLP blocks makes its core VSS block shallower, potentially allowing for more blocks to be stacked given a similar computational budget <a class="yt-timestamp" data-t="02:10:07">[02:10:07]</a>. Vim retains the MLP, adhering closer to traditional Transformer block structures <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>.
*   **Performance vs. Speed**: V Mamba appears to achieve slightly better benchmark scores for a given parameter count <a class="yt-timestamp" data-t="01:53:19">[01:53:19]</a>. Vim, driven by its autonomous vehicle application context, prioritizes raw speed and memory efficiency, even if it means a slight trade-off in accuracy <a class="yt-timestamp" data-t="01:00:03">[01:00:03]</a> <a class="yt-timestamp" data-t="01:56:58">[01:56:58]</a>. This focus is apparent in its detailed analysis of GPU memory I/O <a class="yt-timestamp" data-t="01:23:09">[01:23:09]</a>.

## Applications of Vision Mambas

The linear complexity and efficient processing of Mamba models make them highly suitable for [[applications_of_mambas_in_3d_reconstruction_and_vision_language_models | applications requiring high-resolution images or long sequences]], where ViTs struggle due to quadratic scaling <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a> <a class="yt-timestamp" data-t="01:26:56">[01:26:56]</a>:
*   **Autonomous Vehicles**: Critical for real-time processing of high-resolution camera feeds, where even small distant objects (like stop signs or other vehicles) must be detected reliably <a class="yt-timestamp" data-t="01:27:06">[01:27:06]</a>.
*   **Medical Imaging**: Analyzing large, detailed medical images (e.g., for cancer detection) where maintaining full resolution is paramount <a class="yt-timestamp" data-t="01:36:56">[01:36:56]</a>.
*   **Remote Sensing**: Processing large satellite or aerial imagery datasets <a class="yt-timestamp" data-t="01:37:18">[01:37:18]</a>.
*   **Video Understanding**: Given that video adds another dimension of time, the linear complexity of SSMs is even more beneficial for [[video_mamba_for_video_understanding | long video analysis]] <a class="yt-timestamp" data-t="02:06:03">[02:06:03]</a> <a class="yt-timestamp" data-t="01:37:18">[01:37:18]</a>.
*   [[vision_language_models | Vision language models]] and [[vision_language_models_and_object_manipulation | object manipulation]] (Clip-style pre-training) <a class="yt-timestamp" data-t="01:46:43">[01:46:43]</a>.

## Conclusion

Both V Mamba and Vision Mamba demonstrate the potential of SSMs as efficient [[comparison_of_mamba_models_in_language_and_vision_contexts | vision backbones]], offering competitive performance while significantly improving computational and memory efficiency compared to ViTs <a class="yt-timestamp" data-t="02:35:05">[02:35:05]</a>. While V Mamba generally edges out Vim in benchmark accuracy, Vim's focus on hardware-aware designs and speed makes it compelling for latency-sensitive [[limitations_and_potential_of_mamba_models_in_ai | edge computing applications]] <a class="yt-timestamp" data-t="01:53:53">[01:53:53]</a>. The findings from Vim's ablation study also provide valuable insights, suggesting that complex scanning strategies might not be necessary if positional information is adequately handled by other means like position embeddings <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.