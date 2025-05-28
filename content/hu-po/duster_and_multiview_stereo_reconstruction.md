---
title: Duster and Multiview Stereo Reconstruction
videoId: JdfrG89iPOA
---

From: [[hu-po]] <br/> 

Duster is a novel approach for dense, unconstrained, or under-constrained [[3d_surface_reconstruction_from_rgb_images | 3D Reconstruction]] from uncalibrated and unposed cameras <a class="yt-timestamp" data-t="00:36:19">[00:36:19]</a>. It addresses the challenge of estimating 3D geometry and camera parameters from a set of photographs of a scene, a task that subsumes nearly all other geometric 3D Vision tasks <a class="yt-timestamp" data-t="00:33:53">[00:33:53]</a>.

The name Duster stands for "geometric 3D Vision Made Easy" <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>. It aims to simplify the complex pipelines traditionally used for [[3d_scene_modeling_and_tracking | 3D scene modeling and tracking]] <a class="yt-timestamp" data-t="00:38:06">[00:38:06]</a>.

## Challenges with Traditional Multiview Stereo (MVS) Pipelines

Traditional methods for [[3d_surface_reconstruction_from_rgb_images | 3D reconstruction]], particularly in the context of novel view synthesis (creating an image from an unseen viewpoint of a 3D scene) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, often rely on complex pipelines like COLMAP <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. These methods present several significant challenges:

*   **Camera Parameters:** They typically require an initial estimation of camera intrinsics (information intrinsic to the camera, like focal point, principal point, lens distortion) and extrinsics (position of the camera relative to the 3D scene) <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Obtaining these in real-world scenarios is difficult and cumbersome <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>, <a class="yt-timestamp" data-t="00:32:37">[00:32:37]</a>.
*   **Dense Viewpoints:** Traditional methods often assume dense viewpoints, meaning a large number of images sufficiently covering the entire scene <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>, <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>. This is often impractical in real-world settings where input data is sparse <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **Pipeline Complexity:** Structure-from-Motion (SfM) pipelines like COLMAP involve a complex chain of sequential sub-problems (e.g., feature extraction, image matching, geometric verification, bundle adjustment, triangulation) <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>, <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>. Each sub-problem's imperfect solution can introduce noise that accumulates through the pipeline, increasing overall complexity and engineering effort <a class="yt-timestamp" data-t="00:35:15">[00:35:15]</a>. These over-engineered approaches become very difficult to understand or improve further <a class="yt-timestamp" data-t="00:37:17">[00:37:17]</a>.
*   **Unreliability:** COLMAP software can be unreliable in producing camera poses and registering all input images <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>.

## Duster's Approach

Duster offers a radically novel solution to these problems by:

*   **No Prior Information:** It operates without requiring prior information about camera calibration or viewpoint poses <a class="yt-timestamp" data-t="00:32:44">[00:32:44]</a>.
*   **Simultaneous Problem Solving:** Instead of a complex chain of sub-problems, Duster solves multiple minimal problems simultaneously, allowing for internal collaboration between them <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.
*   **[[transformer_models_in_3d_reconstruction | Transformer Models]]:** Duster leverages pre-trained [[transformer_models_in_3d_reconstruction | Transformer models]] for encoding and decoding <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.
*   **Direct Regression:** The network is trained using a simple regression loss in 3D space, specifically an L1 Euclidean distance between ground truth and predicted point maps <a class="yt-timestamp" data-t="00:56:45">[00:56:45]</a>. This means it directly outputs 3D points without enforcing traditional geometric constraints or inductive biases from human intuition <a class="yt-timestamp" data-t="00:37:42">[00:37:42]</a>, <a class="yt-timestamp" data-t="00:54:25">[00:54:25]</a>.
*   **Point Maps:** Duster outputs "point maps," which are WxHx3 images where the three channels represent XYZ coordinates of 3D scene points, mapping one-to-one with image pixels <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>, <a class="yt-timestamp" data-t="00:39:39">[00:39:39]</a>. It also outputs associated confidence maps for each point <a class="yt-timestamp" data-t="00:44:57">[00:44:57]</a>.
*   **Self-Supervised Pre-training:** The underlying [[transformer_models_in_3d_reconstruction | Vision Transformers]] are pre-trained using a method called KOCO (Cross-view Completion) <a class="yt-timestamp" data-t="00:47:24">[00:47:24]</a>. KOCO uses a masked image modeling loss where a neural network predicts masked patches in an input image, influenced by a reference view of the same scene from a different viewpoint <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>. This pre-training is performed on a massive dataset of over 2 million synthetic image pairs of 3D indoor scenes, rendered in the Habitat simulator using data from Scannet, Replica, ReplicaCAD, and HM3D <a class="yt-timestamp" data-t="00:51:26">[00:51:26]</a>, <a class="yt-timestamp" data-t="00:52:05">[00:52:05]</a>. This allows the model to learn high-level semantics about objects and scenes <a class="yt-timestamp" data-t="00:49:16">[00:49:16]</a>.
*   **Speed:** Duster is significantly faster than COLMAP, taking about 0.13 minutes (roughly 8 seconds) compared to COLMAP's 3 minutes <a class="yt-timestamp" data-t="01:03:47">[01:03:47]</a>.

