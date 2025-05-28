---
title: NeRFs versus Gaussian Splatting
videoId: JdfrG89iPOA
---

From: [[hu-po]] <br/> 

The field of 3D computer vision is continuously evolving, with [[neural_radiance_fields | Neural Radiance Fields]] (NeRFs) and [[gaussian_splatting_and_its_advantages | 3D Gaussian Splatting]] emerging as prominent techniques for [[3d_gaussian_splatting_for_realtime_radiance_field_rendering | realtime radiance field rendering]] and novel view synthesis <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. While both aim to generate new views of a 3D scene from a limited set of images, they differ fundamentally in their underlying representations and operational characteristics <a class="yt-timestamp" data-t="01:17:14">[01:17:14]</a>.

## [[gaussian_splatting_and_its_advantages | 3D Gaussian Splatting]]
[[gaussian_splatting_and_its_advantages | 3D Gaussian Splatting]] is an [[gaussian_splatting_and_its_advantages | explicit 3D representation]] <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>, meaning the 3D scene is directly composed of a set of individual 3D Gaussian "splats" <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. These splats can be thought of as small, adjustable bubbles or ellipses scattered throughout the scene <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

### Properties of a Gaussian Splat
Each Gaussian splat is parameterized by several properties:
*   **Position (mean vector)**: An XYZ coordinate in 3D space <a class="yt-timestamp" data-t="01:15:57">[01:15:57]</a>.
*   **Covariance Matrix**: Defines the shape and orientation of the Gaussian, influencing its ellipsoidal form <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>. This is decomposed into rotation and scaling parameters <a class="yt-timestamp" data-t="00:28:58">[00:28:58]</a>.
*   **Spherical Harmonic Coefficients (SH)**: Used to capture view-dependent color appearance, meaning the splat's color can change based on the viewing angle <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>.
*   **Opacity (Alpha)**: A single number representing the transparency or "see-through" of an individual Gaussian <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>.

The rendering process for [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] is fully differentiable, which is crucial for optimization <a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a>. It involves sorting the Gaussians based on their view position (distance to the camera) using a fast GPU radic sort algorithm <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>. This sorting and the progressive opacity accumulation contribute to its speed <a class="yt-timestamp" data-t="01:13:09">[01:13:09]</a>.

### Advantages of Gaussian Splatting
*   **Explicitness**: Being an explicit representation, [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] makes it easier to compose and manipulate scenes, such as removing or adding objects <a class="yt-timestamp" data-t="01:36:23">[01:36:23]</a>.
*   **Speed**: Its rendering process is noted for being significantly faster than NeRFs in many scenarios, especially with techniques like [[goshan_splat_optimization_for_3d_reconstruction | Gaussian Splat optimization]] and initializations from models like Duster <a class="yt-timestamp" data-t="01:03:53">[01:03:53]</a>.

### Disadvantages of Gaussian Splatting
*   **File Size**: Due to its explicit nature, a [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] scene can result in a larger file size compared to NeRFs <a class="yt-timestamp" data-t="01:35:54">[01:35:54]</a>.
*   **Modeling Amorphous Objects**: It can be less suitable for modeling amorphous objects like smoke or fire, which might be more challenging to represent convincingly with discrete ellipsoids <a class="yt-timestamp" data-t="01:36:03">[01:36:03]</a>.

## [[3d_gaussian_splatting_for_realtime_radiance_field_rendering | Neural Radiance Fields (NeRFs)]]
[[neural_radiance_fields | NeRFs]] are an [[comparisons_between_gaussian_splats_and_other_3d_representation_technologies | implicit 3D representation]] <a class="yt-timestamp" data-t="01:17:09">[01:17:09]</a>. Instead of directly representing the 3D scene, a NeRF is a small multi-layer perceptron (neural network) that acts as a continuous function <a class="yt-timestamp" data-t="01:16:15">[01:16:15]</a>. This function can be queried at any point in 3D space to return a color and an opacity value <a class="yt-timestamp" data-t="01:16:18">[01:16:18]</a>.

### How NeRFs Work
To render an image from a NeRF, rays are cast from the camera into the 3D scene. As each ray intersects the volume of space, the NeRF is queried at multiple points along the ray. The outputs (color and opacity) are then combined using a differentiable rendering process to form a pixel in the final image <a class="yt-timestamp" data-t="01:16:30">[01:16:30]</a>. Optimization involves back-propagating gradients to adjust the weights of the neural network <a class="yt-timestamp" data-t="01:17:06">[01:17:06]</a>.

