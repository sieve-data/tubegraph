---
title: Consistency models introduction and significance
videoId: 8b6NhnNYtpg
---

From: [[hu-po]] <br/> 

Consistency Models are a new family of generative models developed by OpenAI, aiming to overcome the slow sampling speed of [[comparisons_with_diffusion_models | diffusion models]] <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. This paper, described as very math-heavy and dense, was co-authored by Ilya Sutskever <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## Core Concept and Purpose
Consistency models are designed to enable efficient, one-step generation of high-quality samples, while also offering the flexibility of few-step sampling to trade compute for quality <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>. This contrasts with traditional [[comparisons_with_diffusion_models | diffusion models]], which typically require numerous iterative steps for image generation, leading to slow sampling speeds <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.

## Comparison with Diffusion Models
[[comparison_of_diffusion_models_and_consistency_models | Diffusion models]] have made significant breakthroughs in image, audio, and video generation <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>. However, their reliance on an iterative generation process means they often require 10 to 2000 times more compute than single-step generative models like GANs <a class="yt-timestamp" data-t="14:46:00">[14:46:00]</a>. Consistency models aim to achieve the advantages of [[comparisons_with_diffusion_models | diffusion models]] (e.g., high sample quality without adversarial training) but with the speed of single-step generation <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>.

The key difference lies in their approach:
*   **Diffusion Models** progressively perturb data to noise via Gaussian preparations and iteratively refine noise into an image over many steps <a class="yt-timestamp" data-t="28:18:00">[28:18:00]</a>.
*   **Consistency Models** learn to map any point on a "probability flow ODE" trajectory directly to its origin (the original clean image) <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. This allows them to go from noise to image in a single pass <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>.

### Probability Flow ODEs
A central concept to consistency models is the "probability flow Ordinary Differential Equation (ODE)" <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. ODEs are sets of equations that describe a system and its derivatives, often used in physics <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>. A probability flow ODE models how a given probability distribution evolves or changes over time, analogous to mass flow in physics <a class="yt-timestamp" data-t="22:10:00">[22:10:00]</a>. In this context, it smoothly converts data to noise <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>. The model learns to map any point ($x_t$) at any time ($t$) on this trajectory to its original, noise-free state ($x_0$) <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

The name "consistency models" comes from the fact that their outputs are "trained to be consistent for points on the same trajectory" <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>. This means that regardless of which point ($x_t$) on the trajectory (from noise to clean image) is fed into the model, it should consistently output the same original image <a class="yt-timestamp" data-t="56:52:00">[56:52:02]</a>.

## Key Features and Advantages
*   **Fast One-Step Generation**: This is the primary design goal, significantly speeding up image generation compared to [[comparisons_with_diffusion_models | diffusion models]] <a class="yt-timestamp" data-t="06:25:00">[06:25:00]</a>.
*   **Trade-off between Compute and Quality**: Consistency models allow for few-step sampling to improve sample quality by iterating, providing a flexible balance between speed and output fidelity <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>. This is described as a "very nice little feature" <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.
*   **Zero-Shot Data Editing**: They support tasks like image inpainting, colorization, and super-resolution without requiring explicit training on these tasks <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>. This includes applications in medical imaging like MRIs and CT scans <a class="yt-timestamp" data-t="14:14:00">[14:14:00]</a>.
*   **No Adversarial Training**: Unlike GANs, consistency models do not rely on adversarial training, making them less prone to issues like unstable training and mode collapse <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.
*   **Flexible Neural Network Architecture**: They do not impose strict constraints on [[use_of_neural_networks_in_consistency_models | neural network]] architectures <a class="yt-timestamp" data-t="12:10:00">[12:10:00]</a>. They leverage [[use_of_neural_networks_in_consistency_models | skip connections]], similar to ResNets, to help enforce boundary conditions and ensure differentiability <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>.

## How They Work
The core idea is to learn a [[use_of_neural_networks_in_consistency_models | neural network]] function, $F_\theta$, that takes any point $x_t$ along the ODE trajectory (which represents an image with a certain level of noise at time $t$) and maps it directly to the clean original image $x_0$ <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>.

For inference, the process is straightforward:
1.  Sample a random noise vector ($x_T$, representing the end of the diffusion process).
2.  Evaluate the consistency model $F_\theta(x_T, T)$ to directly obtain the generated image $x_0$ in one forward pass <a class="yt-timestamp" data-t="01:04:50">[01:04:50]</a>.

For multi-step sampling, the model can iteratively denoise and inject noise, allowing for a trade-off between quality and compute <a class="yt-timestamp" data-t="01:07:55">[01:07:55]</a>. This means steps are not strictly sequential (e.g., remove noise, remove noise, remove noise), but can involve adding noise back in between denoising steps <a class="yt-timestamp" data-t="01:09:10">[01:09:10]</a>.

