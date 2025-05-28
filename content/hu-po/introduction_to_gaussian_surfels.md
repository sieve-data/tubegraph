---
title: Introduction to Gaussian Surfels
videoId: BRgm5vteAjQ
---

From: [[hu-po]] <br/> 

[[Gaussian Surfels in Computer Vision | Gaussian Surfels]] are a novel point-based representation in computer vision, emerging as a potential challenger in the 3D representation landscape alongside Nerfs and [[gaussian_splatting_and_its_advantages | Gaussian Splats]] <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. This technique, proposed in a paper released on April 27, 2024, titled "High-Quality Surface Reconstruction using Gaussian Surfels," combines the flexible optimization procedures of [[gaussian_splatting_and_its_advantages | 3D Gaussian points]] with the surface alignment properties inherent to surfels <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>. The research originates from Chinese groups like the State Key Lab of CAD and CG, and Style 3D Research <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

## Core Concept
A Gaussian Surfel is created by taking an original 3D Gaussian ellipsoid and flattening it into a 2D ellipse by directly setting its z-scale to zero <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>. This design provides clear guidance to the optimizer by treating the local z-axis as the normal direction, significantly improving optimization stability and surface alignment <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.

Historically, the concept of surfels is not new, dating back to a 2000 paper by Pfister et al. <a class="yt-timestamp" data-t="23:02:00">[23:02:00]</a>. The resurgence of surfels, similar to [[gaussian_splatting_and_its_advantages | Gaussian Splats]], is largely due to their efficiency on GPUs <a class="yt-timestamp" data-t="30:48:00">[30:48:00]</a>.

### Properties
Each Gaussian Surfel is an unstructured Gaussian kernel with several properties:
*   **Position:** The XYZ coordinates of the kernel's center <a class="yt-timestamp" data-t="26:44:00">[26:44:00]</a>.
*   **Orientation/Rotation:** Represented by a quaternion, allowing for 3D orientations in 3D space using four numbers <a class="yt-timestamp" data-t="26:56:00">[26:56:00]</a>.
*   **Opacity:** A single number indicating how translucent the surfel is <a class="yt-timestamp" data-t="27:13:00">[27:13:00]</a>.
*   **Spherical Harmonic Coefficients:** Encode view-dependent direction, influencing how the surfel appears from different viewpoints <a class="yt-timestamp" data-t="27:20:00">[27:20:00]</a>.
*   **Scaling Factors:** Define the shape of the 2D ellipse, derived from the covariance matrix <a class="yt-timestamp" data-t="27:27:00">[27:27:00]</a>.

The flattening of the 3D Gaussian is achieved by setting the z-dimension of the scaling factors to zero <a class="yt-timestamp" data-t="28:26:00">[28:26:00]</a>. This allows the normal for each Gaussian kernel to be directly computed from the last column of its rotation matrix <a class="yt-timestamp" data-t="28:46:00">[28:46:00]</a>. Optimizing this normal direction enables the surfels to align effectively with the actual surface of the object <a class="yt-timestamp" data-t="30:09:00">[30:09:00]</a>.

## [[Comparisons between Gaussian splats and other 3D representation technologies | Comparisons with Other 3D Representations]]

### Vs. Nerfs
*   **Representation:** Nerfs implicitly store appearance and geometry using neural network weights, requiring ray-based point sampling for rendering <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>. This makes Nerfs computationally expensive for rendering <a class="yt-timestamp" data-t="12:29:00">[12:29:00]</a>.
*   **Rendering Speed:** [[gaussian_splatting_and_its_advantages | Gaussian Splats]] and Gaussian Surfels utilize GPU and CUDA-based rasterization, eliminating time-consuming ray-based sampling, enabling real-time rendering <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. This is a primary reason for their speed advantage over Nerfs <a class="yt-timestamp" data-t="14:18:00">[14:18:00]</a>.
*   **Surface Quality:** Nerfs, particularly those using signed distance functions (SDFs), tend to produce overly smooth surfaces, leading to a loss of intricate details <a class="yt-timestamp" data-t="13:42:00">[13:42:00]</a>, <a class="yt-timestamp" data-t="17:18:00">[17:18:00]</a>, <a class="yt-timestamp" data-t="18:24:00">[18:24:00]</a>, <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a>. Gaussian Surfels, due to their explicit surface alignment, can capture sharper details <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

