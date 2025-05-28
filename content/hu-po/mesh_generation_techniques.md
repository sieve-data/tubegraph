---
title: Mesh generation techniques
videoId: SkvyrgSzigo
---

From: [[hu-po]] <br/> 

Mesh generation is a core aspect of creating three-dimensional digital content, with techniques constantly evolving to produce higher-quality, more controllable, and industrially usable 3D assets <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>. While traditional methods often rely on alternative 3D representations like NeRFs, the goal is often to convert these into meshes for use in game engines and CGI tools <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>.

## MeshFormer: 3D Guided Reconstruction

"MeshFormer" is a model developed by UC San Diego, UCLA, and Hbot Inc., released in August 2024 <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. It focuses on generating high-quality 3D textured meshes <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a> with fine-grained geometric details rapidly <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

### Inputs and Key Components
The model takes a sparse set of six multi-view RGB images and their corresponding normal maps as input <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

*   **Normal Maps**: These are images where the color at each pixel represents the direction of the normal vector, which is perpendicular to a surface <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. They allow for a more detailed 3D effect <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a> and provide crucial geometric guidance for 3D reconstruction <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>. The key insight of MeshFormer is the use of [[image_generation_using_advanced_mathematical_models | diffusion models]] to generate these normal maps from arbitrary images <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   **3D Sparse Convolution and Transformers**: MeshFormer leverages a 3D U-Net architecture with a Transformer at the bottleneck <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>. This integrates an explicit 3D structure and projective bias, making it an easier task to learn <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. It uses sparse voxels to manage computational expense by discarding empty space <a class="yt-timestamp" data-t="00:30:25">[00:30:25]</a>.
*   **Projection-Aware Cross-Attention**: Within the U-Net, this mechanism combines features from both RGB and normal map patches, aware of the camera view <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
*   **Signed Distance Function (SDF)**: The model estimates the SDF, which indicates the distance to the object's surface (zero on the surface, positive outside, negative inside) <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>. This, along with color and normal estimates, allows for mesh creation using the marching cubes algorithm <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.
*   **Unified Single-Stage Training**: The entire pipeline can be trained at once, pushing gradients through various losses, although it relies on pre-trained 2D diffusion models for normal map generation and a DINOv2 encoder <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a> <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>.

## MeshAnything: Artist-Created Mesh Generation

"MeshAnything" (June 2024) proposes a different approach to mesh generation, focusing on producing "artist-created" meshes <a class="yt-timestamp" data-t="00:36:32">[00:36:32]</a>.

### The Importance of Topology
Artist-created meshes possess "good topology" <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>, characterized by clean contour lines that facilitate animation and texturing <a class="yt-timestamp" data-t="00:38:06">[00:38:06]</a>. In contrast, meshes from photogrammetry or the marching cubes algorithm often have irregular topology, making them challenging for industry use <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>.

### Approach: VQVAE and Autoregressive Transformers
*   **[[introduction_to_vqvae_and_its_application_in_mesh_generation | VQVAE]] for Mesh Vocabulary**: MeshAnything uses a Vector Quantized Variational AutoEncoder (VQVAE) to learn a discrete "mesh vocabulary" or "shape tokens" <a class="yt-timestamp" data-t="00:48:27">[00:48:27]</a>. This allows the model to output a sequence of these tokens.
*   **Direct Mesh Generation**: Instead of generating an implicit 3D representation (like SDFs or NeRFs) and then converting it to a mesh via marching cubes, MeshAnything directly generates the mesh token by token using a decoder-only Transformer <a class="yt-timestamp" data-t="00:50:03">[00:50:03]</a>. This process literally builds the mesh piece by piece <a class="yt-timestamp" data-t="00:50:46">[00:50:46]</a>.
*   **Noise-Resistant Decoder (Data Augmentation)**: The model uses a data augmentation technique where intentionally corrupted meshes (with "shitty topology") are used during training. The model learns to transform these into higher-quality meshes with good topology <a class="yt-timestamp" data-t="00:58:39">[00:58:39]</a> <a class="yt-timestamp" data-t="00:59:05">[00:59:05]</a>. This helps the Transformer understand and produce meshes with desired topological properties <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>.
*   **Input**: The model starts from a point cloud, which can be obtained from LiDAR scanning or photogrammetry from cell phone images <a class="yt-timestamp" data-t="00:56:31">[00:56:31]</a>.

## JPEG LM: Generating Content with Canonical Codecs

The "JPEG LM" paper (August 2024) explores an extreme form of autoregressive generation, applying similar principles to [[image_generation_using_advanced_mathematical_models | image generation using advanced mathematical models]] and [[techniques_used_in_ai_video_generation | AI video generation techniques]].

### Direct Generation of Compressed Files
This work proposes modeling images and videos directly as compressed files (e.g., JPEG for images, H.264 for video) saved on a computer <a class="yt-timestamp" data-t="01:00:44">[01:00:44]</a>.

*   **Canonical Codec Representation**: The language model generates the literal sequence of "weird text" or tokens that represent the compressed image file <a class="yt-timestamp" data-t="01:01:34">[01:01:34]</a>. This is challenging because the generated sequence needs to be "perfect" for the image to be valid <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>.
*   **Comparison to VQVAE**: Unlike VQVAE, which learns a new, potentially less human-interpretable vocabulary of tokens <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>, JPEG LM uses an existing, standardized compression format. While both are lossy, JPEG encoding is often significantly better at preserving detailed, highly perceptible elements like faces and text, whereas VQVAE might excel in color and sharpness <a class="yt-timestamp" data-t="01:11:55">[01:11:55]</a>.
*   **Absence of Vision-Specific Modules**: JPEG LM uses conventional LLM architectures without any vision-specific modifications like convolutions or 2D positional embeddings <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a>. This aims to maximize the model's generality and unify language and visual generation paradigms <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>.

## Future Implications for 3D Content Creation

These papers highlight a potential shift in how 3D content is generated and represented.
*   **[[comparison_of_3d_representation_techniques | Meshes vs. Implicit Representations]]**: While implicit representations like NeRFs and Gaussian Splats are promising for deep learning, the existing 3D industry heavily relies on meshes <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>. If AI can directly generate high-quality meshes with good topology, it could mean that meshes continue to be the standard 3D representation due to the significant momentum and existing tools <a class="yt-timestamp" data-t="00:54:31">[00:54:31]</a>.
*   **[[compositional_3d_asset_creation_and_multiobject_generation | Text to 3D Content Generation]] and [[text_to_3d_content_generation | Challenges in 3D model generation using diffusion models]]**: The JPEG LM approach suggests that models could directly generate raw 3D file formats (like STL files) token by token <a class="yt-timestamp" data-t="01:12:52">[01:12:52]</a>, bypassing intermediate representations or learned vocabularies. This could simplify [[techniques_for_optimizing_and_refining_3d_models | techniques for optimizing and refining 3D models]] and streamline the creation pipeline, especially if coupled with developments like Universal Scene Description (USD) generation <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.
*   **[[dynamic_3d_gaussian_technique | Dynamic 3D Gaussian Technique]]**: This technique, while distinct, also highlights the evolution of 3D representations alongside meshes.