---
title: 3D mesh generation with AI
videoId: SkvyrgSzigo
---

From: [[hu-po]] <br/> 

The field of [[3D mesh generation with AI | 3D mesh generation]] has seen significant advancements, leveraging artificial intelligence to create complex 3D objects. This article explores three notable papers that showcase different approaches and innovations in this domain: MeshFormer, Mesh Anything, and JpegLM <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## MeshFormer: High-Quality Mesh Generation with 3D-Guided Reconstruction Model

MeshFormer, a paper released on August 19, 2024, by UC San Diego, UCLA, and hbot Inc., focuses on [[Generative AI for highquality meshes | high-quality mesh generation]] through a 3D-guided reconstruction model <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Core Functionality and Inputs
MeshFormer reconstructs a high-quality 3D textured mesh from a sparse set of six multi-view RGB images and their corresponding normal maps <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. "Textured" means the mesh includes an image wrapped around its vertices to provide color and detail <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. Multi-view input, typically from different angles (front, back, top, sides), allows the model to understand the object's full form <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. The term "sparse view" indicates that only a small number of views (e.g., six) are needed, rather than hundreds <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

### The Role of Normal Maps
A key innovation in MeshFormer is the use of normal maps as input <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. A normal map is an image where each pixel's color represents the direction of the normal vector (perpendicular to a surface) at that point <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. These maps are crucial for obtaining a more 3D-like effect in rendering pipelines by informing how light rays interact with the object's surface <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

The ability to generate these normal maps from arbitrary RGB images is facilitated by [[advancements_in_3d_generative_models_using_neural_networks | 2D diffusion models]] <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. These diffusion models, like "Depth Anything," are trained on vast amounts of labeled data, allowing them to generalize well and produce accurate depth or normal maps for unseen images <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. The inclusion of this additional "intelligence" from depth and normal information significantly enhances the quality and detail of the generated meshes, especially when 3D datasets are limited <a class="yt-timestamp" data-t="00:34:07">[00:34:07]</a>.

### Architecture and Training
MeshFormer's architecture integrates a 3D U-Net with a Transformer at its bottleneck <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. It leverages 3D sparse convolutions and a projective bias to explicitly incorporate 3D structure <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. The process involves:
1.  **2D Feature Extraction**: Multi-view RGB and normal images are processed by a 2D feature extractor (e.g., DINOv2) to generate multi-view patch features <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>.
2.  **3D Voxel Processing**: Each 3D voxel is projected into the multiple views to interpolate RGB and normal features <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>. Cross-attention is performed between voxel features and the projected 2D pixel features <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.
3.  **Sparse Feature Volume**: An initial coarse 3D occupancy volume helps in removing empty space, making computations more efficient by creating a sparse feature volume <a class="yt-timestamp" data-t="00:30:31">[00:30:31]</a>.
4.  **Output Generation**: The model predicts normals, color, and a Signed Distance Function (SDF) <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>. An SDF defines the distance to the surface of an object, with zero on the surface, positive outside, and negative inside <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.
5.  **Mesh Extraction**: The SDF is converted into a mesh using a marching cubes algorithm, a common technique for extracting surfaces from implicit functions <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>.
The model uses a unified, single-stage training strategy, though it relies on pre-trained 2D diffusion models for normal map generation <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.

### Limitations
A notable limitation is the requirement for precise camera pose information for multi-view inputs, which is often not available in real-world scenarios, making the approach better suited for simulated or controlled environments <a class="yt-timestamp" data-t="00:27:55">[00:27:55]</a>.

## Mesh Anything: Artist-Created Mesh Generation with Autoregressive Transformers

Mesh Anything, released on June 14, 2024, takes a different approach to [[Generative AI for highquality meshes | mesh generation]], focusing on producing "artist-created meshes" <a class="yt-timestamp" data-t="00:36:32">[00:36:32]</a>.

### The Importance of Topology
The core motivation for Mesh Anything is the desire for "good topology" in generated meshes <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>. Artist-created meshes, meticulously crafted by human digital artists, feature clean contour lines and well-organized polygons, which are essential for smooth animations, efficient texturing, and overall usability in traditional 3D pipelines <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>. This contrasts with meshes generated via photogrammetry (scanning real-world objects), which often have messy, irregular topology with artifacts <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.

The 3D industry predominantly relies on mesh-based pipelines due to their efficiency and controllability <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>. While many [[advancements_in_3d_generative_models_using_neural_networks | generative AI models]] output alternative 3D representations like Nerfs (Neural Radiance Fields) or SDFs, converting these to meshes via marching cubes often results in dense, inefficient meshes with poor topology <a class="yt-timestamp" data-t="00:39:20">[00:39:20]</a>. Even "remeshing" techniques fail to fully capture sharp edges and flat surfaces, highlighting the need for direct generation of well-topologized meshes <a class="yt-timestamp" data-t="00:40:46">[00:40:46]</a>.

