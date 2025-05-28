---
title: Technical Insights Balancing Complexity and Efficiency in 3D Modeling
videoId: BRgm5vteAjQ
---

From: [[hu-po]] <br/> 

The world of computer vision, particularly in 3D representation, is characterized by an "arms race" to find the most efficient and high-quality methods for rendering and reconstructing scenes <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. This pursuit involves balancing computational complexity with rendering and training efficiency, while striving for superior visual and geometric fidelity.

## Evolution of 3D Representations

Historically, [[comparative_analysis_of_3d_representation_techniques | 3D representations]] have evolved from traditional mesh and texture models to more recent neural and point-based systems:

*   **Mesh and Texture Representation**: For decades, the industry standard has involved defining a mesh (a set of vertices representing topology) and mapping a texture onto it <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. This method explicitly stores the object's topology <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>.
*   **Neural Radiance Fields (NeRFs)**: NeRFs implicitly store the appearance and geometry of a scene as the weights of a neural network (multi-layer perceptron) <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>. Rendering NeRFs involves computationally intensive ray-based point sampling and multiple inferences from the neural network for each pixel, making them inefficient for real-time applications <a class="yt-timestamp" data-t="12:07:00">[12:07:00]</a> <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a> <a class="yt-timestamp" data-t="12:25:00">[12:25:00]</a>. NeRFs are often considered "beautiful" due to their implicit representation <a class="yt-timestamp" data-t="16:06:00">[16:06:00]</a>.
*   **3D Gaussian Splatting (3DGS)**: 3DGS represents scenes using a set of explicit, topology-free Gaussian points <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>. These points are dynamically added and removed during optimization <a class="yt-timestamp" data-t="11:15:00">[11:15:15]</a>. 3DGS leverages GPU and CUDA-based [[rendering_technology_and_algorithms | rasterization]], which is highly optimized on GPUs, enabling real-time rendering much faster than NeRFs <a class="yt-timestamp" data-t="12:32:00">[12:32:00]</a> <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a> <a class="yt-timestamp" data-t="16:21:00">[16:21:00]</a>.
    *   **Limitations of 3DGS**:
        *   **Non-zero thickness**: Gaussian points, resembling ellipsoids, have non-zero thickness, hindering close alignment with actual surfaces and resulting in a "bubbly" texture <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a> <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>.
        *   **Ambiguity in normal direction**: The normal vector for each 3D Gaussian can be ambiguous, changing with scale and orientation during optimization <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a>.
        *   **Modeling sharp edges**: Alpha blending in 3DGS can introduce bias, making it difficult to model sharp surface edges cleanly <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>. The semi-transparent nature of Gaussian splats contributes to this <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.

## Gaussian Surfels: A New Challenger

Gaussian Surfels (published April 27, 2024) combine the flexible optimization of 3D Gaussian points with the surface alignment property of surfels <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a> <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a> <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>. This technique aims for high-quality surface reconstruction <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a> <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.

### Core Concept
A surfel is created by setting the z-scale of a 3D Gaussian point to zero, effectively flattening the original 3D ellipsoid into a 2D ellipse or disc <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a> <a class="yt-timestamp" data-t="21:42:00">[21:42:00]</a> <a class="yt-timestamp" data-t="28:26:00">[28:26:00]</a>. This design provides clear guidance to the optimizer by treating the local z-axis as the [[normal_maps_in_3d_modeling | normal direction]], improving optimization stability and surface alignment <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a> <a class="yt-timestamp" data-t="24:39:00">[24:39:00]</a>. Surfels themselves are not new; they originate from a paper published in 2000 <a class="yt-timestamp" data-t="23:09:00">[23:09:00]</a> <a class="yt-timestamp" data-t="23:12:00">[23:12:00]</a>.

