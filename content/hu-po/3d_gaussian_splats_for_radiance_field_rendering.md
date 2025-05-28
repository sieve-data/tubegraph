---
title: 3D Gaussian Splats for Radiance Field Rendering
videoId: xgwvU7S0K-k
---

From: [[hu-po]] <br/> 

The paper "3D Gaussian Splatting for Real-Time Radiance Field Rendering" introduces a novel approach to [[3d_content_generation_using_gaussian_splatting | 3D content generation]] and rendering that aims to overcome the limitations of existing methods, particularly [[3d_representation_techniques_nerfs_vs_gausssian_splats | Neural Radiance Fields (NeRFs)]] <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This technique has gained significant attention for offering a different way of doing [[3d_content_generation_using_gaussian_splatting | 3D rendering]] <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Core Innovation

Traditional [[3d_representation_techniques_nerfs_vs_gausssian_splats | NeRFs]] represent scenes as continuous radiance fields, typically learned by neural networks, which are computationally expensive to train and render <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. The key idea behind 3D Gaussian Splatting is to represent a scene not as an implicit neural field, but as a discrete set of trainable 3D gaussians <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>, <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. This approach aims to achieve state-of-the-art visual quality with competitive training times and real-time novel view synthesis <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## How it Works

The method is built upon three main components:

### 1. [[3D Modeling and Tracking Using Gaussian Splatting | 3D Gaussian Scene Representation]]

Instead of a continuous radiance field, the scene is represented by a collection of 3D gaussians <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. These gaussians are initialized from sparse point clouds, which are typically produced from camera calibration using Structure-from-Motion (SfM) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>, <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>.

Each 3D gaussian is defined by:
*   A 3D position (mean, µ) <a class="yt-timestamp" data-t="00:59:44">[00:59:44]</a>, <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   An opacity (alpha, α) <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>.
*   An anisotropic covariance matrix (Σ) <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>, <a class="yt-timestamp" data-t="00:59:48">[00:59:48]</a>. This allows the gaussians to stretch and rotate, adapting to the geometry of different shapes, which helps represent fine structures compactly <a class="yt-timestamp" data-t="01:00:39">[01:00:39]</a>, <a class="yt-timestamp" data-t="01:13:58">[01:13:58]</a>.
*   Spherical harmonic coefficients for directional appearance (color) <a class="yt-timestamp" data-t="00:59:56">[00:59:56]</a>, <a class="yt-timestamp" data-t="01:00:58">[01:00:58]</a>.

The use of 3D gaussians provides a differentiable volumetric representation that can be efficiently projected into 2D "splats" for rendering <a class="yt-timestamp" data-t="01:04:07">[01:04:07]</a>.

### 2. Optimization with Adaptive Density Control

The process involves optimizing the properties of these 3D gaussians using Stochastic Gradient Descent (SGD) <a class="yt-timestamp" data-t="01:23:38">[01:23:38]</a>. This is interleaved with steps that adaptively control the number and density of gaussians <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>, <a class="yt-timestamp" data-t="01:27:57">[01:27:57]</a>.

*   **Initialization**: Begins with sparse point clouds from SfM <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>.
*   **Optimization Cycle**: Render an image from the current 3D gaussian representation, compare it to the ground truth image using a combined L1 and [[comparison_of_gaussian_splats_and_neural_radiance_fields_nerfs | DSSIM]] loss, and then backpropagate gradients to update gaussian parameters <a class="yt-timestamp" data-t="01:21:44">[01:21:44]</a>, <a class="yt-timestamp" data-t="01:29:19">[01:29:19]</a>.
*   **Density Control**:
    *   **Pruning**: Transparent gaussians (low opacity) are removed every 100 iterations <a class="yt-timestamp" data-t="01:31:58">[01:31:58]</a>.
    *   **Cloning and Splitting**: Gaussians in under-reconstructed areas (identified by large positional gradients) are cloned and moved <a class="yt-timestamp" data-t="01:34:01">[01:34:01]</a>. Large gaussians in regions with high variance are split into two smaller ones <a class="yt-timestamp" data-t="01:35:03">[01:35:03]</a>. This allows the system to create new geometry and refine existing geometry <a class="yt-timestamp" data-t="01:22:15">[01:22:15]</a>.
    *   **Challenges**: [[Challenges and solutions in representing 3D objects with gaussian splatting | Handling constraints on covariance matrices]] (must be positive semi-definite) is addressed by optimizing separate scaling and rotation matrices which can then be converted to a valid covariance matrix <a class="yt-timestamp" data-t="01:13:18">[01:13:18]</a>, <a class="yt-timestamp" data-t="01:14:58">[01:14:58]</a>.

