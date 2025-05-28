---
title: Gaussian splatting and its advantages
videoId: l956ye13F8M
---

From: [[hu-po]] <br/> 

[[3d_gaussian_splatting_and_instant_splat_pipeline | Gaussian Splatting]] is a novel 3D representation technique that has gained significant attention due to its efficiency and quality in representing 3D scenes and objects <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This method, introduced in Kerbal Al 2023, is a pioneering approach for novel view synthesis and 3D reconstruction from multi-view images <a class="yt-timestamp" data-t="00:35:15">[00:35:15]</a>.

## What is Gaussian Splatting?
Unlike traditional 3D formats or Neural Radiance Fields (NeRFs), [[3d_gaussian_splatting_and_instant_splat_pipeline | 3D Gaussian Splatting]] represents a 3D scene using millions of small particles, similar to a point cloud <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Each of these particles is a 3D Gaussian <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

Each [[3d_gaussian_splatting_and_instant_splat_pipeline | 3D Gaussian]] is parameterized by:
*   **Position**: A 3D coordinate in space <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Orientation**: How it's rotated in space (e.g., using a quaternion) <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>, <a class="yt-timestamp" data-t="00:43:46">[00:43:46]</a>.
*   **Scale**: How large it is <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Opacity**: How transparent or visible it is <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>, <a class="yt-timestamp" data-t="00:43:58">[00:43:58]</a>.
*   **View-dependent color**: The color of the Gaussian, which can change based on the camera's viewpoint <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>, <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>. However, in some applications like the papers discussed, a simpler diffuse color (not view-dependent) may be used to prioritize speed <a class="yt-timestamp" data-t="00:44:09">[00:44:09]</a>.

When rendering, these 3D Gaussians are projected onto the camera's image plane, appearing as 2D Gaussians <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>. The final color of each pixel in the rendered image is determined by summing the contributions of all Gaussians within a specific "tile" of the image, sorted by depth using a point-based volume rendering technique <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>.

## Advantages of Gaussian Splatting
[[advantages_and_disadvantages_of_gosh_and_splats | Gaussian Splatting]] offers several significant advantages over previous 3D representation methods:

### Superior Speed and Efficiency
*   **Faster Rendering**: [[3d_gaussian_splatting_for_realtime_radiance_field_rendering | Gaussian Splatting for real-time radiance field rendering]] is significantly faster than NeRFs <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. The rendering process is very fast, enabling real-time rendering <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>, <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>. This is partly due to a GPU-friendly rasterization process that assigns each thread block to render an image tile, maximizing shared memory utilization <a class="yt-timestamp" data-t="00:40:41">[00:40:41]</a>.
*   **Faster Training/Optimization**: [[advantages_and_disadvantages_of_gosh_and_splats | 3D Gaussians]] converge significantly faster for 3D generative tasks <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. For instance, DreamGaussian can produce high-quality textured meshes in just two minutes from a single image on a consumer GPU <a class="yt-timestamp" data-t="01:39:25">[01:39:25]</a>, achieving approximately 10 times acceleration compared to existing methods <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.

### High Quality and Detail
*   **Detailed Scene Reconstruction**: Gaussian Splatting can achieve more detailed scene reconstruction compared to NeRF methods <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>.
*   **Capture High-Frequency Details**: Methods utilizing Gaussian Splatting, like GSGen, exhibit better visual quality, especially in intricate patterns and high-frequency details (small textures and fine elements) <a class="yt-timestamp" data-t="01:21:12">[01:21:12]</a>, <a class="yt-timestamp" data-t="01:29:57">[01:29:57]</a>. This contrasts with mesh-based methods that often yield overly smooth geometry <a class="yt-timestamp" data-t="01:30:07">[01:30:07]</a>.

### Simplicity and Explicitness
*   **Simpler Approach**: Gaussian Splatting is significantly simpler than some of the other previous approaches, like NeRFs <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Explicit Representation**: Unlike implicit representations (e.g., NeRFs), Gaussian Splatting provides an explicit representation of a 3D object <a class="yt-timestamp" data-t="00:41:35">[00:41:35]</a>. This means the XYZ position and other parameters of each Gaussian are directly known <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. This explicit nature enables compositional operations, such as deleting parts of a Splat or combining different Splats <a class="yt-timestamp" data-t="00:42:23">[00:42:23]</a>. For example, one can easily remove a floor from a scene by deleting the Gaussians representing it <a class="yt-timestamp" data-t="00:42:42">[00:42:42]</a>.