### Advantages of NeRFs
*   **Compactness**: A significant advantage of NeRFs is their small file size, as they only require storing the weights of a small neural network <a class="yt-timestamp" data-t="01:34:30">[01:34:30]</a>. This makes them efficient for transmission and loading into devices with limited compute, such as VR headsets <a class="yt-timestamp" data-t="01:34:51">[01:34:51]</a>.
*   **Amorphous Objects**: They are generally better at modeling complex, amorphous phenomena like smoke, fog, or translucent objects due to their continuous, implicit nature <a class="yt-timestamp" data-t="01:35:38">[01:35:38]</a>.

### Disadvantages of NeRFs
*   **Initialization Requirements**: Training a NeRF often requires precise camera intrinsic and extrinsic information (focal length, principal point, pose) and typically a large number of dense viewpoints <a class="yt-timestamp" data-t="01:19:22">[01:19:22]</a>.
*   **Implicit Nature**: Because they are implicit, directly manipulating the 3D geometry of a NeRF scene (e.g., editing objects) is not as straightforward as with explicit representations <a class="yt-timestamp" data-t="01:17:54">[01:17:54]</a>.

## Key Differences and [[comparisons_between_gaussian_splats_and_other_3d_representation_technologies | Comparisons]]

| Feature              | [[gaussian_splatting_and_its_advantages | 3D Gaussian Splatting]]                 | [[neural_radiance_fields | Neural Radiance Fields (NeRFs)]]              |
| :------------------- | :-------------------------------------- | :------------------------------------ |
| **Representation**   | Explicit (set of 3D Gaussians) <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a> | Implicit (neural network function) <a class="yt-timestamp" data-t="01:17:09">[01:17:09]</a> |
| **File Size**        | Larger <a class="yt-timestamp" data-t="01:35:55">[01:35:55]</a>                                 | Smaller/Compressed <a class="yt-timestamp" data-t="01:35:11">[01:35:11]</a>           |
| **Rendering Speed**  | Faster (due to efficient sorting) <a class="yt-timestamp" data-t="01:12:45">[01:12:45]</a> | Generally slower (ray marching)     |
| **Scene Manipulation** | Easier (can compose/remove objects) <a class="yt-timestamp" data-t="01:36:25">[01:36:25]</a>  | Harder (implicit function)          |
| **Amorphous Objects**| Less suitable <a class="yt-timestamp" data-t="01:36:03">[01:36:03]</a>                      | Better <a class="yt-timestamp" data-t="01:35:38">[01:35:38]</a>                            |
| **Initialization**   | Can leverage models like Duster for uncalibrated input <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a> | Often requires known camera parameters and dense views <a class="yt-timestamp" data-t="01:19:22">[01:19:22]</a> |

## Hybrid Approaches
Researchers have explored combining aspects of both technologies. For instance, the RadSplat paper proposes using a [[neural_radiance_fields | NeRF]] to initialize and supervise [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] <a class="yt-timestamp" data-t="01:18:04">[01:18:04]</a>. In this approach, the NeRF's opacity outputs can guide the initialization of new Gaussians where scene density is high, and the NeRF can also provide target supervision for rendering <a class="yt-timestamp" data-t="01:18:53">[01:18:53]</a>. However, such methods might still inherit the NeRF's requirement for known camera parameters <a class="yt-timestamp" data-t="01:19:26">[01:19:26]</a>.

## Conclusion
While [[neural_radiance_fields | NeRFs]] offer highly compressed representations and excel at modeling subtle effects like translucency, their reliance on precise camera information and potentially longer training times can be a limitation for real-world, unconstrained scenarios. [[gaussian_splatting_and_its_advantages | 3D Gaussian Splatting]], especially when combined with robust initializers like Duster (as seen in the [[3d_gaussian_splatting_and_instant_splat_pipeline | Instant Splat Pipeline]]), provides a faster, more flexible approach to 3D reconstruction from sparse, uncalibrated input <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. The explicit nature of [[gaussian_splatting_and_its_advantages | Gaussian Splatting]] is seen as a significant advantage for composing and manipulating 3D objects, potentially leading to broader [[implications_of_gaussian_splatting_in_future_technologies | future applications]] <a class="yt-timestamp" data-t="01:36:30">[01:36:30]</a>.