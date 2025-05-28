---
title: Selfsupervised learning for images
videoId: MVWYTFs9M-s
---

From: [[hu-po]] <br/> 

Self-supervised learning (SSL) in computer vision is an approach to representation learning where the system learns relationships between its inputs without explicit human-provided labels <a class="yt-timestamp" data-t="08:40:40">[08:40:40]</a>. This contrasts with supervised learning, which requires a target (like a class or bounding box) for every input image <a class="yt-timestamp" data-t="08:43:55">[08:43:55]</a>. SSL often involves a masked task where a piece of an image is cut out, and the model tries to reconstruct the missing piece <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

## Semantic Image Representations

A key goal in image-based SSL is to learn "highly semantic image representations" <a class="yt-timestamp" data-t="06:54:15">[06:54:15]</a>. These representations, also called embeddings, are vectors of numbers that represent an image <a class="yt-timestamp" data-t="06:58:34">[06:58:34]</a>. "Highly semantic" means these embeddings are forced to represent the content of an image, rather than its texture, color, or visual appearance <a class="yt-timestamp" data-t="07:07:08">[07:07:08]</a>. The model's capacity should focus entirely on high-level semantics, not pixel-level details like exact colors or edge definitions <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.

## I-JEPA: Joint Embedding Predictive Architecture

The "Image-based Joint Embedding Predictive Architecture" (I-JEPA) is a non-generative approach for [[Unsupervised Learning in Computer Vision | self-supervised learning]] from images <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>. Developed by Meta AI, Mila, McGill, and New York University, it demonstrates an approach for learning highly semantic image representations without relying on handcrafted data augmentation <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>, <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>.

### Core Idea and Mechanism
The simple idea behind I-JEPA is to predict the representations of various target blocks within an image, given a single context block from the same image <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>. This is achieved by predicting missing information in an abstract representation space <a class="yt-timestamp" data-t="25:58:50">[25:58:50]</a>.

### Architecture
I-JEPA utilizes three main components, all based on the Vision Transformer (ViT) architecture <a class="yt-timestamp" data-t="55:16">[55:16]</a>:
*   **Context Encoder (F_Theta):** Processes the visible, unmasked portion of the image (context block) to produce its representation <a class="yt-timestamp" data-t="01:00:01">[01:00:01]</a>.
*   **Target Encoder (F_Theta_bar):** Processes the target blocks (masked out portions) to produce their true representations <a class="yt-timestamp" data-t="00:54:06">[00:54:06]</a>. Its weights are updated via an exponential moving average (EMA) of the context encoder's weights, linking the two <a class="yt-timestamp" data-t="01:17:56">[01:17:56]</a>. This EMA acts as a form of regularization <a class="yt-timestamp" data-t="01:18:33">[01:18:33]</a>.
*   **Predictor (G_Phi):** Takes the context encoder's output and, conditioned on positional tokens, predicts the representations of the target blocks <a class="yt-timestamp" data-t="01:00:34">[01:00:34]</a>, <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.

### Loss Function
I-JEPA uses a simple L2 loss (mean squared error) between the predicted target block representations and the actual representations from the target encoder <a class="yt-timestamp" data-t="01:16:26">[01:16:26]</a>. This means the loss is computed in representation space, not pixel space, which is a key difference from generative models that reconstruct images directly <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>, <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

### Masking Strategy
A crucial design choice is the masking strategy <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>. I-JEPA uses a "multi-block masking strategy" where four possibly overlapping blocks are randomly sampled from the image to serve as targets <a class="yt-timestamp" data-t="01:06:36">[01:06:36]</a>, <a class="yt-timestamp" data-t="02:00:11">[02:00:11]</a>. The scale and aspect ratio of these blocks are also randomized within specified ranges <a class="yt-timestamp" data-t="01:07:32">[01:07:32]</a>.

## Advantages and Performance

