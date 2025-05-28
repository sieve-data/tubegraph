---
title: 3D gaussian splatting for realtime radiance field rendering
videoId: xgwvU7S0K-k
---

From: [[hu-po]] <br/> 

The paper "3D Gaussian Splatting for Real-Time Radiance Field Rendering" introduces a novel method for 3D rendering that aims to overcome limitations of traditional [[Volumetric rendering and neural Radiance fields | neural Radiance Fields (NeRFs)]] <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Published on August 8, 2023, by researchers from Inria and the Max Planck Institute <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, this work claims to be faster and better than existing techniques <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Core Concept: Scene Representation with 3D Gaussians

Traditional [[Volumetric rendering and neural Radiance fields | Radiance field methods]] like [[NeRFs versus Gaussian Splatting | NeRFs]] have revolutionized novel view synthesis, allowing the creation of new images from different viewpoints of a scene captured with multiple photos or videos <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. However, achieving high visual quality with NeRFs often requires costly training and rendering using neural networks, especially for unbounded and complete scenes <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. For example, a standard NeRF might take 48 hours to train and 10 seconds per frame to render <a class="yt-timestamp" data-t="02:10:50">[02:10:50]</a>.

[[3d_gaussian_splatting_and_instant_splat_pipeline | 3D Gaussian Splatting]] offers a different approach by representing a 3D scene not as a continuous [[Volumetric rendering and neural Radiance fields | Radiance field]] learned by a neural network, but as a collection of 3D Gaussians <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. This discrete representation is claimed to preserve desirable properties of continuous volumetric fields while avoiding unnecessary computation in empty space <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>. The term "splatting" refers to the technique of projecting and spreading out these 3D Gaussians onto a 2D image plane during rendering <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

### Properties of a 3D Gaussian <a class="yt-timestamp" data-t="00:59:44">[00:59:44]</a>
Each 3D Gaussian is defined by:
*   A 3D position (mean $\mu$) <a class="yt-timestamp" data-t="00:59:46">[00:59:46]</a>
*   An opacity ($\alpha$) <a class="yt-timestamp" data-t="00:59:53">[00:59:53]</a>
*   An anisotropic covariance matrix <a class="yt-timestamp" data-t="00:59:48">[00:59:48]</a>, which describes its 3D shape and spread (like an ellipsoid, allowing for modeling fine structures) <a class="yt-timestamp" data-t="01:13:02">[01:13:02]</a>. This covariance matrix is optimized using a scaling vector and a quaternion for rotation, ensuring it remains positive semi-definite <a class="yt-timestamp" data-t="01:14:58">[01:14:58]</a>.
*   Spherical harmonic coefficients to represent its view-dependent color <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>.

## Three Key Elements of the Approach

The method's state-of-the-art visual quality and competitive training times are attributed to three main components <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>:

### 1. 3D Gaussian Scene Representation
The process begins with a sparse point cloud derived from Structure-from-Motion (SfM) camera calibration <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This initial point cloud, although noisy, seeds the positions of the 3D Gaussians <a class="yt-timestamp" data-t="02:00:02">[02:00:02]</a>. In contrast to other point-based methods that rely on multi-view stereo data for geometry, this approach achieves high quality using only SfM points <a class="yt-timestamp" data-t="02:05:06">[02:05:06]</a>.

### 2. Optimization with Adaptive Density Control
[[Goshan Splat optimization for 3D reconstruction | Optimization]] involves successive iterations of rendering and comparing the generated image to training views <a class="yt-timestamp" data-t="01:21:46">[01:21:46]</a>. This process uses Stochastic Gradient Descent (SGD) <a class="yt-timestamp" data-t="01:23:38">[01:23:38]</a> and custom CUDA kernels for efficiency <a class="yt-timestamp" data-t="01:23:44">[01:23:44]</a>.

The optimization includes adaptive density control of the Gaussians <a class="yt-timestamp" data-t="01:29:57">[01:29:57]</a>:
*   **Pruning**: Transparent or inconsequential Gaussians are removed periodically (e.g., every 100 iterations) <a class="yt-timestamp" data-t="01:31:58">[01:31:58]</a>.
*   **Cloning**: In under-reconstructed areas (identified by large positional gradients), Gaussians are cloned and moved in the direction of the gradient <a class="yt-timestamp" data-t="01:34:50">[01:34:50]</a>.
*   **Splitting**: Large Gaussians in regions with high variance are split into two smaller Gaussians to capture finer details <a class="yt-timestamp" data-t="01:35:04">[01:35:04]</a>.

The loss function combines an L1 loss (pixel-wise difference) with a structural similarity index (SSIM) <a class="yt-timestamp" data-t="01:27:32">[01:27:32]</a>. The optimization also utilizes specific "tricks," such as warming up computation in lower resolution and gradually introducing spherical harmonic bands <a class="yt-timestamp" data-t="02:06:24">[02:06:24]</a>.

### 3. Fast Differentiable Rasterizer
This is a critical component for achieving real-time performance. The rasterizer is tile-based, meaning it splits the screen into small regions (e.g., 16x16 pixels) <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. It efficiently sorts 3D Gaussians based on their view-space depth and tile ID using a single fast GPU Radix sort <a class="yt-timestamp" data-t="01:43:03">[01:43:03]</a>. This pre-sorting for the entire image avoids the expense of per-pixel sorting <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>.

