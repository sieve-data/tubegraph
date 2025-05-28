---
title: Dynamic and unbounded scenes in NeRFs
videoId: Y73KU0ShHdM
---

From: [[hu-po]] <br/> 

[[nerf_acceleration_with_python_and_nerfacc_toolkit | NerfAcc]] is a recently released toolkit for accelerating [[volumetric_rendering_and_neural_radiance_fields | Neural Radiance Fields]] (NeRFs), developed by the University of California Berkeley. This toolkit aims to extend NeRF techniques to support not only bounded static scenes but also [[dynamic_scene_handling_in_robotics | dynamic scenes]] and unbounded scenes, offering a user-friendly [[python_nerf_libraries | Python]] API for plug-and-play acceleration for most NeRFs <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Understanding Neural Radiance Fields (NeRFs)
[[volumetric_rendering_and_neural_radiance_fields | Neural Radiance Fields]] are a popular type of rendering that may replace current rendering stacks in the future <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. They are used for 3D representation and involve training a neural network, typically a Multi-Layer Perceptron (MLP), to encode the view-dependent appearance of a scene <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The network takes a view vector (direction) and a position as input, and returns pixel values (color and opacity) <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

The key aspect of NeRFs is their [[neural_volume_rendering | volumetric rendering]] algorithm, which uses ray marching. This process is differentiable, allowing NeRFs to be trained with backpropagation and neural networks <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### Traditional NeRF Limitations
Vanilla NeRF models typically require around two days to converge on a single scene, highlighting a significant limitation in training time <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Additionally, older voxel-based radiance fields are less flexible as they apply to only a single static scene <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

## Extending NeRFs with NerfAcc

### Unbounded Scenes
Traditional NeRFs are often limited to "bounded scenes," where the object being rendered is confined within a specific 3D volume <a class="yt-timestamp" data-t="00:25:18">[00:25:18]</a>. An unbounded scene, such as a backyard or a wide landscape, has a large background that extends to infinity, making it impossible to constrain the entire view to a specific volume <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>.

[[nerf_acceleration_with_python_and_nerfacc_toolkit | NerfAcc]] incorporates the scene contraction idea from MIP-NeRF 360 to support unbounded scenes <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>. This involves applying a nonlinear function to coordinates to map the unbounded space into a finite grid <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.

### [[dynamic_scene_handling_in_robotics | Dynamic Scenes]]
For [[dynamic_scene_handling_in_robotics | dynamic scenes]], where the scene itself is moving or changing over time (e.g., bouncing balls or moving synthetic people), an additional dimension of "time" is added to the neural network's input <a class="yt-timestamp" data-t="00:47:45">[00:47:45]</a>. This allows the NeRF model to learn the changes in the scene over time. The occupancy grid for dynamic scenes is shared by all frames and stores the maximum opacity at an area over all timestamps <a class="yt-timestamp" data-t="00:46:17">[00:46:17]</a>.

## Acceleration Techniques

### Ray Marching Optimizations
Efficient ray marching is crucial for NeRF performance. This process involves casting a ray through the scene and generating discrete samples along the ray <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. Since the Radiance Field evaluation is often the main bottleneck, efficiency is achieved by reducing the number of samples as much as possible <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

[[nerf_acceleration_with_python_and_nerfacc_toolkit | NerfAcc]] optimizes this by:
*   **Skipping Empty or Occluded Space**: Samples that have either low opacity (empty space) or low transmittance (occluded by something closer to the camera) contribute little to the final image and can be skipped <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. This significantly reduces computational load; for instance, in a Lego scene, 98% of samples can be ignored <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
*   **Occupancy Grid**: A binary grid is cached and updated to store which areas of the scene are empty <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>. A threshold (opacity < 1e-2) is used to identify empty space, and marching is terminated if transmittance falls below a threshold (1e-4) <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. Gradients are disabled during this process to minimize computation <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.
*   **Coarse-to-Fine Sampling**: Instead of uniformly sampling many points, an initial coarse sampling identifies areas of high opacity, and then denser sampling is performed only in those relevant regions around object surfaces <a class="yt-timestamp" data-t="00:42:22">[00:42:22]</a>.