### Vs. [[gaussian_splatting_and_its_advantages | Gaussian Splats]] (3DGS)
*   **Thickness:** Standard [[gaussian_splatting_and_its_advantages | 3D Gaussian Splats]] resemble ellipsoids with non-zero thickness along each axis, hindering their close alignment with actual surfaces. This can lead to a "bubbly" appearance in surface reconstructions <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>. Gaussian Surfels overcome this by being flat 2D ellipses <a class="yt-timestamp" data-t="21:39:00">[21:39:00]</a>.
*   **Normal Direction:** [[gaussian_splatting_and_its_advantages | 3D Gaussian Splats]] have ambiguity in determining the normal for each Gaussian, as it can change during optimization without strong guidance <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a>. Gaussian Surfels' flattened nature provides a meaningful local z-axis, allowing for direct normal computation and alignment <a class="yt-timestamp" data-t="22:20:00">[22:20:00]</a>.
*   **Sharp Edges:** Alpha blending in [[gaussian_splatting_and_its_advantages | 3DGS]] can introduce bias at reconstructed surface edges, as Gaussians may extend beyond the true edge <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>. Gaussian Surfels, with their flat profile, are better suited for modeling sharp surface edges and orthogonal structures <a class="yt-timestamp" data-t="34:37:00">[34:37:00]</a>.
*   **Efficiency:** By explicitly aligning with the surface, Gaussian Surfels may require fewer points to represent a scene compared to [[gaussian_splatting_and_its_advantages | 3DGS]], which uses many semi-transparent bubbles to approximate a surface <a class="yt-timestamp" data-t="29:21:00">[29:21:00]</a>.

## Optimization and Pipeline

The optimization of Gaussian Surfels involves a complex pipeline with multiple loss functions, making it potentially more complicated than simpler methods <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>. The total loss function is a weighted sum of five different terms <a class="yt-timestamp" data-t="35:12:00">[35:12:00]</a>:

1.  **Photometric Loss (Lp):** Combines an L1 term and a DSSIM term to minimize the difference between the rendered image and the input image <a class="yt-timestamp" data-t="36:19:00">[36:19:00]</a>. This loss pushes gradients to make the surfels' appearance match the original photos <a class="yt-timestamp" data-t="37:00:00">[37:00:00]</a>.
2.  **Normal Prior Loss (Ln):** Utilizes normals estimated from a pre-trained monocular normal estimator (e.g., from OmniData or Marigold) to guide the surfels' normal directions <a class="yt-timestamp" data-t="31:30:00">[31:30:00]</a>, <a class="yt-timestamp" data-t="40:04:00">[40:04:00]</a>. This is an explicit additional learning signal that [[gaussian_splatting_and_its_advantages | vanilla Gaussian Splats]] lack <a class="yt-timestamp" data-t="25:21:00">[25:21:00]</a>.
3.  **Depth-Normal Consistency Loss (Lc):** Enforces consistency between the rendered depth and the rendered normal <a class="yt-timestamp" data-t="39:14:00">[39:14:00]</a>. It leverages the ability to derive normals from depth maps (by transforming depth pixels to 3D points and computing normals from neighboring points) and compares them to the model's rendered normals <a class="yt-timestamp" data-t="41:40:00">[41:40:00]</a>. This bidirectional consistency helps correct both depth and normal errors <a class="yt-timestamp" data-t="42:30:00">[42:30:00]</a>.
4.  **Opacity Loss (Lo):** Promotes non-transparent surfaces by encouraging each Gaussian's opacity to be near zero or near one, preventing "see-through" points common in [[gaussian_splatting_and_its_advantages | 3DGS]] <a class="yt-timestamp" data-t="45:38:00">[45:38:00]</a>.
5.  **Mask Loss (Lm):** Helps define the foreground and background of the scene <a class="yt-timestamp" data-t="35:31:00">[35:31:00]</a>.

The process involves tuning hyper-parameters for each loss term and using different learning rates for different surfel properties (position, scale, opacity, color) <a class="yt-timestamp" data-t="57:27:00">[57:27:00]</a>. Additionally, the gradient based on the normal is scaled by a factor of 10 to ensure correct rotation and alignment of the surfel ellipses <a class="yt-timestamp" data-t="58:38:00">[58:38:00]</a>.

