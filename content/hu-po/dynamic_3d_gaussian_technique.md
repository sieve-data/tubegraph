---
title: Dynamic 3D Gaussian technique
videoId: hDuy1TgD8I4
---

From: [[hu-po]] <br/> 

The Dynamic 3D Gaussian technique is an extension of [[3d_gaussian_splatting_for_realtime_radiance_field_rendering | 3D Gaussian Splatting]] that enables the modeling and tracking of dynamic (changing over time) 3D scenes [00:02:02](<a class="yt-timestamp" data-t="00:02:02">00:02:02</a>). Unlike static representations like most early NeRFs or initial [[3d_gaussian_splatting_for_realtime_radiance_field_rendering | 3D Gaussian Splatting]] papers, this approach incorporates the dimension of time [00:02:02](<a class="yt-timestamp" data-t="00:02:02">00:02:02</a>). It was developed by a research group that includes contributors from Carnegie Mellon University, Akan Germany, and Inria University Cortez [00:02:44](<a class="yt-timestamp" data-t="00:02:44">00:02:44</a>).

## Core Concept: Dynamic 3D Gaussians

The method represents complex dynamic scenes as a collection of 3D Gaussians [01:00:01](<a class="yt-timestamp" data-t="01:00:01">01:00:01</a>). Each 3D Gaussian can be visualized as a small, elongated ellipsoid [01:08:23](<a class="yt-timestamp" data-t="01:08:23">01:08:23</a>). Each Gaussian has the following persistent properties across time steps [01:17:47](<a class="yt-timestamp" data-t="01:17:47">01:17:47</a>):
*   **Color (RGB)** [01:08:30](<a class="yt-timestamp" data-t="01:08:30">01:08:30</a>)
*   **Opacity (log-it)** [01:08:36](<a class="yt-timestamp" data-t="01:08:36">01:08:36</a>)
*   **Size/Standard Deviations** (represented as the covariance matrix, which combines scaling and rotation) [01:13:51](<a class="yt-timestamp" data-t="01:13:51">01:13:51</a>)
*   **Background Log-it** (potentially indicating foreground/background) [01:09:16](<a class="yt-timestamp" data-t="01:09:16">01:09:16</a>)

Crucially, the **position** (3D Center) and **orientation** (rotation via quaternion) of these Gaussians are allowed to vary over time [01:00:01](<a class="yt-timestamp" data-t="01:00:01">01:00:01</a>). This allows for full 6-degree-of-freedom (6-DoF) tracking [01:18:25](<a class="yt-timestamp" data-t="01:18:25">01:18:25</a>).

### Data Capture

The work primarily utilizes data from a specialized "Panoptic Studio" or "geodesic camera dome" [00:03:12](<a class="yt-timestamp" data-t="00:03:12">00:03:12</a>). This studio has:
*   A radius of 5.49 meters and a total height of 4.15 meters [00:03:27](<a class="yt-timestamp" data-t="00:03:27">00:03:27</a>).
*   Up to 480 synchronized cameras, though this paper typically uses 27 training cameras and 4 testing cameras [00:04:05](<a class="yt-timestamp" data-t="00:04:05">00:04:05</a>), [00:54:57](<a class="yt-timestamp" data-t="00:54:57">00:54:57</a>).
*   All cameras are perfectly calibrated, meaning their exact intrinsic and extrinsic (position and orientation) matrices are known [00:04:21](<a class="yt-timestamp" data-t="00:04:21">00:04:21</a>), [00:58:03](<a class="yt-timestamp" data-t="00:58:03">00:58:03</a>). This is a "cheat code" compared to typical real-world video capture [00:04:42](<a class="yt-timestamp" data-t="00:04:42">00:04:42</a>).
*   The setup is designed to provide uniform, soft white lighting [00:17:26](<a class="yt-timestamp" data-t="00:17:26">00:17:26</a>).
*   The data used includes "Panoptic Sports" sequences like jugglebox, softball, tennis, football, and basketball, typically 150 frames at 30 FPS (around 4 seconds) [02:01:29](<a class="yt-timestamp" data-t="02:01:29">02:01:29</a>).

