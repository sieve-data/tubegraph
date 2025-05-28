---
title: 3D content generation using gaussian splatting
videoId: l956ye13F8M
---

From: [[hu-po]] <br/> 

3D content generation, particularly the process of transforming text descriptions into three-dimensional objects, is a rapidly evolving field in computer graphics and artificial intelligence <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. Recent advancements have seen the emergence of [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splatting]] as a highly efficient and effective method for representing and generating 3D objects, challenging older techniques like meshes and [[3D representation techniques Nerfs vs Gausssian Splats | Neural Radiance Fields (NeRFs)]] <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>, <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

## Traditional 3D Representation: Mesh and Texture

Historically, 3D objects in video games, CGI, and other applications have been represented using a combination of meshes and textures <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.
*   **Mesh**: A 3D model is represented as a collection of vertices (points) and polygons (often triangles) that define its surface <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.
*   **Texture**: A 2D image, known as a UV map or texture, is then "wrapped" onto this mesh to provide color and surface details <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>, <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.

This method has been the standard for a long time <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>, but it comes with complexities, especially when attempting to modify or generate new meshes, and requires dealing with issues like surface cleanliness and UV mapping <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>, <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.

## Neural Radiance Fields (NeRFs)

More recently, [[3D representation techniques Nerfs vs Gausssian Splats | Neural Radiance Fields (NeRFs)]] emerged as a new approach to 3D representation <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>. NeRFs implicitly store a 3D object within the weights of a neural network <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>. A trained NeRF can predict the color of every pixel from a given camera position and view, enabling novel view synthesis <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>. While exciting, NeRFs suffer from significant drawbacks:
*   **Per-Sample Optimization**: Each new object requires training a new neural network, which is very slow <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>, <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>.
*   **Implicit Representation**: The 3D object is not explicitly stored, making it difficult to edit, manipulate, or understand its structure <a class="yt-timestamp" data-t="41:47:00">[41:47:00]</a>.

## Gaussian Splatting: A New Paradigm

[[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splatting]] is a newer technique that has garnered significant attention due to its efficiency, quality, and simplicity <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>, <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>.
*   **Explicit Representation**: Unlike NeRFs, Gaussian Splatting explicitly represents a 3D scene as millions of individual 3D Gaussians (particles), similar to a point cloud <a class="yt-timestamp" data-t="08:05:00">[08:05:05]</a>, <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>, <a class="yt-timestamp" data-t="41:35:00">[41:35:00]</a>.
*   **Gaussian Parameters**: Each 3D Gaussian is defined by its:
    *   Position (3D coordinates) <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>
    *   Orientation (rotation) <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>, <a class="yt-timestamp" data-t="43:46:00">[43:46:00]</a>
    *   Scale (size/spread, defined by covariance) <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>, <a class="yt-timestamp" data-t="43:42:00">[43:42:00]</a>
    *   Opacity (how transparent it is) <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>, <a class="yt-timestamp" data-t="43:58:00">[43:58:00]</a>
    *   View-dependent color (RGB values) <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>, <a class="yt-timestamp" data-t="44:02:00">[44:02:00]</a>
*   **Rendering Process**: When rendering, these 3D Gaussians are projected onto the camera's imaging plane as 2D Gaussians <a class="yt-timestamp" data-t="37:09:00">[37:09:00]</a>, <a class="yt-timestamp" data-t="38:23:00">[38:23:00]</a>. The image plane is divided into tiles, and Gaussians within each tile are sorted (e.g., by depth) and blended to determine the final pixel colors <a class="yt-timestamp" data-t="38:42:00">[38:42:00]</a>, <a class="yt-timestamp" data-t="39:00:00">[39:00:00]</a>. This process is highly optimized for GPUs, enabling real-time rendering <a class="yt-timestamp" data-t="39:40:00">[39:40:00]</a>, <a class="yt-timestamp" data-t="40:40:00">[40:40:00]</a>.

The explicit nature of Gaussian Splatting allows for easier manipulation, such as deleting specific parts of a scene or copying and pasting objects, which is difficult with implicit representations like NeRFs <a class="yt-timestamp" data-t="42:23:00">[42:23:00]</a>, <a class="yt-timestamp" data-t="42:51:00">[42:51:00]</a>.

## Text-to-3D with Gaussian Splatting: DreamGaussian and GSGen

Two recent papers, DreamGaussian and Text-to-3D using Gaussian Splatting (GSGen), both released on September 28, 2023, address the problem of generating 3D content from text prompts using [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splatting]] <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>, <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. Both approaches employ a multi-stage optimization process <a class="yt-timestamp" data-t="10:10:00">[10:10:00]</a>, <a class="yt-timestamp" data-t="18:34:00">[18:34:00]</a>.

