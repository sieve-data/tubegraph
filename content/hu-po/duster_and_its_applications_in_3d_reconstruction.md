---
title: Duster and its applications in 3D reconstruction
videoId: JdfrG89iPOA
---

From: [[hu-po]] <br/> 

Duster is a framework that provides a novel approach for dense, unconstrained, and uncalibrated 3D reconstruction from multiple views <a class="yt-timestamp" data-t="32:21:00">[32:21:00]</a>. It estimates both the 3D geometry and camera parameters (intrinsics and extrinsics) of a scene from a set of photographs, without needing prior information about camera calibration or viewpoint poses <a class="yt-timestamp" data-t="32:46:00">[32:46:00]</a>. This capability makes Duster highly significant as it subsumes nearly all other geometric 3D vision tasks <a class="yt-timestamp" data-t="33:57:00">[33:57:00]</a>.

The name "Duster" refers to the paper "Duster: Geometric 3D Vision Made Easy" <a class="yt-timestamp" data-t="32:30:00">[32:30:00]</a>. The approach is described as "radically novel" <a class="yt-timestamp" data-t="32:28:00">[32:28:00]</a> because it simultaneously solves multiple minimal problems, enabling internal collaboration between them <a class="yt-timestamp" data-t="36:33:00">[36:33:00]</a>.

## Problems with Traditional Methods

Traditional [[3d_modeling_and_tracking_using_gaussian_splatting | 3D reconstruction]] pipelines, such as Colmap's Structure-from-Motion (SfM) and Multi-View Stereo (MVS) pipelines, require initial estimations of camera intrinsics and extrinsics from dense viewpoints <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>, <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>. Obtaining these parameters is often tedious and cumbersome, or even impossible without specialized equipment like tracking domes <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.

Colmap's software tends to be unreliable in producing accurate camera poses and registering all input images <a class="yt-timestamp" data-t="24:08:00">[24:08:00]</a>. These pipelines rely on a complex chain of engineering solutions, breaking down the problem into sub-problems like feature extraction, bundle adjustment, and image registration <a class="yt-timestamp" data-t="34:28:00">[34:28:00]</a>, <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>. Each sub-problem's imperfect solution can introduce noise, leading to accumulating errors throughout the pipeline and increasing engineering effort <a class="yt-timestamp" data-t="36:05:00">[36:05:00]</a>.

## Duster's Approach and Architecture

Duster simplifies the process by integrating the solution of these sub-problems into a single, end-to-end model <a class="yt-timestamp" data-t="37:38:00">[37:38:00]</a>.

### Key Components

*   **Input**: Duster takes two views of a scene (Image 1 and Image 2) as input <a class="yt-timestamp" data-t="41:00:00">[41:00:00]</a>. It supports images taken with different orientations (vertical or horizontal) and varying lighting conditions <a class="yt-timestamp" data-t="31:48:00">[31:48:00]</a>.
*   **Siamese Vision Transformer (ViT) Encoders**: The two input images are first processed by identical, shared ViT encoders <a class="yt-timestamp" data-t="41:15:00">[41:15:00]</a>. These encoders convert the images into sequences of patches and generate token representations <a class="yt-timestamp" data-t="41:40:00">[41:40:00]</a>.
*   **Cross-Attention Decoders**: The token representations are then passed to two Transformer decoders. These decoders constantly exchange information via cross-attention, allowing information to be shared between the representations of the two input images <a class="yt-timestamp" data-t="42:24:00">[42:24:28]</a>.
*   **Regression Heads**: Finally, regression heads output two corresponding "point maps" and associated confidence maps <a class="yt-timestamp" data-t="43:20:00">[43:20:00]</a>. A point map is a one-to-one mapping between image pixels and 3D scene points, effectively an image where each pixel's value is an XYZ coordinate <a class="yt-timestamp" data-t="39:39:00">[39:39:00]</a>. Both point maps are expressed in the coordinate frame of the first input image (Image 1), which is assumed to be the origin <a class="yt-timestamp" data-t="43:55:00">[43:55:00]</a>. The confidence map indicates the reliability of each 3D point <a class="yt-timestamp" data-t="45:57:00">[45:57:00]</a>.
*   **Training Objective**: Duster is trained fully supervised using a simple regression loss based on the Euclidean distance between predicted and ground-truth 3D points <a class="yt-timestamp" data-t="56:59:00">[56:59:00]</a>. This loss is weighted by the confidence score, which encourages the network to extrapolate in harder areas <a class="yt-timestamp" data-t="58:44:00">[58:44:00]</a>. Critically, Duster does not explicitly force any geometric constraints or rely on human-curated inductive biases <a class="yt-timestamp" data-t="54:25:00">[54:25:00]</a>.

