---
title: Optimization Techniques and Challenges for 3D Scene Representation
videoId: xgwvU7S0K-k
---

From: [[hu-po]] <br/> 

## Introduction to 3D Scene Representation <a class="yt-timestamp" data-t="01:11:49">[01:11:49]</a>

The field of [[3d_scene_representation_and_simulation | 3D Scene Representation and Simulation]] aims to create novel views of scenes captured from multiple photos or videos <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This involves generating new images of a scene from a different point of view than the original captured data <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. The representation chosen for a 3D scene significantly impacts the efficiency and quality of novel view synthesis <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

Traditional 3D scene representations include meshes and points, which are explicit and well-suited for fast GPU and CUDA-based rasterization <a class="yt-timestamp" data-t="01:12:25">[01:12:25]</a>. However, these methods can struggle with unreconstructed regions or "inexistent geometry" when multi-view stereo generates incorrect data <a class="yt-timestamp" data-t="01:34:01">[01:34:01]</a>.

## Neural Radiance Fields (Nerfs) and their Optimization Challenges <a class="yt-timestamp" data-t="01:48:51">[01:48:51]</a>

Neural Radiance Fields (Nerfs) are a recent advancement in 3D scene representation, building on continuous scene representations <a class="yt-timestamp" data-t="01:48:51">[01:48:51]</a>. A Nerf defines a 3D volume where each point in space has a color and opacity, typically learned by training a multi-layer perceptron (MLP) <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>.

### Limitations of Nerfs <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>

Despite their ability to revolutionize novel view synthesis <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>, Nerfs face several challenges:

*   **Computational Cost:** Achieving high visual quality requires neural networks that are costly to train and render <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Training a Nerf for a scene can take up to 48 hours <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>.
*   **Scene Specificity:** A neural network must be trained for every single scene or object, and even for specific lighting or object arrangements <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Real-time Rendering:** No current method based on Nerfs can achieve real-time display rates at 1080p resolution <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Stochastic Sampling:** Rendering with volumetric ray marching requires a large number of stochastic samples, leading to high cost and potential noise <a class="yt-timestamp" data-t="01:06:23">[01:06:23]</a>.
*   **Memory Usage:** While MLPs are relatively small (e.g., 8-13 MB), the rendering process can still be memory-intensive <a class="yt-timestamp" data-t="02:02:50">[02:02:50]</a>.

Various follow-up methods like Instant NGP and Plenoxels have focused on faster training and rendering by exploiting spatial data structures, different encodings, and MLP capacities, or by interpolating values stored in voxels or hash grids <a class="yt-timestamp" data-t="01:27:24">[01:27:24]</a>.

## 3D Gaussian Splatting: A Novel Approach to Optimization <a class="yt-timestamp" data-t="01:19:12">[01:19:12]</a>

A new method, 3D Gaussian Splatting, proposes three key elements to achieve state-of-the-art visual quality with competitive training times and real-time novel view synthesis <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>:

1.  **3D Gaussian Scene Representation:** The scene is represented as a set of 3D gaussians, preserving desirable properties of continuous volumetric radiance fields while avoiding unnecessary computation in empty space <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. These gaussians are differentiable and can be easily projected into 2D splats for rendering <a class="yt-timestamp" data-t="01:04:07">[01:04:07]</a>. Each 3D gaussian is defined by a 3D position (mean), an opacity (Alpha), and an anisotropic covariance matrix, with color represented by spherical harmonic coefficients <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>.
2.  **Interleaved Optimization and Adaptive Density Control:** The properties of the 3D gaussians are optimized using gradient descent, interleaved with steps to control their density <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. This allows the method to start with a sparse point cloud (from Structure from Motion) and adaptively grow or shrink the number of gaussians to accurately represent the scene <a class="yt-timestamp" data-t="01:31:27">[01:31:27]</a>.
    *   **Covariance Optimization:** Instead of directly optimizing the covariance matrix (which must be positive semi-definite), the method optimizes a scaling matrix and a quaternion for rotation, which are then combined to form a valid covariance matrix <a class="yt-timestamp" data-t="01:12:31">[01:12:31]</a>.
    *   **Density Control:** Gaussians are adaptively controlled. Transparent gaussians are removed periodically <a class="yt-timestamp" data-t="01:31:58">[01:31:58]</a>. New gaussians are added by cloning existing ones (especially in under-reconstructed areas or where gradients suggest large positional changes) or by splitting large gaussians into smaller ones <a class="yt-timestamp" data-t="01:32:54">[01:32:54]</a>.
3.  **Fast Visibility-Aware Rendering Algorithm:** A tile-based rasterizer is developed, supporting anisotropic splatting and accelerating both training and real-time rendering <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. The screen is split into 16x16 tiles <a class="yt-timestamp" data-t="01:41:05">[01:41:05]</a>. Gaussians are pre-sorted for the entire image using a fast GPU Radix sort, avoiding per-pixel sorting costs <a class="yt-timestamp" data-t="01:40:07">[01:40:07]</a>. This allows for approximate Alpha blending that respects visibility order <a class="yt-timestamp" data-t="01:40:32">[01:40:32]</a>.

### [[challenges_of_optimization_in_discrete_and_continuous_spaces | Challenges of Optimization in Discrete and Continuous Spaces]] <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>

The optimization process in 3D Gaussian Splatting presents its own set of challenges:

