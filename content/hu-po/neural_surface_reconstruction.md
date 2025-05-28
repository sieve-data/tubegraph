---
title: Neural surface reconstruction
videoId: ccGxQCpbrnM
---

From: [[hu-po]] <br/> 

[[neural_surface_reconstruction | Neural surface reconstruction]] is a framework for high-fidelity 3D surface reconstruction from RGB images using a [[neural_volume_rendering | neural volume rendering]] approach [00:01:11]. It aims to recover dense geometric scene structures from multiple images observed at different viewpoints [00:10:49]. The recovered surfaces provide structural information useful for applications like 3D asset generation and environment mapping for autonomous navigation [00:11:21].

## Core Concepts

### 3D Surface Reconstruction
This process creates a mesh, which consists of triangles with vertices and edges connecting them [00:01:22]. The goal is to achieve high detail, getting into cracks, and reconstructing occluded areas [00:04:00].

### RGB Images
Standard image types, typically from cell phones, with red, green, and blue color channels [00:01:34]. [[neural_surface_reconstruction | Neural surface reconstruction]] methods like Neural Angelo can achieve results *without* auxiliary data like segmentation or depth [00:01:59].

### Neural Volume Rendering
This technique uses neural networks to render a 3D volume [00:01:48]. It is the technique behind [[volumetric_rendering_and_neural_radiance_fields | Nerfs]] (Neural Radiance Fields) [00:01:44].

### Implicit Functions
[[neural_surface_reconstruction | Neural surface reconstruction]] methods often represent a scene as an implicit function [00:15:58].
*   **Occupancy Fields:** Refer to whether a part of a 3D volume is occupied [00:16:09].
*   **Signed Distance Functions (SDFs):** A function that tells you how far away you are from the surface of an object at any point inside a volume [00:16:29]. An SDF is differentiable and its gradient has a unit norm almost everywhere [01:09:36]. The surface itself is defined by the zero-level set of the SDF [00:55:25].

> [!INFO] Problem with Classic Photogrammetry
> Traditional photometric consistency assumptions often fail due to auto-exposure or non-Lambertian (e.g., shiny) materials, leading to inaccurate reconstructions [00:25:44]. Relaxing these constraints is important for realistic 3D constructions [00:27:07].

## Neural Angelo Framework

Neural Angelo, a paper from Nvidia Research and Johns Hopkins University [00:00:58], combines the representational power of multi-resolution 3D hash grids with neural SDF representations [00:46:27, 02:05:01]. It is optimized from multi-view image observations via [[neural_surface_reconstruction | neural surface rendering]] [02:04:41].

### Key Components

1.  **Multi-resolution Hash Encodings:**
    *   Uses multiple 3D hash grids at different resolutions (e.g., coarse to fine) [00:04:22, 01:00:58].
    *   Each hash entry stores an encoding feature, mapping a 3D position (key) to a feature vector (value) [00:04:30, 01:01:17].
    *   Features across all resolutions are concatenated to form a single feature vector [01:03:48].
    *   These encoded features are then passed to shallow (not many layers) multi-layer perceptrons (MLPs) [01:04:51]. One MLP is for the SDF, and another for color [00:45:25].

2.  **Numerical Gradients for Higher-Order Derivatives:**
    *   [[goshan_splat_optimization_for_3d_reconstruction | Numerical gradients]] are used to compute higher-order derivatives (e.g., surface normals) [00:05:34].
    *   Analytical gradients, while precise, are not continuous across space under tri-linear interpolation when applied to hash encodings [01:15:48]. This discontinuity makes it hard to get smooth surface normals across cell borders [01:16:07].
    *   [[goshan_splat_optimization_for_3d_reconstruction | Numerical gradients]] overcome this locality issue by allowing optimization updates to propagate beyond the single local hash grid cell to multiple grid cells simultaneously [01:25:13, 01:29:56].
    *   This acts as a smoothing operation on the SDF [01:25:52, 01:33:10].
    *   For example, to compute the X-component of the surface normal, two additional SDF samples are taken along each axis (plus and minus Epsilon) around the point `x_i` [01:34:40]. This means six total samples for 3D space [01:35:06].

3.  **Course-to-Fine Optimization Schedule:**
    *   This strategy helps shape the loss landscape to avoid falling into false local minima [01:36:17].
    *   Neural Angelo starts with a coarse resolution (larger step size for [[goshan_splat_optimization_for_3d_reconstruction | numerical gradients]]) [01:40:08, 01:52:50].
    *   Progressively, finer hash grid resolutions are activated during optimization as the step size decreases [01:41:51, 01:53:20]. This allows for a quick "rough" version, which then gets refined with more optimization [01:42:18].
    *   The resolution (V) and the step size (Epsilon) are the two hyper-parameters controlling this [01:39:52].

### Regularization and Losses

Neural Angelo uses a total loss function that combines several components [01:45:35]:
*   **Color Loss (L_RGB):** The primary loss, based on the L1 difference between the rendered pixel color and the actual input image pixel color [00:52:11].
*   **Iconal Loss (L_Ike):** A regularization term that penalizes deviations from the ideal SDF property where the magnitude of its gradient should be equal to one [01:10:05, 01:12:02]. This loss typically ensures a valid SDF representation [01:10:59].
*   **Curvature Regularization (L_Curve):** Imposes a prior by regularizing the mean curvature of the SDF to encourage smoother reconstructed surfaces [01:44:10]. A trade-off exists, as too much smoothing can lose fine details like brick textures [02:03:04]. The strength of this loss (W_curve) is initially small and increases linearly during training [02:03:51].
*   **Weight Decay:** Applied over all parameters to prevent single-resolution features from dominating the final result [01:42:43].

> [!TIP] End-to-End Learning
> All network parameters, including MLPs and hash encodings, are trained jointly end-to-end [01:46:06].

## Advantages and Results

*   **High Fidelity:** Significantly surpasses previous methods in reconstruction accuracy and view synthesis quality [00:08:29, 02:05:14].
*   **No Auxiliary Data:** Achieves strong results using only monocular RGB images, without requiring explicit auxiliary inputs like depth sensors, segmentation, or structured light information [02:00:53, 00:08:01].
*   **Detailed Large-Scale Reconstruction:** Capable of reconstructing detailed large-scale scenes from RGB video captures [00:08:40].
*   **Progressive Level of Detail (LOD):** The course-to-fine optimization naturally yields multiple versions of the asset at different levels of detail, similar to what's used in video games [01:59:17].

## Comparisons

Neural Angelo shows superior quantitative and qualitative results compared to other methods on benchmarks like the DTU and Tanks & Temples datasets [01:56:39, 02:01:10]:
*   **Neural Warp:** Often predicts surfaces for the sky and background [01:59:14].
*   **Noose:** Neural Angelo recovers higher fidelity and denser surfaces [01:59:10].
*   **Instant NGP:** Neural Angelo builds upon the multi-resolution hash encoding idea pioneered in Instant NGP [01:54:50].

> [!WARNING] Data Set Limitations
> While Neural Angelo uses only RGB images, some benchmark datasets like DTU utilize robot-held cameras for image capture [01:47:03]. This provides highly accurate camera pose information, which is easier than handheld capture [01:47:16]. Ground truth data for evaluation is often obtained from structured light scanners or lidar sensors, which are themselves approximations [01:48:04, 01:49:18].

Future work includes exploring more efficient sampling strategies to accelerate the training process [02:06:06].