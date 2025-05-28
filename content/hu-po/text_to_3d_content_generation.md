---
title: Text to 3D content generation
videoId: l956ye13F8M
---

From: [[hu-po]] <br/> 

Text to 3D content generation is a rapidly evolving field focused on creating three-dimensional objects from descriptive text prompts. This technology aims to extend the success seen in [[techniques_for_personalizing_text_to_image_diffusion_models | text-to-image diffusion models]] (e.g., DALL-E 3, Stable Diffusion) to the 3D domain <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. Recent advancements leverage new 3D representation techniques, particularly Gaussian Splatting, to achieve high efficiency and quality <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## 3D Representation Techniques

Historically, 3D objects have been represented in various ways, each with its own advantages and limitations.

### Mesh and Texture

The most traditional and widely used format in video games and CGI is the mesh and texture format <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Mesh**: A 3D model represented as a collection of vertices (points) and polygons (usually triangles) that define its surface <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
*   **Texture (UV Map)**: A 2D image that is "wrapped" or projected onto the mesh to provide color and surface detail <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   The coordinates on this 2D image are often referred to as "UV space" <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
This format requires defining explicit connectivity between points and can be complex to manipulate <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.

### Neural Radiance Fields (NeRFs)

NeRFs emerged as a popular, but different, 3D representation technique <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   **Implicit Representation**: A NeRF trains a neural network (e.g., a multi-layer perceptron) whose weights implicitly store the 3D object <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Given a camera position and viewing angle, the neural network predicts the color of each pixel in the rendered image <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Limitations**: NeRFs often suffer from slow per-sample optimization, meaning a new neural network must be trained for every unique object <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. This implicit nature also makes editing or manipulating the 3D object difficult <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>.

### Gaussian Splatting

Gaussian Splatting is a new, highly efficient technique for 3D representation <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Explicit Representation**: A 3D scene is represented by millions of discrete 3D "Gaussians" (particles) <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Each 3D Gaussian is parameterized by its position (mean), orientation, scale (covariance matrix), opacity, and color <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Rendering**: When rendering, 3D Gaussians are projected onto the camera's imaging plane as 2D Gaussians <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>. The final color of a pixel is determined by summing the contributions of overlapping Gaussians within specific image "tiles" <a class="yt-timestamp" data-t="00:39:47">[00:39:47]</a>. This process leverages GPU-friendly rasterization for extreme speed <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>.
*   **Advantages**: [[Comparison of 3D Representation Techniques | Gaussian Splatting]] offers significantly faster rendering speeds, more detailed scene reconstruction, and reduced memory usage compared to NeRFs <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>. Its explicit nature allows for easier manipulation, such as deleting or copying parts of a scene <a class="yt-timestamp" data-t="00:42:23">[00:42:23]</a>.

## Text to 3D with Gaussian Splatting

The advent of Gaussian Splatting led researchers to adapt existing text-to-3D methodologies to this new representation <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

### Score Distillation Sampling (SDS)

