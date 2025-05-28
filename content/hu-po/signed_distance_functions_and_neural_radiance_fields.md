---
title: Signed distance functions and neural radiance fields
videoId: azCp-b7c-GM
---

From: [[hu-po]] <br/> 

The field of 3D asset generation faces a significant challenge in determining an efficient and easy-to-use representation for 3D assets <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. Unlike 2D images or audio, which have natural fixed-size tensor representations, 3D assets lack such an obvious format <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. Researchers are exploring various methods, including [[neural_volume_rendering_and_radiance_fields | Neural Radiance Fields (NeRFs)]] and Signed Distance Functions (SDFs), as powerful ways to represent and generate complex 3D shapes <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.

## [[neural_volume_rendering_and_radiance_fields | Neural Radiance Fields (NeRFs)]]

[[neural_volume_rendering_and_radiance_fields | Neural Radiance Fields]] are a method for representing a 3D scene as an [[3d_implicit_functions_and_generative_models | implicit function]] <a class="yt-timestamp" data-t="18:32:00">[18:32:00]</a>. A NeRF is a neural network that, given a 3D spatial coordinate (X) and a viewing direction (D), outputs the color (C) and a non-negative density value (Sigma) for that point <a class="yt-timestamp" data-t="18:42:00">[18:42:00]</a>. The color output is dependent on the view direction, while the density is not <a class="yt-timestamp" data-t="21:26:00">[21:26:00]</a>.

### Rendering Process
To render a novel view of a scene using a NeRF, the viewport is treated as a grid of rays. Each pixel in the viewport is assigned a ray extending from the camera origin <a class="yt-timestamp" data-t="21:34:00">[21:34:00]</a>. The NeRF function is queried at multiple points along each ray to obtain color and density information. These values are then integrated using a process called ray marching to approximate the final RGB color for each pixel <a class="yt-timestamp" data-t="22:42:00">[22:42:00]</a>.

The density value (Sigma) along a ray indicates how "see-through" a point is; higher density means less transparency, often spiking when the ray hits an object's surface <a class="yt-timestamp" data-t="26:03:00">[26:03:00]</a>. Techniques like two-stage rendering (coarse and fine sampling) are used to efficiently sample points along the ray, focusing more samples in areas of high density <a class="yt-timestamp" data-t="25:34:00">[25:34:00]</a>.

### Advantages and Challenges
*   **Resolution Independence:** NeRFs are resolution-independent, meaning they can be queried at arbitrary input points rather than encoding information in a fixed grid <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
*   **Differentiability:** They are end-to-end differentiable, making them suitable for various downstream tasks like style transfer or differentiable shape editing <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.
*   **Performance:** A notable challenge with NeRFs is their rendering speed, often being very slow <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>.
*   **Scene Specificity:** Traditionally, a new NeRF model needs to be trained for every single 3D scene, which makes them very cumbersome to use <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>. Researchers aim to develop generalizable NeRF models that can generate many scenes from a single model <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>.

## Signed Distance Functions (SDFs)

Signed Distance Functions (SDFs) are another classic way to represent a 3D shape as a scalar field <a class="yt-timestamp" data-t="29:35:00">[29:35:00]</a>. An SDF maps a 3D coordinate (X) to a scalar value (D), which represents the shortest distance from X to the nearest point on the surface of the shape <a class="yt-timestamp" data-t="29:42:00">[29:42:00]</a>.

### Definition and Properties
The "signed" aspect of an SDF is crucial:
*   If D is negative, the point is inside the shape <a class="yt-timestamp" data-t="30:26:00">[30:26:00]</a>.
*   If D is positive, the point is outside the shape <a class="yt-timestamp" data-t="30:26:00">[30:26:00]</a>.
*   If D is zero, the point lies exactly on the surface of the shape, defining its boundary <a class="yt-timestamp" data-t="30:36:00">[30:36:00]</a>.

Methods like marching cubes or marching tetrahedra can be used to construct 3D meshes from an SDF's zero-level set (where D=0) <a class="yt-timestamp" data-t="31:10:00">[31:10:00]</a>. These techniques allow converting the implicit SDF representation into an explicit mesh format commonly used in game engines and CGI <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.

## Signed Texture Fields (STFs) - A Hybrid Approach

New models, such as Shape-E, introduce a variant called Signed Texture Fields (STFs) <a class="yt-timestamp" data-t="28:38:00">[28:38:00]</a>. An STF is an [[3d_implicit_functions_and_generative_models | implicit function]] that produces both a signed distance value and texture colors for a given point <a class="yt-timestamp" data-t="28:47:00">[28:47:00]</a>. While traditional SDFs only output distance, STFs extend this by also providing RGB color information <a class="yt-timestamp" data-t="35:18:00">[35:18:00]</a>. This allows for rendering the asset as both textured meshes and [[neural_volume_rendering_and_radiance_fields | neural Radiance Fields]] <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

## Context in Generative Models

Generative models like OpenAI's Shape-E leverage these [[3d_implicit_functions_and_generative_models | implicit functions]] for 3D asset generation <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>. Shape-E, a follow-up to Point-E, generates conditional 3D [[3d_implicit_functions_and_generative_models | implicit functions]] from text prompts <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. Unlike earlier approaches that produce a single output representation (e.g., point clouds), Shape-E directly generates the parameters of implicit functions <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

Shape-E trains an encoder that maps 3D assets into the parameters of an [[3d_implicit_functions_and_generative_models | implicit function]], and then uses a [[conditional_diffusion_models_for_neural_networks | conditional diffusion model]] to generate these parameters <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>. This unique approach involves the encoder outputting the weights of a multi-layer perceptron (MLP), which then acts as both a NeRF and an STF <a class="yt-timestamp" data-t="01:10:02">[01:10:02]</a>. This allows for rendering in multiple ways and importing into various 3D applications <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a>.

Despite advancements, the quality of generated 3D assets from models like Shape-E still falls short of optimization-based approaches <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. However, they offer orders of magnitude faster inference times <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. The choice of 3D representation remains a key area of heterogeneity and ongoing research in the field <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.