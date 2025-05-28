---
title: Patchbased Depth Estimation Techniques
videoId: WoiI_Pn9yHw
---

From: [[hu-po]] <br/> 

Patchbased depth estimation techniques involve processing an image in smaller sections, or "patches," to achieve high-resolution depth predictions. This approach attempts to overcome the challenges of handling high-resolution images common in modern consumer cameras and devices <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>.

## Patch Fusion: An End-to-End Tile-Based Framework
One such technique is presented in the paper "Patch Fusion: An End-to-End Tile-Based Framework for High-Resolution Monocular Metric Depth Estimation," published on December 4, 2023, by King Abdullah University of Science and Technology <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a>.

### Core Idea
The fundamental concept behind Patch Fusion is to take a high-resolution input image, such as a 4K image from a game engine, and divide it into multiple overlapping patches <a class="yt-timestamp" data-t="01:14:19">[01:14:19]</a>. A [[Monocular Depth Estimation using Diffusion Models | monocular depth estimation]] model then predicts the depth for each of these patches independently <a class="yt-timestamp" data-t="01:14:28">[01:14:28]</a>. This allows for very fine details to be captured within each patch <a class="yt-timestamp" data-t="01:14:56">[01:14:56]</a>.

### Challenges and Solutions
A significant challenge with this patch-wise approach is the lack of global information, which leads to inconsistent depth predictions, particularly at the boundaries where patches meet <a class="yt-timestamp" data-t="01:15:08">[01:15:08]</a>. The paper addresses this by:
*   Applying an overlap in the patches <a class="yt-timestamp" data-t="01:15:22">[01:15:22]</a>.
*   Hardcoding the patches and their overlaps <a class="yt-timestamp" data-t="01:15:38">[01:15:38]</a>.
*   Employing "consistency-aware training" to ensure that overlapping regions have consistent depth values, effectively stitching the patches together <a class="yt-timestamp" data-t="01:15:17">[01:15:17]</a>.

This method achieves highly detailed results, as it effectively processes the image as many smaller, individual images <a class="yt-timestamp" data-t="01:16:13">[01:16:13]</a>.

### Training Data and Architecture
Patch Fusion primarily uses [[Comparison of Synthetic and Real Depth Data | synthetic data]] sets like Unreal Stereo 4K and MVS Synth, which provide perfect ground truth depth because they originate from game engines <a class="yt-timestamp" data-t="01:19:38">[01:19:38]</a>.

However, the architecture and training approach used in Patch Fusion have been criticized:
*   It trains models from scratch <a class="yt-timestamp" data-t="01:17:28">[01:17:28]</a>.
*   It utilizes older Convolutional Neural Networks (CNNs or convnets) <a class="yt-timestamp" data-t="01:17:51">[01:17:51]</a>.
*   It employs three separate networks: a coarse network for the full image, a fine network for individual patches, and a combined guided fusion network to merge them <a class="yt-timestamp" data-t="01:17:31">[01:17:31]</a>.

Some consider this approach to be "cheating" because it relies on processing smaller, easier-to-detail patches rather than a holistic understanding of the scene <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>.

## Comparison with Holistic Depth Estimation
In contrast to Patch Fusion, the [[Monocular Depth Estimation using Diffusion Models | Marigold paper]] (also from December 2023) approaches [[Monocular Depth Estimation using Diffusion Models | monocular depth estimation using diffusion models]] by taking the entire image, compressing it into a latent space, and then denoising within that latent space to magically infer the depth <a class="yt-timestamp" data-t="01:16:23">[01:16:23]</a>.

The core idea of combining patch-based processing with advanced models like [[Monocular Depth Estimation using Diffusion Models | Marigold]] is seen as a promising direction for future research, potentially leading to [[Monocular Depth Estimation using Diffusion Models | state-of-the-art monocular depth estimation]] results by leveraging the benefits of both approaches <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>.

## Implications for Depth Sensing Hardware
The advancements in [[Monocular Depth Estimation using Diffusion Models | monocular depth estimation]] have significant implications for the market of specialized depth sensors like Lidar and structured light sensors. These traditional sensors often suffer from inherent issues:
*   **Missing depth values** due to physical constraints of the capture rig or sensor properties <a class="yt-timestamp" data-t="01:47:20">[01:47:20]</a>.
*   **Noise and artifacts** caused by reflective surfaces or shadowing effects <a class="yt-timestamp" data-t="01:48:45">[01:48:45]</a>.
*   **Sensitivity to material properties** of the scene <a class="yt-timestamp" data-t="01:48:57">[01:48:57]</a>.

As AI models become capable of producing depth maps of superior quality to those from physical sensors, the need for expensive and cumbersome depth sensors may diminish <a class="yt-timestamp" data-t="01:07:06">[01:07:06]</a>. A simple cell phone camera combined with these advanced models could provide sufficient depth information, making dedicated depth sensors obsolete in many [[Applications and Limitations of Monocular Depth | applications]] like [[Applications and Limitations of Monocular Depth | autonomous driving]] and robotics <a class="yt-timestamp" data-t="01:07:56">[01:07:56]</a>. While inference speed remains a [[Applications and Limitations of Monocular Depth | limitation]] for real-time applications like autonomous vehicles <a class="yt-timestamp" data-t="01:10:42">[01:10:42]</a>, the rapid progress in diffusion models, such as latent consistency models (LCMs), suggests that this hurdle may soon be overcome <a class="yt-timestamp" data-t="01:42:41">[01:42:41]</a>.