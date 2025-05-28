---
title: Optimization and adaptive density control of 3D gaussians
videoId: xgwvU7S0K-k
---

From: [[hu-po]] <br/> 

The core of the [[goshan_splat_optimization_for_3d_reconstruction | 3D Gaussian Splatting]] method involves the optimization and adaptive density control of 3D Gaussians to accurately represent a scene for novel view synthesis <a class="yt-timestamp" data-t="01:20:27">[01:20:27]</a>. This process aims to create a dense set of 3D Gaussians that can accurately represent a scene for free-view synthesis <a class="yt-timestamp" data-t="01:29:29">[01:29:29]</a>.

## Initialization of 3D Gaussians
The process begins with a sparse point cloud generated during camera calibration using [[goshan_splat_optimization_for_3d_reconstruction | Structure from Motion (SfM)]] <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. This sparse point cloud introduces noise and is not perfect, a challenge inherited by both [[comparison_of_3d_gaussian_splatting_to_neural_radiance_fields | Neural Radiance Fields (Nerfs)]] and this method <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>, <a class="yt-timestamp" data-t="01:37:51">[01:37:51]</a>. Initially, the 3D Gaussians are placed at these SfM points <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. The initial covariance (spread) of these Gaussians is set as an isotropic Gaussian, with axes equal to the mean distance to the three closest points in the SfM data <a class="yt-timestamp" data-t="02:44:40">[02:44:40]</a>. For synthetic datasets, high quality can be achieved even with random initialization of Gaussians <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

## Optimized Properties of 3D Gaussians
The optimization process adjusts several properties for each 3D Gaussian:
*   **3D Position (Mean)**: The central point of the Gaussian in 3D space <a class="yt-timestamp" data-t="00:59:44">[00:59:44]</a>.
*   **Opacity (Alpha)**: Determines how transparent or opaque each Gaussian is <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>. A sigmoid activation function is used for Alpha to keep values in the 0-1 range <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.
*   **Anisotropic Covariance Matrix**: Describes the spread and orientation of the Gaussian in 3D space <a class="yt-timestamp" data-t="00:59:48">[00:59:48]</a>.
    *   Instead of directly optimizing the covariance matrix (which must be positive semi-definite and is hard to constrain with gradient descent), it's represented by a scaling vector (s) and a quaternion (q) for rotation <a class="yt-timestamp" data-t="01:13:58">[01:13:58]</a>. This allows for independent optimization of scaling and rotation <a class="yt-timestamp" data-t="01:14:58">[01:14:58]</a>. An exponential activation function is used for the scale of the covariance <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
    *   This anisotropic nature (directionally dependent properties) is crucial for accurately representing fine structures like bicycle spokes or wires <a class="yt-timestamp" data-t="01:00:39">[01:00:39]</a>, <a class="yt-timestamp" data-t="01:54:55">[01:54:55]</a>.
*   **Spherical Harmonic Coefficients**: Represent the view-dependent color of each Gaussian <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>. These are introduced gradually during optimization; initially, only the zero-order component is optimized, with higher bands introduced later <a class="yt-timestamp" data-t="02:07:05">[02:07:05]</a>. This helps compensate for angular regions missing information in captures <a class="yt-timestamp" data-t="02:07:05">[02:07:05]</a>.

## Optimization Algorithm
The optimization uses Stochastic Gradient Descent (SGD) within a PyTorch framework, leveraging custom CUDA kernels for speed <a class="yt-timestamp" data-t="02:39:41">[02:39:41]</a>, <a class="yt-timestamp" data-t="02:44:50">[02:44:50]</a>. The core of the optimization is a sequence of rendering steps followed by comparison to training views <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

The loss function combines:
*   **L1 Loss**: Measures the pixel-wise difference between the rendered image and the ground truth <a class="yt-timestamp" data-t="02:32:55">[02:32:55]</a>.
*   **DSSIM (Structural Similarity Index)**: Measures structural similarity between images <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.
A hyperparameter (Lambda = 0.2) balances these two components <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.

Gradients for all parameters are explicitly derived to avoid significant overhead from automatic differentiation <a class="yt-timestamp" data-t="01:16:05">[01:16:05]</a>. The differentiability of the tile rasterizer is key, allowing gradients to flow back through the rendering process to update the 3D Gaussian parameters <a class="yt-timestamp" data-t="01:29:40">[01:29:40]</a>.

## Adaptive Density Control
Interleaved with the optimization of Gaussian properties are steps that control the number and density of Gaussians <a class="yt-timestamp" data-t="01:29:57">[01:29:57]</a>. This allows the method to adapt from an initial sparse set to a denser, more accurate representation of the scene <a class="yt-timestamp" data-t="01:31:37">[01:31:37]</a>.

### Pruning
Transparent Gaussians (those with an opacity close to zero) are periodically removed <a class="yt-timestamp" data-t="01:31:58">[01:31:58]</a>, typically every 100 iterations <a class="yt-timestamp" data-t="01:31:44">[01:31:44]</a>. This means Gaussians that gradient descent makes increasingly transparent are eventually discarded <a class="yt-timestamp" data-t="01:32:37">[01:32:37]</a>.

