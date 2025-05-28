---
title: Monocular depth estimation and its challenges
videoId: WoiI_Pn9yHw
---

From: [[hu-po]] <br/> 

Monocular depth estimation is a fundamental [[computer_vision_deep_dive | computer vision]] task that involves recovering 3D depth information from a single 2D image <a class="yt-timestamp" data-t="09:39:41">[09:39:41]</a>. This problem is geometrically ill-posed and requires significant scene understanding <a class="yt-timestamp" data-t="09:43:51">[09:43:51]</a>. Historically, depth estimation often leveraged camera geometry from stereo or multi-view camera setups <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>, but more recent advancements focus on monocular (single-image) methods <a class="yt-timestamp" data-t="06:01:03">[06:01:03]</a>.

## Challenges of Monocular Depth Estimation

Monocular depth estimators often struggle with unfamiliar content or "out-of-distribution" images, as their knowledge of the visual world is limited by their training data <a class="yt-timestamp" data-t="11:06:07">[11:06:07]</a>. For example, a model trained on autonomous vehicle datasets may perform poorly on images of a dog <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>.

One major [[challenges_in_video_motion_estimation | challenge]] is that real depth data, often captured by sensors like LiDAR or structured light sensors, can be noisy, have missing values, or contain artifacts due to physical constraints and material properties <a class="yt-timestamp" data-t="47:18:00">[47:18:00]</a>. This contrasts with [[synthetic_data_for_training_depth_estimation_models | synthetic data]], which offers perfectly dense and complete depth information <a class="yt-timestamp" data-t="51:39:40">[51:39:40]</a>.

## Marigold: Repurposing Diffusion Models for Depth

A recent paper, "Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation," introduces Marigold, a state-of-the-art model published on December 4, 2023, by ETH Zurich <a class="yt-timestamp" data-t="03:18:20">[03:18:20]</a>.

### Leveraging Image Priors

Marigold's core idea is to leverage the extensive priors captured in recent generative [[repurposing_diffusionbased_image_generators_for_depth_estimation | diffusion models]], specifically Stable Diffusion models <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. These models have been trained on internet-scale data (like LAION-5B, which contains billions of images) <a class="yt-timestamp" data-t="24:24:00">[24:24:00]</a>, giving them a very rich understanding of the visual world, including implicit depth cues <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.

### How Marigold Works

Marigold frames monocular depth estimation as a conditional denoising diffusion generation task <a class="yt-timestamp" data-t="25:09:11">[25:09:11]</a>. It uses a Stable Diffusion V2 model, with most of its components "frozen" (i.e., not trained):
*   **Frozen VAE:** The Variational Autoencoder (VAE) encoder and decoder components of Stable Diffusion are kept intact <a class="yt-timestamp" data-t="31:51:00">[31:51:00]</a>. This is notable because the VAE was trained only on real RGB images (LAION-5B does not contain depth images), yet it can miraculously encode depth images by duplicating their single channel into three "fake" RGB channels <a class="yt-timestamp" data-t="32:28:00">[32:28:00]</a>. The decoded three-channel output is then averaged to get the final single-channel depth map <a class="yt-timestamp" data-t="54:50:00">[54:50:00]</a>.
*   **Fine-tuned UNet:** The denoising UNet, the core of the diffusion model, is fine-tuned <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a>. It's conditioned on both the encoded real image and the encoded depth latent codes, which are concatenated together <a class="yt-timestamp" data-t="37:28:00">[37:28:00]</a>. The UNet's input channels are doubled, and its initial weights are duplicated and divided by two to prevent activation magnitude inflation <a class="yt-timestamp" data-t="38:47:00">[38:47:00]</a>.
*   **Training Data:** Marigold is fine-tuned on relatively small [[synthetic_data_for_training_depth_estimation_models | synthetic data]] sets like Hypersim and Virtual KITTI (around 74,000 images) <a class="yt-timestamp" data-t="19:00:00">[19:00:00]</a>. [[synthetic_data_for_training_depth_estimation_models | Synthetic data]] is preferred due to its perfect density and lack of real-world sensor artifacts <a class="yt-timestamp" data-t="51:39:40">[51:39:40]</a>.
*   **Denoising Process:** During training, Gaussian noise is progressively added to the depth image's latent representation. The UNet is trained to predict and remove this noise <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>. At inference time, it starts from pure noise and iteratively removes it, conditioned by the input image <a class="yt-timestamp" data-t="29:36:00">[29:36:00]</a>.
*   **Non-Markovian Sampling (DDIM):** Marigold utilizes the DDIM (Denoising Diffusion Implicit Models) approach, which allows for "skipped steps" in the denoising process, accelerating inference <a class="yt-timestamp" data-t="56:45:00">[56:45:00]</a>.
*   **Test-Time Ensembling:** To improve robustness and reduce variance, Marigold employs an ensembling scheme where multiple inferences are run with different initial noise samples, and their results are combined (e.g., by taking the median) <a class="yt-timestamp" data-t="01:01:46">[01:01:46]</a>. Ensembling 10 predictions can reduce error by 8%, and 20 predictions by 9.5% <a class="yt-timestamp" data-t="01:09:18">[01:09:18]</a>.

