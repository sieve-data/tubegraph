---
title: Neural Angelo framework
videoId: ccGxQCpbrnM
---

From: [[hu-po]] <br/> 

Neural Angelo is a framework developed by [[Meta AI research | Nvidia Research]] and John Hopkins University for high-fidelity 3D surface reconstruction from RGB images <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. It employs a [[neural_volume_rendering_and_radiance_fields | neural volume rendering]] approach <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a> and can achieve detailed reconstructions even without auxiliary data like segmentation or depth information <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>, <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## Core Techniques

### Neural Volume Rendering
The framework utilizes [[neural_volume_rendering_and_radiance_fields | neural volume rendering]], a technique often associated with [[neural_volume_rendering_and_radiance_fields | NeRFs]] (Neural Radiance Fields) <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. [[neural_volume_rendering_and_radiance_fields | NeRFs]] represent a 3D scene as volume density and color fields, where a multi-layer perceptron (MLP) maps 3D spatial locations to color and volume density <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>, <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>.

### Multi-resolution 3D Hash Grids
Neural Angelo incorporates the representation power of multi-resolution 3D hash grids <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>, <a class="yt-timestamp" data-t="02:05:01">[02:05:01]</a>. This technique, stemming from Instant NGP, uses multiple grids at different resolutions (e.g., coarse to fine) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>, <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>. Each "hash entry" (like a Python dictionary mapping a 3D position to a value) stores an encoding feature <a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>, <a class="yt-timestamp" data-t="01:02:27">[01:02:27]</a>. These features are obtained via tri-linear interpolation of hash entries at grid cell corners <a class="yt-timestamp" data-t="01:03:17">[01:03:17]</a> and then concatenated across all spatial resolutions to form a comprehensive feature vector <a class="yt-timestamp" data-t="01:04:48">[01:04:48]</a>.

### Numerical Gradients for Higher-Order Derivatives
A key innovation is the use of numerical gradients to compute higher-order derivatives, such as surface normals <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>, <a class="yt-timestamp" data-t="02:04:55">[02:04:55]</a>.
*   **Analytical vs. Numerical**: Analytical gradients involve exactly solving derivative equations <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>, while numerical gradients estimate them by sampling points slightly above and below <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Numerical gradients are generally faster and easier but less accurate <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Locality Issue**: Analytical gradients of hash encodings are not continuous across space under tri-linear interpolation <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>, limiting backpropagation to local grid cells <a class="yt-timestamp" data-t="01:22:39">[01:22:39]</a>. This can lead to non-local smoothness <a class="yt-timestamp" data-t="01:08:49">[01:08:49]</a>, where the surface might be smooth locally but jagged at coarser resolutions <a class="yt-timestamp" data-t="01:09:08">[01:09:08]</a>.
*   **Smoothing Effect**: Numerical gradients, with carefully chosen step sizes, distribute optimization updates beyond the local hash grid cell, acting as a smoothing operation on the analytical gradient expression <a class="yt-timestamp" data-t="01:25:49">[01:25:49]</a>, <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. This allows multiple grid cells to receive optimization updates simultaneously <a class="yt-timestamp" data-t="01:25:42">[01:25:42]</a>.

### Progressive Optimization Schedule
Neural Angelo uses a course-to-fine optimization scheme to reconstruct surfaces with progressive levels of detail <a class="yt-timestamp" data-t="01:39:09">[01:39:09]</a>, <a class="yt-timestamp" data-t="02:04:57">[02:04:57]</a>. This means starting with coarser hash grid resolutions and progressively activating finer hash grids as optimization proceeds and the step size decreases <a class="yt-timestamp" data-t="01:41:51">[01:41:51]</a>, <a class="yt-timestamp" data-t="01:52:50">[01:52:50]</a>.

### Signed Distance Functions (SDFs)
The framework adopts a neural SDF representation for the underlying 3D scene <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. An SDF implicitly represents a surface as its zero-level set, where the function output is positive in front of the surface, negative inside, and zero on the surface <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>, <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>. This provides a more explicit and defined 3D surface compared to simple volume density fields alone <a class="yt-timestamp" data-t="00:36:28">[00:36:28]</a>, <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.

## Key Features and Advantages

*   **High Fidelity**: Neural Angelo aims for high-fidelity surface reconstruction, capable of recovering detailed structures of real-world scenes that current methods struggle with <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a>, <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **RGB-only Input**: It reconstructs surfaces using only standard RGB images (e.g., from a cell phone or video capture), without relying on auxiliary inputs like segmentation or depth <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>, <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Scalability**: The multi-resolution hash encoding provides great scalability for neural scene representations, generating fine-grained details <a class="yt-timestamp" data-t="00:59:59">[00:59:59]</a>.
*   **End-to-End Optimization**: All network parameters, including MLPs and hash encodings, are trained jointly end-to-end, simplifying the pipeline <a class="yt-timestamp" data-t="01:46:06">[01:46:06]</a>.

## Challenges Addressed

Neural Angelo addresses several common issues in 3D reconstruction:

