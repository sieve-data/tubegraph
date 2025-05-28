---
title: Zero shot image editing capabilities
videoId: 8b6NhnNYtpg
---

From: [[hu-po]] <br/> 

Zero-shot image editing capabilities refer to the ability of a generative model to perform image manipulation tasks without requiring explicit training on those specific tasks <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This means the model can adapt to new editing requirements based on its general understanding of image generation and transformation <a class="yt-timestamp" data-t="02:16:18">[02:16:18]</a>.

## How [[Consistency Models]] Enable Zero-Shot Editing

[[Consistency Models]], a new family of generative models, are designed to support fast one-step generation while also allowing for few-step sampling to trade compute for quality <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. This multi-step sampling procedure is crucial for their [[Zero shot image editing capabilities | zero-shot data editing applications]] <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>.

Instead of traditional [[Image generation using advanced mathematical models | diffusion models]] that rely on fixed iterative steps <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>, [[Consistency Models]] learn a function that can map any point on a probability flow ordinary differential equation (ODE) trajectory directly to the original image <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This allows for flexible generation, including the ability to perform zero-shot editing by modifying the multi-step sampling process <a class="yt-timestamp" data-t="02:16:29">[02:16:29]</a>.

The models are trained to recover an original image (`X Sigma`) from any noisy input (`Xt`) across a continuum of noise levels, which allows them to perform denoising for various levels <a class="yt-timestamp" data-t="01:11:13">[01:11:13]</a>. The multi-step generation procedure is particularly useful for solving inverse problems in a zero-shot manner, often through iterative replacement procedures <a class="yt-timestamp" data-t="01:11:26">[01:11:26]</a>.

## Applications

[[Zero shot image editing capabilities]] allow [[Consistency Models]] to solve challenging inverse problems <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. Demonstrated applications include:
*   **Image Inpainting** <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>
*   **Colorization** (e.g., colorizing grayscale bedroom images) <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>, <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>, <a class="yt-timestamp" data-t="02:16:42">[02:16:42]</a>
*   **Super-resolution** <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>
*   **Stroke-guided image editing** (where a user provides strokes to condition image generation) <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>, <a class="yt-timestamp" data-t="02:16:52">[02:16:52]</a>, <a class="yt-timestamp" data-t="02:17:13">[02:17:13]</a>
*   **Photography** and potentially **Medical Resonance Imaging (MRIs)** and **CT scans** <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>, <a class="yt-timestamp" data-t="01:14:11">[01:14:11]</a>.

## Comparison to Other Models

While many [[Foundation models in computer vision | generative models]] offer similar editing functionalities <a class="yt-timestamp" data-t="02:18:48">[02:18:48]</a>, [[Consistency Models]] are notable for their ability to perform these tasks without requiring explicit training datasets for each specific task <a class="yt-timestamp" data-t="01:10:08">[01:10:08]</a>, differentiating them from methods that might prepare large synthetic datasets for distillation <a class="yt-timestamp" data-t="02:10:50">[02:10:50]</a>.

Unlike [[GANbased image manipulation | GANs]] or Variational Autoencoders (VAEs), [[Consistency Models]] do not rely on adversarial training, making them less prone to issues like unstable training and mode collapse <a class="yt-timestamp" data-t="01:11:02">[01:11:02]</a>, <a class="yt-timestamp" data-t="01:11:27">[01:11:27]</a>. They can also easily interpolate between samples by traversing a latent space, similar to other latent variable models <a class="yt-timestamp" data-t="01:11:05">[01:11:05]</a>.