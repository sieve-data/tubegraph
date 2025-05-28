---
title: MeshFormer and MeshAnything comparison
videoId: SkvyrgSzigo
---

From: [[hu-po]] <br/> 

This article dives into three technical papers focusing on advanced computer vision techniques for 3D object generation, particularly contrasting two distinct approaches to mesh creation: MeshFormer and MeshAnything, and linking them to the innovative JPEG LM. The discussion explores the detailed mechanics, advantages, and implications of each method for the future of 3D representation and industry pipelines <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## MeshFormer: High-Quality 3D Textured Mesh Generation

Released on August 19, 2024, by UC San Diego, UCLA, and HBot Inc., MeshFormer focuses on generating high-quality 3D textured meshes <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Input and Core Concept
MeshFormer takes a sparse set of six multiview RGB images and their corresponding normal maps as input <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Textured Mesh**: A textured mesh consists of vertices representing a 3D object, with an image (texture) wrapped around it via a specific mapping <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Multiview RGB Images**: The model requires multiple RGB images from different viewpoints (e.g., front, back, top, sides) to understand the object <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. "Sparse view" indicates that only a few views (e.g., six) are needed <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Normal Maps**: The key insight of MeshFormer is the use of normal maps as input <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. A normal map is an image where each pixel's color represents the direction of the normal vector (perpendicular to a surface) at that point <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Normal maps enhance the 3D effect in rendering by allowing better calculation of light interaction with the object <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
    *   **Generation of Normal Maps**: Historically, obtaining normal maps for arbitrary images was challenging. MeshFormer leverages recent advancements in 2D diffusion models, which can generate high-quality normal maps from RGB images, even for complex scenes like indoor environments or cityscapes <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. These diffusion models, often trained on billions of natural images, embed extensive priors for geometric information <a class="yt-timestamp" data-t="00:35:19">[00:35:19]</a>.

### Architecture and Process
MeshFormer utilizes a 3D U-Net architecture, integrating a Transformer at the bottleneck <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>.
*   **3D U-Net**: It processes a high resolution of voxels (3D pixels) which then decrease in resolution towards the bottleneck while increasing feature dimension, and then scales back up <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.
*   **Sparse Voxels**: To manage computational expense, the model converts the feature volume into a sparse feature volume by using an occupancy volume to remove empty space, focusing computation only on relevant areas <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.
*   **Projection-Aware Cross-Attention**: The U-Net iteratively performs cross-attention between voxel features and 2D pixel features (from RGB and normal maps), allowing the model to be aware of the camera view <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>.
*   **Output**: The model outputs estimates for normals, color, and Signed Distance Function (SDF) <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>.
    *   **Signed Distance Function (SDF)**: An SDF defines a surface by assigning a value to every point in space, indicating its distance to the surface (zero on the surface, positive outside, negative inside) <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.
    *   **Marching Cubes**: The SDF is then converted into a final 3D mesh using a "marching cubes" algorithm, an older computer vision technique for surface extraction <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>.

### Contributions and Limitations
*   **High-Quality Output**: Generates 3D textured meshes with fine-grained geometric details in seconds <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. The learned 3D normal texture can be exported with the mesh for various graphics rendering pipelines, enhancing visual quality <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>.
*   **Unified Training (Claim)**: The paper claims a "unified single-stage training strategy" <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>, but this is debatable as it relies on pre-trained 2D diffusion models and a pre-trained DINOv2 encoder <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.
*   **Reliance on Camera Pose**: A drawback is the requirement for explicit camera positions for each multiview image, which is often unavailable in real-world scenarios <a class="yt-timestamp" data-t="00:27:55">[00:27:55]</a>.
*   **Data Scale**: The paper notes that existing 3D datasets (like Objaverse and ShapeNet used by MeshFormer) are insufficient for learning extensive priors compared to vast 2D image datasets <a class="yt-timestamp" data-t="00:34:58">[00:34:58]</a>. This highlights why integrating signal from diffusion models (trained on massive 2D data) is beneficial <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>.

## MeshAnything: Artist-Created Mesh Generation with Autoregressive Transformers

Released on June 14, 2024, MeshAnything introduces a different approach: generating "artist-created meshes" with autoregressive Transformers <a class="yt-timestamp" data-t="00:36:32">[00:36:32]</a>.

### Focus on Topology
MeshAnything specifically aims to create meshes with "good topology," a characteristic of meshes created by human artists <a class="yt-timestamp" data-t="00:37:18">[00:37:18]</a>.
*   **Good Topology**: Refers to a mesh structure with clean contour lines that facilitate animation and texturing, unlike meshes generated from photogrammetry which often have irregular artifacts <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>.
*   **Industry Relevance**: The current 3D industry heavily relies on mesh-based pipelines due to their efficiency and controllability. Tools like [[comparison_between_unity_and_unreal_engine | Unreal Engine]] and [[comparison_between_unity_and_unreal_engine | Unity]] natively work with meshes <a class="yt-timestamp" data-t="00:38:58">[00:38:58]</a>.
*   **Challenge with Alternative Representations**: Many generative AI techniques for 3D (e.g., Nerfs, Gaussian Splats, SDFs) output alternative 3D representations that need to be converted to meshes using methods like marching cubes. This conversion often results in meshes with poor, dense, and inefficient topology, making them difficult to use in existing 3D pipelines without further "remeshing" or "retopologizing" <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>. Remeshing can still fail to capture sharp edges and flat surfaces <a class="yt-timestamp" data-t="00:40:46">[00:40:46]</a>.

