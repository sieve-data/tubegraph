---
title: Applications and Limitations of Monocular Depth
videoId: WoiI_Pn9yHw
---

From: [[hu-po]] <br/> 

[[Applications and limitations of 3D Gaussians | Monocular depth estimation]] is a fundamental computer vision task that involves recovering 3D depth information from a single 2D image [00:09:37]. This problem is geometrically ill-posed and requires robust scene understanding [00:09:41].

## Core Concepts

*   **Depth Image**: A single-channel image where each pixel's value represents the distance from the camera to that specific point in the scene [00:04:19]. Values typically range from -1 to 1 or 0 to 1 [00:04:44]. For visualization, these are often recolored (e.g., blue for far, red for close) [00:04:52].
*   **Monocular**: Refers to performing depth estimation using just one image or a single shot [00:05:16]. This contrasts with older methods that leveraged [[camera_intrinsics_and_extrinsics_in_computer_vision | camera geometry]] and stereo or multi-view setups [00:05:33].
*   **Dense Structured Regression Task**: Involves predicting a depth value for every single pixel in the image (dense) [01:20:21], where the value is continuous (regression) [00:20:49].

## The Rise of Deep Learning

Deep learning has significantly advanced [[applications_and_limitations_of_3d_gaussians | monocular depth estimation]], with models evolving from modest CNNs to large Transformer architectures [00:10:44]. However, these models traditionally struggle with unfamiliar or out-of-distribution content if their training data is limited [00:11:06].

## Key Papers

Two recent papers, both published on December 4, 2023, highlight different approaches and capabilities in [[monocular_depth_estimation_using_diffusion_models | monocular depth estimation]]:

### Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation

This paper, from ETH Zurich, explores leveraging the extensive priors captured in recent generative [[monocular_depth_estimation_using_diffusion_models | diffusion models]] to achieve more generalizable depth estimation [00:12:22].

#### How Marigold Works

*   **Leveraging Pre-trained Models**: Marigold repurposes [[monocular_depth_estimation_using_diffusion_models | Stable Diffusion]] V2, which has been trained on internet-scale datasets like LAION-5B (five billion images) [01:05:21]. This provides a strong "world model" of visual information [01:06:03].
*   **Fine-tuning Protocol**:
    *   **Frozen VAE**: The variational autoencoder (VAE) encoder and decoder components of [[monocular_depth_estimation_using_diffusion_models | Stable Diffusion]] are kept frozen (unchanged) [00:31:51].
    *   **Encoding Depth Images**: Surprisingly, depth images (which are single-channel) are replicated across three channels to simulate an RGB image and then encoded by this VAE, which was only trained on real images [00:33:55]. This "magically works" despite depth images being out-of-distribution for the VAE's original training [00:34:01].
    *   **Denoising UNet Adaptation**: The core denoising UNet, which is the actual diffusion model, is fine-tuned [01:37:30]. To accommodate the concatenated input of the encoded RGB image and the encoded depth image, the input channels of the UNet are doubled, and the initial weights are divided by two to prevent activation magnitude inflation [00:38:27].
    *   **Synthetic Data Training**: Marigold is fine-tuned for a couple of days on a single consumer GPU using only [[comparison_of_synthetic_and_real_depth_data | synthetic training data]] (Hypersim and Virtual KITTI) [01:09:01]. This is because synthetic depth data is inherently dense and has perfect ground truth, unlike real sensor data which often contains missing values or artifacts [01:01:00].
*   **Inference Process**:
    1.  The input RGB image is encoded into a latent representation using the frozen VAE encoder [00:52:58].
    2.  A pure noise latent variable is sampled [00:53:11].
    3.  The encoded RGB latent and the noise latent are concatenated and iteratively denoised by the fine-tuned UNet [00:53:30]. The UNet is conditioned only on the time step [00:53:50].
    4.  The resulting denoised latent depth is decoded by the frozen VAE decoder [00:54:14].
    5.  Since the decoder outputs three channels, these are averaged to produce the final single-channel depth map [00:54:58].
*   **Performance Enhancements**:
    *   **Affine Invariant Normalization**: The ground truth depth maps are linearly normalized to a range of -1 to 1 [00:42:32]. This means the model learns *affine invariant* depth, preserving relative distances but losing the true metric scale (e.g., meters) [00:14:23].
    *   **Non-Markovian Sampling (DDIM)**: Marigold uses DDIM (Denoising Diffusion Implicit Models) which allows for accelerated inference by skipping steps in the denoising process [00:56:45].
    *   **Test-Time Ensembling**: Multiple inference passes (e.g., 10-20) are run with different initial noise samples, and the median of the resulting depth maps is taken [01:01:46]. This significantly reduces error [01:09:18].

