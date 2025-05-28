---
title: Comparisons between Gaussian splats and other 3D representation technologies
videoId: l956ye13F8M
---

From: [[hu-po]] <br/> 

The field of 3D content creation and representation has seen significant advancements, moving from traditional methods to newer, more efficient techniques. Key technologies include the long-standing mesh and texture format, the more recent [[Comparison of 3D gaussian splatting to neural radiance fields | Neural Radiance Fields (Nerfs)]], and the emerging [[3D Gaussian Splatting and Instant Splat Pipeline | 3D Gaussian Splatting]].

## Traditional 3D Representation: Mesh and Texture

For a long time, and still predominantly in video games and CGI, 3D objects are represented using a combination of texture and mesh formats <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Mesh:** Represents the 3D model as a collection of vertices (dots) and polygons (often triangles) that form a specific surface <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. The entire 3D object is created from these interconnected polygons <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Texture:** A 2D image that "wraps" onto the mesh to provide color and surface detail <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This is often referred to as a UV map <a class="yt-timestamp" data-t="01:00:30">[01:00:30]</a>.
    *   Human-designed UV maps are typically organized in an understandable way for artists to color them <a class="yt-timestamp" data-t="01:07:51">[01:07:51]</a>.
*   **Limitations:** Meshes require explicitly defining triangles and dealing with concepts like "cleanliness" of polygons <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a>. If the mesh changes, the UV texture often needs to be remade <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>. The speaker expresses a strong belief that textures and meshes will be superseded <a class="yt-timestamp" data-t="00:50:59">[00:50:59]</a>.

## [[Comparison of 3D gaussian splatting to neural radiance fields | Neural Radiance Fields (Nerfs)]]

[[Comparison of 3D gaussian splatting to neural radiance fields | Neural Radiance Fields (Nerfs)]] gained popularity as an entirely different type of 3D representation <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **How it works:** A neural network (often a multi-layer perceptron) implicitly stores the 3D object within its weights <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Users can query the neural network for the color of every pixel from a specific camera position and viewpoint <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
*   **Advantages (Initial):** Were considered the potential future of 3D representation due to exciting results <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Disadvantages:**
    *   **Implicit Representation:** The 3D object is implicitly stored, meaning there's no direct understanding or control over individual parts of the object <a class="yt-timestamp" data-t="00:41:47">[00:41:47]</a>. You cannot easily delete parts or copy-paste objects <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>.
    *   **Slow Optimization (Per-Sample):** Training a Nerf is "per sample," meaning a new neural network must be trained for *every* new object, making it a "huge pain" and limiting practical usage due to long optimization times <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
    *   **Artifacts:** Can suffer from "ghost objects" or "mist" and diffuse effects <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

## [[3D Gaussian Splatting and Instant Splat Pipeline | 3D Gaussian Splatting]]

[[3D Gaussian Splatting and Instant Splat Pipeline | 3D Gaussian Splatting]] is a newer technique that represents a 3D scene with millions of small particles <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **How it works:** Each particle is a "gaussian" (a 3D gaussian function) <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
    *   Each 3D gaussian comes with a position, orientation (quaternion), scale, opacity, and a view-dependent color (though sometimes a simple diffuse color is used, as in the discussed papers, meaning no view-dependent lighting like spherical harmonics) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a> <a class="yt-timestamp" data-t="00:43:33">[00:43:33]</a> <a class="yt-timestamp" data-t="01:43:36">[01:43:36]</a>.
    *   When rendering, 3D gaussians are projected onto the camera's imaging plane, appearing as 2D gaussians <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>.
    *   The GPU assigns projected 2D gaussians to individual tiles of the image, sorts them, and then sums their contributions to determine the final pixel color <a class="yt-timestamp" data-t="00:38:46">[00:38:46]</a> <a class="yt-timestamp" data-t="01:40:51">[01:40:51]</a>. This process leverages old techniques like point-based volume rendering and GPU-friendly rasterization <a class="yt-timestamp" data-t="00:39:24">[00:39:24]</a> <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>.
