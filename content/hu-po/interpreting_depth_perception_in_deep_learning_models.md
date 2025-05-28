---
title: Interpreting depth perception in deep learning models
videoId: 3updXylOFvY
---

From: [[hu-po]] <br/> 

This article reviews the paper "Beyond Surface Statistics: Scene Representation in a Latent Diffusion Model," which investigates the internal workings of [[Deep Learning and Neural Networks | deep learning]] models, specifically latent diffusion models (LDMs), concerning their ability to represent scene geometry or depth <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The research explores whether LDMs, even when trained without explicit depth information, develop and utilize an internal understanding of 3D scene geometry <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Paper Context: Pre-print Status
The reviewed paper is a pre-print, meaning it has been publicly released on platforms like arXiv but has not yet undergone or completed a formal academic peer-review process for publication in a journal <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. While this might typically raise alarms about unvetted claims, it is a common practice in the rapidly evolving field of machine learning, where research moves quickly <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## The Core Question: Beyond Surface Statistics
A central question in [[Deep Learning and Neural Networks | deep learning]] interpretability is whether generative networks merely memorize superficial correlations between data features (like pixel values and words) or learn deeper, underlying models of the world, such as an implicit understanding of objects and [[Highdimensional spaces and information storage in neural nets | hierarchical breakdowns of reality]] <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. This paper aims to "dissect a latent diffusion model and kind of probe at it and see what's going on inside" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>, fitting into a broader line of interpretability research <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### What is a Depth Image?
A depth image is a single-channel image (not RGB) where each pixel's value represents its distance from the camera <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Often, these are recolored for human readability, but fundamentally, they encode spatial depth information <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Interpretability Challenges
Historically, [[Computer vision deep dive | computer vision]] relied on [[Patchbased depth prediction techniques | feature engineering]], where features like SIFT or ORB were manually designed and entirely understandable <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. However, the advent of the [[Deep Learning and Neural Networks | deep learning]] paradigm and [[Deep Learning and Neural Networks | neural networks]] led to a loss of this direct interpretability, making it difficult to understand what internal representations mean <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

## Methodology: Linear Probing
To investigate the internal representations, the researchers employed linear probing <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This involves surgically "cutting" into a [[Deep Learning and Neural Networks | neural network]] at an intermediate layer and training a simple linear classifier or regressor on its activations (internal representations) <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>. A high prediction accuracy from this probe indicates a strong correlation between the learned representation and the property being predicted (e.g., depth) <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.

To ensure the findings were not due to spurious correlations or the model's enormous feature space, a controlled experiment was conducted. Probing classifiers were also trained on a randomized, untrained version of the LDM <a class="yt-timestamp" data-t="00:31:41">[00:31:41]</a>. Significantly worse performance from the randomized model confirmed that the detected representations were indeed learned by the trained LDM <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>.

### Types of Depth Representations Probed
The study investigated two types of depth representations:
*   **Discrete Binary Depth:** This categorizes pixels into foreground and background, formulated as a salient object detection task <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>.
*   **Continuous Depth:** This provides a more fine-grained, continuous distance value for each pixel, akin to a [[Monocular depth estimation and its challenges | monocular depth estimation]] map <a class="yt-timestamp" data-t="00:35:42">[00:35:42]</a>.

### [[Synthetic data for training depth estimation models | Synthetic Data for Training Depth Estimation Models]]
A dataset of 1,000 synthetic images was generated using a pre-trained Stable Diffusion V1 model <a class="yt-timestamp" data-t="00:41:42">[00:41:42]</a>. Prompts were sampled from the LAION Aesthetics V2 dataset. Ground truth labels for salient object detection were synthesized using the Tracer model, and relative inverse depth maps were estimated using the Midas model <a class="yt-timestamp" data-t="00:43:53">[00:43:53]</a>. Problematic images, including offensive content, corrupted objects, or those without clear depth concepts (e.g., black and white comic art), were manually filtered out <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>. The final dataset comprised 617 samples <a class="yt-timestamp" data-t="00:45:47">[00:45:47]</a>.

## Key Findings: Early Emergence of Depth
A surprising finding was the dramatic increase in probing performance for both salient object detection and continuous depth estimation during the *first five denoising steps* <a class="yt-timestamp" data-t="01:10:19">[01:10:19]</a>. This means that even when the decoded image still appears largely noisy to a human viewer, the LDM's internal representations are already encoding robust depth and foreground/background information <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a>.

