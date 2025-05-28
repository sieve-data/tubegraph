---
title: Comparison of DreamFusion and stable diffusion
videoId: Z6dB1zIfwr4
---

From: [[hu-po]] <br/> 

## Introduction to DreamFusion
DreamFusion is a variant of [[diffusion_models_and_controlnet | diffusion models]] specifically focused on 3D generative processes <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Its primary function is to transform a text-based prompt into a 3D model <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Examples include generating a 3D mesh of a chimpanzee dressed like Henry VIII, which can be rotated <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

The potential impact of 3D generation is considered "absolutely insane," even more disruptive than 2D image generation <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This is due to the difficulty of 3D modeling and its wide applications in fields like video games <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Generating 3D models with just text prompts is seen as a revolutionary development <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

DreamFusion is early-stage work developed by Ben Poole and Google Research <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. While an official GitHub repository is not publicly available, a PyTorch implementation of the paper exists <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## Core Models and Implementations
The original DreamFusion paper utilizes Google's Imagen model for its diffusion component <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Imagen is Google's proprietary version of an image generation model <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Since Imagen is not publicly available, community implementations, such as the one discussed, use [[stable_diffusion_3_overview | Stable Diffusion]] as a substitute <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Specifically, the Hugging Face Diffusers implementation of [[stable_diffusion_3_overview | Stable Diffusion]] is often used <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Differences in Diffusion Mechanisms: Image Space vs. Latent Space
A key distinction between Imagen and [[stable_diffusion_3_overview | Stable Diffusion]] lies in their diffusion spaces <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>:
*   **Imagen**: Diffuses directly in the image space <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This means noise is added directly to the image pixels and then diffused out <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **[[stable_diffusion_3_overview | Stable Diffusion]]**: Functions as a latent diffusion model <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. It diffuses in a latent space, not the original image space <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This involves encoding the image into a vector representation (latent space) using a neural network and then performing diffusion in that latent space <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. This approach requires propagating back from an autoencoder, which adds extra time cost <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## [[technical_aspects_and_implementation_challenges_of_dreamfusion | Technical Aspects and Implementation Challenges]]
### Training and Hardware Requirements
Training DreamFusion is resource-intensive. A thousand training steps can take about three hours on an Nvidia V100 GPU <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. V100 GPUs are high-end graphics cards, typically costing around $8,000 and often equipped with 16 GB or even 32 GB of memory <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This highlights the significant computational power needed.

### Core Components and Algorithms
DreamFusion uses a Nerf (Neural Radiance Field) backbone, specifically implemented with a multi-resolution grid encoder, inspired by Instant NGP from NV Labs (Nvidia research) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Nerf**: A Nerf model parameterizes volumetric density and Albedo color using a Multi-Layer Perceptron (MLP) <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>. It predicts the color at each point along a ray cast from the camera, along with other 3D modeling properties like Albedo and density <a class="yt-timestamp" data-t="00:34:10">[00:34:10]</a>.
*   **Differentiable Rendering**: The system employs differentiable rendering, which allows neural networks to be used for rendering and enables gradient propagation for training <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
*   **Ray Marching**: The system may utilize ray marching algorithms, an interesting technique to generate procedural scenes from a shader <a class="yt-timestamp" data-t="00:24:39">[00:24:39]</a>.

### The Janus Problem
A notable challenge in 3D generation, identified by Ben Poole (the original author of the DreamFusion paper), is the "Janus problem" <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This issue manifests as models generating objects with multiple faces or inconsistent semantic understanding (e.g., a head having two eyes on the front and another two on the back) <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. It often appears as if the model is combining multiple 2D images into a 3D shape without full semantic coherence <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. The problem is named after Janus, the Roman God of Duality, who is depicted with two faces <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

**View-Dependent Prompting**: This technique is suggested to help alleviate the Janus problem, though it doesn't solve it entirely <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. It involves expanding the original text prompt to include descriptions from different viewpoints (e.g., "overhead view of that") and using these expanded prompts for guidance during generation <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### Training Process and Score Distillation Loss
DreamFusion generates 3D objects by optimizing parameters (Theta) of a 3D volume, with a volumetric renderer (G) transforming these parameters into an image <a class="yt-timestamp" data-t="01:03:12">[01:03:12]</a>. The core of its optimization relies on a technique called **Score Distillation Sampling (SDS) loss function** <a class="yt-timestamp" data-t="01:00:01">[01:00:01]</a>.
1.  **Rendering**: The Nerf model (randomly initialized and trained from scratch for each caption) is repeatedly rendered from random camera angles and positions <a class="yt-timestamp" data-t="00:32:37">[00:32:37]</a>. Shading is applied using normals computed from density gradients and random lighting directions <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>.
2.  **Diffusion and Reconstruction**: The rendered image is diffused (noise is added) <a class="yt-timestamp" data-t="00:35:16">[00:35:16]</a>.
3.  **Score Distillation**: A *frozen* conditional image generation model (Imagen or [[stable_diffusion_3_overview | Stable Diffusion]]) then attempts to predict the injected noise and reconstruct the image <a class="yt-timestamp" data-t="00:35:18">[00:35:18]</a>. The model is *not* fine-tuned <a class="yt-timestamp" data-t="00:35:24">[00:35:24]</a>.
4.  **Backpropagation**: A low-variance update direction is backpropagated *through the rendering process* (not through the diffusion model) to update the Nerf MLP parameters <a class="yt-timestamp" data-t="00:36:24">[00:36:24]</a>.

One important technique to prevent degenerate solutions (where scene content is drawn onto flat geometry) is to randomly replace the Albedo color with white to produce a textureless shaded output <a class="yt-timestamp" data-t="01:11:57">[01:11:57]</a>.

## Practical Implementation Challenges
The user encountered significant "Cuda out of memory" errors when attempting to run DreamFusion on a machine with a less powerful GPU (Nvidia 1080 with 8GB memory) <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. This highlights the demanding memory requirements of these models. Attempts to mitigate this included:
*   Lowering the render width and height (e.g., from 64x64 to 32x32 or 16x16) <a class="yt-timestamp" data-t="00:50:59">[00:50:59]</a>.
*   Adjusting the `CUDA_ALLOC_CONF` environment variable to optimize memory allocation <a class="yt-timestamp" data-t="00:43:10">[00:43:10]</a>.
*   Directly modifying the code to reduce image dimensions (e.g., 512x512 to 256x256 for prompt images) <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>.

Ultimately, the limitations of the consumer-grade GPU prevented full training, as the system ran out of memory when attempting to load the Nerf model or a new batch of data during the training process <a class="yt-timestamp" data-t="01:03:54">[01:03:54]</a>.

## Future Outlook
The speaker believes that 3D [[diffusion_models_and_controlnet | diffusion models]] will be "absolutely massive" <a class="yt-timestamp" data-t="01:20:21">[01:20:21]</a>. There is significant room for improvement, such as making the Nerf MLP larger and pre-training it on millions of objects, similar to [[transformer_architecture_in_diffusion_models | Transformer]] models <a class="yt-timestamp" data-t="01:07:48">[01:07:48]</a>. This would require more powerful GPUs and further advancements in Nerf algorithms <a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a>. The vision for the future includes generating precise 3D environments simply by speaking to a VR headset <a class="yt-timestamp" data-t="01:20:27">[01:20:27]</a>.