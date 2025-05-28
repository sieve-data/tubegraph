---
title: Volumetric rendering and neural Radiance fields
videoId: Y73KU0ShHdM
---

From: [[hu-po]] <br/> 

[[Neural volume rendering | Volumetric rendering]] and [[neural_radiance_fields | Neural Radiance Fields (NeRFs)]] represent a cutting-edge approach to 3D scene representation and rendering. This technique has the potential to replace many current rendering stacks in the future <a class="yt-timestamp" data-t="02:20:20">[02:20:20]</a>.

## Neural Radiance Fields (NeRFs)

[[Neural radiance fields | NeRFs]] are a method for 3D representation that trains a neural network, specifically a Multi-Layer Perceptron (MLP), to encode the view-dependent appearance of a scene <a class="yt-timestamp" data-t="02:50:50">[02:50:50]</a>. Given a view vector (the direction from which the scene is to be rendered), the neural network returns pixel values for that view <a class="yt-timestamp" data-t="03:11:11">[03:11:11]</a>.

A key characteristic of [[neural_radiance_fields | NeRFs]] is their use of a differentiable [[ray_marching_and_differentiable_rendering | volumetric rendering]] algorithm, known as [[ray_marching_and_differentiable_rendering | ray marching]] <a class="yt-timestamp" data-t="03:38:38">[03:38:38]</a>. This differentiability allows the network to be trained using backpropagation <a class="yt-timestamp" data-t="03:43:43">[03:43:43]</a>.

### Limitations of Vanilla NeRF

The original implementation of [[neural_radiance_fields | NeRF]] typically requires about two days to converge on a single scene, which is a significant limitation <a class="yt-timestamp" data-t="03:51:51">[03:51:51]</a> <a class="yt-timestamp" data-t="03:55:55">[03:55:55]</a>. While Nvidia has developed methods to reduce training and rendering times, these often involve specialized CUDA code that is not generalizable to non-Nvidia GPUs or CPUs <a class="yt-timestamp" data-t="09:09:09">[09:09:09]</a> <a class="yt-timestamp" data-t="09:23:23">[09:23:23]</a> <a class="yt-timestamp" data-t="09:33:33">[09:33:33]</a>.

## Nerfack: A General NeRF Acceleration Toolkit

Nerfack (Nerf Acceleration Toolkit) is a recently released paper and toolkit from the University of California Berkeley, designed to accelerate various [[neural_radiance_fields | NeRFs]] across different applications <a class="yt-timestamp" data-t="01:33:33">[01:33:33]</a> <a class="yt-timestamp" data-t="01:47:47">[01:47:47]</a> <a class="yt-timestamp" data-t="04:57:57">[04:57:57]</a>. It provides a user-friendly Python API that is ready for Plug and Play acceleration for most NeRF models <a class="yt-timestamp" data-t="02:33:33">[02:33:33]</a> <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>.

Nerfack extends [[neural_radiance_fields | NeRF]] techniques to support not only bounded static scenes but also dynamic and unbounded scenes <a class="yt-timestamp" data-t="02:25:25">[02:25:25]</a> <a class="yt-timestamp" data-t="02:29:29">[02:29:29]</a>. It significantly reduces training time; for instance, a D-NeRF model for [[dynamic_3d_gaussian_technique | dynamic scenes]] can be trained in one hour rather than two days <a class="yt-timestamp" data-t="13:05:05">[13:05:05]</a> <a class="yt-timestamp" data-t="13:10:10">[13:10:10]</a>. It claims to achieve better quality with less training time <a class="yt-timestamp" data-t="13:18:18">[13:18:18]</a> <a class="yt-timestamp" data-t="13:20:20">[13:20:20]</a>.

## Volumetric Rendering Pipeline

The volumetric rendering pipeline in [[neural_radiance_fields | NeRFs]] is broken down into two main steps: [[ray_marching_and_differentiable_rendering | Ray marching]] and [[ray_marching_and_differentiable_rendering | Differentiable rendering]] <a class="yt-timestamp" data-t="13:31:31">[13:31:31]</a>.

### Ray Marching

[[Ray marching and differentiable rendering | Ray marching]] is the process of casting a ray through the scene and generating discrete samples along that ray <a class="yt-timestamp" data-t="13:41:41">[13:41:41]</a> <a class="yt-timestamp" data-t="13:43:43">[13:43:43]</a>. These samples are later evaluated by the radiance field <a class="yt-timestamp" data-t="13:34:34">[13:34:34]</a>.

