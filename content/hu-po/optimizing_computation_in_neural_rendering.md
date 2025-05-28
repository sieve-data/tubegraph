---
title: Optimizing computation in neural rendering
videoId: Y73KU0ShHdM
---

From: [[hu-po]] <br/> 

## Introduction to Nerf-ack

Nerf-ack (Nerf ass ax nerfack) is a general NeRF acceleration toolkit, a recently released paper from the University of California Berkeley <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. It is designed to accelerate various [[volumetric_rendering_and_neural_radiance_fields | NeRFs]] in different applications <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. Nerf-ack supports not only bounded static scenes but also dynamic and unbounded scenes, offering a user-friendly Python API that is ready for Plug and Play acceleration for most [[volumetric_rendering_and_neural_radiance_fields | Nerfs]] <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

[[volumetric_rendering_and_neural_radiance_fields | Neural Radiance Fields]] (NeRFs) use [[volumetric_rendering_and_neural_radiance_fields | volumetric rendering]], which is differentiable, making it a popular type of rendering that could potentially replace current rendering stacks in the future <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. [[volumetric_rendering_and_neural_radiance_fields | NeRFs]] are used for 3D representation and involve training a neural network, specifically a Multi-Layer Perceptron (MLP), to encode the view-dependent appearance of a scene <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The network takes a view vector (direction) and returns pixel values <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The key aspect is that the [[volumetric_rendering_and_neural_radiance_fields | volumetric rendering]] algorithm, which employs ray marching, is differentiable, allowing training with backpropagation <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## The Need for Speed in NeRFs

A significant challenge with vanilla NeRFs is their training time; they usually take about two days to converge on a single scene <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This limitation highlights the critical need for [[neural_network_optimization_strategies | optimization strategies]] to make NeRFs more practical <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Nerf-ack's [[neural_network_optimization_strategies | Optimization Strategies]]

### Efficient Ray Marching

The volumetric rendering pipeline in NeRFs is broken down into two steps: ray marching and differentiable rendering <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

Ray marching is the process of casting a ray through a scene and generating discrete samples along that ray <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. These samples are then evaluated by the [[volumetric_rendering_and_neural_radiance_fields | Radiance Field]] (the neural network), which is usually the main bottleneck <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>. Nerf-ack achieves efficiency by reducing the number of samples as much as possible during ray marching <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

The core idea for optimization is to skip samples that would have little contribution to the final image, specifically those with low opacity or low transmittance <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. This means safely skipping samples that are in empty or occluded regions of the scene <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. For example, in a dense Lego scene, this pruning can eliminate 98% of the samples <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.

To achieve this, Nerf-ack uses an **occupancy grid**, a binary grid that is cached and updated to store which areas of the scene are empty <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>. They use a threshold where opacity less than `1e-2` or transmittance below `1e-4` leads to termination of ray marching for that segment, preventing unnecessary computations <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.

### [[gpu_implementation_and_optimization | GPU Implementation and Optimization]]

[[gpu_implementation_and_optimization | GPU optimization]] is critical, especially regarding how computations are parallelized <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. There are typically two options for parallelization on the [[gpu_implementation_and_optimization | GPU]]: across rays or across samples <a class="yt-timestamp" data-t="00:21:31">[00:21:31]</a>. Nerf-ack minimizes operations parallelized across rays <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>. Since sample opacity and density are independent of the rays, they can be parallelized across samples <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>. This "clever mapping" onto a single [[gpu_implementation_and_optimization | GPU]] helps in getting the best out of the hardware <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>.

### Handling Unbounded Scenes

Many NeRF papers focus on bounded scenes where the object is confined to a specific 3D volume <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>. However, unbounded scenes (like a backyard) have a huge background that extends to infinity, making it challenging to constrain everything a camera sees to a specific volume <a class="yt-timestamp" data-t="00:25:52">[00:26:10]</a>. Nerf-ack incorporates a scene contraction idea from MIP-NeRF 360 to support unbounded scenes by applying a nonlinear function to coordinates to map the unbounded space into a finite grid <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.

### Course-to-Fine Sampling

