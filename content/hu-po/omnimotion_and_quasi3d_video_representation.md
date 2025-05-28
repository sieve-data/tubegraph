---
title: Omnimotion and quasi3D video representation
videoId: A-Yawvfrivo
---

From: [[hu-po]] <br/> 

Omnimotion is a novel method for estimating full-length motion trajectories for every pixel in a video frame <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Developed by Cornell, [[stateoftheart_video_generation_and_multimodal_models | Google Research]], and UC Berkeley, it aims to achieve accurate, coherent, and long-range motion tracking, even when objects are occluded <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Challenges in Traditional Motion Tracking

Historically, motion estimation methods have relied on two dominant approaches: sparse feature tracking and dense [[structure_from_motion_and_computer_vision | Optical Flow]] <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

*   **Sparse Feature Tracking** focuses on distinctive interest points (e.g., corners and edges) <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>, limiting tracking to a subset of the scene and struggling with featureless textures <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.
*   **Dense Optical Flow** calculates motion vectors for every point in an image <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. However, it typically operates within limited temporal windows (e.g., a couple of frames) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. Chaining these pairwise flows over longer sequences leads to drift and fails to handle occlusions effectively <a class="yt-timestamp" data-t="00:23:56">[00:23:56]</a>. Current [[stateoftheart_video_generation_and_multimodal_models | video generation and multimodal models]] techniques face significant computational constraints, making it difficult to process an entire video's context <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

The key challenges remaining in dense, long-range trajectory estimation include:
*   Maintaining accurate tracks across long sequences <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   Tracking points through occlusions <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.
*   Maintaining coherence in space and time <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

## Omnimotion's Innovative Approach

Omnimotion proposes a holistic method that utilizes all information within a video to jointly estimate full-length motion trajectories for every pixel <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

### Quasi-3D Video Representation

A core element of Omnimotion is its novel quasi-3D canonical volume, denoted as 'G' <a class="yt-timestamp" data-t="00:43:55">[00:43:55]</a>.
*   This volume is mapped to per-frame local volumes ('Li') through a set of local-canonical bijections ('Ti') <a class="yt-timestamp" data-t="00:43:59">[00:43:59]</a>. A bijection ensures a one-to-one mapping where every point in one space corresponds uniquely to a point in another <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   The bijections ('Ti') are parameterized as [[optimization_techniques_and_challenges_for_3d_scene_representation | invertible neural networks]] <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>. Specifically, they use a "Real NVP" (Real-valued Non-Volume Preserving) architecture, which consists of stacked affine transformations that are inherently invertible <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>, <a class="yt-timestamp" data-t="01:10:32">[01:10:32]</a>.
*   The canonical coordinate 'U' is designed to be time-independent, acting as a globally consistent index for a particular scene point throughout the entire video <a class="yt-timestamp" data-t="00:44:43">[00:44:43]</a>.
*   Crucially, Omnimotion's quasi-3D representation is *not* a physically accurate 3D reconstruction <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>. It relaxes the rigid constraints of dynamic multi-view geometry, focusing instead on relative depth ordering (e.g., foreground/background) rather than precise XYZ coordinates <a class="yt-timestamp" data-t="01:17:22">[01:17:22]</a>. This can be conceptualized as a "2.5D prior" <a class="yt-timestamp" data-t="01:47:45">[01:47:45]</a>.

### Tracking Mechanism

