---
title: Benchmarking vision models
videoId: RtHDu6kFPb8
---

From: [[hu-po]] <br/> 

Benchmarking is a crucial process in the development and evaluation of [[Comparison of vision architectures | vision architectures]] and [[Vision language models | vision models]]. It involves using standardized datasets and metrics to compare the performance of different models, helping researchers understand their capabilities and limitations <a class="yt-timestamp" data-t="08:06:08">[08:06:08]</a>. The primary goal is often to assess how well a model can compress an image into a vector representation, which is then judged by its effectiveness on generic tasks <a class="yt-timestamp" data-t="07:33:14">[07:33:14]</a>.

## Key Benchmarks and Tasks

Several classic computer vision tasks serve as benchmarks for evaluating [[Performance analysis and benchmarks | vision models]]:

### Image Classification (ImageNet 1K)
*   **Description:** ImageNet 1K is a widely used classification dataset comprising 1.4 million annotated images categorized according to the WordNet hierarchy <a class="yt-timestamp" data-t="03:59:12">[03:59:12]</a>. The task involves consuming an image and classifying it into one of 1,000 predefined categories (e.g., dog, cat, tree) <a class="yt-timestamp" data-t="03:59:46">[03:59:46]</a>.
*   **Metric:** Top-1 Accuracy is a common metric, meaning the model's single best guess must be the exact correct category <a class="yt-timestamp" data-t="04:33:36">[04:33:36]</a>. ImageNet classification has become less indicative of general backbone quality due to models overfitting to its specific characteristics <a class="yt-timestamp" data-t="04:40:18">[04:40:18]</a>.

### Object Detection and Instance Segmentation (COCO)
*   **Description:** COCO (Common Objects in Context) is a large-scale dataset from Microsoft designed for object detection, segmentation, keypoint detection, and captioning <a class="yt-timestamp" data-t="04:10:07">[04:10:07]</a>. It contains 328,000 images <a class="yt-timestamp" data-t="04:11:19">[04:11:19]</a>.
*   **Metric:** Average Precision (AP) for bounding box detection (AP box) is used to evaluate the accuracy of predicted bounding boxes, considering overlap with ground truth boxes at various Intersection over Union (IoU) thresholds (e.g., AP@50, AP@75) <a class="yt-timestamp" data-t="04:08:14">[04:08:14]</a>.

### Semantic Segmentation (ADE20K)
*   **Description:** ADE20K is a semantic segmentation benchmark containing over 20,000 scene-centric images meticulously annotated with pixel-level object and object-part labels across 150 categories (e.g., sky, road, grass) <a class="yt-timestamp" data-t="04:24:49">[04:24:49]</a>. This is a "dense" task, requiring classification for every single pixel <a class="yt-timestamp" data-t="04:21:49">[04:21:49]</a>.
*   **Metric:** Mean Intersection over Union (mIoU) is often used to measure the overlap between the predicted segmentation mask and the ground truth mask <a class="yt-timestamp" data-t="04:19:20">[04:19:20]</a>.

## Case Study: [[Comparison of Mamba models in language and vision contexts | V Mamba]] vs. [[Vision Mamba model designs | Vision Mamba]]

Two papers, released around the same time in January 2024, introduce [[Vision Mamba model designs | Vision Mamba]] (Vim) and [[Comparison of Mamba models in language and vision contexts | V Mamba]] as new [[Vision Mamba model designs | vision Mamba]] models <a class="yt-timestamp" data-t="05:28:30">[05:28:30]</a>. Both aim to provide efficient visual representation learning, offering an alternative to Transformers and Convolutional Neural Networks (CNNs) by utilizing State Space Models (SSMs) <a class="yt-timestamp" data-t="05:01:21">[05:01:21]</a>. A key advantage of [[Vision Mamba model designs | Mamba]] models is their linear complexity with respect to input sequence length (image size), making them more efficient than Transformers which have quadratic complexity <a class="yt-timestamp" data-t="05:01:21">[05:01:21]</a>.

| Model        | Parameters (Millions) | ImageNet 1K (Top-1 Acc.) | COCO (AP Box) | ADE20K (mIoU) | Scan Directions | Position Embeddings | MLP Block | Hardware Focus      |
| :----------- | :-------------------- | :----------------------- | :------------ | :------------ | :-------------- | :------------------ | :-------- | :------------------ |
| [[Comparison of Mamba models in language and vision contexts | V Mamba]] (V-Mamba-T) | 22 <a class="yt-timestamp" data-t="04:39:27">[04:39:27]</a>      | 82.0 <a class="yt-timestamp" data-t="04:46:58">[04:46:58]</a>            | 46.0 <a class="yt-timestamp" data-t="04:48:47">[04:48:47]</a>      | 47.7 <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>        | 4 (Cross-scan) <a class="yt-timestamp" data-t="03:27:30">[03:27:30]</a>     | No <a class="yt-timestamp" data-t="01:10:06">[01:10:06]</a>           | No <a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a>    | General efficiency  |
| [[Vision Mamba model designs | Vision Mamba]] (Vim-T) | 26 <a class="yt-timestamp" data-t="04:46:46">[04:46:46]</a>      | 80.0 <a class="yt-timestamp" data-t="04:40:40">[04:40:40]</a>            | 45.3 <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>      | 40.0 <a class="yt-timestamp" data-t="04:19:20">[04:19:20]</a>        | 2 (Bidirectional) <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a> | Yes <a class="yt-timestamp" data-t="01:09:56">[01:09:56]</a>          | Yes <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>   | Edge/Autonomous Vehicles <a class="yt-timestamp" data-t="00:54:52">[00:54:52]</a> |

