---
title: Computer vision deep dive
videoId: SkvyrgSzigo
---

From: [[hu-po]] <br/> 

This article provides a technical deep dive into recent advancements in [[computer vision adversarial attacks | computer vision]], focusing on the generation of 3D meshes and 2D images using deep learning models. It examines three distinct papers that explore different approaches to these generative tasks, highlighting their methodologies, innovations, and implications for the future of 3D content creation.

## Overview of Papers Discussed

The stream covered three related papers that delve into [[computer vision adversarial attacks | computer vision]] generation:

*   **MeshFormer: High-Quality Mesh Generation with 3D Guided Reconstruction Model** <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>
    *   Released August 19, 2024, by UC San Diego, UCLA, and HBot Inc. <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>
    *   Focuses on generating 3D meshes using generative AI <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

*   **Mesh Anything: Artist-Created Mesh Generation with Autoregressive Transformers** <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>
    *   Released June 14, 2024, by various Chinese academic institutions and SenseTime <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    *   Also generates meshes, but with a fundamentally different approach <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

*   **JPEG-LM: LLMs as Image Generators with Canonical Codec Representations** <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>
    *   Released August 15, 2024, by the University of Washington and FAIR (Fundamental AI Research, Meta's research lab) <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   Complements the first two by exploring image generation directly from compressed file formats <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

Together, these papers explore generating visual content, including 2D images and videos (sequences of 2D images) <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>, and 3D meshes (collections of vertices representing 3D objects) <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

## MeshFormer: Enhancing 3D Reconstruction with Normal Maps

MeshFormer reconstructs a high-quality 3D textured mesh from a sparse set of six multiview RGB images and their normal maps <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

*   **Textured Mesh**: A mesh with an image (texture) wrapped around its vertices <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Multiview RGB Images**: The model takes multiple RGB images from different viewpoints (front, back, top, sides) of an object to understand its 3D form <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. A sparse view means only a few (e.g., six) views are needed <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

### The Role of Normal Maps
A key innovation in MeshFormer is the use of normal maps as input <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **Normal Map Definition**: A normal map is an image where each pixel's color represents the direction of the normal vector (a vector perpendicular to a surface) at that point in the corresponding RGB image <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Effect on 3D Appearance**: Normal maps create a more 3D effect by providing information that allows rendering pipelines to better calculate how light interacts with the object's surface, enhancing geometric details <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Generation**: The crucial insight is that normal maps can be generated from arbitrary images using [[vision language models with pretrained components | 2D diffusion models]] <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. These models, trained on vast datasets, can generalize well to produce high-quality normal maps for various scenes <a class="yt-timestamp" data-t="00:34:20">[00:34:20]</a>.
    *   This is similar to how depth maps are generated from RGB images using models like "Depth Anything," where a diffusion model, trained on images with ground truth depth, can infer depth from new RGB images <a class="yt-timestamp" data-t="00:42:12">[00:42:12]</a>.
*   **Importance**: Unlike RGB images, depth and normal maps explicitly encode geometric information, providing crucial guidance for 3D reconstruction <a class="yt-timestamp" data-t="00:35:13">[00:35:13]</a>. The learned 3D normal texture can then be exported with the mesh to support various graphics rendering pipelines, leading to "extra crispy" meshes <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>.

### Architecture and Training
MeshFormer's architecture is primarily a 3D U-Net that integrates a Transformer at its bottleneck <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>.
*   **U-Net**: A U-Net starts with high-resolution input, decreases resolution while increasing feature dimension in its "downsampling" path (encoder), processes information at a bottleneck, and then increases resolution back in its "upsampling" path (decoder) <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.
*   **3D Sparse Voxels**: Instead of a triplane representation, MeshFormer uses 3D sparse voxels <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. Voxels are small cubes that discretize a 3D volume, with associated feature vectors <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. Sparse voxels mean computation is only done for occupied space, not empty space, improving efficiency <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>.
*   **Projection-Aware Cross-Attention**: The model performs cross-attention between voxel features and projected 2D patch features (from RGB and normal images) <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>. "Projection aware" means the model understands the camera's view of the object (e.g., front, back) <a class="yt-timestamp" data-t="00:22:49">[00:22:49]</a>. This requires knowing the exact camera pose for each view, which can be a limitation for arbitrary real-world images <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>.
*   **2D Encoder**: RGB and normal images are processed by a 2D feature extractor, such as a trainable DINOv2 model, to generate multiview patch features <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>. This DINOv2 model, as well as the normal map diffusion model, are pre-trained components <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>.
*   **Output**: The U-Net outputs features that are then passed through small multi-layer perceptrons (MLPs) to estimate:
    *   **Normals**: The surface normals <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.
    *   **Color**: The color of the surface <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.
    *   **Signed Distance Function (SDF)**: A function that tells you the distance to the object's surface (zero on surface, positive outside, negative inside) <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>. The SDF represents the geometry of the surface <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.
*   **Mesh Extraction**: A technique like the **Marching Cubes Algorithm** is used to convert the SDF into an explicit mesh representation <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>. This algorithm divides space into cubes and "marches" along boundaries to define the surface <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.
*   **Training Strategy**: MeshFormer emphasizes a unified, single-stage training strategy for its core pipeline <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. While the pipeline itself is trained end-to-end, it leverages pre-trained models (like the normal map diffusion model and DINOv2) <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.

## Mesh Anything: Direct Mesh Generation with Good Topology

Mesh Anything focuses on generating "artist-created meshes," which are distinct from scanned meshes (e.g., from photogrammetry) <a class="yt-timestamp" data-t="00:36:37">[00:36:37]</a>.

*   **Importance of Topology**: Artist-created meshes have "good topology," meaning their vertex and edge arrangement is clean and organized, allowing for easier animation and texturing <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>. Scanned meshes often have chaotic topology with artifacts, making them harder to work with in 3D pipelines <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.
*   **Industry Relevance**: The current 3D industry predominantly relies on mesh-based pipelines due to their efficiency and controllability <a class="yt-timestamp" data-t="00:38:58">[00:38:58]</a>. While many generative AI methods produce alternative 3D representations (like Nerfs or SDFs), these need to be converted to meshes for use in game engines or CGI tools, often resulting in poor topology <a class="yt-timestamp" data-t="00:39:29">[00:39:29]</a>. Generating meshes with good topology directly solves this problem <a class="yt-timestamp" data-t="00:40:17">[00:40:17]</a>.

### Methodology: VQ-VAE and Autoregressive Transformer
Mesh Anything uses a Vector Quantized Variational Autoencoder (VQ-VAE) to learn a "mesh vocabulary" <a class="yt-timestamp" data-t="00:44:27">[00:44:27]</a>.
*   **VQ-VAE**: A VQ-VAE discretizes continuous data (like images or 3D shapes) into a finite vocabulary of tokens <a class="yt-timestamp" data-t="00:45:06">[00:45:06]</a>. An encoder maps input to a latent space, and then vectors are "quantized" by finding the nearest neighbor in a learned codebook (vocabulary) <a class="yt-timestamp" data-t="00:47:25">[00:47:25]</a>. A decoder reconstructs the original input from these quantized tokens <a class="yt-timestamp" data-t="00:48:10">[00:48:10]</a>.
*   **Mesh Vocabulary**: Mesh Anything trains a VQ-VAE on 3D data (e.g., Objaverse and ShapeNet datasets) to create a codebook of 3D "shape tokens" <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>.
*   **Autoregressive Generation**: A decoder-only Transformer (like an LLM) then generates meshes by outputting sequences of these discrete shape tokens, effectively "building the mesh piece by piece" <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>. This is in contrast to methods that generate a continuous 3D representation and then extract a mesh <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a>.
*   **Data Augmentation**: A "noise-resistant decoder" is employed, aided by a data augmentation technique where artist-created meshes are intentionally corrupted <a class="yt-timestamp" data-t="00:58:28">[00:58:28]</a>. The model learns to map these corrupted inputs back to their high-quality, good-topology counterparts, making the Transformer more robust and better at understanding topology <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>.

This approach suggests that directly generating meshes with controlled topology might be more practical than relying on alternative 3D representations that require complex conversion steps <a class="yt-timestamp" data-t="00:54:31">[00:54:31]</a>.

## JPEG-LM: LLMs Generating Images from Codec Representations

JPEG-LM takes the concept of autoregressive generation of tokens even further by generating images and videos using "canonical codec representations" <a class="yt-timestamp" data-t="01:00:41">[01:00:41]</a>.

*   **Direct Codec Generation**: Instead of generating images in pixel space or a learned latent space (like VQ-VAE tokens), JPEG-LM literally generates the raw, compressed data (e.g., JPEG bytes) that represent the image when saved on a computer <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>.
    *   A JPEG file is a compressed representation that is more efficient than storing raw pixel data <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>.
    *   The model predicts this sequence of bytes (tokens) one by one <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>.
*   **No Vision-Specific Modifications**: A notable aspect is that JPEG-LM uses conventional LLM architectures (e.g., Llama 2) without any [[convolutional_neural_networks_and_visual_systems | vision-specific modifications]] like convolutions or 2D positional embeddings <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a>. This aims to maximize the model's generality and proves that a generic language model can handle this task <a class="yt-timestamp" data-t="01:08:07">[01:08:07]</a>.
*   **Comparison to VQ-VAE**: The paper directly compares generating images from JPEG codec tokens versus VQ-VAE tokens <a class="yt-timestamp" data-t="01:06:26">[01:06:26]</a>.
    *   Both are lossy compression methods <a class="yt-timestamp" data-t="01:10:01">[01:10:01]</a>.
    *   JPEG encoding, being a handcrafted method designed for human perception, often preserves detail in critical areas like human faces and text characters better than VQ-VAE, which might prioritize color and sharpness preservation <a class="yt-timestamp" data-t="01:11:53">[01:11:53]</a>.
    *   JPEG-LM consistently outperforms the VQ Transformer in their experiments <a class="yt-timestamp" data-t="01:14:04">[01:14:04]</a>.
*   **Implications**: This work unifies the paradigms of language and visual generation <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>. It's considered groundbreaking because previous research largely avoided this direct codec generation approach due to perceived challenges, making it "a stupid idea that works" <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>. It opens the door to generating any type of file (e.g., 3D file formats like STL or USD) directly by an LLM, byte by byte <a class="yt-timestamp" data-t="01:12:52">[01:12:52]</a>.

## Conclusion and Future Outlook

The three papers present a fascinating progression in generative [[computer vision adversarial attacks | computer vision]].

*   MeshFormer leverages the power of pre-trained [[vision language models with pretrained components | 2D diffusion models]] to extract additional geometric signals (normal maps) from RGB images, leading to higher-quality 3D mesh reconstruction through an SDF-based approach with Marching Cubes <a class="yt-timestamp" data-t="01:23:57">[01:23:57]</a>.
*   Mesh Anything proposes a radical shift: instead of extracting meshes from continuous 3D representations, it directly generates meshes token by token using an autoregressive Transformer, ensuring good topology by incorporating a noise-resistant decoder and specialized data augmentation <a class="yt-timestamp" data-t="01:24:25">[01:24:25]</a>. This raises the question of whether meshes will continue to be the standard 3D representation due to the immense momentum and tooling built around them <a class="yt-timestamp" data-t="01:25:42">[01:25:42]</a>.
*   JPEG-LM pushes the boundary even further by demonstrating that generic LLMs can generate images and videos by directly predicting the byte sequence of their compressed file formats (like JPEG or AVC h264) <a class="yt-timestamp" data-t="01:26:38">[01:26:38]</a>. This approach bypasses the need for specialized [[comparison of vision architectures | vision architectures]] or learned visual vocabularies, simplifying the pipeline and hinting at a future where generative models directly output digital files <a class="yt-timestamp" data-t="01:26:48">[01:26:48]</a>.

These papers collectively challenge existing paradigms in generative AI, particularly in the realm of 3D content, and suggest that the future might involve more direct, token-based generation of digital assets using increasingly generalized models.