#### Optimization through Sample Reduction
Efficiency in [[ray_marching_and_differentiable_rendering | ray marching]] can be achieved by reducing the number of samples as much as possible <a class="yt-timestamp" data-t="13:38:38">[13:38:38]</a> <a class="yt-timestamp" data-t="13:40:40">[13:40:40]</a>. Samples that have low opacity or low transmittance contribute little to the final image and can be safely skipped <a class="yt-timestamp" data-t="14:47:47">[14:47:47]</a> <a class="yt-timestamp" data-t="14:49:49">[14:49:49]</a> <a class="yt-timestamp" data-t="14:58:58">[14:58:58]</a>. This prevents wasting inference time on empty or occluded regions <a class="yt-timestamp" data-t="15:45:45">[15:45:45]</a> <a class="yt-timestamp" data-t="15:49:49">[15:49:49]</a>. For a dense scene like a Lego truck, 98% of samples can be ignored <a class="yt-timestamp" data-t="20:58:58">[20:58:58]</a> <a class="yt-timestamp" data-t="21:00:00">[21:00:00]</a> <a class="yt-timestamp" data-t="21:08:08">[21:08:08]</a>.

Nerfack uses an [[occupancy_grid | occupancy grid]]—a binary grid that is cached and updated to store which areas of the scene are empty <a class="yt-timestamp" data-t="18:18:18">[18:18:18]</a> <a class="yt-timestamp" data-t="19:17:17">[19:17:17]</a>. If transmittance falls below a certain threshold (e.g., 1e-4) or opacity is too low (e.g., 1e-2), ray marching for that segment can be terminated <a class="yt-timestamp" data-t="19:34:34">[19:34:34]</a> <a class="yt-timestamp" data-t="36:43:43">[36:43:43]</a>.

#### Coarse-to-Fine Sampling
Instead of uniformly sampling points along a ray, a "coarse-to-fine" approach involves first sampling a small number of points to identify regions of high opacity, and then densely sampling around those regions (e.g., the surface of an object) <a class="yt-timestamp" data-t="42:22:22">[42:22:22]</a> <a class="yt-timestamp" data-t="42:42:42">[42:42:42]</a> <a class="yt-timestamp" data-t="43:05:05">[43:05:05]</a>.

### Differentiable Rendering

[[Ray marching and differentiable rendering | Differentiable rendering]] is the process of accumulating the color and opacity of the samples along the rays into pixel colors <a class="yt-timestamp" data-t="26:31:31">[26:31:31]</a>. For each point along a ray, the neural network samples the color (RGB) and the alpha (see-throughness/opacity) <a class="yt-timestamp" data-t="07:12:12">[07:12:12]</a> <a class="yt-timestamp" data-t="07:22:22">[07:22:22]</a>. These values are then combined (summed up based on their opacity and transmittance) to determine the final pixel color <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a> <a class="yt-timestamp" data-t="08:10:10">[08:10:10]</a> <a class="yt-timestamp" data-t="16:57:57">[16:57:57]</a>.

The differentiability of this function allows for gradient descent training to minimize errors between observed and rendered images <a class="yt-timestamp" data-t="08:38:38">[08:38:38]</a> <a class="yt-timestamp" data-t="38:12:12">[38:12:12]</a>.

#### Beyond Color and Opacity
[[Neural radiance fields | NeRFs]] are not limited to predicting only color and opacity. The neural network can be extended to predict an arbitrary number of properties, such as specularity, roughness, or even future physics-based properties like hardness or elasticity <a class="yt-timestamp" data-t="27:35:35">[27:35:35]</a> <a class="yt-timestamp" data-t="27:50:50">[27:50:50]</a> <a class="yt-timestamp" data-t="28:04:04">[28:04:04]</a>.

## Nerfack Technical Details and Features

### Optimization Strategies
Nerfack uses clever mapping to optimize GPU utilization. Since the number of valid samples can be much larger than the number of rays, Nerfack hypothesizes and implements parallelization across samples to get the best performance <a class="yt-timestamp" data-t="24:04:04">[24:04:04]</a> <a class="yt-timestamp" data-t="24:11:11">[24:11:11]</a> <a class="yt-timestamp" data-t="24:31:31">[24:31:31]</a> <a class="yt-timestamp" data-t="24:43:43">[24:43:43]</a>.

### Scene Types

*   **Bounded Scenes:** The entire scene to be rendered is an object confined within a specific 3D volume <a class="yt-timestamp" data-t="25:18:18">[25:18:18]</a> <a class="yt-timestamp" data-t="25:21:21">[25:21:21]</a>.
*   **Unbounded Scenes:** Scenes that extend to "infinity," like a backyard, where points can be very far from the camera and cannot be constrained to a specific volume <a class="yt-timestamp" data-t="25:52:52">[25:52:52]</a> <a class="yt-timestamp" data-t="26:01:01">[26:01:01]</a>. Nerfack incorporates the scene contraction idea from MIP-NeRF 360, applying a nonlinear function to map unbounded space into a finite grid <a class="yt-timestamp" data-t="25:10:10">[25:10:10]</a> <a class="yt-timestamp" data-t="25:12:12">[25:12:12]</a> <a class="yt-timestamp" data-t="26:21:21">[26:21:21]</a>.
*   **Dynamic Scenes:** Scenes where objects move over time, requiring an additional time dimension variable for the neural network <a class="yt-timestamp" data-t="46:58:58">[46:58:58]</a> <a class="yt-timestamp" data-t="47:15:15">[47:15:15]</a> <a class="yt-timestamp" data-t="47:48:48">[47:48:48]</a>. For [[dynamic_3d_gaussian_technique | dynamic scenes]], the [[occupancy_grid | occupancy grid]] is shared across all frames, storing the maximum opacity of an area over all timestamps <a class="yt-timestamp" data-t="46:17:17">[46:17:17]</a> <a class="yt-timestamp" data-t="46:23:23">[46:23:23]</a>.

