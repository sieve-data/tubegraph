---
title: Novel view synthesis and rendering techniques
videoId: JdfrG89iPOA
---

From: [[hu-po]] <br/> 

[[multiview_synthesis_and_its_applications | Novel view synthesis]] is the process of creating an image or view from a 3D scene from an angle not previously seen [00:04:54]. This technique allows for generating new perspectives of an object or scene from a limited set of existing photographs [00:13:14].

## Key Techniques in 3D Scene Representation

Historically, [[3d_scene_representation_and_simulation | 3D scene representation]] and novel view synthesis have relied on complex pipelines, but recent advancements in [[rendering_technology_and_algorithms | rendering technology]] have introduced more efficient methods.

### 3D Gaussian Splatting

[[3d_scene_representation_and_simulation | 3D Gaussian Splatting]] (3DGS) is a modern [[comparative_analysis_of_3d_representation_techniques | 3D representation technique]] that models a scene as a set of individual 3D Gaussian "splats" [00:07:54]. Each splat is a small, ellipsoidal bubble with specific properties:
*   **Position (mean vector)**: An XYZ coordinate in 3D space [00:28:21].
*   **Covariance Matrix**: Defines the shape, rotation, and scaling of the ellipsoid [00:28:49].
*   **Spherical Harmonic Coefficients**: Capture view-dependent color appearance, meaning the splat's color can change based on the viewing angle [00:27:28].
*   **Opacity**: Determines how transparent or opaque the splat is [00:28:42].

The rendering process for 3DGS is fully [[differentiable_rendering_for_realtime_image_synthesis | differentiable rendering for real-time image synthesis]], allowing gradients to be pushed directly back to the Gaussian parameters for optimization [01:11:41]. This is achieved by sorting Gaussians based on their distance to the camera and compositing them [01:12:47]. The explicit nature of 3DGS makes it easier to compose and manipulate objects within a scene [01:36:20].

### Neural Radiance Fields (NeRFs)

Neural Radiance Fields (NeRFs) represent a 3D scene implicitly using a small multi-layer perceptron (MLP) [01:15:54]. This MLP takes camera position and view direction as input and outputs a color and opacity for any point in 3D space [01:16:35]. Like 3DGS, NeRFs also use a [[differentiable_rendering_for_realtime_image_synthesis | differentiable rendering]] process for optimization [01:16:47].

#### Comparison: 3D Gaussian Splatting vs. NeRFs
*   **Representation**: 3DGS uses an explicit representation (individual splats), while NeRFs use an implicit representation (neural network weights) [01:17:17].
*   **Size**: NeRFs are generally smaller, making them highly efficient for transmission and loading onto devices with limited compute, such as VR headsets [01:35:16].
*   **Modeling Complex Phenomena**: NeRFs are often better at modeling translucent or amorphous objects like smoke or fire [01:35:36].

## [[challenges_and_limitations_in_3d_generation | Challenges and Limitations in 3D Generation]]

Traditional [[3d_scene_representation_and_simulation | 3D scene representation]] and [[multiview_synthesis_and_its_applications | novel view synthesis]] methods, particularly those relying on Structure from Motion (SfM) pipelines like Colmap, face several [[challenges_and_limitations_in_3d_generation | challenges and limitations]]:
*   **Camera Parameters**: They typically require an initial estimation of camera intrinsics (focal point, principal point, lens distortion) and extrinsics (camera position and pose relative to the 3D scene) [00:05:24]. Obtaining these parameters, especially from real-world photos, is often difficult and prone to error [00:06:13].
*   **Dense Viewpoints**: Many methods necessitate dense viewpoints, meaning a large number of images covering the scene thoroughly [00:13:31]. Sparse input data leads to difficulty in learning details and can introduce errors [00:13:49].
*   **Pipeline Complexity**: Traditional pipelines are modular, breaking down the problem into sub-problems like feature extraction, image registration, and bundle adjustment [00:34:20]. This complexity can lead to accumulating errors and makes further improvements challenging [00:35:12].

## Duster: A Simplified Approach to 3D Vision

Duster (Dense UNconstrained STEReo reconstruction) is a radically novel approach designed to simplify [[3d_scene_representation_and_simulation | 3D scene representation]] by estimating camera parameters and 3D geometry without prior information about camera calibration or viewpoint poses [00:32:44].

