---
title: Optimization Techniques in Surfels
videoId: BRgm5vteAjQ
---

From: [[hu-po]] <br/> 

[[introduction_to_gaussian_surfels | Gaussian Surfels]] are a novel point-based representation designed to combine the advantages of flexible [[optimization_methods_in_machine_learning | optimization]] procedures found in 3D Gaussian Splatting (3DGS) points with the surface alignment property of traditional surfels <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>. They represent a new contender in the "3D representation arms race" that previously saw the rise of Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Core Concept
A [[introduction_to_gaussian_surfels | Gaussian Surfel]] is created by setting the z-scale of a 3D Gaussian point to zero, effectively flattening the original 3D ellipsoid into a 2D ellipse or disc <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>. This design provides clear guidance to the [[optimization_methods_in_machine_learning | optimizer]] by treating the local z-axis as the normal direction, which significantly improves [[optimization_methods_in_machine_learning | optimization]] stability in surface alignment <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### Properties
Each [[introduction_to_gaussian_surfels | Gaussian Surfel]] is an unstructured kernel with several properties:
*   **Position (p)**: The XYZ coordinates of the kernel's center <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>.
*   **Orientation/Rotation (q)**: Represented by a quaternion, defining the 3D orientation of the ellipse <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.
*   **Opacity (alpha)**: A single number representing how transparent the surfel is <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>.
*   **Spherical Harmonic Coefficients (c)**: Encode view-dependent color information <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.
*   **Scaling Factors (s)**: Define the shape of the 2D ellipse (covariance matrix) <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>. The z-dimension scaling factor is set to zero to flatten the Gaussian <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
*   **Normal (n)**: Can be directly computed from the last column of the rotation matrix <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>.

## Comparison to Other [[optimization_techniques_and_challenges_for_3d_scene_representation | 3D Scene Representation]]s

### NeRFs
*   **Implicit Representation**: Stores the weights of a neural network that implicitly define the scene's appearance and geometry <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Rendering**: Uses ray-based point sampling, where rays are projected for each pixel, and multiple points are sampled along each ray for inference. This makes NeRFs computationally inefficient and slow for real-time rendering <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
*   **Surface Quality**: Can produce overly smooth surfaces, leading to a loss of intricate details, especially sharp edges <a class="yt-timestamp" data-t="01:17:11">[01:17:11]</a>.
*   **Training Time**: Often takes longer to train compared to Gaussian-based methods <a class="yt-timestamp" data-t="01:10:01">[01:10:01]</a>.

### 3D Gaussian Splatting (3DGS)
*   **Explicit, Topology-Free Representation**: Represents appearance and geometry through a set of explicit Gaussian points, without a defined topology (no explicit connections between points) <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   **Rendering**: Utilizes GPU and CUDA-based [[rendering_technology_and_algorithms | rasterization]] with closed-form integration, making it significantly faster for real-time rendering than NeRFs <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
*   **Surface Issues**:
    *   **Non-zero thickness**: 3D Gaussians resemble ellipsoids with non-zero thickness, hindering close alignment with actual surfaces, leading to a "bubbly" appearance when visualizing surfaces <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
    *   **Ambiguity in Normal Direction**: The normal direction of a 3D Gaussian is not well-defined and can change during [[optimization_methods_in_machine_learning | optimization]], making it difficult to extract meaningful surface normals <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.
    *   **Sharp Edges**: Alpha blending during [[rendering_technology_and_algorithms | rendering]] can introduce bias, making it difficult to model sharp surface edges accurately <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

### Gaussian Surfels
Gaussian Surfels address the limitations of 3DGS by flattening the Gaussians into 2D ellipses. This allows for a meaningful normal vector, which can be used as an additional learning signal during [[optimization_methods_in_machine_learning | optimization]] <a class="yt-timestamp" data-t="00:25:44">[00:25:44]</a>.

## [[optimization_methods_in_machine_learning | Optimization Techniques]]

The [[optimization_methods_in_machine_learning | optimization]] process for [[introduction_to_gaussian_surfels | Gaussian Surfels]] is multi-faceted and involves several loss functions and strategies:

