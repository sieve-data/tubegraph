---
title: Refining traditional Optical flow methods
videoId: A-Yawvfrivo
---

From: [[hu-po]] <br/> 

Traditional [[pixelwise_motion_tracking_in_videos | optical flow]] methods, along with other approaches to [[complexity_and_effectiveness_of_video_tracking_methods | motion estimation]], have historically faced challenges in accurately tracking movement across video sequences <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. These methods primarily fall into two categories: sparse feature tracking and dense [[pixelwise_motion_tracking_in_videos | optical flow]] <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. While both have proven effective in certain contexts, they often fail to provide a complete and globally consistent representation of motion, especially over long durations or in complex scenes <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

## Challenges with Traditional Optical Flow

Traditional [[pixelwise_motion_tracking_in_videos | optical flow]] and particle video tracking algorithms struggle with several key issues:
*   **Limited Temporal Windows** They typically operate within short temporal windows, often just a few frames, making it difficult to capture motion trajectories over long sequences <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>, <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   **Occlusions** They find it difficult to track points through [[complexity_and_effectiveness_of_video_tracking_methods | occlusions]], where objects temporarily disappear from view <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>, <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>.
*   **Global Consistency** Maintaining global consistency across the entire video sequence is a significant hurdle, leading to accumulated errors over long trajectories <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.
*   **Complexity of Motion** Handling videos with combinations of camera and object motion simultaneously is considerably harder than scenarios where only one is moving <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Computational Constraints** Processing the entire context of a video (e.g., hundreds of frames) is computationally very expensive, forcing algorithms to rely on limited temporal or spatial information <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>, <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.

### OmniMotion: A Refinement Approach

The OmniMotion method proposes a holistic approach to [[challenges_in_video_motion_estimation | video motion estimation]] that uses all information in a video to jointly estimate [[pixelwise_motion_tracking_in_videos | full-length motion trajectories]] for every pixel <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
Key aspects of OmniMotion's approach include:
*   **Quasi-3D Canonical Volume** OmniMotion represents a video using a "quasi-3D" canonical volume, which is a 3D but not physically accurate representation <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>, <a class="yt-timestamp" data-t="00:45:03">[00:45:03]</a>. This volume serves as a globally consistent index for scene points <a class="yt-timestamp" data-t="00:44:45">[00:44:45]</a>.
*   **Local Canonical Bijections** It performs [[pixelwise_motion_tracking_in_videos | pixel-wise tracking]] via bijections (one-to-one mappings) between each frame's local volume and the canonical volume <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>, <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. These bijections are parameterized as invertible neural networks, allowing for mapping from local to canonical space and vice-versa <a class="yt-timestamp" data-t="00:44:12">[00:44:12]</a>, <a class="yt-timestamp" data-t="01:09:54">[01:09:54]</a>.
*   **Occlusion Handling** The representation retains information about all scene points, including their relative "depth" ordering (foreground/background distinction), enabling points to be tracked even when temporarily occluded <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>, <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   **Test-Time Optimization** OmniMotion uses a test-time optimization method, meaning it performs optimization at inference time for each video sequence <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>, <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. This allows for querying any continuous coordinate in the video to receive a motion trajectory spanning the entire video <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>, <a class="yt-timestamp" data-t="00:40:33">[00:40:33]</a>.

## Optimization Process

The optimization process in OmniMotion takes a video sequence and a collection of noisy correspondence predictions (guidance) as input <a class="yt-timestamp" data-t="01:24:42">[01:24:42]</a>. It then refines these initial predictions to generate a complete and globally consistent motion estimate <a class="yt-timestamp" data-t="01:24:50">[01:24:50]</a>.

