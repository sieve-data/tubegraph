---
title: Use of neural networks in consistency models
videoId: 8b6NhnNYtpg
---

From: [[hu-po]] <br/> 

[[consistency_models_introduction_and_significance | Consistency models]] are a family of generative models developed by OpenAI, designed to address the slow sampling speed inherent in [[comparison_of_diffusion_models_and_consistency_models | diffusion models]] <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>, <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. These models achieve fast one-step image generation while still allowing for a trade-off between computational cost and output quality through multi-step sampling <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>, <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, <a class="yt-timestamp" data-t="01:09:08">[01:09:08]</a>.

## Core Concept

[[consistency_models_introduction_and_significance | Consistency models]] learn a mapping from any point on a probability flow ordinary differential equation (ODE) trajectory back to its original data state (e.g., a clean image) <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>, <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. This contrasts with traditional [[comparison_of_diffusion_models_and_consistency_models | diffusion models]] which iteratively refine noise into an image <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. The "consistency" in their name refers to their outputs being consistent for any points belonging to the same trajectory, mapping back to the same initial data point <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>, <a class="yt-timestamp" data-t="00:58:44">[00:58:44]</a>.

## [[consistency_models_introduction_and_significance | Neural Networks]] as Function Approximators

At their heart, [[consistency_models_introduction_and_significance | consistency models]] leverage [[consistency_models_introduction_and_significance | neural networks]] as powerful function approximators <a class="yt-timestamp" data-t="00:38:56">[00:38:56]</a>. The primary neural network in a consistency model is denoted as $F_\theta$, where $\theta$ represents its parameters <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This network takes an image $x_t$ (which may contain noise) and a corresponding time step $t$, and outputs the final, denoised image $x_0$ (or $x_\sigma$, representing a state very close to the original image) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, <a class="yt-timestamp" data-t="00:56:33">[00:56:33]</a>.

### Parameterization

The consistency model $F_\theta$ can be implemented in a piecewise manner or, more commonly, using [[attention_mechanisms_in_neural_networks | skip connections]], which are a cornerstone of modern [[consistency_models_introduction_and_significance | neural network]] architectures like ResNets <a class="yt-timestamp" data-t="01:01:11">[01:01:11]</a>, <a class="yt-timestamp" data-t="01:01:13">[01:01:13]</a>.

> [!info] Skip Connections
> [[attention_mechanisms_in_neural_networks | Skip connections]] allow information to bypass certain layers in a [[consistency_models_introduction_and_significance | neural network]], which can help mitigate issues like vanishing gradients and improve information flow <a class="yt-timestamp" data-t="01:01:58">[01:01:58]</a>, <a class="yt-timestamp" data-t="01:02:04">[01:02:04]</a>.

The use of [[attention_mechanisms_in_neural_networks | skip connections]] in the parameterization of $F_\theta$ ensures differentiability, which is crucial for training the model using gradient-based optimization methods <a class="yt-timestamp" data-t="01:03:45">[01:03:45]</a>, <a class="yt-timestamp" data-t="01:03:47">[01:03:47]</a>.

## Training Consistency Models

[[consistency_models_introduction_and_significance | Consistency models]] can be trained in two primary ways:

