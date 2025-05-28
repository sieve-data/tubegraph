---
title: Comparison of vision architectures
videoId: RtHDu6kFPb8
---

From: [[hu-po]] <br/> 

The field of visual representation learning is dominated by two primary [[computer_vision_deep_dive | vision architectures]]: [[Vision language models | Convolutional Neural Networks]] (CNNs) and [[Vision language models | Vision Transformers]] (ViTs) <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>. Recently, a new class of models, [[Vision language models | Mamba models]] (based on State Space Models), have emerged as potential alternatives, particularly in the vision domain <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. This article provides a [[comparative_analysis_of_model_architectures | comparative analysis of these architectures]], focusing on their characteristics, efficiency, and performance on standard [[benchmarking_vision_models | vision benchmarks]].

## Dominant Architectures

### Convolutional Neural Networks (CNNs)
CNNs have been popular for visual representation learning, exhibiting remarkable scalability with linear complexity concerning image resolution <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>. This means their computational demands increase proportionally to the image size <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>. However, CNNs typically have a local receptive field, meaning that higher layers in the network only "pay attention" to a subset of pixels directly beneath them, limiting their ability to capture global context across an entire image <a class="yt-timestamp" data-t="16:54:00">[16:54:54]</a>. Their weights are considered more static as the same learned kernels are convolved across the image regardless of the input content <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>.

### Vision Transformers (ViTs)
[[Vision language models | Vision Transformers]] have surpassed CNNs in fitting capabilities due to their ability to incorporate global receptive fields and dynamic weights <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>. ViTs process images by cutting them into patches and treating these patches as a sequence of tokens, similar to how Transformers handle text <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>. The core mechanism, self-attention, allows every patch to influence every other patch, leading to a global receptive field <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>.

Despite their strong modeling power, ViTs suffer from quadratic complexity with respect to the input sequence length (or image size), meaning their computational and memory demands grow quadratically as image resolution increases <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>. This makes them less suitable for high-resolution images <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>. Efforts have been made to improve their efficiency by constraining the attention mechanism, but the quadratic scaling remains a fundamental challenge <a class="yt-timestamp" data-t="28:18:00">[28:18:00]</a>.

Common elements in ViTs include:
*   **Patch Embeddings**: Images are divided into patches, which are then projected into tokens <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>.
*   **Position Embeddings**: Small vectors added to patch tokens to provide spatial information, mitigating the bias introduced by flattening 2D images into 1D sequences <a class="yt-timestamp" data-t="15:02:00">[15:02:00]</a>.
*   **Class Token**: An extra learnable token concatenated to the patch sequence, intended to accumulate global semantic information for classification tasks <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   **Multi-Layer Perceptron (MLP)**: Used after the self-attention block in a Transformer block <a class="yt-timestamp" data-t="19:00:00">[19:00:00]</a>.

## [[Comparison of Mamba models in language and vision contexts | The Rise of Vision Mambas]]

[[Vision language models | Mamba models]], based on State Space Models (SSMs), emerged as a promising alternative to address the quadratic complexity of [[Vision language models | Transformers]] while retaining a global receptive field <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>. They achieve linear complexity by processing sequences through a compressed hidden state, which acts as a bottleneck for information flow <a class="yt-timestamp" data-t="29:48:00">[29:48:00]</a>. This limits computational cost but relies on the hidden state's ability to compress crucial information without significant loss <a class="yt-timestamp" data-t="30:26:00">[30:26:00]</a>.

Two notable papers, both released in January 2024, introduce [[Vision language models | Mamba models]] for vision:
1.  **Vamba (Visual Mamba)** <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>
2.  **Vim (Vision Mamba)** <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>

These papers offer different approaches to adapt SSMs for 2D visual data, aiming for efficient visual representation learning.

### Vamba (Visual Mamba)
Vamba, developed by researchers from UCAS, Huawei Inc, and Pen Lab <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>, aims to achieve linear complexity without sacrificing global receptive fields <a class="yt-timestamp" data-t="19:52:00">[19:52:00]</a>.
*   **Cross-Scan Module (CSM)**: To address the "direction-sensitive issue" (the bias from flattening 2D images into 1D sequences like left-to-right, top-to-down), Vamba introduces a Cross-Scan Module <a class="yt-timestamp" data-t="20:02:00">[20:02:00]</a>. This module performs a four-way scanning strategy (left-to-right, right-to-left, top-to-down, bottom-to-up) across the feature map <a class="yt-timestamp" data-t="32:27:00">[32:27:00]</a>. This ensures that each element integrates information from all other locations in different directions, aiming for a global receptive field <a class="yt-timestamp" data-t="32:36:00">[32:36:00]</a>.
*   **Architecture**: Vamba does not utilize position embeddings <a class="yt-timestamp" data-t="01:20:06">[01:20:06]</a> or a Multi-Layer Perceptron (MLP) block in its VSS block, making it shallower than ViT blocks <a class="yt-timestamp" data-t="01:21:05">[01:21:05]</a>.
*   **Effective Receptive Field (ERF)**: Before training, Vamba exhibits a local ERF, but after training, it transforms to a global ERF with a distinctive cross-shaped activation pattern <a class="yt-timestamp" data-t="01:31:50">[01:31:50]</a>. The authors argue this signifies an adaptive process in the model's global capacity, allowing it to adapt its receptive field for better visual representations <a class="yt-timestamp" data-t="01:32:33">[01:32:33]</a>.