*   **Computational Efficiency:** I-JEPA converges faster and requires less compute than pixel reconstruction methods like Masked Autoencoders (MAE) <a class="yt-timestamp" data-t="01:55:59">[01:55:59]</a>. This is because predicting in representation space is significantly less computationally intensive than predicting in high-dimensional pixel space <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. The avoidance of handcrafted data augmentation further contributes to faster training times <a class="yt-timestamp" data-t="01:28:07">[01:28:07]</a>.
*   **Semantic Representations:** The method yields high-level semantic representations, making it effective for tasks like classification, object counting, and depth prediction <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
*   **Reduced Bias:** By not relying on handcrafted data augmentations, I-JEPA avoids introducing strong biases that could be detrimental to certain downstream tasks or different data distributions <a class="yt-timestamp" data-t="01:18:16">[01:18:16]</a>. This allows for generalization to a wider set of tasks <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   **Performance:** I-JEPA achieves strong performance on ImageNet 1K linear evaluation and semi-supervised tasks, often outperforming or matching other state-of-the-art methods while using less pre-training epochs <a class="yt-timestamp" data-t="01:26:30">[01:26:30]</a>, <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

## Related Concepts

### Model Ensembling
The concept of using multiple models to improve final performance is called model ensembling or a mixture model <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. For example, GPT-4 is reported to be an ensemble of eight models, each with approximately 220 billion parameters, likely fine-tuned on slightly different data <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. This strategy is popular in Kaggle competitions to "squeeze out that very last one or two percent" of performance <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. Similarly, OpenAI's Codex paper from 2021 describes generating 100 samples per token and then filtering them down, which is a form of ensembling <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.

### Energy-Based Models (EBMs)
[[Selfimprovement in AI models | Self-supervised learning]] can be framed using Energy-Based Models (EBMs), where the objective is to assign high energy (large scalar value) to incompatible inputs and low energy (low scalar value) to compatible inputs <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. In this context, "energy" can be thought of as the distance between representations in a latent space <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.

### Generative vs. Joint Embedding Architectures
*   **Joint Embedding Architectures:** Learn to output similar embeddings for compatible inputs (e.g., different augmented views of the same image) and distant embeddings for incompatible inputs <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>, <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **Generative Architectures:** Learn to directly reconstruct a signal (e.g., an image) from a compatible input using a decoder network <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>, <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>. The loss here is in the input (pixel) space <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. This approach is computationally more expensive due to the need for a decoder and pixel-level loss <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

### Representation Collapse
A challenge in [[Deep Learning Approaches in Image Correspondence | joint embedding architectures]] is "representation collapse," where the encoder produces a constant output regardless of the input <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. This can be mitigated by techniques like contrastive losses, non-contrastive losses that minimize informational redundancy, clustering-based approaches, or using an asymmetric architectural design between encoders <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>, <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

### Vision Transformer (ViT)
A Vision Transformer (ViT) is a type of Transformer model used as a vision encoder. It breaks an image into small chunks (patches), treats them as a sequence (like words in a sentence), and feeds them into a Transformer, which then applies standard attention blocks <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. Each patch effectively becomes a "token" <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

### ImageNet
ImageNet is a large dataset of images, often used as a benchmark for image classification tasks <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. For example, ImageNet 1K contains 1000 classes like "dog," "cat," and "chair" <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. It's used to evaluate [[promptbased_learning_and_segmentation | zero-shot transfer learning]] and the performance of pre-trained models on new tasks <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.

## Conclusion
I-JEPA represents a step towards simpler, more efficient [[foundation_models_in_computer_vision | self-supervised learning]] for images. Its approach of predicting in representation space, combined with a multi-block masking strategy and avoiding handcrafted data augmentation, leads to faster training and the generation of highly semantic image embeddings that perform well on various downstream tasks <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. While the model shows some sensitivity to hyper-parameters like block size and scale <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>, its overall simplicity and efficiency are significant advantages <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.