### Initialisation and Pruning
Unlike most [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] papers that rely on computationally intensive Structure from Motion (SfM) pipelines for initial point cloud generation, Gaussian Surfels can be initialized with random positions and rotations due to the strong learning signals from the normal and depth consistency losses <a class="yt-timestamp" data-t="54:15:00">[54:15:00]</a>, <a class="yt-timestamp" data-t="56:26:00">[56:26:00]</a>.

For refinement, the method employs a "volumetric cutting" technique, similar to densification and pruning in [[gaussian_splatting_and_its_advantages | 3DGS]] <a class="yt-timestamp" data-t="49:41:00">[49:41:00]</a>. This involves constructing a voxel grid and pruning surfels in voxels with low accumulated opacity, effectively removing erroneous or outlier points <a class="yt-timestamp" data-t="50:49:00">[50:49:00]</a>. This helps remove artifacts like surfels sticking out from sharp corners <a class="yt-timestamp" data-t="52:00:00">[52:00:00]</a>.

### Surface Reconstruction
After optimization, a 3D surface mesh is extracted from the optimized Gaussian Surfels using a method called Screened Poisson Reconstruction <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>, <a class="yt-timestamp" data-t="47:56:00">[47:56:00]</a>. This technique is suitable for creating watertight surfaces from oriented point sets, which is exactly what Gaussian Surfels provide <a class="yt-timestamp" data-t="48:15:00">[48:15:00]</a>.

## [[Challenges and Advantages of Gaussian Surfels | Advantages and Limitations]]

### Advantages
*   **Superior Surface Reconstruction:** Gaussian Surfels achieve better surface reconstruction quality than state-of-the-art neural volume rendering (Nerfs) and point-based rendering methods ([[gaussian_splatting_and_its_advantages | 3DGS]]) <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
*   **Noise-Free Surfaces:** The method excels in reconstructing noise-free surfaces and capturing explicit, intricate details <a class="yt-timestamp" data-t="0:51:00">[0:51:00]</a>.
*   **Sharp Detail Capture:** Unlike Nerfs that produce overly smooth results, Gaussian Surfels can model sharp surface edges and maintain fine details <a class="yt-timestamp" data-t="0:51:00">[0:51:00]</a>, <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>.
*   **Open Surface Reconstruction:** The method can reconstruct open surfaces, unlike techniques that rely on signed distance functions which typically assume closed surfaces <a class="yt-timestamp" data-t="0:47:00">[0:47:00]</a>.

### Limitations
*   **Complex Pipeline:** The reliance on numerous loss functions and carefully tuned hyper-parameters (e.g., different learning rates for different properties, gradient scaling) makes the pipeline complex and potentially fragile <a class="yt-timestamp" data-t="58:59:00">[58:59:00]</a>.
*   **Specular Reflections:** The method struggles with accurate surface reconstruction in areas with strong specular reflections (shiny, reflective surfaces), as these dramatically change appearance with view direction <a class="yt-timestamp" data-t="12:52:00">[12:52:00]</a>. This is a common challenge for 3D reconstruction algorithms <a class="yt-timestamp" data-t="15:04:00">[15:04:04]</a>.

## [[Applications and Future Prospects of Gaussian Surfels | Future Directions]]
While currently focused on static 3D representations <a class="yt-timestamp" data-t="01:02:30">[01:02:30]</a>, future work could explore adapting Gaussian Surfels for [[dynamic_3d_gaussian_technique | dynamic scenes]] by adding time dependence to their properties (position, rotation, opacity) <a class="yt-timestamp" data-t="01:02:42">[01:02:42]</a>. However, their high opacity and perfect surface alignment might make them harder to animate smoothly compared to translucent [[gaussian_splatting_and_its_advantages | Gaussian Splats]] <a class="yt-timestamp" data-t="01:03:42">[01:03:42]</a>.

Incorporating more sophisticated view-dependent color rendering, perhaps by using a separate neural network instead of fixed spherical harmonics, could improve handling of complex lighting effects like specular reflections and subsurface scattering <a class="yt-timestamp" data-t="01:15:09">[01:15:09]</a>, <a class="yt-timestamp" data-t="01:21:26">[01:21:26]</a>.