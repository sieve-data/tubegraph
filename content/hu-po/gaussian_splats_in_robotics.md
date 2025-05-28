---
title: Gaussian Splats in Robotics
videoId: _jqhy-dr7Q4
---

From: [[hu-po]] <br/> 

[[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] are being actively explored for robotics applications, with recent research examining their potential advantages and disadvantages in the field [00:03:28].

## What are Gaussian Splats?
A [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splat]] model represents a 3D scene using a collection of "Gaussian points" [00:26:42]. Each Gaussian point is parameterized by:
*   A center position [00:26:46]
*   A covariance (which can be decomposed into a rotation matrix and a scaling matrix, affecting its spread and scale) [00:26:46] [00:27:54] [01:42:30]
*   A color [00:26:47]
*   An opacity [00:26:48]

The rendering pipeline for [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] is fully differentiable [00:27:07] [00:28:18]. This allows gradients to be pushed back into these parameters, enabling the [[3D modeling and tracking using Gaussian splatting | Gaussian Splats]] to learn and approximate a scene over time by adjusting the positions, colors, sizes, and shapes of the individual Gaussians [00:27:24].

A key advantage is their fast rendering speed, partly due to parallel processing of two-dimensional images in "tiles" [00:29:30] [01:06:14].

## Core Use Cases in Robotics

### Sim-to-Real Transfer
One significant application of [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] in robotics is to bridge the "sim-to-real" gap [00:08:19]. Traditional mesh-based simulations struggle to perfectly transfer learned policies to real-world environments due to a "significant domain shift" in visual data [00:13:52] [00:08:34].

Projects like "SplatSim" use [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] to replace traditional mesh representations in simulators, producing "highly photorealistic synthetic data" [00:08:41] [00:08:47]. This allows robots to be trained in simulation with visual data that more closely resembles the real world, improving transfer performance [00:16:16].

For example, a diffusion policy trained solely on [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splat]] synthetic data achieved an 86% task success rate, compared to 97% when trained on real-world data [00:24:29]. While not 100% equivalent, this significantly closes the sim-to-real gap, reducing the need for costly and time-consuming real-world data collection [00:25:04].

### Image Goal Navigation
[[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] can also be used for embodied image goal navigation [00:17:37]. A robot, such as a blimp, can be given a target image and then use visual perception to navigate to the location where that image was originally captured [00:17:59].

Creating complex environments with meshes and textures for such tasks is difficult and requires significant manual effort from 3D artists [00:18:24] [00:15:27]. Instead, a scene can be captured by simply walking through it with an iPhone (equipped with positional tracking) to collect many RGB images and their poses [00:18:40]. These images are then fed into a [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splatting]] process, which learns the positions of the Gaussians to create a representational model of the entire scene [00:19:11]. This allows rendering of any arbitrary viewpoint within the scene, facilitating path planning based on image similarity to reach a goal [00:19:26] [00:21:46].

## Advantages of Gaussian Splats in Robotics

*   **Photorealism & Ease of Creation**: [[Comparison between gaussian splats and traditional 3D representation methods | Gaussian Splats]] produce highly photorealistic renderings that are easier to create than traditional meshes and textures, which require extensive manual labor from 3D artists [00:08:47] [00:15:27] [00:16:16] [00:20:00]. Instead of manually modeling every detail, one can simply record a scene with a camera and convert it into a Splat [00:16:07].
*   **Fast Rendering Speed**: [[Comparison between gaussian splats and traditional 3D representation methods | Gaussian Splats]] offer high rendering quality at a very high rendering speed, making them suitable for real-time applications like VR headsets and potentially robots [00:30:41] [01:39:56].
*   **Differentiability**: The differentiable rendering pipeline allows for learning-based approaches to create and optimize Splats [00:29:35].
*   **Explicit Representation**: Unlike [[3d_representation_techniques_nerfs_vs_gausssian_splats | Nerfs]] which implicitly store scene information, [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] explicitly store parameters for each Gaussian [00:31:16]. This explicitness allows for easier segmentation of different parts of a scene, enabling manipulation of individual object components [00:31:30]. For example, the different links of a robot arm can be segmented and moved independently within a Splat scene [00:12:40].