### Vim (Vision Mamba)
Vim, from Huazhong University of Science and Technology, Horizon Robotics, and Beijing Academy of Artificial Intelligence <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>, focuses on efficient visual representation learning with bidirectional State Space Models <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>. Horizon Robotics' involvement highlights the model's emphasis on applications requiring small compute footprints, such as autonomous vehicles <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a> and [[vision_language_models_in_ai_agents | Edge Computing]] <a class="yt-timestamp" data-t="01:10:12">[01:10:12]</a>.
*   **Bidirectional Mamba Blocks**: Vim uses bidirectional Mamba blocks to address directional sensitivity <a class="yt-timestamp" data-t="23:18:00">[23:18:00]</a>, processing input sequences in both forward (left-to-right, top-to-down) and backward (right-to-left, bottom-to-up) directions <a class="yt-timestamp" data-t="00:35:39">[00:35:39]</a>. This is a simpler approach compared to Vamba's four-way scan <a class="yt-timestamp" data-t="00:36:01">[00:36:01]</a>.
*   **Architecture**: Vim incorporates position embeddings and a class token <a class="yt-timestamp" data-t="01:09:54">[01:09:54]</a>. It also retains an MLP block after its Mamba encoder <a class="yt-timestamp" data-t="01:11:55">[01:11:55]</a>.
*   **Ablation Study**: An ablation study showed that including bidirectional processing (forward and backward) did not significantly improve performance on ImageNet or ADE20K compared to a unidirectional approach <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>. This suggests that the position embeddings might be strong enough to negate the need for explicit bidirectional scanning <a class="yt-timestamp" data-t="01:50:54">[01:50:54]</a>.
*   **Hardware Awareness**: Vim's design explicitly considers GPU memory hierarchy (High Bandwidth Memory (HBM) vs. SRAM) to optimize memory I/O and reduce computational cost, which is crucial for [[vision_language_models_in_ai_agents | Edge Computing]] <a class="yt-timestamp" data-t="01:23:09">[01:23:09]</a>.

## [[benchmarking_vision_models | Comparative Analysis]]

### Complexity and Efficiency
The primary advantage of [[Vision language models | Mamba models]] over [[Vision language models | Vision Transformers]] is their linear computational complexity with respect to image resolution, in contrast to ViTs' quadratic complexity <a class="yt-timestamp" data-t="01:26:40">[01:26:40]</a>. This allows Mamba models to handle much larger image sizes (e.g., 1248x1248 pixels) with significantly lower GPU memory usage compared to ViTs, which would "explode" at such resolutions <a class="yt-timestamp" data-t="01:10:09">[01:10:09]</a>. This is particularly beneficial for [[vision_language_models_in_ai_agents | Edge Computing]] and autonomous vehicle applications where low latency and limited compute resources are critical <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>.

### Receptive Field Comparison
*   **ViTs**: Maintain a global receptive field, meaning every patch can interact with every other patch, leading to powerful contextual understanding but high computational cost <a class="yt-timestamp" data-t="01:41:51">[01:41:51]</a>.
*   **CNNs**: Have a local receptive field, focusing on nearby pixels through convolutions <a class="yt-timestamp" data-t="01:42:19">[01:42:19]</a>.
*   **Mamba Models (Vamba)**: Claim to achieve global receptive fields while maintaining linear complexity <a class="yt-timestamp" data-t="01:52:47">[01:52:47]</a>. Vamba's cross-scan mechanism leads to a cross-shaped effective receptive field, prioritizing horizontal and vertical dependencies <a class="yt-timestamp" data-t="01:55:40">[01:55:40]</a>.

### [[benchmarking_vision_models | Benchmarking Vision Models]]

