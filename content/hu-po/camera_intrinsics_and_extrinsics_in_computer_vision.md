---
title: Camera Intrinsics and Extrinsics in Computer Vision
videoId: JdfrG89iPOA
---

From: [[hu-po]] <br/> 

In [[computer_vision | computer vision]], particularly in tasks like novel view synthesis, understanding and estimating camera parameters is crucial. These parameters are broadly categorized into camera intrinsics and extrinsics <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

## Camera Intrinsics

Camera intrinsics refer to information inherent to the camera itself <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This includes:
*   Focal point <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>
*   Principal point <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>
*   Lens distortion <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>

The camera's specific properties, such as a fisheye effect or a large lens, will influence its intrinsic parameters <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

## Camera Extrinsics

Camera extrinsics describe the camera's position and orientation relative to the 3D scene <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. This includes its six-dimensional rotation and pose within the scene <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

### Challenges in Obtaining Parameters

Obtaining accurate camera intrinsics and extrinsics is often a significant challenge in [[challenges_and_solutions_in_modern_computer_vision_pipelines | computer vision pipelines]] <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   **Intrinsics:** Requires detailed information about the camera, its manufacturer, specific settings, and any attached lenses, making it a "complicated mess" <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Extrinsics:** Knowing the exact position and orientation of a camera for each picture taken is "basically impossible to know from a ground truth level" in real-world scenarios <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. This typically involves guessing, which introduces errors <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

In simulated environments like Blender, exact camera intrinsics and extrinsics are known <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. However, in the real world, this information is generally unavailable <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

## Traditional Approach: Structure from Motion (SfM)

Traditional [[structure_from_motion_in_computer_vision | Structure from Motion]] (SfM) pipelines, such as COLMAP, typically:
*   Assume precise camera poses <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   Presume dense data coverage (many images) <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
*   Assume knowledge of camera intrinsics <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

COLMAP, though a pinnacle of aggregating various techniques, is often unreliable in producing camera poses and registering all input images <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>. These pipelines break down the problem into sub-problems (e.g., feature extraction, bundle adjustment), leading to accumulating errors and increased engineering complexity <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>.

## Modern Approach: Duster

Duster presents a "radically novel approach" to dense, unconstrained stereo 3D reconstruction from uncalibrated and unposed cameras <a class="yt-timestamp" data-t="00:36:19">[00:36:19]</a>. It addresses the challenges of camera intrinsics and extrinsics by:
*   **No Prior Information:** Operating without prior information about camera calibration or viewpoint poses <a class="yt-timestamp" data-t="00:32:44">[00:32:44]</a>.
*   **Pre-trained Transformers:** Leveraging [[pretraining_and_scaling_laws_for_vision_encoders | pre-trained Transformer models]] (Vision Transformers) to encode images <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. These models are trained on massive datasets of synthetic image pairs, enabling them to learn high-level semantic understanding of scenes and camera angles <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>.
*   **Joint Optimization:** Solving multiple "minimal problems" simultaneously, allowing for internal collaboration between tasks that were traditionally separated <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.
*   **Simple Regression Loss:** Training with a straightforward Euclidean distance loss in 3D space, weighted by a confidence score, without enforcing explicit geometric constraints <a class="yt-timestamp" data-t="00:56:55">[00:56:55]</a>. This contrasts with traditional methods that rely heavily on human-engineered geometric biases <a class="yt-timestamp" data-t="00:55:19">[00:55:19]</a>.
*   **Relative Poses:** Assuming the first camera's position as the origin, all other camera positions are estimated relative to it <a class="yt-timestamp" data-t="00:43:56">[00:43:56]</a>.
*   **Focal Length Estimation:** Duster calculates per-camera focal lengths using the WISE field algorithm <a class="yt-timestamp" data-t="01:06:12">[01:06:12]</a>.

Duster is notably faster than COLMAP, completing tasks in minutes compared to hours <a class="yt-timestamp" data-t="01:03:49">[01:03:49]</a>, and often achieves state-of-the-art results across various [[computer_vision | computer vision]] tasks like [[applications_and_limitations_of_monocular_depth | monocular depth estimation]], multi-view depth, and pose estimation <a class="yt-timestamp" data-t="01:01:36">[01:01:36]</a>.

## Impact on 3D Gaussian Splatting

The "Instant Splat" paper integrates Duster's capabilities directly into the [[gaussian_surfels_in_computer_vision | 3D Gaussian Splatting]] pipeline <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Initialization:** Instead of using COLMAP's sparse point clouds for initialization, Instant Splat uses the globally aligned point maps generated by Duster <a class="yt-timestamp" data-t="01:09:32">[01:09:32]</a>.
*   **Streamlined Optimization:** This approach minimizes the need for manual optimizations, such as adaptive density control (densification, splitting, and opacity reset), which were necessary in earlier 3D Gaussian Splatting methods due to the sparsity of SfM data <a class="yt-timestamp" data-t="01:09:49">[01:09:49]</a>.
*   **Concurrent Optimization:** Instant Splat jointly optimizes both the [[gaussian_surfels_in_computer_vision | 3D Gaussian attributes]] (position, color, opacity, etc.) and the camera parameters (extrinsics) <a class="yt-timestamp" data-t="01:10:01">[01:10:01]</a>. A constraint is added to prevent optimized poses from deviating too much from Duster's initial estimates <a class="yt-timestamp" data-t="01:10:08">[01:10:08]</a>. This concurrent optimization allows for better information exchange and simpler pipelines <a class="yt-timestamp" data-t="01:10:20">[01:10:20]</a>.

This integration makes the 3D Gaussian Splatting process significantly faster and more efficient, achieving scene reconstruction in less than a minute on a consumer GPU <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>, without requiring prior knowledge of camera intrinsics or extrinsics <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.