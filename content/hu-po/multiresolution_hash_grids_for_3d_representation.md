---
title: Multiresolution hash grids for 3D representation
videoId: ccGxQCpbrnM
---

From: [[hu-po]] <br/> 

Multiresolution hash grids are a key component in advanced 3D representation techniques, notably employed in frameworks like Neuralangelo for high-fidelity 3D surface reconstruction from RGB images <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This approach utilizes a neural volume rendering method <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Core Concept

A hash grid functions as a map, establishing a correspondence between a key and a value <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. In the context of 3D representation, a 3D hash grid maps a 3D position in space to a stored value <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This allows for quick access to information within a [[canonical_3d_volume_representation | 3D volume]] <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

The "multiresolution" aspect means that the system employs different sizes or resolutions for this hash map with respect to the volume <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This can include coarse, fine, and even extra-fine resolutions <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. In Neuralangelo, there are typically multiple stages of these resolutions, often more than two <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>, with one example using 16 total grids <a class="yt-timestamp" data-t="01:50:02">[01:50:02]</a>.

Each hash entry in these grids stores an encoding feature <a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>. For a given input 3D position, the system maps it to corresponding positions at each grid resolution <a class="yt-timestamp" data-t="01:02:11">[01:02:11]</a>. The feature vector for a given resolution is obtained through tri-linear interpolation of hash entries at the grid cell corners <a class="yt-timestamp" data-t="01:03:17">[01:03:17]</a>. The encoding features from all spatial resolutions are then concatenated to form a single feature vector, which serves as input to a shallow Multi-Layer Perceptron (MLP) <a class="yt-timestamp" data-t="01:04:49">[01:04:49]</a>.

## Advantages and Applications

Multiresolution hash encoding offers several advantages:
*   **Representation Power and Fine Detail:** It greatly increases [[3d_representations_and_their_applications | representation power]], achieving success in representing fine-grained details for tasks like object shape representation and novel view synthesis <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>, <a class="yt-timestamp" data-t="01:00:06">[01:00:06]</a>.
*   **Scalability and Memory Efficiency:** This hybrid 3D grid structure allows for a lightweight MLP that is more expressive while maintaining a memory footprint that is log-linear to the resolution <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>, <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.
*   **Implicit vs. Explicit Depth:** Neuralangelo demonstrates that multiresolution hash encodings can effectively recover dense 3D surface structures from multi-view RGB images *without* requiring auxiliary data like segmentation or explicit depth (e.g., from stereo cameras or LiDAR) <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>, <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. This contrasts with traditional multi-view stereo algorithms that struggle with homogeneous colors without such depth information <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
*   **Level of Detail (LOD):** The progressive nature of activating finer hash grids means the system can naturally provide different levels of detail for the reconstructed scene <a class="yt-timestamp" data-t="02:00:20">[02:00:20]</a>.

## Comparison with Other Techniques

Multiresolution hash grids differ from sparse voxel structures like octrees <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>. While octrees use a tree structure to represent 3D space with varying resolutions within a single grid <a class="yt-timestamp" data-t="01:06:14">[01:06:14]</a>, hash encoding assumes no spatial hierarchy and handles collisions automatically through gradient averaging <a class="yt-timestamp" data-t="01:07:08">[01:07:08]</a>. This implies that hash grids can have multiple grids "on top of each other," unlike an octree where resolution varies within a single structure <a class="yt-timestamp" data-t="01:07:38">[01:07:38]</a>.

## Role in Neuralangelo's Optimization

Neuralangelo combines multiresolution hash encodings with [[canonical_3d_volume_representation | neural Signed Distance Function (SDF)]] representations <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>. Two key findings in Neuralangelo relate to unlocking the potential of these encodings:

1.  **Numerical Gradients for Higher Order Derivatives:** The analytical gradients of hash encodings are not continuous across space when using tri-linear interpolation due to rounding operations within the grid <a class="yt-timestamp" data-t="01:15:48">[01:15:48]</a>, <a class="yt-timestamp" data-t="01:18:23">[01:18:23]</a>. This discontinuity means analytical gradients are limited to local grid cells <a class="yt-timestamp" data-t="01:23:41">[01:23:41]</a>. To overcome this, Neuralangelo computes surface normals using numerical gradients <a class="yt-timestamp" data-t="01:25:13">[01:25:13]</a>. By taking numerical samples with a step size that extends beyond a single grid cell, the numerical gradient effectively distributes backpropagation updates to hash entries in multiple grid cells simultaneously <a class="yt-timestamp" data-t="01:25:34">[01:25:34]</a>. This also acts as a smoothing operation on the analytical gradient expression <a class="yt-timestamp" data-t="01:25:51">[01:25:51]</a>.
2.  **Course-to-Fine Optimization Strategy:** This strategy helps shape the loss landscape to avoid falling into false local minima <a class="yt-timestamp" data-t="01:36:17">[01:36:17]</a>. Neuralangelo adopts a progressive optimization schedule where it starts with only an initial set of coarse hash grids <a class="yt-timestamp" data-t="01:51:53">[01:51:53]</a>. As the optimization progresses and the numerical gradient's step size decreases (matching the grid size), finer hash grids are progressively activated <a class="yt-timestamp" data-t="01:41:51">[01:41:51]</a>, <a class="yt-timestamp" data-t="01:51:51">[01:51:51]</a>. This allows for rapid initial reconstruction and then iterative refinement for more detailed structures <a class="yt-timestamp" data-t="01:42:14">[01:42:14]</a>.