A common technique in NeRFs, also utilized by Nerf-ack, is course-to-fine sampling <a class="yt-timestamp" data-t="00:42:22">[00:42:22]</a>. This involves initially sampling a small number of points along a ray (coarse sampling) to identify areas with high opacity <a class="yt-timestamp" data-t="00:43:16">[00:43:16]</a>. Then, a larger number of points are sampled densely around these high-opacity areas (fine sampling), optimizing computation by focusing on relevant regions <a class="yt-timestamp" data-t="00:43:23">[00:43:23]</a>.

## Implementation Details

Nerf-ack is implemented in PyTorch, which has surpassed TensorFlow in popularity since around 2020 <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

The toolkit provides two key functions that users need to define for their [[volumetric_rendering_and_neural_radiance_fields | Radiance Field]]:
*   `Sigma FN`: This function takes ray origins, directions, and sample intervals (start and end points `T starts`, `T ends`) along the ray. It calculates the positions of discrete samples and queries the [[volumetric_rendering_and_neural_radiance_fields | Radiance Field]] for the density (sigma) at these positions <a class="yt-timestamp" data-t="00:30:59">[00:30:59]</a>. The density calculation primarily depends on the XYZ position, not the view angle <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.
*   `RGB Sigma FN`: Similar to `Sigma FN`, this function queries the [[volumetric_rendering_and_neural_radiance_fields | Radiance Field]] for both the color (RGB) and density (sigma) at the sampled positions <a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a>. For color prediction, the network needs to be conditioned on the direction of the ray (view angle) in addition to the position, as the color can be view-dependent <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>.

The core [[neural_network_optimization_strategies | optimization strategy]] in Nerf-ack's ray marching function uses parameters like `near_plane`, `far_plane` (sampling distance limits), `early_stop_epsilon` (transmittance threshold), and `alpha_threshold` (opacity threshold) to efficiently skip empty and occluded space <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>.

During training, the system computes a loss by comparing the rendered image (from differentiable rendering) to the ground truth color. It then uses an optimizer (e.g., Adam) and a learning rate scheduler to adjust the MLP's weights and biases via backpropagation <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.

## Performance and Comparisons

Nerf-ack demonstrates significant improvements in training time without sacrificing quality (measured by PSNR) <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. For static scenes, it can reduce training time from two days for vanilla NeRF to roughly four minutes for models like Instant-NGP NeRF <a class="yt-timestamp" data-t="00:43:59">[00:43:59]</a>. For dynamic scenes (e.g., D-NeRF model), training can be reduced from two days to about one hour <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

The training memory footprint for an 8-layer MLP in Nerf-ack for a static scene is about 10 gigabytes <a class="yt-timestamp" data-t="00:40:20">[00:40:20]</a>. For dynamic scenes, which involve an additional time dimension variable, the memory footprint increases, for example, to 11 gigabytes for a setup involving an 8-layer MLP for the [[volumetric_rendering_and_neural_radiance_fields | Radiance Field]] and a 4-layer MLP for a warping field <a class="yt-timestamp" data-t="00:45:49">[00:46:09]</a>.

This acceleration is achieved by saving computation time through masking out unnecessary computations, such as the `packed_info` mask that prevents rendering parts of space not worth rendering <a class="yt-timestamp" data-t="00:41:53">[00:41:53]</a>.

<br>
<hr>
<br>

> [!NOTE] Practical Experience
> The transcript includes a demonstration of setting up and running Nerf-ack, highlighting common [[challenges_in_neural_network_optimization | challenges in neural network optimization]] such as managing Python virtual environments, installing dependencies (`imageio`, `tqdm`, `tiny-cuda-nn`), and resolving [[cuda_kernel_optimization_in_model_computation | CUDA kernel optimization in model computation]] version mismatches <a class="yt-timestamp" data-t="00:49:36">[00:49:36]</a>. A key issue encountered was the `nvcc` compiler not being found, requiring the CUDA path to be explicitly added to the environment variables for the C++ and [[cuda_kernel_optimization_in_model_computation | CUDA kernel optimization in model computation]] extensions to compile correctly <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>. Despite running on less powerful hardware (e.g., an Nvidia 1070 GPU) compared to the Nvidia Titan used in the paper, reduced training epochs and increased learning rates still allowed for a visible, albeit low-quality, render of the scene, demonstrating the effectiveness of the optimization strategies <a class="yt-timestamp" data-t="01:22:46">[01:22:46]</a>.