## Training Methods
Consistency models can be trained in two ways:
1.  **Consistency Distillation**: This method involves distilling knowledge from a pre-trained [[comparisons_with_diffusion_models | diffusion model]] <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>. The pre-trained [[comparisons_with_diffusion_models | diffusion model]] acts as an "Oracle" to generate pairs of images at adjacent points along a diffusion trajectory (e.g., $x_t$ and $x_{t'}$), which the consistency model then learns to map consistently to the same origin $x_0$ <a class="yt-timestamp" data-t="00:52:05">[00:52:05]</a>. The loss function minimizes the difference between the outputs of the consistency model for these pairs <a class="yt-timestamp" data-t="01:19:12">[01:19:12]</a>.
2.  **Consistency Training (Standalone)**: This approach trains the consistency model from scratch, without reliance on a pre-trained [[comparisons_with_diffusion_models | diffusion model]] <a class="yt-timestamp" data-t="01:48:24">[01:48:24]</a>. It leverages an unbiased estimator for the score function <a class="yt-timestamp" data-t="01:50:07">[01:50:07]</a>, which simplifies to $(x_t - x) / t^2$ <a class="yt-timestamp" data-t="01:51:13">[01:51:13]</a>. This allows consistency models to be an independent family of generative models <a class="yt-timestamp" data-t="01:49:22">[01:49:22]</a>.

Both training methods utilize stochastic gradient descent (SGD) <a class="yt-timestamp" data-t="01:26:24">[01:26:24]</a>, with an exponential moving average (EMA) of model weights for stability and regularization <a class="yt-timestamp" data-t="01:26:32">[01:26:32]</a>. The EMA concept is inspired by [[latent_diffusion_models_and_their_internal_representations | deep reinforcement learning]]'s use of "target networks" and "online networks" <a class="yt-timestamp" data-t="01:28:56">[01:28:56]</a>.

### Technical Components
*   **Noise Distribution**: The noise added during the diffusion process is typically Gaussian <a class="yt-timestamp" data-t="00:28:20">[00:28:20]</a>.
*   **Numerical ODE Solvers**: Used to approximate solutions for ODEs. Popular choices include Euler (simpler, faster, less accurate, less stable) and Heun (slower, more complex, but more accurate) <a class="yt-timestamp" data-t="00:43:02">[00:43:02]</a>. Consistency distillation uses these solvers, while standalone consistency training aims to remove this dependency <a class="yt-timestamp" data-t="01:57:02">[01:57:02]</a>.
*   **Loss Metrics**: For measuring the difference between images, standard metrics like L1 and L2 distances are used, but LPIPS (Learned Perceptual Image Patch Similarity) is often preferred due to its ability to capture semantic similarity better than pixel-wise differences <a class="yt-timestamp" data-t="01:23:27">[01:23:27]</a>.

## Performance and Benchmarks
Consistency models demonstrate strong performance:
*   They outperform existing distillation techniques for [[comparisons_with_diffusion_models | diffusion models]] in one-step generation <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.
*   They achieve new state-of-the-art FID (Fréchet Inception Distance) on datasets like CIFAR-10 and ImageNet 64x64 <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>. The FID metric, especially on small, grainy datasets like CIFAR-10, is viewed with skepticism by some, who prefer human evaluation <a class="yt-timestamp" data-t="02:02:02">[02:02:02]</a>.
*   As standalone generative models, they outperform other single-step non-adversarial generative models on standard benchmarks <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.
*   When compared to adversarial models like GANs, their performance can be competitive, though the speaker notes GANs can sometimes be better <a class="yt-timestamp" data-t="02:13:26">[02:13:26]</a>.

## Applications
Beyond general image, audio, and video generation, consistency models are particularly adept at:
*   **Zero-shot image editing**: This includes tasks like image inpainting, colorization, and super-resolution <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>. They can also perform stroke-guided image editing, where a user's drawing guides the generation process <a class="yt-timestamp" data-t="02:17:13">[02:17:13]</a>.
*   **Interpolation in latent space**: Similar to [[latent_diffusion_models_and_their_internal_representations | latent variable models]] like GANs and VAEs, consistency models can interpolate between samples by traversing their [[latent_diffusion_models_and_their_internal_representations | latent space]] <a class="yt-timestamp" data-t="01:11:03">[01:11:03]</a>.

## Significance
Consistency models represent a significant advancement in generative modeling by offering a new paradigm that combines the quality of [[comparisons_with_diffusion_models | diffusion models]] with the speed of single-step generation <a class="yt-timestamp" data-t="02:18:01">[02:18:01]</a>. Their ability to trade off compute for quality and perform zero-shot editing makes them highly versatile. The work also highlights potential [[challenges_and_innovations_in_model_adaptation | cross-pollination of ideas]] from other fields like [[latent_diffusion_models_and_their_internal_representations | deep reinforcement learning]] <a class="yt-timestamp" data-t="02:19:39">[02:19:39]</a>.