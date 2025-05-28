---
title: Pretrained Vision Transformers and KOCO
videoId: JdfrG89iPOA
---

From: [[hu-po]] <br/> 

[[vision_transformers_and_their_efficiency | Vision Transformers]] (ViT) are a type of [[applications_in_vision_transformers | Transformer model]] designed for [[computer_vision deep dive | computer vision]] tasks <a class="yt-timestamp" data-t="00:41:29">[00:41:29]</a>. As a sequence-to-sequence model, a ViT processes two-dimensional images by first converting them into a sequence of patches <a class="yt-timestamp" data-t="00:41:33">[00:41:33]</a>. These patches are then fed into the model from left to right, top to bottom, similar to how a sentence is read <a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>.

## The Role of Pre-training

Pre-training is a crucial step for [[Vision Transformers and their efficiency | Vision Transformers]] as it allows models to leverage vast amounts of information from large datasets <a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>. This approach enables the model to learn high-level semantic understanding of images <a class="yt-timestamp" data-t="00:49:16">[00:49:16]</a>, acting as a "prior influenced by high-level semantics" <a class="yt-timestamp" data-t="00:49:18">[00:49:18]</a>.

## KOCO: Self-Supervised Pre-training

KOCO (Cross-view Completion) is a self-supervised pre-training paradigm specifically for 3D [[computer_vision deep dive | vision tasks]] <a class="yt-timestamp" data-t="00:47:33">[00:47:33]</a>. It was released on January 12, 2023 <a class="yt-timestamp" data-t="00:47:29">[00:47:29]</a>.

### Methodology

KOCO utilizes a masked image modeling pre-training approach <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>:
*   **Masking**: Patches in an input image are masked (zeroed out) <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>.
*   **Prediction**: The neural network then predicts the masked content using only the visible patches as input <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.
*   **Cross-View Completion**: The model starts with pairs of images showing the same scene from different viewpoints <a class="yt-timestamp" data-t="00:48:09">[00:48:09]</a>. This reference view aids in predicting the masked patches <a class="yt-timestamp" data-t="00:48:46">[00:48:46]</a>, even if the appearance changes due to different angles or lighting <a class="yt-timestamp" data-t="00:49:05">[00:49:05]</a>. This process teaches the model to build a high-level semantic notion of objects in the scene <a class="yt-timestamp" data-t="00:49:37">[00:49:37]</a>.

### Data for Pre-training

The quality of deep learning models often depends on the dataset they are trained on <a class="yt-timestamp" data-t="00:50:35">[00:50:35]</a>. KOCO is implemented in PyTorch using a ViT-Base-16 architecture <a class="yt-timestamp" data-t="00:50:56">[00:50:56]</a>. Its pre-training dataset consists of approximately two million synthetic image pairs <a class="yt-timestamp" data-t="00:51:44">[00:51:44]</a> derived from 3D indoor scenes from datasets such as Scannet, Replica, ReplicaCAD, and HM3D <a class="yt-timestamp" data-t="00:51:30">[00:51:30]</a>. These images are synthetically rendered in the Habitat simulator <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>, a simulation environment created by Meta (Facebook) for embodied research <a class="yt-timestamp" data-t="00:52:07">[00:52:07]</a>. This simulator allows for easy generation of image pairs from slightly different viewpoints with known camera information <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>.

## Integration in Duster

Duster, a novel approach for unconstrained 3D reconstruction, leverages KOCO's pre-trained [[vision_language_models_with_pretrained_components | Vision Transformer encoders]] <a class="yt-timestamp" data-t="00:53:29">[00:53:29]</a>. These encoders process two image views <a class="yt-timestamp" data-t="00:56:07">[00:56:07]</a> and feed into decoders that utilize cross-attention to produce point maps and associated confidence maps <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>.

### Advantages in Duster

By utilizing pre-trained models like KOCO, Duster benefits in several ways:
*   **Reduced Reliance on Geometric Constraints**: Duster's architecture does not explicitly force any geometrical constraints or inductive biases <a class="yt-timestamp" data-t="00:54:48">[00:54:48]</a>, a departure from traditional [[comparison_of_vision_architectures | computer vision pipelines]] like COLMAP <a class="yt-timestamp" data-t="00:55:56">[00:55:56]</a>. This allows the model to learn the optimal structure and features directly from the data <a class="yt-timestamp" data-t="00:55:37">[00:55:37]</a>.
*   **Simplicity and Speed**: Duster is a simpler, more efficient, and faster solution compared to older methods <a class="yt-timestamp" data-t="00:36:49">[00:36:49]</a>. It eliminates complex chains of sub-problems that introduce noise and complexity <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.
*   **State-of-the-Art Performance**: Duster achieves state-of-the-art results across various [[computer_vision deep dive | 3D Vision tasks]] <a class="yt-timestamp" data-t="01:01:38">[01:01:38]</a>, including monocular depth estimation, multi-view pose estimation, and 3D reconstruction <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>. It can perform these tasks without prior information about camera calibration or viewpoint poses <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>.

For example, Duster can generate a 3D reconstruction from a set of images in approximately 15 seconds <a class="yt-timestamp" data-t="01:50:05">[01:50:05]</a>, even if images have varying orientations (vertical/horizontal) or lighting conditions <a class="yt-timestamp" data-t="01:50:12">[01:50:12]</a>. Its effectiveness is particularly notable in indoor scenes due to its pre-training on the AI Habitat dataset <a class="yt-timestamp" data-t="01:00:50">[01:00:50]</a>.