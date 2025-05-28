---
title: Ray marching and differentiable rendering
videoId: Y73KU0ShHdM
---

From: [[hu-po]] <br/> 

[[Volumetric rendering and neural Radiance fields | Neural Radiance Fields]] (NeRFs) are a prominent type of [[Volumetric rendering and neural Radiance fields | volumetric rendering]] that uses [[Differentiable rendering and optimization | differentiable rendering]] and may eventually replace current rendering stacks [02:20:00]. This technique is used for [[canonical 3D volume representation | 3D representation]] and involves training a neural network, specifically a Multi-Layer Perceptron (MLP), to encode the view-dependent appearance of a scene [02:50:00].

## What is Ray Marching?
[[Ray marching and differentiable rendering | Ray marching]] is the [[Volumetric rendering and neural Radiance fields | volumetric rendering]] algorithm at the core of NeRFs [03:38:00]. It involves casting a ray into a 3D space and generating discrete samples along that ray [06:12:00].

### Process
1.  **Input**: The neural network receives the position of a camera (`Ray Origins`) and the direction (`Ray Directions`) from which a scene is to be rendered [03:14:00, 06:46:00, 06:49:00].
2.  **Ray Tracing**: A ray is traced through the 3D space [07:12:00].
3.  **Sampling**: At each point along the ray, the neural network is sampled to determine the color and "alpha" (see-throughness or opacity) at that specific point [07:14:00, 07:22:00].
4.  **Accumulation**: The colors and opacities from all sampled points along the ray are added up to determine the final pixel color for that ray [07:27:00, 08:00:00]. This process of accumulating colors along the ray is called [[Differentiable rendering and optimization | differentiable rendering]] [06:15:00, 06:33:00].

## Differentiable Rendering and Training
The [[Volumetric rendering and neural Radiance fields | volumetric rendering]] algorithm, specifically [[Ray marching and differentiable rendering | ray marching]], is [[Differentiable rendering and optimization | differentiable]] [03:43:00]. This differentiability allows the neural network to be trained using backpropagation [03:45:00] and gradient descent to minimize errors between observed images and the rendered views [08:38:00].

A NeRF model can predict an arbitrary number of properties beyond just RGB color and opacity, such as specularity or roughness, potentially enabling [[Mesh generation techniques | physics simulations]] in the future [02:46:00, 02:50:00].

### Optimization in Ray Marching
The "Nerfacc" (NeRF acceleration toolkit) paper focuses on optimizing the ray marching process to achieve efficiency [01:37:00]. The primary bottleneck in NeRF rendering is evaluating the Radiance Field for each sample [01:38:00]. Efficiency can be achieved by reducing the number of samples as much as possible during ray marching [01:40:00].

Key optimization techniques include:
*   **Skipping Empty/Occluded Spaces**: Samples that have very low opacity or low transmittance contribute little to the final image and can be safely skipped [01:48:00, 01:58:00]. For instance, 98% of samples in a dense Lego scene can be ignored due to being empty space or behind an opaque object [02:08:00, 02:10:00].
*   **Occupancy Grid**: A binary grid is cached and updated during training to store which areas of the scene are empty [01:19:17]. This prevents unnecessary computation on areas that will yield zero opacity [01:19:00]. Opacity thresholds (e.g., less than 1e-2) are used to identify empty areas [01:19:24, 01:37:02].
*   **Transmittance Threshold**: Ray marching can be terminated early if the transmittance (the amount of light passing through) falls below a certain threshold (e.g., 1e-4) [01:19:34, 01:36:54].

### GPU Optimization and Parallelization
Optimizing for GPUs involves cleverly managing the batch dimensions of tensors [02:18:00]. Nerfacc minimizes operations parallelized across rays and instead prioritizes parallelization across samples, especially since sample opacity and density are independent of the specific rays [02:34:00, 02:40:00]. This "clever mapping" allows optimal use of a single GPU [02:44:00, 02:46:00].

> ```python
> colors, opacity, _ = nerfack.render_image(
>     ray_origins=rays_o,
>     ray_directions=rays_d,
>     t_starts=t_starts,
>     t_ends=t_ends,
>     ray_indices=ray_indices,
>     n_rays=n_rays,
>     rgb_sigma_fn=rgb_sigma_fn,
>     render_bkgd=render_bkgd,
> )
> ```
> This code snippet demonstrates the [[Differentiable rendering and optimization | differentiable rendering]] process, where `rgb_sigma_fn` calculates colors and opacities for given rays [03:08:00, 03:10:00].

