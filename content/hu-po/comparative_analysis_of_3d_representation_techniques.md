---
title: Comparative Analysis of 3D Representation Techniques
videoId: BRgm5vteAjQ
---

From: [[hu-po]] <br/> 

The field of computer vision is currently engaged in an "arms race" for superior [[3d_scene_representation_and_simulation | 3D representation]] techniques <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. Traditionally, [[comparison_between_gaussian_splats_and_traditional_3d_representation_methods | 3D scenes]] have been represented using meshes and textures, an industry standard for decades <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>. More recently, [[3d_representation_techniques_nerfs_vs_gausssian_splats | Neural Radiance Fields (Nerfs)]] emerged, followed by [[3d_representation_techniques_nerfs_vs_gausssian_splats | 3D Gaussian Splatting (3DGS)]], and now, Gaussian Surfels are being explored <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. Each method offers unique advantages and disadvantages, particularly in terms of rendering speed, surface quality, and [[optimization_techniques_and_challenges_for_3d_scene_representation | optimization techniques]].

## Gaussian Surfels

Gaussian Surfels are a novel [[3d_scene_representation_and_simulation | point-based representation]] proposed to combine the flexible [[optimization_techniques_and_challenges_for_3d_scene_representation | optimization]] of 3D Gaussians with the surface alignment property of traditional surfels <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>. The core idea involves directly setting the z-scale of 3D Gaussian points to zero, effectively flattening the original 3D ellipsoid into a 2D ellipse or disc <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

### Key Characteristics:
*   **Flattened Gaussians** <a class="yt-timestamp" data-t="21:42:00">[21:42:00]</a>: Unlike 3D Gaussian Splats which are "little bubbles" or ellipsoids <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>, surfels are 2D ellipses. This allows their normal direction (local z-axis) to align perfectly with the object's surface <a class="yt-timestamp" data-t="22:18:00">[22:18:00]</a>.
*   **Surface Alignment** <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>: The defined normal direction provides clear guidance to the optimizer, significantly improving optimization stability and surface alignment <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.
*   **Optimization** <a class="yt-timestamp" data-t="35:07:00">[35:07:00]</a>:
    *   Utilizes a complex pipeline with multiple loss functions: photometric loss, normal prior loss, opacity loss, depth-normal consistency loss, and mask loss <a class="yt-timestamp" data-t="35:17:00">[35:17:17]</a>.
    *   Leverages pre-trained monocular normal and depth estimators (e.g., from Omni data or Marigold) to provide additional learning signals from real-world images <a class="yt-timestamp" data-t="31:30:00">[31:30:00]</a>.
    *   The depth-normal consistency loss helps correct both depth and normal directions, leading to improved reconstruction quality <a class="yt-timestamp" data-t="43:40:00">[43:40:00]</a>.
    *   Opacity loss promotes non-transparent surfaces, encouraging Gaussians to be either fully opaque or fully transparent <a class="yt-timestamp" data-t="45:40:00">[45:40:00]</a>.
*   **Initialization** <a class="yt-timestamp" data-t="54:20:00">[54:20:00]</a>: A significant advantage is the ability to initialize Gaussian Surfels with random positions and rotations, unlike many 3DGS pipelines that require [[optimization_techniques_and_challenges_for_3d_scene_representation | Structure-from-Motion (SfM)]] for initialization <a class="yt-timestamp" data-t="56:26:00">[56:26:00]</a>.
*   **Surface Reconstruction** <a class="yt-timestamp" data-t="47:56:00">[47:56:00]</a>: After optimization, a surface mesh is extracted using methods like Screened Poisson Reconstruction, which creates watertight surfaces from oriented point sets <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>.
*   **Volumetric Cutting**: A technique similar to densification and pruning in 3DGS, used to remove erroneous or outlier Gaussian points, often those with low opacity <a class="yt-timestamp" data-t="50:00:00">[50:00:00]</a>.

### Performance and Limitations:
*   **Quality**: Gaussian Surfels achieve superior surface reconstruction quality compared to state-of-the-art neural volume rendering and point-based rendering methods, excelling in noise-free surfaces and intricate details <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
*   **Training Time**: Shows fast training times, often comparable or better than other methods for surface quality <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>.
*   **Complexity**: The optimization pipeline involves numerous hyperparameters, including different learning rates for various Gaussian properties and gradient scaling, making it potentially fragile and difficult to tune <a class="yt-timestamp" data-t="57:27:00">[57:27:00]</a>.
*   **Specular Reflections**: Struggles with accurate surface reconstruction in areas with strong specular reflections <a class="yt-timestamp" data-t="01:12:52">[01:12:52]</a>.
*   **Dynamic Scenes**: While 3DGS can be extended to [[omnimotion_and_quasi3d_video_representation | dynamic scenes]], the high opacity and perfect alignment requirements of surfels might make their use for dynamic objects more challenging <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>.

## 3D Gaussian Splatting (3DGS)

3DGS represents [[3d_scene_representation_and_simulation | appearance and geometry]] through a set of explicit and topology-free Gaussian points <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>.

