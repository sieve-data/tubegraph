---
title: Video diffusion models in generative 3D
videoId: IsRHGf2rGCs
---

From: [[hu-po]] <br/> 

[[video_diffusion_models_in_generative_3d | Generative 3D]] involves creating 3D assets from text and images <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. This field is currently experiencing rapid progress, moving towards applications like real-time 3D generation for virtual reality (VR) and augmented reality (AR) <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a> <a class="yt-timestamp" data-t="03:00:02">[03:00:02]</a>.

A [[diffusion_models_and_image_generation | diffusion model]] typically generates samples from a distribution, traditionally an image distribution <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a> <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. [[video_diffusion_models_in_generative_3d | Video diffusion models]], in contrast, generate entire videos from noise <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Sora, from OpenAI, is considered the current state-of-the-art in [[video_diffusion_models_in_generative_3d | video diffusion models]] <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

## Role in Addressing 3D Data Scarcity

A primary challenge in developing foundational [[video_diffusion_models_in_generative_3d | 3D generative models]] is the limited availability of high-quality 3D data <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a> <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Popular datasets like Objaverse have biases, such as being object-centric <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a> <a class="yt-timestamp" data-t="02:18:06">[02:18:06]</a>.

To overcome this, researchers are exploring the use of generative models themselves as data sources <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. Initially, [[text_to_image_diffusion_models | text to image diffusion models]] like Stable Diffusion were used to generate images that trained [[video_diffusion_models_in_generative_3d | generative 3D models]] <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. The next evolutionary step involves leveraging [[video_diffusion_models_in_generative_3d | video diffusion models]] as knowledgeable sources for 3D data <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a> <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

This approach capitalizes on the "data flywheel" concept, where [[video_diffusion_models_in_generative_3d | video diffusion models]] are fine-tuned to produce large-scale, synthetic multi-view datasets. These datasets consist of videos that simulate 360-degree orbital shots around objects <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a> <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a> <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. The temporal consistency inherent in [[video_diffusion_models_in_generative_3d | video diffusion models]] helps ensure 3D consistency across different views, mitigating issues like the "Yanis effect" (where certain views, like the back of an object, are difficult to generate consistently) <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a> <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a> <a class="yt-timestamp" data-t="02:22:06">[02:22:06]</a>.

## Applications and Techniques

### V-Fusion 3D and SVD3
These papers present similar paradigms:
1.  **Fine-tuning a [[video_diffusion_models_in_generative_3d | video diffusion model]]:** Models like Meta's Emu or Stability AI's Stable Video Diffusion (SVD) are fine-tuned on existing 3D datasets (e.g., Objaverse) to generate multi-view videos <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a> <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a> <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.
2.  **Training a [[3d_implicit_functions_and_generative_models | 3D generative model]]:** The generated multi-view videos are then used to train a feed-forward [[3d_implicit_functions_and_generative_models | 3D generative model]], typically a Neural Radiance Field (NeRF), often based on a tri-plane representation <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a> <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a> <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. These NeRFs can reconstruct a 3D asset from a single image <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
3.  **Mesh Extraction:** The NeRF representation can then be converted into a mesh and texture using techniques like marching cubes <a class="yt-timestamp" data-t="00:31:47">[00:31:47]</a>.

### Gaussian Flow and 4D Content Creation
Some approaches, like Gaussian Flow, leverage [[video_diffusion_models_in_generative_3d | video diffusion models]] to create 4D (3D + time) content using Gaussian Splatting <a class="yt-timestamp" data-t="03:31:59">[03:31:59]</a>. They calculate optical flow (pixel velocities between consecutive frames) within the generated videos <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a> <a class="yt-timestamp" data-t="03:32:14">[03:32:14]</a>. This "Gaussian Flow" is then used to supervise the motion of 3D Gaussians, allowing for dynamic 3D scenes <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a> <a class="yt-timestamp" data-t="03:32:20">[03:32:20]</a>.

