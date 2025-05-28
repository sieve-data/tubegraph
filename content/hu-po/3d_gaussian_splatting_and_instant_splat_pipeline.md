---
title: 3D Gaussian Splatting and Instant Splat Pipeline
videoId: JdfrG89iPOA
---

From: [[hu-po]] <br/> 

[[3d_gaussian_splatting_for_realtime_radiance_field_rendering | 3D Gaussian Splatting]] is a cutting-edge [[gaussian_splatting_and_its_advantages | 3D representation technology]] that defines a scene as a collection of small, 3D Gaussian "bubbles" or ellipses [00:07:54](<a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Each Gaussian splat has properties like its 3D position (center), a covariance matrix defining its shape (rotation and scaling), spherical harmonic coefficients for [[implications_of_gaussian_splatting_in_future_technologies | view-dependent color]], and an opacity value [00:28:16](<a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>. The *Instant Splat* pipeline leverages [[goshan_splat_optimization_for_3d_reconstruction | 3D Gaussian Splatting]] to achieve fast and accurate novel view synthesis, capable of generating new images from unseen angles of a 3D scene [00:04:52](<a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, [00:05:06](<a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Challenges in Novel View Synthesis

Traditionally, novel view synthesis requires an initial estimation of camera parameters, including intrinsic (internal camera properties like focal point, principal point, lens distortion) and extrinsic (camera position and orientation in the 3D scene) information [00:05:24](<a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>, [00:05:28](<a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. Obtaining these parameters can be tedious and cumbersome, especially in real-world scenarios where [[camera intrinsics and extrinsics]] are often unknown [00:06:13](<a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>, [00:06:35](<a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

Older *Structure from Motion (SFM)* pipelines, such as Colmap, often require:
*   Precise camera poses and dense data coverage [00:14:10](<a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
*   Knowledge of camera intrinsics [00:14:22](<a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.
*   Over 100 input images [00:23:31](<a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.
*   A complex, multi-stage process involving feature extraction, matching, geometric verification, triangulation, and bundle adjustment [00:18:16](<a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. Each sub-problem in this chain can introduce noise that accumulates through the pipeline [00:35:15](<a class="yt-timestamp" data-t="00:35:15">[00:35:15]</a>. Colmap, in particular, tends to be unreliable in producing camera poses and registering all input images [01:06:07](<a class="yt-timestamp" data-t="01:06:07">[01:06:07]</a>, [00:24:08](<a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>.

## Instant Splat Pipeline

Instant Splat is designed as a two-part pipeline to rapidly create 3D scenes from multi-view images:
1.  **Course Geometric Initialization (CGI)**: This initial step focuses on generating a globally aligned point cloud and estimating camera parameters [01:09:09](<a class="yt-timestamp" data-t="01:09:09">[01:09:09]</a>. Instant Splat utilizes Duster for this, departing from traditional methods like Colmap [00:04:21](<a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
2.  **Fast 3D Gaussian Optimization (F3DGO)**: The second phase involves optimizing the 3D Gaussian splats and concurrently refining the camera parameters [00:15:05](<a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

The entire process can be completed in less than one minute on an Nvidia A100 GPU [00:28:28](<a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>, [01:07:50](<a class="yt-timestamp" data-t="01:07:50">[01:07:50]</a>. This represents a significant speed improvement over other techniques like Nope-NeRF, which can take 90 minutes [01:12:00](<a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

### Duster: Unconstrained 3D Vision

Duster is a novel approach for dense, unconstrained 3D reconstruction from uncalibrated and unposed cameras [00:32:27](<a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>, [00:32:44](<a class="yt-timestamp" data-t="00:32:44">[00:32:44]</a>. Unlike Colmap, Duster does not require prior information about camera calibration or viewpoint positions [00:32:46](<a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>. It simplifies the traditional reconstruction pipeline by solving multiple minimal problems simultaneously, allowing for internal collaboration between tasks [00:36:31](<a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.

#### How Duster Works
*   **Point Map**: Duster introduces the concept of a "point map," which is a one-to-one mapping between image pixels and 3D scene points. It can be thought of as an image where each pixel stores its XYZ coordinates in 3D space [00:39:41](<a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>.
*   **Architecture**: Duster's architecture uses two identical branches, each with a Vision Transformer (ViT) encoder and a Transformer decoder. The encoders share weights, and the decoders constantly exchange information via cross-attention [00:41:15](<a class="yt-timestamp" data-t="00:41:15">[00:41:15]</a>, [00:42:24](<a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>. The regression heads output corresponding point maps and associated confidence maps [00:44:52](<a class="yt-timestamp" data-t="00:44:52">[00:44:52]</a>.
    *   **Confidence Maps**: These maps indicate the reliability of each predicted 3D point, allowing the system to weigh points with lower confidence less heavily during training [00:45:17](<a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>.
*   **Pre-training (KOCO)**: The power of Duster comes from its reliance on pre-trained Transformers, specifically from the KOCO (Cross-View Completion) work [00:47:25](<a class="yt-timestamp" data-t="00:47:25">[00:47:25]</a>.
    *   KOCO uses a self-supervised pre-training paradigm called Masked Image Modeling, where patches in an input image are masked and then predicted by a neural network using visible patches and a "reference view" of the same scene from a different viewpoint [00:48:00](<a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>, [00:48:46](<a class="yt-timestamp" data-t="00:48:46">[00:48:46]</a>.
    *   This pre-training is performed on synthetic image pairs (around 2 million) derived from 3D indoor scenes from datasets like ScanNet, Replica, ReplicaCAD, and HM3D, all rendered within the Habitat simulator [00:51:26](<a class="yt-timestamp" data-t="00:51:26">[00:51:26]</a>.
*   **Training Objective**: Duster uses a simple regression loss based on Euclidean distance in 3D space, weighted by the confidence map [00:56:59](<a class="yt-timestamp" data-t="00:56:59">[00:56:59]</a>. Crucially, it does not enforce any geometric constraints, allowing it to surpass what existing task-specific architectures can achieve [00:54:55](<a class="yt-timestamp" data-t="00:54:55">[00:54:55]</a>.
*   **Performance**: Duster achieves state-of-the-art results on monocular (single camera) multi-view depth estimation and relative pose estimation [00:33:14](<a class="yt-timestamp" data-t="00:33:14">[00:33:14]</a>, and significantly outperforms Colmap in speed [01:03:49](<a class="yt-timestamp" data-t="01:03:49">[01:03:49]</a>.

<div class="callout">
<div class="callout-title">
<div class="callout-icon">
<svg viewBox="0 0 24 24" width="24" height="24">
<path fill="currentColor" d="M12,1L3,5V11C3,16.55 6.84,21.74 12,23C17.16,21.74 21,16.55 21,11V5L12,1Z"></path>
</svg>
</div>
The "Bitter Lesson" and Duster</div>
<div class="callout-content">
Duster exemplifies Rich Sutton's "bitter lesson" in deep learning: instead of relying on human-engineered geometric constraints and inductive biases that can lead to overly complicated and less effective pipelines, Duster leverages large datasets and generic architectures (Transformers) to learn the underlying structure directly [00:55:02](<a class="yt-timestamp" data-t="00:55:02">[00:55:02]</a>, [00:56:02](<a class="yt-timestamp" data-t="00:56:02">[00:56:02]</a>. This results in a simpler, faster, and often more robust solution.
</div>
</div>

### Instant Splat's Gaussian Optimization

With the high-quality point maps and estimated camera poses from [[open_source_implementation_of_gosh_and_splats | Duster]], Instant Splat initializes its [[goshan_splat_optimization_for_3d_reconstruction | 3D Gaussian Splats]]. This robust initialization minimizes the need for cumbersome manual optimizations common in other [[3d_gaussian_splatting_for_realtime_radiance_field_rendering | 3D Gaussian Splatting]] pipelines, such as adaptive density control (densification, splitting, and opacity resetting) [01:09:49](<a class="yt-timestamp" data-t="01:09:49">[01:09:49]</a>.

Instant Splat jointly optimizes both the Gaussian attributes (position, shape, color, opacity) and the camera extrinsic parameters (poses) [01:10:01](<a class="yt-timestamp" data-t="01:10:01">[01:10:01]</a>. A constraint is introduced to prevent the optimized camera poses from deviating excessively from Duster's initial positions, balancing refinement with the initial good guess [01:10:08](<a class="yt-timestamp" data-t="01:10:08">[01:10:08]</a>, [01:11:16](<a class="yt-timestamp" data-t="01:11:16">[01:11:16]</a>. The rendering process for [[3d_gaussian_splatting_for_realtime_radiance_field_rendering | Gaussian Splats]] is fully differentiable, allowing gradients from reconstruction loss (comparing rendered images to ground truth) to be propagated back to optimize both the Gaussian parameters and the camera poses [01:11:41](<a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a>, [01:12:05](<a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a>.

## Comparisons to Other 3D Representation Technologies

### NeRFs versus Gaussian Splatting

A key distinction between [[nerfs_versus_gaussian_splatting | NeRFs]] (Neural Radiance Fields) and [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] lies in their representation:
*   **[[nerfs_versus_gaussian_splatting | NeRFs]]**: Implicit 3D representations, where the scene is encoded within the weights of a small neural network (multi-layer perceptron). This makes them very compact for storage and efficient for transmission [01:17:31](<a class="yt-timestamp" data-t="01:17:31">[01:17:31]</a>, [01:35:16](<a class="yt-timestamp" data-t="01:35:16">[01:35:16]</a>. [[comparison_of_3d_gaussian_splatting_to_neural_radiance_fields | NeRFs]] are also better at modeling amorphous or translucent objects like smoke [01:35:36](<a class="yt-timestamp" data-t="01:35:36">[01:35:36]</a>. However, they require known camera intrinsics and extrinsics for training [01:19:19](<a class="yt-timestamp" data-t="01:19:19">[01:19:19]</a>.
*   **[[gaussian_splatting_and_its_advantages | Gaussian Splatting]]**: Explicit 3D representations, meaning the 3D object is directly defined by a set of Gaussian points [01:17:17](<a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>. While the file sizes can be larger, their explicit nature makes them easier to compose, manipulate, and render quickly [01:36:20](<a class="yt-timestamp" data-t="01:36:20">[01:36:20]</a>.

Some research, like *RadSplats*, explores combining these two approaches by using a [[nerfs_versus_gaussian_splatting | NeRF]] to initialize and supervise the [[goshan_splat_optimization_for_3d_reconstruction | Gaussian Splatting]] process [01:18:04](<a class="yt-timestamp" data-t="01:18:04">[01:18:04]</a>.

## Performance and Evaluation

Instant Splat demonstrates superior rendering quality and pose estimation accuracy compared to existing methodologies [01:25:55](<a class="yt-timestamp" data-t="01:25:55">[01:25:55]</a>. It is evaluated on datasets such as Tanks and Temples and MVImgNet, using metrics like Absolute Trajectory Error (ATE), Relative Pose Error (RPE), Peak Signal-to-Noise Ratio (PSNR), Structural Similarity Index Measure (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS) [01:21:00](<a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>, [01:20:45](<a class="yt-timestamp" data-t="01:20:45">[01:20:45]</a>. While quantitative metrics can be abstract, qualitative results often show significant improvements in geometry and clarity [01:23:04](<a class="yt-timestamp" data-t="01:23:04">[01:23:04]</a>.