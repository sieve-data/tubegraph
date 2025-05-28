---
title: Challenges and solutions in representing 3D objects with gaussian splatting
videoId: l956ye13F8M
---

From: [[hu-po]] <br/> 

## Introduction to Gaussian Splatting

[[3D Gaussian Splats for Radiance Field Rendering | Gaussian splatting]] is a relatively new technique for representing 3D objects and scenes, gaining popularity for its effectiveness, speed, and simplicity compared to prior methods like [[3D representation techniques Nerfs vs Gausssian Splats | Neural Radiance Fields (Nerfs)]] <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Unlike Nerfs, which implicitly store 3D information within a neural network's weights <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>, [[3D Gaussian Splats for Radiance Field Rendering | Gaussian splatting]] explicitly represents a 3D scene using millions of individual 3D gaussians <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Each of these gaussians is defined by its position, orientation, scale, opacity, and a view-dependent color <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. This explicit nature allows for easier manipulation and compositional operations on the 3D objects <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>.

The rise of [[3D Gaussian Splats for Radiance Field Rendering | Gaussian splatting]] has led to new research in [[3D content generation using gaussian splatting | 3D content generation]], particularly in text-to-3D models. Two recent papers, "DreamGaussian" and "Text to 3D using Gaussian Splatting" (also known as "GSGen"), both explore using [[3D Gaussian Splats for Radiance Field Rendering | Gaussian splatting]] for this task <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. These papers highlight several challenges and proposed solutions in this burgeoning field.

## Challenges in Representing 3D Objects with Gaussian Splatting

### 1. Slow Per-Sample Optimization

Traditional [[3D content generation using gaussian splatting | 3D generation methods]], particularly those based on Nerfs, often involve slow per-sample optimization <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. This means that a new neural network must be trained for every unique 3D object one wishes to generate <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>, making the process time-consuming and limiting practical usage <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

### 2. The "Janus Problem"

A significant challenge in text-to-3D generation from 2D diffusion models is the "Janus problem" <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>. This refers to the tendency for generated 3D objects to have multiple "faces" or inconsistent geometry when viewed from different angles, similar to the Roman god Janus who had two faces <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>. This occurs because 2D diffusion models are often biased towards frontal views of objects, lacking sufficient data or understanding of how objects appear from the back or sides <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>, <a class="yt-timestamp" data-t="01:35:37">[01:35:37]</a>.

### 3. Blurry Appearance and Over-Smoothing

Generated gaussians can often appear blurry <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. This blurriness can be attributed to the ambiguity of the Score Distillation Sampling (SDS) loss, which may provide inconsistent 3D guidance during optimization, making it difficult for the algorithm to correctly densify under-reconstructed regions or prune over-reconstructed ones <a class="yt-timestamp" data-t="01:09:07">[01:09:07]</a>, <a class="yt-timestamp" data-t="01:17:11">[01:17:11]</a>. Furthermore, some mesh-based methods can yield "overly smooth" geometry, resulting in an unnatural appearance <a class="yt-timestamp" data-t="01:30:07">[01:30:07]</a>.

### 4. Arbitrary Hard-Coded Thresholds

The densification and pruning strategies in [[3D Gaussian Splats for Radiance Field Rendering | Gaussian splatting]] often rely on hard-coded thresholds <a class="yt-timestamp" data-t="01:13:42">[01:13:42]</a>. These arbitrary values, such as distances for splitting gaussians or opacity thresholds for removal, are empirically determined and may not generalize well across different scenes or objects, potentially leading to excessive gaussians or blurry results <a class="yt-timestamp" data-t="01:14:03">[01:14:03]</a>.

### 5. "Baked Lighting" and Lack of View-Dependence

In simpler [[3D Gaussian Splats for Radiance Field Rendering | Gaussian splatting]] implementations for text-to-3D, such as those discussed, the color of individual gaussians might be fixed (a "simple diffuse color") rather than view-dependent <a class="yt-timestamp" data-t="00:44:09">[00:44:09]</a>. This leads to "baked lighting," where shadows and lighting effects are static and cannot be changed or interacted with dynamically <a class="yt-timestamp" data-t="01:43:35">[01:43:35]</a>. Spherical harmonics are a technique that could address this, but it's not implemented in these initial papers <a class="yt-timestamp" data-t="00:44:20">[00:44:20]</a>, <a class="yt-timestamp" data-t="01:43:37">[01:43:37]</a>.

### 6. Integration with Traditional 3D Formats

For immediate downstream applications in existing game engines or CGI pipelines (like Blender), there's a need to convert [[3D Gaussian Splats for Radiance Field Rendering | Gaussian splatting]] representations into traditional mesh and texture formats <a class="yt-timestamp" data-t="01:02:53">[01:02:53]</a>. This conversion process itself can be a challenge, as it's a relatively unexplored problem <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>, and the resulting UV maps may be "gross" or unintuitive for human artists <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>.

## Solutions and Approaches

### 1. Multi-Stage Optimization and Efficiency

