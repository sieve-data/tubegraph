---
title: Transformer architecture in image processing
videoId: LBFiKtUBHc0
---

From: [[hu-po]] <br/> 

[[Transformerbased model architectures | Transformer architectures]] are increasingly being applied to image processing, particularly in the domain of feature matching, a fundamental problem in computer vision <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## What is Feature Matching?
Feature matching is the process of identifying corresponding points between two or more images of the same object or scene <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. This allows for the calculation of geometry, such as camera positions and 3D point locations, to reconstruct 3D environments from 2D images <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Applications of Feature Matching
Feature matching is a core component of many computer vision applications:
*   **Simultaneous Localization and Mapping (SLAM)**: Used in devices like the Meta Quest 3 headset, where it simultaneously creates a 3D map and localizes the device within it using RGB cameras <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Robots also use SLAM to build maps for navigation <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Gaussian Splats**: The initial step to create Gaussian Splats from a series of images often involves an algorithm called Colmap, which relies on feature matching <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **3D Reconstruction and Photogrammetry** <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
*   **Camera Tracking** <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

## Traditional Feature Matching: SIFT
Historically, feature matching was dominated by hand-designed features, a practice referred to as "computer vision archaeology" <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Scale-Invariant Feature Transform (SIFT)**: An "ancient" algorithm designed long ago, still used in algorithms like Colmap for Gaussian Splats <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>. SIFT features are based on image gradients, pointing from dark to light areas in a local region <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   **Limitations of Hand-Designed Features**: In this older paradigm, small learnable models were trained on top of these hand-designed features <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. The current paradigm, however, uses deep learning to learn features even at the lowest levels <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   **Challenges**: Reliably describing points is challenging in conditions with symmetries, weak texture, or appearance changes <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

## LightGlue: A Modern Approach to Feature Matching
LightGlue is a deep neural network that learns to match local features across images, serving as a modern, deep learning-based approach to feature matching <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. It revisits and updates design decisions from its predecessor, SuperGlue <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

### Key Properties and Improvements:
*   **Efficiency**: LightGlue is more efficient in terms of both memory and computation <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. It can run in real-time and only requires about 4 GB of memory for calculating correspondences between two images <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. It is notably faster than SuperGlue, sometimes four times faster <a class="yt-timestamp" data-t="01:30:37">[01:30:37]</a>.
*   **Adaptiveness**: It is adaptive to the difficulty of the problem. Inference is faster on image pairs that are intuitively easy to match (e.g., large visual overlap, limited appearance change) <a class="yt-timestamp" data-t="01:11:07">[01:11:07]</a>. This is crucial for VR applications where image pairs are often very close together from a real-time camera feed <a class="yt-timestamp" data-t="01:12:04">[01:12:04]</a>.
*   **Robustness**: It works robustly in both indoor and outdoor environments, and critically, it does not require a depth sensor as a starting point <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>, <a class="yt-timestamp" data-t="01:16:08">[01:16:08]</a>. Depth sensors often struggle outdoors <a class="yt-timestamp" data-t="01:08:58">[01:08:58]</a>.
*   **Ease of Training**: LightGlue is easier to train, reaching state-of-the-art accuracy with just a few GPU days <a class="yt-timestamp" data-t="01:17:54">[01:17:54]</a>.

## LightGlue Architecture
LightGlue uses a stack of L identical layers (L=9 layers in their experiments) that process two sets of local features jointly <a class="yt-timestamp" data-t="01:26:58">[01:26:58]</a>. Each local feature consists of a 2D point position and a visual descriptor <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>.

### Layers and Attention
Each layer is composed of a self-attention unit and a cross-attention unit <a class="yt-timestamp" data-t="00:33:45">[00:33:45]</a>.
*   **Self-Attention**: Each point in an image attends to all points within the *same* image <a class="yt-timestamp" data-t="00:38:36">[00:38:36]</a>. This involves decomposing the point's state into query and key vectors <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>.
*   **Cross-Attention**: Each point in one image pulls information from points in the *other* image <a class="yt-timestamp" data-t="00:38:59">[00:38:59]</a>. This is done by computing the similarity between keys from both images <a class="yt-timestamp" data-t="00:58:33">[00:58:33]</a>.

### Positional Encoding
LightGlue utilizes [[layerwise_scaling_in_transformer_architectures | Rotary Positional Encoding]] (RoPE) in its self-attention units <a class="yt-timestamp" data-t="00:41:56">[00:41:56]</a>.
*   **Relative Position Emphasis**: RoPE is superior for this task because it emphasizes the relative position between points rather than their absolute position <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>. This is particularly useful in computer vision where the relative distances between 3D points remain constant despite camera translations <a class="yt-timestamp" data-t="00:57:18">[00:57:18]</a>.
*   **Contrast to Absolute Positional Encoding**: Traditional sinusoidal positional encodings, as used in original [[Transformerbased model architectures | Transformer models]] <a class="yt-timestamp" data-t="00:43:36">[00:43:36]</a>, or learned absolute encodings, tend to be specific to the training data and may not generalize well to longer sequences <a class="yt-timestamp" data-t="00:51:13">[00:51:13]</a>. RoPE offers a more robust way to capture long-range dependencies <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>.
*   **Efficiency**: The positional encoding is identical for all layers and is computed once and cached, further improving efficiency <a class="yt-timestamp" data-t="00:57:52">[00:57:52]</a>. Positional information is not applied during cross-attention, as relative positions are not meaningful across images <a class="yt-timestamp" data-t="00:59:31">[00:59:31]</a>.

