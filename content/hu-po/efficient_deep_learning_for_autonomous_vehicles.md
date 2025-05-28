---
title: Efficient deep learning for autonomous vehicles
videoId: RtHDu6kFPb8
---

From: [[hu-po]] <br/> 

The field of [[deep_learning_and_neural_networks | deep learning]] in [[computer_vision_deep_dive | computer vision]] has seen significant advancements, with two primary foundation models for visual representation learning: Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) <a class="yt-timestamp" data-t="01:21:53">[01:21:53]</a>. While ViTs have generally surpassed CNNs in fitting capabilities and popularity, especially in the language space <a class="yt-timestamp" data-t="01:30:04">[01:30:04]</a>, they suffer from quadratic complexity concerning image resolution, making them computationally expensive for high-resolution images <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a> <a class="yt-timestamp" data-t="01:21:20">[01:21:20]</a>. CNNs, by contrast, offer linear complexity but have limitations in global receptive fields <a class="yt-timestamp" data-t="01:37:49">[01:37:49]</a>.

This trade-off between [[performance_and_efficiency_in_machine_learning_models | performance and efficiency]] is particularly critical for applications like autonomous vehicles, where [[energy_and_compute_optimization_in_ai_models | energy and compute optimization]] is paramount <a class="yt-timestamp" data-t="00:56:51">[00:56:51]</a>. This has led to the exploration of alternative architectures, such as State Space Models (SSMs), specifically the Mamba architecture <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Mamba Architecture for Vision

Mamba, a State Space Model, is presented as an alternative to Transformers or ConvNets <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Initially popular for sequence-to-sequence language models, Mamba is now being applied in the vision space <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. The name "Mamba" is derived from a type of snake known for its speed, highlighting the architecture's focus on efficiency <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

The core advantage of Mamba models is their computational efficiency, achieving linear complexity while retaining global receptive fields <a class="yt-timestamp" data-t="01:52:53">[01:52:53]</a>. This contrasts with Vision Transformers, which have quadratic complexity with respect to input sequence length or image size <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>.

### State Space Models Explained

State Space Models map a continuous input signal (stimulation XT) to a continuous output (response YT) through a compressed hidden state (H) <a class="yt-timestamp" data-t="00:59:23">[00:59:23]</a>. This hidden state acts as a bottleneck, limiting the information passed from token to token, thereby reducing compute but potentially leading to information loss <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

SSMs typically formulate operations as linear ordinary differential equations with parameters A, B, C, and D (for skip connections) <a class="yt-timestamp" data-t="01:00:20">[01:00:20]</a>. For integration into [[deep_learning_and_neural_networks | deep learning algorithms]], these continuous systems are discretized using methods like Zero-Order Hold (ZOH) <a class="yt-timestamp" data-t="01:01:11">[01:01:11]</a>.

### Addressing Direction Sensitivity in Vision

Unlike textual data, which has a causal, one-dimensional sequence flow, images are 2D and lack inherent causality <a class="yt-timestamp" data-t="03:08:18">[03:08:18]</a>. Directly applying a 1D SSM to a flattened image sequence can result in restricted receptive fields <a class="yt-timestamp" data-t="03:19:52">[03:19:52]</a>. Two papers propose different solutions to this "direction-sensitive problem":

*   **V-Mamba (Visual Mamba)**: Introduces a **Cross-Scan Module (CSM)** <a class="yt-timestamp" data-t="02:02:03">[02:02:03]</a>. The CSM adopts a four-way scanning strategy (e.g., left-to-right, top-to-down, and their permutations) across the feature map <a class="yt-timestamp" data-t="02:05:15">[02:05:15]</a>. This ensures each element integrates information from all other locations in different directions, yielding a global receptive field without increasing linear computational complexity <a class="yt-timestamp" data-t="03:22:23">[03:22:23]</a> <a class="yt-timestamp" data-t="03:36:20">[03:36:20]</a>.
*   **Vision Mamba (Vim)**: Uses **Bidirectional Mamba Blocks** <a class="yt-timestamp" data-t="02:21:52">[02:21:52]</a>. This approach processes tokens with both forward (left-to-right, top-to-down) and backward (right-to-left, bottom-to-up) directions <a class="yt-timestamp" data-t="03:51:50">[03:51:50]</a>. Vim also incorporates position embeddings and a learnable classification token, similar to ViTs <a class="yt-timestamp" data-t="03:54:54">[03:54:54]</a>.

### Model Architecture Differences

| Feature               | V-Mamba (Visual Mamba)                                          | Vision Mamba (Vim)                                                       |
| :-------------------- | :---------------------------------------------------------------- | :----------------------------------------------------------------------- |
| Direction Handling    | Cross-Scan Module (4-way scanning) <a class="yt-timestamp" data-t="01:40:01">[01:40:01]</a> | Bidirectional Mamba Blocks (forward and backward) <a class="yt-timestamp" data-t="03:51:50">[03:51:50]</a> |
| Position Embeddings   | No <a class="yt-timestamp" data-t="02:06:05">[02:06:05]</a>                                                     | Yes <a class="yt-timestamp" data-t="02:06:05">[02:06:05]</a>                                                       |
| Class Token           | No <a class="yt-timestamp" data-t="02:06:05">[02:06:05]</a>                                                     | Yes <a class="yt-timestamp" data-t="02:06:05">[02:06:05]</a>                                                       |
| MLP in blocks         | No, "shallower" design <a class="yt-timestamp" data-t="02:06:05">[02:06:05]</a>                                 | Yes <a class="yt-timestamp" data-t="02:06:05">[02:06:05]</a>                                                       |
| Activation Function   | SiLU <a class="yt-timestamp" data-t="02:06:05">[02:06:05]</a>                                                      | (Not specified, likely ReLU or GeLU as commonly seen in Transformers)   |

