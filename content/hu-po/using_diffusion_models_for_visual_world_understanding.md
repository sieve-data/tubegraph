---
title: Using diffusion models for visual world understanding
videoId: WoiI_Pn9yHw
---

From: [[hu-po]] <br/> 

## Introduction to Monocular Depth Estimation

Monocular depth estimation is a foundational computer vision task that involves recovering 3D depth from a single image [09:37]. This task is geometrically ill-posed and necessitates extensive scene understanding [09:43]. Historically, depth estimation often relied on camera geometry and stereo or multi-view setups using multiple cameras to capture simultaneous images [05:27]. However, modern approaches increasingly focus on monocular methods, performing depth estimation from just one image [06:01].

Previous monocular depth estimators have struggled with "out of distribution" content, meaning images with unfamiliar content or layout, as their knowledge of the visual world is limited by their training data [11:06]. For instance, a model trained exclusively on autonomous vehicle datasets would perform poorly on images of different domains, such as a dog [12:02].

## Diffusion Models and Visual World Understanding

The advent of deep learning has revolutionized monocular depth estimation, with progress mirroring the growth in model capacity from modest Convolutional Neural Networks (CNNs) to large [[Diffusion models and Transformers | Transformer architectures]] [10:44].

The *Marigold* paper, titled "Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation" (published December 4, 2023, by ETH Zurich), explores whether the extensive "priors" captured in recent generative [[Diffusion models and image generation | diffusion models]] can enable more generalizable depth estimation [03:18, 03:29, 12:21]. These [[Diffusion models and image generation | diffusion models]], trained on internet-scale data like LAION 5B (five billion clip images), possess a robust "world model of the visual world" [04:00, 11:11, 12:24, 01:05:21]. This comprehensive understanding of the visual world is hypothesized to be the cornerstone for effective monocular depth estimation [10:05, 12:12, 01:03:03].

Diffusion models learn to reverse a diffusion process that gradually adds Gaussian noise to images [00:00:03.491]. By learning to predict and remove this noise, they can generate new samples that align with a given condition, such as text in [[Text to image diffusion models | text-to-image diffusion models]] [00:00:03.491, 00:23:24].

## Marigold: Repurposing Diffusion Models for Depth

The *Marigold* method frames monocular depth estimation as a [[Conditional diffusion models for neural networks | conditional denoising diffusion generation task]], where the model predicts depth conditioned on an input image [02:50].

### Leveraging Pre-trained Components

*Marigold* utilizes a pre-trained [[Latent diffusion models and architectures | latent diffusion model]], specifically Stable Diffusion V2, which operates in a lower-dimensional latent space for computational efficiency and suitability for high-resolution image generation [03:56, 02:57]. The method employs a **frozen Variational Autoencoder (VAE)** from Stable Diffusion to encode both the input image and the corresponding depth map into this latent space [03:19, 03:44].

A surprising aspect of *Marigold* is its ability to encode depth images, which are single-channel, using a VAE trained exclusively on three-channel RGB images (like those in LAION 5B, which does not contain depth images) [03:28, 03:51]. To enable this, the single-channel depth image is replicated across three channels to simulate an RGB image before encoding [03:51]. Remarkably, the encoded depth maps can be reconstructed from their latent codes with negligible error, suggesting the VAE can effectively process this "out-of-distribution" input [03:55].

### Adapted Denoising U-Net

The core of the [[Latent diffusion models and scene representation | latent diffusion model]] is a U-Net, which performs the denoising task [02:57]. In *Marigold*, this U-Net is modified to accept a concatenated input of both the encoded RGB image and the encoded depth latent codes [03:09, 03:28]. To accommodate the expanded input dimension, the input channels of the U-Net are doubled, and the corresponding weight tensors are duplicated and their values halved to prevent an inflation of activation magnitude [03:47]. This seemingly "weird" but effective modification allows the pre-trained U-Net to be fine-tuned for depth estimation [03:57, 04:40].

### Training and Normalization

