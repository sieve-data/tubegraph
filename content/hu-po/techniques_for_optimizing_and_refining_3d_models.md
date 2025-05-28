---
title: Techniques for optimizing and refining 3D models
videoId: l956ye13F8M
---

From: [[hu-po]] <br/> 

The field of 3D content creation has seen rapid advancements, particularly with the emergence of text-to-3D generation. This process typically involves multiple stages of optimization and refinement to produce high-quality, consistent 3D models <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a> <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

## Evolution of 3D Representations

Historically, [[3d_representations_and_their_applications | 3D objects]] have been represented in various formats, each with its own advantages and limitations.

### Traditional Meshes and Textures
For a long time, the dominant 3D representation in video games and CGI has been the texture and mesh format <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Mesh**: Represents the 3D model as a collection of vertices (dots) and polygons (triangles) that form a surface <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a> <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.
*   **Texture**: A 2D image that is "wrapped" onto the mesh to provide color and surface details <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a> <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
This format requires defining precise triangles and handling issues like UV mapping, which can be complex <a class="yt-timestamp" data-t="00:50:12">[00:50:12]</a> <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>.

### Neural Radiance Fields (Nerfs)
More recently, Neural Radiance Fields (Nerfs) gained popularity as an entirely different type of [[3d_representations_and_their_applications | 3D representation]] <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a> <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Implicit Representation**: Nerfs train a neural network (e.g., a multi-layer perceptron) to implicitly store the 3D object within its weights <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a> <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **View Synthesis**: The neural network can be queried to predict the color of every pixel from a specific camera position and viewpoint <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
A major limitation of Nerfs is that each neural network typically learns only one object, requiring a new network to be trained for every new object <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a> <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. This implicit nature also makes operations like deleting parts of an object difficult <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>.

### Gaussian Splatting
Gaussian Splatting is a newer [[3d_representations_and_their_applications | 3D representation technique]] that has gained significant attention due to its speed, quality, and simplicity <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a> <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Explicit Representation**: It represents a 3D scene using millions of individual 3D Gaussian particles, similar to a point cloud <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a> <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a> <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>.
*   **Parameters**: Each 3D Gaussian has a position, orientation, scale, opacity, and a view-dependent color <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a> <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a> <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>. These Gaussians are projected onto the camera's image plane as 2D Gaussians for rendering <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a> <a class="yt-timestamp" data-t="00:38:23">[00:38:23]</a>.
*   **Efficiency**: Gaussian Splatting is significantly faster than Nerfs for [[3d_representations_and_their_applications | 3D reconstruction]] and rendering <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a> <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a> <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>. This is partly due to a GPU-friendly rasterization process that tiles images and sorts Gaussians efficiently <a class="yt-timestamp" data-t="00:38:46">[00:38:46]</a>.
The explicit nature of Gaussian Splatting also makes compositional operations (e.g., deleting parts of a scene) much easier <a class="yt-timestamp" data-t="00:42:23">[00:42:23]</a> <a class="yt-timestamp" data-t="02:01:04">[02:01:04]</a>.

## Optimization and Refinement Techniques
Creating 3D models from text prompts involves complex multi-stage optimization processes.

### Score Distillation Sampling (SDS)
Score Distillation Sampling (SDS) is a core technique used in text-to-3D generation, originating from the DreamFusion paper <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a> <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>.
*   **Principle**: Instead of directly generating 3D models, SDS optimizes a [[3d_representations_and_their_applications | 3D representation]] (like Gaussians or Nerfs) using a 2D pre-trained image diffusion model as a prior <a class="yt-timestamp" data-t="00:47:31">[00:47:31]</a> <a class="yt-timestamp" data-t="00:48:07">[00:48:07]</a>.
*   **Differentiable Rendering**: The 3D representation is differentiably rendered into an image based on camera parameters, allowing gradients to be back-propagated <a class="yt-timestamp" data-t="00:48:23">[00:48:23]</a> <a class="yt-timestamp" data-t="00:51:24">[00:51:24]</a>.
*   **Guidance**: A diffusion model provides a "score estimation function" to guide the gradient updates, refining the 3D model so that its rendered views align with plausible samples from the diffusion model <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a> <a class="yt-timestamp" data-t="00:51:10">[00:51:10]</a>.

### Progressive Densification and Pruning
Both Nerfs and Gaussian Splatting utilize techniques to refine the density of their 3D representations:
*   **Occupancy Pruning**: In Nerfs, this involves removing empty space or diffuse effects to clean up the 3D representation <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a> <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   **Progressive Densification**: For 3D Gaussians, this means adding more small points (Gaussians) in areas that should be dense, leading to faster convergence for 3D generative tasks <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a> <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.
*   **Pruning**: Removing unnecessary Gaussians, often those with low opacity or outside a certain threshold, to reduce memory usage and improve detail <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a> <a class="yt-timestamp" data-t="01:15:21">[01:15:21]</a>. These processes often involve hard-coded thresholds which can be a limitation <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>.

### Mesh Extraction and Texture Refinement (DreamGaussian)
The DreamGaussian paper extends the process by converting the generated Gaussian Splat into a traditional mesh and texture format <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a> <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **Purpose**: This conversion allows the 3D object to be imported into existing game engines or CGI pipelines like Blender <a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a>.
*   **Process**: They use an algorithm (e.g., Marching Cubes, an older algorithm) to convert the point cloud-like Gaussian Splat into a polygonal mesh <a class="yt-timestamp" data-t="01:05:32">[01:05:32]</a>. A "color back projection" creates a UV map for the texture <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.
*   **Refinement**: A subsequent UV space texture refinement stage (using a diffusion model like Stable Diffusion) is applied to enhance texture quality <a class="yt-timestamp" data-t="01:08:22">[01:08:22]</a>.