Both "DreamGaussian" and "GSGen" adopt a multi-stage optimization process to achieve efficiency and quality <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>, <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.
*   **DreamGaussian:** Involves a Stage One (geometry optimization) and a Stage Two (refinement) <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. This approach can generate high-quality textured meshes in as little as two minutes on a single consumer-grade GPU (e.g., 8 GB of VRAM) <a class="yt-timestamp" data-t="01:39:18">[01:39:18]</a>, achieving approximately 10 times acceleration compared to existing methods <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   **GSGen:** Also uses a two-stage process: Geometry Optimization and Appearance Refinement <a class="yt-timestamp" data-t="00:58:02">[00:58:02]</a>.

### 2. Leveraging 3D Priors for Geometry Consistency

To combat the Janus problem and improve geometry accuracy, both papers integrate 3D priors with 2D diffusion models using Score Distillation Sampling (SDS) <a class="yt-timestamp" data-t="01:33:01">[01:33:01]</a>.
*   **GSGen:** Initializes [[3D Gaussian Splats for Radiance Field Rendering | Gaussian splatting]] positions using a point cloud generated by Point-E, an OpenAI model that creates 3D point clouds from text prompts <a class="yt-timestamp" data-t="00:59:17">[00:59:17]</a>, <a class="yt-timestamp" data-t="01:19:17">[01:19:17]</a>. This provides a stronger initial 3D geometry compared to a simple sphere <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>, <a class="yt-timestamp" data-t="01:17:31">[01:17:31]</a>. However, Point-E's color patterns are simple, so random color initialization is preferred <a class="yt-timestamp" data-t="01:19:30">[01:19:30]</a>.
*   **DreamGaussian:** Initially uses a simple grey sphere of points as a prior <a class="yt-timestamp" data-t="00:59:59">[00:59:59]</a>, which limits it to generating object-centric scenes with rotational or bilateral symmetry <a class="yt-timestamp" data-t="01:32:35">[01:32:35]</a>.
*   **View-Conditioned Diffusion Models:** Models like 0-1-2-3-XL (trained on the Objaverse dataset) or Point-E are used. These models are conditioned on camera viewpoint, allowing them to generate consistent views of an object from different angles, which helps prevent the Janus problem <a class="yt-timestamp" data-t="00:27:25">[00:27:25]</a>, <a class="yt-timestamp" data-t="00:31:15">[00:31:15]</a>.

### 3. Progressive Densification and Refinement

To improve detail and continuity, both methods employ iterative refinement strategies:
*   **GSGen:** Uses "compactness-based densification" and pruning <a class="yt-timestamp" data-t="01:14:23">[01:14:23]</a>, which involves adding more gaussians in dense areas and removing unnecessary ones <a class="yt-timestamp" data-t="01:20:17">[01:20:17]</a>. This helps fill holes and achieve a more complete geometric structure <a class="yt-timestamp" data-t="01:19:18">[01:19:18]</a>. The SDS gradients are primarily used to adjust the positions of gaussians <a class="yt-timestamp" data-t="01:10:14">[01:10:14]</a>.
*   **DreamGaussian:** Also progressively densifies 3D gaussians, which converges significantly faster for 3D generative tasks <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

### 4. Adaptive Loss Weighting

"DreamGaussian" adjusts the weights of its regularization losses (Lambda RGB and Lambda A) by linearly increasing them during training <a class="yt-timestamp" data-t="01:29:30">[01:29:30]</a>. This allows for better convergence and refinement of details as the optimization progresses.

### 5. Mesh Extraction and Texture Refinement (DreamGaussian)

To make generated objects compatible with existing 3D pipelines, "DreamGaussian" uniquely includes a mesh extraction and texture refinement step <a class="yt-timestamp" data-t="01:27:27">[01:27:27]</a>.
*   It uses the marching cubes algorithm, an older technique, to convert the 3D gaussians into a polygonal mesh <a class="yt-timestamp" data-t="01:05:38">[01:05:38]</a>.
*   It then applies a "texture refinement in UV space," which involves using a diffusion model to clean up and enhance the 2D texture map that is wrapped onto the mesh <a class="yt-timestamp" data-t="01:28:22">[01:28:22]</a>, <a class="yt-timestamp" data-t="01:28:30">[01:28:30]</a>.

While this conversion provides "ready-to-use 3D assets" <a class="yt-timestamp" data-t="01:43:23">[01:43:23]</a>, the speaker suggests that meshes and UV maps might become obsolete in the future, advocating for direct use and manipulation of [[3D Gaussian Splats for Radiance Field Rendering | Gaussian splatting]] in game engines and other applications <a class="yt-timestamp" data-t="01:58:19">[01:58:19]</a>.

## Conclusion

The rapid advancements in [[3D Gaussian Splats for Radiance Field Rendering | Gaussian splatting]] are pushing the boundaries of [[3D content generation using gaussian splatting | 3D content creation]]. While challenges like the "Janus problem," blurry details, and the need for arbitrary thresholds persist, innovations in leveraging 3D priors, multi-stage optimization, and progressive densification are providing promising solutions. The explicit nature of [[3D Gaussian Splats for Radiance Field Rendering | Gaussian splatting]] also opens up new possibilities for directly manipulating and using 3D content in various applications, potentially bypassing the need for traditional mesh and texture formats in the long term <a class="yt-timestamp" data-t="01:58:19">[01:58:19]</a>.