### How Duster Works
Duster's core innovation lies in its use of pre-trained Transformer models [00:33:00]. It processes two input images (I1 and I2) using a shared Siamese Vision Transformer (ViT) encoder [00:41:17]. These encoders produce token representations (F1 and F2) which are then fed into two Transformer decoders. Crucially, these decoders constantly exchange information via cross-attention, allowing for internal collaboration between the views [00:42:26].

The regression heads of the decoders directly output two corresponding Point Maps (X11 and X21) and associated Confidence Maps [00:43:23].
*   **Point Map**: A 2D grid (width x height) where each "pixel" stores an XYZ coordinate in 3D space, mapping image pixels to 3D scene points [00:39:41].
*   **Confidence Map**: For each pixel in the point map, a single number indicates the confidence in that 3D point's accuracy [00:45:17]. This helps the network extrapolate in harder areas, such as those with shadows or partial views [00:59:07].

Duster is trained using a simple regression loss based on the Euclidean distance between predicted and ground truth point maps, weighted by the confidence score [00:57:48]. Unlike traditional methods, it does not enforce any geometric constraints, relying instead on the power of large datasets and deep learning to infer the necessary relationships [00:54:55]. The ViT encoders are pre-trained using Croco, a self-supervised method that uses a masked image modeling loss on synthetic indoor scene image pairs from the Habitat simulator [00:48:00].

### Duster vs. Colmap
Duster is significantly faster and simpler than Colmap, often outperforming it in various [[evaluation_of_3d_generative_techniques | evaluation of 3D generative techniques]] tasks, including monocular and multi-view depth estimation, and relative pose estimation [00:24:18]. While Colmap takes around 3 minutes for certain tasks, Duster can complete them in about 0.13 minutes [01:03:49]. Duster's ability to work with uncalibrated and unposed cameras without needing ground truth information is a major advantage for real-world applications [00:32:44].

## Instant-Splat: Leveraging Duster for 3D Gaussian Splatting

Instant-Splat is a framework that unifies explicit [[3d_scene_representation_and_simulation | 3D Gaussian Splatting]] representation with pose priors obtained from Duster [01:09:42]. It offers a fast pipeline for novel view synthesis, capable of completing the process in less than one minute on a consumer GPU (e.g., Nvidia A100) [01:02:03].

### Instant-Splat's Two-Part Pipeline
1.  **Coarse Geometric Initialization (CGI)**: This initial step leverages Duster to provide a globally aligned point map and initial camera poses. This replaces the traditional, time-consuming SfM pipelines like Colmap [01:09:32]. This part typically takes about 20 seconds [01:07:42].
2.  **Fast 3D Gaussian Optimization (F3D-GO)**: Using the output from Duster, Instant-Splat performs a rapid optimization of the 3D Gaussian attributes (position, color, opacity, etc.) and concurrently optimizes camera parameters [01:10:01].

### Optimization Techniques
A key aspect of Instant-Splat's efficiency is its ability to minimize the need for manual optimization steps common in other 3DGS pipelines, such as adaptive density control (densification, splitting, and opacity resets) [01:09:49]. By jointly optimizing the Gaussian attributes and camera poses, Instant-Splat allows information to "leak" and help both tasks, leading to a more streamlined and simplified procedure [01:10:01]. A constraint is added to ensure that the optimized camera poses do not deviate excessively from Duster's initial positions, maintaining geometric consistency [01:10:08].

## Evaluation and Performance

Instant-Splat demonstrates superior rendering quality and pose estimation accuracy compared to existing methodologies [01:25:55]. It achieves significant speedups, for example, processing a scene in roughly 37 seconds compared to 90 minutes for some NeRF-based techniques [01:12:03].

Metrics used for evaluation include:
*   **Absolute Trajectory Error (ATE)** [01:21:00]
*   **Relative Pose Error (RPE)** [01:21:02]
*   **Peak Signal-to-Noise Ratio (PSNR)** [01:21:04]
*   **Structural Similarity Index Measure (SSIM)** [01:21:07]
*   **Learned Perceptual Image Patch Similarity (LPIPS)** [01:21:11]

While quantitative metrics like PSNR and SSIM are commonly used, subjective human evaluation is considered the "gold standard" for assessing rendering quality [01:21:36]. Instant-Splat consistently shows strong performance across various datasets, often outperforming or matching state-of-the-art methods, especially considering it doesn't require specific training on the evaluation datasets [01:02:00].