The rasterizer supports anisotropic splatting and allows gradients to be propagated to an arbitrary number of blended Gaussians during the backward pass, crucial for optimization <a class="yt-timestamp" data-t="01:40:39">[01:40:39]</a>. By tracking accumulated Alpha values and performing both front-to-back and back-to-front traversals, it minimizes memory consumption and speeds up gradient computation <a class="yt-timestamp" data-t="01:54:15">[01:54:15]</a>.

## [[Comparison of 3D gaussian splatting to neural radiance fields | Comparisons]] and [[Gaussian splatting and its advantages | Advantages]]

The paper presents compelling evidence for the efficacy of [[3d_gaussian_splatting_and_instant_splat_pipeline | 3D Gaussian Splatting]] over existing methods:

### Quality
Qualitatively, [[3d_gaussian_splatting_and_instant_splat_pipeline | 3D Gaussian Splatting]] produces sharper images with fewer artifacts like blurriness or "NeRF fuzz" compared to [[NeRFs versus Gaussian Splatting | NeRFs]] and even [[Comparisons between Gaussian splats and other 3D representation technologies | state-of-the-art NeRF variants]] like MIP-NeRF 360 and Instant NGP <a class="yt-timestamp" data-t="01:59:01">[01:59:01]</a>. It excels at reconstructing fine details, such as bicycle spokes or distant window frames <a class="yt-timestamp" data-t="01:59:54">[01:59:54]</a>.

Quantitatively, the method achieves superior PSNR and SSIM scores across various datasets <a class="yt-timestamp" data-t="02:09:55">[02:09:55]</a>.

### Speed
*   **Training Time**: [[3d_gaussian_splatting_and_instant_splat_pipeline | 3D Gaussian Splatting]] achieves state-of-the-art quality with significantly reduced training times, around 35-45 minutes, compared to 48 hours for MIP-NeRF 360 <a class="yt-timestamp" data-t="02:10:50">[02:10:50]</a>. It is also competitive with faster methods like Instant NGP, which can train in ~7 minutes <a class="yt-timestamp" data-t="02:01:14">[02:01:14]</a>.
*   **Rendering Speed**: The method enables real-time rendering, achieving display rates at 1080p resolution that no previous method could <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This is largely due to its efficient, GPU-accelerated rasterization pipeline <a class="yt-timestamp" data-t="01:19:31">[01:19:31]</a>.

### Memory Consumption
A notable trade-off is the memory footprint. While [[NeRFs versus Gaussian Splatting | NeRFs]] are very compact (e.g., Instant NGP at 8-13 MB) <a class="yt-timestamp" data-t="02:03:03">[02:03:03]</a>, [[3d_gaussian_splatting_and_instant_splat_pipeline | 3D Gaussian Splatting]] models require substantially more memory. A final scene representation can range from 200,000 to 500,000 Gaussians <a class="yt-timestamp" data-t="02:11:46">[02:11:46]</a>, leading to model sizes of 734 MB <a class="yt-timestamp" data-t="02:13:19">[02:13:19]</a>. During training of large scenes, peak GPU memory consumption can exceed 20 GB <a class="yt-timestamp" data-t="02:23:45">[02:23:45]</a>.

## Limitations and [[Implications of Gaussian splatting in future technologies | Future Work]]

Despite its advancements, the method has limitations:
*   **Unobserved Regions**: Artifacts can appear in areas of the scene not well-observed during capture <a class="yt-timestamp" data-t="02:20:56">[02:20:56]</a>.
*   **Elongated/Splotchy Artifacts**: The anisotropic Gaussians can sometimes create elongated or "splotchy" artifacts <a class="yt-timestamp" data-t="02:21:09">[02:21:09]</a>.
*   **Popping Artifacts**: Sudden appearance or disappearance of large Gaussians ("popping") can occur, especially in view-dependent appearance regions, partly due to the "guard band" used for Gaussian rejection <a class="yt-timestamp" data-t="02:21:40">[02:21:40]</a>.
*   **Hyperparameter Tuning**: The optimization process involves several hard-coded hyperparameters and sequential steps (e.g., progressive resolution increase, gradual spherical harmonic introduction), which might require scene-specific tuning <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.
*   **Memory Consumption**: The high memory usage remains a challenge <a class="yt-timestamp" data-t="02:23:37">[02:23:37]</a>.

Future work directions include:
*   Improving memory efficiency through careful low-level implementation (e.g., porting more Python code to CUDA) or adopting point cloud compression techniques <a class="yt-timestamp" data-t="02:23:57">[02:23:57]</a>.
*   Addressing anti-aliasing to mitigate popping artifacts <a class="yt-timestamp" data-t="02:22:16">[02:22:16]</a>.
*   Exploring [[Dynamic 3D Gaussian technique | dynamic scenes]] with time-varying components <a class="yt-timestamp" data-t="02:44:26">[02:44:26]</a>.
*   Investigating the use of Gaussians for mesh reconstruction, which is crucial for integration into traditional graphics pipelines like video games <a class="yt-timestamp" data-t="02:27:22">[02:27:22]</a>.

In conclusion, [[3d_gaussian_splatting_and_instant_splat_pipeline | 3D Gaussian Splatting]] presents a significant step towards real-time, high-quality [[Volumetric rendering and neural Radiance fields | radiance field rendering]] by demonstrating that a continuous scene representation is not strictly necessary for such performance <a class="yt-timestamp" data-t="02:25:54">[02:25:54]</a>.