## Handling Scene Types
*   **Bounded Scenes**: These scenes contain an object confined within a specific 3D volume [02:27:00]. Many early NeRF papers focused on bounded scenes [02:37:00].
*   **Unbounded Scenes**: These include environments like backyards where a large background technically extends to infinity, making it impossible to constrain the entire scene to a specific volume [02:52:00, 02:58:00]. Nerfacc incorporates a scene contraction idea from "MIP NeRF 360" to support unbounded scenes by applying a nonlinear function to map the unbounded space into a finite grid [02:09:00, 02:11:00, 02:21:00].

## Core Functions in Nerfacc
Users primarily define two Python functions within Nerfacc:
1.  **`Sigma FN`**: Given sample interval starts (`t_starts`) and ends (`t_ends`) along a ray, and ray indices, this function queries the [[Volumetric rendering and neural Radiance fields | Radiance Field]] (MLP) for the *density* (opacity) at those positions [03:00:00, 03:06:00, 03:26:00, 03:32:00]. Density only requires the XYZ position, not the view angle [03:41:00].
2.  **`RGB Sigma FN`**: Similar to `Sigma FN`, but it also queries the Radiance Field for the *color* (RGB) in addition to density [03:27:00, 03:31:00]. To get the color, the network needs both the position (XYZ) and the view angles (pitch and yaw) of the ray [03:48:00, 03:55:00].

## Performance Improvements
Vanilla NeRF models can take up to two days to converge on a single scene [03:54:00]. Nerfacc significantly reduces this training time:
*   **Static Scenes**: An "instant NGP" NeRF model can be trained in less than one hour to better quality [01:29:00].
*   **Dynamic Scenes**: A "D-NeRF" model for dynamic scenes, which adds a time dimension to the input of the neural network [04:48:00], can be trained in one hour rather than two days [01:05:00, 01:07:00, 01:10:00, 01:12:00].

> **Training Time Comparison (Original NeRF vs. Nerfacc)**
> | Scene   | Original NeRF Training Time | Nerfacc Training Time |
> | :------ | :-------------------------- | :-------------------- |
> | Static  | Days (e.g., 4 mins for Nerfacc) [04:12:00, 04:16:00] | ~4.5 minutes [05:08:00, 05:09:00] |
> | Dynamic | ~2 days [01:10:00, 03:54:00] | ~1 hour [01:05:00, 01:07:00] |

These improvements come from the computational savings achieved by skipping unnecessary computations via the occupancy grid and transmittance thresholds [04:17:00, 04:45:00].# Ray Marching and Differentiable Rendering

[[Volumetric rendering and neural Radiance fields | Neural Radiance Fields]] (NeRFs) are a prominent type of [[Volumetric rendering and neural Radiance fields | volumetric rendering]] that utilizes [[Differentiable rendering and optimization | differentiable rendering]] and may eventually replace current rendering stacks [02:20:00]. This technique is used for [[canonical 3D volume representation | 3D representation]] and involves training a neural network, specifically a Multi-Layer Perceptron (MLP), to encode the view-dependent appearance of a scene [02:50:00, 03:01:00].

## What is Ray Marching?
[[Ray marching and differentiable rendering | Ray marching]] is the [[Volumetric rendering and neural Radiance fields | volumetric rendering]] algorithm at the core of NeRFs [03:38:00]. It involves casting a ray into a 3D space and generating discrete samples along that ray [06:12:00, 01:43:00].

### Process
1.  **Input**: The neural network receives the position of a camera (`Ray Origins`) and the direction (`Ray Directions`) from which a scene is to be rendered [03:14:00, 06:46:00, 06:49:00, 02:52:00].
2.  **Ray Tracing**: A ray is traced through the 3D space [07:12:00].
3.  **Sampling**: At each point along the ray, the neural network is sampled to determine the color and "alpha" (see-throughness or opacity) at that specific point [07:14:00, 07:22:00].
4.  **Accumulation**: The colors and opacities from all sampled points along the ray are added up to determine the final pixel color for that ray [07:27:00, 08:00:00]. This process of accumulating colors along the ray is called [[Differentiable rendering and optimization | differentiable rendering]] [06:15:00, 06:33:00].

## Differentiable Rendering and Training
The [[Volumetric rendering and neural Radiance fields | volumetric rendering]] algorithm, specifically [[Ray marching and differentiable rendering | ray marching]], is [[Differentiable rendering and optimization | differentiable]] [03:43:00]. This differentiability allows the neural network to be trained using backpropagation [03:45:00] and gradient descent to minimize errors between observed images and the rendered views [08:38:00].

A NeRF model can predict an arbitrary number of properties beyond just RGB color and opacity, such as specularity or roughness, potentially enabling [[Mesh generation techniques | physics simulations]] in the future [02:46:00, 02:50:00, 02:53:00].