Both Vamba and Vim were [[benchmarking_vision_models | benchmarked]] on the same three standard computer vision tasks:
1.  **ImageNet-1K**: For image classification (e.g., identifying objects like "dog" or "cat") <a class="yt-timestamp" data-t="03:52:20">[03:52:20]</a>.
2.  **COCO (Common Objects in Context)**: For object detection (bounding boxes around objects) and instance segmentation (pixel-level masks for objects) <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.
3.  **ADE20K**: For semantic segmentation (pixel-level classification of entire scenes, e.g., "sky," "road," "tree") <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.

#### ImageNet-1K Accuracy
*   Vamba-S (22M parameters): 82% top-1 accuracy <a class="yt-timestamp" data-t="01:53:34">[01:53:34]</a>
*   Vim-S (26M parameters): 80% top-1 accuracy <a class="yt-timestamp" data-t="01:53:46">[01:53:46]</a>
*   Vamba-B (larger model): 83% top-1 accuracy <a class="yt-timestamp" data-t="00:47:04">[00:47:04]</a>

Vamba generally showed slightly better performance on ImageNet-1K for comparable model sizes <a class="yt-timestamp" data-t="01:54:14">[01:54:14]</a>.

#### COCO Object Detection/Instance Segmentation
*   Vamba-T: 46 (AP Box) / 42 (AP Mask) <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>
*   Vim-T: 45 (AP Box) / 39 (AP Mask) <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>

Vamba consistently outperformed Vim in COCO object detection and instance segmentation <a class="yt-timestamp" data-t="00:49:02">[00:49:02]</a>.

#### ADE20K Semantic Segmentation
*   Vamba-T (22M parameters, 512x512 image): 47 (mIoU) <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a>
*   Vim-T (13M parameters, 224x224 image): 40 (mIoU) <a class="yt-timestamp" data-t="00:49:20">[00:49:20]</a>
*   Vim-S (46M parameters, 512x512 image): 44 (mIoU) <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>

Again, Vamba shows stronger performance, though direct comparison is sometimes complicated by slightly different image resolutions and parameter counts used in the tables <a class="yt-timestamp" data-t="00:49:45">[00:49:45]</a>.

## Applications and Future Directions

[[Vision language models | Mamba models]] hold significant potential for applications requiring high efficiency and the processing of high-resolution images or long sequences, such as:
*   [[vision_language_models_in_ai_agents | Edge Computing]] <a class="yt-timestamp" data-t="01:10:12">[01:10:12]</a>
*   Autonomous Vehicles: Where high-resolution images are crucial to detect distant small objects (e.g., cars or road signs) and low latency is required <a class="yt-timestamp" data-t="01:27:06">[01:27:06]</a>.
*   High-Resolution Medical Images: Essential for tasks like cancer detection, where downsampling images can lead to loss of critical information <a class="yt-timestamp" data-t="01:36:56">[01:36:56]</a>.
*   Remote Sensing Images <a class="yt-timestamp" data-t="01:37:18">[01:37:18]</a>.
*   Long Videos: Where the additional dimension of time would exacerbate the quadratic complexity of ViTs <a class="yt-timestamp" data-t="02:06:04">[02:06:04]</a>.

While [[Vision language models with pretrained components | Mamba models]] may not "usurp" [[Vision language models | Transformers]] as the leading generic [[Vision language models | vision backbone]] due to the strong "Transformer brand" <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>, they are poised to gain traction in latency-sensitive and resource-constrained scenarios <a class="yt-timestamp" data-t="01:53:53">[01:53:53]</a>.

## Conclusion

In the "battle of the mambas," Vamba generally exhibited slightly better performance on the common [[benchmarking_vision_models | vision benchmarks]] (ImageNet-1K, COCO, ADE20K) compared to Vim <a class="yt-timestamp" data-t="01:54:14">[01:54:14]</a>. Vamba's innovative cross-scan module, enabling four-way scanning and achieving an adaptive cross-shaped effective receptive field after training, distinguishes its approach to handling 2D visual data <a class="yt-timestamp" data-t="01:55:40">[01:55:40]</a>. Vim's emphasis on hardware-aware designs and bidirectional processing, though showing less performance gain in ablation studies, demonstrates a strong focus on practical efficiency for [[vision_language_models_in_ai_agents | Edge Computing]] applications <a class="yt-timestamp" data-t="01:56:01">[01:56:01]</a>.

Overall, both Vamba and Vim represent significant steps forward in developing efficient [[Vision language models | vision architectures]] that overcome the quadratic scaling limitations of [[Vision language models | Transformers]], making them highly relevant for [[vision_language_models_and_object_manipulation | AI agents]] operating in real-world, resource-constrained environments.