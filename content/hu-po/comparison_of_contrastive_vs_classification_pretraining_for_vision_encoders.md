---
title: Comparison of contrastive vs classification pretraining for vision encoders
videoId: 446QYqELoIs
---

From: [[hu-po]] <br/> 

Vision encoders are models specifically designed for processing images and videos. They are model architectures similar to ConvNets or ResNets, but [[Pretrained Vision Transformers and KOCO | Vision Transformers]] are currently considered state-of-the-art for images and video tasks [00:06:04]<a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. These encoders convert raw image data into a more compressed representation, often called an embedding or latent space [00:15:37]<a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. The choice of pretraining objective for these [[Challenges in visual segmentation and encoding | vision encoders]] significantly impacts their downstream performance, particularly in [[Vision language models with pretrained components | Vision Language Models]] (VLMs) [01:41:55]<a class="yt-timestamp" data-t="01:41:55">[01:41:55]</a>.

## Classification Pretraining

Classification pretraining is a traditional method for training [[Challenges in visual segmentation and encoding | image encoders]] [02:20:05]<a class="yt-timestamp" data-t="02:20:05">[02:20:05]</a>. It typically involves training a model, such as a VGG or ResNet 101, on a large-scale image classification dataset like ImageNet [02:07:07]<a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>.

The process involves:
*   Adding a classification head on top of the base model [02:26:00]<a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
*   Pushing gradients through a classification loss function across the entire dataset for many epochs [02:27:00]<a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.
*   Once training is complete, the classification head is removed, and the remaining model serves as an [[Challenges in visual segmentation and encoding | image encoder]] [02:37:00]<a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

The representations learned by these encoders are highly optimized for classification tasks [02:47:00]<a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

## Contrastive Pretraining

Contrastive pretraining encourages the embeddings of matching data pairs to align, while pushing embeddings of unmatched pairs apart [01:03:04]<a class="yt-timestamp" data-t="01:03:04">[01:03:04]</a>. In the context of [[Vision language models with pretrained components | vision language models]], this involves pairing images with their corresponding text captions [01:25:00]<a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.

Key aspects of contrastive pretraining:
*   **Objective**: To pull semantically similar items (e.g., an image of a dog and the text "dog") closer together in the representation space, and push dissimilar items (e.g., an image of a dog and the text "cat") further apart [00:15:17]<a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   **Data Pairs**: Models are trained on image-text pairs (e.g., an image and its caption) [00:13:22]<a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
*   **Loss Functions**: Common loss functions include softmax-based contrastive loss and sigmoid-based loss (SigLIP) [01:14:00]<a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. SigLIP, for example, processes each image and text pair independently, turning the problem into a binary classification task for matching and non-matching pairs [01:46:00]<a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.
*   **Noise**: The assumption that a randomly sampled text from a different image is unrelated can introduce noise, but deep learning models often work effectively despite this [01:57:00]<a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
*   **[[Pretraining scaling laws for vision encoders | Locked Image Tuning]]**: A technique used to leverage [[Pretrained Vision Transformers and KOCO | pretrained vision encoders]] and text encoders without overwriting their initial pretraining, often involving freezing one encoder while training the other [01:56:00]<a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

## Comparison and Performance

The Pali-3 paper, developed by Google DeepMind and Google Research, focused on directly [[Comparison of vision architectures | comparing]] classification-pretrained [[Pretrained Vision Transformers and KOCO | Vision Transformers]] with contrastively pretrained ones for [[Vision language models with pretrained components | Vision Language Models]] (VLMs) [03:05:00]<a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>.

Key findings from Pali-3:
*   **General Performance**: Contrastively pretrained models (like SigLIP-based Pali-3) showed superior performance across various multimodal benchmarks [00:07:00]<a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Specific Tasks**: They were particularly effective for visually situated text understanding and localization tasks [00:07:00]<a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a> and also for video benchmarks, even without specific video data pretraining [03:43:00]<a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.
*   **Efficiency**: Contrastively trained models were found to lead to better and more efficient [[Vision language models with pretrained components | Vision Language Models]] [01:41:00]<a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **ImageNet Performance**: While classification-pretrained models naturally excelled at ImageNet classification, this performance did not necessarily translate to better VLM performance [01:38:52]<a class="yt-timestamp" data-t="01:38:52">[01:38:52]</a>. For instance, a contrastively trained model might have worse ImageNet accuracy but still outperform classification-trained models on VQA tasks [01:39:45]<a class="yt-timestamp" data-t="01:39:45">[01:39:45]</a>. This suggests that ImageNet classification performance is not a reliable indicator of a [[Challenges in visual segmentation and encoding | vision encoder's]] quality for VQA [01:39:19]<a class="yt-timestamp" data-t="01:39:19">[01:39:19]</a>.

## Conclusion

The evidence from the Pali-3 paper strongly suggests that contrastively pretrained [[Challenges in visual segmentation and encoding | vision encoders]] are generally superior for developing [[Vision language models with pretrained components | Vision Language Models]] compared to those pretrained with classification objectives [01:41:55]<a class="yt-timestamp" data-t="01:41:55">[01:41:55]</a>. This is especially true for tasks requiring visual grounding, localization, and visually situated text understanding.