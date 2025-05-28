---
title: 3D Gaussian splatting and Nerfs
videoId: JdfrG89iPOA
---

From: [[hu-po]] <br/> 

This article explores two prominent [[3D representation techniques Nerfs vs Gausssian Splats | 3D representation techniques]]: [[3D Gaussian Splats for Radiance Field Rendering | 3D Gaussian Splatting]] (3DGS) and Neural Radiance Fields (NeRFs), highlighting their characteristics, applications, and distinctions in the field of computer vision. The discussion also touches upon the ongoing "war" between these two methods <a class="yt-timestamp" data-t="07:47:33">[07:47:33]</a>.

## [[3D Gaussian Splats for Radiance Field Rendering | 3D Gaussian Splatting]]

[[3D Gaussian Splats for Radiance Field Rendering | 3D Gaussian Splatting]] is a [[3D representation techniques Nerfs vs Gausssian Splats | 3D representation]] method that constructs a scene from a collection of "little 3D Gaussian Splats" <a class="yt-timestamp" data-t="07:54:19">[07:54:19]</a>. These can be thought of as small, scattered bubbles or ellipses that collectively form the [[3D representation techniques Nerfs vs Gausssian Splats | 3D scene]] <a class="yt-timestamp" data-t="07:57:33">[07:57:33]</a>.

### Parameters of a Gaussian Splat
Each individual [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splat]] is defined by several properties <a class="yt-timestamp" data-t="15:54:20">[15:54:20]</a>:
*   **Position (X):** The 3D coordinates (x, y, z) of the splat's center <a class="yt-timestamp" data-t="15:27:07">[15:27:07]</a>.
*   **Covariance Matrix:** Defines the shape and orientation of the splat, indicating how ellipsoidal it is <a class="yt-timestamp" data-t="15:33:55">[15:33:55]</a>. This is decomposed into rotation and scaling parameters <a class="yt-timestamp" data-t="28:50:00">[28:50:00]</a>.
*   **Spherical Harmonic (SH) Coefficients:** Used to capture view-dependent appearance and color <a class="yt-timestamp" data-t="27:26:00">[27:26:00]</a>. This means a splat can appear differently when viewed from various angles, accounting for reflections or material properties <a class="yt-timestamp" data-t="26:48:46">[26:48:46]</a>.
*   **Opacity (Alpha):** A single number representing the "see-through" quality of the individual splat <a class="yt-timestamp" data-t="28:42:25">[28:42:25]</a>.

The process of [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splatting]] involves optimizing these properties by pushing gradients directly into them over a series of steps <a class="yt-timestamp" data-t="16:03:00">[16:03:00]</a>. This allows for continuous refinement of the [[3D representation techniques Nerfs vs Gausssian Splats | 3D scene]] <a class="yt-timestamp" data-t="16:07:00">[16:07:00]</a>.

### Rendering in 3DGS
[[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splatting]] utilizes a fully differentiable rendering process. This is crucial for enabling backpropagation of gradients from the rendered image to the splats' parameters <a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a>. Key to its speed is a fast sorting mechanism, often using a single fast GPU radix sort, which sorts splats based on their distance from the camera view <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>. Opacity plays a role in efficiently rendering the scene, as splats behind opaque ones don't need to be fully rendered <a class="yt-timestamp" data-t="01:13:35">[01:13:35]</a>.

### Advantages and Disadvantages
*   **Advantages:**
    *   **Explicit Representation:** [[3D Gaussian Splats for Radiance Field Rendering | 3DGS]] is an explicit [[3D representation techniques Nerfs vs Gausssian Splats | 3D representation]], meaning the splats themselves constitute the object <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>. This makes them easier to compose, allowing for removal or addition of objects in a scene <a class="yt-timestamp" data-t="01:36:23">[01:36:23]</a>.
    *   **Speed:** Modern 3DGS pipelines, like Instant-Splat, can generate [[3D representation techniques Nerfs vs Gausssian Splats | 3D models]] rapidly, often in under a minute on a consumer GPU <a class="yt-timestamp" data-t="01:00:27">[01:00:27]</a>, significantly faster than traditional methods like NeRFs <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

*   **Disadvantages:**
    *   **File Size:** As an explicit representation, [[3D Gaussian Splats for Radiance Field Rendering | 3DGS]] models can result in larger file sizes, making them heavier to transfer or load <a class="yt-timestamp" data-t="01:35:54">[01:35:54]</a>.
    *   **Amorphous Objects:** Representing amorphous objects like smoke or fire can be more challenging with discrete ellipsoids <a class="yt-timestamp" data-t="01:36:03">[01:36:03]</a>.

## Neural Radiance Fields (NeRFs)