### Densification (Cloning and Splitting)
To populate empty areas or refine [[challenges_in_3d_gaussian_representation | areas with high variance]], Gaussians are either cloned or split <a class="yt-timestamp" data-t="01:32:54">[01:32:54]</a>.
*   **Cloning**: For small Gaussians in under-reconstructed regions (identified by large positional gradients), a copy of the Gaussian is created and moved in the direction of the positional gradient <a class="yt-timestamp" data-t="01:34:36">[01:34:36]</a>.
*   **Splitting**: Large Gaussians or those in regions with high variance are replaced by two new smaller Gaussians, dividing their scale by a factor of 1.6 <a class="yt-timestamp" data-t="01:35:08">[01:35:08]</a>, <a class="yt-timestamp" data-t="01:35:12">[01:35:12]</a>.

These density control steps are based on hard-coded hyperparameters, such as thresholds for positional gradients and opacity <a class="yt-timestamp" data-t="01:35:50">[01:35:50]</a>. For example, Alpha values are periodically reset to near zero every 3,000 iterations to moderate the increase in Gaussian count <a class="yt-timestamp" data-t="01:36:21">[01:36:21]</a>.

### Regularization and Stability
The method incorporates strategies to prevent issues like "floaters" (Gaussians drifting too close to the camera) <a class="yt-timestamp" data-t="01:36:01">[01:36:01]</a>. It also periodically removes very large Gaussians or those with a big footprint in view space <a class="yt-timestamp" data-t="01:37:38">[01:37:38]</a>. The method aims to handle scenes with arbitrarily varying depth complexity by not limiting the number of blended primitives that receive gradient updates <a class="yt-timestamp" data-t="01:52:04">[01:52:04]</a>.

## Training Process Specifics
The optimization starts with a warm-up phase, initially using a lower image resolution (4x smaller) and gradually upsampling <a class="yt-timestamp" data-t="02:06:26">[02:06:26]</a>. This strategy, along with the gradual introduction of spherical harmonic bands, helps manage the optimization process <a class="yt-timestamp" data-t="02:07:05">[02:07:05]</a>.

The number of Gaussians can grow significantly during training, starting from around 100,000 initial Gaussians, pruning them down to 6,000-10,000, but ultimately growing to 200,000 to 500,000 Gaussians per scene <a class="yt-timestamp" data-t="02:11:57">[02:11:57]</a>.

## Advantages and Limitations
::admonition[Advantages]{.info}
*   **High Visual Quality**: The anisotropic nature of 3D Gaussians allows them to align well with surfaces and capture fine details, outperforming [[comparison_of_3d_gaussian_splatting_to_neural_radiance_fields | Nerfs]] and other methods in metrics like SSIM <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="01:59:19">[01:59:19]</a>.
*   **Competitive Training Times**: The fast, differentiable tile-based rasterizer, optimized with CUDA kernels, significantly reduces training time compared to traditional Nerfs <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>, <a class="yt-timestamp" data-t="02:01:06">[02:01:06]</a>.
*   **Real-time Rendering**: Once trained, the scene can be rendered at real-time display rates (e.g., 30 frames per second) for novel view synthesis <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>, <a class="yt-timestamp" data-t="01:30:54">[01:30:54]</a>.
*   **Handles Complex Scenes**: Capable of reconstructing and rendering complete, complex indoor and outdoor scenes with large depth complexity, unlike some methods limited to isolated objects <a class="yt-timestamp" data-t="01:57:57">[01:57:57]</a>.
::

::admonition[Limitations]{.warning}
*   **High Memory Consumption**: The explicit representation of scenes with hundreds of thousands of Gaussians leads to significantly higher memory usage (e.g., 734 MB per scene) compared to implicit [[comparison_of_3d_gaussian_splatting_to_neural_radiance_fields | Nerfs]] (e.g., 13 MB) <a class="yt-timestamp" data-t="02:03:02">[02:03:02]</a>, <a class="yt-timestamp" data-t="02:37:09">[02:37:09]</a>. Training large scenes can exceed 20 GB of GPU memory <a class="yt-timestamp" data-t="02:23:45">[02:23:45]</a>.
*   **Hard-coded Hyperparameters**: The reliance on specific thresholds and factors for density control (e.g., scale division factor of 1.6, iteration counts for pruning/splitting) implies sensitivity to scene types <a class="yt-timestamp" data-t="01:35:50">[01:35:50]</a>.
*   **Artifacts**: Can exhibit "popping" artifacts where Gaussians suddenly appear or disappear due to view-dependent appearance or simple visibility culling <a class="yt-timestamp" data-t="02:21:18">[02:21:18]</a>. Elongated or "splotchy" Gaussians can also occur <a class="yt-timestamp" data-t="02:21:10">[02:21:10]</a>.
*   **Static Scenes**: The method, like most existing approaches, is limited to static scenes and does not currently handle dynamic, time-varying environments <a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>, <a class="yt-timestamp" data-t="02:44:20">[02:44:20]</a>.

## Future Prospects
There are several avenues for future work, including:
*   Further reducing memory consumption through careful low-level implementation or [[applications_and_limitations_of_3d_gaussians | compression techniques]] <a class="yt-timestamp" data-t="02:24:25">[02:24:25]</a>.
*   Adapting the method for [[dynamic_3d_gaussian_technique | dynamic 3D Gaussian Splatting]] or time-varying scenes <a class="yt-timestamp" data-t="02:44:50">[02:44:50]</a>.
*   Exploring the use of 3D Gaussians for mesh reconstruction, which is a common requirement for integration into existing game engines and CGI pipelines <a class="yt-timestamp" data-t="02:27:22">[02:27:22]</a>.
*   Porting more of the optimization logic from Python to optimized CUDA kernels for even greater speedups <a class="yt-timestamp" data-t="02:26:24">[02:26:24]</a>.