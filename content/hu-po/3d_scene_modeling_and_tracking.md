---
title: 3D scene modeling and tracking
videoId: hDuy1TgD8I4
---

From: [[hu-po]] <br/> 

The paper "Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis" presents a novel approach to [[3d_representations_and_their_applications | 3D scene modeling and tracking]] that extends the concept of 3D Gaussians to dynamic environments. This work, originating from Carnegie Mellon University, Akan Germany, and Inria University Cortez, builds upon previous research on 3D Gaussian Splatting for static scenes <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

## What are Dynamic 3D Gaussians?

[[3d_representations_and_their_applications | 3D Gaussians]] are a relatively new [[3d_representations_and_their_applications | 3D format]] that represents complex scenes as a collection of numerous colored 3D Gaussians <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Each Gaussian is akin to a point cloud with a defined spread or variance <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

Unlike traditional static 3D Gaussian representations or NeRFs (Neural Radiance Fields), Dynamic 3D Gaussians incorporate the dimension of time, enabling the modeling of dynamic scenes <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This means the scene itself changes over time <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

Each individual 3D Gaussian is parameterized by several attributes <a class="yt-timestamp" data-t="01:07:35">[01:07:35]</a>:
*   A 3D center (position) for each time step <a class="yt-timestamp" data-t="01:07:40">[01:07:40]</a>.
*   A rotation (orientation), often represented by a quaternion <a class="yt-timestamp" data-t="01:07:43">[01:07:43]</a>.
*   A 3D size, defined by standard deviations that can be interpreted as an ellipsoid's radii <a class="yt-timestamp" data-t="01:08:12">[01:08:12]</a>.
*   A single color (RGB) <a class="yt-timestamp" data-t="01:08:30">[01:08:30]</a>.
*   An opacity (how see-through it is), typically a logit value squashed between 0 and 1 using a sigmoid function <a class="yt-timestamp" data-t="01:08:36">[01:08:36]</a>.
*   A background logit, which may indicate if the Gaussian belongs to the foreground or background <a class="yt-timestamp" data-t="01:09:16">[01:09:16]</a>.

A key insight of this paper is that the number, color, opacity, and size of the Gaussians are kept constant over time, while only their position and orientation are allowed to vary <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a>. This treats the Gaussians as a particle-based physical model, where "oriented particles undergo rigid body transformations over time" <a class="yt-timestamp" data-t="01:14:55">[01:14:55]</a>. This approach works well for non-deformable objects like humans or bats but may struggle with soft, deformable objects like smoke or water <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>.

## Methodology: Persistent Dynamic View Synthesis

The method operates as an analysis-by-synthesis approach, constructing a persistent dynamic [[3d_representations_and_their_applications | 3D scene representation]] that is consistent with all input observations <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

### Input Data
The system requires synchronized multi-view video input <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>. The experiments utilize data from a "camera geodesic dome," known as the Panoptic Studio, which houses 480 synchronized cameras <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Crucially, the exact position (extrinsic matrices) and internal properties (intrinsic matrices) of every camera are known and perfectly calibrated beforehand <a class="yt-timestamp" data-t="00:58:06">[00:58:06]</a>. This provides a strong starting point and is considered a "cheat code" for the quality of results, as such perfect calibration is difficult to replicate in real-world scenarios outside of controlled studio environments <a class="yt-timestamp" data-t="00:42:26">[00:42:26]</a>, <a class="yt-timestamp" data-t="00:59:50">[00:59:50]</a>.

### Optimization Process
The reconstruction is performed via test-time optimization, meaning no additional training data beyond the specific scene being modeled is used <a class="yt-timestamp" data-t="01:00:12">[01:00:12]</a>. The process runs "temporally online," reconstructing one time step of the scene at a time, with each subsequent step initialized using the representation from the previous time step <a class="yt-timestamp" data-t="01:11:10">[01:11:10]</a>.

