---
title: Challenges in 3D Gaussian representation
videoId: hDuy1TgD8I4
---

From: [[hu-po]] <br/> 

[[Dynamic 3D Gaussian technique | Dynamic 3D Gaussian]] representations, while powerful for modeling dynamic scenes, come with several inherent challenges and limitations.

## Data Acquisition and Calibration <a class="yt-timestamp" data-t="02:27:41">[02:27:41]</a>
A significant challenge lies in the data required for training and optimization. The current method heavily relies on highly controlled environments:
*   **Multi-camera setup:** The approach requires a multi-camera setup, such as a giant geodesic dome with perfectly calibrated cameras, rather than off-the-shelf monocular video <a class="yt-timestamp" data-t="02:21:27">[02:21:27]</a>. The cameras need to be uniformly sampled around the area of interest to provide sufficient viewpoints <a class="yt-timestamp" data-t="02:02:32">[02:02:32]</a>.
*   **Known camera parameters:** The extrinsic camera matrices (camera position in 3D space) for every single camera must be precisely known <a class="yt-timestamp" data-t="00:59:44">[00:59:44]</a>. This is difficult to replicate in real-world scenarios, like filming with an iPhone in a backyard <a class="yt-timestamp" data-t="00:59:29">[00:59:29]</a>.
*   **Background information:** The method benefits from having a background data set to differentiate foreground from background objects, which requires consistent lighting across different shots <a class="yt-timestamp" data-t="02:03:55">[02:03:55]</a>.

## Modeling Dynamic Scenes <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>
The core assumptions made about [[Introduction to Gaussian Surfels | Gaussians]] themselves introduce limitations:
*   **Fixed attributes:** The size, opacity, and color of the [[Introduction to Gaussian Surfels | Gaussians]] are fixed over time <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>. This means the model struggles with deformable objects such as smoke or water, where these attributes would naturally change <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>.
*   **Local rigidity constraints:** While essential for tracking, the local rigidity constraints assumed in the model might not be suitable for all dynamic scenes, especially those involving turbulent fluids or highly deformable materials <a class="yt-timestamp" data-t="01:28:51">[01:28:51]</a>.
*   **Inability to handle new objects:** The method can only track parts of the scene that are visible in the initial frame <a class="yt-timestamp" data-t="02:21:11">[02:21:11]</a>. It will fail to reconstruct new objects that enter the scene after initialization <a class="yt-timestamp" data-t="01:05:57">[01:05:57]</a>.
*   **Uniform color areas:** Large areas of near-uniform color pose a challenge for tracking, as [[Introduction to Gaussian Surfels | Gaussians]] can freely move within these areas without significant penalty to the reconstruction loss <a class="yt-timestamp" data-t="01:33:40">[01:33:40]</a>. This necessitates additional regularization.
*   **Conflicting losses and hyperparameters:** The use of multiple [[Optimization and adaptive density control of 3D gaussians | regularization]] losses, some of which may compete (e.g., rigid body constraints vs. isometric loss for deformable objects), can lead to the need for "magical values for hyperparameters" that are specific to certain scenes or datasets <a class="yt-timestamp" data-t="01:46:25">[01:46:25]</a>.

## Technical and Practical Considerations
*   **Memory Footprint:** Storing an explicit 3D Gaussian representation requires significantly more memory than storing the weights of a neural network in a [[Comparisons between Gaussian splats and other 3D representation technologies | Nerf]] model <a class="yt-timestamp" data-t="02:11:08">[02:11:08]</a>.
*   **Simplifications:** For simplicity, the current model turns off view-dependent color rendering using spherical harmonics <a class="yt-timestamp" data-t="01:10:41">[01:10:41]</a>. This means the color of a [[Introduction to Gaussian Surfels | Gaussian]] does not change based on the viewing angle, impacting photorealism in certain scenarios <a class="yt-timestamp" data-t="01:10:54">[01:10:54]</a>.
*   **Initial Velocity Estimation:** The method initializes by assuming constant velocity from the previous time step, which is a primitive approach and could fail in scenarios involving sudden changes in motion like collisions <a class="yt-timestamp" data-t="01:54:15">[01:54:15]</a>.
*   **Lack of Re-lighting:** While the [[Applications and future prospects of Gaussian Surfels | compositional]] nature of [[Introduction to Gaussian Surfels | Gaussians]] allows for adding objects, there is currently no lighting model for re-lighting these objects when composited into new scenes <a class="yt-timestamp" data-t="01:16:40">[01:16:40]</a>. Objects might look "out of place" due to unmatched lighting <a class="yt-timestamp" data-t="01:39:07">[01:39:07]</a>.
*   **Lack of Physics-Based Interactions:** The current [[Dynamic 3D Gaussian technique | Dynamic 3D Gaussians]] do not inherently support complex physics-based interactions like collisions between objects <a class="yt-timestamp" data-t="02:00:50">[02:00:50]</a>. While their explicit nature makes it *easier* than implicit representations like Nerfs to integrate physics, it's not a free feature <a class="yt-timestamp" data-t="02:00:50">[02:00:50]</a>.

Despite these challenges, the rapid development and impressive results of [[Dynamic 3D Gaussian technique | Dynamic 3D Gaussians]], particularly their real-time rendering capabilities <a class="yt-timestamp" data-t="02:27:29">[02:27:29]</a> and ability to provide dense 6-degree-of-freedom tracking <a class="yt-timestamp" data-t="02:26:50">[02:26:50]</a>, suggest a promising direction for future research in 3D modeling and tracking.