*   **Complicated Optimization Process:** The interleaved optimization with different loss functions and alternating steps can be slower and harder to implement/understand <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Dynamic Number of Gaussians:** The ability to "create and destroy" gaussians during optimization makes the process more complex than working with a fixed set <a class="yt-timestamp" data-t="01:22:37">[01:22:37]</a>.
*   **Hyperparameter Tuning:** The method relies on several hard-coded hyperparameters, such as thresholds for position change, transparency for pruning, and scaling factors for splitting, which are determined experimentally <a class="yt-timestamp" data-t="01:34:09">[01:34:09]</a>. This indicates potential scene-specific tuning <a class="yt-timestamp" data-t="01:52:54">[01:52:54]</a>.
*   **Floaters and Popping Artifacts:** The optimization can get stuck with "floaters" (gaussians close to the camera) <a class="yt-timestamp" data-t="01:36:01">[01:36:01]</a>. Also, "popping artifacts" can occur where large gaussians suddenly appear or disappear when the view changes slightly, partly due to the trivial rejection of gaussians via a "guard band" or simple visibility issues <a class="yt-timestamp" data-t="02:21:18">[02:21:18]</a>.

### Performance and [[Evaluation of 3D Generative Techniques | Evaluation of 3D Generative Techniques]] <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>

3D Gaussian Splatting demonstrates significant improvements over existing methods:

*   **Training Time:** It achieves state-of-the-art quality with training times as low as 41-51 minutes <a class="yt-timestamp" data-t="02:01:06">[02:01:06]</a>, compared to 48 hours for some Nerfs <a class="yt-timestamp" data-t="02:10:50">[02:10:50]</a>.
*   **Rendering Speed:** The method enables real-time novel view synthesis (30+ FPS possible) <a class="yt-timestamp" data-t="01:31:08">[01:31:08]</a>, with rendering times significantly faster than Nerfs which can take 10 seconds per frame <a class="yt-timestamp" data-t="02:10:54">[02:10:54]</a>.
*   **Visual Quality:** It achieves comparable or superior visual quality to methods like MIP-Nerf 360, particularly in rendering fine structures (e.g., bicycle spokes) and avoiding blurring or "fuzzy" effects <a class="yt-timestamp" data-t="01:59:01">[01:59:01]</a>.

### [[Technical Insights Balancing Complexity and Efficiency in 3D Modeling | Technical Insights Balancing Complexity and Efficiency in 3D Modeling]] <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>

Key technical decisions contribute to the balance:

*   **Differentiable Rasterizer:** The rasterizer is fully differentiable, crucial for backpropagating gradients from the image reconstruction loss back to the 3D gaussian parameters <a class="yt-timestamp" data-t="01:29:40">[01:29:40]</a>.
*   **Custom CUDA Kernels:** Implementing bottlenecks, such as the fast sorting algorithm, as custom CUDA kernels on the GPU is critical for efficiency <a class="yt-timestamp" data-t="01:23:44">[01:23:44]</a>.
*   **Anisotropic Covariance:** Allowing gaussians to have anisotropic (directionally dependent) covariance matrices significantly improves their ability to align with surfaces and represent complex shapes <a class="yt-timestamp" data-t="01:51:52">[01:51:52]</a>, leading to a more compact representation in terms of modeling capability per gaussian.
*   **Spherical Harmonics:** Using spherical harmonic coefficients for directional appearance (color) helps capture view-dependent effects and improves overall quality <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>.

## Memory Consumption: A Significant Challenge <a class="yt-timestamp" data-t="02:37:39">[02:37:39]</a>

Despite the performance gains, a major challenge for 3D Gaussian Splatting is its memory footprint:

*   **Explicit Representation:** Unlike implicit representations like Nerfs (which store only MLP weights, typically 8-13 MB) <a class="yt-timestamp" data-t="02:02:50">[02:02:50]</a>, 3D Gaussian Splatting is an explicit representation. It stores the position, covariance, opacity, and color for hundreds of thousands of gaussians per scene <a class="yt-timestamp" data-t="02:36:09">[02:36:09]</a>.
*   **High Memory Usage:** This leads to a single scene representation consuming hundreds of megabytes (e.g., 734 MB) <a class="yt-timestamp" data-t="02:01:22">[02:01:22]</a>, with peak GPU memory consumption exceeding 20 gigabytes during training of large scenes <a class="yt-timestamp" data-t="02:23:45">[02:23:45]</a>.
*   **Opportunities for Reduction:** Future work could explore compression techniques for point clouds to reduce memory consumption <a class="yt-timestamp" data-t="02:24:29">[02:24:29]</a>.

## [[limitations_and_assumptions_of_dynamic_3d_modeling | Limitations and Assumptions of Dynamic 3D Modeling]] <a class="yt-timestamp" data-t="02:44:27">[02:44:27]</a>

A shared limitation with existing Nerf-based approaches is that 3D Gaussian Splatting is designed for **static scenes** <a class="yt-timestamp" data-t="00:58:48">[00:58:48]</a>. The ability to represent and render [[challenges_and_opportunities_in_dynamic_scenes_representation | dynamic scenes]] (scenes with a time component, like videos) remains a significant future challenge for 3D scene representation <a class="yt-timestamp" data-t="02:44:27">[02:44:27]</a>. Current techniques rely on camera positions calibrated by Structure from Motion (SFM), which introduces noise and inherent limitations <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Conclusion <a class="yt-timestamp" data-t="02:25:20">[02:25:20]</a>

3D Gaussian Splatting represents a significant step towards real-time, high-quality radiance field rendering. By leveraging an explicit 3D Gaussian primitive representation, interleaved optimization, and an efficient tile-based rasterizer, it overcomes many performance limitations of previous methods. However, challenges related to memory consumption and the current focus on static scenes provide fertile ground for future research in [[challenges_and_limitations_in_3d_generation | 3D generation]].