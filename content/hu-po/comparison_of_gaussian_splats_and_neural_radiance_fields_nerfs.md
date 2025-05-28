---
title: Comparison of Gaussian Splats and Neural Radiance Fields NeRFs
videoId: xgwvU7S0K-k
---

From: [[hu-po]] <br/> 

[[3D Gaussian Splats for Radiance Field Rendering | 3D Gaussian Splatting]] and [[Neural volume rendering and Radiance Fields | Neural Radiance Fields (NeRFs)]] are both cutting-edge techniques in computer vision aimed at generating novel views of 3D scenes from a collection of 2D images or videos <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. While their goal is similar, they employ fundamentally different approaches to represent and render 3D scenes.

## Neural Radiance Fields (NeRFs)

[[Neural volume rendering and Radiance Fields | NeRFs]] represent a 3D scene as a continuous radiance field <a class="yt-timestamp" data-t="00:55:51">[00:55:51]</a>. This field is encoded by a neural network, typically a Multi-Layer Perceptron (MLP), which learns the color and opacity for any given point in 3D space <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>.

### Key Aspects of NeRFs:
*   **Scene Representation**: A continuous density field that implicitly represents empty and occupied space <a class="yt-timestamp" data-t="00:48:43">[00:48:43]</a>.
*   **Rendering**: Utilizes volumetric ray marching <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. For each pixel in a desired novel view, rays are cast through the scene, and numerous points along these rays are sampled to query the MLP for color and opacity <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>. This process can be computationally intensive, especially for high-resolution images <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
*   **Training**: Requires training a separate neural network for every individual scene or object <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Changes to lighting or object positions necessitate retraining <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Training times can be very long; for example, a basic NeRF could take 48 hours <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Limitations**:
    *   **Costly**: High computational cost for both training and rendering <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
    *   **Real-time Challenges**: Cannot achieve real-time display rates at 1080p resolution <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
    *   **Artifacts**: Can struggle to represent empty space effectively and produce blurring or "misty" effects <a class="yt-timestamp" data-t="00:39:36">[00:39:36]</a>, <a class="yt-timestamp" data-t="02:00:05">[02:00:05]</a>.
    *   **Explicit Camera Positions**: Requires precise camera positions for each input photo or video, usually obtained via Structure from Motion (SFM) <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.
*   **Memory Footprint**: Relatively small because only the weights of the neural network are stored (e.g., 8-13 MB for instant NGP) <a class="yt-timestamp" data-t="02:03:21">[02:03:21]</a>.

## [[3D Gaussian Splats for Radiance Field Rendering | 3D Gaussian Splatting]]

[[3D Gaussian Splats for Radiance Field Rendering | 3D Gaussian Splatting]] proposes a different, more explicit scene representation that aims to be faster and better than [[Neural volume rendering and Radiance Fields | NeRFs]] <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Key Aspects of Gaussian Splats:
*   **Scene Representation**: An unstructured set of 3D gaussians <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Each gaussian is defined by:
    *   A 3D position (mean) <a class="yt-timestamp" data-t="00:59:44">[00:59:44]</a>.
    *   An anisotropic covariance matrix, representing its 3D spread and orientation <a class="yt-timestamp" data-t="00:59:49">[00:59:49]</a>. This allows for complex shapes and fine structures to be modeled compactly <a class="yt-timestamp" data-t="01:00:40">[01:00:40]</a>, <a class="yt-timestamp" data-t="02:19:51">[02:19:51]</a>.
    *   An opacity (alpha) <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>.
    *   Spherical harmonic coefficients for view-dependent color <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>, <a class="yt-timestamp" data-t="02:26:27">[02:26:27]</a>.
*   **Initialization**: Starts from sparse point clouds, similar to NeRFs, produced by Structure from Motion (SFM) during camera calibration <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>, <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>.
*   **Optimization**: Involves interleaved optimization and adaptive density control of the 3D gaussians <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. This process dynamically adds ("clones" or "splits") and removes ("prunes") gaussians based on factors like transparency and positional gradients, adapting their number and density to better represent the scene <a class="yt-timestamp" data-t="01:21:28">[01:21:28]</a>, <a class="yt-timestamp" data-t="01:31:55">[01:31:55]</a>.
*   **Rendering**: Employs a fast, differentiable, tile-based rasterizer for [[3D Gaussian splatting and Nerfs | splatting]] <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>, <a class="yt-timestamp" data-t="01:39:58">[01:39:58]</a>. This involves:
    *   Dividing the screen into 16x16 tiles <a class="yt-timestamp" data-t="01:41:05">[01:41:05]</a>.
    *   Culling gaussians that don't intersect the view frustum <a class="yt-timestamp" data-t="01:42:12">[01:42:12]</a>.
    *   Sorting remaining gaussians based on view space depth and tile ID using a fast GPU Radix sort <a class="yt-timestamp" data-t="01:43:18">[01:43:18]</a>.
    *   Performing alpha blending in parallel for each tile, accumulating colors and alpha values until saturation <a class="yt-timestamp" data-t="01:46:11">[01:46:11]</a>, <a class="yt-timestamp" data-t="01:47:01">[01:47:01]</a>.