### Core Functions

Nerfack requires users to define two key functions: `Sigma FN` and `RGB Sigma FN`.

*   **`Sigma FN`**: Given the start and end of a sample interval along a ray, and specific ray indices, this function queries the radiance field for the density (opacity) at those positions <a class="yt-timestamp" data-t="30:50:50">[30:50:50]</a> <a class="yt-timestamp" data-t="32:28:28">[32:28:28]</a> <a class="yt-timestamp" data-t="32:56:56">[32:56:56]</a>. Density primarily depends on the XYZ position, not the view angle <a class="yt-timestamp" data-t="34:19:19">[34:19:19]</a> <a class="yt-timestamp" data-t="34:36:36">[34:36:36]</a>.
*   **`RGB Sigma FN`**: Similar to `Sigma FN`, but it also queries the radiance field for the RGB color at the given positions. For color prediction, the network needs to be conditioned on the direction (view angle) of the ray, as the apparent color can change based on the viewing angle due to view-dependent effects <a class="yt-timestamp" data-t="33:27:27">[33:27:27]</a> <a class="yt-timestamp" data-t="34:06:06">[34:06:06]</a> <a class="yt-timestamp" data-t="34:51:51">[34:51:51]</a>.

### Performance Metrics

The quality of reconstructed images in [[neural_radiance_fields | NeRFs]] is often measured using PSNR (Peak Signal-to-Noise Ratio), which quantifies reconstruction quality for images and videos subject to lossy compression <a class="yt-timestamp" data-t="11:42:42">[11:42:42]</a> <a class="yt-timestamp" data-t="12:03:03">[12:03:03]</a>.

## Comparison to Other Techniques

### Voxel-based Radiance Fields
[[Neural radiance fields | NeRFs]] that are voxel-based are generally less flexible than MLP-based ones, as they typically apply only to a single static scene <a class="yt-timestamp" data-t="04:35:35">[04:35:35]</a> <a class="yt-timestamp" data-t="04:37:37">[04:37:37]</a> <a class="yt-timestamp" data-t="05:51:51">[05:51:51]</a>. Voxels involve breaking up a 3D space into smaller volumetric squares <a class="yt-timestamp" data-t="04:43:43">[04:43:43]</a> <a class="yt-timestamp" data-t="04:54:54">[04:54:54]</a>. Alternatives like Octrees offer variable resolution voxels, allowing more detail in areas with information <a class="yt-timestamp" data-t="05:07:07">[05:07:07]</a> <a class="yt-timestamp" data-t="05:18:18">[05:18:18]</a>.

### Instant NGP
The [[3d_gaussian_splatting_for_realtime_radiance_field_rendering | Instant NGP]] paper, often referenced for its speed improvements in [[comparison_of_3d_gaussian_splatting_to_neural_radiance_fields | radiance field rendering]], uses the alpha channel in images to apply random background augmentation. This data augmentation technique helps regularize the training and improves the overall NeRF quality <a class="yt-timestamp" data-t="44:15:15">[44:15:15]</a> <a class="yt-timestamp" data-t="44:18:18">[44:18:18]</a> <a class="yt-timestamp" data-t="45:05:05">[45:05:05]</a> <a class="yt-timestamp" data-t="45:20:20">[45:20:20]</a> <a class="yt-timestamp" data-t="45:27:27">[45:27:27]</a>.

### Deep Learning Frameworks
Nerfack is built using PyTorch <a class="yt-timestamp" data-t="09:57:57">[09:57:57]</a>. PyTorch has seen a significant increase in popularity, surpassing TensorFlow since around 2020 <a class="yt-timestamp" data-t="10:40:40">[10:40:40]</a> <a class="yt-timestamp" data-t="10:46:46">[10:46:46]</a> <a class="yt-timestamp" data-t="10:53:53">[10:53:53]</a>. Frameworks like JAX also aim to optimize GPU usage through features like `pmap` (parallel mapping), which compiles and executes functions in parallel across devices <a class="yt-timestamp" data-t="22:34:34">[22:34:34]</a> <a class="yt-timestamp" data-t="23:29:29">[23:29:29]</a> <a class="yt-timestamp" data-t="23:43:43">[23:43:43]</a>.