### Pre-training with KOCO

The pre-trained ViT encoders in Duster come from a work called KOCO (Cross-View Completion) <a class="yt-timestamp" data-t="48:07:00">[48:07:00]</a>. KOCO uses a self-supervised pre-training paradigm called masked image modeling, where patches in an input image are masked and then predicted by a neural network using visible patches from the same image and a reference view of the same scene from a different viewpoint <a class="yt-timestamp" data-t="48:00:00">[48:00:00]</a>. This allows the model to learn high-level semantics about objects and scenes <a class="yt-timestamp" data-t="49:16:00">[49:16:00]</a>.

KOCO was trained on approximately two million synthetic image pairs of 3D indoor scenes, derived from datasets like Scannet, Replica, ReplicaCAD, and HM3D. These images were synthetically rendered in the Habitat simulator, a simulation environment developed by Meta <a class="yt-timestamp" data-t="51:26:00">[51:26:00]</a>.

## Advantages and Performance

Duster offers several key advantages over traditional SfM/MVS pipelines:

*   **No Prior Camera Information**: Unlike Colmap, Duster does not require ground truth camera poses or intrinsics <a class="yt-timestamp" data-t="33:38:00">[33:38:00]</a>, <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>. Users can simply feed it a set of pictures from a cell phone, and it figures out the camera intrinsics and extrinsics <a class="yt-timestamp" data-t="31:26:00">[31:26:00]</a>.
*   **Simplicity and Unified Approach**: By solving multiple sub-problems simultaneously, Duster avoids the accumulating error of chained modular systems <a class="yt-timestamp" data-t="36:05:00">[36:05:00]</a>. It unifies [[high_fidelity_3d_surface_reconstruction | 3D vision tasks]] and simplifies the traditional reconstruction pipeline <a class="yt-timestamp" data-t="38:06:00">[38:06:00]</a>.
*   **Speed**: Duster is markedly faster than Colmap <a class="yt-timestamp" data-t="24:18:00">[24:18:00]</a>. For example, it can process data in 0.13 minutes compared to Colmap's 3 minutes on some datasets <a class="yt-timestamp" data-t="01:03:53">[01:03:53]</a>.
*   **State-of-the-Art Performance**: Duster achieves state-of-the-art results on monocular and multi-view depth estimation, as well as multi-view camera pose estimation benchmarks <a class="yt-timestamp" data-t="33:14:00">[33:14:00]</a>, <a class="yt-timestamp" data-t="38:15:00">[38:15:00]</a>. While it may not always outperform methods specifically trained on evaluation datasets with ground truth poses, its generalizability without such specific training is remarkable <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

A live demonstration of Duster shows it can take diverse images (e.g., vertical and horizontal shots of a robot with shadows) and produce a reasonable 3D reconstruction and camera positions within 15 seconds <a class="yt-timestamp" data-t="01:49:50">[01:49:50]</a>.

## Applications

Duster's primary application is in enabling more accessible and efficient [[high_fidelity_3d_surface_reconstruction | 3D reconstruction]]. Its ability to accurately estimate camera parameters and dense 3D points from uncalibrated images makes it highly valuable.

### Instant-Splat

One significant application is its use in the Instant-Splat pipeline. Instant-Splat is a [[3d_modeling_and_tracking_using_gaussian_splatting | 3D Gaussian Splatting]] paper that leverages Duster for the initialization of its Gaussians <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>, <a class="yt-timestamp" data-t="01:06:04">[01:06:04]</a>. This replaces the traditional Colmap initialization process, which is often slow and requires extensive optimization time for densification and refinement of Gaussians <a class="yt-timestamp" data-t="01:09:13">[01:09:13]</a>.

Instant-Splat, using Duster for initial coarse geometric initialization (dubbed "CGI" in the paper, not to be confused with computer-generated imagery), greatly streamlines the process <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. It minimizes the need for manual optimizations, omitting densification, splitting, and opacity reset processes <a class="yt-timestamp" data-t="01:09:49">[01:09:49]</a>. Instant-Splat can perform [[comparative_analysis_of_3d_representation_techniques | novel view synthesis]] in under a minute on an Nvidia A100 GPU <a class="yt-timestamp" data-t="01:01:27">[01:01:27]</a>, a significant improvement over methods like Nope-Nerf, which can take 90 minutes <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

This integration of Duster within Instant-Splat allows for the concurrent optimization of 3D Gaussian attributes and camera parameters, as the initial camera poses provided by Duster are further refined during the Gaussian optimization <a class="yt-timestamp" data-t="01:10:01">[01:10:01]</a>.