1.  **Consistency Distillation**: In this mode, a pre-trained [[comparison_of_diffusion_models_and_consistency_models | diffusion model]] acts as an "oracle" <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>, <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. The diffusion model generates intermediate steps of the denoising process, providing pairs of adjacent points on an ODE trajectory. The consistency model $F_\theta$ is then trained to map these noisy inputs to the corresponding clean image, minimizing the difference between its outputs for points on the same trajectory <a class="yt-timestamp" data-t="02:00:27">[02:00:27]</a>, <a class="yt-timestamp" data-t="01:19:12">[01:19:12]</a>.

    *   **Loss Function**: The objective function (loss) for consistency distillation measures the distance between the outputs of the main network $F_\theta$ and a target network $F_{\theta^-}$ (an exponential moving average of $F_\theta$'s past weights) <a class="yt-timestamp" data-t="01:19:30">[01:19:30]</a>.
    *   **Metrics**: Learned Perceptual Image Patch Similarity (LPIPS) is often preferred as a metric function `D` for calculating loss due to its ability to capture semantic similarity between images better than simple L1 or L2 distances <a class="yt-timestamp" data-t="02:04:47">[02:04:47]</a>, <a class="yt-timestamp" data-t="02:04:50">[02:04:50]</a>, <a class="yt-timestamp" data-t="01:23:27">[01:23:27]</a>. This means a cat in a red sweater is semantically closer to a cat in a blue sweater than a dog in a red sweater, which LPIPS can discern <a class="yt-timestamp" data-t="01:24:04">[01:24:04]</a>.

2.  **Consistency Training (Standalone Mode)**: This method allows [[consistency_models_introduction_and_significance | consistency models]] to be trained from scratch, without relying on a pre-trained [[comparison_of_diffusion_models_and_consistency_models | diffusion model]] <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>, <a class="yt-timestamp" data-t="00:53:55">[00:53:55]</a>. In this mode, the model directly learns the properties of the score function, which describes how probability distributions change over time <a class="yt-timestamp" data-t="01:48:26">[01:48:26]</a>, <a class="yt-timestamp" data-t="01:50:02">[01:50:02]</a>. This makes them a new, independent family of generative models <a class="yt-timestamp" data-t="01:49:33">[01:49:33]</a>.

## Sampling and Performance

Once trained, [[consistency_models_introduction_and_significance | consistency models]] can generate samples by taking an initial noise distribution (typically Gaussian) and evaluating the consistency model in a single forward pass <a class="yt-timestamp" data-t="01:04:37">[01:04:37]</a>, <a class="yt-timestamp" data-t="01:04:50">[01:04:50]</a>. This single-step process significantly reduces the [[compute_efficiency_in_language_models | computational cost]] compared to [[comparison_of_diffusion_models_and_consistency_models | diffusion models]], which can require hundreds or thousands of steps <a class="yt-timestamp" data-t="01:44:40">[01:44:40]</a>, <a class="yt-timestamp" data-t="01:46:46">[01:46:46]</a>.

While they can achieve high quality in one step, multi-step sampling is also supported, allowing for further refinement of sample quality by alternating denoising and noise injection steps <a class="yt-timestamp" data-t="01:07:54">[01:07:54]</a>. This provides flexibility to trade [[compute_efficiency_in_language_models | compute]] for quality <a class="yt-timestamp" data-t="01:08:07">[01:08:07]</a>.

> [!abstract] Comparison to other models
> [[consistency_models_introduction_and_significance | Consistency models]] outperform existing distillation techniques for [[comparison_of_diffusion_models_and_consistency_models | diffusion models]] in one-step and few-step generation <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. As standalone generative models, they also outperform single-step non-adversarial generative models on standard benchmarks like CIFAR-10 and ImageNet <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>, <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. However, they may not consistently beat adversarial generative networks (GANs) in all metrics <a class="yt-timestamp" data-t="02:13:26">[02:13:26]</a>.

## Applications

[[consistency_models_introduction_and_significance | Consistency models]] support zero-shot data editing capabilities, meaning they can perform tasks without explicit training on those specific tasks <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>, <a class="yt-timestamp" data-t="01:10:08">[01:10:08]</a>. These applications include:
*   Image inpainting <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>
*   Colorization <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>
*   Super-resolution <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>
*   Stroke-guided image editing <a class="yt-timestamp" data-t="02:17:13">[02:17:13]</a>

They also enable interpolation between samples by traversing the latent space, similar to other latent variable models like GANs and VAEs <a class="yt-timestamp" data-t="01:11:05">[01:11:05]</a>.

## Connections to Other Fields

The development of [[consistency_models_introduction_and_significance | consistency models]] draws parallels to techniques in other fields of AI, particularly deep reinforcement learning. Concepts like the use of a "target network" (similar to the exponential moving average of parameters) and an "online network" are common in algorithms like Deep Q-Networks (DQNs) <a class="yt-timestamp" data-t="01:28:54">[01:28:54]</a>, <a class="yt-timestamp" data-t="01:29:50">[01:29:50]</a>. This cross-pollination of ideas highlights the potential for future advancements by applying insights from different domains of machine learning <a class="yt-timestamp" data-t="02:19:44">[02:19:44]</a>.