### Reduced Memory Usage
*   Gaussian Splatting reduces memory usage during training compared to NeRF methods <a class="yt-timestamp" data-t="00:40:58">[00:40:58]</a>.
*   It can generate high-quality 3D assets with relatively low GPU memory (e.g., 8 GB of GPU memory) <a class="yt-timestamp" data-t="01:39:27">[01:39:27]</a>, making it accessible on consumer-grade GPUs <a class="yt-timestamp" data-t="01:39:42">[01:39:42]</a>.

## [[comparisons_between_gaussian_splats_and_other_3d_representation_technologies | Comparisons to Other 3D Representations]]

### Mesh and Texture Format
The traditional method for representing 3D objects involves a mesh (a collection of vertices and polygons forming the 3D model) and a 2D texture image that is "wrapped" onto the mesh to provide color <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. This format is prevalent in video games and CGI <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

However, this method has limitations:
*   Modifying the mesh often requires creating a new UV texture <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>.
*   Mesh generation can be complex and prone to "garbage" due to the polygon structure <a class="yt-timestamp" data-t="00:50:12">[00:50:12]</a>.
*   It's not an intuitive way to represent real-world objects, which have volume rather than infinitely thin surfaces <a class="yt-timestamp" data-t="01:24:58">[01:24:58]</a>.

### Neural Radiance Fields (NeRFs)
NeRFs represent 3D objects implicitly by training a neural network that learns to output the color and density of any point in space from a given viewpoint <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. While innovative, NeRFs are slower for per-sample optimization, requiring a new neural network to be trained for each new object <a class="yt-timestamp" data-t="01:19:58">[01:19:58]</a>. Their implicit nature also makes direct manipulation or "explainability" difficult, as the 3D object is stored within the neural network's weights rather than as explicit geometric data <a class="yt-timestamp" data-t="00:41:47">[00:41:47]</a>.

[[nerfs_versus_gaussian_splatting | Gaussian Splatting]] directly addresses these limitations by offering an explicit, faster, and more versatile 3D representation <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Applications in Text-to-3D Generation
Recent research has focused on leveraging [[3d_gaussian_splatting_and_instant_splat_pipeline | Gaussian Splatting]] for text-to-3D content creation. Two notable papers in this area are DreamGaussian and GSGen:

*   **DreamGaussian**: This paper focuses on generating 3D content efficiently and with high quality by designing a generative [[3d_gaussian_splatting_and_instant_splat_pipeline | Gaussian Splatting]] model. It includes a multi-stage optimization process and features mesh extraction and texture refinement, allowing the generated 3D objects to be compatible with existing game engines and CGI pipelines <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>, <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
*   **GSGen (Text to 3D using Gaussian Splatting)**: This approach aims to generate high-quality 3D objects from text by exploiting the explicit nature of [[3d_gaussian_splatting_and_instant_splat_pipeline | 3D Gaussian Splatting]] and incorporating a 3D prior (such as a point cloud from Point E) <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. It uses a progressive optimization strategy with geometry optimization and appearance refinement stages, directly manipulating the Gaussian representation <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>, <a class="yt-timestamp" data-t="01:09:05">[01:09:05]</a>.

Both methods utilize Score Distillation Sampling (SDS) loss, a technique originally from the DreamFusion paper, to guide the 3D generation process using pre-trained 2D image diffusion models <a class="yt-timestamp" data-t="00:47:27">[00:47:27]</a>.

## [[implications_of_gaussian_splatting_in_future_technologies | Future Implications]]
The explicit nature and efficiency of [[3d_gaussian_splatting_and_instant_splat_pipeline | Gaussian Splatting]] suggest it could become the standard 3D representation format, potentially replacing traditional meshes and textures <a class="yt-timestamp" data-t="01:01:03">[01:01:03]</a>, <a class="yt-timestamp" data-t="01:58:19">[01:58:19]</a>. This shift could simplify 3D content creation pipelines, including game engines and augmented/virtual reality (AR/VR) applications, allowing direct manipulation and rendering of splats <a class="yt-timestamp" data-t="01:57:47">[01:57:47]</a>. It might also revolutionize 3D printing by enabling direct printing from dense Gaussian representations, bypassing the need for intermediate mesh formats like STL <a class="yt-timestamp" data-t="01:12:53">[01:12:53]</a>.