### 3. Fast Differentiable Rendering

This is crucial for achieving real-time performance. The method employs a tile-based rasterizer for gaussian splats, inspired by recent software rasterization approaches <a class="yt-timestamp" data-t="01:39:58">[01:39:58]</a>, <a class="yt-timestamp" data-t="01:40:01">[01:40:01]</a>.

*   **Tile-based Processing**: The screen is split into 16x16 pixel tiles <a class="yt-timestamp" data-t="01:41:04">[01:41:04]</a>.
*   **GPU Sorting**: Gaussians are pre-sorted once per frame using a fast GPU Radix sort <a class="yt-timestamp" data-t="01:41:16">[01:41:16]</a>, <a class="yt-timestamp" data-t="01:43:22">[01:43:22]</a>. This avoids the expense of sorting per pixel and allows for efficient Alpha blending that respects visibility order <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>, <a class="yt-timestamp" data-t="01:40:54">[01:40:54]</a>.
*   **Parallel Accumulation**: Threads within each tile collaboratively load gaussians and accumulate colors and alpha values, stopping when a target saturation is reached (similar to [[3d_representation_techniques_nerfs_vs_gausssian_splats | NeRFs]]' ray marching stopping criterion) <a class="yt-timestamp" data-t="01:46:50">[01:46:50]</a>.
*   **Differentiability**: The entire rasterization pipeline is fully differentiable, allowing gradients to be backpropagated through it to update the gaussian parameters <a class="yt-timestamp" data-t="01:40:46">[01:40:46]</a>.

## [[Comparison Between Gaussian Splats and Traditional 3D Representation Methods | Comparison with Existing Methods]]

The paper presents comparisons primarily against [[3d_representation_techniques_nerfs_vs_gausssian_splats | NeRFs]] and other fast radiance field methods like Instant-NGP and Plenoxels.

*   **Training Time**: The method achieves state-of-the-art quality with competitive training times, often in minutes compared to hours for [[3d_representation_techniques_nerfs_vs_gausssian_splats | NeRFs]] <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>, <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>, <a class="yt-timestamp" data-t="02:10:48">[02:10:48]</a>. For example, 3D Gaussian Splatting can train a scene in 35-45 minutes compared to 48 hours for [[3d_representation_techniques_nerfs_vs_gausssian_splats | NeRFs]] <a class="yt-timestamp" data-t="02:10:48">[02:10:48]</a>.
*   **Rendering Speed**: It enables real-time rendering, unlike many previous methods that struggled to achieve real-time display rates for 1080p resolution <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>, <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>. Rendering time for [[3d_representation_techniques_nerfs_vs_gausssian_splats | NeRFs]] could be 10 seconds per frame, while 3D Gaussian Splatting offers comparable quality in real-time (e.g., five to ten minutes of training) <a class="yt-timestamp" data-t="02:10:52">[02:10:52]</a>, <a class="yt-timestamp" data-t="02:10:58">[02:10:58]</a>.
*   **Visual Quality**: The visual results demonstrate higher fidelity in fine details (e.g., bicycle spokes) and less blurriness or "Nerf fuzz" compared to [[3d_representation_techniques_nerfs_vs_gausssian_splats | NeRFs]] <a class="yt-timestamp" data-t="01:58:50">[01:58:50]</a>, <a class="yt-timestamp" data-t="01:59:11">[01:59:11]</a>. Quantitative metrics like PSNR and SSIM generally show superior performance <a class="yt-timestamp" data-t="02:09:41">[02:09:41]</a>.
*   **Memory Footprint**: While smaller than some [[comparison_between_gaussian_splats_and_traditional_3d_representation_methods | explicit scene representations]] like Plenoxels, 3D Gaussian Splatting requires significantly more memory than [[3d_representation_techniques_nerfs_vs_gausssian_splats | NeRFs]]. A single scene can consume 734 MB, compared to 8-13 MB for [[3d_representation_techniques_nerfs_vs_gausssian_splats | NeRFs]] <a class="yt-timestamp" data-t="02:01:18">[02:01:18]</a>, <a class="yt-timestamp" data-t="02:13:12">[02:13:12]</a>, <a class="yt-timestamp" data-t="02:13:22">[02:13:22]</a>. This is due to storing parameters for millions of gaussians (e.g., up to 500,000 per scene) <a class="yt-timestamp" data-t="02:11:46">[02:11:46]</a>.

## [[Challenges and Solutions in Representing 3D Objects with Gaussian Splatting | Limitations and Future Work]]

Despite its advancements, 3D Gaussian Splatting has [[challenges_and_solutions_in_representing_3d_objects_with_gaussian_splatting | limitations]]:
*   **Artifacts**: Regions that are not well-observed can still have artifacts <a class="yt-timestamp" data-t="02:20:56">[02:20:56]</a>.
*   **Elongated/Splotchy Gaussians**: The anisotropic gaussians can sometimes create elongated artifacts or splotchy appearances <a class="yt-timestamp" data-t="02:21:08">[02:21:08]</a>.
*   **Popping Artifacts**: Sudden appearance or disappearance of large gaussians when changing viewpoints can occur, partly due to the "guard band" rejection in the rasterizer <a class="yt-timestamp" data-t="02:21:18">[02:21:18]</a>, <a class="yt-timestamp" data-t="02:21:47">[02:21:47]</a>.
*   **Hyperparameter Tuning**: The optimization process involves several hard-coded hyperparameters for density control (e.g., transparency thresholds, scaling factors for splitting) <a class="yt-timestamp" data-t="01:35:12">[01:35:12]</a>, <a class="yt-timestamp" data-t="01:36:31">[01:36:31]</a>.
*   **Memory Consumption**: While efficient for rendering, the explicit representation can lead to high GPU memory consumption during training (e.g., exceeding 20 GB) <a class="yt-timestamp" data-t="02:23:43">[02:23:43]</a>.
*   **Static Scenes**: Like [[3d_gaussian_splatting_and_nerfs | NeRFs]], the current method is designed for static scenes, not dynamic ones with time-varying components <a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>, <a class="yt-timestamp" data-t="02:44:19">[02:44:19]</a>.

Future work directions include addressing artifacts, improving memory efficiency (e.g., with compression techniques), and potentially using gaussians for mesh reconstruction <a class="yt-timestamp" data-t="02:29:27">[02:29:27]</a>, <a class="yt-timestamp" data-t="02:42:58">[02:42:58]</a>.

## Conclusion

3D Gaussian Splatting presents a compelling alternative to [[3d_gaussian_splatting_and_nerfs | NeRFs]] for [[3d_content_generation_using_gaussian_splatting | radiance field rendering]] by leveraging a discrete, explicit representation of 3D gaussians <a class="yt-timestamp" data-t="02:55:54">[02:55:54]</a>. Its ability to achieve high visual quality, competitive training times, and real-time rendering marks a significant step forward in novel view synthesis. While memory consumption is a drawback, the method's efficiency in GPU utilization and its distinct approach to scene representation open up new avenues for [[physicsbased_modeling_in_gaussian_splats | 3D graphics]] and [[gaussian_splats_in_robotics | computer vision]].