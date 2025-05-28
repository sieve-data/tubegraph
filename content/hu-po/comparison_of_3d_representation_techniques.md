---
title: Comparison of 3D Representation Techniques
videoId: BRgm5vteAjQ
---

From: [[hu-po]] <br/> 

The field of computer vision is currently experiencing an "arms race" in [[3D Representations and Their Applications | 3D scene representations]] <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. Key contenders include Neural Radiance Fields (NeRFs), Gaussian Splats (3DGS), and the newly emerging Gaussian Surfels <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This article explores these methods, their advantages, disadvantages, and how they compare in terms of surface reconstruction quality, rendering speed, and underlying principles.

## Gaussian Surfels

Gaussian Surfels are a novel point-based representation proposed in a paper released on April 27, 2024 <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>. They aim to combine the flexible optimization of 3D Gaussian points with the surface alignment properties of "surfels" <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.

### What are Gaussian Surfels?
A surfel is fundamentally a flattened 3D Gaussian, achieved by setting the z-scale of the 3D Gaussian point to zero, effectively transforming the original 3D ellipsoid into a 2D ellipse (or disc) <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a> <a class="yt-timestamp" data-t="21:42:00">[21:42:00]</a>. This means a Gaussian Surfel has no thickness in its z-dimension <a class="yt-timestamp" data-t="28:31:00">[28:31:00]</a>. The concept of surfels itself is not new, originating from a paper published in 2000 <a class="yt-timestamp" data-t="23:02:00">[23:02:00]</a>.

Each Gaussian Surfel kernel possesses several properties:
*   **Position**: The X, Y, Z coordinates of the kernel's center <a class="yt-timestamp" data-t="26:44:00">[26:44:00]</a>.
*   **Orientation/Rotation**: Represented by a quaternion (four numbers) <a class="yt-timestamp" data-t="26:56:00">[26:56:00]</a>.
*   **Opacity**: A single number indicating how transparent the surfel is <a class="yt-timestamp" data-t="27:13:00">[27:13:00]</a>.
*   **Spherical Harmonic Coefficients**: Encode view-dependent direction <a class="yt-timestamp" data-t="27:20:00">[27:20:00]</a>.
*   **Scaling Factors (Covariance Matrix)**: Determine the spread and shape of the 2D ellipse <a class="yt-timestamp" data-t="27:27:00">[27:27:00]</a> <a class="yt-timestamp" data-t="27:41:00">[27:41:00]</a>.

### Advantages
*   **Clear Normal Direction**: Flattening the Gaussian allows the local z-axis to be treated as the normal direction <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>. This provides clear guidance to the optimizer, significantly improving optimization stability and surface alignment <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a> <a class="yt-timestamp" data-t="24:39:00">[24:39:00]</a>.
*   **Improved Surface Reconstruction**: The ability to align normals with the surface allows for additional learning signals <a class="yt-timestamp" data-t="25:21:00">[25:21:00]</a> <a class="yt-timestamp" data-t="30:09:00">[30:09:09]</a>. Gaussian Surfels achieve superior performance in surface reconstruction compared to state-of-the-art neural volume rendering and point-based rendering methods <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>. They excel at reconstructing noise-free surfaces and capturing intricate details <a class="yt-timestamp" data-t="01:12:51">[01:12:51]</a>.
*   **Random Initialization**: Unlike many Gaussian Splatting methods that rely on [[structure_from_motion | Structure-from-Motion]] (SFM) pipelines for initialization, Gaussian Surfels can be initialized with random positions and rotations, simplifying the setup process <a class="yt-timestamp" data-t="54:20:00">[54:20:00]</a> <a class="yt-timestamp" data-t="56:26:00">[56:26:00]</a>.
*   **Open Surfaces**: Gaussian Surfels do not assume closed surfaces, making them suitable for reconstructing open surfaces, unlike signed distance function (SDF) representations <a class="yt-timestamp" data-t="01:06:45">[01:06:45]</a>.

### Disadvantages
*   **Complicated Pipeline**: The optimization process involves multiple loss functions: photometric loss, normal prior loss, opacity loss, depth normal consistency loss, and mask loss <a class="yt-timestamp" data-t="35:07:00">[35:07:00]</a>. Each of these losses has specific weights that act as hyperparameters requiring tuning <a class="yt-timestamp" data-t="35:50:00">[35:50:00]</a>.
*   **Custom Learning Rates**: Different properties of the surfels (position, scale, opacity, view-dependent colors) use custom learning rates, which also need to be tuned manually <a class="yt-timestamp" data-t="57:50:00">[57:50:00]</a>.
*   **Gradient Scaling**: The gradient from the normal loss is scaled by a factor of 10, a "magic number" that can be fragile <a class="yt-timestamp" data-t="58:38:00">[58:38:00]</a>.
*   **Specular Reflections**: The method struggles with accurate surface reconstruction in areas with strong specular reflections <a class="yt-timestamp" data-t="01:12:51">[01:12:51]</a>.

