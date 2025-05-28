---
title: Differentiable rendering and optimization
videoId: hDuy1TgD8I4
---

From: [[hu-po]] <br/> 

[[ray_marching_and_differentiable_rendering | Differentiable rendering]] and optimization are fundamental techniques in 3D scene reconstruction and novel view synthesis, particularly relevant to modern 3D formats like 3D Gaussians. These methods allow for the iterative refinement of 3D scene parameters by using gradients calculated from rendering outputs.

## Core Concepts

### Differentiable Rendering
[[ray_marching_and_differentiable_rendering | Differentiable rendering]] enables the computation of gradients with respect to 3D scene parameters directly from rendered images. This means that if a rendered image differs from a target "ground truth" image, the error (or "reconstruction loss") can be backpropagated through the rendering process to adjust the 3D scene elements [00:30:00]. This is crucial for optimizing the parameters that define the 3D scene representation [01:03:04].

In the context of 3D Gaussians, the rendering function takes a dynamic scene `S` at a specific time step `T`, along with the camera's intrinsic (`K`) and extrinsic (`E`) matrices, to produce a rendered image `I_hat` [01:03:11]. This `I_hat` is then compared to the input "ground truth" image `I` [01:03:49]. The parameters of `S` are iteratively updated using automatic differentiation to minimize this error [01:03:53]. This allows gradients to flow to 3D Gaussians, even if they are initially in the wrong 3D location, pushing them towards the correct position [01:17:04].

### Gradient-Based Optimization
[[Continuous vs Discrete Optimization | Gradient-based optimization]] is a machine learning technique where gradients are used to iteratively improve the values of parameters [00:30:17]. For 3D Gaussians, the parameters being optimized include:
*   **Position** (3D center `mu`) [00:30:25]
*   **Rotation** (quaternion `q`) [00:30:25]
*   **Size** (3D standard deviations) [00:30:25]
*   **Color** (RGB) [00:30:25]
*   **Opacity** [00:30:25]

This optimization is typically performed via an iterative process [01:03:53].

### Reconstruction Loss
The primary objective of the optimization process is to minimize a "reconstruction loss" [01:04:01]. This loss measures how well the rendered image `I_hat` matches the ground truth image `I` [01:04:01]. By minimizing this loss, the 3D Gaussian parameters are adjusted to accurately represent the scene captured by the input images [01:04:01].

## Optimization Process for Dynamic Scenes

For dynamic scenes, the optimization often involves two main parts:
1.  **Initial Static Reconstruction**: The first time step of a scene is treated as a static scene, and all parameters (position, rotation, size, color, opacity) of the 3D Gaussians are optimized to represent this initial state [01:02:51], [01:52:01]. This step typically involves more compute and time [01:01:43].
2.  **Dynamic Motion Tracking**: For subsequent time steps, the size, color, and opacity of the Gaussians are fixed, and only their positions and rotations are optimized [01:52:12]. This ensures that each Gaussian represents the same physical aspect of space as it moves over time [01:18:15].

The optimization for dynamic scenes is often performed "temporally online," meaning one time step of the scene is reconstructed at a time, with each subsequent step initialized using the previous scene's representation [01:11:10].

### Optimization Techniques and Considerations
*   **Adam Optimizer**: The Adam optimizer is used for gradient-based updates. Its momentum terms are reset at the start of each time step to prevent accumulation of momentum that might not be suitable for potentially erratic particle motion [01:54:54].
*   **Differentiable 3D Gaussian Renderer**: The rendering is based on [[fast_differentiable_tile_rasterization_for_rendering | fast differentiable tile rasterization]], which efficiently splats 3D Gaussians onto the image plane [01:19:43]. This involves projecting the 3D Gaussian's center and covariance matrix into 2D pixel coordinates, then combining the influence of all Gaussians on each pixel by sorting them by depth [01:21:22], [01:27:42].
*   **Physical Priors and Regularization**: To ensure physically plausible motion and improve tracking, several regularization losses are introduced [01:34:55]:
    *   **Short-term Local Rigidity (L_rigid)**: Encourages nearby Gaussians to move in a way that follows the rigid body transform of their local coordinate system between time steps [01:36:06], [01:39:05]. This is considered the most important prior [01:35:21].
    *   **Local Rotational Similarity (L_rot)**: Explicitly forces neighboring Gaussians to have similar rotations over time [01:35:11], [01:38:35].
    *   **Long-term Local Isometry (L_iso)**: A weaker constraint that enforces distances between Gaussians to remain similar over long time horizons, preventing "drift" [01:35:15], [01:51:11].
*   **Hyperparameters**: The application of these priors involves hyperparameters, such as the number of K-nearest neighbors (e.g., K=20) for defining "nearby" Gaussians [01:43:47].
*   **Foreground/Background Segmentation**: To improve tracking, particularly for objects with low contrast against the background, a foreground/background mask is used. This allows regularization losses to be applied only to foreground points, improving efficiency and preventing unwanted interactions with the static background [01:57:17].
*   **Camera Property Modeling**: To account for variations in color representation due to different camera properties, a scale and offset parameter for each color channel is optimized per camera during the first time step and then fixed [01:58:45].

## Advantages and Limitations

**Advantages:**
*   **Fast Rendering**: Thanks to efficient [[fast_differentiable_tile_rasterization_for_rendering | GPU-optimized splatting]], rendering is extremely fast, achieving up to 850 frames per second [02:27:28], surpassing human perception limits for frame rates [01:01:22].
*   **Free Tracking**: The method naturally yields dense 6-degree-of-freedom tracking of all 3D points without requiring explicit correspondence or optical flow as input [00:41:00], [01:13:31]. This "free" tracking capability is highly appealing for downstream applications [01:16:16].
*   **Editability and Composability**: Because 3D Gaussians explicitly represent objects, they are amenable to various creative scene editing techniques, such as adding, removing, or duplicating dynamic objects, and propagating edits over time [01:54:50], [02:16:36].

**Limitations:**
*   **Multi-Camera Setup Requirement**: The method heavily relies on a multi-camera setup with perfectly calibrated cameras that are uniformly distributed around the area of interest (e.g., within a geodesic dome) [02:27:51]. It does not work well with "off-the-shelf" monocular video [02:21:28].
*   **No New Object Reconstruction**: It can only track parts of the scene visible in the initial frame and will fail to reconstruct new objects entering the scene [01:05:55], [02:21:11].
*   **Assumptions on Scene Properties**: The physical priors (e.g., local rigidity) assume non-deformable objects, making the method less suitable for modeling soft bodies, smoke, or water [01:16:16], [02:28:44].
*   **Lighting**: The current approach does not inherently handle re-lighting of objects in compositional scenes, as the Gaussian colors are fixed and view-dependent color (e.g., using spherical harmonics) is turned off for simplicity [01:41:40], [01:10:50].
*   **Initialization Dependence**: The quality of the output depends on a good initial representation, often obtained from sparse point clouds or specialized depth cameras [01:52:48].