---
title: Introduction to Gaussian Surfels
videoId: BRgm5vteAjQ
---

From: [[hu-po]] <br/> 

[[Gaussian surfels]] are a novel point-based 3D representation that emerged as a potential new challenger in the [[3d_representation_techniques_nerfs_vs_gausssian_splats | 3D representation]] "arms race," following [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] (3DGS) and NeRFs [00:02:54]. The paper "High-quality Surface Reconstruction Using Gaussian Surfels" was released on April 27, 2024, by Chinese research groups and Style3D Research [00:03:35].

## What are Gaussian Surfels?
[[Gaussian surfels]] combine the advantages of flexible [[Optimization Techniques in Surfels | optimization procedures]] found in 3D Gaussian points with the surface alignment properties of traditional surfels [00:06:26]. This is achieved by directly setting the z-scale of a 3D Gaussian point to zero, effectively flattening the original 3D ellipsoid into a 2D ellipse [00:06:36]. This design provides clear guidance to the optimizer by treating the local z-axis as the normal direction [00:06:43], greatly improving [[Optimization Techniques in Surfels | optimization stability]] and surface alignment [00:06:48].

A [[Gaussian surfel]] is defined as a set of unstructured Gaussian kernels [00:26:25]. Each kernel possesses several properties:
*   **Position:** The XYZ coordinates of the kernel's center [00:26:44].
*   **Orientation (Rotation):** Represented by a quaternion (four numbers in R4) [00:26:56].
*   **Opacity:** A single number indicating how transparent the surfel is [00:27:13].
*   **Spherical Harmonic Coefficients:** Used to encode view-dependent appearance [00:27:20, 01:15:15, 01:22:09].
*   **Scaling Factors:** Define the shape of the 2D ellipse through a covariance matrix [00:27:27, 00:27:41].
    *   The z-scale (Siz) is explicitly set to zero to flatten the 3D Gaussian into a 2D disc [00:28:30].
    *   The normal for each [[Gaussian surfel]] kernel can be directly computed from the last column of its rotation matrix [00:28:46, 00:29:53].

## Origin of Surfels
The concept of surfels is not new. The term "surfels" and their application as "surface elements as rendering primitives" date back to a paper published in 2000 [00:23:09]. In the original surfel paper, they were used to recreate textured meshes by placing small, flat discs along the object's surface [00:23:51].

## Comparison with other 3D Representations
[[Gaussian surfels]] are positioned as an advancement over existing [[3d_representation_techniques_nerfs_vs_gausssian_splats | 3D representation techniques]]:

### [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] (3DGS)
*   **Explicit and Topology-Free:** Both [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] and [[Gaussian surfels]] are explicit, point-based representations, meaning their points are literally stored in memory [00:09:11, 00:09:18]. They are also "topology-free," as there's no inherent connection or surface definition between points, unlike traditional mesh representations [00:09:51, 00:10:51].
*   **Dynamic Adaptation:** Points can be dynamically added and removed during the [[Optimization Techniques in Surfels | optimization process]] (densification and pruning) [00:11:15, 00:29:50].
*   **Rendering Speed:** Both leverage GPU and CUDA-based rasterization, eliminating time-consuming ray-based sampling methods used by NeRFs [00:11:30]. This allows for real-time rendering [00:16:34].
*   **Limitations of 3DGS:**
    *   **Non-Zero Thickness:** Traditional 3DGS points resemble ellipsoids with non-zero thickness, hindering close alignment with actual surfaces [00:17:33]. This leads to a "bubbly" appearance when trying to extract a surface [00:18:03, 01:33:42].
    *   **Ambiguity in Normal Direction:** For 3D Gaussians, the normal direction is ambiguous and can change during [[Optimization Techniques in Surfels | optimization]], making it difficult to relate to the true surface normal [00:18:46].
    *   **Modeling Sharp Edges:** The alpha blending process in 3DGS can introduce bias, making it difficult to model sharp surface edges, as Gaussians may extend beyond the true edge [00:19:27].

### Neural Radiance Fields (NeRFs)
*   **Implicit Representation:** Unlike [[Gaussian surfels]] and [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]], NeRFs implicitly store appearance and geometry as weights of a neural network (multi-layer perceptron) [00:09:22, 00:09:39].
*   **Rendering Process:** NeRFs use ray-based point sampling and volume rendering, which is computationally expensive due to multiple neural network inferences per ray [00:11:35, 00:12:11].
*   **Surface Quality:** NeRFs often produce "overly smooth" surfaces, which can be visually appealing but may lose intricate details or struggle with sharp angles [00:05:05, 01:16:55, 01:34:11].
*   **Closed Surfaces:** Some NeRF variants use signed distance functions (SDFs), which typically assume closed surfaces [01:06:50]. [[Gaussian surfels]] do not have this limitation and can reconstruct open surfaces [01:06:45].

