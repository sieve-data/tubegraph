---
title: DreamFusion and its relation to diffusion models
videoId: Z6dB1zIfwr4
---

From: [[hu-po]] <br/> 

DreamFusion is a notable variant of [[diffusion_models_and_transformers | diffusion models]] specifically designed for [[future_potential_of_3d_diffusion_models | 3D generation]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It allows for the creation of 3D models from a text-based prompt <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This capability is considered potentially "extremely disruptive" to the art community, similar to how [[diffusion_models_and_image_generation | 2D image generation]] was, and "absolutely insane" for industries like video games where 3D modeling is typically very difficult <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

> [!NOTE] Early Work
> DreamFusion is still in its very early stages, with development stemming from Google Research by Ben Poole <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

## Core Technology

DreamFusion leverages [[diffusion_models_and_transformers | diffusion models]] as its foundation, which fundamentally operate by adding and then removing noise to generate content <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### Diffusion Models in DreamFusion

DreamFusion utilizes large pre-trained [[diffusion_models_and_image_generation | image generation]] models to guide the 3D synthesis process:

*   **Imagen:** Google's [[diffusion_models_and_image_generation | image generation]] model, which diffuses directly in the image space (e.g., adding noise to an image of a frog) <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. The original DreamFusion paper uses Imagen <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Stable Diffusion:** An open-source implementation of DreamFusion uses Stable Diffusion because Imagen is not publicly available <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Stable Diffusion is a [[latent_diffusion_models_and_architectures | latent diffusion model]], meaning it diffuses in a latent space (a vector representation of the image) rather than directly in the original image space <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This requires propagating back from an autoencoder, which adds extra time cost <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

### Neural Radiance Fields (NeRF)

A core component of DreamFusion is the Neural Radiance Field (NeRF) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. NeRFs are used to represent the 3D scene:

*   **Parameterization:** The 3D scene is represented by a neural radiance field that parameterizes volumetric density and Albedo color using a Multi-Layer Perceptron (MLP) <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>.
*   **Training:** The NeRF MLP is randomly initialized and trained from scratch for each given text caption <a class="yt-timestamp" data-t="00:32:37">[00:32:37]</a>.
*   **Rendering:** The NeRF is rendered from random camera angles and positions. Normals computed from the density gradients are used to shade the scene with varied lighting directions <a class="yt-timestamp" data-t="00:34:56">[00:34:56]</a>. Shading helps reveal geometric details that might be ambiguous from a single viewpoint <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>.

### Score Distillation Sampling (SDS)

DreamFusion uses a technique called Score Distillation Sampling (SDS) as its loss function <a class="yt-timestamp" data-t="01:00:01">[01:00:01]</a>. This allows the model to optimize 3D parameters (NeRF) using a frozen pre-trained [[conditional_diffusion_models_for_neural_networks | conditional image generation model]] (Imagen/Stable Diffusion) without needing to backpropagate through the diffusion model itself <a class="yt-timestamp" data-t="00:35:14">[00:35:14]</a>, <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>.

The process involves:
1.  Rendering views of the NeRF from random camera angles <a class="yt-timestamp" data-t="01:00:11">[01:00:11]</a>.
2.  Diffusing the rendered image by adding noise sampled from a normal distribution <a class="yt-timestamp" data-t="00:35:16">[00:35:16]</a>.
3.  Feeding the combined (noisy) image and the text embedding into the frozen diffusion model <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>.
4.  The diffusion model attempts to predict and unapply the injected noise <a class="yt-timestamp" data-t="00:36:06">[00:36:06]</a>.
5.  A low-variance update direction (gradients) is then backpropagated through the rendering process to update the NeRF MLP parameters <a class="yt-timestamp" data-t="00:36:24">[00:36:24]</a>.

## Challenges and Limitations

*   **Computational Resources:** Training is computationally intensive. 1,000 training steps can take about three hours on an NVIDIA V100 GPU, an enterprise-grade graphics card costing around $8,000 <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>, <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. These GPUs typically have 16GB or 32GB of VRAM <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Lower-end GPUs often run into "CUDA out of memory" errors due to insufficient memory <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>, <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.
*   **The "Janus Problem":** This common issue results in 3D objects having multiple faces or inconsistent semantic understanding (e.g., a monkey model with multiple heads or eyes in the wrong place when rotated) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Ben Poole named this after Janus, the Roman God of Duality, who has two faces <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. View-dependent prompting (e.g., specifying "overhead view of that" in the prompt) can help alleviate this but doesn't solve it entirely <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>, <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Degenerate Solutions:** The model might produce "flat geometry" where the scene content is drawn onto a 2D surface to satisfy text conditioning, rather than a true 3D shape <a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a>. This is mitigated by randomly replacing the Albedo color with white during shading to produce a textureless output <a class="yt-timestamp" data-t="01:11:59">[01:11:59]</a>.

## Future Potential

The speaker expresses strong belief in the [[future_potential_of_3d_diffusion_models | future potential of 3D diffusion models]], stating they will be "absolutely massive" <a class="yt-timestamp" data-t="01:20:21">[01:20:21]</a>. The ability to generate 3D models from text is seen as a crucial step towards the metaverse, where users could simply speak to their VR headsets to generate desired objects <a class="yt-timestamp" data-t="01:20:27">[01:20:27]</a>.

Further improvements could include:
*   Making the NeRF MLP significantly larger, possibly using a [[scalability_of_transformerbased_diffusion_models | Transformer-based architecture]] <a class="yt-timestamp" data-t="01:07:53">[01:07:53]</a>.
*   Pre-training the NeRF MLP on millions of objects, rather than initializing it randomly for each generation <a class="yt-timestamp" data-t="01:07:56">[01:07:56]</a>.
*   Advancements in GPU technology and NeRF algorithms themselves will be necessary for these advancements <a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a>.