---
title: Goshan Splat optimization for 3D reconstruction
videoId: IsRHGf2rGCs
---

From: [[hu-po]] <br/> 

[[3D Gaussian Splatting and Instant Splat Pipeline | Gaussian Splatting]], particularly its optimization for 3D reconstruction, is a burgeoning field in generative 3D modeling. This technique involves representing a 3D scene or object as a collection of 3D Gaussian "splats," each with its own position, rotation, color, and opacity <a class="yt-timestamp" data-t="03:06:59">[03:06:59]</a>. Unlike implicit representations like Neural Radiance Fields (NeRFs), Gaussian Splats offer a more explicit and potentially higher-capacity representation for complex scenes <a class="yt-timestamp" data-t="03:10:05">[03:10:05]</a>.

## Core Concepts

### 4D Gaussian Splatting
Traditional [[3D Gaussian Splatting and Instant Splat Pipeline | 3D Gaussian Splatting]] creates static 3D scenes. [[Goshen Splats in Robotics | 4D Gaussian Splatting]] extends this by adding a time dimension, allowing for the representation of dynamic content, such as a moving object or a sequence of 3D scenes <a class="yt-timestamp" data-t="00:36:18">[00:36:18]</a>. This means the properties of each Gaussian (like position and rotation) can change over time, enabling animation <a class="yt-timestamp" data-t="03:32:11">[03:32:11]</a>.

### Gaussian Flow
A novel concept introduced to optimize [[Goshen Splats in Robotics | 4D Gaussian Splatting]] is "Gaussian flow" <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a>. This connects the dynamics of 3D Gaussians with 2D pixel velocities between consecutive video frames <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>. It's efficiently obtained by splatting Gaussian dynamics into the image space, making the process differentiable <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. This enables dynamic supervision from optical flow, which is a pixel-level representation of movement in a video <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a> <a class="yt-timestamp" data-t="00:39:15">[00:39:15]</a>.

The optimization process for Gaussian flow typically involves:
1.  **Initialization**: Since 3D Gaussians need initial XYZ positions, a pre-trained model like "0123" (using Score Distillation Sampling, SDS) can be used to set the initial starting positions of these Gaussian points <a class="yt-timestamp" data-t="00:37:50">[00:37:50]</a>.
2.  **Frame-by-frame optimization**: Gradients are pushed directly into the Gaussians using SDS based on photometric consistency <a class="yt-timestamp" data-t="00:38:44">[00:38:44]</a>.
3.  **Optical Flow Integration**: Optical flow, while sometimes a "weakest link" due to its pixel-level nature and difficulty with uniform colors <a class="yt-timestamp" data-t="02:23:17">[02:23:17]</a>, provides a crucial signal. The Gaussian flow is distilled by combining the optical flow with the movement of Gaussians through a weighted sum, ensuring consistency between the rendered Gaussian splat and the video's optical flow <a class="yt-timestamp" data-t="00:43:11">[00:43:11]</a> <a class="yt-timestamp" data-t="00:45:59">[00:45:59]</a>. This allows direct dynamic supervision of 3D Gaussian dynamics <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>.

## Advantages and Comparisons

### Representational Capacity
One of the key [[Advantages and Disadvantages of Gosh and Splats | advantages of Gaussian Splats]] over [[Comparison of 3D gaussian splatting to neural radiance fields | NeRFs]] is their higher representational capacity <a class="yt-timestamp" data-t="03:10:05">[03:10:05]</a>. While a NeRF implicitly stores scene information within a tiny Multi-Layer Perceptron (MLP), Gaussian Splats explicitly define individual Gaussian primitives with distinct attributes (position, rotation, color, opacity). This explicit nature allows for potentially finer details and better quality reconstructions <a class="yt-timestamp" data-t="03:10:05">[03:10:05]</a>.

### Efficiency and Real-time Rendering
[[3D gaussian splatting for realtime radiance field rendering | Gaussian Splatting]] is noted for its efficiency, particularly for real-time rendering and handling dynamic content <a class="yt-timestamp" data-t="03:17:14">[03:17:14]</a>. Models like the "Large Gaussian Reconstruction Model" (GRM) are designed as feedforward Transformer-based models, translating input pixels into pixel-aligned Gaussians for rapid reconstruction from sparse view images (around 0.1 seconds, though hardware dependent) <a class="yt-timestamp" data-t="02:52:02">[02:52:02]</a> <a class="yt-timestamp" data-t="03:12:32">[03:12:32]</a>.

### Overcoming Limitations
Gaussian Splatting also helps address issues like "color drifting" in 4D content <a class="yt-timestamp" data-t="00:37:25">[00:37:25]</a>. The use of multi-view information, often derived from video diffusion models, helps overcome the "Yanis problem" (inconsistent generation of different views, especially the back of an object), leading to more consistent 3D reconstructions <a class="yt-timestamp" data-t="02:54:25">[02:54:25]</a>.

## Implications for Future Technologies
The future of [[Implications of Gaussian splatting in future technologies | generative 3D models]] is likely to heavily involve [[3D Gaussian Splatting and Instant Splat Pipeline | Gaussian Splatting]]. The ability to generate billions of splats from vast video datasets (like YouTube) could lead to diffusion models that generate [[Open Source Implementation of Gosh and Splats | Gaussian Splatting]] directly from noise <a class="yt-timestamp" data-t="00:57:33">[00:57:33]</a> <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>. This could enable advanced applications like text-conditioned or speech-conditioned 4D Gaussian Splat diffusion models, potentially powering future VR headset experiences by 2030 <a class="yt-timestamp" data-t="00:57:57">[00:57:57]</a>.

It is predicted that advancements in video diffusion models, such as Sora, will feed into these [[3D Gaussian Splatting and Instant Splat Pipeline | Gaussian Splatting]] techniques, leading to even higher quality and more consistent 3D generation <a class="yt-timestamp" data-t="03:15:01">[03:15:01]</a>.