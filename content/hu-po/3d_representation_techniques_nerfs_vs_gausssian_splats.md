---
title: 3D representation techniques Nerfs vs Gausssian Splats
videoId: IsRHGf2rGCs
---

From: [[hu-po]] <br/> 

The field of generative 3D modeling is rapidly advancing, with significant progress being made in creating 3D assets from text and images <a class="yt-timestamp" data-t="02:29:37">[02:29:37]</a>. Two prominent 3D representation techniques emerging in this domain are Neural Radiance Fields (Nerfs) and Gaussian Splats <a class="yt-timestamp" data-t="03:17:01">[03:17:01]</a>.

## Neural Radiance Fields (Nerfs)

Neural Radiance Fields (Nerfs) are implicit representations, meaning they define a field approximated by a neural network, typically a Multi-Layer Perceptron (MLP) <a class="yt-timestamp" data-t="01:27:17">[01:27:17]</a>. This function can be evaluated at any point in space, theoretically offering infinite resolution <a class="yt-timestamp" data-t="01:37:39">[01:37:39]</a>.

### Characteristics and Usage
*   **Implicit Representation**: A Nerf is a neural network that approximates a function defining a field <a class="yt-timestamp" data-t="01:37:32">[01:37:32]</a>. It can output properties like color and radiance, or a signed distance function (SDF), at any given 3D coordinate <a class="yt-timestamp" data-t="01:22:42">[01:22:42]</a>.
*   **Triplane Nerfs**: Many recent papers utilize a triplane representation to condition a Nerf <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>. This involves storing features on three axis-aligned or orthogonal planes, which are then combined to get a feature vector for any point in 3D space <a class="yt-timestamp" data-t="01:10:03">[01:10:03]</a>.
*   **Conversion to Mesh**: While Nerfs are implicit, they can be converted into explicit representations like meshes using techniques such as Marching Cubes <a class="yt-timestamp" data-t="01:17:07">[01:17:07]</a>, or Marching Cubes and DM-Tet <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>.
*   **Inference Speed**: Some Nerf-based methods can generate a 3D asset from a single image in seconds, such as the V-Fusion 3D paper <a class="yt-timestamp" data-t="01:22:26">[01:22:26]</a>.

### Perceived Limitations
*   **Representational Capacity**: While theoretically infinite resolution, the practical representation quality can be limited by the capacity of the underlying MLP <a class="yt-timestamp" data-t="03:10:07">[03:10:07]</a>. This can lead to fuzzy artifacts and difficulties in capturing fine details <a class="yt-timestamp" data-t="02:07:22">[02:07:22]</a>.
*   **Optimization-based**: Many Nerf methods involve per-instance optimization, meaning a multi-step process of pushing gradients into the representation for each generated 3D object <a class="yt-timestamp" data-t="01:55:52">[01:55:52]</a>.

## Gaussian Splats

[[3D Gaussian Splats for Radiance Field Rendering | 3D Gaussian Splats for Radiance Field Rendering]] (often shortened to Gaussian Splats) provide an explicit 3D representation that consists of a set of individual 3D Gaussians <a class="yt-timestamp" data-t="03:10:35">[03:10:35]</a>. Each Gaussian has properties such as XYZ position, rotation, color, and opacity <a class="yt-timestamp" data-t="03:06:56">[03:06:56]</a>.

### Characteristics and Usage
*   **Explicit Representation**: Unlike Nerfs, Gaussian Splats directly store properties for each component, making them explicit <a class="yt-timestamp" data-t="03:10:35">[03:10:35]</a>.
*   **4D Gaussian Splats**: The concept extends to [[3d_modeling_and_tracking_using_gaussian_splatting | 4D Gaussian Splats]], which add the time dimension, meaning a 3D Gaussian Splat that varies over time, similar to a sequence of 3D Gaussian Splats <a class="yt-timestamp" data-t="03:32:02">[03:32:02]</a>. These can capture motion and dynamics <a class="yt-timestamp" data-t="03:17:15">[03:17:15]</a>.
*   **Optimization**: The properties of individual Gaussians can be optimized by pushing gradients from reconstruction losses, allowing for precise positioning and rotation <a class="yt-timestamp" data-t="03:07:54">[03:07:54]</a>.
*   **Quality and Efficiency**: [[3d_gaussian_splatting_and_nerfs | Gaussian Splats]] are highlighted for their efficiency and ability to handle dynamic content <a class="yt-timestamp" data-t="03:17:15">[03:17:15]</a>. Some papers suggest [[challenges_and_solutions_in_representing_3d_objects_with_gaussian_splatting | Gaussian Splats]] have a much higher representational capacity than Nerfs, leading to better quality and finer details in rendered outputs <a class="yt-timestamp" data-t="03:10:03">[03:10:03]</a>.
*   **Conversion to Mesh**: Like Nerfs, Gaussian Splats can also be converted into meshes if desired <a class="yt-timestamp" data-t="03:14:02">[03:14:02]</a>.