*   **Ambiguous Observations**: Classical multi-view stereo algorithms struggle with regions of homogeneous colors or non-Lambertian materials (surfaces that don't reflect light uniformly), leading to inaccurate reconstructions <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>, <a class="yt-timestamp" data-t="01:14:18">[01:14:18]</a>.
*   **Noisy Surfaces**: Previous [[neural_volume_rendering_and_radiance_fields | NeRF]]-based methods often produce noisy or fuzzy surfaces due to insufficient constraints, making it hard to define clear boundaries <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>, <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>. Neural Angelo aims for smooth and complete surface representations <a class="yt-timestamp" data-t="01:17:01">[01:17:01]</a>.
*   **Locality of Gradients**: The analytical gradients in hash encodings suffer from locality issues, meaning optimization updates only propagate to local grid cells <a class="yt-timestamp" data-t="01:08:44">[01:08:44]</a>. Numerical gradients overcome this by enabling updates to multiple cells simultaneously <a class="yt-timestamp" data-t="01:25:42">[01:25:42]</a>.
*   **Smoothness vs. Detail Trade-off**: While smoothing operations are beneficial, excessive smoothness can lead to a loss of fine details (e.g., brick textures) <a class="yt-timestamp" data-t="02:03:04">[02:03:04]</a>. The progressive optimization schedule helps manage this by introducing finer details over time <a class="yt-timestamp" data-t="01:56:22">[01:56:22]</a>.

## Technical Details

*   **MLP Structure**: The encoded features from the hash grids are passed to a shallow MLP, which outputs both the SDF value and color for a given 3D point <a class="yt-timestamp" data-t="01:49:51">[01:49:51]</a>, <a class="yt-timestamp" data-t="01:53:45">[01:53:45]</a>.
*   **Loss Functions**: The total loss function is a weighted sum of:
    *   **Color Loss (L_RGB)**: Measures the L1 difference between the rendered pixel color and the input image pixel color <a class="yt-timestamp" data-t="01:10:09">[01:10:09]</a>, <a class="yt-timestamp" data-t="01:12:40">[01:12:40]</a>.
    *   **Iconal Loss (L_Ike)**: Regularizes the SDF predictions to ensure the gradient of the SDF has a unit norm (magnitude of one) almost everywhere <a class="yt-timestamp" data-t="01:11:01">[01:11:01]</a>, <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>.
    *   **Curvature Regularization (L_Curve)**: Imposes a prior by regularizing the mean curvature of the SDF to encourage smoothness and prevent undesirable sharp transitions <a class="yt-timestamp" data-t="01:44:10">[01:44:10]</a>, <a class="yt-timestamp" data-t="02:01:25">[02:01:25]</a>. The strength of this loss is gradually increased during training <a class="yt-timestamp" data-t="02:03:51">[02:03:51]</a>.
*   **Weight Decay**: Applied over all parameters to prevent single-resolution features from dominating the final result <a class="yt-timestamp" data-t="01:42:43">[01:42:43]</a>.

## Performance and Evaluation

Neural Angelo was evaluated on various datasets:

*   **DTU Dataset**: Consists of 15 object-centric scenes with 49 or 64 images captured by a robot-held monocular RGB camera <a class="yt-timestamp" data-t="01:46:47">[01:46:47]</a>. Ground truth is obtained from a structured light scanner <a class="yt-timestamp" data-t="01:48:04">[01:48:04]</a>.
*   **Tanks and Temples Dataset**: Includes six large-scale indoor and outdoor scenes with 263 to 1107 images captured using a handheld monocular RGB camera <a class="yt-timestamp" data-t="01:48:27">[01:48:27]</a>, <a class="yt-timestamp" data-t="01:48:52">[01:48:52]</a>. Ground truth is obtained using a lidar sensor <a class="yt-timestamp" data-t="01:49:18">[01:49:18]</a>.

Metrics used for evaluation include Chamfer distance and F1 score for surface quality, and Peak Signal-to-Noise Ratio (PSNR) for image synthesis quality <a class="yt-timestamp" data-t="01:52:10">[01:52:10]</a>, <a class="yt-timestamp" data-t="01:52:17">[01:52:17]</a>. Neural Angelo generally achieved the lowest Chamfer distance and highest PSNR, indicating superior reconstruction quality <a class="yt-timestamp" data-t="01:56:40">[01:56:40]</a>.

Ablation studies confirmed the effectiveness of numerical gradients (NG) in achieving smoother results compared to analytical gradients (AG) <a class="yt-timestamp" data-t="01:54:57">[01:54:57]</a>. The progressive activation of hash resolutions also plays a crucial role in capturing fine details <a class="yt-timestamp" data-t="01:56:22">[01:56:22]</a>.

## Limitations and Future Work

The current method samples pixels randomly from images without tracking their statistics or errors, leading to long training iterations <a class="yt-timestamp" data-t="02:05:31">[02:05:31]</a>. Future work will explore more efficient sampling strategies to accelerate the training process <a class="yt-timestamp" data-t="02:06:06">[02:06:06]</a>.