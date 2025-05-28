---
title: Rectified flow in diffusion models
videoId: yTXMK2TZOZc
---

From: [[hu-po]] <br/> 

Rectified flow is a generative model formulation designed to connect data and noise distributions in a straight line during the [[diffusion_models_and_image_generation | image generation]] process <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. It is highlighted as a specific type of flow used in the latest version of [[diffusion_models_and_image_generation | Stable Diffusion]] due to its superior performance over other methods <a class="yt-timestamp" data-t="00:34:35">[00:34:35]</a>.

## Principle and Advantages

Traditional [[diffusion_models_and_image_generation | diffusion models]] often follow a "curved path" when transforming noise into an image in a high-dimensional space <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. This means the process involves multiple intermediate steps, where the generated image might temporarily deviate in semantic attributes before returning to the desired final state <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>, <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. Each step in this process requires an evaluation of the neural network, directly impacting sampling speed <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>, <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.

Rectified flow aims to eliminate this curvature by taking a "straight path" from pure noise to the target data distribution <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>, <a class="yt-timestamp" data-t="00:35:56">[00:35:56]</a>. This straight path means the process can ideally be simulated with a single step, making it less prone to error accumulation and significantly improving sampling speed <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>, <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. It is also noted for being the simplest possible formulation mathematically for this process <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.

## Experimental Validation and Optimal Sampling

In Stable Diffusion 3, various flow trajectories were compared, including EDM, Cosine, and LDM Linear <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>, <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>, <a class="yt-timestamp" data-t="00:35:12">[00:35:12]</a>. Experiments demonstrated that rectified flow consistently outperformed these alternatives <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>, <a class="yt-timestamp" data-t="00:49:09">[00:49:09]</a>, <a class="yt-timestamp" data-t="00:51:17">[00:51:17]</a>.

The performance of rectified flow is further optimized when combined with a specific time-step sampling strategy called **logit normal sampling** <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>, <a class="yt-timestamp" data-t="00:49:52">[00:49:52]</a>. Unlike common uniform sampling, which picks random time steps with equal probability between noise and data <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>, logit normal sampling biases the training towards intermediate steps <a class="yt-timestamp" data-t="00:41:57">[00:41:57]</a>. The intuition behind this is that these intermediate stages (often between 0.4 and 0.6) are where the model faces the most difficulty and opportunity for learning how to effectively remove or predict noise <a class="yt-timestamp" data-t="00:39:47">[00:39:47]</a>, <a class="yt-timestamp" data-t="00:42:22">[00:42:22]</a>, <a class="yt-timestamp" data-t="00:44:31">[00:44:31]</a>.

The combination of rectified flow with logit normal sampling proved to be the most efficient and robust approach among 24 tested combinations of sampler settings <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>, <a class="yt-timestamp" data-t="00:51:17">[00:51:17]</a>. This specific combination shows better results even when using fewer sampling steps during inference <a class="yt-timestamp" data-t="00:51:20">[00:51:20]</a>, <a class="yt-timestamp" data-t="00:51:54">[00:51:54]</a>.

> [!NOTE] Practical Implications
> The explicit comparison and validation of different flow trajectories and sampling methods by Stability AI saves other researchers and developers significant computational resources, as they can directly implement the most efficient and effective combination without extensive independent experimentation <a class="yt-timestamp" data-t="01:59:02">[01:59:02]</a>, <a class="yt-timestamp" data-t="01:59:22">[01:59:22]</a>. This contributes to the overall [[scaling_and_optimization_in_diffusion_models | scaling and optimization in diffusion models]] <a class="yt-timestamp" data-t="01:53:06">[01:53:06]</a>.