---
title: Techniques for text to 3D conversion involving diffusion models
videoId: l956ye13F8M
---

From: [[hu-po]] <br/> 

[[text_to_3d_model_conversion_process | Text to 3D model conversion process]] is a rapidly evolving field, with recent advancements largely leveraging [[diffusion_models_and_image_generation | diffusion models]] to generate three-dimensional (3D) content from text prompts <a class="yt-timestamp" data-t="03:47:50">[03:47:50]</a>. This area has seen significant progress, particularly with the emergence of Gaussian Splatting as a novel 3D representation <a class="yt-timestamp" data-t="04:40:41">[04:40:41]</a>.

## Evolution of 3D Representations

Traditionally, 3D objects in video games and CGI were represented using a combination of a mesh and a texture <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.
*   A **Mesh** is a 3D model composed of vertices (dots) and polygons (triangles) that form a surface <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.
*   A **Texture** is a 2D image wrapped onto the mesh to color the 3D object <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>. This method, while prevalent, can be complex to work with, especially when modifications are needed <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>.

More recently, **Neural Radiance Fields (Nerfs)** gained popularity <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>. Nerfs implicitly store 3D objects within the weights of a neural network <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>. While innovative, Nerfs are "per-sample" (meaning a new neural network must be trained for each object) <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>, making them slow for new content generation <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>.

A new technique called **Gaussian Splatting** has recently emerged as a significant advancement <a class="yt-timestamp" data-t="04:40:41">[04:40:41]</a>.
*   Gaussian Splatting represents a 3D scene using millions of small, explicit particles called 3D gaussians <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>.
*   Each 3D gaussian has a position, orientation, scale, opacity, and view-dependent color <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.
*   These representations are significantly faster to render and are explicit, meaning parts of the 3D object can be easily manipulated or removed <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>. This explicitness is seen as a major advantage over implicit Nerfs <a class="yt-timestamp" data-t="41:37:00">[41:37:00]</a>.

## Recent Advancements in Text to 3D

Two extremely fresh papers, "DreamGaussian" and "Text to 3D Using Gaussian Splatting (GSGen)", both released on September 28, 2023, apply Gaussian Splatting to the text to 3D problem <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.

### Common Techniques

Both papers employ a **multi-stage optimization process** <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>, similar to pre-training and fine-tuning in large language models <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>. They typically involve:
1.  **Geometry Optimization Stage**: Establishing a coarse 3D representation <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>.
2.  **Appearance Refinement Stage**: Iteratively improving fine-grained details and fidelity <a class="yt-timestamp" data-t="18:48:00">[18:48:00]</a>.

A core component in both approaches is **Score Distillation Sampling (SDS)** <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>. This technique, originally from the "DreamFusion" paper <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>, optimizes a 3D representation by leveraging a pre-trained 2D [[text_to_image_generation_with_diffusion_transformers | image diffusion model]] <a class="yt-timestamp" data-t="47:31:00">[47:31:00]</a>. The model computes a "score estimation function" to guide the gradient update, iteratively refining the 3D object to ensure that rendered 2D images from various viewpoints closely resemble plausible samples from the diffusion model <a class="yt-timestamp" data-t="48:42:00">[48:42:00]</a>. This process involves conditioning the [[diffusion_models_and_image_generation | diffusion model]] on camera parameters (rotation and translation) to generate viewpoint-specific images <a class="yt-timestamp" data-t="27:49:00">[27:49:00]</a>.

Both papers use **densification and pruning** to refine the gaussian distribution <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>. This involves adding more gaussians in dense areas and removing those in empty space, enhancing continuity and improving fidelity <a class="yt-timestamp" data-t="20:13:00">[20:13:00]</a>.

### DreamGaussian's Approach

*   **Initialization**: DreamGaussian initializes the 3D gaussians from an amorphous cloud of gray points within a sphere <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>. These gaussians have 0.01 opacity and a gray color <a class="yt-timestamp" data-t="01:20:01">[01:20:01]</a>.
*   **Multi-Stage Pipeline**: It employs a two-stage process: generative gaussian splatting followed by mesh extraction and texture refinement <a class="yt-timestamp" data-t="58:04:00">[58:04:00]</a>.
*   **Mesh Extraction and Texture Refinement**: A unique aspect of DreamGaussian is its ability to convert the generated Gaussian Splat into a textured mesh, enabling compatibility with existing game engines and CGI pipelines like Blender <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>. This is achieved by dividing the 3D space into blocks and using the marching cubes algorithm <a class="yt-timestamp" data-t="01:05:32">[01:05:32]</a>. The texture refinement occurs in "UV space" using [[diffusion_models_and_image_generation | stable diffusion]] <a class="yt-timestamp" data-t="01:08:22">[01:08:22]</a>.
*   **Performance**: DreamGaussian can produce high-quality textured meshes in just two minutes on a single Nvidia V100 GPU (16 GB memory), and even with 8 GB of GPU memory, making it accessible for consumer hardware <a class="yt-timestamp" data-t="01:03:02">[01:03:02]</a>. This represents approximately a 10x acceleration compared to existing methods <a class="yt-timestamp" data-t="01:27:27">[01:27:27]</a>.

