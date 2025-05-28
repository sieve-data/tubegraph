---
title: OpenAIs ShapeE and PointE
videoId: azCp-b7c-GM
---

From: [[hu-po]] <br/> 

ShapeE is an artificial intelligence model developed by OpenAI that focuses on generating 3D assets from text or images. Released in May 2023, it serves as a follow-up to OpenAI's previous work, PointE <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## PointE as Predecessor

PointE, released approximately four months prior to ShapeE, was also a text-to-3D shape generation model <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Both projects were primarily developed by Alex Nichol and Heewoo Jun within OpenAI <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a> <a class="yt-timestamp" data-t="01:56:12">[01:56:12]</a>. PointE generated explicit point cloud representations, whereas ShapeE focuses on implicit functions <a class="yt-timestamp" data-t="01:43:09">[01:43:09]</a>.

## ShapeE Overview

ShapeE is a conditional generative model for 3D assets, meaning it generates 3D objects based on conditioning inputs like text descriptions or images <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a> <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

Unlike other recent 3D generative models that produce a single output representation, ShapeE directly generates the parameters of implicit functions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. These implicit functions can then be rendered as both textured meshes (common in video games and CGI) and [[3d_representation_techniques_nerfs_vs_gausssian_splats | neural radiance fields (NeRFs)]] <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a> <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. This multi-representation output space is a key feature, allowing generated assets to be imported into various downstream 3D applications <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a>.

The model is trained in two main stages:
1.  An encoder that maps 3D assets into the parameters of the implicit function <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
2.  A conditional diffusion model <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

ShapeE can generate complex and diverse 3D assets in a matter of seconds, specifically around 13 seconds on a single Nvidia V100 GPU (likely 32GB memory version) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a> <a class="yt-timestamp" data-t="01:17:16">[01:17:16]</a>. Compared to PointE, ShapeE converges faster and achieves comparable or better sample quality despite modeling a higher-dimensional output space <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. OpenAI has released the model weights, inference code, and samples on GitHub <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### Challenges in 3D Representation