### Surface Reconstruction in Gaussian Surfels
To achieve high-quality surface meshes from Gaussian Surfel point sets, a multi-step pipeline is used:
1.  **Rendering**: The color, depth, and normal maps are rendered from the Gaussian Surfel representation <a class="yt-timestamp" data-t="32:12:00">[32:12:00]</a>.
2.  **Monocular Priors**: Pre-trained deep learning models (e.g., from Omni data, or potentially Marigold) are used to estimate surface normals and depths from the input RGB images <a class="yt-timestamp" data-t="31:30:00">[31:30:00]</a> <a class="yt-timestamp" data-t="40:53:00">[40:53:00]</a>. This provides a learning signal for normal and depth consistency <a class="yt-timestamp" data-t="39:51:00">[39:51:00]</a>.
3.  **Volumetric Cutting**: This process, similar to densification and pruning in 3DGS, removes erroneous outlier points by analyzing the opacity of voxels in a grid <a class="yt-timestamp" data-t="49:30:00">[49:30:00]</a> <a class="yt-timestamp" data-t="50:47:00">[50:47:00]</a>. This helps eliminate artifacts like surfels "sticking out" from sharp edges <a class="yt-timestamp" data-t="52:03:00">[52:03:00]</a>.
4.  **[[screened_poisson_reconstruction | Screened Poisson Reconstruction]]**: This technique is applied to the fused depth maps to extract the final surface mesh <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>. It is particularly effective for creating watertight surfaces from oriented point sets <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.

## 3D Gaussian Splatting (3DGS)

3D Gaussian Splatting (3DGS) represents 3D scenes using an explicit and topology-free set of Gaussian points <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>. Each point is an explicit entity stored in memory <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>.

### How they work
3DGS utilizes GPU and CUDA-based rasterization with closed-form integration during rendering <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. This eliminates the time-consuming ray-based point sampling used in volume rendering methods like NeRFs <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. The efficiency on GPUs stems from leveraging the GPU's original design as a graphics processing unit, optimized for processes like rasterization <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. This allows for real-time rendering <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

### Advantages
*   **Real-time Rendering**: A major advantage over NeRFs, as it can render novel views very quickly <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.
*   **Explicit Representation**: Points are directly stored, which can be beneficial for certain applications.

### Disadvantages and [[challenges_in_3d_gaussian_representation | Challenges]]
*   **Non-zero Thickness**: 3D Gaussians resemble ellipsoids with non-zero thickness along each axis, hindering their precise alignment with actual surfaces. This results in a "bubbly" or "fuzzy" appearance when trying to extract surfaces <a class="yt-timestamp" data-t="01:17:33">[01:17:33]</a>.
*   **Ambiguity in Normal Direction**: There's ambiguity in determining the normal for each 3D Gaussian. The normal axis can change arbitrarily during optimization, meaning the normals of individual Gaussians don't reliably correspond to the surface normal <a class="yt-timestamp" data-t="01:18:43">[01:18:43]</a>.
*   **Sharp Edges**: The alpha blending process used in rendering can introduce bias at sharp surface edges, as Gaussians may extend beyond the true edge <a class="yt-timestamp" data-t="01:19:27">[01:19:27]</a>.
*   **Initialization**: Often requires initialization from [[structure_from_motion | Structure-from-Motion]] (SFM) point clouds, which can be "crusty and shitty and old" <a class="yt-timestamp" data-t="00:55:02">[00:55:02]</a> <a class="yt-timestamp" data-t="00:55:36">[00:55:36]</a>.

## Neural Radiance Fields (NeRFs)

NeRFs represent scenes implicitly, storing the appearance and geometry within the weights of a neural network (typically a multi-layer perceptron) <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.

### How they work
NeRFs use ray-based point sampling and volume rendering. For each pixel in an image, a ray is cast through the neural volume. Multiple points are sampled along this ray, and at each sample point, the neural network is queried to determine color and opacity. These values are then integrated to produce the final pixel color <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

### Advantages
*   **"Beautiful" Solution**: The implicit representation, where a small neural network learns the scene's geometry and appearance, is considered an elegant approach <a class="yt-timestamp" data-t="01:13:13">[01:13:13]</a>.

