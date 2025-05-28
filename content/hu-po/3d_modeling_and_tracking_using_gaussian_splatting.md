---
title: 3D modeling and tracking using Gaussian splatting
videoId: hDuy1TgD8I4
---

From: [[hu-po]] <br/> 

The paper "Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis" introduces an extension of [[3d_gaussian_splatting_and_nerfs | 3D Gaussian splatting]] to model and track dynamic scenes <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Unlike most [[3d_gaussian_splatting_and_nerfs | Nerfs]] and the original static [[3d_gaussian_splatting_and_nerfs | 3D Gaussian splatting]] paper, this work incorporates the dimension of time, allowing for dynamic scene representation <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Core Concepts

[[dynamic_3d_gaussian_methodology | Dynamic 3D Gaussian methodology]] simultaneously addresses dynamic scene novel view synthesis and six-degree-of-freedom (6DoF) tracking of dense scene elements <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Novel view synthesis involves creating images from a viewpoint not previously seen <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. The "dynamic" aspect refers to the scene changing over time <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. 6DoF tracking accounts for three positional (X, Y, Z) and three rotational degrees of freedom <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

The scene is represented as a collection of [[3d_gaussian_splatting_and_nerfs | 3D Gaussians]] <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Each gaussian has a center, rotation, size, color (RGB), and opacity <a class="yt-timestamp" data-t="01:07:38">[01:07:38]</a>. The total number of parameters for each gaussian is seven times the number of time steps plus eight <a class="yt-timestamp" data-t="01:09:51">[01:09:51]</a>. In this approach, the number, color, opacity, and size of gaussians are fixed across time, while their position and orientation are allowed to vary <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>, enabling them to move and rotate <a class="yt-timestamp" data-t="01:12:02">[01:12:02]</a>. This allows them to be thought of as a particle-based physical model of the world <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>.

## Key Features and Advantages

*   **Novel View Synthesis:** The method allows for the creation of new views, including depth maps <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
*   **Dense 6DoF Tracking:** By enforcing local rigidity and tracking gaussian movement, dense 6DoF tracking emerges naturally <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. This means the system can infer motion and rotation of points in space without explicit inputs like optical flow or skeletons <a class="yt-timestamp" data-t="01:13:59">[01:13:59]</a>.
*   **Real-time Rendering:** A significant advantage of [[3d_gaussian_splatting_and_nerfs | 3D Gaussian splatting]] is its rendering speed due to GPU-optimized sorting <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. This method achieves 850 frames per second on dynamic novel views <a class="yt-timestamp" data-t="00:38:27">[00:38:27]</a>, which is faster than typically required for VR headsets (120 FPS) <a class="yt-timestamp" data-t="00:38:52">[00:38:52]</a>.
*   **Composability and Editing:** [[3d_content_generation_using_gaussian_splatting | Dynamic 3D Gaussians]] are amenable to creative scene editing, such as propagating edits over time, adding or removing dynamic objects, and having cameras follow scene elements <a class="yt-timestamp" data-t="01:52:51">[01:52:51]</a>. This contrasts with [[3d_representation_techniques_nerfs_vs_gausssian_splats | Nerfs]], which lack an explicit notion of objects, making composability difficult <a class="yt-timestamp" data-t="02:16:45">[02:16:45]</a>.
*   **[[physicsbased_modeling_in_gaussian_splats | Physics-based Interactions]]:** Unlike [[3d_gaussian_splatting_and_nerfs | Nerfs]], the explicit nature of [[3d_gaussian_splatting_and_nerfs | 3D Gaussians]] makes them potentially suitable for modeling [[physicsbased_modeling_in_gaussian_splats | physics-based interactions]], such as collisions <a class="yt-timestamp" data-t="02:11:01">[02:11:01]</a>.

## Methodology

### Data Acquisition
The work utilizes synchronized multi-view video captured within a "Panoptic Studio Dome" <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>. This geodesic dome (5.49m radius, 4.15m height) houses 480 synchronized cameras, allowing for instantaneous capture of 400+ pictures with known, calibrated camera positions <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. For experiments, they used 31 cameras (27 for training, 4 for testing) <a class="yt-timestamp" data-t="02:02:18">[02:02:18]</a>. The cameras are roughly positioned in a hemisphere around the area of interest <a class="yt-timestamp" data-t="02:02:27">[02:02:27]</a>.

### Optimization Process
The reconstruction is performed via test-time optimization <a class="yt-timestamp" data-t="01:00:12">[01:00:12]</a>.
1.  **First Time Step Initialization:** The initial scene is optimized by allowing all gaussian properties (position, rotation, size, color, opacity) to vary <a class="yt-timestamp" data-t="01:01:25">[01:01:25]</a>. This first step is crucial as it initializes subsequent time steps <a class="yt-timestamp" data-t="01:01:35">[01:01:35]</a>. It uses a sparse point cloud for initialization, obtained from depth cameras or tools like COLMAP <a class="yt-timestamp" data-t="01:52:48">[01:52:48]</a>. Densification is used to increase gaussian density <a class="yt-timestamp" data-t="01:52:55">[01:52:55]</a>.
2.  **Subsequent Time Steps:** After the first time step, the size, color, and opacity of the gaussians are fixed <a class="yt-timestamp" data-t="01:12:17">[01:12:17]</a>. Only the position and rotation are optimized <a class="yt-timestamp" data-t="01:52:17">[01:52:17]</a>. This is done by iteratively updating parameters using automatic differentiation to decrease the error between rendered and input images <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>. Each time step uses 2,000 iterations, taking approximately 50 seconds per time step for a total of two hours for 150 time steps <a class="yt-timestamp" data-t="01:53:53">[01:53:53]</a>.