#### Marigold's Advantages

*   **State-of-the-Art Performance**: Marigold achieves state-of-the-art results across various datasets, often outperforming previous methods by over 20% [01:05:59].
*   **High Quality**: Produces very clean and detailed depth maps, even for fine features like fur or intricate building details [00:06:58].
*   **Generalizability**: Due to the strong prior knowledge from internet-scale training, it generalizes well to images with unfamiliar content [00:12:22].
*   **Resource Efficiency**: Fine-tuning is relatively fast and can be done on consumer-grade GPUs [01:11:14].

#### Marigold's Limitations

*   **Affine Invariant Depth**: The primary limitation is that it outputs affine invariant depth, not true metric depth [00:14:23]. This means it tells you that one pixel is closer than another, but not the exact physical distance in meters [00:14:29]. For applications like [[duster_and_multiview_stereo_reconstruction | SLAM]] or [[3d_representations_and_their_applications | 3D reconstruction]] that require absolute distances, an additional step would be needed to infer the true scale [01:32:01].
*   **Inference Speed**: While DDIM helps, the iterative denoising process and test-time ensembling still make inference slower than single-pass methods [01:10:07]. This can be a bottleneck for real-time applications like autonomous driving [01:10:47].

### PatchFusion: An End-to-End Tile-Based Framework for High-Resolution Monocular Metric Depth Estimation

This paper, from King Abdullah University of Science and Technology, focuses on high-resolution [[monocular_depth_estimation_using_diffusion_models | monocular depth estimation]] for consumer cameras [01:13:16].

#### How PatchFusion Works

*   **Tile-Based Processing**: The core idea is to divide a high-resolution input image into multiple overlapping patches [01:16:01].
*   **Independent Processing**: Each patch is processed independently by a depth estimation model [01:16:01].
*   **Fusion**: The individual depth predictions from each patch are then fused, using overlapping regions to enforce consistency and align the relative depths [01:15:22].

#### PatchFusion's Advantages

*   **High Detail**: Can produce incredibly detailed depth maps due to processing at a patch level [01:17:13].

#### PatchFusion's Limitations

*   **Computational Overhead**: Processing many overlapping patches independently is computationally intensive [01:17:21].
*   **Lack of Global Context**: Patch-wise processing inherently suffers from a lack of global information, which needs to be compensated for during fusion [01:15:08].
*   **Outdated Architecture**: The paper uses [[Patchbased Depth Estimation Techniques | CNN-based architectures]] and trains models from scratch, which is less efficient and powerful than leveraging large pre-trained diffusion models [01:17:51].

## Broader Implications and Future Directions

The significant advancements in [[monocular_depth_estimation_using_diffusion_models | monocular depth estimation]], particularly with models like Marigold, suggest a future where dedicated depth sensors (such as LiDAR or structured light sensors) may become obsolete [01:06:06].

*   **Limitations of Traditional Depth Sensors**: Real-world depth sensors often produce noisy data with missing values, artifacts, and sensitivity to material properties (e.g., reflective surfaces, shadows) [01:06:35]. This makes their "ground truth" less clean than synthetic data [00:50:51].
*   **Cost-Effectiveness**: Obtaining depth from a standard RGB camera and a monocular depth estimation model is significantly cheaper and easier than purchasing and integrating expensive specialized depth sensors [01:08:02].
*   **Potential for Hybrid Approaches**: A promising research direction involves combining the strengths of Marigold and PatchFusion:
    *   Take Marigold's state-of-the-art generalizable depth estimation.
    *   Apply a patching strategy (like PatchFusion) to process high-resolution images, feeding individual patches into Marigold's pipeline [01:18:28].
    *   Fuse the results to gain both high fidelity and global consistency.
*   **Speeding Up Inference**: Further research could focus on integrating techniques like [[finetuning_pretrained_models_for_depth_estimation | Latent Consistency Models]] (LCMs) to drastically reduce the number of inference steps required for diffusion models, making monocular depth estimation viable for real-time applications [01:42:42].

The progress in 2D to 3D reconstruction is rapidly changing various fields, leading to significant disruption for companies and professionals involved in traditional hardware sensor development [01:08:51].