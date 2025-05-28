---
title: 3D Scene Representation and Simulation
videoId: _jqhy-dr7Q4
---

From: [[hu-po]] <br/> 

Gaussian Splats are emerging as a significant 3D primitive for scene representation and simulation, particularly in the field of robotics. This technique offers advantages in terms of photorealism, ease of creation, and rendering speed compared to traditional methods like meshes and Neural Radiance Fields (NeRFs) <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a>.

## What are Gaussian Splats?

A Gaussian Splat is a method for rendering a 3D model into 2D images given a specific camera pose <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a>. A 3D scene is represented by a collection of Gaussian points, each parameterized by:
*   A covariance matrix (interpretable as rotation and scale) <a class="yt-timestamp" data-t="00:27:55">[00:27:55]</a>
*   A center position <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>
*   A color <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>
*   An opacity <a class="yt-timestamp" data-t="00:26:48">[00:26:48]</a>

The rendering process is fully differentiable, allowing gradients to be pushed back to these parameters for optimization and scene reconstruction <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>. The final color of a pixel is computed by Alpha blending the subset of Gaussians that intersect a ray emanating from the camera, sorted by depth <a class="yt-timestamp" data-t="00:28:12">[00:28:12]</a>. Gaussian Splats render quickly due to tile-based parallel rendering, which significantly speeds up image generation <a class="yt-timestamp" data-t="00:29:45">[00:29:45]</a>.

## Gaussian Splats in Robotics Simulation

Traditional 3D scene representations using meshes and textures require extensive manual labor to create, especially for high-quality volumetric videos <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. This labor-intensive process makes it difficult to achieve photorealistic simulations that can effectively bridge the "Sim-to-Real" gap in robotics. The Sim-to-Real problem refers to the challenge of transferring policies trained in a simulated environment to real-world deployment <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

Gaussian Splats offer a solution by providing a much easier way to create photorealistic synthetic data <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>:
*   **SplatSim (Carnegie Mellon)**: This paper explores the use of [[Optimization Techniques and Challenges for 3D Scene Representation|Gaussian Splats]] for zero-shot Sim-to-Real transfer of RGB manipulation policies <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. By replacing traditional mesh representations with Gaussian Splats in simulators, SplatSim produces highly photorealistic synthetic data <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. For instance, a robotic arm (UR5 robot with a Robotiq gripper and Intel RealSense depth cameras) is trained on simulated data rendered as Gaussian Splats <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>. This approach achieved an 86% task success rate, compared to 97% when trained on real-world data, demonstrating significant improvement in closing the Sim-to-Real gap <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>.
*   **Beijian Embodied Image-Goal Navigation**: Another application is in robot navigation, where a robot blimp uses Gaussian Splats for image-goal navigation <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. The room scene is captured by collecting 534 RGB images with known camera positions (using an iPhone with markers in an OptiTrack-equipped room) <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This data is fed into a Gaussian Splatting process to create a dense 3D representation. The robot then uses image similarity between its current view (rendered from the Splat) and a target image to navigate <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

### Limitations in Static Scenes

A primary limitation of current Gaussian Splatting for robotics is its application to static scenes <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. In cases where objects within the scene move (e.g., a robot arm), complex segmentation and manipulation of individual Gaussians representing robot links are required <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

## Handling Dynamic Scenes and Streaming

To overcome the static scene limitation and enable large-scale, dynamic 3D environments, new [[Challenges and Opportunities in Dynamic Scenes Representation|techniques for dynamic 3D scene representation]] and streaming are being developed:
*   **Sliding Window Gaussian Splatting (SwinGS)**: This method focuses on streaming Gaussian Splat volumetric videos to [[Meta Quest Pro VR headsets | edge devices]] like VR headsets or robots with limited compute <a class="yt-timestamp" data-t="00:33:39">[00:33:39]</a>. Instead of sending the entire scene, SwinGS streams "slices" of Gaussians, dynamically loading new slices and replacing expired ones to maintain efficient GPU memory usage <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>.
*   **Robust Dual Gaussian Splatting**: Some approaches, like "Robust Dual Gaussian Splatting for Immersive Human-Centric Volumetric Videos," treat every frame of a dynamic scene as a new Gaussian Splat <a class="yt-timestamp" data-t="00:36:27">[00:36:27]</a>. This necessitates highly engineered compression strategies for Gaussian properties (position, rotation, scale, opacity, spherical harmonics), often using techniques like [[residual vector quantization | residual vector quantization]] <a class="yt-timestamp" data-t="00:37:52">[00:37:52]</a>. While impressive (achieving real-time rendering on devices like the Pico VR headset <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>), this approach can be overly complex and less scalable for large, evolving worlds <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.

## Gaussian Splat Optimization and Underlying Principles

