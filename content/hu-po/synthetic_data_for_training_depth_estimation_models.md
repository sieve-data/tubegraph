---
title: Synthetic data for training depth estimation models
videoId: WoiI_Pn9yHw
---

From: [[hu-po]] <br/> 

Synthetic data plays a crucial role in training and fine-tuning deep learning models for depth estimation, particularly in overcoming the limitations of real-world sensor data <a class="yt-timestamp" data-t="01:19:39">[01:19:39]</a>.

## Why Synthetic Data is Used

Real depth data sets, often captured using physical sensors like Lidar or structured light sensors, suffer from several inherent problems <a class="yt-timestamp" data-t="01:41:56">[01:41:56]</a>:
*   **Missing Values and Noise:** Physical constraints of capture rigs and material properties (e.g., shiny surfaces reflecting Lidar beams, shadowing effects in structured light) lead to missing depth values, noise, and mixed pixels <a class="yt-timestamp" data-t="00:47:20">[00:47:20]</a>, <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>. For example, ground truth depth from real sensors can appear "trash" or "garbage" <a class="yt-timestamp" data-t="00:50:53">[00:50:53]</a>.
*   **Artifacts:** All depth sensors are sensitive to the material properties of the scene, which can result in artifacts in the ground truth depth <a class="yt-timestamp" data-t="00:48:54">[00:48:54]</a>.

In contrast, synthetic depth data, often generated from game engines or simulations, offers significant advantages <a class="yt-timestamp" data-t="00:51:39">[00:51:39]</a>:
*   **Density and Completeness:** [[synthetic_data_sets_for_training_ai | Synthetic data sets for training AI]] are inherently dense, meaning every pixel has a valid ground truth depth value, with no missing pieces <a class="yt-timestamp" data-t="00:51:40">[00:51:40]</a>.
*   **Cleanliness and Guarantee:** Synthetic depth is the "cleanest possible form of depth," guaranteed by the rendering pipeline <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>. This reduces noise and gradient updates during the fine-tuning protocol <a class="yt-timestamp" data-t="00:52:14">[00:52:14]</a>.
*   **Suitability for Dense Prediction Tasks:** Its perfection at every pixel makes [[synthetic_data_generation_in_ai_training | synthetic data generation in AI training]] particularly useful for dense prediction tasks like monocular depth estimation or panoptic segmentation <a class="yt-timestamp" data-t="00:52:27">[00:52:27]</a>.

## Application in Depth Estimation Models

### Marigold (ETH Zurich)
The paper [[repurposing_diffusionbased_image_generators_for_depth_estimation | Repurposing diffusion-based image generators for monocular depth estimation]], also known as Marigold, leverages the extensive priors learned by large-scale diffusion models (like Stable Diffusion 2) to enable more generalized depth estimation <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
*   **Training Data:** Marigold was fine-tuned on synthetic training data from datasets like Hypersim and Virtual KITTI <a class="yt-timestamp" data-t="01:06:10">[01:06:10]</a>. Hypersim, for example, consists of simulated images from a game engine, where the exact, perfect depth for every pixel is known <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>.
*   **Performance:** Despite being fine-tuned primarily on synthetic data, Marigold delivers state-of-the-art performance across a wide range of real data sets <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. Its predictions can even be better than the ground truth obtained from "shitty" real sensors <a class="yt-timestamp" data-t="01:06:50">[01:06:50]</a>.
*   **Affine Invariant Depth:** A key characteristic of Marigold is that it produces [[interpreting_depth_perception_in_deep_learning_models | affine invariant depth]]. This means it predicts the *relative* distance between pixels (e.g., this pixel is closer than that pixel) but not the *true* metric distance in real-world units (like meters) <a class="yt-timestamp" data-t="01:32:03">[01:32:03]</a>. This "dirty secret" is due to the normalization applied during training, which erases the true distance information <a class="yt-timestamp" data-t="01:32:03">[01:32:03]</a>.

### Patch Fusion (King Abdullah University of Science and Technology)
The paper [[patchbased_depth_prediction_techniques | Patch Fusion: An end-to-end tile-based framework for high-resolution monocular metric depth estimation]] also relies on synthetic data <a class="yt-timestamp" data-t="01:13:56">[01:13:56]</a>.
*   **Training Data:** This model shows impressive results on datasets like Unreal Stereo 4K and MVS Synth, both of which provide synthetic 4K images with perfect ground truth depth <a class="yt-timestamp" data-t="01:13:56">[01:13:56]</a>.
*   **Technique:** The core idea is to cut high-resolution images into multiple patches, run depth prediction on each independently, and then fuse them back together using overlap consistency <a class="yt-timestamp" data-t="01:15:08">[01:15:08]</a>. This approach aims to address the challenge of performing depth estimation on increasing resolutions from consumer cameras <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## Implications for the Future of Depth Sensing

The rapid advancement of [[monocular_depth_estimation_and_its_challenges | monocular depth estimation]] using models trained on [[synthetic_data_in_feature_detection | synthetic data in feature detection]] suggests a future where dedicated depth sensors might become obsolete for many applications <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a>.
*   **Cost-Effectiveness:** Generating depth estimations from a single camera image (like a cell phone camera) and processing it with a model is significantly cheaper and easier than purchasing and integrating expensive Lidar or structured light sensors <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.
*   **Overcoming Sensor Limitations:** AI models can produce cleaner and more complete depth maps than real-world sensors, which are plagued by physical constraints and environmental factors <a class="yt-timestamp" data-t="01:06:50">[01:06:50]</a>.
*   **Industry Disruption:** Entire fields of computer vision focused on specialized depth cameras and hardware sensors could be disrupted as software-based monocular depth estimation becomes good enough for a wide range of use cases <a class="yt-timestamp" data-t="01:08:41">[01:08:41]</a>.

While inference speed remains a current limitation for latency-sensitive applications like autonomous vehicles, ongoing advancements in diffusion models, such as [[Synthetic_Audio_Data_Sets | latent consistency models (LCMs)]], are addressing this by drastically reducing the number of inference steps required <a class="yt-timestamp" data-t="01:42:46">[01:42:46]</a>. Combining these faster techniques with patch-based methods could lead to very fast, state-of-the-art monocular depth estimation <a class="yt-timestamp" data-t="01:42:57">[01:42:57]</a>.