### Controlled Multi-view Editing
Techniques like MV-Edit use multi-view diffusion and a training-free 3D adapter to extend pre-trained [[diffusion_models_and_image_generation | image diffusion models]] for 3D-aware diffusion. They employ ancestral sampling to jointly denoise multi-view images and produce high-quality textured meshes <a class="yt-timestamp" data-t="01:02:50">[01:02:50]</a> <a class="yt-timestamp" data-t="01:03:31">[01:03:31]</a>. This allows for diverse tasks like image-to-3D, 3D-to-3D, and high-quality texture synthesis <a class="yt-timestamp" data-t="01:17:22">[01:17:22]</a>.

### Compositional 3D Generation
For complex scenes with multiple objects, methods like ComboVerse break down an input image into individual objects, reconstruct each in 3D, and then use spatially aware [[techniques_for_text_to_3d_conversion_involving_diffusion_models | score distillation sampling]] from pre-trained [[text_to_image_diffusion_models | diffusion models]] to guide the optimal positioning (size, rotation, location) of these objects relative to each other <a class="yt-timestamp" data-t="02:13:01">[02:13:01]</a> <a class="yt-timestamp" data-t="02:13:53">[02:13:53]</a>. This addresses the "multi-object gap" in current [[video_diffusion_models_in_generative_3d | generative 3D models]] which often have a single-object bias inherited from datasets like Objaverse <a class="yt-timestamp" data-t="02:18:06">[02:18:06]</a> <a class="yt-timestamp" data-t="02:21:35">[02:21:35]</a>.

## Comparison of 3D Representations

The field primarily utilizes two main 3D representations:
*   **Neural Radiance Fields (NeRFs):** Represent scenes implicitly as a continuous function that can be queried at any point in space, offering "infinite resolution" <a class="yt-timestamp" data-t="01:37:39">[01:37:39]</a> <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. Many models use tri-plane NeRFs, where 3D information is encoded into three orthogonal feature planes <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   **Gaussian Splatting:** Represents scenes explicitly as a set of individual 3D Gaussians, each with properties like position, rotation, color, and opacity <a class="yt-timestamp" data-t="02:55:53">[02:55:53]</a> <a class="yt-timestamp" data-t="03:06:56">[03:06:56]</a>. Gaussian Splatting models, like GRM, are emerging as promising alternatives due to their efficiency and ability to handle dynamic content <a class="yt-timestamp" data-t="03:12:08">[03:12:08]</a>.

While NeRFs offer fine detail, Gaussian Splatting provides advantages in efficiency and scalability, potentially leading to higher quality results as seen in some comparisons <a class="yt-timestamp" data-t="03:09:50">[03:09:50]</a> <a class="yt-timestamp" data-t="03:17:28">[03:17:28]</a>.

## Future Potential

The [[future_potential_of_3d_diffusion_models | future potential of 3D diffusion models]] is significant. Key areas of development include:

*   **Large-scale video datasets:** As [[video_diffusion_models_in_generative_3d | video diffusion models]] like Sora become more prevalent, they will generate massive 3D datasets, enabling the training of diffusion models that can directly produce 3D representations (e.g., Gaussian Splats) from noise <a class="yt-timestamp" data-t="00:57:33">[00:57:33]</a> <a class="yt-timestamp" data-t="03:15:01">[03:15:01]</a>.
*   **Human Preference Alignment:** Incorporating human feedback, similar to Reinforcement Learning from Human Feedback (RLHF) in large language models, will be crucial. This involves training reward models based on human judgments of 3D generation quality, alignment, and consistency, to fine-tune generative models <a class="yt-timestamp" data-t="02:33:42">[02:33:42]</a> <a class="yt-timestamp" data-t="02:37:07">[02:37:07]</a> <a class="yt-timestamp" data-t="03:25:56">[03:25:56]</a>.
*   **Real-time and On-device Generation:** The ultimate goal is to achieve real-time 3D generation that can run efficiently on devices like VR headsets, requiring highly optimized, feed-forward models <a class="yt-timestamp" data-t="03:28:22">[03:28:22]</a>.
*   **Intuitive User Interfaces:** Future interfaces for 3D modeling will likely incorporate voice commands, gestures, and augmented reality, making 3D creation more interactive and accessible <a class="yt-timestamp" data-t="03:25:24">[03:25:24]</a>.

This progression suggests a future where users can effortlessly generate and manipulate complex 3D environments, potentially even through thought in brain-computer interfaces <a class="yt-timestamp" data-t="03:39:50">[03:39:50]</a>.