**Key Differences and Performance Insights:**
*   **Scanning Strategy:** [[Comparison of Mamba models in language and vision contexts | V Mamba]] uses a "cross-scan module" that traverses the image in four directions to achieve a global receptive field <a class="yt-timestamp" data-t="03:30:19">[03:30:19]</a>. [[Vision Mamba model designs | Vision Mamba]] employs bidirectional Mamba blocks, scanning only in forward and backward directions <a class="yt-timestamp" data-t="03:25:25">[03:25:25]</a>.
*   **Position Embeddings:** [[Comparison of Mamba models in language and vision contexts | V Mamba]] refrains from using position embeddings due to its causal nature, while [[Vision Mamba model designs | Vision Mamba]] includes them <a class="yt-timestamp" data-t="01:10:06">[01:10:06]</a>. An ablation study in the [[Vision Mamba model designs | Vision Mamba]] paper suggested that bidirectional scanning offered minimal performance gain over unidirectional scanning, possibly due to the strength of position embeddings <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.
*   **MLP Block:** [[Comparison of Mamba models in language and vision contexts | V Mamba]]'s VSS block is shallower than a traditional Vision Transformer (ViT) block, discarding the Multi-Layer Perceptron (MLP) module to allow for more stacked blocks with a similar computational budget <a class="yt-timestamp" data-t="01:10:06">[01:10:06]</a>. [[Vision Mamba model designs | Vision Mamba]] retains the MLP block <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>.
*   **Results:** [[Comparison of Mamba models in language and vision contexts | V Mamba]] generally shows slightly better performance across the benchmarks, achieving higher accuracy on ImageNet 1K and better AP box scores on COCO <a class="yt-timestamp" data-t="04:46:58">[04:46:58]</a>, <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>. However, the differences are often marginal, and [[Vision Mamba model designs | Vision Mamba]] prioritizes speed and efficiency, making it suitable for edge computing applications like autonomous vehicles where low latency and small compute footprint are critical <a class="yt-timestamp" data-t="00:59:56">[00:59:56]</a>.

## Factors Influencing Benchmarking

### Image Resolution and Computational Complexity
[[Vision Mamba model designs | Mamba]] models excel with high-resolution images because their linear complexity allows them to scale much better than [[Vision language models | Vision Transformers]] (ViTs), which suffer from quadratic complexity <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. This is particularly beneficial for applications like autonomous vehicles or medical imaging, where retaining full image resolution is crucial for detecting small, distant objects or subtle anomalies <a class="yt-timestamp" data-t="01:26:59">[01:26:59]</a>.

### Hardware-Aware Design
The performance of [[Vision Mamba model designs | vision models]] can be significantly influenced by hardware-aware designs that optimize memory access and computation <a class="yt-timestamp" data-t="01:23:33">[01:23:33]</a>. For instance, [[Vision Mamba model designs | Vision Mamba]]'s design minimizes memory I/O by strategically moving data between different GPU memory caches (e.g., high-bandwidth memory (HBM) and SRAM) and recomputing intermediate activations instead of storing them <a class="yt-timestamp" data-t="01:25:27">[01:25:27]</a>. Such optimizations can make direct speed comparisons between models difficult, as performance might vary across different GPU architectures <a class="yt-timestamp" data-t="01:54:50">[01:54:50]</a>.

### Inductive Biases and Receptive Fields
Different [[Comparison of vision architectures | vision architectures]] inherently possess different inductive biases:
*   **ViTs** (e.g., DeiT): Exhibit a global receptive field, meaning every patch can influence every other patch, leading to powerful fitting capabilities but quadratic complexity <a class="yt-timestamp" data-t="01:39:59">[01:39:59]</a>.
*   **CNNs** (e.g., ResNet, ConvNeXt): Have a local receptive field, providing linear scalability but potentially limiting their ability to model global relationships <a class="yt-timestamp" data-t="01:16:18">[01:16:18]</a>.
*   [[Vision Mamba model designs | **Mamba**]] models: Aim to combine the best of both worlds—linear complexity like CNNs while retaining a global receptive field like ViTs through mechanisms like the cross-scan module or bidirectional processing <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. The effective receptive field of [[Comparison of Mamba models in language and vision contexts | V Mamba]], for example, shows a cross-shaped pattern, which adapts to be more global after training <a class="yt-timestamp" data-t="01:54:45">[01:54:45]</a>.

### Pre-training and Distillation
Model performance on benchmarks can also be influenced by pre-training strategies. For example, DeiT models are [[Vision language models with pretrained components | Vision Transformers]] distilled from Convolutional Neural Networks (CNNs), demonstrating how pre-training on existing models can impact performance <a class="yt-timestamp" data-t="01:08:52">[01:08:52]</a>. Future work for [[Vision Mamba model designs | Mamba]] models includes exploring their suitability for unsupervised tasks like masked image modeling pre-training <a class="yt-timestamp" data-t="01:16:09">[01:16:09]</a>.

## Resources

*   **Papers With Code:** This website provides leaderboards for various computer vision benchmarks, allowing researchers to track the performance of different models over time <a class="yt-timestamp" data-t="03:53:55">[03:53:55]</a>.

Benchmarking is essential for tracking progress and identifying promising [[Comparison of vision architectures | vision architectures]], especially for [[Vision language models and their applications | applications]] requiring high efficiency and specific performance characteristics.