### Methodology: Token-Based Generation
MeshAnything directly generates meshes token by token using an autoregressive Transformer <a class="yt-timestamp" data-t="00:50:46">[00:50:46]</a>.
*   **VQ-VAE for Mesh Vocabulary**: They train a Vector Quantized Variational Autoencoder (VQ-VAE) to learn a "mesh vocabulary" or "shape tokens" <a class="yt-timestamp" data-t="00:48:27">[00:48:27]</a>.
    *   A VQ-VAE discretizes continuous data (here, 3D meshes) into a finite vocabulary of tokens. An encoder maps an input to a latent space, and then the closest token from a learned codebook is selected, which a decoder then uses to reconstruct the original input <a class="yt-timestamp" data-t="00:44:27">[00:44:27]</a>.
*   **Autoregressive Transformer**: A decoder-only Transformer takes a point cloud (e.g., from a LiDAR scanner or photogrammetry) as input, encodes it into shape features, which are then projected into the mesh token space <a class="yt-timestamp" data-t="00:56:19">[00:56:19]</a>. The Transformer then generates a sequence of these shape tokens, and the VQ-VAE decoder converts this sequence back into a mesh <a class="yt-timestamp" data-t="00:49:07">[00:49:07]</a>.
*   **Noise-Resistant Decoder**: A unique data augmentation technique involves intentionally corrupting the topology of artist-created meshes and then training the model to reconstruct the original high-quality topology <a class="yt-timestamp" data-t="00:43:16">[00:43:16]</a>. This makes the Transformer more robust to noisy token sequences and improves the quality of the generated topology <a class="yt-timestamp" data-t="00:58:28">[00:58:28]</a>.

## The JPEG LM Connection: Direct File Generation
The JPEG LM paper, released August 15, 2024, by University of Washington and Meta AI Research (FAIR), offers a paradigm-shifting approach that relates to MeshAnything's token-based generation <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.

### Canonical Codec Representations
JPEG LM directly models images and videos as compressed files saved on a computer via canonical codecs (like JPEG for images and AVC h264 for videos) <a class="yt-timestamp" data-t="01:00:41">[01:00:41]</a>.
*   **Direct Generation of Encoded Bytes**: Instead of generating images in pixel space or through a learned latent space (like VQ-VAE's tokens), JPEG LM trains an autoregressive LLM to literally generate the byte sequence of a compressed image file <a class="yt-timestamp" data-t="01:01:37">[01:01:37]</a>. This means the LLM generates the "weird text" that a computer sees when opening a JPEG file in a text editor <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>.
*   **No Vision-Specific Modifications**: Remarkably, this approach uses conventional LLM architectures without any vision-specific modifications like convolutions or 2D positional embeddings, maximizing generality <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a>.
*   **Comparison to VQ-VAE**: JPEG LM directly compared its method to VQ-VAE-based image generation <a class="yt-timestamp" data-t="01:06:26">[01:06:26]</a>. While both are lossy compression methods, JPEG (a human-designed codec) tends to preserve details in "highly perceptible elements like small human faces and text characters" better, while VQ-VAE has advantages in "color and sharpness preservation" <a class="yt-timestamp" data-t="01:11:55">[01:11:55]</a>.

### Implications for 3D Generation
The JPEG LM paper suggests a radical future for [[generative_ai_for_highquality_meshes | generative AI for high-quality meshes]] and [[3d_mesh_generation_with_ai | 3D mesh generation with AI]]. If an LLM can directly generate the byte sequence of a JPEG image, could it also directly generate the byte sequence of a 3D file format like an STL or Universal Scene Description (USD) file <a class="yt-timestamp" data-t="01:12:44">[01:12:44]</a>? This would eliminate the need for intermediary learned representations (like VQ-VAE tokens or SDFs) and their associated encoding/decoding processes.

## Conclusion: The Future of 3D Representation
The three papers present a fascinating [[comparative_analysis_of_model_architectures | comparative analysis of model architectures]] for 3D generation:
*   **MeshFormer** represents the bleeding edge of traditional multiview reconstruction, enhancing quality through the clever integration of diffusion-model-generated normal maps <a class="yt-timestamp" data-t="01:23:25">[01:23:25]</a>.
*   **MeshAnything** offers a new path for direct mesh generation by leveraging VQ-VAEs and autoregressive Transformers to prioritize "good topology," a critical factor for integration into existing 3D industry pipelines and animation workflows <a class="yt-timestamp" data-t="01:24:23">[01:24:23]</a>. This approach directly challenges the notion that meshes will be entirely replaced by other 3D representations like Nerfs or Gaussian Splats <a class="yt-timestamp" data-t="01:25:42">[01:25:42]</a>.
*   **JPEG LM** pushes the boundaries of "direct generation" by having LLMs create raw, compressed file data <a class="yt-timestamp" data-t="01:26:36">[01:26:36]</a>. This "stupid idea that works" <a class="yt-timestamp" data-t="01:14:17">[01:14:17]</a> could revolutionize how all digital assets are generated, by simply teaching models to produce the data structures that computers already understand.

This [[potential_future_of_meshbased_models_versus_gaussian_splats_in_virtual_environments | comparison between mesh-based models versus gaussian splats]] highlights a potential future where high-quality meshes with good topology remain a dominant 3D representation due to the immense momentum and established tools in the 3D industry <a class="yt-timestamp" data-t="00:54:55">[00:54:55]</a>. The ability to directly generate these meshes, potentially even at the raw file format level, could simplify workflows and accelerate content creation significantly.