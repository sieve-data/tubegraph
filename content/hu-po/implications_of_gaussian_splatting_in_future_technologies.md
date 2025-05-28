---
title: Implications of Gaussian splatting in future technologies
videoId: l956ye13F8M
---

From: [[hu-po]] <br/> 

[[Gaussian splatting and its advantages | Gaussian Splatting]] is emerging as a groundbreaking 3D representation technology, rapidly gaining attention for its efficiency, speed, and explicit nature compared to previous methods <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This new approach holds significant implications for various fields, particularly in 3D content creation, gaming, virtual reality (VR), augmented reality (AR), and even 3D printing.

## Evolution of 3D Representation
Historically, 3D objects in areas like video games and CGI have primarily relied on the **mesh and texture format** <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. In this format, a 3D model is represented by a mesh—a collection of vertices and polygons (often triangles)—that defines its geometric shape <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. A 2D texture (or UV map) is then "wrapped" onto this mesh to provide color and surface details <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. While ubiquitous, this method introduces complexities such as mesh cleanliness and the rigid coupling between the 3D geometry and its 2D texture, making modifications challenging <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>.

More recently, **Neural Radiance Fields (NeRFs)** gained popularity as a different type of 3D representation <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. [[NeRFs versus Gaussian Splatting | NeRFs implicitly store a 3D object within the weights of a neural network]] <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. While capable of synthesizing novel views, NeRFs are "per-sample" (meaning a new neural network must be trained for each object) and suffer from slow optimization times <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

## [[Gaussian splatting and its advantages | The Rise of Gaussian Splatting]]
[[3D gaussian splatting for realtime radiance field rendering | 3D Gaussian Splatting]] offers a distinct approach. Instead of implicit neural networks or rigid meshes, a 3D scene is represented by millions of small, explicit 3D Gaussian particles <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Each Gaussian possesses parameters such as position, orientation, scale, opacity, and view-dependent color <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

Key advantages of [[Gaussian splatting and its advantages | Gaussian Splats]] include:
*   **Speed**: They are significantly faster for reconstruction and real-time rendering compared to [[Comparison of 3D gaussian splatting to neural radiance fields | NeRFs]] <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. Generation times for textured meshes can be as low as two minutes on a consumer GPU <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   **Explicitness**: Unlike implicit NeRFs, [[Gaussian splatting and its advantages | Gaussian Splats]] explicitly store 3D information, making them directly manipulable <a class="yt-timestamp" data-t="00:41:35">[00:41:35]</a>. This allows for compositional operations like deleting parts of a scene or merging objects <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>.
*   **Quality**: They achieve high-quality and detailed scene reconstruction, particularly excelling in high-frequency details (fine textures) compared to older methods <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>, which often result in "overly smooth" geometry <a class="yt-timestamp" data-t="01:30:08">[01:30:08]</a>.

## Applications and Future Prospects
The rapid development in [[3D Gaussian Splatting and Instant Splat Pipeline | 3D Gaussian Splatting]] is already leading to novel applications:

### Text-to-3D Generation
Recent papers like "DreamGaussian" and "Text to 3D using Gaussian Splatting" (also known as GSGen) demonstrate the ability to generate 3D content from text prompts <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. These methods often employ a multi-stage optimization process leveraging 2D diffusion models (like Stable Diffusion) and 3D point cloud diffusion priors (like Point-E or 0123) with a technique called Score Distillation Sampling (SDS) <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>, <a class="yt-timestamp" data-t="00:47:31">[00:47:31]</a>.

One significant challenge in text-to-3D generation is the "Janus problem," where generated 3D objects may have distorted or multiple faces due to the bias of 2D diffusion models towards frontal views <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>. Incorporating 3D priors (e.g., from Point-E) helps mitigate this, but it is not entirely eliminated <a class="yt-timestamp" data-t="01:13:13">[01:13:13]</a>.

### VR, AR, and Game Engines
The explicitness and real-time rendering capabilities of [[Gaussian splatting and its advantages | Gaussian Splats]] make them ideal candidates for immersive technologies <a class="yt-timestamp" data-t="01:57:39">[01:57:39]</a>. There's a strong hypothesis that future game engines will directly utilize [[Gaussian splatting and its advantages | Splats]] instead of meshes and textures, potentially streamlining content creation and interaction <a class="yt-timestamp" data-t="01:58:20">[01:58:20]</a>.

### 3D Printing and Manufacturing
While currently 3D printing relies on mesh formats like STL <a class="yt-timestamp" data-t="01:13:08">[01:13:08]</a>, there's a possibility that [[Applications and Future Prospects of Gaussian Surfels | Gaussian Splats]] could directly inform additive manufacturing processes. The inherent volume and density information within [[Gaussian splatting and its advantages | Splats]] might make them a more intuitive representation for creating physical objects, potentially bypassing the need to convert to meshes <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>, <a class="yt-timestamp" data-t="01:25:01">[01:25:01]</a>.

## [[Challenges and Advantages of Gaussian Surfels | Current Challenges and Future Outlook]]
Despite their advantages, current [[goshan_splat_optimization_for_3d_reconstruction | Gaussian Splatting]] implementations for generative tasks face some challenges:
*   **Baked Lighting**: Many current models produce "baked lighting" because they don't use spherical harmonics for view-dependent color, limiting dynamic lighting effects <a class="yt-timestamp" data-t="01:43:35">[01:43:35]</a>.
*   **Hyperparameter Dependency**: The refinement stages often rely on hard-coded thresholds and hyperparameters for densification and pruning, which may need to be fine-tuned for different scenes <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>.
*   **Complexity of Prompts**: Generating complex scenes with intricate logic from text prompts is still challenging due to limitations in language understanding of underlying models like Point-E and CLIP encoders <a class="yt-timestamp" data-t="01:36:09">[01:36:09]</a>.

However, the field is rapidly advancing. It's anticipated that [[Gaussian splatting and its advantages | Gaussian Splat]] generation will become even faster, potentially taking mere seconds <a class="yt-timestamp" data-t="01:17:22">[01:17:22]</a>. The explicit nature of Splats also suggests natural extensions for tasks like object removal using models such as the Segment Anything Model (SAM) <a class="yt-timestamp" data-t="02:00:17">[02:00:17]</a>. The ongoing research and rapid adoption indicate that [[Gaussian splatting and its advantages | Gaussian Splats]] are poised to become the new standard for 3D content creation and interaction across various industries.