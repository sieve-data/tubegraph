---
title: Pixelwise motion tracking in videos
videoId: A-Yawvfrivo
---

From: [[hu-po]] <br/> 
## Pixelwise motion tracking in videos

A new method for estimating full-length motion trajectories for every pixel in a video has been developed by researchers at Cornell, Google Research, and UC Berkeley <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This approach focuses on tracking individual pixels rather than semantic concepts like objects <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. The method aims to produce accurate, coherent, and long-range motion estimates, even for fast-moving objects and through occlusions <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Traditional Approaches and Their Limitations
Historically, [[motion_modeling_in_AI | motion estimation]] methods have typically followed two dominant approaches:
*   **[[feature_matching_in_computer_vision | Sparse feature tracking]]** <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>: This involves tracking a limited set of distinctive interest points, like corners and edges, which are easy to recognize regardless of object orientation <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. While effective for establishing long-range correspondence, it doesn't model the motion of all pixels <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Dense [[Refining traditional Optical flow methods | Optical flow]]** <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>: This method estimates motion for a much higher number of features in an individual frame <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. However, it generally operates within limited temporal windows (e.g., just a couple of frames) and struggles to capture motion trajectories over long durations <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Chaining pairwise [[Refining traditional Optical flow methods | Optical flow]] often leads to drift and failure in handling occlusions <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.

[[Challenges in video motion estimation | Key challenges]] in achieving dense and long-range trajectories include:
*   Maintaining accurate tracks across long sequences <a class="yt-timestamp" data-t="01:14:15">[01:14:15]</a>.
*   Tracking points through occlusions <a class="yt-timestamp" data-t="01:14:19">[01:14:19]</a>.
*   Maintaining coherence in space and time <a class="yt-timestamp" data-t="01:14:22">[01:14:22]</a>.
Traditional methods often disregard information that is either temporally or spatially distant, leading to accumulated errors and spatio-temporal inconsistencies <a class="yt-timestamp" data-t="01:13:34">[01:13:34]</a>.

### Omnimotion: A Holistic Approach
The proposed method, dubbed Omnimotion, aims to address these challenges by providing a complete and globally consistent motion representation <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Omnimotion represents a video using a [[Omnimotion and quasi3D video representation | quasi-3D canonical volume]] (G) and performs pixel-wise tracking via bijections (one-to-one mappings) <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

#### Quasi-3D Representation
Unlike traditional 3D reconstructions, the Omnimotion system does not aim for a physically accurate 3D model <a class="yt-timestamp" data-t="00:44:59">[00:44:59]</a>. Instead, it uses a "quasi-3D" representation where the depth dimension is more akin to a foreground/background concept rather than true Euclidean depth <a class="yt-timestamp" data-t="00:41:51">[00:41:51]</a> <a class="yt-timestamp" data-t="00:46:09">[00:46:09]</a>. This relaxation of dynamic multi-view geometry allows the system to sidestep ambiguities that make traditional dynamic 3D reconstruction challenging <a class="yt-timestamp" data-t="00:45:07">[00:45:07]</a>.

The canonical volume (G) is managed by a coordinate-based neural network (F_Theta), similar to a [[Developments in Volumetric Video | Neural Radiance Field (NeRF)]], which maps 3D coordinates to density (Sigma) and color (C) <a class="yt-timestamp" data-t="00:48:46">[00:48:46]</a>. This density is crucial for determining which surfaces are present in the canonical space <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a>.

#### Bijective Mappings
Omnimotion uses local-canonical bijections (T_I), parameterized as invertible neural networks, to map 3D points from each local coordinate frame (L_I) to the canonical 3D coordinate frame (U) <a class="yt-timestamp" data-t="00:44:03">[00:44:03]</a> <a class="yt-timestamp" data-t="00:53:12">[00:53:12]</a>.
*   These bijections are "continuous" (smooth) and "bijective" (one-to-one mapping) <a class="yt-timestamp" data-t="00:53:12">[00:53:12]</a>.
*   The canonical coordinate (U) is time-independent, serving as a globally consistent index for a particular scene point <a class="yt-timestamp" data-t="00:54:43">[00:54:43]</a>.
*   The system uses the same invertible neural network for all bijections (M_Theta), but conditions it on a per-frame latent code that is derived from the time <a class="yt-timestamp" data-t="01:04:46">[01:04:46]</a> <a class="yt-timestamp" data-t="01:42:50">[01:42:50]</a>.
*   The invertible nature of these networks (using Real NVP architecture) allows for mapping a 3D point from one local frame to another via the canonical space and its inverse <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a> <a class="yt-timestamp" data-t="00:59:36">[00:59:36]</a>.

#### Pixelwise Tracking Process
To compute 2D motion for any query pixel (P_I), Omnimotion performs the following steps <a class="yt-timestamp" data-t="01:05:53">[01:05:53]</a>:
1.  **Lift to 3D**: Samples points along a ray from the query pixel in its local volume <a class="yt-timestamp" data-t="01:06:17">[01:06:17]</a>.
2.  **Map to Canonical Space**: These 3D samples are mapped to the canonical space using the bijection (T_I), and their density and color are queried from F_Theta <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.
3.  **Map to Target Frame**: The canonical points are then mapped to the target frame (J) using the inverse bijection (T_J^-1) <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>.
4.  **Render**: The mapped 3D points are aggregated using Alpha compositing (similar to [[Developments in Volumetric Video | NeRF]]), resulting in a single predicted 3D correspondence (X_hat_J) <a class="yt-timestamp" data-t="01:14:17">[01:14:17]</a>.
5.  **Project to 2D**: Finally, X_hat_J is projected back to 2D using a fixed orthographic camera model to yield the predicted 2D corresponding location (P_hat_J) <a class="yt-timestamp" data-t="01:19:40">[01:19:40]</a>. This process enables tracking through occlusions because the system retains information about all scene points and their relative depth ordering <a class="yt-timestamp" data-t="01:26:56">[01:26:56]</a>.

