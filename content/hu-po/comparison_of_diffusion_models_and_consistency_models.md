---
title: Comparison of diffusion models and consistency models
videoId: 8b6NhnNYtpg
---

From: [[hu-po]] <br/> 

[[consistency_models_introduction_and_significance | Consistency Models]] (CMs) are a new family of generative models, emerging from OpenAI, designed to address the slow sampling speeds inherent in traditional [[diffusion_models_and_controlnet | diffusion models]] (DMs) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. While DMs have achieved significant breakthroughs in image, audio, and video generation, their iterative generation process can require 10 to 2000 times more compute compared to single-step generative models <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>, <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.

## Core Principles

### [[diffusion_models_and_controlnet | Diffusion Models]]
[[diffusion_models_and_controlnet | Diffusion Models]] operate on a paradigm of smoothly converting data to noise during training and then iteratively refining noise into an image during inference <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Training**: They start from an actual image and progressively add Gaussian noise to it, moving from a time step of 0 to a capital T time step (pure noise) <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>, <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>.
*   **Inference**: They reverse this process, starting from pure Gaussian noise (at time T) and iteratively removing noise over many steps to generate the desired image (moving backwards to time 0) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>, <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>. Each step removes some amount of noise <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Mathematical Basis**: DMs are built upon probability flow Ordinary Differential Equations (ODEs) that smoothly transition data distributions to noise <a class="yt-timestamp" data-t="01:15:12">[01:15:12]</a>.
*   **Architecture**: DMs do not impose strict constraints on model architectures, unlike auto-regressive models or Variational Autoencoders (VAEs) <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. Many [[diffusion_models_and_controlnet | diffusion models]] also operate in a [[latent_diffusion_models_and_their_internal_representations | latent/embedding space]] for efficiency <a class="yt-timestamp" data-t="01:10:46">[01:10:46]</a>.

### [[consistency_models_introduction_and_significance | Consistency Models]]
[[consistency_models_introduction_and_significance | Consistency Models]] are designed to directly map any point on a probability flow ODE trajectory to its origin (the original data, or `x_sigma` where `sigma` is a small non-zero value for numerical stability) in a single step <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>, <a class="yt-timestamp" data-t="00:55:12">[00:55:12]</a>.
*   **Consistency Property**: Their outputs are trained to be "consistent" for any points on the same trajectory. This means that regardless of how far along the "noise" trajectory an input image is, the model should produce the same original image <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, <a class="yt-timestamp" data-t="00:56:52">[00:56:52]</a>.
*   **One-Step Generation**: CMs support fast one-step generation by design, requiring only a single network evaluation to convert a random noise vector into a data sample <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>, <a class="yt-timestamp" data-t="01:05:03">[01:05:03]</a>.
*   **Quality vs. Compute Trade-off**: Crucially, CMs still allow for few-step sampling to trade compute for quality. By chaining outputs and re-injecting noise, they can improve sample quality with additional steps <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>, <a class="yt-timestamp" data-t="01:08:07">[01:08:07]</a>, <a class="yt-timestamp" data-t="02:22:50">[02:22:50]</a>.
*   **Training Approaches**:
    1.  **Distillation Mode**: CMs can distill the knowledge of pre-trained [[diffusion_models_and_controlnet | diffusion models]] (e.g., Stable Diffusion) into a single-step sampler <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>, <a class="yt-timestamp" data-t="00:51:17">[00:51:17]</a>. This involves using the pre-trained DM to generate pairs of adjacent points on a trajectory and training the CM by minimizing the output difference for these pairs <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.
    2.  **Standalone Training**: CMs can also be trained in isolation, without dependence on pre-trained [[diffusion_models_and_controlnet | diffusion models]] <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>, <a class="yt-timestamp" data-t="00:53:55">[00:53:55]</a>, <a class="yt-timestamp" data-t="01:48:24">[01:48:24]</a>. This positions them as an independent family of generative models <a class="yt-timestamp" data-t="02:22:49">[02:22:49]</a>.

## [[comparisons_with_diffusion_models | Comparisons with Diffusion Models]]

| Feature              | [[diffusion_models_and_controlnet | Diffusion Models]]                 | [[consistency_models_introduction_and_significance | Consistency Models]]             |
| :------------------- | :----------------------------------- | :----------------------------- |
| **Sampling Speed**   | Slow, iterative (10s to 1000s of steps) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>, <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a> | Fast, one-step by design <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a> |
| **Generation Process** | Iterative refinement from noise <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a> | Direct mapping from any point on ODE trajectory to origin <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a> |
| **Quality/Compute Trade-off** | Yes, more steps generally mean higher quality <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a> | Yes, inherent feature allowing user choice of steps <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a> |
| **Adversarial Training** | No, less prone to unstable training/mode collapse <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a> | No <a class="yt-timestamp" data-t="00:46:28">[00:46:28]</a>                               |
| **Architecture Constraints** | More flexible <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>                 | Flexible [[use_of_neural_networks_in_consistency_models | neural network]] architectures <a class="yt-timestamp" data-t="00:47:48">[00:47:48]</a> |
| **Zero-Shot Data Editing** | Yes (e.g., inpainting, colorization) <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a> | Yes, by modifying multi-step sampling <a class="yt-timestamp" data-t="01:11:50">[01:11:50]</a> |
| **Training Independence** | Usually trained from scratch on specific datasets <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a> | Can be distilled from pre-trained DMs or trained standalone <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a> |

### Advantages of [[consistency_models_introduction_and_significance | Consistency Models]]
*   **Efficiency**: The primary advantage of CMs is their ability to generate high-quality samples with significantly fewer steps, ideally in a single step <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   **Flexibility**: They offer a continuous trade-off between computation and sample quality, allowing users to choose the desired balance <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Independence**: CMs can be trained independently of existing [[diffusion_models_and_controlnet | diffusion models]], making them a distinct class of generative models <a class="yt-timestamp" data-t="01:48:24">[01:48:24]</a>.

### Challenges and Considerations
*   **Benchmarking**: Evaluating generative models, especially on low-resolution datasets like CIFAR-10, with metrics like FID (Fréchet Inception Distance) or Inception Score can be misleading due to the grainy nature of the images and the limitations of the quantitative metrics <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>, <a class="yt-timestamp" data-t="02:02:02">[02:02:02]</a>.
*   **Hyperparameter Tuning**: Optimal hyperparameter values (e.g., for step schedules) may vary based on image resolution or modality, requiring application-specific tuning <a class="yt-timestamp" data-t="02:10:14">[02:10:14]</a>.
*   **[[use_of_neural_networks_in_consistency_models | Neural Network]] Implementation**: While CMs support flexible [[use_of_neural_networks_in_consistency_models | neural network]] architectures, certain mathematical operations like Jacobian-vector products and forward-mode automatic differentiation might not be well-supported in all deep learning frameworks <a class="yt-timestamp" data-t="01:44:47">[01:44:47]</a>.

Overall, [[consistency_models_introduction_and_significance | Consistency Models]] represent a significant step towards faster and more flexible generative model sampling, building upon the strengths of [[diffusion_models_and_controlnet | diffusion models]] while mitigating their primary weakness of slow inference. They also demonstrate exciting possibilities for cross-pollination of ideas from other fields like deep reinforcement learning through concepts like target and online networks <a class="yt-timestamp" data-t="02:19:39">[02:19:39]</a>.