The optimization is split into two main parts:
1.  **First Time Step Initialization**: All parameters of the Gaussians (position, rotation, size, color, opacity) are optimized. This initial step is critical as any error here can propagate through the entire sequence <a class="yt-timestamp" data-t="01:01:25">[01:01:25]</a>, <a class="yt-timestamp" data-t="01:52:01">[01:52:01]</a>. It begins with a sparse point cloud, often from depth cameras or [[duster_and_multiview_stereo_reconstruction | COLMAP]] <a class="yt-timestamp" data-t="01:52:48">[01:52:48]</a>. Densification techniques are used to increase the number of Gaussians <a class="yt-timestamp" data-t="01:53:25">[01:53:25]</a>.
2.  **Subsequent Time Steps**: After the first frame, the size, color, and opacity of the Gaussians are fixed. Only their position and rotation are optimized <a class="yt-timestamp" data-t="01:52:17">[01:52:17]</a>. This part of the optimization uses a forward estimate based on previous velocities to initialize the next time step's Gaussian positions and rotations <a class="yt-timestamp" data-t="01:54:13">[01:54:13]</a>.

Both stages employ gradient-based optimization using a differentiable renderer <a class="yt-timestamp" data-t="01:02:56">[01:02:56]</a>. This [[techniques_for_optimizing_and_refining_3d_models | differentiable rendering]] allows for the backpropagation of reconstruction loss (the difference between rendered and ground truth images) through the rendering function directly to the Gaussian parameters <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>. The rendering process projects 3D Gaussians into 2D image planes using [[techniques_for_optimizing_and_refining_3d_models | splatting]] <a class="yt-timestamp" data-t="02:26:19">[02:26:19]</a>. The final color of a pixel is a weighted sum of the colors of all influencing Gaussians, sorted by depth <a class="yt-timestamp" data-t="01:27:57">[01:27:57]</a>. This process is highly optimized using Cuda kernels for speed on GPUs <a class="yt-timestamp" data-t="01:30:41">[01:30:41]</a>.

### Physically-Based Priors (Regularization Losses)
To ensure robust and plausible [[motion_tracking_methods | tracking]] and prevent Gaussians from freely drifting in areas of uniform color, three regularization losses are introduced <a class="yt-timestamp" data-t="01:35:05">[01:35:05]</a>:
1.  **Short-term Local Rigidity Loss (L_rigid)**: This is the most important loss <a class="yt-timestamp" data-t="01:35:21">[01:35:21]</a>. It enforces that nearby Gaussians move in a way that follows the rigid body transformation of their local coordinate system between time steps <a class="yt-timestamp" data-t="01:36:41">[01:36:41]</a>. This means the relative distance and orientation between nearby Gaussians should remain consistent <a class="yt-timestamp" data-t="01:36:06">[01:36:06]</a>.
2.  **Short-term Local Rotational Similarity Loss (L_rot)**: This loss explicitly forces neighboring Gaussians to maintain similar rotations over time <a class="yt-timestamp" data-t="01:37:33">[01:37:33]</a>.
3.  **Long-term Local Isometry Loss (L_iso)**: Applied over longer time horizons, this weaker constraint ensures that the distances between nearby Gaussians remain consistent with their initial distances at time step zero <a class="yt-timestamp" data-t="01:50:09">[01:50:09]</a>. This helps to prevent long-term drift <a class="yt-timestamp" data-t="01:51:09">[01:51:09]</a>.

These losses are applied to Gaussians identified as "foreground points" (using a pseudoground truth foreground/background mask) to improve efficiency and avoid enforcing rigidity on static background elements <a class="yt-timestamp" data-t="01:57:58">[01:57:58]</a>. The regularization parameters (e.g., number of nearest neighbors, weights) are chosen empirically and can be considered "sketchy hyper parameters" specific to the scenes <a class="yt-timestamp" data-t="01:42:50">[01:42:50]</a>.

## Applications and Performance