### Optimization Process
Omnimotion is optimized per video at test-time <a class="yt-timestamp" data-t="01:05:03">[01:05:03]</a>. It takes a video sequence and a collection of noisy correspondence predictions as input <a class="yt-timestamp" data-t="01:24:44">[01:24:44]</a>. The predictions are initially generated using existing [[Refining traditional Optical flow methods | Optical flow]] methods like RAFT <a class="yt-timestamp" data-t="01:25:25">[01:25:25]</a>.

The optimization minimizes a combined loss function <a class="yt-timestamp" data-t="01:28:28">[01:28:28]</a>:
*   **Flow Loss (L_Flow)**: Minimizes the mean absolute error (MAE) between the predicted flow from Omnimotion and the noisy input flow from RAFT/TapNet <a class="yt-timestamp" data-t="01:32:41">[01:32:41]</a>.
*   **Photometric Loss (L_Pho)**: Minimizes the mean squared error (MSE) between the predicted color and the observed color <a class="yt-timestamp" data-t="01:32:25">[01:32:25]</a>.
*   **Regularization Term (L_Reg)**: Penalizes large accelerations of the 3D motion, promoting temporal smoothness <a class="yt-timestamp" data-t="01:32:15">[01:32:15]</a>.
*   **Auxiliary Loss (L_P_Grad)**: An additional loss function found in the supplementary materials, minimizing the distance between colors <a class="yt-timestamp" data-t="02:13:05">[02:13:05]</a>.

To handle imbalanced input data (where rigid backgrounds have more reliable correspondences than fast-moving foreground objects), the method employs a "hard mining" strategy <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. It periodically computes error maps and samples regions with higher error more frequently during optimization <a class="yt-timestamp" data-t="01:38:36">[01:38:36]</a>.

### Evaluation and Results
Omnimotion was evaluated on benchmarks like TapVid (a DeepMind/Google-created benchmark) <a class="yt-timestamp" data-t="01:51:13">[01:51:13]</a>, Davis, Kinetics, and RGB-Stacking datasets <a class="yt-timestamp" data-t="01:51:41">[01:51:41]</a>. Metrics used include:
*   **Position Accuracy**: Average position accuracy of visible points across various pixel thresholds <a class="yt-timestamp" data-t="01:54:19">[01:54:19]</a>.
*   **Occlusion Accuracy (AJ/OA)**: Evaluates the accuracy of visibility and occlusion <a class="yt-timestamp" data-t="01:56:16">[01:56:16]</a>.
*   **Temporal Coherence (TC)**: Measures the L2 distance between the acceleration of ground truth and predicted tracks <a class="yt-timestamp" data-t="01:56:32">[01:56:32]</a>.

Qualitative results demonstrate impressive tracking through occlusions and handling of camera zoom <a class="yt-timestamp" data-t="02:01:41">[02:01:41]</a>. Quantitatively, Omnimotion generally achieves the best performance across these metrics <a class="yt-timestamp" data-t="02:00:08">[02:00:08]</a>. However, improvements over the initial (RAFT/TapNet) results are sometimes marginal, suggesting that Omnimotion acts more as a refining technique <a class="yt-timestamp" data-t="02:04:06">[02:04:06]</a>.

Ablation studies confirmed the importance of the invertible mapping networks (Real NVP), showing that models without invertibility performed significantly worse <a class="yt-timestamp" data-t="02:06:27">[02:06:27]</a>. The photometric loss and hard mining also contribute to performance, though their impact varies <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a> <a class="yt-timestamp" data-t="02:07:34">[02:07:34]</a>.

### [[Complexity and effectiveness of video tracking methods | Limitations]] and Future Work
Despite its strengths, Omnimotion has several limitations:
*   **Rapid and Non-rigid Motion**: The method struggles with rapid and highly non-rigid motion, potentially due to the acceleration regularization term <a class="yt-timestamp" data-t="02:09:41">[02:09:41]</a>.
*   **Dependency on Initialization**: It relies on an initial set of noisy correspondence predictions, making it more of a refinement process <a class="yt-timestamp" data-t="02:16:40">[02:16:40]</a>.
*   **Computational Expense**: The per-video test-time optimization is computationally expensive <a class="yt-timestamp" data-t="02:11:32">[02:11:32]</a>.
*   **[[Challenges in video motion estimation | Non-convex Optimization]]**: The highly non-convex nature of the optimization problem can lead to solutions trapped in local minima <a class="yt-timestamp" data-t="02:09:57">[02:09:57]</a>.
*   **Video Length**: The canonical 3D space has a finite capacity, which could become a bottleneck for very long videos with continuously changing scenes or objects <a class="yt-timestamp" data-t="01:53:37">[01:53:37]</a>.

Future work could explore more efficient alternatives to exhaustive matching to improve scalability <a class="yt-timestamp" data-t="02:11:46">[02:11:46]</a>.