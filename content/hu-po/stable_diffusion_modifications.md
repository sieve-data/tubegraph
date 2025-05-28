---
title: Stable Diffusion modifications
videoId: Mp-HMQcB_M4
---

From: [[hu-po]] <br/> 

ControlNet is a neural network structure designed to add conditional control to pre-trained large [[diffusion_models_and_image_generation | diffusion models]], specifically [[latent_diffusion_models_and_architectures | Stable Diffusion]] <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. Released in early 2023, its GitHub repository quickly garnered significant attention, demonstrating rapid internet adoption <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## The Problem ControlNet Solves

While [[diffusion_models_and_image_generation | diffusion models]] excel at text-to-image generation, it has been challenging to achieve precise control over the exact image output <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Prompt-based control, while revolutionary, often doesn't offer the fine-tuned control needed for practical content creation <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. ControlNet addresses this by allowing users to specify detailed conditions, such as object edges or human poses, to guide the image generation process <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Core Concept and Architecture

ControlNet works by cloning the weights of a large [[latent_diffusion_models_and_architectures | diffusion model]] (like [[latent_diffusion_models_and_architectures | Stable Diffusion]]) into two copies: a **locked copy** and a **trainable copy** <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.
*   The **locked copy** preserves the network's extensive capabilities learned from billions of images <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
*   The **trainable copy** is specifically trained on task-specific datasets to learn the desired conditional control <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>. This approach helps avoid overfitting with smaller datasets and maintains the quality of the pre-trained model <a class="yt-timestamp" data-t="00:44:57">[00:44:57]</a>.

These two copies are connected by a unique type of convolutional layer called a **zero convolution** <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.
*   **Zero Convolution**: This is a 1x1 convolutional layer with both weights and biases initialized to zero <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>. Initially, it does not add new noise or influence the deep features, ensuring the pre-trained model's performance is perfectly preserved at the first training step <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. As training progresses, its weights progressively grow from zeros to optimized parameters <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
*   **Integration**: The input condition (e.g., an Edge Map) is first encoded into a 64x64 feature space using a "Tiny Network E" (a small convolutional network) to match the [[latent_diffusion_models_and_architectures | latent image]] dimensionality of [[latent_diffusion_models_and_architectures | Stable Diffusion]] <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a>. This conditioned feature map is then fed into the ControlNet, which influences the [[latent_diffusion_models_and_architectures | U-Net]] architecture of the [[latent_diffusion_models_and_architectures | Stable Diffusion]] model via these zero convolution connections <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>. The original [[latent_diffusion_models_and_architectures | Stable Diffusion]] [[diffusion_models_and_transformers | U-Net]] blocks are conditioned by text prompts (encoded by OpenCLIP) <a class="yt-timestamp" data-t="01:10:25">[01:10:25]</a> and diffusion time steps (encoded by positional encoding) <a class="yt-timestamp" data-t="01:10:25">[01:10:25]</a>.

## Training Strategies

ControlNet's training is designed to be efficient and robust across different computational environments and dataset sizes. The core objective is to predict noise within the [[latent_diffusion_models_and_architectures | latent space]], using the current noisy image, time step, text prompt, and the task-specific condition <a class="yt-timestamp" data-t="01:21:44">[01:21:44]</a>.

*   **Small-Scale Training**: For limited computational devices (e.g., personal GPUs), partially breaking connections between ControlNet and [[latent_diffusion_models_and_architectures | Stable Diffusion]] (e.g., only connecting to the middle block instead of all decoder blocks) can accelerate convergence by 1.6 times <a class="yt-timestamp" data-t="01:24:50">[01:24:50]</a>. Once a reasonable association is learned, these links can be reconnected for continued training to improve accuracy <a class="yt-timestamp" data-t="01:25:12">[01:25:12]</a>.
*   **Large-Scale Training**: When powerful computational clusters are available (e.g., Nvidia A100 GPUs with 80 GB memory), a two-part training scheme is used:
    1.  **Phase 1 (50,000 steps)**: Only the ControlNet weights are trained, while the [[latent_diffusion_models_and_architectures | Stable Diffusion]] weights remain locked <a class="yt-timestamp" data-t="01:26:30">[01:26:30]</a>.
    2.  **Phase 2**: After sufficient initial training, all weights of the [[latent_diffusion_models_and_architectures | Stable Diffusion]] model are unlocked, and both ControlNet and the [[latent_diffusion_models_and_architectures | Stable Diffusion]] model are jointly trained <a class="yt-timestamp" data-t="01:26:39">[01:26:39]</a>. This robust approach helps prevent overfitting on smaller task-specific datasets <a class="yt-timestamp" data-t="01:26:16">[01:26:16]</a>.