The process for computing 2D motion for any query pixel (Pi) involves:
1.  **Lifting to 3D:** The query pixel is lifted to a "3D" ray within the quasi-3D space <a class="yt-timestamp" data-t="01:06:17">[01:06:17]</a>.
2.  **Sampling along Ray:** Points are sampled along this ray (e.g., 32 samples per ray) <a class="yt-timestamp" data-t="01:50:14">[01:50:14]</a>.
3.  **Mapping to Canonical Space:** Each sampled point (x_i_k) is mapped to the canonical space (U) using the invertible neural network (M_theta), conditioned on a per-frame latent code derived from time <a class="yt-timestamp" data-t="01:43:09">[01:43:09]</a>, <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.
4.  **Density and Color Query:** A separate neural network (F_theta), similar to a [[3d_scene_representation_and_simulation | Nerf]] model, queries the canonical space at point 'U' to obtain its density (sigma) and color (C) <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>, <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.
5.  **Mapping to Target Frame:** The point is then mapped to a target frame (J) using the inverse of the bijective mapping <a class="yt-timestamp" data-t="01:13:54">[01:13:54]</a>.
6.  **Alpha Compositing:** All samples along the ray are aggregated using alpha compositing (similar to [[3d_scene_representation_and_simulation | Nerf]] rendering) to produce a single 2D correspondence in the target frame (P_hat_J) <a class="yt-timestamp" data-t="01:15:18">[01:15:18]</a>.
7.  **Occlusion Handling:** The representation inherently handles occlusions by retaining information about all scene points projected onto each pixel, along with their relative depth ordering <a class="yt-timestamp" data-t="01:17:52">[01:17:52]</a>.

### Per-Video Optimization

Omnimotion employs a "test-time optimization" approach, meaning the model is optimized *per video* <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
*   **Initialization:** It takes a collection of frames and *noisy correspondence predictions* (pseudo-labels) as guidance <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. This initialization is typically obtained from existing optical flow algorithms like RAFT or TAP-Net <a class="yt-timestamp" data-t="01:24:42">[01:24:42]</a>. The paper acknowledges this as a "refining process" rather than starting from scratch <a class="yt-timestamp" data-t="02:16:57">[02:16:57]</a>.
*   **Loss Functions:** The optimization process minimizes a combination of losses:
    *   **Flow Loss (L_flow):** Mean Absolute Error (MAE) between the predicted flow and the supervised input flow <a class="yt-timestamp" data-t="01:28:44">[01:28:44]</a>.
    *   **Photometric Loss (L_photometric):** Mean Squared Error (MSE) between the predicted color and the observed color <a class="yt-timestamp" data-t="01:31:23">[01:31:23]</a>.
    *   **Regularization Term (L_reg):** Penalizes large accelerations to ensure temporal smoothness of the 3D motion <a class="yt-timestamp" data-t="01:32:13">[01:32:13]</a>.
    *   An additional auxiliary gradient loss (L_P_grad) is also used <a class="yt-timestamp" data-t="02:13:05">[02:13:05]</a>.
*   **Hard Mining:** To address imbalances in the initial correspondence data (where rigid backgrounds have more reliable points than fast-moving foreground objects), Omnimotion employs a "hard mining" strategy. This involves periodically computing error maps and sampling more frequently from regions with higher prediction errors <a class="yt-timestamp" data-t="01:38:05">[01:38:05]</a>.

### Implementation Details

*   **Network Architecture:**
    *   The mapping network (M_theta) comprises six affine coupling layers <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. It uses positional encoding with four frequencies for pixel coordinates <a class="yt-timestamp" data-t="01:41:36">[01:41:36]</a>. A small 2-layer MLP generates a 128-dimensional latent code for each frame, which conditions the mapping network <a class="yt-timestamp" data-t="01:43:09">[01:43:09]</a>.
    *   The canonical representation network (F_theta) is a 3-layer MLP <a class="yt-timestamp" data-t="01:43:40">[01:43:40]</a>.
    *   Both MLPs are implemented using a GaborNet architecture, where filters in the first layer are constrained to fit Gabor functions <a class="yt-timestamp" data-t="01:45:07">[01:45:07]</a>.
*   **Training:** Each video sequence is trained for 200,000 iterations using the Adam optimizer <a class="yt-timestamp" data-t="01:49:46">[01:49:46]</a>. A batch consists of 256 pairs of correspondences sampled from eight pairs of images <a class="yt-timestamp" data-t="01:50:11">[01:50:11]</a>.
*   **Camera Model:** A fixed orthographic camera is assumed, as camera motion is subsumed by the local-canonical bijections <a class="yt-timestamp" data-t="01:07:54">[01:07:54]</a>.

