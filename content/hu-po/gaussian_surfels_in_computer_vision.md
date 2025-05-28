---
title: Gaussian Surfels in Computer Vision
videoId: BRgm5vteAjQ
---

From: [[hu-po]] <br/> 

**Gaussian Surfels** represent a novel point-based representation in computer vision, emerging as a potential contender in the realm of 3D representations <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This technique, released on April 27, 2024, by Chinese research groups and Style3D Research, aims to combine the advantages of flexible optimization from [[gaussian_splatting_and_its_advantages | 3D Gaussian points]] with the surface alignment property of surfels <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

## What are Gaussian Surfels?

Gaussian Surfels are a set of unstructured Gaussian kernels, effectively a collection of 3D points <a class="yt-timestamp" data-t="00:26:25">[00:26:25]</a>. They are created by setting the z-scale of [[gaussian_splatting_and_its_advantages | 3D Gaussian points]] to zero, transforming the original 3D ellipsoid into a 2D ellipse <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a> <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>. This design provides clear guidance to the optimizer by treating the local z-axis as the normal direction <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

Each Gaussian surfel possesses several properties:
*   **Position**: The XYZ coordinates of the kernel's center <a class="yt-timestamp" data-t="00:26:44">[00:26:44]</a>.
*   **Orientation/Rotation**: Represented by a quaternion (four numbers) <a class="yt-timestamp" data-t="00:26:56">[00:26:56]</a>.
*   **Opacity**: A single number indicating how transparent the surfel is <a class="yt-timestamp" data-t="00:27:13">[00:27:13]</a>.
*   **Spherical Harmonic Coefficients**: Used to encode view-dependent appearance <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.
*   **Scaling Factors**: Adjust the size of the 2D ellipse <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>.
*   **Covariance Matrix**: Represents the shape and spread of the surfel <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>.

The concept of "surfels" is not new, dating back to a 2000 paper that introduced surface elements as rendering primitives <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.

## Advantages of Gaussian Surfels

Gaussian Surfels offer several key advantages:

*   **Surface Alignment**: By flattening the Gaussians, the local z-axis can be directly interpreted as the normal direction, significantly improving surface alignment <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a> <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>. This allows for an additional learning signal to align surfels with the actual surface <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
*   **Optimization Stability**: The clear guidance provided by the flattened design enhances optimization stability <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **Training Speed**: They are quite fast in terms of training, achieving high quality with a low chamfer distance <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a> <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Random Initialization**: Unlike many [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] papers that require initialization via structure from motion (SfM), Gaussian Surfels can be initialized with random positions and rotations due to the strength of their loss functions <a class="yt-timestamp" data-t="00:54:20">[00:54:20]</a> <a class="yt-timestamp" data-t="00:56:26">[00:56:26]</a>. This removes a significant pain point in the pipeline <a class="yt-timestamp" data-t="00:56:52">[00:56:52]</a>.
*   **Open Surface Reconstruction**: They do not assume closed surfaces, making them suitable for reconstructing open surfaces, unlike signed distance functions (SDFs) often used in implicit representations <a class="yt-timestamp" data-t="01:06:44">[01:06:44]</a>.
*   **Noise-Free & Intricate Details**: The method excels in reconstructing noise-free surfaces and capturing intricate details <a class="yt-timestamp" data-t="01:07:50">[01:07:50]</a> <a class="yt-timestamp" data-t="01:17:26">[01:17:26]</a>.
*   **Potential Efficiency**: In theory, fewer surfels might be needed compared to [[gaussian_splatting_and_its_advantages | Gaussian Splats]] to represent a surface, as they can cover it with a very thin layer without requiring thickness <a class="yt-timestamp" data-t="01:29:17">[01:29:17]</a>.

## Comparisons to Other 3D Representations

### [[gaussian_splatting_and_its_advantages | Gaussian Splatting (3DGS)]]

