---
title: Contrastive and reconstructive losses in vision encoders
videoId: viiB3JmK21M
---

From: [[hu-po]] <br/> 
This article discusses different pre-training approaches for [[Vision language models and encoders|vision encoders]], focusing on contrastive and reconstructive losses and their impact on the resulting features.

## Types of Vision Encoder Losses

[[Vision language models and encoders|Vision encoders]] can be trained using various methods, primarily categorized by the type of loss function used during pre-training. Two prominent categories are contrastive losses and reconstructive losses <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.

### Contrastive Loss

Contrastive losses aim to endow a [[Vision language models and encoders|vision encoder]] with semantic knowledge <a class="yt-timestamp" data-t="00:33:35">[00:33:35]</a>. This is achieved by feeding pairs of inputs to the model:
*   **Positive Examples**: Images or data that represent the same semantic concept are pulled closer together in the embedding space <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>. For instance, two different pictures of the same person would be considered positive examples <a class="yt-timestamp" data-t="00:34:22">[00:34:22]</a>.
*   **Negative Examples**: Images or data that represent different semantic concepts are pushed further apart in the embedding space <a class="yt-timestamp" data-t="00:35:06">[00:35:06]</a>. For example, pictures of different individuals would be negative examples <a class="yt-timestamp" data-t="00:35:06">[00:35:06]</a>.

The training process involves continually feeding these examples, contrasting similar items to be close and dissimilar items to be far apart <a class="yt-timestamp" data-t="00:35:28">[00:35:28]</a>. Models like [[Vision language models and encoders|CLIP]] (Contrastive Language–Image Pre-training) are trained with contrastive losses <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>.

### Reconstructive Loss

Reconstructive losses, in contrast, explicitly capture all parts of an image <a class="yt-timestamp" data-t="00:33:46">[00:33:46]</a>. This approach often involves an encoder-decoder setup <a class="yt-timestamp" data-t="00:35:57">[00:35:57]</a>. An image is encoded into a representation and then decoded back into an output, with a loss function (e.g., mean squared error) penalizing discrepancies between the original and reconstructed images at a pixel level <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.

Models like [[Vision language models and encoders|DINOv2]] (Self-supervised learning with Vision Transformers) use a form of reconstructive loss <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>.

### Comparison of Features

The choice of loss significantly impacts the nature of the visual features produced by the [[Vision language models and encoders|encoder]]:
*   **Contrastive Losses**: Provide semantic knowledge <a class="yt-timestamp" data-t="00:36:34">[00:36:34]</a>. Features from models like [[Vision language models and encoders|CLIP]] focus on high-level semantic concepts, resulting in high similarity scores for images that are semantically the same (e.g., different pictures of a pizza) <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>.
*   **Reconstructive Losses**: Result in more nuanced and low-level features <a class="yt-timestamp" data-t="00:37:47">[00:37:47]</a>. Models like [[Vision language models and encoders|DINOv2]] capture fine details, leading to lower similarity scores even for semantically similar images if their fine-grained visual details differ (e.g., pizza on different surfaces or with different toppings) <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.

## Application in Multimodal Models

In the context of [[Vision language models and encoders|multimodal large language models]] (MLLMs), the choice of [[Vision language models and encoders|vision encoder]] and its pre-training method is crucial <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

Apple's MM1 model, for example, uses a [[Vision Transformer Encoders and PreTraining|ViT]] pre-trained with a [[Comparison of contrastively pretrained vs classificationpretrained vision encoders|CLIP objective]] <a class="yt-timestamp" data-t="01:00:18">[01:00:18]</a>. This choice reflects a preference for semantic understanding in its [[Vision language models and encoders|vision encoder]].

While a single [[Vision language models and encoders|vision encoder]] is often used for simplicity and computational efficiency, especially for deployment on devices like iPhones <a class="yt-timestamp" data-t="01:48:40">[01:48:40]</a>, the open-source community has explored [[combining_multiple_vision_encoders_for_improved_performance|ensembles]] of [[Vision language models and encoders|image encoders]] <a class="yt-timestamp" data-t="00:38:40">[00:38:40]</a>. This approach involves feeding an image through multiple encoders (e.g., CLIP, SAM for segmentation, OCR-focused encoders), concatenating their respective tokens, and feeding them to the [[Vision language models and encoders|language model]] <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. This can lead to better results by leveraging different types of features, but at the cost of increased computational overhead and higher token counts, which impact the [[Pretraining and scaling laws for vision encoders|LLM's context length]] <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a>.