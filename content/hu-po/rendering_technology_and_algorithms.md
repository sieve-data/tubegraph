---
title: Rendering Technology and Algorithms
videoId: _jqhy-dr7Q4
---

From: [[hu-po]] <br/> 

## Gaussian Splats: A New 3D Primitive

Gaussian Splatting (GS) is an emerging [[novel_view_synthesis_and_rendering_techniques | 3D rendering technique]] gaining traction for its efficiency and photorealism. In the context of robotics, GS is being explored as a powerful alternative to traditional 3D scene representations for simulation and navigation tasks.

### What are Gaussian Splats?
A Gaussian Splat model represents a 3D scene as a collection of individual Gaussian points, each parameterized by its covariance, a center position, a color, and an opacity [00:00:21]. The rendering pipeline for Gaussian Splats is fully [[differentiable_rendering_for_realtime_image_synthesis | differentiable]], allowing for optimization through image similarity and reconstruction losses [00:27:01]. This means that gradients can be pushed back into the parameters of each Gaussian to slowly adjust their positions, colors, sizes, and shapes to approximate a scene [00:27:24].

When rendering a 2D image from a given camera pose, rays emanate from the camera, intersecting various Gaussians [00:28:07]. The final color of a pixel is computed by alpha blending the subset of Gaussians sorted by depth, with closer, more opaque Gaussians contributing more to the pixel's color [00:28:14]. The rendering process is often done in parallel by dividing the image into tiles, significantly increasing speed [00:29:49].

### [[comparative_analysis_of_3d_representation_techniques | Comparison with Other 3D Primitives]]
Gaussian Splats offer distinct advantages compared to other 3D primitives like meshes and Neural Radiance Fields (NeRFs):

*   **Meshes:** Traditional 3D representations used in video games, meshes are compact and rendering-friendly but "require extensive manual labor to create, especially for high-quality volumetric videos" [00:15:27]. Capturing a photorealistic scene with meshes involves significant effort from 3D artists to model every detail, texture, and lighting [00:15:56].
*   **Neural Radiance Fields (NeRFs):** NeRFs can deliver high-quality renderings with reasonable storage [00:15:17]. They implicitly store scene information within the parameters of a multi-layer perceptron (MLP), making them efficient in terms of storage and compressed [00:30:52]. However, unlike Gaussian Splats, it's not possible to segment or manipulate individual parts of a NeRF [00:31:58].
*   **Gaussian Splats:** GS provides a high rendering quality at a very high rendering speed, with a middle amount of storage compared to meshes and NeRFs [00:30:41]. Their explicit representation of individual Gaussians allows for segmentation and manipulation of scene components, a feature not easily achievable with NeRFs [00:31:50]. Creating a GS scene is often simpler than meshes, requiring only a camera to film the environment and then feeding the images into a GS pipeline [00:16:07].

## Applications in Robotics

Gaussian Splats are revolutionizing robotic simulation by enabling [[novel_view_synthesis_and_rendering_techniques | photorealistic rendering]] that bridges the "sim-to-real" gap.

### SplatSim: Zero-Shot Sim-to-Real Transfer
Researchers from Carnegie Mellon University developed **SplatSim**, a method for zero-shot sim-to-real transfer of RGB manipulation policies using Gaussian Splatting [00:06:15]. The core idea is to replace traditional mesh representations in simulators with Gaussian Splats [00:08:41].

*   **Process:** Instead of manually creating simulated environments with meshes and textures, a real-world scene can be captured using an iPhone or depth cameras (like Intel RealSense) to generate a Gaussian Splat model [00:16:07]. This Splat serves as a highly photorealistic simulated environment. While the background remains static, articulated objects like robot arms require specific segmentation of Gaussians for movement [00:12:41].
*   **Benefits:** This approach significantly reduces the manual effort of creating detailed simulations and yields highly photorealistic synthetic data [00:08:47]. Training a robot policy (e.g., a diffusion policy) purely on Gaussian Splat-rendered synthetic data can achieve high task success rates (e.g., 86% for pushing tasks), approaching performance from real-world data training (97%) [00:24:29]. The ultimate goal is to eliminate the need for costly and time-consuming real-world data collection [00:25:17].

### Embodied Image Goal Navigation
Gaussian Splats are also used for robot navigation, as demonstrated in the paper "Beijan: Embodied Image Goal Navigation with Gaussian Splatting" [00:17:37].

*   **Setup:** A robot blimp navigates a physical room using image goal navigation, where a target location is given as an image [00:17:59].
*   **Scene Creation:** The room's 3D environment is captured by collecting 534 RGB images with an iPhone, whose position and pose are tracked by an OptiTrack system [00:18:43]. This data is fed into a Gaussian Splatting process to create a dense 3D representation of the static scene [00:19:16].
*   **Navigation:** The robot uses visual perception to guide itself to the target location [00:18:13]. A model predictive control system utilizes the Gaussian Splat scene to render arbitrary viewpoints and compare them to the goal image, allowing for path planning based on image similarity [00:21:51]. This offers a major shortcut by avoiding manual mesh and texture creation for realistic simulations [00:19:31].

## [[optimization_techniques_and_challenges_for_3d_scene_representation | Optimization Techniques and Challenges]]

### Dynamic Scene Handling and Streaming
A primary [[challenges_and_limitations_in_3d_generation | limitation]] of current Gaussian Splat applications in robotics is their static nature [00:20:21]. To overcome this for dynamic scenes or large environments, streaming techniques are crucial.