[[gaussian_splatting_and_its_advantages | 3DGS]] represents appearance and geometry using explicit, topology-free Gaussian points <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. It leverages GPU and CUDA-based rasterization for real-time rendering, making it faster than Nerfs <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a> <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

However, [[challenges_and_advantages_of_gaussian_surfels | 3DGS presents challenges]]:
*   **Non-zero Thickness**: [[gaussian_splatting_and_its_advantages | 3D Gaussian points]] resemble ellipsoids with non-zero thickness, hindering close alignment with actual surfaces. This results in "bubbly" or "fuzzy" textures <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a> <a class="yt-timestamp" data-t="01:33:42">[01:33:42]</a>.
*   **Ambiguity in Normal Direction**: The normal direction for each [[gaussian_splatting_and_its_advantages | 3D Gaussian]] is ambiguous and can change during optimization, lacking a consistent relationship with the surface <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.
*   **Sharp Surface Edges**: Alpha blending in [[gaussian_splatting_and_its_advantages | 3DGS]] can introduce bias, making it difficult to model sharp surface edges due to Gaussian points extending beyond the surface <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

Gaussian Surfels address these by being inherently flat, allowing a meaningful normal vector and leading to cleaner, crispier surfaces <a class="yt-timestamp" data-t="01:33:35">[01:33:35]</a>.

### Nerfs (Neural Radiance Fields)

Nerfs are implicit representations, storing the weights of a neural network (multi-layer perceptron) that implicitly defines the scene's appearance and geometry <a class="yt-timestamp" data-t="00:9:24">[00:09:24]</a>.

Nerfs have distinct characteristics:
*   **Implicit Representation**: Points are not explicitly stored; instead, a neural network is used to generate color and density <a class="yt-timestamp" data-t="00:9:24">[00:09:24]</a>.
*   **Slow Rendering**: They use ray-based point sampling and volume rendering, which is computationally expensive due to multiple inferences per ray for each pixel <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a> <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.
*   **Overly Smooth Surfaces**: Nerfs, especially those using signed distance functions (SDFs), tend to produce overly smooth surfaces, sometimes losing intricate details or sharp angles <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a> <a class="yt-timestamp" data-t="01:17:09">[01:17:09]</a> <a class="yt-timestamp" data-t="01:34:16">[01:34:16]</a>.

## Optimization and Losses

The optimization pipeline for Gaussian Surfels is complex, incorporating five different loss functions that contribute to the final gradients:

1.  **Photometric Loss (Lp)**: Combines an L1 term (80%) and a DSSIM term (20%) to minimize the visual difference between the rendered image and the input image <a class="yt-timestamp" data-t="00:36:19">[00:36:19]</a> <a class="yt-timestamp" data-t="00:37:20">[00:37:20]</a>.
2.  **Normal Prior Loss (Ln)**: Utilizes normals derived from a pre-trained monocular normal estimator (e.g., from OmniData) to guide the surfel normals towards the actual surface normal <a class="yt-timestamp" data-t="00:39:51">[00:39:51]</a> <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a> <a class="yt-timestamp" data-t="00:44:17">[00:44:17]</a>. An L1 loss is also introduced to normalize the gradient of the rendered normal, regularizing surface curvature <a class="yt-timestamp" data-t="00:41:14">[00:41:14]</a> <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a> <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>.
3.  **Opacity Loss (Lo)**: Promotes non-transparent surfaces by encouraging each surfel's opacity to be near zero or near one, preventing "see-through" points common in [[gaussian_splatting_and_its_advantages | Gaussian Splats]] <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a> <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.
4.  **Depth Normal Consistency Loss (Lc)**: Enforces consistency between the rendered depth and the rendered normal <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a> <a class="yt-timestamp" data-t="00:43:09">[00:43:09]</a>. This loss helps correct both depth and normal directions if they are inaccurate, leading to improved reconstruction quality <a class="yt-timestamp" data-t="00:42:49">[00:42:49]</a>.
5.  **Mask Loss (Lm)**: Used to enhance quality with foreground masks <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