*   **Advantages (Compared to Nerfs):**
    *   **Speed:** Significantly faster for 3D generative tasks and rendering <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. Can produce high-quality textured meshes in as little as two minutes on a single consumer GPU <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a> <a class="yt-timestamp" data-t="01:39:42">[01:39:42]</a>. This is approximately 10 times faster than existing methods <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    *   **Simplicity:** Simpler than previous approaches <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
    *   **Explicit Representation:** The 3D object is explicitly stored as a collection of particles, allowing for compositional tasks like deleting parts, adding, or copying/pasting <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a> <a class="yt-timestamp" data-t="00:42:24">[00:42:24]</a>. This contrasts with the implicit nature of Nerfs <a class="yt-timestamp" data-t="00:41:47">[00:41:47]</a>.
    *   **Quality:** Works "really, really well" and can achieve "more detailed scene reconstruction" <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a> <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>. Quality is comparable to or better than Nerfs <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
    *   **Memory Usage:** Reduced memory usage during training compared to Nerfs <a class="yt-timestamp" data-t="00:40:58">[00:40:58]</a>.

## [[Comparison of 3D Representation Techniques | Direct Comparisons and Future Implications]]

### Nerfs vs. [[Gaussian splatting and its advantages | Gaussian Splatting]]
The speaker strongly advocates that [[Gaussian splatting and its advantages | Gaussian Splatting]] will supersede [[Comparison of 3D gaussian splatting to neural radiance fields | Nerfs]] due to its speed and explicit representation <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a> <a class="yt-timestamp" data-t="00:42:13">[00:42:13]</a>. While Nerfs offer good quality, [[Gaussian splatting and its advantages | Gaussian Splatting]] achieves similar or better quality with significantly faster rendering and training times <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a> <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>.

### Meshes/Textures vs. [[Gaussian splatting and its advantages | Gaussian Splatting]]
The speaker believes that meshes and textures will also be replaced by [[Gaussian splatting and its advantages | Gaussian Splatting]] as the standard 3D representation <a class="yt-timestamp" data-t="00:50:59">[00:50:59]</a>. The explicit nature of [[Gaussian splatting and its advantages | Gaussian Splatting]] makes it more flexible for manipulation and composition than meshes <a class="yt-timestamp" data-t="00:42:42">[00:42:42]</a>. For example, removing parts of a scene is much easier with [[Gaussian splatting and its advantages | Gaussian Splatting]] than with meshes <a class="yt-timestamp" data-t="02:00:57">[02:00:57]</a>.

Some papers like DreamGaussian, however, do include a mesh extraction step from [[Gaussian splatting and its advantages | Gaussian Splatting]] <a class="yt-timestamp" data-t="01:04:44">[01:04:44]</a>, acknowledging that it's a new and unexplored problem to convert [[Gaussian splatting and its advantages | 3D Gaussian Splats]] into polygonal meshes <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. This conversion can involve using algorithms like marching cubes <a class="yt-timestamp" data-t="01:05:38">[01:05:38]</a>. However, this process can lead to "gross" or machine-generated UV maps that are not human-interpretable <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. Additionally, mesh-based methods can yield "overly smooth geometry" due to limitations in capturing intricate, high-frequency details <a class="yt-timestamp" data-t="01:30:08">[01:30:08]</a>.

### [[Implications of Gaussian splatting in future technologies | Future Outlook]]
The explicit nature of [[Gaussian splatting and its advantages | Gaussian Splats]] is seen as a major advantage that will enable future applications. The speaker hypothesizes that game engines and VR/AR applications will eventually operate directly with [[Gaussian splatting and its advantages | Splats]], eliminating the need for meshes and textures <a class="yt-timestamp" data-t="01:58:21">[01:58:21]</a>. Even 3D printing, currently based on meshes, might eventually transition to direct [[Gaussian splatting and its advantages | Splat]] representation <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.