## Methodology

The technique uses a two-part optimization process [01:52:17](<a class="yt-timestamp" data-t="01:52:17">01:52:17</a>):

### 1. Initial Static Reconstruction
*   The first time step is optimized to reconstruct the static scene [01:52:01](<a class="yt-timestamp" data-t="01:52:01">01:52:01</a>).
*   All Gaussian parameters (position, rotation, size, color, opacity) are optimized [01:52:02](<a class="yt-timestamp" data-t="01:52:02">01:52:02</a>).
*   This step can be initialized from a sparse point cloud (e.g., from Colmap or depth cameras) [01:52:48](<a class="yt-timestamp" data-t="01:52:48">01:52:48</a>).
*   Densification and pruning steps, similar to [[3d_gaussian_splatting_for_realtime_radiance_field_rendering | the original 3D Gaussian paper]], are used to increase Gaussian density [01:53:25](<a class="yt-timestamp" data-t="01:53:25">01:53:25</a>).
*   This phase takes about 10,000 iterations for the first frame [01:53:46](<a class="yt-timestamp" data-t="01:53:46">01:53:46</a>).

### 2. Dynamic Motion Tracking
*   For subsequent time steps, the size, color, and opacity of the Gaussians are fixed [01:52:12](<a class="yt-timestamp" data-t="01:52:12">01:52:12</a>).
*   Only the position and rotation of each Gaussian are optimized [01:52:17](<a class="yt-timestamp" data-t="01:52:17">01:52:17</a>).
*   This optimization is performed "temporarily online," meaning one time step is reconstructed at a time, initialized using the previous time step's representation [01:00:57](<a class="yt-timestamp" data-t="01:00:57">01:00:57</a>), [01:11:00](<a class="yt-timestamp" data-t="01:11:00">01:11:00</a>).
*   A forward estimate based on previous velocity is used to initialize Gaussian positions and rotations for the current time step [01:54:13](<a class="yt-timestamp" data-t="01:54:13">01:54:13</a>).
*   Each time step uses 2,000 iterations, totaling two hours for 150 time steps on an RTX 4090 GPU [01:53:53](<a class="yt-timestamp" data-t="01:53:53">01:53:53</a>).

### Differentiable Rendering
*   To optimize Gaussian parameters, a differentiable [[3d_gaussian_splatting_for_realtime_radiance_field_rendering | 3D Gaussian Splatting]] renderer is used [01:19:31](<a class="yt-timestamp" data-t="01:19:31">01:19:31</a>).
*   This process involves "splatting" 3D Gaussians onto a 2D image plane, approximating the projection of their influence function [01:20:33](<a class="yt-timestamp" data-t="01:20:33">01:20:33</a>).
*   The center of a 3D Gaussian is projected into 2D using the camera's extrinsic (world-to-camera) and intrinsic projection matrices [01:21:22](<a class="yt-timestamp" data-t="01:21:22">01:21:22</a>).
*   The 3D covariance matrix is also projected into 2D using a Jacobian of the projection formula [01:25:33](<a class="yt-timestamp" data-t="01:25:33">01:25:33</a>).
*   The influence of all Gaussians on a pixel is combined by sorting them by depth and performing front-to-back volume rendering [01:27:40](<a class="yt-timestamp" data-t="01:27:40">01:27:40</a>).

### Physically-Based Priors (Regularization Losses)
To ensure long-term persistent and physically plausible tracking, three regularization losses are introduced [01:35:05](<a class="yt-timestamp" data-t="01:35:05">01:35:05</a>):

