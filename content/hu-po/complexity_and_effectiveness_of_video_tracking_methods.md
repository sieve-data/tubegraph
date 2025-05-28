---
title: Complexity and effectiveness of video tracking methods
videoId: A-Yawvfrivo
---

From: [[hu-po]] <br/> 

## Introduction to OmniMotion
A recent paper titled "Tracking Everything Everywhere All At Once" proposes a new method for estimating full-length motion trajectories for every pixel in a video frame <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This research was developed by Cornell, Google Research, and UC Berkeley <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. The paper's core idea is to perform [[pixelwise_motion_tracking_in_videos | pixel-wise tracking]] for every pixel across all frames, rather than focusing on semantic concepts or sparse features <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. While the method computes motion for all pixels, for clarity, sparse trajectories are often shown for foreground objects <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. The goal is to yield accurate, coherent, long-range motion, even for fast-moving objects, and robustly track through occlusions <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## [[challenges_in_video_motion_estimation | Challenges in Video Motion Estimation]]
Traditionally, motion estimation methods have followed two main approaches: sparse [[feature_matching_in_computer_vision | feature tracking]] and dense optical flow <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Sparse feature tracking** focuses on distinctive interest points, like corners and edges, which are easier to recognize regardless of object orientation <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. However, this correspondence is limited to these distinct points and struggles with featureless textures <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.
*   **Dense optical flow** calculates where every point in an image moves between frames <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. While precise for consecutive frames, it is not suited for long-range motion estimation due to accumulated drift and failure to handle occlusions when chained together <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>. Optical flow algorithms typically lack an understanding of objects or occlusions <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>.

The fundamental [[challenges_in_video_motion_estimation | challenges in video motion estimation]] are:
*   Maintaining accurate tracks across long sequences <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   Tracking points through occlusions <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
*   Maintaining coherence in space and time <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

Many existing methods operate within limited temporal windows (e.g., just a couple of frames or up to eight frames) due to computational expense, leading to accumulated errors and spatio-temporal inconsistencies <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Handling combined camera and object motion simultaneously also increases complexity <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## OmniMotion Approach
OmniMotion proposes a holistic approach that uses all information in a video to jointly estimate a full-length motion trajectory for every pixel <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

### Quasi-3D Canonical Volume
The method represents the scene as a canonical 3D volume (G) that is mapped to local volumes (Li) for each frame through a set of local-canonical bijections <a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>.
*   This "quasi-3D" representation is not a physically accurate [[3d_modeling_and_tracking_using_gaussian_splatting | 3D reconstruction]] of Euclidean space <a class="yt-timestamp" data-t="00:44:59">[00:44:59]</a>. Instead, its "depth" dimension represents foreground-background relationships crucial for handling occlusions <a class="yt-timestamp" data-t="01:08:42">[01:08:42]</a>.
*   It functions similarly to a Neural Radiance Field (NeRF) by mapping 3D coordinates to density (sigma) and color (C) <a class="yt-timestamp" data-t="00:48:29">[00:48:29]</a>. However, unlike a NeRF, it uses a fixed orthographic camera prior <a class="yt-timestamp" data-t="01:07:58">[01:07:58]</a> and does not explicitly disentangle camera and scene motion, which helps sidestep ambiguities inherent in dynamic [[structure_from_motion_and_computer_vision | 3D reconstruction]] <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>.

### Invertible Neural Networks for Bijections
The local-canonical bijections (Ti) are parameterized as neural networks <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>. Crucially, these are *invertible* neural networks, specifically inspired by RealNVP, which uses stacked affine coupling layers <a class="yt-timestamp" data-t="00:59:08">[00:59:08]</a>.
*   This invertibility allows for a one-to-one mapping between the canonical space (U) and the real 3D space (X) of each frame <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>.
*   All bijective mappings (Ti) share the same underlying neural network (M Theta), conditioned on a per-frame latent code that is the time index <a class="yt-timestamp" data-t="01:04:41">[01:04:41]</a>.
*   This representation ensures global cycle consistency and can track all pixels, even when occluded <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

### Test-Time Optimization
OmniMotion employs a test-time optimization approach, meaning the model is optimized for *each* video sequence <a class="yt-timestamp" data-t="01:04:43">[01:04:43]</a>.
*   The process takes a video sequence and a collection of noisy, pairwise correspondence predictions as input guidance <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.
*   These initial correspondences are computed using existing methods like RAFT or TapNet, and then filtered for cycle and appearance consistency <a class="yt-timestamp" data-t="02:25:25">[02:25:25]</a>. This makes OmniMotion more of a [[refining_traditional_optical_flow_methods | refining technique]] rather than a pure motion estimation from scratch <a class="yt-timestamp" data-t="02:17:02">[02:17:02]</a>.