*   **Advantages**:
    *   **Speed**: Achieves significantly faster training times (e.g., 35-45 minutes compared to NeRF's 48 hours) and real-time rendering <a class="yt-timestamp" data-t="02:10:48">[02:10:48]</a>.
    *   **Quality**: Delivers state-of-the-art visual quality, surpassing NeRFs in rendering fine details and avoiding blurriness <a class="yt-timestamp" data-t="02:00:05">[02:00:05]</a>, <a class="yt-timestamp" data-t="02:11:08">[02:11:08]</a>.
    *   **Flexibility**: The explicit representation allows for creation, destruction, and displacement of geometry during optimization <a class="yt-timestamp" data-t="01:22:37">[01:22:37]</a>.
*   **Limitations**:
    *   **Memory Footprint**: Significantly higher memory consumption compared to NeRFs. A single scene can require hundreds of megabytes (e.g., 734 MB) to store all the gaussians <a class="yt-timestamp" data-t="02:03:03">[02:03:03]</a>, <a class="yt-timestamp" data-t="02:13:16">[02:13:16]</a>. Training large scenes can exceed 20 GB of GPU memory <a class="yt-timestamp" data-t="02:23:43">[02:23:43]</a>.
    *   **Optimization Complexity**: The optimization process involves several hard-coded hyperparameters and sequential steps (e.g., starting optimization at lower resolutions, gradually introducing spherical harmonic bands) <a class="yt-timestamp" data-t="02:06:24">[02:06:24]</a>, <a class="yt-timestamp" data-t="02:10:04">[02:10:04]</a>, <a class="yt-timestamp" data-t="02:13:11">[02:13:11]</a>.
    *   **Artifacts**: Can still produce artifacts in unobserved regions or exhibit "popping" artifacts due to sudden changes in gaussian visibility or blending order <a class="yt-timestamp" data-t="02:20:54">[02:20:54]</a>.

## Comparison Summary

| Feature              | [[Neural volume rendering and Radiance Fields | Neural Radiance Fields (NeRFs)]]                                         | [[3D Gaussian Splats for Radiance Field Rendering | 3D Gaussian Splatting]]                                            |
| :------------------- | :----------------------------------------------------------------------- | :----------------------------------------------------------- |
| **Scene Representation** | Implicit, continuous radiance field (neural network weights) <a class="yt-timestamp" data-t="00:55:51">[00:55:51]</a> | Explicit, discrete set of 3D gaussians <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a> |
| **Rendering Algorithm**  | Volumetric Ray Marching <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>                                                 | Tile-based Rasterization with GPU Radix Sort <a class="yt-timestamp" data-t="01:43:18">[01:43:18]</a>   |
| **Training Time**    | Very slow (e.g., 48 hours for a basic NeRF) <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>                     | Significantly faster (e.g., 35-45 minutes) <a class="yt-timestamp" data-t="02:10:48">[02:10:48]</a>    |
| **Rendering Speed**  | Not real-time at 1080p <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>                                            | Real-time <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>                     |
| **Visual Quality**   | Good, but can have blurring/misty artifacts <a class="yt-timestamp" data-t="02:00:05">[02:00:05]</a>                  | State-of-the-art, clearer fine details <a class="yt-timestamp" data-t="02:00:05">[02:00:05]</a>       |
| **Memory Usage**     | Low (e.g., 8-13 MB) <a class="yt-timestamp" data-t="02:03:21">[02:03:21]</a>                                                | High (e.g., 734 MB, up to 20 GB GPU memory) <a class="yt-timestamp" data-t="02:13:16">[02:13:16]</a>, <a class="yt-timestamp" data-t="02:23:43">[02:23:43]</a> |
| **Geometry**         | Continuous, inferred <a class="yt-timestamp" data-t="00:48:43">[00:48:43]</a>                                           | Discrete (gaussians), explicit <a class="yt-timestamp" data-t="00:49:25">[00:49:25]</a>                       |
| **Initial Input**    | Calibrated camera positions via SFM <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>                                 | Sparse point clouds from SFM <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>                        |

Despite its higher memory consumption, [[3D Gaussian Splats for Radiance Field Rendering | 3D Gaussian Splatting]] presents a compelling alternative to [[Neural volume rendering and Radiance Fields | NeRFs]], offering superior visual quality and real-time performance that could potentially transform [[3D content generation using gaussian splatting | 3D content generation]] and [[Physicsbased Modeling in Gaussian Splats | rendering]] in applications like virtual reality or [[Gaussian Splats in Robotics | robotics]].