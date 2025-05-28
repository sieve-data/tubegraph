---
title: Generative AI for highquality meshes
videoId: SkvyrgSzigo
---

From: [[hu-po]] <br/> 

Recent advancements in generative AI are pushing the boundaries of 3D content creation, specifically in the generation of high-quality meshes. This area is seeing a shift towards techniques that not only produce realistic 3D models but also ensure "good topology," which is crucial for integration into existing 3D pipelines like game engines and CGI tools <a class="yt-timestamp" data-t="00:38:51">[00:38:51]</a>.

## Approaches to Mesh Generation

Three notable papers illustrate different strategies in this domain:

### MeshFormer: Leveraging Diffusion Models for Enhanced Detail

**MeshFormer** is a model that reconstructs high-quality [[3d_mesh_generation_with_ai | 3D textured meshes]] from a sparse set of multi-view RGB images and their corresponding normal maps <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Released in August 2024, this paper from UC San Diego, UCLA, and HBot Inc. stands out for its unique input <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

*   **Input**: Six sparse multi-view RGB images and their respective [[Data Generation for AI Models | normal maps]] <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **Normal Maps**: A key innovation is the use of normal maps, which are images where each pixel's color represents the direction of the normal vector perpendicular to a surface <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. These provide crucial geometric information that enhances the 3D effect of the generated meshes, making them "crispier" <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>, <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.
*   **Generation of Normal Maps**: Historically, obtaining normal maps for arbitrary images was challenging <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. MeshFormer addresses this by leveraging pre-trained 2D [[advancements_in_3d_generative_models_using_neural_networks | diffusion models]] capable of generating high-quality normal maps from any RGB image <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>, <a class="yt-timestamp" data-t="00:35:19">[00:35:19]</a>.
*   **Architecture**: It uses a 3D U-Net architecture with a Transformer integrated at the bottleneck <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. The model explicitly leverages 3D structure and projective bias, utilizing sparse voxels for efficient computation <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>, <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>. Cross-attention mechanisms combine features from RGB and normal map inputs <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
*   **Output**: The model estimates surface normals, color, and a Signed Distance Function (SDF) <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>. The SDF, which indicates the distance to the object's surface, is then converted into a mesh using a [[Evaluation of 3D Generative Techniques | marching cubes algorithm]] <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>, <a class="yt-timestamp" data-t="00:31:11">[00:31:11]</a>.
*   **Limitations**: Requires precise camera pose information for input images, limiting its use with arbitrary real-world multi-view datasets <a class="yt-timestamp" data-t="00:27:53">[00:27:53]</a>. It also relies on a limited amount of 3D data for training, which is a common challenge in the field <a class="yt-timestamp" data-t="00:33:06">[00:33:06]</a>.

### Mesh Anything: Generating Meshes with Artist-like Topology

**Mesh Anything**, released in June 2024, focuses on generating "artist-created meshes" – meshes with good topology that are suitable for animation and editing <a class="yt-timestamp" data-t="00:36:58">[00:36:58]</a>, <a class="yt-timestamp" data-t="00:40:17">[00:40:17]</a>. This contrasts with meshes generated from photogrammetry or marching cubes, which often have disorganized topology and artifacts <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>, <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>.

*   **Motivation**: The current 3D industry heavily relies on mesh-based pipelines due to their efficiency and controllability, but many generative 3D methods produce alternative representations (like NeRFs or GaSplat) that need conversion to meshes, often resulting in poor topology <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>, <a class="yt-timestamp" data-t="00:52:46">[00:52:46]</a>.
*   **Approach**: Instead of producing an implicit 3D representation and then converting it, Mesh Anything directly generates the mesh token-by-token using an auto-regressive Transformer <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a>, <a class="yt-timestamp" data-t="00:56:03">[00:56:03]</a>.
*   **Mesh Vocabulary**: It uses a Vector Quantized Variational Autoencoder (VQ-VAE) to learn a "mesh vocabulary" <a class="yt-timestamp" data-t="00:48:27">[00:48:27]</a>. The VQ-VAE discretizes continuous 3D shapes into a limited set of tokens, similar to how language models have a vocabulary of words <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>, <a class="yt-timestamp" data-t="00:49:03">[00:49:03]</a>.
*   **Training and Data Augmentation**: The Transformer is trained to output these shape tokens sequentially. A clever data augmentation technique involves intentionally corrupting the topology of artist-created meshes during training <a class="yt-timestamp" data-t="00:43:16">[00:43:16]</a>. This makes the decoder more robust to noisy token sequences and encourages it to produce higher quality topology in the final mesh <a class="yt-timestamp" data-t="00:58:56">[00:58:56]</a>.
*   **Input**: The model starts from a point cloud (e.g., from a LiDAR scan or photogrammetry) and encodes it into features before generating the mesh <a class="yt-timestamp" data-t="00:56:19">[00:56:19]</a>.