### Direct Gaussian Splat Refinement (GSGen)
The GSGen paper, in contrast, performs its refinement directly within the Gaussian Splat representation <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a> <a class="yt-timestamp" data-t="01:08:55">[01:08:55]</a>.
*   **3D Prior Initialization**: GSGen initializes its Gaussians using a point cloud generated by Point-E, an OpenAI model for generating 3D point clouds from text prompts <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a> <a class="yt-timestamp" data-t="00:59:17">[00:59:17]</a>. Point-E's intelligence comes from a proprietary dataset of 3D models <a class="yt-timestamp" data-t="01:31:52">[01:31:52]</a>.
*   **Optimization Stages**: Both papers use a two-stage optimization strategy:
    1.  **Geometry Optimization**: Establishes a coarse representation. GSGen uses a 3D point cloud diffusion prior (Point-E) alongside the 2D SDS loss <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a> <a class="yt-timestamp" data-t="01:37:51">[01:37:51]</a>. DreamGaussian starts from a simple gray sphere of Gaussians <a class="yt-timestamp" data-t="00:59:59">[00:59:59]</a>.
    2.  **Appearance Refinement**: Iteratively refines details and enhances continuity <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. GSGen uses a "compactness-based densification" approach, adding Gaussians between close neighbors and pruning those with low opacity <a class="yt-timestamp" data-t="01:14:31">[01:14:31]</a> <a class="yt-timestamp" data-t="01:15:28">[01:15:28]</a>.

### Role of 3D Priors
A significant factor in optimization is the choice of 3D prior for initialization <a class="yt-timestamp" data-t="01:19:50">[01:19:50]</a>.
*   **Point-E (GSGen)**: Leverages Point-E to generate an initial point cloud geometry based on the text prompt, which helps mitigate the "Janus problem" (discussed below) and generates more sensible geometry <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a> <a class="yt-timestamp" data-t="01:09:53">[01:09:53]</a>.
*   **Zero-1-2-3 (DreamGaussian)**: Uses a view-conditioned diffusion model (Zero-1-2-3 XL) which is trained on the Objaverse dataset (800,000 3D models) <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a> <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>. This model can generate images from specific camera viewpoints (e.g., "down 30 degrees") <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>.

## Efficiency and Quality
[[efficiency_and_performance_of_finetuning_methods | Gaussian Splatting-based methods]] like DreamGaussian and GSGen offer significant improvements in speed and quality over previous text-to-3D approaches.
*   DreamGaussian can produce high-quality textured meshes in just two minutes on a single Nvidia V100 GPU (or even with 8GB of consumer GPU memory), which is approximately 10 times faster than existing methods <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a> <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a> <a class="yt-timestamp" data-t="01:39:16">[01:39:16]</a>.
*   GSGen demonstrates superior visual quality, especially in capturing high-frequency details (small textures and intricate patterns), partly because it avoids the "smoothing" effect that can occur when converting to and refining meshes <a class="yt-timestamp" data-t="01:21:11">[01:21:11]</a> <a class="yt-timestamp" data-t="01:30:08">[01:30:08]</a>.

## Challenges in 3D Generation

*   **Janus Problem**: This refers to the tendency of 3D models generated from 2D diffusion models (which often have a frontal bias from their training data) to have multiple "faces" or inconsistent geometry when viewed from different angles <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a> <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>. Incorporating a 3D prior, like Point-E, helps mitigate this problem <a class="yt-timestamp" data-t="01:09:21">[01:09:21]</a> <a class="yt-timestamp" data-t="01:37:13">[01:37:13]</a>.
*   **Unstable Gradients**: The SDS loss can lead to unstable gradients because the underlying 2D diffusion model used as a prior may be biased towards certain viewpoints (e.g., the front of an object), leading to inconsistent feedback for 3D optimization <a class="yt-timestamp" data-t="01:34:36">[01:34:36]</a>.
*   **Hard-coded Hyperparameters**: Current Gaussian Splatting techniques still rely on many hard-coded thresholds for densification and pruning, suggesting room for further optimization and automation <a class="yt-timestamp" data-t="01:27:21">[01:27:21]</a>.
*   **Baked Lighting**: Many current models use a simple diffuse color for Gaussians and do not account for view-dependent lighting effects (e.g., shadows), leading to "baked lighting" that cannot be changed <a class="yt-timestamp" data-t="01:43:35">[01:43:35]</a>. This can be addressed by incorporating spherical harmonics or other advanced techniques <a class="yt-timestamp" data-t="01:43:55">[01:43:55]</a>.

## Future Outlook
There is a strong belief that Gaussian Splatting will become the dominant [[3d_representations_and_their_applications | 3D representation]] format, potentially replacing traditional meshes and textures due to its speed, quality, and explicit nature <a class="yt-timestamp" data-t="00:42:13">[00:42:13]</a> <a class="yt-timestamp" data-t="00:49:59">[00:49:59]</a>. Implementations are already appearing in real-time applications like augmented reality (AR) and virtual reality (VR) environments <a class="yt-timestamp" data-t="01:57:35">[01:57:35]</a>. The ability to directly manipulate explicit Gaussians opens doors for advanced applications, including potentially direct 3D printing from Gaussian Splats <a class="yt-timestamp" data-t="01:12:01">[01:12:01]</a>.