The rendering process for optimization uses a differentiable [[3d_gaussian_splatting_and_nerfs | 3D Gaussian splatting]] renderer <a class="yt-timestamp" data-t="01:19:27">[01:19:27]</a>. This involves "splatting" [[3d_gaussian_splatting_and_nerfs | 3D Gaussians]] onto the 2D image plane and combining their influence on each pixel by sorting them by depth and performing front-to-back volume rendering <a class="yt-timestamp" data-t="01:20:33">[01:20:33]</a>.

### Physical Priors and Regularization
To ensure long-term persistent tracks and prevent gaussians from moving freely in uniform color areas, three regularization losses are introduced <a class="yt-timestamp" data-t="01:34:54">[01:34:54]</a>:
*   **Short-term Local Rigidity Loss:** Enforces that nearby gaussians move together, following the rigid body transform of their local coordinate system between time steps <a class="yt-timestamp" data-t="01:36:34">[01:36:34]</a>. This is applied over short time horizons (between current and immediately preceding time step) <a class="yt-timestamp" data-t="01:43:09">[01:43:09]</a>. It uses the 20 nearest neighbors (K=20) for each gaussian <a class="yt-timestamp" data-t="01:43:45">[01:43:45]</a>.
*   **Local Rotational Similarity Loss:** Explicitly forces neighboring gaussians to have similar rotations over time <a class="yt-timestamp" data-t="01:45:33">[01:45:33]</a>. This also operates on short time horizons and uses the same K-nearest neighbors <a class="yt-timestamp" data-t="01:47:09">[01:47:09]</a>.
*   **Long-term Local Isometry Loss:** A weaker constraint that enforces only the distances between gaussians to remain similar over long time horizons (compared to their initial distances at time step zero) <a class="yt-timestamp" data-t="01:49:11">[01:49:11]</a>.

These losses are primarily applied to foreground points, improving efficiency and preventing interactions between foreground and static background elements <a class="yt-timestamp" data-t="01:57:58">[01:57:58]</a>.

### Limitations and [[challenges_and_solutions_in_representing_3d_objects_with_gaussian_splatting | Challenges and Solutions in Representing 3D Objects with Gaussian Splatting]]
*   **New Objects:** The method can only track parts of the scene visible in the initial frame and will fail to reconstruct new objects entering the scene <a class="yt-timestamp" data-t="02:11:11">[02:11:11]</a>.
*   **Multi-Camera Setup Dependence:** It requires a specialized multi-camera setup with perfectly calibrated cameras and known extrinsic matrices, making it unsuitable for "off-the-shelf" monocular video <a class="yt-timestamp" data-t="02:11:51">[02:11:51]</a>.
*   **Uniform Color Areas:** Tracking can be challenging in large areas of near-uniform color, as gaussians might drift without sufficient restriction <a class="yt-timestamp" data-t="01:33:53">[01:33:53]</a>.
*   **Lack of Relighting:** The current implementation fixes gaussian color, disabling view-dependent color (spherical harmonics) for simplicity, which means it cannot naturally handle relighting for compositional scenes <a class="yt-timestamp" data-t="01:10:47">[01:10:47]</a>.

## Applications
[[dynamic_3d_gaussian_methodology | Dynamic 3D Gaussian methodology]] has potential applications across various fields, including:
*   [[gaussian_splats_in_robotics | Robotics]] <a class="yt-timestamp" data-t="02:04:43">[02:04:43]</a>
*   Augmented Reality (AR) <a class="yt-timestamp" data-t="02:04:43">[02:04:43]</a>
*   Self-driving vehicles <a class="yt-timestamp" data-t="02:04:43">[02:04:43]</a>
*   [[3d_content_generation_using_gaussian_splatting | Content creation]] for movies, video games, or the metaverse <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>

## Performance Metrics
The approach achieves a 28.7 Peak Signal-to-Noise Ratio (PSNR) for dynamic novel view rendering <a class="yt-timestamp" data-t="00:38:22">[00:38:22]</a>. For 3D dense non-rigid long-term scene tracking, it shows an average L2 error of 2.21 centimeters <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>. It also achieves an average of 1.57 normalized pixel error on 2D tracking, an order of magnitude better than previous state-of-the-art <a class="yt-timestamp" data-t="00:40:31">[00:40:31]</a>. An ablation study shows that the rigidity loss, background segmentation loss, fixed color/opacity/size parameters, and forward propagation for time initialization are key components for good tracking and view synthesis results <a class="yt-timestamp" data-t="02:18:13">[02:18:13]</a>.

> [!NOTE] Comparison with [[3d_representation_techniques_nerfs_vs_gausssian_splats | Nerfs]]
> [[3d_gaussian_splatting_and_nerfs | 3D Gaussian splatting]] is presented as a strong competitor to [[3d_gaussian_splatting_and_nerfs | Nerfs]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. While [[3d_gaussian_splatting_and_nerfs | Nerfs]] are implicitly represented by neural networks, making them memory efficient, [[3d_gaussian_splatting_and_nerfs | 3D Gaussians]] are explicit. This explicit representation allows for much faster rendering speeds compared to [[3d_gaussian_splatting_and_nerfs | Nerfs]] (850 FPS vs. slower rendering for [[3d_gaussian_splatting_and_nerfs | Nerfs]]) <a class="yt-timestamp" data-t="01:02:02">[01:02:02]</a>. Additionally, the explicit nature of [[3d_gaussian_splatting_and_nerfs | 3D Gaussians]] provides a more direct path towards [[physicsbased_modeling_in_gaussian_splats | physics-based modeling]] and greater composability for scene editing <a class="yt-timestamp" data-t="02:10:51">[02:10:51]</a>.

The research highlights the potential for future innovation in 3D modeling and tracking, especially for real-time applications <a class="yt-timestamp" data-t="02:22:12">[02:22:12]</a>.