### GSGen's Approach

*   **Initialization**: GSGen utilizes Point-E to initialize the positions of the gaussians, feeding the text prompt into Point-E to generate an initial 3D point cloud <a class="yt-timestamp" data-t="01:19:17">[01:19:17]</a>. This provides a stronger geometric prior than a simple sphere <a class="yt-timestamp" data-t="01:18:38">[01:18:38]</a>. Although Point-E can produce colored point clouds, GSGen opts for random color initialization as Point-E generates relatively simple color patterns <a class="yt-timestamp" data-t="01:19:26">[01:19:26]</a>.
*   **Multi-Stage Pipeline**: GSGen follows a geometry optimization stage (using a 3D point cloud diffusion prior and the standard 2D SDS loss) and an iterative appearance refinement stage (densification and pruning) <a class="yt-timestamp" data-t="01:37:40">[01:37:40]</a>.
*   **Refinement**: Unlike DreamGaussian, GSGen performs refinement directly within the 3D Gaussian Splatting representation <a class="yt-timestamp" data-t="01:08:55">[01:08:55]</a>. It uses a "compactness-based densification" method, adding gaussians based on the distance to their K-nearest neighbors <a class="yt-timestamp" data-t="01:14:31">[01:14:31]</a>.
*   **Performance**: GSGen achieves high visual quality, especially in high-frequency details like textures, which contrasts with the overly smooth geometry often produced by mesh-based methods <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

### Challenges and Limitations

Both methods face challenges inherent to text to 3D generation:
*   **Janus Problem**: This refers to the tendency of [[diffusion_models_and_image_generation | diffusion models]], which are often trained on 2D images with a frontal bias, to generate 3D objects with multiple "faces" or inconsistent geometry from different viewpoints <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. While incorporating a 3D prior mitigates this, it doesn't entirely eliminate it <a class="yt-timestamp" data-t="01:13:13">[01:13:13]</a>.
*   **Baked Lighting**: Current methods often use a "simple diffuse color" for gaussians, meaning the color is not view-dependent <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. This results in "baked lighting," where the lighting cannot be changed after generation <a class="yt-timestamp" data-t="01:43:35">[01:43:35]</a>.
*   **Complex Prompts**: Generating satisfactory results with complex text prompts or complicated logic remains a limitation, primarily due to the limited language understanding of models like Point-E and the CLIP text encoder <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>.

### Comparative Analysis of Approaches

*   **Priors**: GSGen's use of Point-E as a 3D prior is considered more sophisticated than DreamGaussian's simple gray sphere initialization, leading to better initial geometry, especially for asymmetric scenes <a class="yt-timestamp" data-t="01:19:26">[01:19:26]</a>.
*   **Refinement Space**: GSGen's direct refinement in the Gaussian Splat space generally yields finer, more intricate details and avoids the smoothing effect seen in mesh-based refinement <a class="yt-timestamp" data-t="01:08:55">[01:08:55]</a>. DreamGaussian's conversion to a mesh for refinement may introduce issues like overly smooth geometry <a class="yt-timestamp" data-t="01:30:07">[01:30:07]</a>.
*   **Usability**: DreamGaussian's focus on outputting textured meshes makes its results immediately compatible with existing 3D tools and game engines <a class="yt-timestamp" data-t="01:04:02">[01:04:02]</a>.
*   **Hyperparameters**: Both approaches still rely on hard-coded thresholds and hyperparameters for their densification and pruning strategies, indicating room for further optimization <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>.

## [[Future potential of 3D diffusion models | Future Potential]]

The speed and explicitness of Gaussian Splatting position it as a strong candidate to become the standard 3D representation, potentially superseding meshes and textures <a class="yt-timestamp" data-t="01:03:57">[01:03:57]</a>. The ability to directly manipulate individual gaussians, for example, by removing specific parts of a scene, offers significant advantages <a class="yt-timestamp" data-t="01:04:26">[01:04:26]</a>. Rapid developments are already integrating Gaussian Splatting into real-time applications like augmented reality (AR) and virtual reality (VR) environments, where explicit, high-fidelity, and fast-rendering 3D representations are crucial <a class="yt-timestamp" data-t="01:57:35">[01:57:35]</a>.