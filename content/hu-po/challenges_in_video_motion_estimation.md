---
title: Challenges in video motion estimation
videoId: A-Yawvfrivo
---

From: [[hu-po]] <br/> 

Estimating full-length motion trajectories for every pixel in a video presents several significant challenges in computer vision <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. These challenges often lead to accumulated errors and spatio-temporal inconsistencies in motion estimates <a class="yt-timestamp" data-t="01:48:47">[01:48:47]</a>.

## Key Challenges in Motion Estimation

### Temporal Limitations and Long-Range Tracking
Traditional methods, such as [[Refining traditional Optical flow methods | Optical flow]] or particle video tracking algorithms, typically operate within limited temporal windows, often just a couple of frames <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>. This short-range focus means they struggle to capture motion trajectories over long temporal windows <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. Chaining together pairwise [[Refining traditional Optical flow methods | Optical flow]] fields to extend tracking results in drift and temporal inconsistency <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. Similarly, directly computing [[Refining traditional Optical flow methods | Optical flow]] between distant frames can lead to temporal inconsistencies <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.

### Occlusions
Tracking points through occlusions is a major hurdle <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>, as many classical representations lose track of objects when they are temporarily hidden <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>. For instance, in earlier methods, a visual entity that reappears after occlusion might be treated as a different particle <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

### Maintaining Global Consistency and Coherence
Ensuring global consistency and coherence in motion estimation across an entire video is critical <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>. Prior methods often struggle to maintain coherence in space and time <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>, leading to fragmented or inconsistent motion paths.

### Computational Expense and Context Size
Video processing is inherently expensive due to the large number of frames <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. A 10-second video at 30 frames per second means 300 frames <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. It's often impossible to fit the entire video context into any algorithm run on a computer <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. This necessitates choosing either temporally or spatially constrained computations, leading to limitations in tracking <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. Modern methods still operate with limited temporal windows (e.g., eight frames are considered "wide" <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>).

### Complex Camera and Object Motion Combinations
Combining camera and object motion makes the tracking problem significantly harder <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>. Simple object-centric priors, where the camera is still and an object moves, are not useful for scenarios where the camera is also moving, or new objects enter and exit the frame <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>. Disentangling 3D scene geometry, camera pose, and scene motion is an extremely challenging problem <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>. Systems relying on known camera poses often produce erroneous motion when those poses are not perfectly accurate <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.

### Non-Rigid and Rapid Motion
Highly non-rigid motion and rapid movements pose difficulties for motion estimation <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. While the OmniMotion method penalizes large accelerations as a regularization term <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>, this approach could theoretically hinder tracking of genuinely fast-moving objects like a UFO <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

### Data Imbalance and Noisy/Incomplete Input
When using initial estimations from other methods (e.g., [[Refining traditional Optical flow methods | RAFT]]) to guide an optimization process, the resulting dataset can be imbalanced <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. Rigid background regions often have many reliable correspondences, while fast-moving and deforming foreground objects have fewer, leading to a bias where the network might focus solely on simple background motions <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>. These initial correspondences are also inherently noisy and inconsistent <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

### Non-Convex Optimization
The optimization problem involved in motion estimation is often highly non-convex <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. This means the training process can easily become trapped in sub-optimal local minima rather than reaching the global best solution <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

### Reliance on Fixed Priors
Using fixed priors, such as a fixed orthographic camera model for simplification, can be a limitation <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. Additionally, the use of "pseudo-depth" maps, which categorize foreground/background rather than actual physical depth, simplifies the problem but doesn't capture true 3D spatial relationships <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>. While this can be a clever approach, it deviates from physically accurate 3D reconstruction <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.

### Complexity and Overfitting
Methods introducing multiple loss functions with distinct weights, along with complex strategies like hard example mining, add significant engineering complexity <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. This can make re-implementation, understanding, and building upon the technique more difficult <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>. The use of specific, manually chosen thresholds for evaluation metrics also indicates a degree of hard-coding <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. The length of videos used for benchmarks (e.g., 3-4 seconds, 34-250 frames) is also very short <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>, raising concerns about scalability to longer sequences.

### Limitations of Sparse vs. Dense Tracking
Historically, motion estimation has followed two dominant approaches: sparse feature tracking and dense [[Refining traditional Optical flow methods | Optical flow]] <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. Sparse feature tracking, like SIFT features, is limited to a distinctive set of interest points (e.g., corners and edges) and struggles with featureless textures <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. Dense [[Refining traditional Optical flow methods | Optical flow]] provides more features but is generally restricted to precise motion estimation between *consecutive* frames <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. Neither fully models the motion of an entire video <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.