1.  **Short-term Local Rigidity Loss (L_rigid)**:
    *   This is the most important loss [01:35:21](<a class="yt-timestamp" data-t="01:35:21">01:35:21</a>).
    *   It ensures that nearby Gaussians (within a K-nearest neighbors set of K=20) move together, following the rigid body transform of their local coordinate system between time steps [01:36:06](<a class="yt-timestamp" data-t="01:36:06">01:36:06</a>), [01:43:45](<a class="yt-timestamp" data-t="01:43:45">01:43:45</a>).
    *   It's applied in both directions between pairs of Gaussians [01:45:21](<a class="yt-timestamp" data-t="01:45:21">01:45:21</a>).
    *   This allows for global non-rigid reconstruction while maintaining local rigidity [01:45:01](<a class="yt-timestamp" data-t="01:45:01">01:45:01</a>).

2.  **Local Rotational Similarity Prior (L_rot)**:
    *   Explicitly forces neighboring Gaussians to have similar rotations over time [01:45:33](<a class="yt-timestamp" data-t="01:45:33">01:45:33</a>).
    *   Uses normalized quaternions for smooth optimization [01:47:21](<a class="yt-timestamp" data-t="01:47:21">01:47:21</a>).

3.  **Long-term Local Isometry Loss (L_iso)**:
    *   A weaker constraint that enforces the distances between nearby Gaussians to remain the same over the long term (e.g., from time step 0 to time step T) [01:50:09](<a class="yt-timestamp" data-t="01:50:09">01:50:09</a>), [01:51:46](<a class="yt-timestamp" data-t="01:51:46">01:51:46</a>).
    *   This helps prevent "drift" of scene elements over longer time horizons [01:48:28](<a class="yt-timestamp" data-t="01:48:28">01:48:28</a>).

These losses are primarily applied to foreground elements to improve efficiency and prevent static backgrounds from influencing dynamic tracking [01:57:40](<a class="yt-timestamp" data-t="01:57:40">01:57:40</a>).

## Applications and Benefits

The Dynamic 3D Gaussian technique offers several advantages:

*   **Novel View Synthesis**: Allows creating images from previously unseen camera viewpoints [00:06:08](<a class="yt-timestamp" data-t="00:06:08">00:06:08</a>).
*   **Dense 6-DoF Tracking**: Achieves highly accurate tracking of all 3D points, including position and rotation, without needing explicit inputs like optical flow, skeletons, or correspondence information [00:41:00](<a class="yt-timestamp" data-t="00:41:00">00:41:00</a>), [01:13:51](<a class="yt-timestamp" data-t="01:13:51">01:13:51</a>). This "tracking for free" is a key benefit [01:10:00](<a class="yt-timestamp" data-t="01:10:00">01:10:00</a>).
*   **Real-time Rendering**: Can render dynamic novel views at extremely high frame rates, up to 850 frames per second on an RTX 4090 [00:38:27](<a class="yt-timestamp" data-t="00:38:27">00:38:27</a>). This is much faster than [[comparison_of_3d_gaussian_splatting_to_neural_radiance_fields | NeRFs]] because it avoids per-pixel neural network inference [01:02:04](<a class="yt-timestamp" data-t="01:02:04">01:02:04</a>).
*   **Scene Editing and Composability**:
    *   Dynamic objects can be easily removed, duplicated, or added to scenes [02:16:36](<a class="yt-timestamp" data-t="02:16:36">02:16:36</a>). This is a significant advantage over implicit representations like NeRFs [02:16:45](<a class="yt-timestamp" data-t="02:16:45">02:16:45</a>).
    *   Edits can be propagated over time [02:19:21](<a class="yt-timestamp" data-t="02:19:21">02:19:21</a>).
    *   Camera views can be attached to moving scene elements (e.g., first-person view synthesis) [01:59:57](<a class="yt-timestamp" data-t="01:59:57">01:59:57</a>).
*   **Potential for Physics-Based Interactions**: Unlike NeRFs, the explicit nature of 3D Gaussians could facilitate physics simulations and collision detection [02:08:50](<a class="yt-timestamp" data-t="02:08:50">02:08:50</a>).

## [[Applications and limitations of 3D Gaussians | Limitations]]

Despite its capabilities, the Dynamic 3D Gaussian technique has several [[Applications and limitations of 3D Gaussians | limitations]]:

*   **Reliance on Multi-Camera Setup**: Requires a specialized, perfectly calibrated multi-camera capture system (like the Panoptic Studio) [02:12:00](<a class="yt-timestamp" data-t="02:12:00">02:12:00</a>), [02:11:27](<a class="yt-timestamp" data-t="02:11:27">02:11:27</a>). It is not designed for off-the-shelf monocular video [02:12:28](<a class="yt-timestamp" data-t="02:12:28">02:12:28</a>).
*   **Initial Frame Visibility**: Can only track parts of the scene that are visible in the initial frame [02:12:10](<a class="yt-timestamp" data-t="02:12:10">02:12:10</a>).
*   **New Object Ingress**: The method will fail to reconstruct new objects entering the scene after the initial frame [01:05:55](<a class="yt-timestamp" data-t="01:05:55">01:05:55</a>).
*   **Assumptions about Rigidity**: The core assumption of persistent size, opacity, and color, along with local rigidity priors, makes it less suitable for highly deformable objects like smoke or water [01:31:16](<a class="yt-timestamp" data-t="01:31:16">01:31:16</a>), [01:32:01](<a class="yt-timestamp" data-t="01:32:01">01:32:01</a>), [02:28:51](<a class="yt-timestamp" data-t="02:28:51">02:28:51</a>).
*   **No Explicit Lighting Model**: Does not account for realistic lighting effects, making compositional scenes appear unnatural if the lighting environments don't match [01:16:38](<a class="yt-timestamp" data-t="01:16:38">01:16:38</a>), [01:11:11](<a class="yt-timestamp" data-t="01:11:11">01:11:11</a>).
*   **Hyperparameter Tuning**: Involves several "sketchy" hyperparameters (e.g., K-nearest neighbors for local constraints, weighting factors for losses) that might need specific tuning for different scenes [01:47:40](<a class="yt-timestamp" data-t="01:47:40">01:47:40</a>), [01:51:15](<a class="yt-timestamp" data-t="01:51:15">01:51:15</a>).
*   **Foreground/Background Dependence**: Uses a foreground/background mask to improve tracking, which may require specific reference frames or consistent lighting conditions [01:57:14](<a class="yt-timestamp" data-t="01:57:14">01:57:14</a>).

## [[Comparison of 3D gaussian splatting to neural radiance fields | Comparison to Neural Radiance Fields (NeRFs)]]

The Dynamic 3D Gaussian technique is presented as a strong alternative to NeRFs for dynamic scene representation:
*   **Explicit vs. Implicit**: 3D Gaussians offer an explicit representation of the scene, allowing for direct manipulation and composability [00:08:48](<a class="yt-timestamp" data-t="00:08:48">00:08:48</a>), while NeRFs are implicit representations (a neural network learns to predict color and density) [00:08:08](<a class="yt-timestamp" data-t="00:08:08">00:08:08</a>).
*   **Rendering Speed**: 3D Gaussians are significantly faster to render in real-time than NeRFs, which require multiple neural network inferences per pixel [01:02:04](<a class="yt-timestamp" data-t="01:02:04">01:02:04</a>), [02:27:29](<a class="yt-timestamp" data-t="02:27:29">02:27:29</a>).
*   **Physics Integration**: The explicit nature of Gaussians makes them more amenable to physics simulations and interactions compared to NeRFs, which lack an explicit concept of objects [02:08:50](<a class="yt-timestamp" data-t="02:08:50">02:08:50</a>).
*   **Tracking**: Dynamic 3D Gaussians inherently yield dense 6-DoF tracking as a byproduct of their optimization process, whereas many dynamic NeRFs require external optical flow or correspondence inputs [01:13:59](<a class="yt-timestamp" data-t="01:13:59">01:13:59</a>), [01:53:05](<a class="yt-timestamp" data-t="01:53:05">01:53:05</a>).

Overall, the Dynamic 3D Gaussian technique shows promising directions for real-time rendering, tracking, and creative scene editing in applications like robotics, augmented reality, and video games [02:21:57](<a class="yt-timestamp" data-t="02:21:57">02:21:57</a>).