### Score Distillation Sampling (SDS)
A core technique used by both papers is [[3D modeling and tracking using Gaussian splatting | Score Distillation Sampling (SDS)]], originally proposed in the DreamFusion paper <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>, <a class="yt-timestamp" data-t="34:36:00">[34:36:00]</a>. SDS leverages a pre-trained 2D image diffusion model (like Stable Diffusion) to guide the 3D generation process <a class="yt-timestamp" data-t="37:31:00">[37:31:00]</a>. The 2D diffusion model, conditioned on camera parameters and text prompts, provides a "score estimation" (a gradient) that helps refine the 3D representation <a class="yt-timestamp" data-t="48:26:00">[48:26:00]</a>, <a class="yt-timestamp" data-t="51:10:00">[51:10:00]</a>.

A common challenge in text-to-3D generation, especially when relying on 2D diffusion models, is the **Janus problem** <a class="yt-timestamp" data-t="23:01:00">[23:01:00]</a>. This refers to the tendency of generated 3D objects to have inconsistent appearances from different viewpoints (e.g., a panda with multiple faces), because 2D diffusion models are often biased towards frontal views of objects <a class="yt-timestamp" data-t="23:51:00">[23:51:00]</a>, <a class="yt-timestamp" data-t="27:36:00">[27:36:00]</a>.

### DreamGaussian

*   **Initialization**: DreamGaussian starts its 3D Gaussians from a simple sphere of gray points <a class="yt-timestamp" data-t="45:55:00">[45:55:00]</a>, <a class="yt-timestamp" data-t="00:59:59">[00:59:59]</a>.
*   **Pipeline**: It follows a two-stage process:
    1.  **Generative Gaussian Splatting**: Uses SDS to optimize the initial Gaussians into a rough 3D shape <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>.
    2.  **Mesh Extraction and Texture Refinement**: A unique aspect of DreamGaussian is its ability to convert the generated Gaussian splat into a traditional textured mesh <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>. This is done using an algorithm like marching cubes to extract the mesh, followed by UV space texture refinement <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>, <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. This step aims to produce "ready-to-use 3D assets" for existing game engines and CGI pipelines <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>, <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
*   **Performance**: DreamGaussian can produce high-quality textured meshes in just two minutes on a single Nvidia V100 GPU (16GB memory), or even with 8GB of GPU memory, showcasing a 10x acceleration over existing methods <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>, <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>, <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

### GSGen

*   **Initialization**: GSGen utilizes a stronger 3D prior for initialization, starting from a point cloud generated by OpenAI's Point-E model <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>, <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>, <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. Point-E itself is a text-to-point cloud model trained on a large dataset of 3D models <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. While Point-E can produce colored point clouds, GSGen opts for random color initialization <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.
*   **Pipeline**: GSGen also has a two-stage optimization process:
    1.  **Geometry Optimization**: Establishes a coarse 3D Gaussian representation under the guidance of the Point-E prior and the SDS loss <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. This 3D prior helps mitigate the Janus problem by providing a more consistent initial shape <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.
    2.  **Appearance Refinement**: Iteratively refines the Gaussians by increasing their number through "compactness-based densification" and pruning unnecessary ones <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. This refinement occurs directly in the Gaussian splatting space, without converting to a mesh <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.
*   **Quality**: GSGen exhibits higher visual quality, particularly in capturing high-frequency details (small textures), compared to older mesh-based methods that often produce overly smooth geometry <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>, <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.

### [[Challenges and solutions in representing 3D objects with gaussian splatting | Challenges and Limitations]]

Both papers share common limitations with previous text-to-3D works:
*   **Janus Problem**: While mitigated by 3D priors, it's not entirely eliminated, especially with text prompts biased by 2D diffusion models <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>, <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.
*   **Complex Prompts**: Generating satisfying results from complex or logically intricate text prompts remains a challenge due to the limitations of language understanding in the underlying models (e.g., Point-E and CLIP) <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
*   **Baked Lighting**: Current implementations often use a simple diffuse color for each Gaussian, meaning lighting cannot be dynamically changed, as spherical harmonics (for view-dependent color) are typically disabled for simplicity <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

## Future Outlook for Gaussian Splatting

Gaussian Splatting is poised to become a dominant 3D representation format <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. Its advantages in speed, quality, and explicit nature make it highly suitable for various applications:
*   **Gaming and VR/AR**: The explicit nature and real-time rendering capabilities suggest that future game engines and virtual/augmented reality environments may directly use Gaussian Splats instead of traditional meshes and textures <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>, <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.
*   **3D Printing**: While currently 3D printing relies on mesh formats like STL, the volumetric and explicit nature of 3D Gaussians could potentially lead to direct conversion to G-code or other additive manufacturing instructions, bypassing meshes entirely <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>, <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
*   **Editing and Composition**: The ability to manipulate individual Gaussians easily will enable more advanced editing, object removal, and scene composition directly within the Gaussian splatting representation <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

As [[Dynamic 3D Gaussian methodology | Gaussian Splatting]] continues to advance, it promises to revolutionize [[3D modeling and tracking using Gaussian splatting | 3D modeling and tracking]] and content creation by offering unprecedented levels of efficiency and detail.