### Properties of Gaussian Surfels
Each Gaussian surfel is an unstructured kernel with properties including:
*   Position (XYZ coordinates) <a class="yt-timestamp" data-t="26:44:00">[26:44:00]</a>
*   Orientation/Rotation (represented by a quaternion) <a class="yt-timestamp" data-t="26:56:00">[26:56:00]</a>
*   Opacity (how transparent the surfel is) <a class="yt-timestamp" data-t="27:13:00">[27:13:00]</a>
*   Spherical harmonic coefficients (for view-dependent color encoding) <a class="yt-timestamp" data-t="27:20:00">[27:20:00]</a>
*   Scaling factors (for the 2D ellipsoid) <a class="yt-timestamp" data-t="27:27:00">[27:27:00]</a>
The covariance matrix of the surfel defines its shape <a class="yt-timestamp" data-t="27:41:00">[27:41:00]</a>.

### Optimization Techniques
The optimization process for Gaussian surfels is complex, incorporating multiple loss functions to achieve high-quality surface reconstruction:

*   **Photometric Loss (Lp)**: Minimizes the difference between the rendered image and the input image, combining an L1 term (80%) and a DSSIM term (20%) <a class="yt-timestamp" data-t="35:19:00">[35:19:00]</a> <a class="yt-timestamp" data-t="36:19:00">[36:19:00]</a>. DSSIM is a metric for visual similarity <a class="yt-timestamp" data-t="37:37:00">[37:37:00]</a>.
*   **Normal Prior Loss (Ln)**: Utilizes normals derived from a pre-trained monocular normal estimator (e.g., OmniData) <a class="yt-timestamp" data-t="31:30:00">[31:30:00]</a> <a class="yt-timestamp" data-t="40:07:00">[40:07:00]</a>. This loss helps align the surfel's normal direction with the ground truth surface normal <a class="yt-timestamp" data-t="25:46:00">[25:46:00]</a>.
*   **Depth Normal Consistency Loss (Lc)**: Enforces consistency between the rendered depth and the rendered normal <a class="yt-timestamp" data-t="39:14:00">[39:14:00]</a>. It pushes gradients to correct both depth and normal if they are inconsistent, leading to improved reconstruction <a class="yt-timestamp" data-t="42:52:00">[42:52:00]</a> <a class="yt-timestamp" data-t="43:24:00">[43:24:00]</a>.
*   **Opacity Loss**: Promotes non-transparent surfaces by encouraging each Gaussian's opacity to be near zero or near one <a class="yt-timestamp" data-t="45:38:00">[45:38:00]</a>. This contrasts with 3DGS, where medium opacity points are common <a class="yt-timestamp" data-t="46:45:00">[46:46:00]</a>. This can potentially lead to more efficient representations with fewer points <a class="yt-timestamp" data-t="1:29:17">[1:29:17]</a>.
*   **Mask Loss (Lm)**: (Mentioned in the total loss equation, but not detailed further in transcript) <a class="yt-timestamp" data-t="35:31:00">[35:31:00]</a>.

This multi-loss system provides additional learning signals compared to vanilla 3DGS, which primarily relies on photometric loss <a class="yt-timestamp" data-t="24:51:00">[24:51:00]</a>.

### Surface Reconstruction
After optimization, the surfel point set is used to extract a surface mesh using [[optimization_techniques_in_surfels | Screened Poisson Reconstruction]] <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a> <a class="yt-timestamp" data-t="47:59:00">[47:59:00]</a>. This technique is designed to create watertight surfaces from oriented point sets <a class="yt-timestamp" data-t="48:15:00">[48:15:00]</a>, which Gaussian surfels provide due to their defined normals <a class="yt-timestamp" data-t="48:28:00">[48:28:00]</a>.

### Handling Erroneous Points
A "volumetric cutting" method is applied to remove erroneous outlier Gaussian points, similar to the pruning and densification strategies in other 3DGS pipelines <a class="yt-timestamp" data-t="49:41:00">[49:41:00]</a>. This involves constructing a voxel grid and pruning voxels with low accumulated opacity <a class="yt-timestamp" data-t="50:52:00">[50:52:00]</a>.

## Advantages and Limitations