The method demonstrates impressive performance:
*   **Speed**: Achieves 850 frames per second (fps) for dynamic novel view rendering <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>, significantly faster than typical VR headset requirements (60-120 fps) <a class="yt-timestamp" data-t="00:38:44">[00:38:44]</a>. This speed is attributed to the efficient, non-neural network based rendering process <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.
*   **Accuracy**: Achieves a 28.7 Peak Signal-to-Noise Ratio (PSNR) for dynamic novel view rendering <a class="yt-timestamp" data-t="00:28:25">[00:28:25]</a>. It also provides accurate metric [[motion_tracking_methods | 3D dense non-rigid long-term scene tracking]] with an average L2 error of 2.21 centimeters <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>.
*   **Training Time**: Training a 150-time step (approx. 4 seconds) scene takes only two hours on a single RTX 4090 GPU <a class="yt-timestamp" data-t="00:39:37">[00:39:37]</a>.

A significant advantage is that [[motion_tracking_methods | dense 6-DOF tracking]] (position and three rotation degrees of freedom) "emerges naturally" from the persistent dynamic view synthesis, without requiring explicit inputs like optical flow, pose skeletons, or other correspondence information <a class="yt-timestamp" data-t="01:13:59">[01:13:59]</a>. This makes the method appealing for various [[potential_applications_and_future_directions_in_3d_scene_representations | downstream applications]].

### Downstream Applications
The dynamic 3D Gaussian representation enables several [[potential_applications_and_future_directions_in_3d_scene_representations | applications]] <a class="yt-timestamp" data-t="01:54:52">[01:54:52]</a>:
*   **First-person View Synthesis**: Cameras can be attached to moving scene elements, allowing for novel views from an object's perspective <a class="yt-timestamp" data-t="01:55:07">[01:55:07]</a>.
*   **Dynamic Compositional Scene Synthesis**: Objects can be easily added to, removed from, or duplicated within scenes. This is a significant advantage over NeRFs, which lack explicit object notions <a class="yt-timestamp" data-t="02:16:43">[02:16:43]</a>. However, the current method does not handle re-lighting, which remains a challenge for compositional scenes <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.
*   **4D Video Editing**: Allows for editing of 3D scenes over time <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
*   **Robotics, Augmented Reality (AR), Self-Driving**: The explicit, trackable nature of 3D Gaussians could facilitate [[dynamic_scene_handling_in_robotics | physics-based interactions]] and enable better understanding of metric space reconstruction over time <a class="yt-timestamp" data-t="02:08:50">[02:08:50]</a>.

## Limitations

Despite its strengths, the method has notable limitations <a class="yt-timestamp" data-t="02:11:07">[02:11:07]</a>:
*   **Initial Visibility**: It can only track parts of the scene visible in the initial frame, failing to reconstruct new objects entering the scene <a class="yt-timestamp" data-t="02:11:11">[02:11:11]</a>.
*   **Multi-Camera Requirement**: The approach relies heavily on a multi-camera setup with perfectly calibrated, synchronized cameras uniformly distributed around the area of interest <a class="yt-timestamp" data-t="02:02:30">[02:02:30]</a>. It does not work well with off-the-shelf monocular video <a class="yt-timestamp" data-t="02:11:27">[02:11:27]</a>.
*   **Assumptions**: The physical priors assume local rigidity, which limits application to deformable objects like fluids or smoke <a class="yt-timestamp" data-t="02:28:40">[02:28:40]</a>.
*   **Hyperparameter Tuning**: The reliance on empirically set hyperparameters for regularization losses might make it sensitive to different scene types <a class="yt-timestamp" data-t="01:51:30">[01:51:30]</a>.

## Future Directions

The paper highlights the potential for future innovation in [[3d_representations_and_their_applications | 3D modeling and tracking]]. Future work could explore incorporating [[generative_3d_models_using_video_diffusion | generative AI]] for content creation, integrating complex lighting models using spherical harmonics, and addressing the challenges of monocular video input and highly deformable scenes.