## Challenges and Future Directions

### Static Scene Limitation
A major limitation of current [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splat]] models used in robotics is their static nature [00:20:14]. Once a scene is recorded and a Splat is created, dynamic changes within the environment are difficult to represent without complex workarounds [00:20:23] [00:20:47].

### Dynamic Scene Handling
To address dynamic scenes and volumetric video, research explores techniques like "sliding window [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splatting]]" (Swin-GS) [00:32:33] [00:33:36]. This involves continuously bringing new Gaussians into GPU memory and removing old, irrelevant ones [00:34:36] [01:27:55]. This streaming approach is crucial for robotics where a robot might navigate a large, dynamic world, streaming only the relevant parts of the environment from a cloud server [00:33:57].

### Optimization and Densification
The process of optimizing [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] involves "densification" (adding Gaussians to represent empty spaces) and "sparsification" or "pruning" (removing dead or transparent Gaussians) [00:51:11]. Traditionally, these processes rely on heuristic-based approaches with manually tuned hyperparameters, which can be arbitrary and difficult to optimize [00:53:21] [01:29:02].

A novel approach reinterprets [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splatting]] densification as a Markov Chain Monte Carlo (MCMC) sampling task, specifically using "stochastic gradient Langevin Dynamics" (SGLD) [00:43:12] [00:48:52]. This framework, inspired by molecular dynamics and Brownian motion, treats Gaussians as particles moving in a 3D space [00:59:50] [01:00:00]. Instead of adding or removing Gaussians, dead Gaussians are "relocated" to areas that need more representation [00:55:57]. This maintains a uniform data volume, which is crucial for streaming content and optimizing GPU memory usage on edge devices like robots [00:56:31] [01:20:42].

### Physics Integration
A current gap in [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] is the lack of inherent physics capabilities [01:09:04]. Unlike meshes, which have well-developed physics engines for interaction, collision, and deformation, Splats do not yet have widely adopted physics properties like weight, friction, or deformability [01:09:50] [01:10:07].

Research like "Gaussian Garments" explores adding "physical energies" to Gaussians [01:11:42]. This involves defining relationships between Gaussians to simulate properties like bending or stretching energy in clothing, allowing for more realistic and interactive volumetric videos [01:12:05] [01:25:36]. The long-term goal is to move towards fully [[physicsbased_modeling_in_gaussian_splats | physics-based Gaussian Splat]] scenes where even interaction physics are handled by Gaussians [01:12:56].

### Accessibility and Tooling
The development of open-source libraries like "gplat" is a significant step forward [00:45:05]. It provides a clean, fast, and openly licensed implementation of [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]], including CUDA code for optimized operations like rasterization and sorting [00:45:52] [01:30:46]. This collaborative effort by various institutions and companies, including Luma AI, promotes faster progress in the field by making the technology more accessible for research and development [00:46:56] [00:47:50].

### Rendering on Edge Devices
A key focus is enabling [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splat]] rendering on lower-compute edge devices like VR headsets and robots [00:49:51]. This requires efficient compression strategies and leveraging browser-based GPU access through standards like WebGPU [00:41:27] [01:04:46] [01:06:50]. This will allow volumetric videos and interactive experiences to be accessed and rendered directly in VR headsets or on robots [01:07:03].

## Conclusion
[[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] offer a promising alternative to traditional 3D representations for robotics due to their ease of creation, photorealism, and fast rendering speeds [01:52:19]. They are already being used to improve sim-to-real transfer and enable image-goal navigation by providing more realistic simulated environments [01:51:42]. While challenges remain in handling dynamic scenes and integrating full physics models, ongoing research, particularly the adoption of MCMC-inspired optimization and the development of open-source tooling, is rapidly advancing their capabilities and paving the way for a future where [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] form the core of robot world models and immersive virtual environments [01:59:19] [01:55:05] [02:00:50].