### Advantages:
*   **High-quality surface reconstruction**: Gaussian surfels offer superior performance in surface reconstruction compared to state-of-the-art neural volume rendering and point-based rendering methods <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
*   **Faster training**: The method exhibits fast training times <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a> <a class="yt-timestamp" data-t="11:10:00">[11:10:10]</a>.
*   **Random Initialization**: Unlike many 3DGS methods that require structure-from-motion (SfM) pipelines for initialization, Gaussian surfels can be initialized with random positions and rotations due to the stronger learning signals from the normal and depth consistency losses <a class="yt-timestamp" data-t="54:15:00">[54:15:00]</a> <a class="yt-timestamp" data-t="56:26:00">[56:26:00]</a>. This bypasses the need for "crusty and shitty" SfM pipelines <a class="yt-timestamp" data-t="55:36:00">[55:36:00]</a>.
*   **Open Surfaces**: The method can reconstruct open surfaces, unlike signed distance function (SDF) representations used in some NeRFs that assume closed surfaces <a class="yt-timestamp" data-t="1:06:45">[1:06:45]</a>.
*   **Noise-free and intricate details**: The method excels at reconstructing noise-free surfaces and capturing intricate details, outperforming overly smooth NeRF-based reconstructions <a class="yt-timestamp" data-t="1:07:50">[1:07:50]</a> <a class="yt-timestamp" data-t="1:17:21">[1:17:21]</a>.

### [[challenges_and_limitations_in_3d_generation | Limitations and Assumptions of Dynamic 3D Modeling]]:
*   **Complexity of Optimization**: The method requires balancing multiple loss functions, each with customizable weights (hyperparameters), and different learning rates for various surfel properties (position, scale, opacity, color) <a class="yt-timestamp" data-t="35:50:00">[35:50:00]</a> <a class="yt-timestamp" data-t="57:27:00">[57:27:00]</a>. Gradient scaling (e.g., scaling normal-based gradients by 10) also adds to the manual tuning effort <a class="yt-timestamp" data-t="58:59:00">[58:59:00]</a>.
*   **Specular Reflections**: The method struggles with accurate surface reconstruction in areas with strong specular reflections (shiny objects) <a class="yt-timestamp" data-t="1:12:49">[1:12:49]</a>. This is a common challenge for 3D reconstruction algorithms <a class="yt-timestamp" data-t="1:15:01">[1:15:01]</a>.
*   **Dynamic Scenes**: While 3DGS can be extended to dynamic scenes by adding time dependence to point properties, it's unclear if Gaussian surfels, with their high opacity and perfect surface alignment requirements, would be as adaptable for [[limitations_and_assumptions_of_dynamic_3d_modeling | dynamic 3D scene representation]] <a class="yt-timestamp" data-t="1:03:07">[1:03:07]</a> <a class="yt-timestamp" data-t="1:03:51">[1:03:51]</a>.

## The Role of Hardware
The efficiency of 3D representations, especially point-based ones like 3DGS and Gaussian surfels, heavily relies on [[rendering_technology_and_algorithms | GPU-accelerated rasterization]] <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>. The ability to implement algorithms efficiently in CUDA and run them on GPUs is a key factor in their success, echoing moments like Alex Krizhevsky's AlexNet in 2012 that kicked off the deep learning revolution by leveraging GPUs for neural network training <a class="yt-timestamp" data-t="14:54:00">[14:54:00]</a> <a class="yt-timestamp" data-t="15:30:00">[15:30:00]</a>.

## Future Outlook
The path forward for 3D representations likely involves integrating more sophisticated light modeling and physics-based interactions. Current methods often pack view-dependent effects into spherical harmonic coefficients, which can be limiting <a class="yt-timestamp" data-t="1:18:04">[1:18:04]</a> <a class="yt-timestamp" data-t="1:19:10">[1:19:10]</a>. Future work might involve using neural networks to model complex lighting effects like specular reflections and subsurface scattering, potentially by feeding explicit lighting features into the network <a class="yt-timestamp" data-t="1:19:18">[1:19:18]</a> <a class="yt-timestamp" data-t="1:21:09">[1:21:09]</a>.

The evolution of 3D modeling techniques is a continuous process of balancing representational capacity, rendering speed, and algorithmic complexity, often influenced by the pragmatic considerations of hardware efficiency and ease of implementation.