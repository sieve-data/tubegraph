---
title: Neural volume rendering and Radiance Fields
videoId: ccGxQCpbrnM
---

From: [[hu-po]] <br/> 

[[neural_volume_rendering_and_radiance_fields | Neural volume rendering]] is a technique that uses [[neural_network_diffusion_and_applications | neural networks]] to render a 3D volume, which is a 3D space <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It is the technique behind [[comparison_of_gaussian_splats_and_neural_radiance_fields_nerfs | Neural Radiance Fields]] (NeRFs) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## Neural Radiance Fields (NeRFs)
A [[comparison_of_gaussian_splats_and_neural_radiance_fields_nerfs | NeRF]] encodes a 3D scene using a [[highdimensional_spaces_and_information_storage_in_neural_nets | multi-layer perceptron]] (MLP) to map 3D spatial locations to color and volume density <a class="yt-timestamp" data-t="03:09:58">[03:09:58]</a>. An MLP is a fancy term for a fully connected neural network <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>.

### How NeRFs Work
1.  **Scene Encoding**: A [[comparison_of_gaussian_splats_and_neural_radiance_fields_nerfs | NeRF]] takes an X, Y, and Z coordinate (3D position) and a view angle (Theta and Phi) as input to its MLP <a class="yt-timestamp" data-t="03:11:55">[03:11:55]</a>. Given this information, the MLP outputs the color (RGB) and opacity (or volume density) of that specific point in space <a class="yt-timestamp" data-t="03:17:16">[03:17:16]</a>.
2.  **Ray Marching**: To render a 2D image from a [[comparison_of_gaussian_splats_and_neural_radiance_fields_nerfs | NeRF]], a "ray marching" algorithm is used <a class="yt-timestamp" data-t="03:26:59">[03:26:59]</a>. For each pixel in the 2D image, a ray is cast from the camera's origin through that pixel into the 3D scene <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>.
3.  **Sampling**: Points are sampled along this ray <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. For each sampled point, the MLP predicts its color and opacity <a class="yt-timestamp" data-t="03:11:14">[03:11:14]</a>.
4.  **Volume Rendering**: The predicted colors and opacities from the sampled points along the ray are then integrated to determine the final color of the pixel <a class="yt-timestamp" data-t="03:04:05">[03:04:05]</a>. As light travels along the ray, transparency accumulates. Once a high level of opacity is reached, further sampling along the ray may not be necessary as the light is blocked <a class="yt-timestamp" data-t="03:11:12">[03:11:12]</a>.

### Challenges with NeRFs
*   **Implicit Representation**: A significant challenge is that [[comparison_of_gaussian_splats_and_neural_radiance_fields_nerfs | NeRFs]] provide an implicit representation of a scene <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. This means the underlying geometry is not explicitly defined, making it difficult to extract a mesh or texture for applications like video games or physics simulations <a class="yt-timestamp" data-t="03:26:02">[03:26:02]</a>.
*   **Fuzzy Surfaces**: Due to insufficient constraints, surfaces extracted from density-based [[comparison_of_gaussian_splats_and_neural_radiance_fields_nerfs | NeRF]] representations can often be noisy or fuzzy, lacking crisp, defined edges <a class="yt-timestamp" data-t="03:52:09">[03:52:09]</a>.
*   **Computational Cost**: [[comparison_of_gaussian_splats_and_neural_radiance_fields_nerfs | NeRFs]] are computationally expensive because inference must be performed on the MLP for every sampled point along every ray for every pixel in an image <a class="yt-timestamp" data-t="03:38:40">[03:38:40]</a>. This leads to slow rendering times <a class="yt-timestamp" data-t="03:40:40">[03:40:40]</a>.

## Related Concepts and Solutions

### [[signed_distance_functions_and_neural_radiance_fields | Signed Distance Functions (SDFs)]]
[[signed_distance_functions_and_neural_radiance_fields | Signed Distance Functions]] (SDFs) are a common surface representation that tell you how far away you are from the surface of an object at any point inside a volume <a class="yt-timestamp" data-t="01:26:26">[01:26:26]</a>. They are "signed" because the value is positive outside the surface, zero at the surface, and negative inside the surface <a class="yt-timestamp" data-t="01:27:07">[01:27:07]</a>. [[signed_distance_functions_and_neural_radiance_fields | SDFs]] are differentiable, which is important for gradient-based optimization in machine learning <a class="yt-timestamp" data-t="01:09:36">[01:09:36]</a>.

Recent approaches combine [[comparison_of_gaussian_splats_and_neural_radiance_fields_nerfs | NeRFs]] with [[signed_distance_functions_and_neural_radiance_fields | SDFs]] to better define 3D surfaces <a class="yt-timestamp" data-t="01:39:55">[01:39:55]</a>.

### Multi-resolution Hash Encodings
[[neural_angelo_framework | Neuralangelo]] combines [[signed_distance_functions_and_neural_radiance_fields | SDFs]] with multi-resolution hash encodings <a class="yt-timestamp" data-t="02:05:01">[02:05:01]</a>.
*   A hash is a map between a key and a value, like a Python dictionary <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>.
*   A 3D hash grid maps a 3D position in space to some stored value <a class="yt-timestamp" data-t="00:44:49">[00:44:49]</a>.
*   "Multi-resolution" means there are different sizes of these hash maps, from coarse to fine resolutions, which allows quick access to information within a 3D volume <a class="yt-timestamp" data-t="00:45:12">[00:45:12]</a>.
*   [[neural_angelo_framework | Neuralangelo]] utilizes 16 different grid resolutions, with each hash entry having a channel size of 8 <a class="yt-timestamp" data-t="01:49:49">[01:49:49]</a>.

