---
title: Dynamic 3D Gaussian methodology
videoId: hDuy1TgD8I4
---

From: [[hu-po]] <br/> 

**Dynamic 3D Gaussians** represent a novel approach to modeling dynamic three-dimensional scenes, extending the concepts of static [[3d_gaussian_splats_for_radiance_field_rendering | 3D Gaussian Splatting]] to include the dimension of time <a class="yt-timestamp" data-t="02:02:04">[02:02:04]</a>. This methodology allows for the reconstruction and tracking of moving objects within a scene, offering an alternative to traditional methods and [[3d_representation_techniques_nerfs_vs_gausssian_splats | Neural Radiance Fields (Nerfs)]] <a class="yt-timestamp" data-t="01:51:53">[01:51:53]</a>.

## Core Concepts

The system models a dynamic scene as a collection of 3D Gaussians <a class="yt-timestamp" data-t="01:00:01">[01:00:01]</a>. Each Gaussian is characterized by several parameters:
*   A 3D center (position) for each time step <a class="yt-timestamp" data-t="01:07:40">[01:07:40]</a>.
*   Rotation (orientation), represented by a quaternion <a class="yt-timestamp" data-t="01:07:46">[01:07:46]</a>.
*   3D size (standard deviations, defining an ellipsoid shape) <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>.
*   Color (RGB) <a class="yt-timestamp" data-t="01:08:30">[01:08:30]</a>.
*   Opacity (see-throughness), often represented as a logit <a class="yt-timestamp" data-t="01:08:36">[01:08:36]</a>.
*   A background logit, potentially distinguishing foreground from background elements <a class="yt-timestamp" data-t="01:09:16">[01:09:16]</a>.

A key insight of this method is that while a Gaussian's position and orientation can vary over time, its color, opacity, and size remain constant <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>. This restriction simplifies the model, treating Gaussians as a particle-based physical representation of the world <a class="yt-timestamp" data-t="01:14:55">[01:14:55]</a>.

## Methodology and Optimization

The modeling process involves a two-stage optimization:
1.  **Static Scene Reconstruction:** The first time step is initialized, and all Gaussian properties (position, rotation, size, color, opacity) are optimized to reconstruct the initial static scene from input images <a class="yt-timestamp" data-t="01:01:25">[01:01:25]</a>. This process leverages a differentiable renderer that can convert 3D Gaussians into 2D camera views <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.
2.  **Dynamic Motion Optimization:** For subsequent time steps, the size, color, and opacity of the Gaussians are *fixed* <a class="yt-timestamp" data-t="01:52:12">[01:52:12]</a>. Only their position and rotation are optimized <a class="yt-timestamp" data-t="01:52:17">[01:52:17]</a>. This ensures temporal consistency and enables [[3d_modeling_and_tracking_using_gaussian_splatting | dense 6-degree-of-freedom (6-DoF) tracking]] <a class="yt-timestamp" data-t="01:06:42">[01:06:42]</a>.

### Physically Based Priors
To ensure physically plausible and spatially consistent motion, three regularization losses are introduced during the dynamic optimization stage <a class="yt-timestamp" data-t="01:35:05">[01:35:05]</a>:
*   **Local Rigidity Prior (L_rigid):** This is the most important prior <a class="yt-timestamp" data-t="01:35:21">[01:35:21]</a>. It enforces that nearby Gaussians move in a way that follows the rigid body transformation of their local coordinate system <a class="yt-timestamp" data-t="01:36:44">[01:36:44]</a>. This prevents Gaussians from drifting apart in areas of uniform color <a class="yt-timestamp" data-t="01:34:10">[01:34:10]</a>.
*   **Local Rotational Similarity Prior (L_rot):** Encourages neighboring Gaussians to have similar rotations over time <a class="yt-timestamp" data-t="01:35:11">[01:35:11]</a>.
*   **Long-Term Local Isometry Prior (L_iso):** A weaker constraint that ensures the distances between nearby Gaussians remain consistent over longer time periods <a class="yt-timestamp" data-t="01:35:15">[01:35:15]</a>.

These priors are applied locally, typically to the 20 nearest neighbors of each Gaussian <a class="yt-timestamp" data-t="01:43:47">[01:43:47]</a>. The optimization uses a differentiable renderer, allowing gradients from reconstruction loss (comparing rendered images to ground truth) to update Gaussian parameters <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>. The Adam optimizer is used, with its momentum terms reset at each time step <a class="yt-timestamp" data-t="01:55:04">[01:55:04]</a>.