### Loss Functions
The optimization minimizes a combined loss function consisting of:
1.  **Flow Loss (L_flow)**: Minimizes the Mean Absolute Error (MAE) between the predicted flow from OmniMotion's representation and the supervising input flow obtained from methods like RAFT <a class="yt-timestamp" data-t="01:29:32">[01:29:32]</a>.
2.  **Photometric Loss (L_fo)**: Minimizes the Mean Squared Error (MSE) between the predicted color and the observed color <a class="yt-timestamp" data-t="01:31:23">[01:31:23]</a>.
3.  **Regularization Term (L_Reg)**: Penalizes large accelerations to ensure temporal smoothness of the 3D motion <a class="yt-timestamp" data-t="01:32:13">[01:32:13]</a>. This prior assumes smoother motion, which might not be ideal for highly dynamic scenes <a class="yt-timestamp" data-t="02:09:41">[02:09:41]</a>.
4.  **Auxiliary Loss (L_Pgrad)**: An additional loss mentioned in the supplementary material that further minimizes color distances <a class="yt-timestamp" data-t="02:13:05">[02:13:05]</a>.
The weighting of these different losses (Lambda_Foe, Lambda_Reg) introduces hyper-parameters that need to be tuned <a class="yt-timestamp" data-t="01:28:35">[01:28:35]</a>.

### Hard Mining Strategy
To address the imbalance in initial correspondence data (e.g., more reliable points in static backgrounds than in fast-moving foreground objects), OmniMotion uses a "hard mining" strategy during training <a class="yt-timestamp" data-t="01:35:52">[01:35:52]</a>. It periodically computes error maps (Euclidean distance between predicted and input flows) and samples regions with higher error more frequently, focusing the optimization on challenging moving objects <a class="yt-timestamp" data-t="01:38:05">[01:38:05]</a>.

## Performance and Limitations

### Evaluation Benchmarks and Metrics
The method was evaluated on the TapVid Benchmark (created by DeepMind/Google, the authors' organization), Davis, Kinetics, and RGB Stacking datasets <a class="yt-timestamp" data-t="01:51:12">[01:51:12]</a>.
Key quantitative metrics used are:
*   **Position Accuracy (ΔX average)**: Measures the average positional accuracy of visible points across five thresholds (e.g., within 1, 2, 4 pixels of ground truth) <a class="yt-timestamp" data-t="01:54:20">[01:54:20]</a>.
*   **Occlusion Accuracy (AJ - Average Jacquard)**: Evaluates the accuracy of visibility and occlusion <a class="yt-timestamp" data-t="01:56:16">[01:56:16]</a>.
*   **Temporal Coherence (TC)**: Measures the L2 distance between the acceleration of ground truth and predicted tracks <a class="yt-timestamp" data-t="01:56:32">[01:56:32]</a>.

### Qualitative Results
OmniMotion demonstrates impressive qualitative results, robustly tracking through occlusions (e.g., dog passing posts, person on a swing), handling busy street scenes, and accommodating camera zooms <a class="yt-timestamp" data-t="02:00:19">[02:00:19]</a>. The pseudo-depth maps generated also show effective relative ordering between surfaces, which is critical for occlusion handling <a class="yt-timestamp" data-t="02:08:23">[02:08:23]</a>.

### Quantitative Analysis
Quantitatively, OmniMotion generally achieves state-of-the-art performance across position, occlusion, and temporal consistency metrics <a class="yt-timestamp" data-t="02:00:05">[02:00:05]</a>.
However, a closer look reveals that while it outperforms prior methods, the improvement is often marginal, especially considering it builds upon and refines the outputs of those initial methods <a class="yt-timestamp" data-t="02:04:06">[02:04:06]</a>. For instance, the improvement over RAFT can be as small as 2% in some cases <a class="yt-timestamp" data-t="02:05:13">[02:05:13]</a>.

### Computational Expense and Generalizability
*   **Computational Expense**: The method is computationally expensive, requiring 200,000 optimization iterations per video sequence <a class="yt-timestamp" data-t="01:49:46">[01:49:46]</a>. This is partly due to the large number of samples (32) taken along each ray in the quasi-3D volume <a class="yt-timestamp" data-t="01:50:14">[01:50:14]</a>.
*   **Video Length**: The current implementation is limited to relatively short videos (e.g., clips of 34-104 frames, or up to 250 frames, roughly 3-8 seconds) <a class="yt-timestamp" data-t="01:51:44">[01:51:44]</a>. The concept of a "time-independent" canonical volume suggests that capacity issues would arise with significantly longer videos, as more and more unique scene points would need to be encoded, potentially exceeding the representation's capacity <a class="yt-timestamp" data-t="01:55:50">[01:55:50]</a>.
*   **Underlying Assumptions**: The assumption of penalizing large accelerations might hinder performance for highly dynamic or non-rigid motions <a class="yt-timestamp" data-t="02:09:41">[02:09:41]</a>. The reliance on initial noisy correspondences means the method's ultimate performance is somewhat tied to the quality of its input.
*   **Optimization Complexity**: The optimization process is complex, involving multiple loss functions with tunable weights and a hard mining strategy. This intricate design can make it difficult to re-implement, understand, or adapt for other applications <a class="yt-timestamp" data-t="01:40:50">[01:40:50]</a>. The non-convex nature of the optimization problem also means training can get trapped in sub-optimal solutions <a class="yt-timestamp" data-t="02:11:11">[02:11:11]</a>.

While OmniMotion presents a novel and interesting approach to video motion estimation by leveraging a quasi-3D representation, its practical application is currently limited by its computational cost, reliance on external initialization, and complexity. Further [[developments_in_volumetric_video | developments in volumetric video]] and [[computer_vision_deep_dive | computer vision]] might address these limitations.