### Optimization in Ray Marching
The "Nerfacc" (NeRF acceleration toolkit) paper focuses on optimizing the [[Ray marching and differentiable rendering | ray marching]] process to achieve efficiency [01:37:00]. The primary bottleneck in NeRF rendering is evaluating the Radiance Field for each sample [01:38:00]. Efficiency can be achieved by reducing the number of samples as much as possible during ray marching [01:40:00].

Key optimization techniques include:
*   **Skipping Empty/Occluded Spaces**: Samples that have very low opacity or low transmittance contribute little to the final image and can be safely skipped [01:48:00, 01:58:00]. For instance, 98% of samples in a dense Lego scene can be ignored due to being empty space or behind an opaque object [02:08:00, 02:10:00].
*   **Occupancy Grid**: A binary grid is cached and updated during training to store which areas of the scene are empty [01:19:17]. This prevents unnecessary computation on areas that will yield zero opacity [01:19:00]. Opacity thresholds (e.g., less than 1e-2) are used to identify empty areas [01:19:24, 01:37:02].
*   **Transmittance Threshold**: [[Ray marching and differentiable rendering | Ray marching]] can be terminated early if the transmittance (the amount of light passing through) falls below a certain threshold (e.g., 1e-4) [01:19:34, 01:36:54].

### GPU Optimization and Parallelization
Optimizing for GPUs involves cleverly managing the batch dimensions of tensors [02:18:00]. Nerfacc minimizes operations parallelized across rays and instead prioritizes parallelization across samples, especially since sample opacity and density are independent of the specific rays [02:34:00, 02:40:00]. This "clever mapping" allows optimal use of a single GPU [02:44:00, 02:46:00]. Modern deep learning frameworks like PyTorch and Jax can automatically handle such parallelization (e.g., `vmap` and `pmap` in Jax) [02:48:00, 02:51:00, 02:54:00].

> ```python
> colors, opacity, _ = nerfack.render_image(
>     ray_origins=rays_o,
>     ray_directions=rays_d,
>     t_starts=t_starts,
>     t_ends=t_ends,
>     ray_indices=ray_indices,
>     n_rays=n_rays,
>     rgb_sigma_fn=rgb_sigma_fn,
>     render_bkgd=render_bkgd,
> )
> ```
> This code snippet demonstrates the [[Differentiable rendering and optimization | differentiable rendering]] process, where `rgb_sigma_fn` calculates colors and opacities for given rays [03:08:00, 03:10:00].

## Handling Scene Types
*   **Bounded Scenes**: These scenes contain an object confined within a specific 3D volume [02:27:00]. Many early NeRF papers focused on bounded scenes [02:37:00].
*   **Unbounded Scenes**: These include environments like backyards where a large background technically extends to infinity, making it impossible to constrain the entire scene to a specific volume [02:52:00, 02:58:00]. Nerfacc incorporates a scene contraction idea from "MIP NeRF 360" to support unbounded scenes by applying a nonlinear function to map the unbounded space into a finite grid [02:09:00, 02:11:00, 02:21:00].

## Core Functions in Nerfacc
Users primarily define two Python functions within Nerfacc:
1.  **`Sigma FN`**: Given sample interval starts (`t_starts`) and ends (`t_ends`) along a ray, and ray indices, this function queries the [[Volumetric rendering and neural Radiance fields | Radiance Field]] (MLP) for the *density* (opacity) at those positions [03:00:00, 03:06:00, 03:26:00, 03:32:00]. Density only requires the XYZ position, not the view angle [03:41:00].
2.  **`RGB Sigma FN`**: Similar to `Sigma FN`, but it also queries the Radiance Field for the *color* (RGB) in addition to density [03:27:00, 03:31:00]. To get the color, the network needs both the position (XYZ) and the view angles (pitch and yaw) of the ray [03:48:00, 03:55:00].

## Performance Improvements
Vanilla NeRF models can take up to two days to converge on a single scene [03:54:00]. Nerfacc significantly reduces this training time:
*   **Static Scenes**: An "instant NGP" NeRF model can be trained in less than one hour to better quality [01:29:00].
*   **Dynamic Scenes**: A "D-NeRF" model for dynamic scenes, which adds a time dimension to the input of the neural network [04:48:00], can be trained in one hour rather than two days [01:05:00, 01:07:00, 01:10:00, 01:12:00].

> **Training Time Comparison (Original NeRF vs. Nerfacc)**
> | Scene | Original NeRF Training Time | Nerfacc Training Time |
> | :---- | :-------------------------- | :-------------------- |
> | Static | Days (e.g., 4 mins for Nerfacc) [04:12:00, 04:16:00] | ~4.5 minutes [05:08:00, 05:09:00] |
> | Dynamic | ~2 days [01:10:00, 03:54:00] | ~1 hour [01:05:00, 01:07:00] |

These improvements come from the computational savings achieved by skipping unnecessary computations via the occupancy grid and transmittance thresholds [04:17:00, 04:45:00].