### Loss Functions
The total loss is a weighted sum of five different terms <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>:
1.  **Photometric Loss ($L_P$)**: This is the primary reconstruction loss, similar to 3DGS. It combines an L1 term (80%) and a DSSIM term (20%) to minimize the difference between the rendered image and the input image <a class="yt-timestamp" data-t="00:36:19">[00:36:19]</a>. This loss drives the surfels to accurately represent the visual appearance of the scene <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>.
2.  **Normal Prior Loss ($L_N$)**: Enforces that the surfel's local z-axis (its normal) aligns with the surface normal <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>. This loss is crucial as it leverages the meaningful normal direction of surfels. The normal information for the input images is obtained using a pre-trained monocular normal estimator model <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>.
3.  **Depth Normal Consistency Loss ($L_C$)**: Enforces consistency between the rendered depth map and the rendered normal map <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a>. This loss helps correct errors in either depth or normal direction, leading to better surface alignment <a class="yt-timestamp" data-t="00:42:52">[00:42:52]</a>. It ensures that the normal derived from the depth map (by analyzing neighboring points) matches the surfel's intrinsic normal <a class="yt-timestamp" data-t="00:41:56">[00:41:56]</a>.
4.  **Opacity Loss ($L_\alpha$)**: Promotes non-transparent surfaces by encouraging each Gaussian's opacity to be either near zero or near one <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>. This reduces the "thickness" observed in 3DGS, as surfels become either fully opaque or completely transparent, leading to a thinner and potentially more efficient representation <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.
5.  **Mask Loss ($L_M$)**: Mentioned as part of the overall loss but not explicitly detailed in the transcript <a class="yt-timestamp" data-t="00:35:31">[00:35:31]</a>.

### Volumetric Cutting (Densification and Pruning)
Similar to 3DGS, [[introduction_to_gaussian_surfels | Gaussian Surfels]] employ strategies for dynamically adding and removing points during [[optimization_methods_in_machine_learning | optimization]] <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. They use a method called "volumetric cutting" to remove erroneous outlier surfels <a class="yt-timestamp" data-t="00:49:43">[00:49:43]</a>. This involves constructing a voxel grid and pruning voxels (and the surfels within them) that have low accumulated opacity, indicating they are far from the foreground or background <a class="yt-timestamp" data-t="00:50:52">[00:50:52]</a>. This helps eliminate floating artifacts and maintain a clean surface <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>.

### Initialization
A significant advantage of [[introduction_to_gaussian_surfels | Gaussian Surfels]] is their ability to initialize from random positions and rotations, without relying on classic structure-from-motion (SfM) pipelines that are often "crusty and shitty and old" <a class="yt-timestamp" data-t="00:54:20">[00:54:20]</a>. The strength of their loss functions, particularly those involving normals, allows for robust convergence from random initializations <a class="yt-timestamp" data-t="00:56:19">[00:56:19]</a>.

## Surface Reconstruction
Once the [[introduction_to_gaussian_surfels | Gaussian Surfels]] are optimized, a surface mesh can be extracted using a technique called "screened Poisson reconstruction" <a class="yt-timestamp" data-t="00:47:59">[00:47:59]</a>. This method creates watertight surfaces from oriented point sets, which perfectly aligns with the properties of [[introduction_to_gaussian_surfels | Gaussian Surfels]] (a collection of points with defined normal orientations) <a class="yt-timestamp" data-t="00:48:15">[00:48:15]</a>.

## Challenges and Limitations
Despite their advantages, [[introduction_to_gaussian_surfels | Gaussian Surfels]] and their [[optimization_methods_in_machine_learning | optimization]] present certain challenges:

*   **Hyperparameter Tuning**: The pipeline is considered complicated due to the number of loss functions and their associated weights, which are hyperparameters that need to be carefully tuned <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   **Custom Learning Rates**: Different properties of the surfels (position, scale, opacity, view-dependent colors) use custom learning rates, which adds another layer of complexity to the [[optimization_methods_in_machine_learning | optimization]] process <a class="yt-timestamp" data-t="00:57:48">[00:57:48]</a>.
*   **Gradient Scaling**: The gradient based on the normal is scaled by a factor of 10 to guide rotation, indicating the presence of "very fragile little magic numbers" in the [[optimization_methods_in_machine_learning | optimization]] scheme <a class="yt-timestamp" data-t="00:59:09">[00:59:09]</a>.
*   **Specular Reflections**: The method struggles with accurate surface reconstruction in areas with strong specular reflections <a class="yt-timestamp" data-t="01:12:55">[01:12:55]</a>. This is a common problem in 3D reconstruction and is exacerbated by the reliance on spherical harmonics for view-dependent effects <a class="yt-timestamp" data-t="01:15:15">[01:15:15]</a>. Future work might involve using neural networks to handle view-dependent colors for better reflection handling <a class="yt-timestamp" data-t="01:15:48">[01:15:48]</a>.
*   **Dynamic Scenes**: While 3DGS can be extended to dynamic scenes by adding time dependence to point properties, it is hypothesized that the high opacity and strict surface alignment requirements of surfels might make them harder to use for dynamic [[optimization_techniques_and_challenges_for_3d_scene_representation | 3D Scene Representation]]s compared to the "weird deformable blob of semi-transparent bubbles" of 3DGS <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a>.