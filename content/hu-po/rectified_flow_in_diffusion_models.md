---
title: Rectified Flow in Diffusion Models
videoId: yTXMK2TZOZc
---

From: [[hu-po]] <br/> 

Rectified flow is a generative model formulation that connects data and noise in a straight line, offering a significant advantage over methods that traverse a "curved path" through the high-dimensional image space <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

## Core Concept: Straight Paths vs. Curved Paths

In the context of diffusion models, the process of transforming pure noise into a coherent image involves a series of inference steps <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. Traditionally, the path taken through this high-dimensional space is "curved" <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. This means that, for example, a cat image might briefly pass through an "orange cat" representation before finally settling on the desired "gray cat" <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. Each of these intermediate steps requires an inference call to the neural network, adding computational overhead <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

Rectified flow aims to simplify this trajectory by defining the forward process as a straight path from the noise distribution to the data distribution <a class="yt-timestamp" data-t="00:35:56">[00:35:56]</a>. The objective is to achieve the final image in a single, direct step, thereby eliminating the need for numerous intermediate computations <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. This approach is rooted in a simple mathematical formulation, `Z(t) = (1-t) * x0 + t * epsilon` <a class="yt-timestamp" data-t="00:36:24">[00:36:24]</a>, representing a straight line between the initial image (`x0`) and the final noise (`epsilon`) across time `t` <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>, <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>.

## Advantages and Benefits

The primary benefits of rectified flow include:
*   **Computational Efficiency**: By enabling the model to predict the final output in potentially a single step, it significantly reduces the number of required integration steps during sampling <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.
*   **Reduced Error Accumulation**: Straight paths are less prone to error accumulation, as each step corresponds to an evaluation of the neural network <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

## Comparison to Other Flow Trajectories

Stable Diffusion 3's developers extensively compared rectified flow against other prominent flow formulations:
*   **EDM (Elucidated Diffusion Models)** <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>
*   **Cosine (from the 2021 Nichel and Dariwal paper)** <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>
*   **LDM Linear (from the 2022 LDM Romach paper)** <a class="yt-timestamp" data-t="00:35:13">[00:35:13]</a>

Across 24 combinations of flow types and sampling settings, rectified flow consistently outperformed other formulations, particularly when combined with optimized time step sampling strategies <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>, <a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>. This extensive [[comparisons_with_diffusion_models | comparative study]] positions rectified flow as the most efficient and effective choice <a class="yt-timestamp" data-t="00:51:18">[00:51:18]</a>.

> "Rectified flow is actually the best variant of a flow trajectory to use as a loss for these diffusion models" <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.

## Time Step Sampling with Rectified Flow

The choice of how to sample time steps (`t`) during training also significantly impacts performance. While many [[scaling_and_training_techniques_for_diffusion_models | diffusion models]] traditionally use a uniform distribution for `t` <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>, Stable Diffusion 3 introduces **Logit Normal sampling** <a class="yt-timestamp" data-t="00:40:41">[00:40:41]</a>. This method biases the sampling towards intermediate time steps (e.g., between t=0.4 and t=0.6) <a class="yt-timestamp" data-t="00:41:57">[00:41:57]</a>. The intuition behind this is that these "middle" steps, where the image is neither pure noise nor a fully formed image, are the most crucial for the model to learn effective noise removal or prediction <a class="yt-timestamp" data-t="00:42:22">[00:42:22]</a>.

Experiments showed that rectified flow combined with Logit Normal sampling consistently yielded the best performance <a class="yt-timestamp" data-t="00:44:31">[00:44:31]</a>, outperforming even rectified flow with uniform time step sampling <a class="yt-timestamp" data-t="00:49:01">[00:49:01]</a>. This confirms the hypothesis that intermediate time steps are more important for model training <a class="yt-timestamp" data-t="00:49:05">[00:49:05]</a>.

## Integration in Stable Diffusion 3

Rectified flow is a foundational component of Stable Diffusion 3's architecture. It is coupled with a novel [[transformer_architecture_in_diffusion_models | Transformer-based architecture]], the Multimodal Diffusion Transformer (MMD) <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. The combination of these innovations enables Stable Diffusion 3 to achieve state-of-the-art results in text-to-image generation <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>.