*Marigold* is fine-tuned on synthetic training data, specifically the Hypersim and Virtual KITTI datasets [01:01:21]. Synthetic depth data is inherently dense and complete, ensuring every pixel has a valid ground truth depth value, which is crucial as VAEs cannot handle invalid pixels [05:12, 05:40]. This contrasts with real depth data captured by sensors like LiDAR or structured light sensors, which often suffer from missing values, noise, and artifacts due to physical constraints and material properties of the scene [04:36, 04:51].

Depth maps are normalized to a range of -1 to 1 to match the VAE's expected input [04:42]. This linear normalization enforces an "affine invariant depth representation," meaning the model predicts relative distances (e.g., this pixel is closer than that) but not absolute, real-world distances in meters [04:48, 01:32:01]. This choice, while simplifying training, means the output is not "true depth" and requires an additional step to convert it to a metric scale for applications requiring precise physical measurements, such as Simultaneous Localization and Mapping (SLAM) or photogrammetry [01:14:00, 01:16:00].

### Inference Process and Techniques

At inference time, a random pure noise latent variable is sampled. The denoising U-Net iteratively refines this latent, conditioned on the encoded input RGB image, to produce a denoised depth latent [00:52:57]. This depth latent is then decoded by the VAE's decoder, and its three channels are averaged to yield the final single-channel depth map [00:54:11].

To improve robustness and performance, *Marigold* utilizes:
*   **Non-Markovian Sampling (DDIM)**: This technique, introduced in the "Denoising Diffusion Implicit Models" paper, allows the denoising process to skip steps, significantly accelerating inference compared to traditional Markovian diffusion models [00:56:41].
*   **Multi-resolution Noise**: Composed of superimposing several Gaussian noise images of different scales, this noise helps the model learn both high-frequency details (textures) and low-frequency global structures [00:55:07].
*   **Test-Time Ensembling**: Multiple inference passes are performed with different initial noise samples, and the median of the resulting depth maps is taken to generate a more accurate and stable final prediction [01:01:46, 01:09:18]. Ensembling 10 predictions can reduce the absolute relative error by 8%, while 20 predictions lead to a 9.5% reduction [01:09:20].

## Comparison with Other Methods

*Marigold* achieves state-of-the-art performance across a wide range of datasets, outperforming prior art in most cases [01:05:10, 01:05:59]. This success highlights the power of leveraging large pre-trained [[Diffusion models and image generation | diffusion models]] and their inherent visual world understanding.

In contrast, the *Patch Fusion* paper (also published December 4, 2023, by King Abdullah University of Science and Technology) addresses high-resolution monocular depth estimation by dividing images into overlapping patches [01:11:45, 01:13:59]. Each patch is processed independently by separate networks (course and fine networks, trained from scratch using CNNs), and the resulting inconsistent depth predictions are then fused together [01:15:08, 01:17:28]. While achieving high detail, this approach is more computationally complex, relies on older architectures, and does not leverage the broad prior knowledge of pre-trained [[Diffusion models and image generation | diffusion models]] as effectively as *Marigold* [01:17:09].

## Challenges and Future Potential

Despite its impressive results, *Marigold*'s affine invariant output means that direct application in fields like robotics or autonomous vehicles, where precise metric depth is crucial for tasks like SLAM, remains a challenge [01:10:47]. However, methods exist to infer true depth by fine-tuning on datasets with real depth or by applying post-hoc normalization techniques [01:00:28].

The inference speed of *Marigold* can be a bottleneck due to the iterative denoising process and ensembling [01:10:09]. However, advancements in [[Latent diffusion models and architectures | latent diffusion models]] (such as Latent Consistency Models (LCMs) and LoRAs) promise drastically faster inference, potentially enabling real-time applications [01:42:40].

The rapid progress in monocular depth estimation, particularly with [[Video diffusion models in generative 3D | diffusion models]], suggests a future where dedicated depth sensors (LiDAR, structured light) become obsolete, as AI-powered methods can generate superior depth information from standard RGB cameras at a fraction of the cost [01:06:06, 01:07:06, 01:41:41]. This could lead to a significant disruption in the hardware sensor market [01:08:51]. The simplicity of combining current state-of-the-art techniques, such as integrating *Marigold*'s diffusion-based approach with *Patch Fusion*'s tiling strategy, also points to accessible avenues for further research and immediate improvements in performance [01:18:29].