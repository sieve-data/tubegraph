---
title: Probing classifiers for understanding AI models
videoId: 3updXylOFvY
---

From: [[hu-po]] <br/> 

Probing classifiers are a methodology used in machine learning to investigate and understand the internal workings and representations learned by deep neural networks <a class="yt-timestamp" data-t="02:26:50">[02:26:50]</a>. This technique involves taking intermediate activations (the values of neurons at specific layers) from a neural network and [[training_and_finetuning_processes_for_ai_models | training]] a simpler model, such as a linear classifier or regressor, on these activations to predict certain properties <a class="yt-timestamp" data-t="02:51:39">[02:51:39]</a>. A high prediction accuracy indicates a strong correlation between the learned internal representation and the predicted property <a class="yt-timestamp" data-t="02:54:54">[02:54:54]</a>.

## What is a Pre-print?

The paper "Beyond surface statistics scene representation in a latent diffusion model" is a pre-print, meaning it has been publicly released on platforms like arXiv or social media but has not yet undergone or completed a formal academic peer-review process for journal publication <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. In machine learning, releasing pre-prints is common due to the rapid pace of research, especially from reputable institutions like Harvard <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.

## Why Probe AI Models?

Historically, computer vision relied on "feature engineering," where manual, interpretable features like SIFT or ORB were designed for tasks such as classification or tracking <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>. However, with the advent of deep learning and neural networks, this interpretability was largely lost <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>. It became difficult to understand exactly what internal features meant or how representations within a neural net contributed to its output <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>.

Probing models, as an [[selfimprovement_in_ai_models | interpretability research]] method, aims to dissect these complex systems to gain intuition and insights into their inner workings <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. It seeks to answer whether generative neural networks merely aggregate surface statistics or learn deeper "world models" <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>.

## How Probing Classifiers Work

Probing classifiers essentially "surgically cut" a neural network at a specific layer to examine its intermediate activations <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. A small, typically linear, model is then [[training_and_finetuning_processes_for_ai_models | trained]] on these activations to predict a desired property <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

### Types of Probes

*   **Binary Depth / Salient Object Detection**: For discrete properties like foreground/background distinction, a linear classifier is used. This classifier outputs pixel-level logits, which are then converted to probabilities (e.g., 0 or 1 for foreground/background) using a softmax function and a cross-entropy loss <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>, <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>.
*   **Continuous Depth**: For continuous properties like depth, a linear regressor is employed. This model directly outputs a numerical value for each pixel, [[training_and_finetuning_processes_for_ai_models | trained]] with a Huber loss to measure the difference from the ground truth depth map <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>.

### Baseline for Comparison

To ensure the found correlations are not spurious, probing performance on a [[pretraining_and_finetuning_in_ai_models | trained]] model is compared against a "randomized" baseline. This baseline uses the same network architecture but with randomly initialized, untrained weights <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. If the trained model significantly outperforms the randomized one, it suggests a genuine learned representation <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

## Application: Latent Diffusion Models (LDMs)

The paper applies probing to Stable Diffusion V1, an [[open_source_vs_proprietary_ai_models | open-source]] text-to-image [[foundation_models_in_ai | diffusion model]] <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. Stable Diffusion is a two-stage generative framework consisting of:
1.  **Latent Diffusion Model (LDM)**: Predicts noise to remove it during the image generation process <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. This model operates in a [[foundation_models_in_ai | latent space]] <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.
2.  **Variational Autoencoder (VAE)**: Compresses RGB images into a lower-dimensional [[foundation_models_in_ai | latent space]] (via an encoder) and reconstructs images from that space (via a decoder) <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. The use of [[foundation_models_in_ai | latent space]] reduces compute and memory requirements for diffusion <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

LDMs, even when [[training_and_finetuning_processes_for_ai_models | trained]] purely on images without explicit depth information, consistently produce images with coherent 3D scenes <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. The research investigates whether these models create and utilize an internal representation of simple scene geometry, specifically 3D depth and salient object/background distinction <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

