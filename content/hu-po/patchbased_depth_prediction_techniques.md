---
title: Patchbased depth prediction techniques
videoId: WoiI_Pn9yHw
---

From: [[hu-po]] <br/> 

Patch-based depth prediction techniques offer an alternative approach to [[monocular_depth_estimation_and_its_challenges | monocular depth estimation]], particularly for high-resolution images. While capable of producing highly detailed results, these methods can introduce inconsistencies and may rely on older model architectures.

## Patch Fusion Framework

One such technique is presented in the paper "Patch Fusion: An End-to-End Tile-Based Framework for High-Resolution Monocular Metric Depth Estimation" <a class="yt-timestamp" data-t="01:16:11">[01:16:11]</a>. Published on December 4, 2023, by King Abdullah University of Science and Technology <a class="yt-timestamp" data-t="01:12:38">[01:12:38]</a>, this paper introduces a "tile-based" framework for depth estimation <a class="yt-timestamp" data-t="01:13:38">[01:13:38]</a>.

The core idea of Patch Fusion is to process an image by dividing it into smaller patches or tiles <a class="yt-timestamp" data-t="01:14:19">[01:14:19]</a>. This allows for high-resolution images, such as 4K resolution, to be handled effectively <a class="yt-timestamp" data-t="01:13:17">[01:13:17]</a>.

### How it Works

1.  **Patch Division**: A high-resolution input image is cut into multiple patches <a class="yt-timestamp" data-t="01:14:25">[01:14:25]</a>.
2.  **Independent Depth Prediction**: [[monocular_depth_estimation_and_its_challenges | Monocular depth estimation]] is performed independently on each of these patches <a class="yt-timestamp" data-t="01:14:30">[01:14:30]</a>.
    *   This independent processing helps capture intricate details within each sub-patch, leading to highly detailed depth maps, such as visible individual edges on beams and plants <a class="yt-timestamp" data-t="01:17:09">[01:17:09]</a>.
3.  **Consistency Awareness**: A "consistency-aware training" step is implemented to address inconsistencies that arise because patches are processed independently and their depth values might not align <a class="yt-timestamp" data-t="01:15:17">[01:15:17]</a>.
    *   This involves applying some overlap in the patches <a class="yt-timestamp" data-t="01:15:22">[01:15:22]</a>.
    *   The paper utilizes 49 hardcoded and overlapping patches <a class="yt-timestamp" data-t="01:15:31">[01:15:31]</a>.
    *   An L2 loss is imposed on overlapping regions to ensure consistent depth predictions across patch boundaries <a class="yt-timestamp" data-t="01:19:36">[01:19:36]</a>.
4.  **Fusion**: The individual patch predictions are then combined to form a complete, consistent depth map for the entire image <a class="yt-timestamp" data-t="01:16:04">[01:16:04]</a>.

### Data and Architectures

The Patch Fusion framework was evaluated using synthetic datasets such as Unreal Stereo 4K and MVSSynth <a class="yt-timestamp" data-t="01:13:56">[01:13:56]</a>. [[synthetic_data_for_training_depth_estimation_models | Synthetic data for training depth estimation models]] is inherently dense and complete, ensuring every pixel has a valid ground truth depth value, which is beneficial for training <a class="yt-timestamp" data-t="01:51:39">[01:51:39]</a>.

The paper uses three different networks:
*   A coarse network that sees the full image <a class="yt-timestamp" data-t="01:17:35">[01:17:35]</a>.
*   A fine network that processes individual patches <a class="yt-timestamp" data-t="01:17:38">[01:17:38]</a>.
*   A "combined guided Fusion Network" that merges their outputs <a class="yt-timestamp" data-t="01:17:43">[01:17:43]</a>.

A notable aspect is that all three networks are trained from scratch, and they rely on conventional CNN architectures, such as 3x3 convolutions and max pooling operations, which contrasts with more modern approaches like Transformers <a class="yt-timestamp" data-t="01:17:46">[01:17:46]</a>.

### Comparison to Other Methods

Unlike approaches that compress the entire image into a latent space and then denoise it (e.g., Marigold, a [[repurposing_diffusionbased_image_generators_for_depth_estimation | diffusion-based image generator for depth estimation]]), patch-based methods explicitly treat sub-sections of the image as individual problems <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a>. While this yields high detail, it is considered by some to be a "cheating" method as it simplifies the global context problem by breaking it down into many smaller, localized problems <a class="yt-timestamp" data-t="01:16:47">[01:16:47]</a>.

## Future Potential

The core idea of patching and fusing, despite its perceived "cheating" aspect, is seen as a valuable technique <a class="yt-timestamp" data-t="01:16:47">[01:16:47]</a>. It can be applied to other state-of-the-art [[monocular_depth_estimation_and_its_challenges | monocular depth estimation]] models, such as those that leverage diffusion models, to potentially achieve even better results <a class="yt-timestamp" data-t="01:18:26">[01:18:26]</a>. Combining the high-level understanding of models trained on internet-scale data with the fine-grained detail provided by patch processing could lead to significant advancements <a class="yt-timestamp" data-t="01:19:07">[01:19:07]</a>. This integration would involve taking an image, cutting it into patches, feeding each patch through a diffusion-based depth model, and then intelligently combining the outputs, potentially requiring minimal additional training <a class="yt-timestamp" data-t="01:18:41">[01:18:41]</a>.