The "Swin-GS" (Sliding Window Gaussian Splatting) paper addresses how to stream Gaussian Splats chunk-by-chunk to edge devices like VR headsets or robots [00:33:39]. This involves bringing new Gaussians into GPU memory and removing "expired" ones as the viewpoint or scene content changes over time [00:34:36]. This dynamic swapping of Gaussians is essential for streaming volumetric video or large-scale world models to devices with limited compute resources [00:34:36].

Some approaches to dynamic volumetric video, however, treat each frame as a completely new Gaussian Splat, leading to significant overhead and complex, hand-engineered compression strategies [00:36:51]. These strategies use methods like residual vector quantization for various Gaussian properties (position, rotation, scale, opacity, spherical harmonics) [00:38:06]. While achieving real-time rendering on devices like Pico VR headsets, such overly engineered pipelines are complex and potentially difficult to reproduce or generalize [00:41:54].

### Markov Chain Monte Carlo for Densification and Sparsification
A significant advancement in [[optimization_techniques_and_challenges_for_3d_scene_representation | optimizing Gaussian Splats]] involves reinterpreting the densification and sparsification processes using Markov Chain Monte Carlo (MCMC) sampling [00:43:52].

*   **Initialization and Densification Challenges:** The initial placement of Gaussians (initialization) can be done randomly, via Colmap (structure from motion), or using depth camera point clouds [00:50:07]. Densification (adding Gaussians) and sparsification (removing Gaussians) are crucial for refining the scene representation [00:51:14]. Traditional methods often involve heuristic-based approaches, like splitting a Gaussian into three when it becomes too large, which requires tuning multiple hyperparameters [00:53:27]. This arbitrary hyperparameter tuning can lead to suboptimal results and make the process annoying to manage [00:53:51].
*   **MCMC Reinterpretation:** The 3DGS-MCMC paper reformulates Gaussian Splat densification as a stochastic gradient Langevin Dynamics update [00:49:03]. Instead of arbitrary splitting or pruning, "dead Gaussians" (those with low opacity, contributing little to the scene) are relocated to positions where more Gaussians are needed [00:55:59]. This ensures a uniform data volume, crucial for streaming content where GPU memory must be consistently utilized [00:56:33]. This approach draws an analogy between Gaussian movement and Brownian motion in molecular dynamics, where particles shift in 3D space [00:59:40]. The realization that the Gaussian update equation is strikingly similar to the Langevin equation (used in molecular dynamics) provided a core intuition for this reframing [01:00:00].

### Physical Properties and Interaction
A current [[challenges_and_limitations_in_3d_generation | missing piece]] for Gaussian Splats, especially in robotics and interactive virtual environments, is the integration of physics [01:09:04]. While meshes inherently support physics properties (e.g., collision, friction, weight, deformability), this is still an active area of research for Gaussian Splats [01:09:57].

Some work, like "Gaussian Garments," is beginning to add physics-based properties and relationships between Gaussians [01:11:01]. By integrating "physical energies" (e.g., bending energy) between adjacent Gaussians, researchers are moving towards creating deformable objects (like clothing) within a Gaussian Splat representation [01:11:42]. The ultimate goal is to enable fully interactive volumetric videos where objects can be touched, moved, and react to physical forces [01:12:46].

## [[future_potential_and_direction_for_generative_3d_technology | Future Development and Standardization]]

### Open Source Implementations
The release of open-source libraries like **gplat** (from the creators of NerfStudio, with contributions from UC Berkeley, Amazon, and Luma AI) is a significant step forward for Gaussian Splats [00:45:05]. Prior to gplat, implementations were fragmented and often had licensing issues, making widespread adoption difficult [00:45:32]. gplat provides a clean, fast, Apache 2 licensed implementation, including the underlying CUDA source code for core operations like rasterization [00:46:06]. This collaborative effort accelerates research and development by allowing more people to use, modify, and build upon Gaussian Splats, ultimately fostering faster field progression [00:47:50].

### WebGPU and GPU Acceleration
To make Gaussian Splats universally accessible, especially for VR headsets and web-based applications, it's crucial to leverage browser-based GPU acceleration. WebGL, an older standard, has evolved into WebGPU, which allows direct access to a computer's GPU from within a web browser [01:05:06]. This enables fast, parallel rendering capabilities inherent to Gaussian Splats (like tile-based rendering and optimized sorting) to be performed directly on client devices without requiring specialized software installations [01:06:16]. Major organizations like Apple, Google, Mozilla, Microsoft, and Intel are collaborating on WebGPU, aiming to standardize how Gaussian Splats and other GPU-intensive tasks can be rendered on any browser-enabled device [01:06:50].

### Future Outlook
The [[future_potential_and_direction_for_generative_3d_technology | future potential]] of Gaussian Splats points towards fully immersive volumetric videos and interactive simulated worlds in VR and robotics [01:26:20]. While still facing [[challenges_and_limitations_in_3d_generation | limitations]] such as handling extremely complex materials (e.g., see-through glass, smoke, hair) or requiring multi-camera setups for dynamic scenes, the simplicity of their primitive structure suggests they might fundamentally be better suited for these challenges than traditional meshes [01:49:43]. The ongoing research aims to achieve single-camera capture for dynamic scenes and seamless physics integration, further solidifying Gaussian Splats as a foundational technology for next-generation 3D experiences.