### Differentiable Rendering
Differentiable rendering is the process of accumulating the color of samples along the rays into pixel colors <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>. The differentiability of this process allows for gradient descent optimization, minimizing errors between observed and rendered images <a class="yt-timestamp" data-t="00:38:38">[00:38:38]</a>. Beyond just RGB and opacity, NeRFs can predict arbitrary properties like specularity or roughness, potentially leading to physics-based properties for simulations in the future <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>.

### [[optimizing_gpu_usage_in_nerf_training | GPU Optimization]]
[[optimizing_gpu_usage_in_nerf_training | Optimizing GPU usage]] in NeRFs involves clever management of tensor dimensions. [[nerf_acceleration_with_python_and_nerfacc_toolkit | NerfAcc]] minimizes operations parallelized across rays and instead parallelizes across samples <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. This is because sample opacity and density are independent of the rays, allowing for efficient parallelization on a single GPU <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.

## Performance Benchmarks
[[nerf_acceleration_with_python_and_nerfacc_toolkit | NerfAcc]] significantly reduces training time. While a vanilla NeRF can take two days to converge on a single scene <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, [[nerf_acceleration_with_python_and_nerfacc_toolkit | NerfAcc]] allows training a D-NeRF model for [[dynamic_scene_handling_in_robotics | dynamic scenes]] in just one hour <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>, compared to two days <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. For static scenes, it can train models like Instant NGP in minutes <a class="yt-timestamp" data-t="00:41:20">[00:41:20]</a>. Although the PSNR (Peak Signal-to-Noise Ratio, a quality metric) might be similar to original methods, the substantial reduction in training time is the key advantage <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. Training memory footprint is also manageable, around 10-11 gigabytes, fitting comfortably on high-end GPUs like an Nvidia Titan (24 GB) or even a 3090 (16 GB) <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>.

## Implementation Details
[[nerf_acceleration_with_python_and_nerfacc_toolkit | NerfAcc]] provides a [[python_nerf_libraries | Python]] API, integrating with PyTorch <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. It requires defining two main functions: `Sigma FN` (for density) and `RGB Sigma FN` (for color and density) <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>. These functions take ray origins, directions, sample intervals (start/end), and ray indices as input <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>. The `Sigma FN` queries the neural network for density based on position, while `RGB Sigma FN` queries for color and density, also conditioning on the view angle <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>.

The toolkit is designed for easy integration with existing NeRF models. Standard datasets like the NeRF Synthetic Dataset (e.g., the Lego truck scene) and D-NeRF Synthetic Dataset (for [[dynamic_scene_handling_in_robotics | dynamic scenes]]) are used for testing and examples <a class="yt-timestamp" data-t="01:00:40">[01:00:40]</a>. Training typically uses an Adam optimizer with a learning rate scheduler <a class="yt-timestamp" data-t="02:00:40">[02:00:40]</a>.

**Example Code Snippet:**
```python
import nerfacc

# Example functions for density and color queries
def sigma_fn(t_starts, t_ends, ray_indices, ray_origins, ray_directions, radiance_field):
    # Calculate positions along the ray
    positions = ray_origins[ray_indices] + ray_directions[ray_indices] * ((t_starts + t_ends) / 2)
    # Query density from the radiance field
    sigmas = radiance_field.query_density(positions)
    return sigmas

def rgb_sigma_fn(t_starts, t_ends, ray_indices, ray_origins, ray_directions, radiance_field):
    # Calculate positions along the ray
    positions = ray_origins[ray_indices] + ray_directions[ray_indices] * ((t_starts + t_ends) / 2)
    # Query color and density from the radiance field, conditioned on view direction
    rgbs, sigmas = radiance_field.query_rgb_sigma(positions, ray_directions[ray_indices])
    return rgbs, sigmas

# Ray marching and rendering process
# samples, packed_info = nerfacc.ray_marching(
#     ray_origins, ray_directions, sigma_fn,
#     near_plane=0.2, far_plane=1.0,
#     early_stop_eps=1e-4, alpha_thre=1e-2
# )
# colors, opacities = nerfacc.render_visibility(
#     samples, packed_info, rgb_sigma_fn
# )
```