### Token-by-Token Mesh Generation
Mesh Anything's key innovation is directly generating meshes token by token using an autoregressive Transformer <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a>. This contrasts with methods that produce an implicit 3D representation and then convert it. The process involves:
1.  **Mesh Vocabulary Learning**: They use a [[generative_latent_spaces_in_ai | Vector Quantized Variational Autoencoder]] (VQ-VAE) to learn a "mesh vocabulary" or "shape tokens" from existing artist-created meshes (like those in the Objaverse and ShapeNet datasets) <a class="yt-timestamp" data-t="00:48:27">[00:48:27]</a>. A VQ-VAE discretizes continuous images (or, in this case, 3D shapes) into a limited vocabulary of tokens, allowing for a learnable, discrete representation <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>.
2.  **Transformer Generation**: A decoder-only Transformer is trained to generate sequences of these learned shape tokens <a class="yt-timestamp" data-t="00:50:05">[00:50:05]</a>. Given a point cloud input, it encodes them into features and then generates the mesh token sequence <a class="yt-timestamp" data-t="00:56:19">[00:56:19]</a>.
3.  **Decoding to Mesh**: The VQ-VAE's decoder then converts the generated token sequence back into a full 3D mesh <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>.

### Data Augmentation for Robustness
A clever aspect of Mesh Anything is its data augmentation strategy. By intentionally corrupting the shape quality of artist meshes (e.g., reordering points) and using these "shitty meshes" as input, they train a "noise-resistant decoder" <a class="yt-timestamp" data-t="00:58:28">[00:58:28]</a>. This teaches the Transformer to understand and recover good topology even from low-quality token sequences, leading to higher-quality outputs <a class="yt-timestamp" data-t="00:59:01">[00:59:01]</a>.

This approach suggests that meshes might continue to be the standard 3D representation due to the significant accumulated momentum and investment in existing 3D tools and pipelines that rely on them <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.

## JpegLM: LLMs as Image Generators with Canonical Codec Representations

JpegLM, a paper released on August 15, 2024, by the University of Washington and Meta AI (FAIR), extends the concept of token-by-token generation to images and videos <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>. While not directly about [[3D mesh generation with AI | 3D mesh generation]], it provides a fundamental insight into how LLMs can directly generate complex data formats.

### Generating Compressed Files Directly
JpegLM's radical idea is to directly model and generate images and videos as compressed files saved on a computer via canonical codecs like JPEG for images or H.264 for videos <a class="yt-timestamp" data-t="01:00:44">[01:00:44]</a>. Instead of generating pixels or features in a latent space, the LLM literally generates the raw binary (or textual) data of the compressed file <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>. For example, when you open a JPEG file in a text editor, it appears as "weird text" or a "bunch of weird tokens" <a class="yt-timestamp" data-t="01:01:23">[01:01:23]</a>; JpegLM's LLM generates this exact sequence of tokens <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>.

### Advantages and Implications
This approach is particularly challenging because the generated token sequence must be "perfect" for the image to decode correctly <a class="yt-timestamp" data-t="01:03:04">[01:03:04]</a>. The model uses conventional LLM architectures (like a 7B Llama 2 model) without any vision-specific modifications (e.g., no convolutions, no 2D positional embeddings), maximizing the model's generality and proving a point about the raw power of LLMs <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a>.

A comparison with VQ-VAE-based generation reveals that while VQ-VAEs might preserve color and sharpness well, canonical codecs like JPEG, which are hand-designed and incorporate human intuition (e.g., prioritizing detail in faces), can be significantly better for highly perceptible elements like small human faces and text <a class="yt-timestamp" data-t="01:12:06">[01:12:06]</a>.

The profound implication of JpegLM is that it unifies the paradigms of language generation and visual generation <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>. It suggests that any digital file format, be it an image, video, or even a 3D mesh file (like an STL or USD), could potentially be generated directly, byte by byte or token by token, by an LLM <a class="yt-timestamp" data-t="01:12:52">[01:12:52]</a>. This opens up new avenues for [[data_generation_for_ai_models | data generation for AI models]] by circumventing the need for specialized encoders and decoders like VQ-VAEs for different modalities, relying instead on the inherent structure of existing digital formats <a class="yt-timestamp" data-t="01:15:40">[01:15:40]</a>.

## Conclusion

These three papers represent different facets of [[3D mesh generation with AI | 3D generative techniques]]. MeshFormer exemplifies the evolution of reconstruction models by incorporating external "intelligence" from [[motion_modeling_in_ai | 2D diffusion models]] to enhance detail <a class="yt-timestamp" data-t="01:17:30">[01:17:30]</a>. Mesh Anything explores the direct generation of meshes with "good topology" using [[generative_latent_spaces_in_ai | VQ-VAEs]] and Transformers, highlighting the continued relevance of meshes in established 3D pipelines and presenting solutions to [[challenges_and_limitations_in_3d_generation | challenges and limitations in 3D generation]] <a class="yt-timestamp" data-t="01:18:05">[01:18:05]</a>. JpegLM pushes the boundaries further by demonstrating that LLMs can directly generate the compressed raw data of images and videos, suggesting a future where AI models might generate complex digital assets by simply understanding and producing their underlying file formats <a class="yt-timestamp" data-t="01:18:36">[01:18:36]</a>. Together, they demonstrate the diverse and rapidly evolving landscape of AI in creating 3D content, from highly detailed models to directly generating entire digital files <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>.