### Analytical vs. Numerical Gradients
*   **Analytical Gradients**: Involve mathematically solving for the exact derivative of a function <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>.
*   **Numerical Gradients**: Involve approximating the derivative by sampling points slightly above and below the point of interest and estimating the slope <a class="yt-timestamp" data-t="01:06:02">[01:06:02]</a>. They are generally faster but fundamentally less accurate <a class="yt-timestamp" data-t="01:09:42">[01:09:42]</a>.
*   For [[neural_angelo_framework | Neuralangelo]], analytical gradients for hash encodings are not continuous across space under tri-linear interpolation, which limits back-propagation to local hash grid cells <a class="yt-timestamp" data-t="01:15:48">[01:15:48]</a>. Using numerical gradients allows back-propagation updates to be distributed beyond just the local hash grid cell, acting as a smoothing operation on the [[signed_distance_functions_and_neural_radiance_fields | SDF]] <a class="yt-timestamp" data-t="01:27:26">[01:27:26]</a>. This means a wider area of the grid cells receive optimization updates simultaneously <a class="yt-timestamp" data-t="01:25:34">[01:25:34]</a>.

### Higher-Order Derivatives
Higher-order derivatives are any derivatives beyond the first (e.g., second, third derivatives) <a class="yt-timestamp" data-t="01:06:59">[01:06:59]</a>. The gradient of an [[signed_distance_functions_and_neural_radiance_fields | SDF]] satisfies the eikonal equation, meaning its magnitude is typically one <a class="yt-timestamp" data-t="01:10:14">[01:10:14]</a>. An eikonal loss is added to the optimization process to enforce this property <a class="yt-timestamp" data-t="01:11:01">[01:11:01]</a>. Numerical gradients are used to compute these higher-order derivatives for surface normals and curvature <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>.

### Progressive Optimization and Level of Detail (LOD)
[[neural_angelo_framework | Neuralangelo]] uses a coarse-to-fine optimization schedule <a class="yt-timestamp" data-t="02:28:28">[02:28:28]</a>. It starts with an initial set of coarse hash grids and progressively activates finer hash grids throughout the optimization process <a class="yt-timestamp" data-t="01:53:11">[01:53:11]</a>. The step size for numerical gradients is initialized to match the coarsest hash grid and then exponentially decreases, matching different hash grid sizes over time <a class="yt-timestamp" data-t="01:53:29">[01:53:29]</a>. This strategy helps shape the loss landscape to avoid falling into false local minima during optimization <a class="yt-timestamp" data-t="01:36:15">[01:36:15]</a>.

This progressive approach naturally yields a Level of Detail (LOD) capability, similar to what's used in video games. A coarser, lower-resolution version of the scene is initially produced, and as optimization continues, finer details are added, allowing for a trade-off between optimization time and reconstruction fidelity <a class="yt-timestamp" data-t="02:00:17">[02:00:17]</a>.

### Regularization
*   **Curvature Regularization**: [[neural_angelo_framework | Neuralangelo]] imposes a prior by regularizing the mean curvature of the [[signed_distance_functions_and_neural_radiance_fields | SDF]] to encourage smoothness <a class="yt-timestamp" data-t="01:44:10">[01:44:10]</a>. Without this, surfaces can have undesirable sharp transitions <a class="yt-timestamp" data-t="02:01:25">[02:01:25]</a>. However, too much smoothing can prevent the modeling of sharp features like bricks or concave shapes <a class="yt-timestamp" data-t="02:03:13">[02:03:13]</a>.
*   **Weight Decay**: Applied to all parameters to prevent single-resolution features from dominating the final result <a class="yt-timestamp" data-t="01:43:43">[01:43:43]</a>.
*   **Topology Warm-up**: The [[signed_distance_functions_and_neural_radiance_fields | SDF]] is initially approximated as a sphere during a short warm-up period, and the curvature loss strength is linearly increased later in training <a class="yt-timestamp" data-t="02:03:29">[02:03:29]</a>. This leverages the common "object-centric" prior that many 3D scenes have <a class="yt-timestamp" data-t="02:02:16">[02:02:16]</a>.

## Applications
The recovered surfaces from these methods provide structural information useful for:
*   3D asset generation <a class="yt-timestamp" data-t="01:11:21">[01:11:21]</a>
*   Environment mapping for autonomous navigation of robotics <a class="yt-timestamp" data-t="01:11:55">[01:11:55]</a>
*   Augmented and Virtual Reality <a class="yt-timestamp" data-t="01:12:04">[01:12:04]</a>
*   Novel view synthesis, which can involve interpolating between existing views or generating views from entirely new camera angles <a class="yt-timestamp" data-t="01:00:09">[01:00:09]</a>.

[[neural_angelo_framework | Neuralangelo]] specifically aims to reconstruct dense 3D surface structures from multi-view [[RGB images]] (or video) without requiring auxiliary data like depth or segmentation <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.