### Data Generation

A synthetic dataset of 1,000 images was generated using a [[pretraining_and_finetuning_in_ai_models | pre-trained]] Stable Diffusion model, with prompts sampled from the LAION Aesthetics V2 dataset <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. Ground truth labels for depth and salient objects were obtained using existing [[pretraining_and_finetuning_in_ai_models | pre-trained]] models like Midas for monocular depth estimation and Tracer for salient object tracing <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

## Key Findings

### Early Emergence of Depth and Saliency
The most surprising finding is that internal representations of 3D depth and salient object/background distinction appear "surprisingly early in the denoising process" <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>. Even when the images appear as complete noise to a human observer, the LDM's internal representations already encode information about foreground/background and depth <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>, <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. This suggests that the model is making high-level semantic decisions about scene composition very early on, possibly to allow more steps for fine-grained texture generation <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>, <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

### LDM vs. VAE for Depth Representation
Crucially, the LDM, not the VAE, is responsible for building this early depth representation <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.
*   **LDM**: Probing the LDM's internal representations reveals strong depth and saliency information even in the early denoising steps <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **VAE**: The VAE's internal representations, when processing corrupted (noisy) latents from early denoising steps, show very poor depth and saliency information <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. Only when the latent is nearly fully denoised and the image is perceptible does the VAE's internal representation show strong depth <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

### Vision Transformers (ViTs) vs. Convolutional Neural Networks (CNNs)
The study also found that Vision Transformers (ViTs), which are part of the LDM architecture, exhibit stronger depth and saliency representations in their self-attention layers compared to convolutional layers in CNNs <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. ViTs generally outperformed CNNs in depth estimation tasks <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.

### Bottleneck Layer Anomaly
Interestingly, the bottleneck layer within the LDM, despite having a high number of feature dimensions, shows a dip in its ability to predict depth accurately compared to layers just before and after it <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>, <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. This is attributed to its extremely small spatial resolution (e.g., 8x8 pixels), which makes it difficult to infer fine-grained depth accurately even with more channels <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

## Causal Role and Intervention Experiments

While probing establishes correlation, intervention experiments demonstrate a causal link <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. Researchers designed experiments to modify the LDM's internal representations directly and measure the effects on its output images <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

The process involves:
1.  Generating an image and obtaining its predicted salient object mask or depth map from a probing classifier.
2.  Manually modifying this predicted label (e.g., by shifting the foreground object's position).
3.  Calculating the gradient of the loss between the probing classifier's output and the *modified* label, with respect to the LDM's internal representation <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
4.  Adjusting the LDM's internal representation in the direction of this gradient <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.
5.  Allowing the denoising process to continue with this modified internal representation <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

The results show that by intervening early in the denoising process and shifting the internal representation of a salient object, the final generated image also shows the object repositioned <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. This demonstrates that these internal representations play a causal role in image synthesis <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>. This technique bears a strong resemblance to ControlNet, which conditions diffusion models on external inputs like edge maps or poses to control image generation <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.

## Significance and Future Work

The findings add nuance to the debate on whether [[taskspecific_vs_general_ai_models | generative models]] learn more than just [[the_significance_of_longcontext_processing_in_ai_models | surface statistics]] <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. The evidence suggests that Stable Diffusion, despite being [[training_and_finetuning_processes_for_ai_models | trained]] solely on 2D images, develops an internal linear representation of scene geometry, including salient object distinction and relative depth <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. This means the model has "discovered" a semantic hierarchy of the real world, understanding concepts like objects and their depth relationships <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

Future research avenues include:
*   Looking for representations of other scene attributes like lighting or texture <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   Investigating models of semantic aspects of a scene, such as sentiment <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>, similar to how [[meta_ai_research | language models]] have been found to recapitulate NLP pipelines <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

This [[selfimprovement_in_ai_models | interpretability research]] provides valuable intuition into the "black box" nature of neural networks, demonstrating that complex models can learn abstract, meaningful representations of the world <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.