The field of Gaussian Splatting is rapidly advancing, with new optimization techniques and open-source implementations:
*   **gplat: An Open Source Library**: This library provides a clean, fast, and Apache 2 licensed implementation of Gaussian Splatting, including CUDA source code for core operations like rasterization and depth compositing <a class="yt-timestamp" data-t="00:45:05">[00:45:05]</a>. Developed by institutions like UC Berkeley, ShanghaiTech University, Amazon, and Luma AI, `gplat` is a significant step towards democratizing Gaussian Splat research and development <a class="yt-timestamp" data-t="00:46:56">[00:46:56]</a>.
*   **3D Gaussian Splatting as Markov Chain Monte Carlo**: A key conceptual advancement is the reinterpretation of 3DGS's initialization and densification strategy as a [[Markoff chain Monte Carlo|Markov Chain Monte Carlo]] (MCMC) sampling task <a class="yt-timestamp" data-t="00:49:52">[00:49:52]</a>. This approach formulates Gaussian Splatting densification as a stochastic gradient Langevin Dynamics update <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>.
    *   **Stochastic Gradient Langevin Dynamics**: This technique draws inspiration from molecular dynamics and Brownian motion, where particles move randomly but are also influenced by forces <a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>. In Gaussian Splatting, "dead" Gaussians (those with low opacity not contributing to the scene) are relocated to positions where more Gaussians are needed (high opacity) <a class="yt-timestamp" data-t="00:57:18">[00:57:18]</a>. This ensures a uniform data volume across time, crucial for streaming volumetric content <a class="yt-timestamp" data-t="00:56:33">[00:56:33]</a>. This reinterpretation helps solve arbitrary hyperparameter issues associated with traditional densification and pruning <a class="yt-timestamp" data-t="00:53:51">[00:53:51]</a>.

## Future of Gaussian Splats and Physics/Interaction

While significant progress has been made in rendering and representation, a missing piece for comprehensive 3D simulation is the integration of physics:
*   **Physics Properties**: Current Gaussian Splats primarily focus on visual appearance. For robotic interactions, properties like weight, friction coefficient, and deformability (elasticity) need to be associated with individual Gaussians <a class="yt-timestamp" data-t="01:10:16">[01:10:16]</a>.
*   **Gaussian Garments**: Research like "Gaussian Garments" explores reconstructing simulation-ready clothing with photorealistic appearance <a class="yt-timestamp" data-t="01:11:01">[01:11:01]</a>. This involves initializing Gaussians on mesh vertices and introducing "physical energies" (e.g., bending energy) to govern the dynamics between adjacent Gaussians, moving towards interactive volumetric video <a class="yt-timestamp" data-t="01:11:56">[01:11:56]</a>. However, current methods often rely on expensive multi-camera setups (e.g., 81 Z CAM cinema cameras <a class="yt-timestamp" data-t="01:17:36">[01:17:36]</a>) or pre-existing Physically Based Rendering (PBR) assets <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>, which limits their accessibility. The goal is to enable creation from simpler inputs like single iPhone videos <a class="yt-timestamp" data-t="01:17:25">[01:17:25]</a>.
*   **[[Camera setup for 3D scene capture|Fisheye Gaussian Splats]]**: This work adapts Gaussian Splatting to integrate input from fisheye cameras, which offer a wider field of view valuable for robotics, addressing the inherent warping in such lenses <a class="yt-timestamp" data-t="01:24:07">[01:24:07]</a>.
*   **[[isotropic Gaussian marbles | Isotropic Gaussian Marbles]]**: To further accelerate rendering, some research simplifies Gaussians to isotropic "marbles" (small circles), reducing the degrees of freedom and achieving faster frame rates <a class="yt-timestamp" data-t="01:42:19">[01:42:19]</a>.
*   **[[LangSplat | LangSplat]]**: This technique adds semantic properties (like object labels) to individual Gaussians, enabling open-vocabulary 3D querying and segmentation <a class="yt-timestamp" data-t="01:47:50">[01:47:50]</a>.
*   **WebGPU Integration**: The development of WebGPU, an open standard supported by major tech companies, aims to allow browser-based access to a device's GPU <a class="yt-timestamp" data-t="01:06:45">[01:06:45]</a>. This will enable real-time rendering of Gaussian Splats and [[video diffusion models in generative 3D|ML inference]] directly within web browsers, expanding their reach to VR headsets and other devices without extensive local compute <a class="yt-timestamp" data-t="01:30:08">[01:30:08]</a>.

### Challenges with Complex Materials

Despite their strengths, Gaussian Splats, like meshes, still face [[Limitations and assumptions of dynamic 3D modeling|challenges in representing complex materials]] such as hair, see-through glass, and smoke <a class="yt-timestamp" data-t="01:49:43">[01:49:43]</a>. However, their fundamental nature as discrete points with properties might offer a more intuitive pathway for future solutions compared to meshes for such difficult materials.

## Conclusion

[[Comparative Analysis of 3D Representation Techniques|Gaussian Splats]] are rapidly becoming a preferred 3D primitive due to their balance of rendering quality and speed, and their relative ease of creation compared to traditional meshes <a class="yt-timestamp" data-t="01:52:13">[01:52:13]</a>. Their differentiable nature supports learning-based approaches, and ongoing research into dynamic scene handling, physics integration, and robust open-source implementations is paving the way for their widespread adoption in robotics simulation, volumetric video, and immersive VR experiences <a class="yt-timestamp" data-t="01:26:20">[01:26:20]</a>.