## Advantages of Gaussian Surfels
*   **High-Quality Surface Reconstruction:** [[Gaussian surfels]] yield superior surface reconstruction compared to both [[3D Gaussian Splats for Radiance Field Rendering | vanilla Gaussian Splats]] and state-of-the-art NeRF-based methods [00:04:55, 00:07:29, 01:07:50]. This is largely due to the explicit normal direction derived from their flattened nature [00:30:09].
*   **Faster Training and Lower Chamfer Distance:** They show quick training times and a low chamfer distance (a metric for surface quality), indicating high-quality and fast reconstruction [00:06:08, 00:06:17].
*   **Random Initialization:** Unlike [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] which often require initialization from Structure-from-Motion (SfM) point clouds, [[Gaussian surfels]] can be initialized with random positions and rotations [00:54:15, 00:56:10]. This eliminates the need for crusty SfM pipelines [00:55:36].
*   **Efficiency (Potential):** Due to their ability to align perfectly with surfaces and promoting near-binary opacity, [[Gaussian surfels]] might potentially use fewer points to represent a scene compared to 3DGS, which often uses many semi-transparent bubbles to create the appearance of a surface [00:47:00, 01:29:12].
*   **Open Surface Reconstruction:** [[Gaussian surfels]] do not assume closed surfaces, making them suitable for reconstructing objects or scenes with open geometries [01:06:45].

## Challenges and Limitations
*   **Complex Pipeline:** The [[Gaussian surfel]] [[Optimization Techniques in Surfels | optimization pipeline]] is complicated, incorporating five distinct loss functions (photometric, normal prior, opacity, depth normal consistency, mask) [00:35:17].
*   **Hyperparameter Tuning:** Each loss function has tunable weights (e.g., lambda zero, lambda C, lambda M), which are hyperparameters that must be carefully selected and balanced [00:35:50].
*   **Custom Learning Rates:** Different properties of the surfels (position, radius, scale, opacity, view-dependent colors) use different, hand-tuned learning rates [00:57:27].
*   **Gradient Scaling:** The gradient from the normal loss is scaled by a factor of 10 to guide the Gaussian ellipse rotation [00:58:38]. These custom learning rates and gradient scaling factors represent "fragile little magic numbers" that can be difficult to manage [00:59:09].
*   **Specular Reflections:** The method struggles with accurate surface reconstruction in areas with strong specular reflections (shiny, reflective surfaces) [01:12:51]. This is a common challenge in 3D reconstruction and is exacerbated by the reliance on spherical harmonics for view-dependent effects [01:15:09]. The paper suggests replacing spherical harmonics with a dedicated neural network decoder to better handle such effects [01:15:11].
*   **Dynamic Scenes:** While [[Dynamic 3D Gaussian methodology | dynamic 3D Gaussian]] representations exist for moving objects, it is still "TBD" if [[Gaussian surfels]] will perform as well for [[Dynamic 3D Gaussian methodology | dynamic scenes]]. Their high opacity and strict surface alignment might make it harder for them to deform and move naturally compared to semi-transparent 3D Gaussian bubbles [01:03:13, 01:03:42].

## Optimization and Reconstruction
The [[Optimization Techniques in Surfels | optimization process]] for [[Gaussian surfels]] involves several key components:

1.  **Loss Functions:**
    *   **Photometric Loss (Lp):** Combines L1 term (80%) and DSSIM term (20%) to minimize the difference between the rendered image and the input image [00:36:19]. DSSIM, while useful for visual similarity, can be sensitive to rotations, shifts, and scaling [00:38:15].
    *   **Normal Prior Loss (Ln):** Enforces alignment with normal maps obtained from a pre-trained monocular normal estimator (e.g., OmniData or Marigold) [00:31:30, 00:40:07, 01:14:03].
    *   **Depth Normal Consistency Loss (Lc):** Ensures consistency between the rendered depth and the rendered normal [00:39:14]. This self-supervised loss leverages a model that produces approximate surface normals and depths from an RGB image [00:31:51, 00:41:01]. It helps correct both incorrect depth and incorrect normal directions, leading to improved reconstruction [00:42:52].
    *   **Opacity Loss (Lo):** Promotes non-transparent surfaces by encouraging each Gaussian's opacity to be near zero or near one [00:45:38]. This helps create a clear, thin surface, potentially leading to more efficient representations [00:47:00].
    *   **Mask Loss (Lm):** Used for foreground masking [00:35:31].
2.  **Volumetric Cutting:** Similar to densification and pruning in [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]], this technique removes erroneous or outlier [[Gaussian surfels]] [00:49:37]. It constructs a voxel grid and prunes voxels (and the 3D points within them) if they have low accumulated opacity, indicating they are far from the foreground or background [00:50:52]. This helps refine the surface by removing "sticking out" surfels on corners [00:52:07].
3.  **Surface Reconstruction:** After [[optimization]], the point-based representation of [[Gaussian surfels]] is converted into a surface mesh using "screened Poisson reconstruction" [00:07:09, 00:47:59]. This technique is designed to create watertight surfaces from oriented point sets [00:48:15].

## Future Outlook
The development of [[Gaussian surfels]] is seen as a step towards more advanced 3D content. Future work aims to incorporate [[Physicsbased Modeling in Gaussian Splats | physical properties]] like elasticity, weight, gravity, collisions, and friction into [[Gaussian splats in robotics | Gaussian Splats]] and surfels, moving beyond static representations [01:01:11, 01:01:49]. This would enable their use in applications like video games or complex simulations [01:01:11]. The ability to create [[Dynamic 3D Gaussian methodology | dynamic 3D scenes]] by adding time dependence to surfel properties is also a key area of research [01:03:04].