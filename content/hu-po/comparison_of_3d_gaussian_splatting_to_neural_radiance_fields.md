---
title: Comparison of 3D gaussian splatting to neural radiance fields
videoId: xgwvU7S0K-k
---

From: [[hu-po]] <br/> 
The development of 3D scene representation has seen significant advancements, particularly with the introduction of [[volumetric_rendering_and_neural_radiance_fields | Neural Radiance Fields (NeRFs)]]. More recently, a new technique called [[3D gaussian splatting for realtime radiance field rendering | 3D Gaussian Splatting]] has emerged, offering a different approach to rendering and scene synthesis. Both technologies aim to create novel views of scenes captured from multiple photos or videos [00:03:09, 00:03:22, 00:04:09, 00:17:44, 00:58:48].

### Similarities
*   **Novel View Synthesis:** Both [[nerfs_versus_gaussian_splatting | NeRFs]] and [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] revolutionize the creation of new images from different viewpoints of a scene [00:03:09, 00:03:22].
*   **Input Data:** They both require multiple photos or videos of a scene as input [00:03:46, 00:04:09, 00:17:44, 00:58:48].
*   **Camera Calibration:** A crucial prerequisite for both is the precise calibration of camera positions, typically achieved using Structure-from-Motion (SfM) techniques, which inherently introduce noise and are susceptible to artifacts in featureless or shiny areas [00:06:06, 00:59:27, 01:06:01, 01:13:22, 01:16:32, 01:20:04, 01:24:40, 01:37:00, 01:47:10, 00:43:55, 01:36:01].
*   **Image Formation Model:** The underlying principle for generating images is similar: summing up opacity and color contributions along rays [01:37:00, 01:47:10].
*   **Static Scenes:** Currently, both methods are primarily limited to static scenes and do not yet handle dynamic or time-varying elements [00:58:53, 02:44:23].

### Key Differences and Advantages of Gaussian Splatting
The core difference lies in their scene representation and rendering mechanisms, leading to distinct advantages for Gaussian Splatting:

*   **Scene Representation:**
    *   **[[nerfs_versus_gaussian_splatting | NeRFs]]**: Represent a scene as a continuous radiance field encoded by a neural network (Multi-Layer Perceptron or MLP). This MLP learns the color and opacity of different points in 3D space [00:01:19, 00:04:25, 00:14:51, 00:15:20].
    *   **[[gaussian_splatting_and_its_advantages | Gaussian Splatting]]**: Represents the scene using a discrete set of 3D Gaussians. Each Gaussian has a 3D position (mean), an opacity (alpha), a 3D anisotropic covariance matrix (defining its shape and spread), and spherical harmonic coefficients for color [00:01:25, 00:06:48, 00:59:59, 01:00:59, 01:01:04, 01:01:08, 01:01:10, 01:01:12, 01:01:13, 01:01:15, 01:01:16].

*   **Training Time:**
    *   [[nerfs_versus_gaussian_splatting | NeRFs]] require significant training time (e.g., a standard NeRF can take 48 hours) [00:02:52, 02:10:50].
    *   [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] offers competitive training times, often completing in minutes (e.g., 51 minutes for comparable results, or even 5-10 minutes for high quality) [00:03:00, 01:17:15, 02:10:06, 02:10:50, 02:10:58].

*   **Rendering Speed and Quality:**
    *   [[nerfs_versus_gaussian_splatting | NeRFs]] typically struggle to achieve real-time rendering rates at high resolutions (e.g., 1080p), due to the costly stochastic sampling and neural network inferences required for each ray [00:05:56, 00:16:23].
    *   [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] achieves state-of-the-art visual quality with real-time novel view synthesis (e.g., 1080p resolution) [00:05:52, 00:06:20, 01:17:18]. This is facilitated by a fast, differentiable, tile-based rasterizer that efficiently sorts 3D Gaussians using GPU Radix sort [01:15:15, 01:17:15, 01:18:15, 01:19:15, 01:20:15, 01:21:15, 01:22:15, 01:23:15, 01:24:15, 01:25:15, 01:26:15, 01:27:15, 01:28:15, 01:29:15, 01:30:15, 01:31:15, 01:32:15, 01:33:15, 01:34:15, 01:35:15, 01:36:15, 01:37:15, 01:38:15, 01:39:15, 01:40:15, 01:41:15, 01:42:15, 01:43:15, 01:44:15, 01:45:15, 01:46:15, 01:47:15, 01:48:15, 01:49:15, 01:50:15, 01:51:15, 01:52:15, 01:53:15, 01:54:15, 01:55:15, 01:56:15, 01:57:15, 01:58:15, 01:59:15, 02:00:15, 02:01:15, 02:02:15, 02:03:15, 02:04:15, 02:05:15, 02:06:15, 02:07:15, 02:08:15, 02:09:15, 02:10:15, 02:11:15, 02:12:15, 02:13:15, 02:14:15, 02:15:15, 02:16:15, 02:17:15, 02:18:15, 02:19:15, 02:20:15, 02:21:15, 02:22:15, 02:23:15, 02:24:15, 02:25:15, 02:26:15, 02:27:15, 02:28:15, 02:29:15, 02:30:15, 02:31:15, 02:32:15, 02:33:15, 02:34:15, 02:35:15, 02:36:15, 02:37:15, 02:38:15, 02:39:15, 02:40:15, 02:41:15, 02:42:15, 02:43:15, 02:44:15, 02:45:15].
