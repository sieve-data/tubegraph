---
title: 3D surface reconstruction from RGB images
videoId: ccGxQCpbrnM
---

From: [[hu-po]] <br/> 

[[3D scene modeling and tracking | 3D surface reconstruction]] aims to recover dense geometric scene structures from multiple images observed at different viewpoints <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This process involves creating a mesh, which is typically a collection of triangles with vertices and connecting edges <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The input data often consists of standard RGB images, similar to those captured by a cellphone, which contain red, green, and blue color channels <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## How it Works: Neural Volume Rendering

A key technique used in this field is [[Neural surface reconstruction | neural volume rendering]], which involves using neural networks to render a 3D volume <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This approach can perform [[Neural surface reconstruction | 3D surface reconstruction]] even without auxiliary data like segmentation or depth information <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

> [!NOTE] RGB Images
> RGB images are standard color images with Red, Green, and Blue channels, obtained from devices like cellphones <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

> [!NOTE] Auxiliary Data
> *   **Segmentation:** Dividing an RGB image into different semantic areas (e.g., background, foreground) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
> *   **Depth:** Information about the distance of objects from the camera. This can be implicit (from a stereo camera) or explicit (from a structured light sensor or Lidar) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Challenges in 3D Surface Reconstruction

The primary challenge in [[Neural surface reconstruction | surface reconstruction]] is achieving high detail, including recovering features like cracks, occluded areas, and fine structures <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

Classical multi-view stereo algorithms, while capable of sparse [[3D scene modeling and tracking | 3D reconstruction]], struggle with ambiguous observations, such as regions with homogeneous colors <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. For example, it's difficult for a stereo camera rig to determine the depth of a plain white wall without distinct textures <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. This is due to the "photometric consistency assumption," which relies on consistent color across views but fails with issues like auto-exposure or non-Lambertian (non-uniformly reflective) materials <a class="yt-timestamp" data-t="00:25:44">[00:25:44]</a>.

Another challenge is relying on the quality of generated [[duster_and_multiview_stereo_reconstruction | point clouds]], which often leads to missing or noisy surfaces <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>.

> [!INFO] Point Clouds
> A [[duster_and_multiview_stereo_reconstruction | point cloud]] is a collection of 3D points representing a scene, often obtained from sensors like Lidar <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>.

## Neuralangelo's Approach

Neuralangelo is a framework for high-fidelity [[Neural surface reconstruction | 3D surface reconstruction]] developed by Nvidia Research and Johns Hopkins University <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. It leverages the representation power of [[multiresolution_hash_grids_for_3d_representation | multi-resolution 3D hash grids]] and [[Goshan Splat optimization for 3D reconstruction | neural Signed Distance Functions (SDFs)]] <a class="yt-timestamp" data-t="00:42:20">[00:42:20]</a>.

Key ingredients of Neuralangelo include:
1.  **Numerical gradients for higher-order derivatives:** Instead of analytical gradients, which are exact but can be discontinuous across space with tri-linear interpolation in hash encodings, numerical gradients approximate the derivative <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This allows for smoother surface normals and distributes backpropagation updates beyond local hash grid cells, acting as a smoothing operation on the SDF <a class="yt-timestamp" data-t="01:25:09">[01:25:09]</a>. Numerical gradients are generally faster and easier to compute, especially for complex functions <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
2.  **Progressive optimization schedule:** This involves a course-to-fine approach, where the algorithm starts with a coarse resolution and gradually adds finer resolutions during optimization <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This helps avoid falling into false local minima in the loss landscape <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

### Core Components

*   **[[multiresolution_hash_grids_for_3d_representation | Multi-resolution 3D Hash Grids]]:** Neuralangelo utilizes a system of 16 different 3D grids, each at a different resolution <a class="yt-timestamp" data-t="01:01:31">[01:01:31]</a>. Each entry in these hash maps stores an encoding feature, which is a vector representing the feature at a specific point in space <a class="yt-timestamp" data-t="01:02:27">[01:02:27]</a>. These features are interpolated using tri-linear interpolation <a class="yt-timestamp" data-t="01:03:17">[01:03:17]</a>. The encoded features from all resolutions are concatenated and fed into a shallow Multi-Layer Perceptron (MLP) <a class="yt-timestamp" data-t="01:04:49">[01:04:49]</a>.
    *   Unlike sparse voxel structures (like OctTrees) which have a hierarchical decomposition and fixed resolutions, hash encoding assumes no spatial hierarchy, resolving collisions through gradient averaging <a class="yt-timestamp" data-t="01:07:08">[01:07:08]</a>.