The combination of these losses, especially those leveraging normal information, allows Gaussian Surfels to achieve superior surface reconstruction <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a> <a class="yt-timestamp" data-t="00:44:12">[00:44:12]</a>.

### Volumetric Cutting
Similar to the densification and pruning strategies in [[3d_gaussian_splatting_and_instant_splat_pipeline | Gaussian Splatting pipelines]], Gaussian Surfels utilize "volumetric cutting" to remove erroneous outlier points <a class="yt-timestamp" data-t="00:49:37">[00:49:37]</a>. This involves constructing a voxel grid and pruning voxels (and the 3D points within them) that have low accumulated opacity, indicating a large distance from the foreground or background <a class="yt-timestamp" data-t="00:50:52">[00:50:52]</a>.

### Surface Reconstruction
Once the surfels are optimized, a surface mesh is extracted using a screen Poisson reconstruction method <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a> <a class="yt-timestamp" data-t="00:48:03">[00:48:03]</a>. This technique creates watertight surfaces from oriented point sets, which is ideal given the surfels' explicit normal directions <a class="yt-timestamp" data-t="00:48:15">[00:48:15]</a>.

## Challenges and Limitations

Despite their advantages, Gaussian Surfels face certain challenges:
*   **Complexity**: The pipeline is intricate, involving numerous losses with individual weights and custom learning rates for different parameters (position, radius, opacity, view-dependent colors) <a class="yt-timestamp" data-t="00:35:12">[00:35:12]</a> <a class="yt-timestamp" data-t="00:57:48">[00:57:48]</a>. Gradient scaling for the normal is also applied <a class="yt-timestamp" data-t="00:58:38">[00:58:38]</a>. This makes the system potentially fragile due to many "magic numbers" <a class="yt-timestamp" data-t="00:59:17">[00:59:17]</a>.
*   **Specular Reflections**: The method struggles with accurate surface reconstruction in areas with strong specular reflections, as these can cause conflicts in photometric consistency across different views <a class="yt-timestamp" data-t="01:12:51">[01:12:51]</a> <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **[[dynamic_3d_gaussian_technique | Dynamic Scenes]]**: While not explicitly stated as a limitation, the high opacity and perfect alignment requirements for surfels might make it harder to represent [[dynamic_3d_gaussian_technique | dynamic scenes]] compared to the more deformable, semi-transparent blobs of [[gaussian_splatting_and_its_advantages | Gaussian Splats]] <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a>.

## Applications and Future Prospects

Gaussian Surfels demonstrate superior performance in surface reconstruction compared to state-of-the-art neural volume rendering and point-based rendering methods <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a> <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. They have been benchmarked on datasets like DTU (laboratory-captured scenes) and Blended MVS (varying number of images), consistently showing strong geometric quality <a class="yt-timestamp" data-t="01:04:56">[01:04:56]</a> <a class="yt-timestamp" data-t="01:08:37">[01:08:37]</a>.

Future work could explore incorporating more sophisticated rendering capabilities beyond spherical harmonics to better handle complex lighting effects like reflections and subsurface scattering, potentially by using dedicated neural networks for view-dependent color <a class="yt-timestamp" data-t="01:18:11">[01:18:11]</a> <a class="yt-timestamp" data-t="01:20:07">[01:20:07]</a> <a class="yt-timestamp" data-t="01:21:26">[01:21:26]</a>. Additionally, extending Gaussian Surfels to [[dynamic_3d_gaussian_technique | dynamic scenes]] by adding time dependence to their properties remains an area for research <a class="yt-timestamp" data-t="01:03:07">[01:03:07]</a>. The integration of physics properties, as seen in other works, could also enable their use in interactive applications like video games <a class="yt-timestamp" data-t="01:16:11">[01:16:11]</a>.