---
title: Comparison of contrastively pretrained vs classificationpretrained vision encoders
videoId: 446QYqELoIs
---

From: [[hu-po]] <br/> 

[[vision_language_models_and_encoders | Vision language models]] (VLMs) are a rapidly evolving field, combining visual and textual understanding. A key component of these models is the vision encoder, which processes image data. Recent research focuses on the optimal pretraining strategies for these encoders, primarily comparing classification-based pretraining with contrastive pretraining <a class="yt-timestamp" data-t="05:50:00">[00:05:50]</a>.

## Vision Encoders in VLMs

A [[vision_language_models_and_encoders | vision language model]] fundamentally combines some visual model (a vision encoder) and a large language model (LLM), with a mechanism to connect them <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. The vision encoder's role is to convert raw image data into a compressed numerical representation, often called an embedding or latent space <a class="yt-timestamp" data-t="01:55:48">[01:55:48]</a>. The choice and pretraining method of this vision encoder significantly impact the VLM's performance <a class="yt-timestamp" data-t="01:14:09">[01:14:09]</a>.

Common architectures for vision encoders include [[Vision Transformers vs Convolutional Networks | Vision Transformers (ViTs)]] and Convolutional Neural Networks (CNNs) like ResNets <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. ViTs are currently considered state-of-the-art for images and video <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

## Classification Pretraining

In classification pretraining, a vision encoder is trained on large datasets like ImageNet to classify images into predefined categories <a class="yt-timestamp" data-t="02:20:05">[02:20:05]</a>. This involves adding a "classification head" on top of the encoder and pushing gradients from a classification loss function through the network <a class="yt-timestamp" data-t="02:26:07">[02:26:07]</a>. After training, the classification head is removed, leaving an image encoder whose representations are highly effective for classification tasks <a class="yt-timestamp" data-t="02:27:39">[02:27:39]</a>.

## Contrastive Pretraining

[[Contrastive and reconstructive losses in vision encoders | Contrastive pretraining]] aims to learn representations by encouraging embeddings of matching pairs (e.g., an image and its corresponding text caption) to be close together, while pushing embeddings of unmatched pairs apart <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a>. Popular examples include CLIP (Contrastive Language-Image Pre-training) and SigLIP <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a> <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

### Loss Functions
*   **Softmax Loss**: A traditional approach that computes attention weights across images and text, often performing normalization independently across modalities <a class="yt-timestamp" data-t="01:37:41">[01:37:41]</a> <a class="yt-timestamp" data-t="01:21:26">[01:21:26]</a>.
*   **Sigmoid Loss (SigLIP)**: A newer approach that processes every image and text pair independently, turning the learning problem into a standard binary classification on all pair combinations (positive for matching, negative for others) <a class="yt-timestamp" data-t="01:43:08">[01:43:08]</a> <a class="yt-timestamp" data-t="01:48:47">[01:48:47]</a>. This method simultaneously allows for scaling up batch sizes and can be combined with [[Vision Transformer Encoders and PreTraining | locked image tuning]] <a class="yt-timestamp" data-t="01:25:22">[01:25:22]</a> <a class="yt-timestamp" data-t="01:27:26">[01:27:26]</a>.

[[Vision Transformer Encoders and PreTraining | Locked image tuning (LIT)]] is a technique where parts of the model (e.g., the vision encoder) are "frozen" during training, preventing gradients from flowing into them. This allows for training other parts of the model (like a connector MLP) faster and with lower compute budgets, while leveraging the pre-training of the frozen encoder <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a> <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>.

## Findings from Pali (Google DeepMind)

The *Pali* paper (by Google DeepMind and Google Research) conducted a direct [[comparison_of_different_vision_language_models | comparison of different vision language models]], specifically contrasting vision encoders pre-trained with classification objectives against those pre-trained with contrastive objectives <a class="yt-timestamp" data-t="01:50:56">[01:50:56]</a>.