### Key Characteristics:
*   **Explicit Representation** <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>: Gaussian points are literally stored in memory, making them a point-based representation <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.
*   **Topology-Free** <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>: Unlike traditional meshes, 3DGS does not explicitly store connectivity between points, just a collection of independent points <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>.
*   **Fast Rendering**: Utilizes GPU and CUDA-based rasterization with closed-form integration during rendering, eliminating the need for time-consuming ray-based point sampling seen in volume rendering (Nerfs) <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>. This efficiency is likened to the AlexNet moment in deep learning, where GPU optimization led to significant breakthroughs <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   **Dynamic Point Management**: Gaussians are dynamically added and removed during the optimization process (densification and pruning) <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>.

### Disadvantages for Surface Reconstruction:
*   **Non-Zero Thickness**: 3D Gaussians (ellipsoids) have non-zero thickness, hindering their precise alignment with actual surfaces. This results in a "bubbly" or "fuzzy" appearance when attempting to reconstruct surfaces from 3DGS <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>.
*   **Ambiguity in Normal Direction**: The normal direction for each 3D Gaussian is ambiguous and can change during [[optimization_techniques_and_challenges_for_3d_scene_representation | optimization]], lacking a clear relationship to the overall surface normal <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>. This prevents the use of normal-based learning signals for surface refinement <a class="yt-timestamp" data-t="39:35:00">[39:35:00]</a>.
*   **Sharp Edge Modeling**: Alpha blending can introduce bias, making it difficult to model sharp surface edges accurately, as Gaussians may extend beyond the true edge <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>.
*   **Initialization**: Often requires initialization from [[optimization_techniques_and_challenges_for_3d_scene_representation | Structure-from-Motion (SfM)]] point clouds, which can be "crusty and shitty" <a class="yt-timestamp" data-t="55:02:00">[55:02:00]</a>.

## Neural Radiance Fields (Nerfs)

Nerfs are an [[3d_scene_representation_and_simulation | implicit 3D representation]] where the scene's [[3d_scene_representation_and_simulation | appearance and geometry]] are stored within the weights of a neural network (multi-layer perceptron or MLP) <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.

### Key Characteristics:
*   **Implicit Representation** <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>: Points are not explicitly stored; instead, a neural network implicitly learns the scene's properties.
*   **Ray-Based Rendering**: Rendering involves casting rays from each pixel and sampling multiple points along each ray. Each sample requires an inference from the neural network, making the process computationally intensive and slow <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>.
*   **Smooth Surfaces**: Nerfs often produce overly smooth surfaces, which can be visually appealing for some objects (e.g., a nose) <a class="yt-timestamp" data-t="01:16:55">[01:16:55]</a>.
*   **Signed Distance Functions (SDFs)**: Some Nerf variants (like "Noose") use SDFs to implicitly represent surfaces, which generally assume closed surfaces <a class="yt-timestamp" data-t="01:06:50">[01:06:50]</a>.

### Disadvantages:
*   **Slow Rendering**: The ray-based sampling process is time-consuming, preventing real-time rendering in many scenarios <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>.
*   **Loss of Detail**: The tendency to produce smooth surfaces can lead to a loss of intricate details and sharp edges, such as windows with right angles <a class="yt-timestamp" data-t="01:17:36">[01:17:36]</a>.
*   **Lighting and Reflections**: Like 3DGS, standard Nerfs (using spherical harmonics) may struggle with complex lighting effects like specular reflections, and often require separate neural networks for better view-dependent color handling <a class="yt-timestamp" data-t="01:19:18">[01:19:18]</a>.

## Traditional Mesh and Texture Representation

This method has been the industry standard for decades, used in CGI and video games <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>.

### Key Characteristics:
*   **Mesh**: A set of vertices that represent the object's topology (how points connect to form surfaces) <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>.
*   **Texture**: An image mapped onto the mesh to provide color and visual detail <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>.
*   **Explicit Topology**: The explicit storage of how vertices connect defines the object's topology <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>.
*   **GPU Optimization**: GPUs were originally designed as "graphics processing units" and are highly optimized for rasterization, the process of rendering images from mesh and texture models <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>.
*   **Physics Integration**: Well-established methods and physics packages exist to add physical properties (e.g., elasticity, gravity, friction, collision) to meshes for interactive applications like video games <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a>.

## Conclusion

The "arms race" in 3D representation highlights a continuous trade-off between realism, rendering speed, and ease of [[optimization_techniques_and_challenges_for_3d_scene_representation | optimization]]. While traditional meshes remain robust for interactive environments, [[3d_representation_techniques_nerfs_vs_gausssian_splats | Nerfs]] offer beautiful implicit representations but suffer from rendering speed. [[3d_representation_techniques_nerfs_vs_gausssian_splats | 3D Gaussian Splatting]] gained traction due to its real-time rendering capabilities by leveraging GPU rasterization, even with its limitations in surface quality. Gaussian Surfels appear to be the next step, improving surface reconstruction by flattening Gaussians to enable strong normal-based learning signals, making them more robust in terms of initialization and surface detail, though they introduce complexity in their [[optimization_techniques_and_challenges_for_3d_scene_representation | pipeline]] and may face [[limitations_and_assumptions_of_dynamic_3d_modeling | challenges with dynamic scenes]]. The future of 3D representations will likely see further convergence and hybrid approaches, possibly incorporating explicit lighting models and advanced physics for truly immersive and interactive experiences.