### Affine Invariance

Marigold predicts "affine invariant depth" <a class="yt-timestamp" data-t="12:49:00">[12:49:00]</a>. This means the model learns relative distances (e.g., pixel A is closer than pixel B) but not true metric distances (e.g., pixel A is 1 meter away) <a class="yt-timestamp" data-t="14:23:00">[14:23:00]</a>. The depth values are normalized to a range like -1 to 1 <a class="yt-timestamp" data-t="43:29:00">[43:29:00]</a>. This simplifies the problem for the model but requires an additional step to recover true scale for applications needing precise physical distances (like [[complexity_and_effectiveness_of_video_tracking_methods | SLAM]] or photogrammetry) <a class="yt-timestamp" data-t="14:46:00">[14:46:00]</a>.

### Performance and Implications

Marigold achieves state-of-the-art performance across various datasets, often outperforming prior methods, with reported gains over 20% in specific cases <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. Its fine-tuning protocol is resource-efficient, taking only a couple of days on a single consumer GPU <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. The quality of depth predictions from Marigold can even surpass the "ground truth" derived from some real-world sensors, which often produce noisy or incomplete data <a class="yt-timestamp" data-t="01:06:50">[01:06:50]</a>. This advancement suggests that specialized depth sensors (like LiDAR or structured light cameras) may become obsolete, as a simple cell phone camera combined with such models could provide superior depth information at a much lower cost <a class="yt-timestamp" data-t="01:07:02">[01:07:02]</a>.

## PatchFusion: A Tile-Based Approach

Another paper, "PatchFusion: An End-to-End Tile-Based Framework for High-Resolution Monocular Metric Depth Estimation," published on the same day as Marigold, proposes a different strategy for high-resolution depth estimation <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

### Tile-Based Framework

PatchFusion's main idea is to divide a high-resolution image into overlapping patches <a class="yt-timestamp" data-t="01:13:59">[01:13:59]</a>. Depth prediction is then run independently on each patch. Because these predictions are independent, the resulting depth maps for each patch might not be globally consistent (e.g., object depths don't line up across patch boundaries) <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>. PatchFusion addresses this by applying a consistency-aware training method that leverages overlapping regions to fuse the individual patch predictions into a coherent high-resolution depth map <a class="yt-timestamp" data-t="01:15:15">[01:15:15]</a>.

### Critique

While PatchFusion can produce highly detailed depth maps, its approach is seen as less elegant. It trains its networks from scratch using convolutional neural networks (ConvNets) rather than leveraging large pre-trained models like diffusion models <a class="yt-timestamp" data-t="01:17:51">[01:17:51]</a>. This method, while effective for detail, essentially "cheats" by processing smaller, easier-to-handle sub-problems independently <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. A potential future research direction is to combine PatchFusion's tile-based strategy with Marigold's diffusion-based method for even more accurate and detailed results <a class="yt-timestamp" data-t="01:18:28">[01:18:28]</a>.

## Future Outlook

The rapid progress in monocular depth estimation, driven by the power of large pre-trained models, suggests a future where dedicated depth sensors are less critical <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. While current diffusion models might be slower for real-time applications due to iterative inference steps and ensembling <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a>, advancements like Latent Consistency Models (LCMs) are addressing this by enabling significantly faster inference <a class="yt-timestamp" data-t="01:42:40">[01:42:40]</a>. This efficiency, combined with techniques like patch processing, could soon deliver both high-quality and high-speed monocular depth estimation.