### Disadvantages
*   **Time-Consuming Rendering**: The ray-based sampling process involves multiple inferences of the neural network per ray (and many rays per image), making rendering slow and inefficient <a class="yt-timestamp" data-t="01:12:20">[01:12:20]</a>.
*   **Overly Smooth Surfaces**: NeRFs, especially those using signed distance functions (SDFs) to represent surfaces (e.g., NeuS2), tend to produce overly smooth surfaces, losing sharp details <a class="yt-timestamp" data-t="01:06:56">[01:06:56]</a> <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

## Mesh and Texture Representation

This is the traditional industry standard for 3D representation, used in CGI and video games for decades <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. It consists of two main components:
*   **Mesh**: A set of vertices defining the object's topology <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   **Texture**: An image mapped onto the mesh to provide color and visual detail <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
This representation explicitly stores the object's topology <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

## [[Comparisons between Gaussian splats and other 3D representation technologies | Comparative Analysis]]

*   **Surface Quality**:
    *   **Gaussian Surfels**: Offer high-quality, noise-free, and detailed surface reconstruction due to explicit normal guidance <a class="yt-timestamp" data-t="01:07:50">[01:07:50]</a> <a class="yt-timestamp" data-t="01:33:35">[01:33:35]</a>. They avoid the "bubbly" artifacts of 3DGS and the overly smooth appearance of NeRFs <a class="yt-timestamp" data-t="01:33:55">[01:33:55]</a>.
    *   **3DGS**: While excellent for rendering photorealistic *images*, they struggle to extract a clean, distinct surface due to the inherent thickness of the 3D Gaussians <a class="yt-timestamp" data-t="01:17:33">[01:17:33]</a>.
    *   **NeRFs**: Often produce very smooth, visually appealing surfaces, but can lose sharp details and right angles found in real-world objects <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a> <a class="yt-timestamp" data-t="01:34:57">[01:34:57]</a>.

*   **Rendering Speed**:
    *   **3DGS and Gaussian Surfels**: Leverage GPU rasterization, allowing for real-time rendering, a significant speed advantage over NeRFs <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a> <a class="yt-timestamp" data-t="01:35:50">[01:35:50]</a>.
    *   **NeRFs**: Slower to render new views due to ray-based sampling and multiple neural network inferences <a class="yt-timestamp" data-t="01:12:20">[01:12:20]</a>.

*   **Efficiency and File Size**:
    *   While not explicitly stated, Gaussian Surfels, by being flattened and aligning closely with surfaces, theoretically might require fewer points to represent a scene compared to 3DGS, which uses numerous semi-transparent bubbles to create the *appearance* of a surface <a class="yt-timestamp" data-t="01:29:17">[01:29:17]</a>.

## [[Potential applications and future directions in 3D scene representations | Future Directions]]

*   **Dynamic Scenes**: Current 3D representations like Gaussian Splats are primarily static. Adding a time dimension to the properties of individual splats (position, rotation, opacity) can enable [[potential_applications_and_future_directions_in_3d_scene_representations | dynamic scenes]] <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>. However, it's speculative if the high opacity and strict surface alignment of surfels would make them harder to deform dynamically compared to the "deformable blob" nature of 3DGS <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a>.
*   **Physics Integration**: For applications like video games, integrating physical properties (elasticity, weight, gravity, collision detection, friction) into 3D representations is crucial. This would involve adding physics packages, a nascent area for splat-based methods <a class="yt-timestamp" data-t="01:01:11">[01:01:11]</a>.
*   **Advanced Lighting and Reflections**: Current methods often rely on spherical harmonics to encode view-dependent effects, including lighting and reflections <a class="yt-timestamp" data-t="01:18:04">[01:18:04]</a>. However, this is limited for complex phenomena like strong specular reflections or subsurface scattering <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a> <a class="yt-timestamp" data-t="01:21:26">[01:21:26]</a>. Future work may involve dedicated neural networks for view-dependent color that can incorporate explicit lighting features (e.g., environment lighting, shadows) to achieve higher quality and more realistic rendering <a class="yt-timestamp" data-t="01:19:51">[01:19:51]</a>. Techniques like [[multiresolution_hash_grids_for_3d_representation | hash encoding]] (as seen in Neural Angelo) could be integrated to efficiently store and query lighting information <a class="yt-timestamp" data-t="01:39:55">[01:39:55]</a>.
*   **Optimization of [[techniques_for_optimizing_and_refining_3d_models | Optimization and Refinement]]**: Continued research aims to simplify the complex pipelines and reduce the number of hyperparameters (e.g., custom learning rates, gradient scaling factors) that currently require manual tuning for methods like Gaussian Surfels <a class="yt-timestamp" data-t="01:28:30">[01:28:30]</a>.