Key findings:
*   **Superiority for VLMs**: [[Contrastive and reconstructive losses in vision encoders | Contrastively pre-trained vision encoders]] (like SigLIP-based ViTs) show superior performance across various multimodal benchmarks <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. They are particularly effective for visually situated text understanding and localization tasks <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a> <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **Classification Benchmarks**: While contrastive models might slightly underperform on standard image classification benchmarks (e.g., ImageNet), this doesn't indicate their overall quality for VLM tasks <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a> <a class="yt-timestamp" data-t="01:39:19">[01:39:19]</a>. A model worse on ImageNet classification can still be better for Visual Question Answering (VQA) <a class="yt-timestamp" data-t="01:39:45">[01:39:45]</a>.
*   **Efficiency**: [[Contrastive and reconstructive losses in vision encoders | Contrastively pre-trained models]] can lead to more efficient [[vision_language_models_and_encoders | Vision Language Models]] <a class="yt-timestamp" data-t="01:41:09">[01:41:09]</a>.

## Insights from Other Papers

### Comm (Huawei)
This paper, though retracted, investigated the effectiveness of different visual encoders for [[multimodal_large_language_models_vs_vision_language_models | Multimodal Large Language Models (MLLMs)]].
*   **Combining Encoders**: It explored [[combining_multiple_vision_encoders_for_improved_performance | combining multiple vision encoders]], specifically CLIP and DINOv2 <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.
*   **Multi-Level Features**: The paper also proposed using multi-level feature fusion, extracting features from intermediate layers of the vision encoders, as different layers capture different types of information (e.g., low-level details from shallow layers, global semantic information from CLIP, fine-grained pixel information from DINOv2) <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a> <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a> <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a> <a class="yt-timestamp" data-t="01:12:54">[01:12:54]</a>. While this combination showed slight improvements, the speaker questioned if the gains justified the increased complexity and inference cost <a class="yt-timestamp" data-t="01:26:50">[01:26:50]</a>.

### Deep Speed Visual Chat (Microsoft)
This work provided several observations from their training process:
*   **Better Visual Encoder**: Using a higher-resolution visual encoder, such as the one from *Qwen VL* (which uses fine-tuned *OpenCLIP*), significantly improves model quality <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a> <a class="yt-timestamp" data-t="00:59:52">[00:59:52]</a>.
*   **Scaling**: While not the primary focus, they acknowledge that [[pretraining_and_scaling_laws_for_vision_encoders | larger language models]] can offer superior quality <a class="yt-timestamp" data-t="01:45:09">[01:45:09]</a>. They also note a potential mismatch in efficiency when combining a very large LLM (e.g., Llama 2 70B) with a relatively small vision encoder (e.g., 2B parameters) <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a> <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>.
*   **Projection Layers**: They experimented with different projection layers (connectors) between the vision encoder and the language model, finding no significant benefits from using a complex Vision Transformer layer over a simple linear layer <a class="yt-timestamp" data-t="01:31:23">[01:31:23]</a>.

### Qwen VL (Alibaba)
*   **OpenCLIP as Base**: *Qwen VL* uses *OpenCLIP* (an open-source reimplementation of CLIP) as its vision encoder, specifically the ViT-BigG model <a class="yt-timestamp" data-t="00:48:33">[00:48:33]</a> <a class="yt-timestamp" data-t="00:49:07">[00:49:07]</a>.
*   **Complex Training Recipe**: *Qwen VL* employs a multi-stage training recipe, including initial pre-training where the language model is frozen and gradients are pushed into the vision encoder, followed by multitask pre-training where gradients are pushed into everything, and finally supervised fine-tuning where the vision encoder is frozen again <a class="yt-timestamp" data-t="01:52:16">[01:52:16]</a>.
*   **Cross-Attention Adapter**: Instead of a simple MLP connector, *Qwen VL* uses a single-layer cross-attention module as an "adapter" to compress image features <a class="yt-timestamp" data-t="01:53:59">[01:53:59]</a>.

## General Considerations

*   **Data Cleanliness**: As data sets grow, especially with synthetic or scraped internet data, noise and imperfection in data become a significant challenge <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.
*   **Data Augmentation**: While simple image augmentations (like flipping or rotating) are generally safe, more complex data blending methods for VLMs (e.g., shuffling images in conversations) can lead to deteriorated performance due to incorrect references <a class="yt-timestamp" data-t="01:32:50">[01:32:50]</a> <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
*   **Terminology Confusion**: The field currently suffers from a lack of standardized terminology, with different research groups using various acronyms like [[multimodal_large_language_models_vs_vision_language_models | MLMs]], [[vision_language_models_and_encoders | VLMs]], LMMs, and LVMs to describe similar model architectures <a class="yt-timestamp" data-t="01:55:04">[01:55:04]</a>.