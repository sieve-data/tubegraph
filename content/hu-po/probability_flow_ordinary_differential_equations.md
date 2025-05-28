---
title: Probability Flow Ordinary Differential Equations
videoId: 8b6NhnNYtpg
---

From: [[hu-po]] <br/> 

[[Consistency models | Consistency Models]], a new family of generative models, are built upon the concept of Probability Flow Ordinary Differential Equations (PF-ODEs) <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

## Definition and Purpose
A Probability Flow Ordinary Differential Equation (PF-ODE) combines probability theory with ordinary differential equations to model the dynamics of [[concepts_of_probability_distributions_in_ml | probability distributions]] over time <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>. It serves as a framework to understand how a given [[concepts_of_probability_distributions_in_ml | probability distribution]] evolves or changes <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>. In essence, these are differential equations that describe the change of a [[concepts_of_probability_distributions_in_ml | probability distribution]] over time <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>.

PF-ODEs are particularly useful in machine learning, physics, and finance, especially where system behavior involves stochastic processes or random variables <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>. In the context of [[Consistency models | Consistency Models]], a PF-ODE smoothly converts data to noise <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>, or conversely, noise back to data <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.

## Relation to Diffusion Models
PF-ODEs are closely related to [[Conditional diffusion models for neural networks | diffusion models]], which progressively perturb data into noise using Gaussian perturbations <a class="yt-timestamp" data-t="02:28:14">[02:28:14]</a> <a class="yt-timestamp" data-t="00:28:19">[00:28:19]</a>. While [[Conditional diffusion models for neural networks | diffusion models]] typically involve an iterative process of adding or removing noise over fixed steps <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>, PF-ODEs model this as a continuous trajectory <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

### Mathematical Representation
The diffusion process is initially described by a stochastic differential equation (SDE):
`dxt = μ(xt, t)dt + G(t)dWT` <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>
where:
*   `xt` is the image at time `t` <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>.
*   `μ(xt, t)` is the drift coefficient, influencing the mean of the distribution <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.
*   `G(t)` is the diffusion coefficient <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.
*   `WT` denotes standard Brownian motion, representing random fluctuations <a class="yt-timestamp" data-t="00:31:02">[00:31:02]</a>.

A remarkable property of this SDE is that its solution trajectory can be represented by an ordinary differential equation, dubbed the Probability Flow ODE <a class="yt-timestamp" data-t="00:32:35">[00:32:35]</a>:
`dxt = [μ(xt, t) - 0.5 * G(t)^2 * ∇log(pt(xt))]dt` <a class="yt-timestamp" data-t="00:33:16">[00:33:16]</a>

Here, `∇log(pt(xt))` is known as the **score function**, a crucial component in [[Bayesian Flow Networks | score-based generative models]] <a class="yt-timestamp" data-t="00:34:47">[00:34:47]</a>.

For simplified configurations (common in [[Conditional diffusion models for neural networks | diffusion models]]), `μ(xt, t)` is set to 0 and `G(t)^2` to `2t` <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. In this case, the distribution `pt(x)` becomes a convolution of the data distribution `pdata(x)` with a Gaussian distribution centered at zero and variance `t^2` <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>. At time `t=T` (the end of the process), the distribution is a pure Gaussian noise distribution <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>.

## Empirical PF-ODE and Score Models
To utilize PF-ODEs for image generation, a **score model** `s_phi(x_t, t)` (a separate neural network parameterized by `phi`) is trained to approximate the score function <a class="yt-timestamp" data-t="00:38:07">[00:38:07]</a> <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>. This approximation leads to the empirical PF-ODE:
`dxt/dt = -t * s_phi(xt, t)` <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a> <a class="yt-timestamp" data-t="00:40:51">[00:40:51]</a>

### Solving PF-ODEs
During inference (image generation), the empirical PF-ODE is solved **backwards in time** using [[Rectified flow in diffusion models | numerical ODE solvers]] <a class="yt-timestamp" data-t="00:41:21">[00:41:21]</a>. This means starting from noise (at time `T`) and iteratively moving towards the desired image (at time `0`) <a class="yt-timestamp" data-t="00:41:56">[00:41:56]</a>. Common solvers include the Euler solver (simpler, faster, less accurate) and the Heun solver (more complex, slower, more accurate) <a class="yt-timestamp" data-t="00:43:02">[00:43:02]</a>. Other multi-step methods like Adam-Bashford and Adams-Moulton also exist <a class="yt-timestamp" data-t="01:17:25">[01:17:25]</a>.

## Consistency Models and PF-ODEs
[[Consistency models | Consistency Models]] are designed to directly map any point on the PF-ODE trajectory back to the original data point (the generated image) <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a> <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>. This allows for fast, one-step image generation, reducing the computational cost inherent in iterative [[scaling_and_optimization_in_diffusion_models | diffusion model sampling]] <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a> <a class="yt-timestamp" data-t="00:50:54">[00:50:54]</a>.

[[Consistency models | Consistency Models]] can be trained in two ways:
1.  **Distillation Mode**: By distilling knowledge from pre-trained [[Conditional diffusion models for neural networks | diffusion models]] <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a> <a class="yt-timestamp" data-t="00:51:17">[00:51:17]</a>. This involves using the pre-trained model to generate pairs of adjacent points on PF-ODE trajectories and minimizing the difference in outputs for these pairs <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.
2.  **Standalone Generative Model**: Trained independently without relying on pre-trained [[Conditional diffusion models for neural networks | diffusion models]] <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a> <a class="yt-timestamp" data-t="01:48:24">[01:48:24]</a>. This uses an unbiased estimator of the score function based on the identity `s(x_t, t) = E[ (x_t - x) / t^2 | x_t ]` <a class="yt-timestamp" data-t="01:50:07">[01:50:07]</a>.

The ability to directly map any point on the trajectory to the origin (the final image) is key to enabling flexible sampling and applications like [[DreamFusion and its relation to diffusion models | zero-shot data editing]] <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a> <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.