### JPEG LM: LLMs Generating Raw Compressed Data

**JPEG LM**, released in August 2024 by University of Washington and Meta AI Research, explores a radical idea: training [[Generative Latent Spaces in AI | LLMs]] to directly generate images and videos by modeling them as compressed files (e.g., JPEG or H.264) <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>, <a class="yt-timestamp" data-t="01:00:41">[01:00:41]</a>.

*   **Novelty**: Instead of generating pixels or learned latent representations (like VQ-VAE tokens), the LLM outputs the raw bytes of a compressed image file token by token <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a>, <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>. This approach was considered "stupid" but works <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.
*   **Architecture**: It uses conventional LLM architectures (e.g., a 7B Llama 2 model) without any vision-specific modifications like convolutions or 2D positional embeddings, maximizing generality <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a>, <a class="yt-timestamp" data-t="01:09:08">[01:09:08]</a>.
*   **Implications**: This method suggests a new way to unify language and visual generation, demonstrating that a simple auto-regressive model can learn the complex, highly structured patterns of compressed data <a class="yt-timestamp" data-t="01:13:58">[01:13:58]</a>, <a class="yt-timestamp" data-t="01:16:32">[01:16:32]</a>.
*   **Comparison to VQ-VAE**: JPEG LM shows that direct JPEG encoding preserves more detail in highly perceptible elements like faces and text compared to VQ-VAE encoding, which tends to preserve color and sharpness better <a class="yt-timestamp" data-t="01:11:53">[01:11:53]</a>.
*   **[[Future potential and direction for generative 3D technology | Future Potential]]**: This approach could be extended to directly generate 3D file formats (like STL or USD) token by token <a class="yt-timestamp" data-t="01:12:49">[01:12:49]</a>, <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>, potentially bypassing intermediate representations and generating ready-to-use assets for existing 3D software.

## Discussion: The Future of 3D Representations

These papers present a fascinating dilemma regarding the [[Future potential and direction for generative 3D technology | future of 3D generative technology]]:

*   **MeshFormer** exemplifies how enhancing existing mesh generation pipelines with additional learned information (like normal maps from [[Advancements in 3D Generative Models Using Neural Networks | diffusion models]]) can significantly improve quality.
*   **Mesh Anything** champions the importance of "good topology" in meshes, suggesting that if AI can generate meshes with artist-like quality, the industry can continue to leverage its massive investment in mesh-based tools and animation pipelines without refactoring everything for new representations like NeRFs or Gaussian Splats <a class="yt-timestamp" data-t="00:53:51">[00:53:51]</a>.
*   **JPEG LM** introduces a disruptive paradigm by showing that LLMs can directly generate highly structured data formats, opening the door for direct generation of 3D file formats, which could eliminate the need for intermediate 3D representations altogether <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>.

The question remains whether the industry will adapt to new, perhaps more "deep learning-friendly" 3D representations, or if the strong momentum and existing infrastructure around meshes will lead to more advanced AI techniques for generating meshes directly <a class="yt-timestamp" data-t="00:54:33">[00:54:33]</a>. The ability to directly generate standard 3D formats with good topology would integrate seamlessly into current workflows, potentially making alternative representations an "oddity" <a class="yt-timestamp" data-t="00:55:15">[00:55:15]</a>.