For instance, conventional [[Monocular depth estimation and its challenges | monocular depth estimation]] models like Midas failed to detect significant structure in these early, noisy images <a class="yt-timestamp" data-t="01:11:03">[01:11:03]</a>. However, the simple linear probes applied to the LDM's internal states successfully predicted these properties <a class="yt-timestamp" data-t="01:11:34">[01:11:34]</a>.

### LDM vs. VAE: Where is Depth Encoded?
The study also compared the depth representations in the LDM versus the Variational Autoencoder (VAE) component <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>.
*   The VAE's internal representations showed weak depth information and struggled to decode salient objects from corrupted latents in early steps <a class="yt-timestamp" data-t="01:13:03">[01:13:03]</a>. Its performance only improved significantly when the latents were nearly fully denoised <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>.
*   Conversely, the LDM itself encodes a much stronger representation of depth, particularly in the early denoising stages <a class="yt-timestamp" data-t="01:13:30">[01:13:30]</a>. This indicates that the LDM's internal processes, rather than just relying on depth encoded by the VAE for reconstruction, actively develop this understanding during the denoising process <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>.

### Vision Transformers (ViT) vs. Convolutional Neural Networks (CNN)
As a side study, the researchers found that [[Recurrent depth approach in AI and its advantages over Transformers | Vision Transformers]] (ViTs) generally produced stronger depth representations in their self-attention layers compared to convolutional layers in CNNs <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. ViTs maintained a much better internal representation for depth even in the final layers of the decoder compared to CNNs <a class="yt-timestamp" data-t="01:44:24">[01:44:24]</a>.

## Causal Role of Depth Representation
To establish a causal link, the researchers performed intervention experiments <a class="yt-timestamp" data-t="01:19:59">[01:19:59]</a>. They aimed to change the LDM's output image by solely modifying its internal depth representations <a class="yt-timestamp" data-t="01:20:25">[01:20:25]</a>.
*   They identified the foreground object using the probing classifier <a class="yt-timestamp" data-t="01:21:08">[01:21:08]</a>.
*   They then translated (shifted) its representation in 2D space <a class="yt-timestamp" data-t="01:21:09">[01:21:09]</a>.
*   The LDM's internal representation was updated using gradients from the probing classifier, effectively "pushing" the representation towards the desired shifted position <a class="yt-timestamp" data-t="01:22:09">[01:22:09]</a>.
*   By modifying these internal activations, the final generated images showed the foreground object repositioned accordingly <a class="yt-timestamp" data-t="01:26:38">[01:26:38]</a>.

This process bears a strong resemblance to [[Repurposing diffusionbased image generators for depth estimation | ControlNet]], which also intervenes at multiple layers to condition diffusion models based on inputs like skeleton poses or edge maps <a class="yt-timestamp" data-t="01:27:19">[01:27:19]</a>.

While many interventions successfully repositioned objects, the study noted instances where the model "hallucinated" other things or altered background textures and coloration, suggesting complex interactions beyond simple object shifting <a class="yt-timestamp" data-t="01:31:51">[01:31:51]</a>.

## Conclusion
The experiments provide strong evidence that the Stable Diffusion model, despite being trained exclusively on 2D images, develops an internal linear representation related to scene geometry <a class="yt-timestamp" data-t="01:41:32">[01:41:32]</a>. This includes both a salient object/background distinction and information about relative depth <a class="yt-timestamp" data-t="01:41:40">[01:41:40]</a>. The intervention experiments further support a causal link between these internal representations and the final image output <a class="yt-timestamp" data-t="01:42:19">[01:42:19]</a>. These results add nuance to the ongoing debate about whether generative models learn more than just surface statistics, suggesting they indeed build deeper "world models" <a class="yt-timestamp" data-t="01:42:30">[01:42:30]</a>.

Future work could explore representations of other scene attributes like lighting or texture, or investigate whether LDMs "recapitulate standard steps in [[Computer vision deep dive | computer graphics]]" or semantic aspects like sentiment <a class="yt-timestamp" data-t="01:42:40">[01:42:40]</a>.