## Performance and Applications

Duster achieves state-of-the-art results in various 3D Vision tasks, including:

*   [[applications_and_limitations_of_monocular_depth | Monocular Depth Estimation]] <a class="yt-timestamp" data-t="00:33:16">[00:33:16]</a>
*   Multi-view depth <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>
*   Multi-view camera pose estimation <a class="yt-timestamp" data-t="00:33:21">[00:33:21]</a>
*   3D reconstruction <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>
*   Visual localization <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>

The model demonstrates robust performance even with varying image orientations (vertical vs. horizontal) and challenging lighting conditions like shadows <a class="yt-timestamp" data-t="01:50:12">[01:50:12]</a>. Its ability to infer camera intrinsics (like focal length, using the Weiss field algorithm) and extrinsics directly from uncalibrated images is a major breakthrough <a class="yt-timestamp" data-t="01:06:12">[01:06:12]</a>.

## Instant Splat: Integrating Duster with 3D Gaussian Splatting

Instant Splat is a framework that unifies explicit 3D Gaussian Splatting with pose priors obtained from Duster <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. It's a two-part pipeline:

1.  **Coarse Geometric Initialization (CGI):** This first part leverages Duster to obtain globally aligned point clouds and initial camera poses from uncalibrated and unposed images <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. This replaces the traditional, more cumbersome COLMAP initialization <a class="yt-timestamp" data-t="01:09:42">[01:09:42]</a>.
2.  **Fast 3D Gaussian Optimization (F3DGO):** This second part involves optimizing the 3D Gaussian Splats. Unlike traditional Gaussian Splatting pipelines that require extensive optimization time for densification, splitting, and refining Gaussians (known as Adaptive Density Control) <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>, <a class="yt-timestamp" data-t="01:09:13">[01:09:13]</a>, Instant Splat minimizes this need <a class="yt-timestamp" data-t="01:09:47">[01:09:47]</a>.

Instant Splat jointly optimizes both 3D Gaussian attributes (position, spherical harmonic coefficients, opacity, rotation, scaling) <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a> and camera parameters <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. It uses a regularization term to prevent the optimized camera poses from deviating excessively from Duster's initial positions <a class="yt-timestamp" data-t="01:10:08">[01:10:08]</a>. This integrated approach makes the process significantly faster, completing the reconstruction in less than a minute on a consumer GPU (e.g., Nvidia A100) <a class="yt-timestamp" data-t="01:09:55">[01:09:55]</a>, <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

## Duster Demo

A live demo of Duster showcases its capabilities. Users can upload a set of photos taken with a cell phone, without providing any camera intrinsic or extrinsic information <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>. Duster processes these images in approximately 15 seconds to produce a reconstructed 3D point cloud and accurately estimate the camera positions for each input image <a class="yt-timestamp" data-t="01:49:50">[01:49:50]</a>. However, it will struggle if the underlying scene changes between photos (e.g., a robot's arm position changing), as it assumes a static scene <a class="yt-timestamp" data-t="01:04:16">[01:04:16]</a>.