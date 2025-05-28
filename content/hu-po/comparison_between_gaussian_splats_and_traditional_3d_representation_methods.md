---
title: Comparison between gaussian splats and traditional 3D representation methods
videoId: l956ye13F8M
---

From: [[hu-po]] <br/> 

The field of [[3D content generation using gaussian splatting | 3D content generation]] has seen rapid advancements, particularly with the emergence of [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]]. These new techniques are often compared against established and previously popular 3D representation methods like mesh and texture formats, and [[3D representation techniques Nerfs vs Gausssian Splats | Neural Radiance Fields (NeRFs)]] <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

## Traditional 3D Representation: Mesh and Texture

The most widely used 3D representation method, found in nearly all video games and CGI (Computer-Generated Imagery), is the mesh and texture format <a class="yt-timestamp" data-t="00:51:21">[00:51:21]</a>.

*   **Mesh**: The mesh represents the 3D model itself <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. It is a collection of vertices (individual points) connected by polygons, typically triangles, which form the surface of the 3D object <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. This means a mesh explicitly defines the 3D points and their connectivity <a class="yt-timestamp" data-t="00:26:24">[00:26:24]</a>.
*   **Texture**: To color the 3D object, a 2D image called a "texture" (or UV map) is "wrapped" onto the mesh <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. The coordinates used for this 2D image are often referred to as UV space <a class="yt-timestamp" data-t="01:13:38">[01:13:38]</a>.
*   **Limitations**: This format can be challenging to work with due to the need to deal with the "cleanliness" of polygons <a class="yt-timestamp" data-t="01:50:19">[01:50:19]</a>. If the mesh changes, the UV texture often needs to be remade <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>. This method can also lead to "overly smooth geometry" in generative tasks, obscuring intricate details <a class="yt-timestamp" data-t="01:30:08">[01:30:08]</a>.

## Neural Radiance Fields (NeRFs)

[[3D representation techniques Nerfs vs Gausssian Splats | Neural Radiance Fields]], or NeRFs, gained significant popularity as a new type of 3D representation technique <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

*   **Implicit Representation**: With NeRFs, a neural network implicitly stores the 3D object within its weights <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Users can query the neural network from a specific camera position and angle, and it will generate the color for every pixel in that view <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Limitations**: NeRFs are *per-sample* (or per-object), meaning a new neural network must be trained for every new object <a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a>. This results in "slow per sample optimization" <a class="yt-timestamp" data-t="01:11:55">[01:11:55]</a>. Furthermore, their implicit nature makes it difficult to edit or manipulate specific parts of the 3D object, unlike explicit representations <a class="yt-timestamp" data-t="01:42:51">[01:42:51]</a>.

## Gaussian Splats

[[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] are a newer and highly acclaimed technique for 3D representation <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. They represent a 3D scene using millions of individual 3D gaussians, akin to a point cloud <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

*   **Explicit Representation**: Each 3D gaussian is explicitly parameterized by its position, orientation, scale, opacity, and view-dependent color <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. When rendered, these 3D gaussians are projected into the camera's imaging plane as 2D gaussians <a class="yt-timestamp" data-t="01:37:22">[01:37:22]</a>.
*   **Rendering Process**: The GPU efficiently processes these gaussians by assigning them to image "tiles," sorting them by depth, and compositing them to determine the final pixel color <a class="yt-timestamp" data-t="01:38:46">[01:38:46]</a>. This process leverages existing GPU capabilities for fast rasterization <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>.

## Key Comparisons

| Feature               | Traditional (Mesh + Texture)                                | [[3D representation techniques Nerfs vs Gausssian Splats | Neural Radiance Fields (NeRFs)]]                                         | [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]]                                                      |
| :-------------------- | :---------------------------------------------------------- | :---------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **Representation**    | Explicit (vertices, faces, 2D texture map)                  | Implicit (neural network weights)                                       | Explicit (millions of 3D gaussians, each with properties)              |
| **Speed/Efficiency**  | Standard for real-time rendering in game engines            | Slow per-sample optimization <a class="yt-timestamp" data-t="01:11:55">[01:11:55]</a>        | Very fast, real-time rendering <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>, significantly faster for 3D generative tasks <a class="yt-timestamp" data-t="01:06:04">[01:06:04]</a> |
| **Quality**           | Can result in "overly smooth geometry" <a class="yt-timestamp" data-t="01:30:08">[01:30:08]</a> | "Pretty good in terms of quality" <a class="yt-timestamp" data-t="01:16:26">[01:16:26]</a>     | More detailed scene reconstruction, "high frequency details" <a class="yt-timestamp" data-t="01:29:57">[01:29:57]</a>, competitive generation quality <a class="yt-timestamp" data-t="01:06:04">[01:06:04]</a> |
| **Simplicity**        | Relatively complex workflow (modeling, UV unwrapping)     | Complex neural network architecture, difficult to interpret             | "Significantly simpler" than previous approaches <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a> |
| **Editability**       | Explicit but changing mesh invalidates texture maps <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a> | Difficult to edit due to implicit nature <a class="yt-timestamp" data-t="01:42:51">[01:42:51]</a>           | Highly editable; parts can be deleted, copied, or pasted easily <a class="yt-timestamp" data-t="01:42:23">[01:42:23]</a> |

### [[Challenges and solutions in representing 3D objects with gaussian splatting | Challenges and Limitations]]

*   **Janus Problem**: A recurring issue in text-to-3D generation using 2D diffusion models, where objects develop multiple faces <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>. This is due to the "frontal bias" of 2D image datasets used to train diffusion models <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>. Addressing this often requires incorporating a [[3D modeling and tracking using Gaussian splatting | 3D prior]] <a class="yt-timestamp" data-t="01:09:12">[01:09:12]</a>.
*   **Baked Lighting**: Current implementations of [[3D content generation using gaussian splatting | generative Gaussian Splats]] (e.g., DreamGaussian) may not use spherical harmonics for view-dependent color, leading to "baked lighting" where the lighting cannot be changed <a class="yt-timestamp" data-t="01:43:35">[01:43:35]</a>. This is a current limitation, not inherent to [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] themselves <a class="yt-timestamp" data-t="01:43:55">[01:43:55]</a>.
*   **Hyperparameter Dependence**: The refinement processes in [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] often rely on empirically determined, hard-coded thresholds for densification and pruning, which could be improved <a class="yt-timestamp" data-t="01:27:21">[01:27:21]</a>.

## The Future of 3D Representation

The inherent advantages of [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]], such as their explicit nature, speed, and quality, suggest they may supersede mesh and texture formats in the future <a class="yt-timestamp" data-t="01:41:55">[01:41:55]</a>. The ability to directly manipulate [[Physicsbased Modeling in Gaussian Splats | individual gaussians]] and the potential for direct integration into [[Potential future of meshbased models versus gaussian splats in virtual environments | game engines]] and augmented/virtual reality environments without intermediate mesh conversions are significant <a class="yt-timestamp" data-t="01:57:47">[01:57:47]</a>. While [[3D modeling and tracking using Gaussian splatting | mesh extraction]] from [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] is being explored for compatibility with existing pipelines, the long-term vision is for [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splats]] to become the standard 3D format <a class="yt-timestamp" data-t="01:05:16">[01:05:16]</a>.