## Comparison and Future Outlook

The choice between Nerfs and [[3d_modeling_and_tracking_using_gaussian_splatting | Gaussian Splats]] often depends on the specific goals of the generative model <a class="yt-timestamp" data-t="03:17:23">[03:17:23]</a>.
*   **Representational Trade-offs**: Nerfs are seen as potentially better for fine detail due to their continuous nature, while [[3d_gaussian_splatting_and_nerfs | Gaussian Splats]] offer advantages in efficiency and scalability <a class="yt-timestamp" data-t="03:17:27">[03:17:27]</a>. However, the speaker believes [[3d_gaussian_splatting_and_nerfs | Gaussian Splats]] will scale better and achieve sufficient quality for fine detail, potentially rendering Nerfs' "infinite resolution" less relevant in practice <a class="yt-timestamp" data-t="03:18:17">[03:18:17]</a>.
*   **Explicit vs. Implicit**: [[comparison_between_gaussian_splats_and_traditional_3d_representation_methods | Gaussian Splats]] are explicit, making them potentially more adaptable to scaling than the implicit nature of Nerfs <a class="yt-timestamp" data-t="03:10:31">[03:10:31]</a>.

### The Future of Generative 3D Models
The speaker predicts that the [[potential_future_of_meshbased_models_versus_gaussian_splats_in_virtual_environments | future of 3D generative models]] will increasingly leverage video diffusion models, such as Sora, as the primary source of signal <a class="yt-timestamp" data-t="03:23:01">[03:23:01]</a>. This is because video data sets are the largest available, offering a rich source for learning 3D properties <a class="yt-timestamp" data-t="03:23:04">[03:23:04]</a>.

It is speculated that the future generative 3D model will:
*   Be based on [[3d_modeling_and_tracking_using_gaussian_splatting | Gaussian Splats]], particularly [[physicsbased_modeling_in_gaussian_splats | 4D Gaussian Splats]], capable of representing objects and their movement over time <a class="yt-timestamp" data-t="02:00:04">[02:00:04]</a>, <a class="yt-timestamp" data-t="03:27:02">[03:27:02]</a>.
*   Move away from legacy formats like textures and meshes <a class="yt-timestamp" data-t="00:43:43">[00:43:43]</a>.
*   Integrate human feedback and preference tuning, similar to RLF (Reinforcement Learning from Human Feedback) in language models <a class="yt-timestamp" data-t="02:46:52">[02:46:52]</a>, <a class="yt-timestamp" data-t="03:27:37">[03:27:37]</a>.
*   Overcome the [[challenges_and_solutions_in_representing_3d_objects_with_gaussian_splatting | object-centric bias]] prevalent in current 3D datasets like Objaverse <a class="yt-timestamp" data-t="02:24:01">[02:24:01]</a>.
*   Be highly efficient, potentially running on mobile or VR devices in real-time, necessitating feed-forward models over multi-step optimization processes <a class="yt-timestamp" data-t="03:28:03">[03:28:03]</a>.
*   Feature interactive and intuitive user interfaces, possibly involving voice commands, gestures, or even brain signals for direct 3D content generation <a class="yt-timestamp" data-t="03:25:24">[03:25:24]</a>, <a class="yt-timestamp" data-t="03:39:50">[03:39:50]</a>.

While current models are still "very slow" and quality isn't "100% there," significant progress is expected in the coming years, potentially leading to indistinguishable 3D quality from various inputs <a class="yt-timestamp" data-t="03:30:11">[03:30:11]</a>.