Neural Radiance Fields (NeRFs) are another method for [[3D representation techniques Nerfs vs Gausssian Splats | 3D scene]] synthesis, but they rely on an implicit representation. A NeRF is essentially a "little multi-layer perceptron" (a type of neural network) that defines a field <a class="yt-timestamp" data-t="01:15:54">[01:15:54]</a>.

### How NeRFs Work
A NeRF takes as input the position in 3D space and the view direction of a camera <a class="yt-timestamp" data-t="01:15:57">[01:15:57]</a>. It then projects rays into a volume of space. For each point along these rays, the NeRF is queried to output a color and an opacity value <a class="yt-timestamp" data-t="01:16:06">[01:16:06]</a>. This process is differentiable, allowing gradients to be backpropagated into the weights of the neural network during training <a class="yt-timestamp" data-t="01:16:47">[01:16:47]</a>.

### Advantages and Disadvantages
*   **Advantages:**
    *   **Compactness:** The primary advantage of a NeRF is its very small size, as it's just a trained neural network. This makes it efficient for transmission and loading on devices with limited compute, such as VR headsets <a class="yt-timestamp" data-t="01:35:09">[01:35:09]</a>.
    *   **Amorphous Objects:** Due to their implicit nature, NeRFs are often better at modeling translucent or amorphous objects like smoke, fog, or reflections <a class="yt-timestamp" data-t="01:35:36">[01:35:36]</a>.

*   **Disadvantages:**
    *   **Implicit Representation:** Unlike [[3D Gaussian Splats for Radiance Field Rendering | 3DGS]], a NeRF is an implicit representation; the [[3D representation techniques Nerfs vs Gausssian Splats | 3D object]] itself is not directly defined by discrete points but rather by the learned function of the neural network <a class="yt-timestamp" data-t="01:17:09">[01:17:09]</a>. This can make them less intuitive to manipulate or compose.
    *   **Training Requirements:** NeRFs often require a dense set of multi-view images and precise camera poses (intrinsics and extrinsics) for effective training <a class="yt-timestamp" data-t="01:19:19">[01:19:19]</a>. Obtaining this ground truth camera information can be challenging in real-world scenarios <a class="yt-timestamp" data-t="01:19:40">[01:19:40]</a>.

## [[Comparison of Gaussian Splats and Neural Radiance Fields NeRFs | Comparison and Integration]]

### Explicit vs. Implicit
The key [[Comparison of Gaussian Splats and Neural Radiance Fields NeRFs | difference]] lies in their representation:
*   [[3D Gaussian Splats for Radiance Field Rendering | 3DGS]] uses an **explicit** representation, where the [[3D representation techniques Nerfs vs Gausssian Splats | 3D object]] is directly defined by a set of discrete, manipulable Gaussian splats <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>.
*   NeRFs use an **implicit** representation, where the [[3D representation techniques Nerfs vs Gausssian Splats | 3D scene]] is encoded within the weights of a neural network, evaluated as a function in space <a class="yt-timestamp" data-t="01:17:09">[01:17:09]</a>.

### Workflow Differences
Traditional NeRF pipelines often rely on pre-processing steps, like those found in COLMAP (a Structure from Motion pipeline), to estimate camera parameters and dense point clouds <a class="yt-timestamp" data-t="02:23:44">[02:23:44]</a>. This can be time-consuming and prone to errors <a class="yt-timestamp" data-t="02:23:44">[02:23:44]</a>.

In contrast, recent advancements like Instant-Splat, leverage models like Duster, which can estimate camera intrinsics and extrinsics and generate dense point maps directly from uncalibrated and unposed images, significantly streamlining the process <a class="yt-timestamp" data-t="01:44:56">[01:44:56]</a>. This removes the need for detailed camera information typically required by NeRFs <a class="yt-timestamp" data-t="01:19:40">[01:19:40]</a>.

### Combined Approaches
While often seen as competing techniques, there are instances where NeRFs and [[3D Gaussian Splats for Radiance Field Rendering | 3DGS]] are combined. For example, some approaches use a NeRF to initialize or supervise the [[3D Gaussian Splats for Radiance Field Rendering | Gaussian Splatting]] process <a class="yt-timestamp" data-t="01:18:04">[01:18:04]</a>. This might involve using the NeRF's density output to determine where to place initial splats or using its rendering capabilities to provide additional supervisory signals during the [[3D Gaussian Splats for Radiance Field Rendering | 3DGS]] optimization <a class="yt-timestamp" data-t="01:18:53">[01:18:53]</a>. An example of such a paper is "RadSplat" <a class="yt-timestamp" data-t="01:15:14">[01:15:14]</a>.