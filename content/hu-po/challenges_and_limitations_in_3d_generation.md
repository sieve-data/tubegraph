---
title: Challenges and limitations in 3D generation
videoId: Z6dB1zIfwr4
---

From: [[hu-po]] <br/> 

3D generative AI, exemplified by models like DreamFusion, presents a significant leap beyond 2D image generation, promising to revolutionize fields such as video games and other industries reliant on 3D modeling <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. However, this nascent technology faces considerable challenges and limitations in its current state <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

## Current State of 3D Generative Models

While [[advancements_in_3d_generative_models_using_neural_networks | 3D generative models using neural networks]] like DreamFusion can generate 3D models from text prompts, these models are still in their early stages <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The examples shared, while impressive, are often "cherry-picked paper examples" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Creating 3D models traditionally is "very difficult," involving many professionals who make a living from it <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. The ability to generate complex 3D objects with just text promises to be "absolutely insane" for various industries <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Technical and Computational Hurdles

### High Computational Demands
Training 3D generative models like DreamFusion is computationally intensive. For instance, 1000 training steps can take approximately three hours on an NVIDIA V100 GPU <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. These V100 GPUs are high-end "Big Boy graphics cards," costing around $8,000 <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Attempting to run such models on less powerful hardware, like a 1080 GPU, frequently results in "Cuda out of memory" errors <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>, <a class="yt-timestamp" data-t="00:41:12">[00:41:12]</a>. Even with reduced image dimensions (e.g., 256x256 instead of 512x512) or lower `render_width` and `render_height`, memory limitations persist <a class="yt-timestamp" data-t="00:45:40">[00:45:40]</a>, <a class="yt-timestamp" data-t="00:50:59">[00:50:59]</a>.

The process of loading new models or batches of data during different phases of training can exceed available GPU memory <a class="yt-timestamp" data-t="01:05:53">[01:05:53]</a>. There's also a potential for memory leaks in the training loop, where memory accumulates without being recycled, leading to eventual out-of-memory errors <a class="yt-timestamp" data-t="01:04:51">[01:04:51]</a>.

### Software Dependencies and Compatibility
Installing and configuring the necessary software, such as PyTorch, can be complex due to version mismatches with CUDA <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>. Specific versions of PyTorch compatible with the system's CUDA version (e.g., CUDA 11.6) are required <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>. These dependencies can be very large, with a single PyTorch package reaching 1.9 gigabytes <a class="yt-timestamp" data-t="00:31:21">[00:31:21]</a>.

## Quality and Consistency Issues ([[limitations_and_assumptions_of_dynamic_3d_modeling | Limitations and Assumptions of Dynamic 3D Modeling]])

### The Janus Problem
A significant issue observed in generated 3D models is the "Janus problem," named after the Roman God of Duality <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. This problem manifests as models having multiple faces or lacking semantic consistency, for example, a head having two eyes on different sides, or an inconsistent back <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This occurs because the model struggles to understand a coherent 3D structure, often combining multiple 2D images into a 3D shape without full semantic understanding <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. While "view-dependent prompting" can help alleviate this, it doesn't solve the problem in all cases <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Geometric Degeneration
Models can sometimes produce a "degenerate solution" where scene content is drawn onto flat geometry to satisfy text conditioning, rather than creating genuine 3D structures <a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a>. This issue can be mitigated by randomly replacing the Albedo color with white, forcing a "textureless shaded output" <a class="yt-timestamp" data-t="01:11:59">[01:11:59]</a>.

## Optimization and Future Directions ([[optimization_techniques_and_challenges_for_3d_scene_representation | Optimization Techniques and Challenges for 3D Scene Representation]])

Current [[3d_scene_representation_and_simulation | 3D Scene Representation and Simulation]] models, specifically Neural Radiance Fields (NeRFs), are typically initialized randomly and trained from scratch for each text caption <a class="yt-timestamp" data-t="00:32:39">[00:32:39]</a>, rather than leveraging pre-trained knowledge. This suggests an opportunity for significant improvement:

*   **Larger, Pre-trained NeRF MLPs:** Making the NeRF Multi-Layer Perceptron (MLP) significantly larger and pre-training it on millions of objects could greatly enhance model power and efficiency <a class="yt-timestamp" data-t="01:07:48">[01:07:48]</a>. This would require more powerful GPUs and potential improvements in the NeRF algorithm itself <a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a>.
*   **Super-Resolution Integration:** DreamFusion currently only uses a 64x64 base model, without incorporating "super-resolution cascade" models that typically increase resolution in 2D image generation <a class="yt-timestamp" data-t="00:58:53">[00:58:53]</a>. Integrating these could improve the visual quality of generated 3D assets.
*   **Direct Parameterization of Color:** NeRFs traditionally predict color at each point along a ray <a class="yt-timestamp" data-t="01:10:06">[01:10:06]</a>. The model here directly parameterizes the color of the surface and then uses a separate shading process to determine interaction with light <a class="yt-timestamp" data-t="01:10:11">[01:10:11]</a>. This contrasts with traditional rendering where light bounces off triangle meshes are calculated based on material properties like specularity and metallicness <a class="yt-timestamp" data-t="01:09:04">[01:09:04]</a>.

Despite the current challenges, the potential for [[future_potential_and_direction_for_generative_3d_technology | 3D diffusion models]] is "absolutely massive" <a class="yt-timestamp" data-t="01:20:21">[01:20:21]</a>, envisioned to enable interaction with VR headsets to generate desired virtual environments <a class="yt-timestamp" data-t="01:20:32">[01:20:32]</a>.