Unlike 2D images or audio, which have natural fixed-size tensor representations, 3D assets lack an obvious, universally adopted format <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This leads to a heterogeneity of approaches, including:
*   [[3d_representation_techniques_nerfs_vs_gausssian_splats | Neural Radiance Fields (NeRFs)]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>
*   [[3d_mesh_generation_with_ai | Textured meshes]] (common in video games like Unity, Unreal Engine, Roblox) <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a> <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>
*   [[signed_distance_functions_and_neural_radiance_fields | Signed Distance Functions (SDFs)]] <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>

A significant challenge is generating 3D assets in a way that is both efficient to create and easy to use in downstream applications, as many current game engines require textured meshes <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a> <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

## Technical Deep Dive: ShapeE's Approach

ShapeE combines several approaches to address the complexities of 3D representation and generation <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>.

### Implicit Neural Representations (INRs)

Implicit Neural Representations (INRs) are an umbrella term for techniques that encode 3D assets by mapping 3D coordinates to location-specific information (e.g., density, color) <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. They are resolution-independent, meaning they can be queried at arbitrary points <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

*   **NeRFs**: A function that represents a 3D scene based on viewing directions and densities of RGB colors. NeRFs can be rendered from arbitrary views by querying densities and colors along camera rays <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **DM-Tet / Get3D**: These models represent a textured 3D mesh as a function mapping coordinates to colors, signed distances, and vertex offsets <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a> <a class="yt-timestamp" data-t="01:02:58">[01:02:58]</a>. They allow for the differentiable construction of 3D triangle meshes <a class="yt-timestamp" data-t="01:09:40">[01:09:40]</a>.

### ShapeE's Implicit Function (STF)

ShapeE introduces a new implicit function called STF (Signed Texture Field) <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>. An STF produces both a signed distance (indicating whether a point is inside or outside an object) and texture colors <a class="yt-timestamp" data-t="00:28:44">[00:28:44]</a>. The surface of the shape is defined where the signed distance is zero <a class="yt-timestamp" data-t="00:30:36">[00:30:36]</a>. [[3d_mesh_generation_with_ai | Marching Cubes]] or marching tetrahedra can be used to construct meshes from this implicit representation <a class="yt-timestamp" data-t="00:31:14">[00:31:14]</a>.

### Architecture and Training

ShapeE's core architecture involves a Transformer-based encoder and a conditional diffusion model <a class="yt-timestamp" data-t="01:06:02">[01:06:02]</a>.
*   The encoder takes both point clouds (16,000 points, downsampled to 1,000) and rendered RGBA (Red, Green, Blue, Alpha) views (60 views per object) as input <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a> <a class="yt-timestamp" data-t="01:12:43">[01:12:43]</a>. The alpha channel is used for transmittance targets <a class="yt-timestamp" data-t="01:19:44">[01:19:44]</a>.
*   Crucially, the encoder's output is a latent representation that is linearly projected to obtain the *weights* of a Multi-Layer Perceptron (MLP) <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>. This MLP then acts as both the NeRF and the STF <a class="yt-timestamp" data-t="01:13:35">[01:13:35]</a>. When queried with a 3D point, this MLP outputs opacity, signed distance, and color <a class="yt-timestamp" data-t="01:23:37">[01:23:37]</a>. This unique design allows one neural network to output the parameters of another <a class="yt-timestamp" data-t="01:24:39">[01:24:39]</a>.
*   The diffusion model operates directly on these [[memory_and_computational_efficiency_in_pointbased_methods | latent vectors]] (sequences of 1024x1024 tokens) <a class="yt-timestamp" data-t="01:39:12">[01:39:12]</a>.
*   The model uses a two-stage training process:
    1.  **Pre-training**: The encoder is initially pre-trained using a NeRF rendering objective, minimizing L1 loss between predicted and true colors, and an L1 loss on transmittance <a class="yt-timestamp" data-t="01:15:43">[01:15:43]</a> <a class="yt-timestamp" data-t="01:18:14">[01:18:14]</a>.
    2.  **Fine-tuning**: Additional output heads for SDF and texture color predictions are added to the MLP. These are initially distilled from approximations and then fine-tuned end-to-end using both NeRF and STF rendering objectives <a class="yt-timestamp" data-t="01:15:47">[01:15:47]</a> <a class="yt-timestamp" data-t="01:36:12">[01:36:12]</a>. L2 loss is used for STF rendering <a class="yt-timestamp" data-t="01:37:27">[01:37:27]</a>.

### Dataset

ShapeE was trained on a large dataset of paired 3D and text data <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. It leverages the same underlying 3D assets as PointE, but with extended post-processing, including 60 views (instead of 20) and 16,000 points (instead of 4,000) for point clouds <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. For its text-conditional model, ShapeE uses an expanded dataset incorporating roughly 1 million more 3D assets from "high quality data sources" and over 120,000 human-provided captions <a class="yt-timestamp" data-t="01:12:06">[01:12:06]</a>. The specific source of this extended dataset is not disclosed, implying it may be an internal OpenAI proprietary dataset <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a> <a class="yt-timestamp" data-t="01:47:40">[01:47:40]</a>.

### Diffusion Models and Latent Space

ShapeE's generative component is a [[foundation_models_in_ai | latent diffusion model]], which operates on a continuous latent space rather than directly on pixel space <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a> <a class="yt-timestamp" data-t="01:50:24">[01:50:24]</a>. The model can be conditioned on text or image embeddings. For image conditioning, ShapeE uses a 256-token CLIP embedding sequence appended to the Transformer input <a class="yt-timestamp" data-t="01:39:46">[01:39:46]</a>. This contradicts an earlier statement in the paper claiming it "does not require a separate text to image model" <a class="yt-timestamp" data-t="01:40:31">[01:40:31]</a>.

## Performance and Limitations

ShapeE demonstrates strong performance, with a generation time of about 13 seconds per sample <a class="yt-timestamp" data-t="01:17:16">[01:17:16]</a>. In comparisons to PointE, it shows slightly better or comparable quantitative results (e.g., PSNR, CLIP R-Precision) <a class="yt-timestamp" data-t="01:42:20">[01:42:20]</a>. However, since both ShapeE and PointE were trained on the same (undisclosed) dataset, direct comparison with other 3D generative techniques is limited <a class="yt-timestamp" data-t="01:50:47">[01:50:47]</a>.

Limitations of ShapeE include:
*   **Compositional Understanding**: While it understands single-object prompts, it struggles to compose multiple attributes to different objects (e.g., "green seat, red legs") or reliably produce the correct number of objects when asked for more than two <a class="yt-timestamp" data-t="01:46:51">[01:46:51]</a>. This is likely due to limitations in the paired training data <a class="yt-timestamp" data-t="01:47:03">[01:47:03]</a>.
*   **Texture Details**: The encoder sometimes loses detailed textures <a class="yt-timestamp" data-t="01:50:09">[01:50:09]</a>.
*   **Lighting**: All rendered images in the dataset are from a constant 30-degree elevation and use fixed diffuse and ambient shading, limiting variability in lighting <a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a> <a class="yt-timestamp" data-t="02:04:25">[02:04:25]</a>.
*   **Computational Constraints**: The paper's authors (only two main contributors) likely operated under a limited computational budget, leading to choices like not conducting extensive hyperparameter sweeps or full ablation studies <a class="yt-timestamp" data-t="02:05:09">[02:05:09]</a>.