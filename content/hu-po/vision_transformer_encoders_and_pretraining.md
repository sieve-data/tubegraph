---
title: Vision Transformer Encoders and PreTraining
videoId: JdfrG89iPOA
---

From: [[hu-po]] <br/> 

Vision Transformer (ViT) encoders play a crucial role in modern computer vision tasks, particularly in 3D scene reconstruction. These models leverage [[pretraining_and_scaling_laws_for_vision_encoders | pre-trained Transformers]] to process image data efficiently and effectively <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>.

## Vision Transformer (ViT) Overview
A [[vision_transformers_and_their_applications | Vision Transformer]] operates as a sequence-to-sequence model <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>. To process a two-dimensional image, the image is "patch-ified," meaning it is cut into small patches <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. These patches are then fed into the ViT encoder as a sequence, similar to reading a sentence from left to right, top to bottom <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a>. The encoder then produces "token representations," which are vector representations of the image <a class="yt-timestamp" data-t="00:42:15">[00:42:15]</a>.

In the Duster architecture, two views of a scene (Image 1 and Image 2) are first encoded in a "siamese manner" using a shared ViT encoder <a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>. This means both images pass through identical encoder pathways <a class="yt-timestamp" data-t="00:47:12">[00:47:12]</a>. The resulting token representations are then passed to two Transformer decoders that exchange information through cross-attention mechanisms <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>.

### Patching in Vision Transformers
The size of these patches is a configurable parameter. For instance, the ViT base model discussed uses a patch size of 16 <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>. The ViT model comes in different sizes, such as "small," "large," and "base," with "base" typically being the medium size <a class="yt-timestamp" data-t="00:51:11">[00:51:11]</a>.

## Pre-training for Vision Transformers
The effectiveness of ViT encoders, particularly in tasks like 3D vision, heavily relies on [[pretraining_and_scaling_laws_for_vision_encoders | pre-training]] <a class="yt-timestamp" data-t="00:33:06">[00:33:06]</a>. [[pretraining_and_scaling_laws_for_vision_encoders | Pre-trained models]] allow for leveraging vast amounts of information from large datasets <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>.

### KOCO Pre-training Method
Duster specifically utilizes ViT encoders pre-trained with the KOCO method <a class="yt-timestamp" data-t="00:47:09">[00:47:09]</a> <a class="yt-timestamp" data-t="01:48:07">[01:48:07]</a>. KOCO, or "Cross-View Completion," is a self-supervised [[pretraining_and_scaling_laws_for_vision_encoders | pre-training]] paradigm for 3D Vision tasks <a class="yt-timestamp" data-t="00:47:33">[00:47:33]</a>.

The core idea of KOCO is "masked image modeling" <a class="yt-timestamp" data-t="00:47:58">[00:47:58]</a>. This involves masking (hiding) patches in an input image, and then a neural network predicts the masked content using only the visible patches <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>. For 3D Vision tasks, KOCO extends this by using pairs of images showing the same scene from different viewpoints <a class="yt-timestamp" data-t="00:48:09">[00:48:09]</a>.

For example, given two views of a building, one view might be masked, and the model attempts to reconstruct the masked parts while also having access to the second, unmasked "reference view" <a class="yt-timestamp" data-t="00:48:23">[00:48:23]</a> <a class="yt-timestamp" data-t="00:48:46">[00:48:46]</a>. Since the two views are slightly different, the task is more challenging and forces the model to learn high-level semantic understanding <a class="yt-timestamp" data-t="00:49:07">[00:49:07]</a> <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a>. This high-level semantic notion allows the model to predict details that are consistent across different viewpoints <a class="yt-timestamp" data-t="00:49:32">[00:49:32]</a>.

### Pre-training Datasets
The quality of a deep learning model is highly dependent on the dataset it is trained on <a class="yt-timestamp" data-t="00:50:35">[00:50:35]</a>. KOCO uses synthetic image pairs derived from several 3D indoor scene datasets, including:
*   Scannet <a class="yt-timestamp" data-t="00:51:33">[00:51:33]</a>
*   Replica <a class="yt-timestamp" data-t="00:51:35">[00:51:35]</a>
*   ReplicaCAD <a class="yt-timestamp" data-t="00:51:35">[00:51:35]</a>
*   HM3D <a class="yt-timestamp" data-t="00:51:37">[00:51:37]</a>

These datasets are synthetically rendered within the Habitat simulator, a simulation environment created by Facebook (Meta) <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a> <a class="yt-timestamp" data-t="00:52:05">[00:52:05]</a>. The Habitat simulator allows for easy generation of millions of paired images (approximately 2 million pairs) of the same scene from slightly different viewpoints, providing the necessary data for [[pretraining_and_scaling_laws_for_vision_encoders | pre-training]] <a class="yt-timestamp" data-t="00:51:44">[00:51:44]</a> <a class="yt-timestamp" data-t="00:52:47">[00:52:47]</a>.

## Benefits of Pre-trained ViTs in Duster
By leveraging powerful [[pretraining_and_scaling_laws_for_vision_encoders | pre-training]] techniques, Duster's generic architecture, which does not explicitly force any geometrical constraints, can surpass existing task-specific architectures <a class="yt-timestamp" data-t="00:54:34">[00:54:34]</a>. This approach aligns with the "bitter lesson" in deep learning, advocating for large datasets and simpler models over heavily engineered, constrained systems <a class="yt-timestamp" data-t="00:55:02">[00:55:02]</a>. The [[new_techniques_in_vision_encoder_integration | Vision Transformer encoder]] learns intricate features directly from the data without relying on human-defined geometric priors <a class="yt-timestamp" data-t="00:55:52">[00:55:52]</a>.