### Confidence Classifier and Pruning
A confidence classifier, implemented as a small MLP (Multi-Layer Perceptron) <a class="yt-timestamp" data-t="01:08:26">[01:08:26]</a>, decides whether to halt inference and prune points at each layer <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>.
*   **Adaptive Depth and Width**: The model can stop computation early if enough points are confidently matched, adapting its "depth" (number of layers processed) <a class="yt-timestamp" data-t="01:11:13">[01:11:13]</a>. It also prunes "unmatchable" points, reducing the "width" (number of points) fed into subsequent layers, which combats the quadratic complexity of attention mechanisms <a class="yt-timestamp" data-t="01:03:57">[01:03:57]</a>. This pruning saves significant computation <a class="yt-timestamp" data-t="01:10:42">[01:10:42]</a>.
*   **Example**: Points that are clearly not co-visible across images (e.g., people in one image but not the other) are quickly pruned in early layers. More ambiguous features (like repeating window patterns) might take more layers to prune <a class="yt-timestamp" data-t="01:09:13">[01:09:13]</a>.

## Comparison with SuperGlue
LightGlue was developed as an improvement on SuperGlue.
*   **Architecture**: SuperGlue used ConvNets and Graph Neural Networks (GNNs), popular in 2018 <a class="yt-timestamp" data-t="01:09:05">[01:09:05]</a>. LightGlue leverages a [[Transformerbased model architectures | Transformer architecture]], reflecting more modern deep learning practices <a class="yt-timestamp" data-t="01:11:03">[01:11:03]</a>.
*   **Positional Encoding**: SuperGlue used an MLP to encode absolute point positions, fusing them early with descriptors <a class="yt-timestamp" data-t="01:20:35">[01:20:35]</a>. LightGlue's reliance on [[layerwise_scaling_in_transformer_architectures | relative positional encoding]] (RoPE) is a key distinction <a class="yt-timestamp" data-t="01:21:37">[01:21:37]</a>.
*   **Loss Supervision**: SuperGlue could only make predictions and be supervised at the final layer, leading to potential vanishing gradients <a class="yt-timestamp" data-t="01:23:22">[01:23:22]</a>. LightGlue's ability to predict and push gradients at each layer speeds up convergence <a class="yt-timestamp" data-t="01:23:45">[01:23:45]</a>.
*   **Matchability**: LightGlue disentangles similarity and matchability, which are more efficient to predict and yield cleaner gradients, unlike SuperGlue's "dustbin" mechanism <a class="yt-timestamp" data-t="01:22:15">[01:22:15]</a>.

## Training and Data
LightGlue employs fully supervised training, relying on ground truth labels <a class="yt-timestamp" data-t="01:17:54">[01:17:54]</a>.
*   **Synthetic Homographies**: The model is pre-trained with synthetic homographies generated from large datasets like MegaDepth (1 million images of landmarks) <a class="yt-timestamp" data-t="01:24:32">[01:24:32]</a>. This synthetic pre-training is crucial for generalization, especially since real-world landmark scenes can be distinctive and lead to overfitting <a class="yt-timestamp" data-t="01:25:31">[01:25:31]</a>.
*   **Feature Extraction**: LightGlue itself doesn't generate the feature points. It takes them as input, typically from algorithms like SuperPoint (a 2018 Magic Leap paper trained on synthetic data) or even traditional SIFT features <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>, <a class="yt-timestamp" data-t="01:27:20">[01:27:20]</a>.
*   **Hardware and Settings**: Training involved using 2K points per image, gradient checkpointing, and mixed precision on a single GPU with 24GB of VRAM (likely an RTX 3090) <a class="yt-timestamp" data-t="01:26:41">[01:26:41]</a>.

## Performance and Insights
LightGlue is generally considered a "drop-in replacement" for SuperGlue with clear benefits <a class="yt-timestamp" data-t="01:43:11">[01:43:11]</a>.
*   **Accuracy vs. Speed**: While LightGlue's accuracy is only marginally better than SuperGlue's (e.g., 0.1% improvement), its primary advantage lies in its speed, being roughly three to four times faster <a class="yt-timestamp" data-t="01:30:37">[01:30:37]</a>.
*   **Ablation Studies**:
    *   **Matchability Classifier**: Removing the pruning classifier leads to higher recall (finding more matches) but worse precision (more false positives), confirming its importance for discriminating good from bad matches <a class="yt-timestamp" data-t="01:31:47">[01:31:47]</a>.
    *   **Rotary Positional Encoding**: Using RoPE instead of absolute positional encodings provides a slight but consistent improvement in accuracy <a class="yt-timestamp" data-t="01:32:13">[01:32:13]</a>.
*   **Failure Cases**: LightGlue can struggle with repetitive objects in a scene (e.g., identical chairs or Coke bottles) where local feature descriptors might be too similar, leading to incorrect matches <a class="yt-timestamp" data-t="01:45:15">[01:45:15]</a>. This suggests a need for more global context in feature descriptors.

## Future Outlook
The current pipeline for applications like Gaussian Splats often involves multiple modular steps <a class="yt-timestamp" data-t="01:37:50">[01:37:50]</a>. While LightGlue improves one specific step (feature matching), an "end-to-end" approach that integrates feature extraction, matching, structure from motion, and splatting from video to 3D representation could be a significant future advancement <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. This would streamline complex [[applications_in_vision_transformers | computer vision pipelines]].