1.  **Input Correspondences**: OmniMotion leverages existing [[pixelwise_motion_tracking_in_videos | optical flow]] algorithms like RAFT or TapNet to compute initial pairwise [[complexity_and_effectiveness_of_video_tracking_methods | correspondences]] <a class="yt-timestamp" data-t="01:25:25">[01:25:25]</a>. These are then filtered for spurious correspondences using cycle consistency and appearance consistency <a class="yt-timestamp" data-t="01:27:15">[01:27:15]</a>.
2.  **Loss Functions**: The overall optimization minimizes a weighted sum of three primary loss functions <a class="yt-timestamp" data-t="01:28:28">[01:28:28]</a>:
    *   **Flow Loss ($L_{flow}$)**: Minimizes the mean absolute error between the predicted flow (from OmniMotion) and the supervising input flow (from RAFT/TapNet) <a class="yt-timestamp" data-t="01:29:32">[01:29:32]</a>.
    *   **Photometric Loss ($L_{pho}$)**: Minimizes the mean squared error between the predicted color and the observed color <a class="yt-timestamp" data-t="01:31:24">[01:31:24]</a>. This ensures visual consistency.
    *   **Regularization Term ($L_{reg}$)**: Penalizes large accelerations to ensure temporal smoothness of the 3D motion estimated by the invertible mapping network <a class="yt-timestamp" data-t="01:31:56">[01:31:56]</a>.
3.  **Hard Mining**: To address the imbalance in initial correspondence data (where rigid backgrounds have more reliable points than fast-moving or deforming foreground objects), OmniMotion employs a hard mining strategy <a class="yt-timestamp" data-t="01:36:47">[01:36:47]</a>. This involves periodically computing error maps and sampling regions with higher errors more frequently during optimization <a class="yt-timestamp" data-t="01:38:32">[01:38:32]</a>.

## Nuances and Criticisms

While OmniMotion presents impressive qualitative results, several aspects invite discussion:
*   **Reliance on Pseudo-Labels**: The method's initialization relies on pre-computed (and often noisy) correspondences from other [[pixelwise_motion_tracking_in_videos | optical flow]] algorithms, meaning it functions more as a refining technique rather than a standalone motion estimation solution <a class="yt-timestamp" data-t="02:03:55">[02:03:55]</a>, <a class="yt-timestamp" data-t="02:16:54">[02:16:54]</a>.
*   **Complexity**: The optimization process involves multiple loss functions with tunable weights and a hard mining strategy, adding considerable engineering complexity and potential for difficulty in re-implementation <a class="yt-timestamp" data-t="01:40:50">[01:40:50]</a>, <a class="yt-timestamp" data-t="02:17:08">[02:17:08]</a>.
*   **Computational Expense**: It is noted as computationally expensive, requiring per-video optimization <a class="yt-timestamp" data-t="01:46:42">[01:46:42]</a>.
*   **"Quasi-3D" Limitation**: The time-independent nature of the canonical volume and its "pseudo-depth" (foreground/background rather than physical depth) might limit its applicability to very long or highly dynamic videos with significant scene changes <a class="yt-timestamp" data-t="01:53:37">[01:53:37]</a>, <a class="yt-timestamp" data-t="02:08:52">[02:08:52]</a>.
*   **Metric Bias**: The inclusion of an acceleration regularization term in the loss functions may artificially boost performance on metrics related to temporal coherence <a class="yt-timestamp" data-t="01:56:56">[01:56:56]</a>, <a class="yt-timestamp" data-t="01:57:09">[01:57:09]</a>.

## Comparison to Other Methods

OmniMotion's quantitative performance, while state-of-the-art on the chosen benchmark (TapVid, which is noted as somewhat obscure <a class="yt-timestamp" data-t="01:51:12">[01:51:12]</a>), shows that the most significant gains in accuracy are often attributed to the strong performance of the initial [[pixelwise_motion_tracking_in_videos | optical flow]] methods (like RAFT) it builds upon <a class="yt-timestamp" data-t="02:04:41">[02:04:41]</a>. The refinement typically adds a modest percentage improvement, suggesting its primary role is to enhance existing, strong baselines <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.

This approach sits among other efforts in [[video_diffusion_models_in_generative_3d | generative 3D]] and [[structure_from_motion_and_computer_vision | structure from motion]], which often contend with similar challenges of global consistency and occlusion handling. Unlike some methods that focus on [[developments_in_volumetric_video | volumetric video]] or direct 3D reconstruction, OmniMotion's relaxation of strict physical 3D constraints allows it to overcome some ambiguities inherent in [[challenges_in_video_motion_estimation | dynamic 3D reconstruction]] <a class="yt-timestamp" data-t="00:45:03">[00:45:03]</a>.