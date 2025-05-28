---
title: Structure from motion and computer vision
videoId: JdfrG89iPOA
---

From: [[hu-po]] <br/> 

## Introduction to Structure from Motion (SfM)

[[Structure from motion and computer vision | Structure from motion]] (SfM) is a [[Computer vision deep dive | computer vision]] task that aims for unconstrained image-based dense 3D reconstruction from multiple views <a class="yt-timestamp" data-t="00:33:37">[00:33:37]</a>. This involves estimating the 3D geometry and camera parameters of a particular scene given a set of photographs <a class="yt-timestamp" data-t="00:33:46">[00:33:46]</a>. SfM subsumes nearly all other geometric 3D [[Computer vision deep dive | vision]] tasks <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>.

A core challenge in novel view synthesis, a related task, is that it typically requires an initial estimation of camera intrinsic and extrinsics from dense viewpoints <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Camera Intrinsics** refers to information intrinsic to the camera, such as the focal point, principal point, and lens distortion <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Camera Extrinsics** refers to the position of the camera relative to the three-dimensional scene, including its six-dimensional rotation and pose <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

Obtaining these camera parameters accurately is often difficult, especially in real-world scenarios without controlled environments or ground truth data <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. This often introduces errors into the SfM pipeline <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Traditional SfM Pipelines: Colmap

Traditional SfM and Multi-View Stereo (MVS) pipelines, such as Colmap, attempt to solve the complex problem of 3D reconstruction by breaking it down into a series of minimal sub-problems <a class="yt-timestamp" data-t="00:34:18">[00:34:18]</a>, <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>.
The Colmap pipeline typically involves:
*   **Feature extraction:** Identifying distinctive points or features in images <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>.
*   [[feature matching in computer vision | Matching]] key points <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
*   Geometric verification <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a>.
*   Incremental reconstruction initialization <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.
*   Image registration <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>.
*   Triangulation <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>.
*   Outlier filtering <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.
*   Bundle adjustment <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

### Challenges with Colmap
*   **Assumptions:** Colmap assumes precise camera poses and dense data coverage, which are often unavailable in real-world applications <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
*   **Unreliability:** The software tends to be unreliable in producing camera poses and registering all input images <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>.
*   **Complexity:** The modular nature of Colmap, where each sub-problem is solved independently, means that errors from one step can accumulate and propagate to the next, increasing the complexity and engineering effort required <a class="yt-timestamp" data-t="00:35:12">[00:35:12]</a>.
*   **Tedious Pre-processing:** These traditional methods often require over 100 images as input and utilize pre-processing software like Colmap to compute camera intrinsics and extrinsics <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.

## Duster: A Radically Novel Approach

Duster (Dense Underconstrained STereo REconstruction) is a newer, "radically novel" approach for dense 3D reconstruction from uncalibrated and unposed cameras <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>, <a class="yt-timestamp" data-t="00:36:19">[00:36:19]</a>. It operates without prior information about camera calibration or viewpoint poses <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>, meaning it doesn't need to know the camera type or where pictures were taken from <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.

### Methodology
Duster's core innovation lies in simultaneously solving multiple minimal problems <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>. This enables "internal collaboration" between tasks, simplifying the traditional reconstruction pipeline and reducing accumulated errors <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>, <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.
*   **Pre-trained Transformers:** Duster leverages pre-trained Transformer models (Vision Transformers or ViT) to encode and decode images <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>, <a class="yt-timestamp" data-t="00:46:55">[00:46:55]</a>.
    *   These ViT encoders are trained using a self-supervised pre-training paradigm called KOCO (Cross-view Completion) <a class="yt-timestamp" data-t="00:47:29">[00:47:29]</a>.
    *   KOCO utilizes "masked image modeling" where patches in an input image are masked, and the model predicts the masked content using visible patches and a reference view of the same scene from a different viewpoint <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.
    *   This pre-training is performed on a massive dataset of synthetic image pairs (around two million) derived from 3D indoor scenes like ScanNet, Replica, ReplicaCAD, and HM3D, rendered in the Habitat simulator <a class="yt-timestamp" data-t="00:50:53">[00:50:53]</a>.
*   **Direct Regression:** Duster is trained fully supervised using a simple regression loss in 3D space, specifically an L1 Euclidean distance, weighted by a confidence score for each pixel <a class="yt-timestamp" data-t="00:56:57">[00:56:57]</a>.
*   **No Geometric Constraints:** The architecture never explicitly forces any geometrical constraints, allowing it to leverage strong pre-training techniques and surpass task-specific architectures <a class="yt-timestamp" data-t="00:54:25">[00:54:25]</a>.

### Performance
Duster is markedly faster than Colmap <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>, taking about 0.13 minutes compared to Colmap's 3 minutes for certain tasks <a class="yt-timestamp" data-t="01:03:53">[01:03:53]</a>. It achieves state-of-the-art results on monocular multi-view depth estimation, as well as relative pose estimation <a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>. It performs well across various [[Computer vision deep dive | computer vision]] tasks, including multi-view depth, 3D reconstruction, monocular depth, multi-view pose estimation, and visual localization <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>.

For instance, Duster can reconstruct a 3D scene and camera positions from a few cellphone pictures without any pre-existing camera information in about 15 seconds <a class="yt-timestamp" data-t="01:49:50">[01:49:50]</a>.

## Instant Splat: Integrating Duster with 3D Gaussian Splatting

Instant Splat is a framework that unifies explicit 3D Gaussian Splatting representation with pose priors obtained from Duster <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>, <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. The key innovation is using Duster for the initialization of 3D Gaussian Splats, replacing the older Colmap method <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

The Instant Splat pipeline consists of two main parts <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>:
1.  **Coarse Geometric Initialization (CGI):** This phase uses Duster to obtain an initial globally aligned point cloud and camera poses <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. Duster uses the WISE field algorithm to calculate per-camera focal length, a camera intrinsic parameter <a class="yt-timestamp" data-t="01:06:12">[01:06:12]</a>.
2.  **Fast 3D Gaussian Optimization (F3D GO):** This part optimizes the 3D Gaussian attributes and camera parameters <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a>.

By utilizing Duster's globally aligned point map for preliminary scene geometry, Instant Splat minimizes the need for manual optimizations in 3D Gaussian Splatting <a class="yt-timestamp" data-t="01:09:47">[01:09:47]</a>. This includes omitting the "adaptive density control" processes (densification, splitting, and opacity reset) that are common in other 3D Gaussian Splatting pipelines <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>, <a class="yt-timestamp" data-t="01:09:49">[01:09:49]</a>.

Instant Splat jointly optimizes both Gaussian parameters and camera extrinsics <a class="yt-timestamp" data-t="01:10:01">[01:10:01]</a>. While Duster provides good initial camera positions, Instant Splat refines these by adding a constraint that prevents the optimized poses from deviating excessively from Duster's initial estimates <a class="yt-timestamp" data-t="01:10:08">[01:10:08]</a>, <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

Instant Splat is designed to be fast, claiming to complete its process in less than one minute on an Nvidia A100 GPU <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>, <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>. This is significantly faster than traditional methods like NOP-Nerf, which can take 90 minutes for similar tasks <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.