### Data Augmentation for Conditions
The paper details various methods to generate condition-image pairs for training:
*   **Canny Edge Detection**: Generates 3 million edge-to-image caption pairs using random thresholds for the Canny detector <a class="yt-timestamp" data-t="01:27:51">[01:27:51]</a>.
*   **Hough Lines**: Uses a deep Hough transform to detect straight lines, typically starting from a Canny Edge model checkpoint <a class="yt-timestamp" data-t="01:29:56">[01:29:56]</a>.
*   **HED Boundary Detection**: Another type of edge detection method, yielding holistic nested edge maps <a class="yt-timestamp" data-t="01:31:11">[01:31:11]</a>.
*   **User Scribbles**: Synthesized by combining HED boundary detection with aggressive data augmentations (e.g., random masking, morphological transformations) <a class="yt-timestamp" data-t="01:31:47">[01:31:47]</a>.
*   **Human Pose Estimation**: Utilizes learning-based pose estimation to detect human key points, filtering for complete skeletons <a class="yt-timestamp" data-t="01:32:43">[01:32:43]</a>.
*   **Semantic Segmentation**: Leverages datasets like COCO or AD20K for pixel-level or polygon-mask segmentation information <a class="yt-timestamp" data-t="01:35:08">[01:35:08]</a>.
*   **Depth Estimation**: Uses models like Midas to approximate depth maps from single images, generating millions of pairs <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.
*   **Normal Maps**: Derived from depth maps or explicit datasets, representing surface orientations <a class="yt-timestamp" data-t="01:39:09">[01:39:09]</a>.
*   **Cartoon Line Drawing**: Extracts line art from cartoon illustrations <a class="yt-timestamp" data-t="01:40:54">[01:40:54]</a>.

## Capabilities and Examples

ControlNet significantly enhances the control over [[diffusion_models_and_image_generation | Stable Diffusion]] outputs:

*   **Fine-Grained Control**: Users can specify conditions like Edge Maps, segmentation maps, or key points to dictate the structure of generated images <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Robustness**: The model is robust even with small training datasets (under 100K samples), avoiding overfitting <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Diverse Conditions**: ControlNet has been demonstrated with various inputs:
    *   **Canny Edge**: Maintaining intricate structural details (e.g., deer antlers, architectural details) <a class="yt-timestamp" data-t="01:44:03">[01:44:03]</a>.
    *   **Human Pose**: Generating images based on a detected human skeleton, allowing manipulation of posture <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
    *   **Semantic Segmentation**: Guiding image composition based on object regions <a class="yt-timestamp" data-t="01:51:26">[01:51:26]</a>.
    *   **Depth and Normal Maps**: Controlling the 3D structure and surface orientation <a class="yt-timestamp" data-t="01:52:35">[01:52:35]</a>.
    *   **Scribbles**: Even primitive user scribbles can effectively control the output <a class="yt-timestamp" data-t="02:03:51">[02:03:51]</a>.
*   **Sudden Convergence**: During training, there's a phenomenon where the model suddenly learns to adapt to the input conditions, transitioning from generic text-to-image outputs to precisely controlled ones <a class="yt-timestamp" data-t="01:58:39">[01:58:39]</a>.

## Performance and Computational Efficiency

ControlNet's design ensures that training is as fast as fine-tuning a [[latent_diffusion_models_and_architectures | diffusion model]] <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. Because the original [[latent_diffusion_models_and_architectures | Stable Diffusion]] weights are locked during the initial training phase, gradient computation on the core model is avoided, saving GPU memory and accelerating training <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>. Training with ControlNet requires only about 23% more GPU memory and 34% more time per session compared to standard [[latent_diffusion_models_and_architectures | Stable Diffusion]] training <a class="yt-timestamp" data-t="01:17:28">[01:17:28]</a>.

## Authorship and Origin

The ControlNet paper, "Adding Conditional Control to Text-to-Image [[diffusion_models_and_image_generation | Diffusion Models]]", was written by Lvmin Zhang and Maneesh Agrawala from Stanford University <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. It was released on February 10, 2023 <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. The core concept of "HyperNetwork," where a small recurrent network influences the weights of a larger one, originated in natural language processing and was later applied to image generation with GANs and other [[latent_diffusion_models_and_architectures | diffusion models]] <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

## Future Potential

ControlNet represents a significant advancement in controllable [[diffusion_models_and_image_generation | image generation]], opening floodgates for various types of content creation <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Its simple yet powerful concept allows for broad applicability to other [[diffusion_models_and_image_generation | diffusion models]] and potentially combinations of multiple control conditions in the future <a class="yt-timestamp" data-t="02:07:06">[02:07:06]</a>.