## Performance and Efficiency for Autonomous Vehicles

Autonomous vehicle companies, such as Horizon Robotics (a contributor to the Vision Mamba paper), are highly interested in efficient [[deep_learning_and_neural_networks | deep learning]] architectures <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

>[!info] Why Efficiency Matters in Autonomous Vehicles
>Autonomous vehicles require very low latency and must run models on edge devices or the car's GPU directly, not via API calls to a server <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. This necessitates extremely quick and efficient processing <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. Furthermore, unlike general vision-language models where image compression is acceptable (e.g., for calorie counting from food photos), autonomous vehicles cannot afford to reduce image resolution <a class="yt-timestamp" data-t="02:27:06">[02:27:06]</a>. Small, distant objects (e.g., other cars, stop signs) can be critical, requiring full-resolution images to maintain detectability <a class="yt-timestamp" data-t="02:27:57">[02:27:57]</a>.

Mamba models are highlighted for their speed, especially at higher resolutions, and improved GPU memory usage compared to ViTs <a class="yt-timestamp" data-t="02:22:30">[02:22:30]</a>. For example, Vision Mamba (Vim) can save significant GPU memory on large images (e.g., 1248x1248) <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>. The computational complexity of self-attention in ViTs is O(M²), where M is sequence length, making them explode with larger images <a class="yt-timestamp" data-t="02:21:14">[02:21:14]</a>. In contrast, SSMs have O(N²M) complexity, where N is the SSM dimension (much smaller than M), demonstrating their linear scaling <a class="yt-timestamp" data-t="02:26:30">[02:26:30]</a>.

### Benchmark Comparisons

Both V-Mamba and Vision Mamba are evaluated on standard [[computer_vision_deep_dive | computer vision]] benchmarks:
*   **ImageNet 1K**: A classification dataset with 14 million annotated images and 1,000 categories <a class="yt-timestamp" data-t="00:39:12">[00:39:12]</a>.
*   **COCO (Common Objects in Context)**: A large-scale dataset for object detection and instance segmentation, among other tasks <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>.
*   **ADE20K**: A semantic segmentation benchmark requiring pixel-level classification into 150 categories <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a>.

In a head-to-head comparison:
*   **ImageNet-1K Accuracy**: V-Mamba (e.g., V-Mamba-S with 22M parameters) achieves 82% top-1 accuracy <a class="yt-timestamp" data-t="01:53:31">[01:53:31]</a>, while Vision Mamba (Vim-S with 26M parameters) achieves 80% <a class="yt-timestamp" data-t="01:53:50">[01:53:50]</a>. This suggests V-Mamba performs slightly better for fewer parameters <a class="yt-timestamp" data-t="01:54:14">[01:54:14]</a>.
*   **COCO Object Detection**: V-Mamba generally shows slightly better AP box scores compared to Vim for similar model sizes <a class="yt-timestamp" data-t="01:54:14">[01:54:14]</a>.
*   **ADE20K Semantic Segmentation**: V-Mamba also outperforms Vim, for instance, a V-Mamba with 46M parameters achieves 47-48% mIoU, while a Vim with 13M parameters achieves 40% <a class="yt-timestamp" data-t="01:54:14">[01:54:14]</a>.

V-Mamba generally shows slightly better benchmark performance across the board <a class="yt-timestamp" data-t="01:54:14">[01:54:14]</a>. However, it's worth noting that Vim aims for greater computational and memory efficiency, which might explain its slightly lower performance <a class="yt-timestamp" data-t="00:56:51">[00:56:51]</a>.

### GPU Memory Optimization

Vision Mamba (Vim) implements specific [[developments_in_deep_learning_hardware | hardware-aware designs]] to optimize performance on GPUs. They focus on minimizing memory I/O between different GPU memory components, such as High Bandwidth Memory (HBM) and SRAM <a class="yt-timestamp" data-t="02:39:09">[02:39:09]</a>. SRAM has larger bandwidth, while HBM has larger memory size <a class="yt-timestamp" data-t="02:44:03">[02:44:03]</a>. Vim's SSM implementation optimizes memory I/O to O(BME + N) compared to O(BME * N), where B is batch size, M is sequence length, E is expanded state dimension, and N is SSM dimension <a class="yt-timestamp" data-t="02:45:06">[02:45:06]</a>. They also recompute intermediate activations during the backward pass to reduce GPU memory requirements <a class="yt-timestamp" data-t="02:51:30">[02:51:30]</a>. This attention to detail in [[energy_and_compute_optimization_in_ai_models | hardware-aware design]] is crucial for deployment in resource-constrained environments like autonomous vehicles.

## Future Directions

While Mamba models show promise for high-resolution images and videos, particularly in time-sensitive and edge computing applications like autonomous vehicles, medical imaging, and remote sensing <a class="yt-timestamp" data-t="02:26:03">[02:26:03]</a> <a class="yt-timestamp" data-t="02:30:53">[02:30:53]</a>, it remains to be seen if they will usurp Transformers in more generic vision tasks <a class="yt-timestamp" data-t="02:48:40">[02:48:40]</a>.

The ability of V-Mamba to adapt its effective receptive field from local (before training) to global (after training) suggests a flexible architecture <a class="yt-timestamp" data-t="03:31:55">[03:31:55]</a>. This adaptability allows the model to learn the most useful receptive field for visual representations <a class="yt-timestamp" data-t="03:38:26">[03:38:26]</a>.