*   **Detail and Artifacts:** [[nerfs_versus_gaussian_splatting | NeRFs]] can suffer from blurriness, "fuzz," or "smear" effects, especially with fine details like bicycle spokes or window frames [01:59:01, 01:59:09, 02:00:06]. [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] is noted for its ability to capture fine structures more accurately and avoid these artifacts [01:00:46, 01:59:01, 01:59:54, 02:11:13].

### Implementation and Optimization
The [[3D Gaussian Splatting and Instant Splat Pipeline | 3D Gaussian Splatting pipeline]] involves several key steps:

*   **Initialization:** It starts with sparse point clouds generated from SfM [00:06:35, 00:59:37, 02:00:10]. These points are used to initialize the positions of the 3D Gaussians, with their initial scale based on the distance to the closest three points [01:24:40].
*   **Optimization with Adaptive Density Control:** The properties of the 3D Gaussians (position, opacity, covariance, spherical harmonic coefficients for color) are optimized using gradient descent. This process is interleaved with adaptive density control steps [00:47:04, 01:00:07, 01:11:26, 01:20:00].
    *   **Creation/Destruction:** Gaussians can be added (cloned) in under-reconstructed areas (regions with large positional gradients) or split into smaller Gaussians in regions with high variance [01:22:37, 01:33:10, 01:34:36, 01:35:01, 01:35:06].
    *   **Pruning:** Transparent Gaussians (those with very low opacity) are periodically removed [01:31:58, 01:32:21].
    *   **Regularization:** Techniques are applied to prevent "floaters" (Gaussians drifting too close to the camera) and to manage the overall number and size of Gaussians [01:36:01, 01:37:51].
    *   **Loss Function:** Optimization uses a combination of L1 loss (pixel difference) and the Structural Similarity Index Measure (SSIM) loss [01:25:26, 01:27:32].
*   **Fast Differentiable Rasterizer:** A critical component for speed is a tile-based rasterizer that projects 3D Gaussians into 2D "splats" [01:39:58, 02:41:10].
    *   **GPU Optimization:** The rasterizer leverages fast GPU sorting algorithms, such as Radix sort, to order Gaussians by depth for correct Alpha blending, working on 16x16 pixel tiles [01:40:00, 01:41:05, 01:41:17, 01:43:01, 01:44:15, 01:45:15, 01:46:15, 01:47:15, 01:48:15].
    *   **Differentiability:** The rasterizer is fully differentiable, allowing gradients from the image reconstruction loss to be propagated back to all Gaussian parameters [01:40:46, 01:40:54, 02:40:24].

### Limitations and Future Implications
Despite its advantages, [[applications_and_limitations_of_3d_gaussians | 3D Gaussian Splatting]] has its limitations:

*   **Memory Consumption:** It requires significantly higher GPU memory compared to [[nerfs_versus_gaussian_splatting | NeRFs]] (e.g., 734 MB vs. 13 MB for a scene representation), storing individual parameters for hundreds of thousands to millions of Gaussians per scene [02:01:22, 02:02:10, 02:03:03, 02:11:46, 02:12:12, 02:13:10, 02:23:37, 02:23:45].
*   **Artifacts:** In unobserved regions, it can still produce artifacts like "splotchy" Gaussians or "popping" effects when rapidly changing camera views [02:20:56, 02:21:09, 02:21:10, 02:21:18, 02:21:26].
*   **Hyperparameter Dependence:** The optimization process includes several hard-coded hyperparameters for density control and learning rate schedules, which may require scene-specific tuning [01:34:11, 01:35:12, 01:36:24, 02:22:56].
*   **Static Scenes:** Like NeRFs, the current method is designed for static scenes. Future work could explore [[dynamic_3d_gaussian_technique | adapting the technique for dynamic scenes]] [02:44:23].
*   **Explicit vs. Implicit:** The large number of Gaussians makes this an explicit scene representation, contrasting with NeRF's implicit representation. This explicit nature contributes to higher memory usage but allows for faster rendering via direct rasterization [02:12:34, 02:13:23].

[[comparisons_between_gaussian_splats_and_other_3d_representation_technologies | Comparisons between Gaussian splats and other 3D representation technologies]] suggest that while NeRFs are compact due to their implicit representation, Gaussian Splatting leverages an explicit, point-based approach that is well-suited for fast GPU processing, opening new avenues for [[implications_of_gaussian_splatting_in_future_technologies | future applications in real-time graphics and virtual reality]] [02:43:32, 02:43:57]. Optimizing the non-rasterization parts of the pipeline with lower-level programming (e.g., Cuda) could yield further significant speedups [02:26:24].