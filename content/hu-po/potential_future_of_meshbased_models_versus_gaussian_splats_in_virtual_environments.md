---
title: Potential future of meshbased models versus gaussian splats in virtual environments
videoId: l956ye13F8M
---

From: [[hu-po]] <br/> 

The field of 3D content creation and representation is rapidly evolving, with new techniques challenging established norms. Historically, mesh-based models dominated virtual environments, but recent advancements, particularly with [[3d_gaussian_splatting_and_nerfs | Gaussian Splats]], suggest a significant shift in how 3D objects and scenes will be represented and rendered.

## Traditional 3D Representation: Meshes and Textures

For a very long time, and still predominantly today, 3D objects in video games and CGI are represented using a **texture and mesh format** <a class="yt-timestamp" data-t="05:23:00">[05:23:00]</a>. This format consists of two primary components:
*   **Mesh**: The 3D model itself, which is a collection of vertices forming polygons (often triangles) that define the object's surface <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.
*   **Texture**: A 2D image that is "wrapped" onto the mesh to provide color and surface detail <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.

This approach has been the standard due to its established pipelines in game engines and CGI tools <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>. However, it presents challenges: meshes involve complexities like handling polygon cleanliness and connectivity, and textures are inherently 2D, meaning they need re-creation if the mesh changes significantly <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>, <a class="yt-timestamp" data-t="05:08:50">[05:08:50]</a>.

## Neural Radiance Fields (NeRFs)

A relatively recent development before [[3d_gaussian_splatting_and_nerfs | Gaussian Splats]] were [[3d_representation_techniques_nerfs_vs_gausssian_splats | Neural Radiance Fields]] (NeRFs), which gained significant popularity <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>. NeRFs represent 3D objects implicitly by training a neural network <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>. This network stores the 3D object within its weights and can generate the color of every pixel from any given camera position and viewpoint <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.

While exciting, NeRFs suffer from a key limitation: they are "per-sample" <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>. This means a new neural network must be trained for *each* object, leading to slow optimization times and limiting practical usage <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>. Furthermore, their implicit nature makes it difficult to directly understand or modify individual components of the 3D object <a class="yt-timestamp" data-t="41:47:00">[41:47:00]</a>.

## Gaussian Splats: A New Paradigm

[[3d_gaussian_splatting_and_nerfs | Gaussian Splats]] represent a new [[3d_representation_techniques_nerfs_vs_gausssian_splats | 3D representation technique]] that has garnered significant attention due to its efficiency and quality <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>, <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>. They represent a 3D scene using millions of small particles, similar to a point cloud <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>. Each of these particles is a 3D Gaussian, defined by:
*   A 3D **position** <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>
*   An **orientation** <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>
*   A **scale** <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>
*   An **opacity** <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>
*   A **view-dependent color** <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>

When rendering, these 3D Gaussians are projected onto the camera's image plane, appearing as 2D Gaussians <a class="yt-timestamp" data-t="38:23:00">[38:23:00]</a>. The final color at each pixel is calculated by summing the contributions of Gaussians within a specific tiled area, sorted by depth <a class="yt-timestamp" data-t="39:12:00">[39:12:00]</a>, <a class="yt-timestamp" data-t="40:41:00">[40:41:00]</a>.

### Advantages of Gaussian Splats
[[Comparison between gaussian splats and traditional 3D representation methods | Gaussian Splats]] offer several key advantages over previous methods:
*   **Speed**: They are significantly faster than NeRFs, enabling real-time rendering <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>, <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>.
*   **Quality**: They can achieve very clean and detailed 3D scene reconstructions <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>, <a class="yt-timestamp" data-t="16:21:00">[16:21:00]</a>.
*   **Simplicity**: They are conceptually simpler than NeRFs <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.
*   **Explicit Nature**: Unlike NeRFs, [[3d_modeling_and_tracking_using_gaussian_splatting | Gaussian Splats]] explicitly store the 3D object's properties. This allows for direct manipulation, such as deleting parts of a scene or copying and pasting objects, which is extremely difficult or impossible with implicit representations like NeRFs <a class="yt-timestamp" data-t="42:23:00">[42:23:00]</a>. This compositionality is a crucial advantage for [[3d_content_generation_using_gaussian_splatting | 3D content generation]] and editing <a class="yt-timestamp" data-t="42:40:00">[42:40:00]</a>.

## The Future: A Splat-Dominated Virtual Landscape

The explicit and efficient nature of [[3d_gaussian_splatting_and_nerfs | Gaussian Splats]] leads to a strong prediction about their future dominance:
*   **Superseding Meshes and Textures**: Meshes and textures are predicted to "disappear" or be "superseded" by [[3d_gaussian_splatting_and_nerfs | Gaussian Splats]] <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>, <a class="yt-timestamp" data-t="51:03:00">[51:03:00]</a>. This is because Splats offer better detail capture and avoid the "smoothness" issues seen in mesh-based methods <a class="yt-timestamp" data-t="0:0:55:00">[01:30:08]</a>.
*   **Direct Integration into Game Engines**: Instead of converting Splats to meshes for use in game engines, the expectation is that game engines will directly support Splats, making entire virtual worlds composed of them <a class="yt-timestamp" data-t="01:57:50">[01:57:50]</a>, <a class="yt-timestamp" data-t="01:58:20">[01:58:20]</a>.
*   **Addressing the "Janus Problem"**: Older text-to-3D methods suffered from the "Janus problem," where objects generated from 2D diffusion models would have inconsistent views (e.g., multiple faces) due to the models' bias towards frontal views <a class="yt-timestamp" data-t="23:05:00">[23:05:00]</a>, <a class="yt-timestamp" data-t="01:34:57">[01:34:57]</a>. [[3d_content_generation_using_gaussian_splatting | Gaussian Splatting]] approaches, especially when combined with 3D point cloud priors, mitigate this problem by better shaping the 3D geometry from the outset <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>, <a class="yt-timestamp" data-t="01:33:15">[01:33:15]</a>.
*   **Evolution of 3D Printing**: While currently 3D printing often relies on mesh formats like STL, the explicit nature of [[3d_gaussian_splatting_and_nerfs | Gaussian Splats]] could lead to new additive manufacturing processes that directly utilize Splat data, potentially offering a more natural representation of 3D volume than infinitely thin surfaces <a class="yt-timestamp" data-t="01:12:53">[01:12:53]</a>, <a class="yt-timestamp" data-t="01:25:01">[01:25:01]</a>.

While current [[3d_content_generation_using_gaussian_splatting | text-to-3D Gaussian Splatting]] methods might still have limitations like "baked lighting" (lack of view-dependent lighting effects) or blurriness in certain views, these are considered solvable problems with further advancements in 2D diffusion models and other techniques <a class="yt-timestamp" data-t="01:43:35">[01:43:35]</a>, <a class="yt-timestamp" data-t="01:45:53">[01:45:53]</a>. The underlying architecture and explicit representation of [[3d_gaussian_splatting_and_nerfs | Gaussian Splats]] position them as a strong candidate for the future standard of 3D content in virtual environments.