## Data Acquisition and Experimental Setup

The research heavily relies on multi-camera capture data from environments like the "Panoptic Studio," a large geodesic dome housing 480 synchronized cameras with precisely known intrinsic and extrinsic matrices <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This setup provides high-quality, synchronized multi-view video, which is crucial for the method's performance <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>. The "Panoptic Sports" dataset, comprising various activities like juggling and softball, was used for experiments <a class="yt-timestamp" data-t="02:01:29">[02:01:29]</a>.

> [!NOTE] Camera Calibration "Cheat Code"
> The exact, pre-calibrated positions and properties of each camera in a studio dome provide a significant advantage, which is difficult to replicate with consumer-grade equipment like a smartphone <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.

## Advantages and Applications

Dynamic 3D Gaussians offer several compelling advantages:
*   **Real-time Rendering:** Achieves high rendering speeds, up to 850 frames per second on an RTX 4090 GPU <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>. This is significantly faster than [[3d_representation_techniques_nerfs_vs_gausssian_splats | Nerfs]], which are typically slower due to neural network inference <a class="yt-timestamp" data-t="01:02:04">[01:02:04]</a>.
*   **Implicit Tracking:** Provides [[3d_modeling_and_tracking_using_gaussian_splatting | dense 6-DoF tracking]] of scene elements as a natural outcome of the persistent dynamic view synthesis, without requiring explicit inputs like optical flow, skeletons, or correspondence information <a class="yt-timestamp" data-t="01:13:54">[01:13:54]</a>.
*   **Scene Editing and [[3d_content_generation_using_gaussian_splatting | Content Generation]]**: The explicit nature of Gaussian elements allows for easy manipulation:
    *   Removing or adding dynamic objects <a class="yt-timestamp" data-t="01:57:58">[01:57:58]</a>.
    *   Duplicating elements <a class="yt-timestamp" data-t="02:16:41">[02:16:41]</a>.
    *   Composing elements from different scenes <a class="yt-timestamp" data-t="01:54:13">[01:54:13]</a>.
    *   Attaching camera views to moving scene elements <a class="yt-timestamp" data-t="02:17:13">[02:17:13]</a>.
    *   Propagating edits over time <a class="yt-timestamp" data-t="02:19:21">[02:19:21]</a>.
*   **Potential for [[physicsbased_modeling_in_gaussian_splats | Physics-based Modeling]]**: Unlike implicit representations, the explicit nature of 3D Gaussians makes them amenable to modeling [[physicsbased_modeling_in_gaussian_splats | physics-based interactions]] and simulations, crucial for applications like video games <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

These capabilities open doors for various [[applications_of_dynamic_3d_gaussians_in_film_and_vr | applications of dynamic 3D Gaussians in film and VR]], robotics, augmented reality (AR), self-driving vehicles, and the metaverse <a class="yt-timestamp" data-t="02:21:57">[02:21:57]</a>.

## Limitations and Future Directions

Despite its strengths, the methodology has notable [[challenges_and_solutions_in_representing_3d_objects_with_gaussian_splatting | limitations]]:
*   **Initial Scene Dependency:** It can only track parts of the scene visible in the initial frame and would fail to reconstruct new objects entering the scene later <a class="yt-timestamp" data-t="02:11:11">[02:11:11]</a>.
*   **Multi-Camera Requirement:** Requires a precisely calibrated multi-camera setup; it does not work well with off-the-shelf monocular video <a class="yt-timestamp" data-t="02:11:27">[02:11:27]</a>.
*   **Fixed Gaussian Properties:** The assumption of constant color, opacity, and size means it's less suitable for deformable objects like smoke or water, where these properties might change <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>.
*   **Lighting Model:** The current implementation does not account for view-dependent color using spherical harmonics, meaning re-lighting composite scenes is not currently supported <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.
*   **Hyperparameter Tuning:** The regularization losses rely on specific hyperparameters, which can be "sketchy" and scene-dependent <a class="yt-timestamp" data-t="01:47:38">[01:47:38]</a>.

Future work could explore addressing these limitations, such as incorporating more sophisticated deformation models for Gaussians, handling dynamic scene changes, and integrating advanced lighting techniques.