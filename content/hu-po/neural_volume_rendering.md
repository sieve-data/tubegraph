---
title: Neural volume rendering
videoId: ccGxQCpbrnM
---

From: [[hu-po]] <br/> 

[[volumetric_rendering_and_neural_radiance_fields | Neural volume rendering]] is a technique that leverages neural networks to render a 3D volume <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It is the underlying technology for approaches such as [[volumetric_rendering_and_neural_radiance_fields | Neural Radiance Fields]] (Nerfs) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. In this context, "volume" refers to a 3D space <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## How it Works: The Role of Neural Radiance Fields (Nerfs)

A [[volumetric_rendering_and_neural_radiance_fields | Nerf]] encodes a 3D scene using a multi-layer perceptron (MLP), which is a fully connected neural network <a class="yt-timestamp" data-t="03:09:58">[03:09:58]</a>. This MLP maps 3D spatial locations to color (RGB) and volume density (opacity) <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.

To render a pixel, the [[volumetric_rendering_and_neural_radiance_fields | Nerf]] takes as input a 3D position (X, Y, Z) and a view angle (Theta, Phi) <a class="yt-timestamp" data-t="03:12:06">[03:12:06]</a>. The MLP outputs the color and opacity for that specific point when viewed from that direction <a class="yt-timestamp" data-t="03:17:16">[03:17:16]</a>.

The process of rendering a 2D image from a [[volumetric_rendering_and_neural_radiance_fields | Neural Radiance Field]] involves a [[ray_marching_and_differentiable_rendering | ray marching algorithm]] <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. This involves:
1.  Sampling points along a ray extending from the camera through a pixel <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
2.  For each sampled point, the MLP predicts its color and opacity (density) <a class="yt-timestamp" data-t="03:06:06">[03:06:06]</a>.
3.  These predicted colors and opacities are integrated along the ray to determine the final color of the pixel <a class="yt-timestamp" data-t="03:08:05">[03:08:05]</a>.

### Advantages of Nerfs

*   **Implicit Scene Encoding:** [[volumetric_rendering_and_neural_radiance_fields | Nerfs]] implicitly encode a scene within the weights of a neural network, allowing reconstruction of images without an explicit mesh or texture <a class="yt-timestamp" data-t="03:28:28">[03:28:28]</a>.
*   **Photorealistic View Synthesis:** They achieve remarkable photorealistic view synthesis, including view-dependent effects <a class="yt-timestamp" data-t="03:04:53">[03:04:53]</a>.
*   **Future Potential:** Some believe [[volumetric_rendering_and_neural_radiance_fields | Nerfs]] are the future of 3D representation, potentially replacing explicit meshes and textures in applications like VR <a class="yt-timestamp" data-t="03:39:59">[03:39:59]</a>.

### Disadvantages of Nerfs

*   **Slow Inference:** [[volumetric_rendering_and_neural_radiance_fields | Nerfs]] are computationally intensive because inference must be performed for many samples along each ray for every pixel, making them very slow <a class="yt-timestamp" data-t="03:40:40">[03:40:40]</a>.
*   **Fuzzy Surfaces:** Due to insufficient constraints, surfaces extracted from density-based representations like [[volumetric_rendering_and_neural_radiance_fields | Nerfs]] can be noisy and unrealistic, often appearing "fuzzy" with unclear edges <a class="yt-timestamp" data-t="03:51:17">[03:51:17]</a>.
*   **Lack of Explicit Geometry:** [[volumetric_rendering_and_neural_radiance_fields | Nerfs]] do not provide an explicit representation of the underlying geometry, making it difficult to perform physics simulations or directly import into game engines like Unity <a class="yt-timestamp" data-t="03:43:23">[03:43:23]</a>.

## Connection to [[neural_surface_reconstruction | Neural Surface Reconstruction]]

[[volumetric_rendering_and_neural_radiance_fields | Neural volume rendering]] and specifically [[volumetric_rendering_and_neural_radiance_fields | Nerfs]] have shown great potential for [[neural_surface_reconstruction | neural surface reconstruction]] <a class="yt-timestamp" data-t="03:20:20">[03:20:20]</a>. The *Neuralangelo* paper utilizes a [[volumetric_rendering_and_neural_radiance_fields | neural volume rendering]] approach for high-fidelity 3D surface reconstruction from RGB images <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

To address the limitations of implicit surfaces in [[volumetric_rendering_and_neural_radiance_fields | Nerfs]], methods often integrate implicit functions like occupancy grids or [[neural_surface_reconstruction | Signed Distance Functions]] (SDFs) <a class="yt-timestamp" data-t="03:54:04">[03:54:04]</a>. An SDF tells you the distance from any point in a volume to the surface of an object, with positive values outside, negative values inside, and zero at the surface <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.

The *Neuralangelo* framework combines the representational power of multi-resolution 3D hash grids with a [[neural_surface_reconstruction | neural SDF]] representation <a class="yt-timestamp" data-t="02:05:01">[02:05:01]</a>. This allows for optimized surface systems that meaningfully interpolate between spatial locations, resulting in smooth and complete surface representations <a class="yt-timestamp" data-t="01:56:51">[01:56:51]</a>.