*   **Neural SDF Representation:** Neuralangelo uses a [[Goshan Splat optimization for 3D reconstruction | neural SDF]] to represent the underlying 3D scene <a class="yt-timestamp" data-t="02:05:04">[02:05:04]</a>. An SDF is a function that gives the signed distance from any point in 3D space to the surface of an object <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The surface itself is defined as the zero-level set of this function (where the distance is zero) <a class="yt-timestamp" data-t="00:55:25">[00:55:25]</a>.
*   **Neural Volume Rendering (Similar to [[Transformer models in 3D reconstruction | NeRFs]]):** The method samples 3D locations along camera view directions and uses an MLP to predict color and volume density for each point <a class="yt-timestamp" data-t="00:46:06">[00:46:06]</a>. The final pixel color is approximated by integrating the color radiance and opacity of sampled points along the ray <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.
    *   > [!INFO] [[Transformer models in 3D reconstruction | Neural Radiance Fields (NeRFs)]]
        > A [[Transformer models in 3D reconstruction | NeRF]] encodes a 3D scene within the weights of a Multi-Layer Perceptron (MLP), mapping 3D spatial locations and viewing directions to color and volume density <a class="yt-timestamp" data-t="03:09:58">[03:09:58]</a>. While powerful for novel view synthesis, [[Transformer models in 3D reconstruction | NeRFs]] typically result in fuzzy surfaces and do not provide an explicit geometric representation, making surface extraction challenging <a class="yt-timestamp" data-t="03:25:23">[03:25:23]</a>.

### Optimization and Loss Functions

Neuralangelo uses an end-to-end training approach <a class="yt-timestamp" data-t="01:46:07">[01:46:07]</a>, optimizing through a total loss function that combines:
*   **RGB Loss (L_RGB):** Measures the L1 distance between the rendered image pixels (C_hat) and the actual input image pixels (C) <a class="yt-timestamp" data-t="00:52:11">[00:52:11]</a>.
*   **Iconal Loss (L_ike):** A regularization term that enforces the gradient of the SDF to have a unit norm (magnitude of one) almost everywhere, promoting a valid SDF representation <a class="yt-timestamp" data-t="01:09:59">[01:09:59]</a>.
*   **Curvature Loss (L_curve):** Another regularization term that penalizes mean curvature, encouraging smoother reconstructed surfaces <a class="yt-timestamp" data-t="01:44:10">[01:44:10]</a>. This loss is progressively increased over training iterations using a "warm-up" period <a class="yt-timestamp" data-t="02:03:30">[02:03:30]</a>.
*   **Weight Decay:** Applied to all parameters to prevent single-resolution features from dominating the final result <a class="yt-timestamp" data-t="01:42:43">[01:42:43]</a>.

The course-to-fine optimization strategy progressively activates finer hash grids and decreases the numerical gradient step size over time <a class="yt-timestamp" data-t="01:52:50">[01:52:50]</a>.

## Applications

[[3D Representations and Their Applications | Recovered surfaces]] provide structural information useful for many downstream applications <a class="yt-timestamp" data-t="01:11:18">[01:11:18]</a>, including:
*   **3D asset generation:** Creating meshes for use in video games or other virtual environments <a class="yt-timestamp" data-t="01:11:21">[01:11:21]</a>.
*   **Environment mapping:** For autonomous navigation in robotics <a class="yt-timestamp" data-t="01:11:55">[01:11:55]</a>.
*   **Augmented and Virtual Reality (AR/VR):** Enabling realistic digital twins of the real world <a class="yt-timestamp" data-t="01:12:08">[01:12:08]</a>.

## Evaluation and Results

Neuralangelo was evaluated on standard benchmarks:
*   **DTU dataset:** Consists of 15 object-centric scenes with 49-64 images captured by a robot-held monocular RGB camera, providing highly accurate camera poses <a class="yt-timestamp" data-t="01:46:47">[01:46:47]</a>. Ground truth surfaces were obtained from a structured light scanner <a class="yt-timestamp" data-t="01:48:02">[01:48:02]</a>.
*   **Tanks and Temples dataset:** Features six large-scale indoor and outdoor scenes with 263-1107 images captured by a handheld monocular RGB camera, offering less accurate poses but more images <a class="yt-timestamp" data-t="01:48:25">[01:48:25]</a>. Ground truth was obtained via Lidar <a class="yt-timestamp" data-t="01:49:18">[01:49:18]</a>.

Neuralangelo achieves the lowest Chamfer distance and highest F1 score for surface evaluation, and the highest Peak Signal-to-Noise Ratio (PSNR) for image synthesis quality, indicating superior reconstruction quality <a class="yt-timestamp" data-t="01:52:09">[01:52:09]</a>.

> [!INFO] [[Comparison of 3D Representation Techniques | Level of Detail (LOD)]]
> The course-to-fine optimization naturally provides [[Comparison of 3D Representation Techniques | multiple levels of detail]] for the reconstructed assets, similar to how video games render objects with varying complexity based on their distance from the viewer <a class="yt-timestamp" data-t="01:59:31">[01:59:31]</a>.

## Limitations and Future Directions

The method currently samples pixels from images randomly, which requires long training iterations to ensure sufficient detail sampling <a class="yt-timestamp" data-t="02:05:30">[02:05:30]</a>. Future work aims to explore more efficient sampling strategies to accelerate the training process <a class="yt-timestamp" data-t="02:06:06">[02:06:06]</a>.