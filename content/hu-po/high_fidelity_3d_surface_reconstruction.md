---
title: High Fidelity 3D surface reconstruction
videoId: ccGxQCpbrnM
---

From: [[hu-po]] <br/> 

Neuralangelo is a framework developed by Nvidia Research and Johns Hopkins University for achieving [[High Fidelity 3D surface reconstruction | high-fidelity 3D surface reconstruction]] from standard [[camera setup for 3D scene capture | RGB images]] <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. It stands out by performing this reconstruction without requiring auxiliary data like segmentation or explicit depth information <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>, <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Core Concepts and Techniques

Neuralangelo's approach is built upon several key components:

### 3D Surface Reconstruction
At its core, [[High Fidelity 3D surface reconstruction | 3D surface reconstruction]] aims to create a [[3D mesh generation with AI | mesh]], which is composed of triangles with vertices and connecting edges, from a series of 2D images <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, <a class="yt-timestamp" data-t="00:10:49">[10:49]</a>. The input `RGB images` are standard full-color images, similar to those captured by a cell phone <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The framework can process `RGB videos`, which are considered a series of RGB images <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Neural Volume Rendering
A central technique is [[3D modeling and tracking using Gaussian splatting | neural volume rendering]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This involves using neural networks, specifically [[techniques for text to 3D conversion involving diffusion models | Neural Radiance Fields (NeRFs)]], to render a 3D volume <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, <a class="yt-timestamp" data-t="00:30:43">[30:43]</a>. A `NeRF` encodes a 3D scene within a multi-layer perceptron (MLP), mapping 3D spatial locations to color and volume density <a class="yt-timestamp" data-t="00:31:00">[31:00]</a>. This allows for photorealistic view synthesis without an explicit mesh <a class="yt-timestamp" data-t="00:32:34">[32:34]</a>. However, `NeRFs` can struggle with clearly defined surfaces, leading to noisy or fuzzy results <a class="yt-timestamp" data-t="00:35:17">[35:17]</a>, <a class="yt-timestamp" data-t="00:35:58">[35:58]</a>.

### Multi-resolution 3D Hash Grids
Neuralangelo leverages [[duster_and_its_applications_in_3d_reconstruction | multi-resolution 3D hash grids]], a concept pioneered by Nvidia's `Instant NGP` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>, <a class="yt-timestamp" data-t="00:18:41">[18:41]</a>. A hash grid acts like a 3D table, mapping 3D positions to stored values <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. "Multi-resolution" means there are multiple grids of different sizes (e.g., coarse, fine, extra-fine), allowing for varying levels of detail <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>, <a class="yt-timestamp" data-t="01:01:01">[1:01:01]</a>. Features across these 16 different grid resolutions are concatenated and fed into an MLP <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>, <a class="yt-timestamp" data-t="01:04:49">[01:04:49]</a>.

### Signed Distance Functions (SDFs)
To address the surface definition problem of `NeRFs`, Neuralangelo integrates [[comparative_analysis_of_3d_representation_techniques | Signed Distance Functions (SDFs)]] <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>, <a class="yt-timestamp" data-t="00:54:59">[54:59]</a>. An SDF represents a surface as the set of all points where the function's value is zero <a class="yt-timestamp" data-t="00:55:25">[00:55:25]</a>. Positive values mean outside the surface, negative mean inside <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>. This provides a more explicit surface representation compared to `NeRF`'s volume density <a class="yt-timestamp" data-t="00:37:37">[37:37]</a>.

### Numerical Gradients for Higher-Order Derivatives
A key innovation is the use of `numerical gradients` to compute `higher order derivatives` (derivatives beyond the first) <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>, <a class="yt-timestamp" data-t="00:50:50">[50:50]</a>. Unlike analytical gradients, which are exact, numerical gradients provide approximations by sampling points around the function <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, <a class="yt-timestamp" data-t="01:30:06">[1:30:06]</a>. This is crucial because analytical gradients of hash encodings are discontinuous across space due to tri-linear interpolation, limiting back-propagation updates to local hash grid cells <a class="yt-timestamp" data-t="01:15:48">[1:15:48]</a>, <a class="yt-timestamp" data-t="01:22:01">[1:22:01]</a>. By sampling points in nearby cells (e.g., six additional SDF samples in 3D space for normal computation <a class="yt-timestamp" data-t="01:35:06">[1:35:06]</a>), numerical gradients distribute updates beyond local cells, acting as a smoothing operation and promoting consistency across the surface <a class="yt-timestamp" data-t="01:25:27">[1:25:27]</a>, <a class="yt-timestamp" data-t="01:32:28">[1:32:28]</a>. This avoids the need for additional networks seen in other approaches <a class="yt-timestamp" data-t="01:28:49">[1:28:49]</a>.

### Course-to-Fine Optimization
Neuralangelo employs a [[limitations_and_assumptions_of_dynamic_3d_modeling | course-to-fine optimization]] schedule <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>, <a class="yt-timestamp" data-t="00:21:46">[21:46]</a>. This means the optimization starts with coarser hash grid resolutions and progressively activates finer ones over time, typically adding a new hash resolution every 5,000 iterations <a class="yt-timestamp" data-t="01:41:51">[1:41:51]</a>. This strategy helps avoid falling into undesirable local minima in the loss landscape <a class="yt-timestamp" data-t="01:36:17">[1:36:17]</a>. The step size for numerical gradients is initially large, matching the coarsest grid, and exponentially decreases as finer grids are introduced <a class="yt-timestamp" data-t="01:40:44">[1:40:44]</a>. This progressive refinement also naturally enables [[3d_scene_representation_and_simulation | Level of Detail (LOD)]] for the reconstructed assets <a class="yt-timestamp" data-t="02:00:20">[2:00:20]</a>.

### Regularization
To further enhance surface quality, Neuralangelo uses two regularization terms in its total loss function:
*   **Iconal Regularization:** This loss term enforces the `iconal equation`, which states that the magnitude of the SDF gradient should be approximately one everywhere <a class="yt-timestamp" data-t="01:02:14">[1:02:14]</a>, <a class="yt-timestamp" data-t="01:10:17">[1:10:17]</a>. This helps ensure the neural representation produces a valid SDF <a class="yt-timestamp" data-t="01:10:59">[1:10:59]</a>.
*   **Mean Curvature Regularization:** This term promotes smoothness by regularizing the mean curvature of the SDF <a class="yt-timestamp" data-t="01:44:09">[1:44:09]</a>. Initially, the strength of this loss is very small and is linearly increased during the training process, balancing smoothness with capturing fine details that might be inherently sharp (e.g., bricks) <a class="yt-timestamp" data-t="02:03:31">[2:03:31]</a>.

> [!NOTE] Differentiability
> A key challenge for neural networks is that many operations, like rounding, are non-differentiable, which hinders gradient-based optimization <a class="yt-timestamp" data-t="01:18:26">[1:18:26]</a>. Numerical gradients provide a workaround by approximating the derivative through sampling <a class="yt-timestamp" data-t="01:30:06">[1:30:06]</a>.

## Experimental Validation

Neuralangelo was evaluated on several datasets:
*   **DTU Dataset:** Contains 15 object-centric scenes with 49 to 64 images captured by a robot-held monocular RGB camera, providing highly accurate camera positions. Ground truth was obtained from a structured light scanner <a class="yt-timestamp" data-t="01:46:47">[1:46:47]</a>.
*   **Tanks and Temples Dataset:** Features six large-scale indoor and outdoor scenes with 263 to 1107 images captured using a handheld monocular RGB camera (less accurate camera positions but more images). Ground truth was obtained using a lidar sensor <a class="yt-timestamp" data-t="01:48:25">[1:48:25]</a>.

The performance was measured using:
*   **Chamfer Distance** and **F1 Score** for surface evaluation <a class="yt-timestamp" data-t="01:52:10">[1:52:10]</a>.
*   **Peak Signal-to-Noise Ratio (PSNR)** for image synthesis quality <a class="yt-timestamp" data-t="01:52:17">[1:52:17]</a>.

Neuralangelo consistently achieved superior `reconstruction accuracy` and `view synthesis quality` compared to previous methods like `NeRF`, `Volume SDF`, and `Neural Warp` <a class="yt-timestamp" data-t="01:56:39">[1:56:39]</a>. For example, `Neural Warp` sometimes predicts surfaces for the sky and background, which Neuralangelo avoids <a class="yt-timestamp" data-t="01:59:12">[1:59:12]</a>.

## [[Challenges and limitations in 3D generation | Limitations and Future Work]]

A current limitation of Neuralangelo is its reliance on long training iterations due to random pixel sampling from input images <a class="yt-timestamp" data-t="02:05:29">[2:05:29]</a>. Future work aims to explore more efficient sampling strategies to accelerate the training process <a class="yt-timestamp" data-t="02:06:06">[2:06:06]</a>. The paper also does not disclose specific details regarding the computational resources (e.g., type and number of GPUs, training time) used for its development <a class="yt-timestamp" data-t="02:07:03">[2:07:03]</a>.