## Results and Evaluation

Omnimotion demonstrates strong qualitative results, showcasing impressive tracking through complex scenarios, including occlusions (e.g., a person passing behind posts) and camera zoom <a class="yt-timestamp" data-t="02:00:21">[02:00:21]</a>.

Quantitatively, the method is evaluated on benchmarks like TAP-Vid (which includes both real-world and synthetic videos) <a class="yt-timestamp" data-t="01:51:13">[01:51:13]</a>. It measures:
*   **Position accuracy:** Average position accuracy of visible points across five thresholds (e.g., within 1, 2, 4, 8, 16 pixels) <a class="yt-timestamp" data-t="01:54:12">[01:54:12]</a>.
*   **Occlusion accuracy (AJ):** Evaluates the correctness of visible/occluded predictions <a class="yt-timestamp" data-t="01:55:49">[01:55:49]</a>.
*   **Temporal consistency (TC):** Measures the L2 distance between the acceleration of ground truth and predicted tracks <a class="yt-timestamp" data-t="01:56:32">[01:56:32]</a>.

Omnimotion achieves [[stateoftheart_video_generation_and_multimodal_models | state-of-the-art]] performance on these metrics, outperforming prior methods like RAFT, PIPS, and FlowWalk <a class="yt-timestamp" data-t="02:03:07">[02:03:07]</a>. However, the quantitative improvements over existing initialization methods (like RAFT) are often marginal, suggesting that Omnimotion acts more as a refinement tool <a class="yt-timestamp" data-t="02:04:35">[02:04:35]</a>.

### Ablation Studies
*   **No Invertible:** Replacing the invertible mapping network with separate forward and backward networks severely degrades tracking performance, highlighting the importance of the invertible property <a class="yt-timestamp" data-t="02:06:27">[02:06:27]</a>.
*   **No Photometric:** Removing the photometric loss does not significantly impact results <a class="yt-timestamp" data-t="02:06:58">[02:06:58]</a>.
*   **Uniform Sampling:** Using uniform sampling instead of hard mining also has minimal impact <a class="yt-timestamp" data-t="02:07:34">[02:07:34]</a>.

## Limitations and Conclusion

While innovative, Omnimotion has several limitations:
*   **Computational Expense:** It is computationally intensive, requiring per-video optimization and initial pairwise flow computations <a class="yt-timestamp" data-t="02:11:31">[02:11:31]</a>.
*   **Non-Rigid Motion:** The method struggles with rapid and highly non-rigid motion, potentially due to the acceleration regularization term <a class="yt-timestamp" data-t="02:09:39">[02:09:39]</a>.
*   **Optimization Complexity:** The optimization problem is highly non-convex, meaning the training process can get trapped in sub-optimal solutions <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   **Reliance on Initialization:** Its performance is dependent on the quality of the initial noisy correspondence predictions <a class="yt-timestamp" data-t="02:16:16">[02:16:16]</a>.
*   **Video Length:** The use of a single canonical space to represent the entire video limits its scalability to very long videos, as the capacity may be exhausted <a class="yt-timestamp" data-t="01:53:56">[01:53:56]</a>.

Despite these complexities and its role as a refinement technique, Omnimotion presents a unique approach to dense, long-range motion estimation through its quasi-3D representation and invertible neural network mappings. Its qualitative results are very impressive, demonstrating effective tracking through occlusions and varying camera dynamics <a class="yt-timestamp" data-t="02:17:51">[02:17:51]</a>. The concept of a "2.5D Nerf" where depth represents foreground/background rather than physical distance is particularly noteworthy and could inspire future work in [[3d_scene_representation_and_simulation | generative 3D]] and [[video_diffusion_models_in_generative_3d | video diffusion models]] <a class="yt-timestamp" data-t="01:17:47">[01:17:47]</a>, <a class="yt-timestamp" data-t="02:18:41">[02:18:41]</a>.