A core technique used in text-to-3D generation is [[dreamfusion_for_text_to_3d_model_generation | Score Distillation Sampling (SDS)]], originally proposed in the DreamFusion paper <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Mechanism**: Instead of directly generating 3D models, SDS optimizes a 3D representation (like Gaussians) by leveraging a pre-trained 2D image diffusion model as a "prior" or guide <a class="yt-timestamp" data-t="00:47:31">[00:47:31]</a>.
*   **Process**: A 3D representation is iteratively refined. For any given camera pose, the rendered 2D image from the 3D model is fed to the diffusion model, which provides a "score estimation" (gradient) indicating how much the image deviates from a plausible sample for the given text prompt <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>. This gradient is then back-propagated to update the 3D model's parameters <a class="yt-timestamp" data-t="00:51:10">[00:51:10]</a>.
*   **The "Janus Problem"**: A common challenge in text-to-3D methods relying solely on 2D diffusion models is the "Janus problem" <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>. Since 2D image datasets often have a frontal bias (e.g., more images of a panda's front than its back), the generated 3D objects may exhibit inconsistencies like multiple faces or distorted geometry when viewed from different angles <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>.

### DreamGaussian

"DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation" was published on September 28, 2023, by researchers from S-LAB, Nanyang Technological University, Baidu Inc., and Peking University <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

*   **Approach**: It proposes a multi-stage optimization process <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>:
    1.  **Generative Gaussian Splatting**: Initializes with a sphere of gray Gaussians <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. It uses the SDS loss, guided by a 2D diffusion model (specifically, the zero-one-two-three model, which is trained on the Objaverse dataset) <a class="yt-timestamp" data-t="00:53:51">[00:53:51]</a>.
    2.  **Mesh Extraction**: Converts the generated Gaussian Splat into a polygonal mesh using the marching cubes algorithm, a method for reconstructing a surface from a volumetric dataset <a class="yt-timestamp" data-t="01:05:32">[01:05:32]</a>.
    3.  **Texture Refinement in UV Space**: Applies a fine-tuning stage to refine the texture of the extracted mesh in UV space, further improving details <a class="yt-timestamp" data-t="01:21:02">[01:21:02]</a>.
*   **Performance**: DreamGaussian can produce high-quality textured meshes in just two minutes from a single image on a consumer-grade GPU (e.g., 8GB of VRAM), achieving approximately 10 times acceleration compared to existing methods <a class="yt-timestamp" data-t="01:03:57">[01:03:57]</a>.
*   **Limitations**:
    *   Starting with a simple gray sphere prior can lead to "degenerated 3D objects," especially for prompts depicting asymmetric scenes <a class="yt-timestamp" data-t="01:32:15">[01:32:15]</a>.
    *   The process of converting to a mesh and refining in UV space can result in "overly smooth geometry," losing high-frequency details <a class="yt-timestamp" data-t="01:30:08">[01:30:08]</a>.
    *   It suffers from the Janus problem and "baked lighting" (lack of view-dependent color due to not using spherical harmonics) <a class="yt-timestamp" data-t="01:43:33">[01:43:33]</a>.

### GSGen

"Text to 3D using Gaussian Splatting" (GSGen) was also published on September 28, 2023, by researchers from Tsinghua University and other institutions <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

*   **Approach**: GSGen adopts a progressive optimization strategy with two main stages <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>:
    1.  **Geometry Optimization**: Establishes a coarse 3D Gaussian representation guided by a [[point_e_for_text_to_3d_model_generation | 3D point cloud diffusion prior]] from [[point_e_for_text_to_3d_model_generation | Point-E]] (OpenAI's text-to-3D point cloud model) <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>. This is a more robust starting point than a simple sphere <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. It combines this with the standard 2D SDS loss <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.
    2.  **Appearance Refinement**: Iteratively refines the Gaussians by increasing their number through "compactness-based densification" and pruning unnecessary Gaussians <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. This refinement is done directly in the Gaussian Splat representation, avoiding conversion to meshes <a class="yt-timestamp" data-t="01:09:01">[01:09:01]</a>. It uses a combination of SDS loss and regularization terms for position and opacity <a class="yt-timestamp" data-t="01:15:52">[01:15:52]</a>.
*   **Advantages**:
    *   The use of a 3D point cloud prior (e.g., from [[point_e_for_text_to_3d_model_generation | Point-E]]) helps mitigate the Janus problem more effectively and generates more sensible 3D geometry <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>.
    *   Produces higher visual quality, especially in high-frequency details, compared to mesh-based methods <a class="yt-timestamp" data-t="01:21:12">[01:21:12]</a>.
    *   The refinement directly within the Gaussian Splat representation avoids the smoothing effect seen in mesh-based refinement <a class="yt-timestamp" data-t="01:30:29">[01:30:29]</a>.
*   **Limitations**:
    *   The quality of the generated objects can be limited by the language understanding ability of the [[point_e_for_text_to_3d_model_generation | Point-E]] model and the Clip text encoder <a class="yt-timestamp" data-t="01:36:16">[01:36:16]</a>.
    *   Still faces the Janus problem in extreme cases where text prompts are highly biased <a class="yt-timestamp" data-t="01:37:13">[01:37:13]</a>.
    *   Relies on hard-coded thresholds for densification and pruning, which may need tuning for different scenes <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>.

## Comparison and Future Outlook

Both DreamGaussian and GSGen represent significant steps in text-to-3D generation by leveraging Gaussian Splatting for efficiency and quality.

| Feature              | DreamGaussian                               | GSGen                                            |
| :------------------- | :------------------------------------------ | :----------------------------------------------- |
| **Initialization**   | Gray sphere of Gaussians <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>      | [[point_e_for_text_to_3d_model_generation | Point-E]] generated point cloud (stronger prior) <a class="yt-timestamp" data-t="00:59:17">[00:59:17]</a> |
| **Refinement Stage** | Mesh extraction and UV texture refinement <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a> | Direct Gaussian densification and pruning <a class="yt-timestamp" data-t="01:09:01">[01:09:01]</a> |
| **Output**           | Textured polygonal meshes <a class="yt-timestamp" data-t="01:53:03">[01:53:03]</a>           | Gaussian Splats <a class="yt-timestamp" data-t="01:55:06">[01:55:06]</a>                               |
| **Speed**            | ~2 minutes <a class="yt-timestamp" data-t="01:03:57">[01:03:57]</a>                         | ~2 minutes <a class="yt-timestamp" data-t="01:19:10">[01:19:10]</a>                            |
| **Janus Problem**    | Present <a class="yt-timestamp" data-t="01:45:22">[01:45:22]</a>                             | Mitigated by 3D prior <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>                      |

The debate continues regarding the optimal 3D representation. While meshes are currently prevalent in [[applications_of_text_to_3d_model_generation_in_various_industries | game engines]] and [[applications_of_text_to_3d_model_generation_in_various_industries | 3D printing]], the explicit, flexible, and efficient nature of Gaussian Splats suggests they could become the future standard <a class="yt-timestamp" data-t="01:58:20">[01:58:20]</a>. This could lead to game engines natively supporting Splats and new methods for [[applications_of_text_to_3d_model_generation_in_various_industries | 3D printing]] directly from Splats, bypassing meshes entirely <a class="yt-timestamp" data-t="01:58:20">[01:58:20]</a>.

Future work in this area will likely focus on:
*   Integrating spherical harmonics for view-dependent color and realistic lighting <a class="yt-timestamp" data-t="01:43:53">[01:43:53]</a>.
*   Developing more robust and adaptive densification strategies that do not rely on hard-coded thresholds <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>.
*   Further improving the [[human_preference_learning_for_text_to_3d_models | 3D consistency]] and fidelity of generated objects, especially for complex or asymmetric scenes.
*   Exploring [[compositional_3d_asset_creation_and_multiobject_generation | compositional 3D asset creation]] and [[generative_3d_models_using_video_diffusion | multi-object generation]].