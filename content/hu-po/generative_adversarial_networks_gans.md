---
title: Generative adversarial networks GANs
videoId: ExfMg4v5DMA
---

From: [[hu-po]] <br/> 

Generative Adversarial Networks (GANs) are a class of deep generative models that have achieved significant success in synthesizing realistic visual content <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Co-invented by Ian Goodfellow, the foundational GAN paper has garnered over 59,000 citations <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. While [[innovations_in_generative_ai_from_gans_to_diffusion_models | diffusion models]] have recently gained popularity, GANs are experiencing a resurgence due to their unique properties and capabilities <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

## How GANs Work

At their core, GANs involve two neural networks, a generator and a discriminator, locked in an adversarial training process <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. The generator creates new data samples, while the discriminator tries to distinguish between real data and the generator's fake data. Through this competition, both networks improve, leading to the generation of highly realistic outputs <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

### Unconditional vs. Conditional GANs

*   **Unconditional GANs**: These models transform a low-dimensional randomly supplied latent factor (often called "noise" or a "latent vector") into photorealistic images <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>. The generator takes this vector as input and produces an image <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
*   **Conditional GANs**: These networks receive an additional input, or "condition," which can be anything from text, to segmentation maps, to 3D variables, allowing for more controlled generation <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>.

### Latent Space Manipulation

A key aspect of GANs is their [[generative_latent_space_reasoning | latent space reasoning]] <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. The shared latent space allows for "embedding space math," where operations like `smiling woman - neutral woman + neutral man = smiling man` can be performed on image features <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. Moving within this latent space can lead to meaningful interpolations, where intermediate points between two distinct images (e.g., a closed mouth lion and an open mouth lion) still produce coherent, realistic outputs <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.

However, traditional latent space manipulation often only allowed for coarse geometric or semantic attribute editing <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>. The controllability of GANs has been a critical requirement for real-world applications <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

### Alias Artifacts

Early GANs, particularly StyleGAN, were known to produce "alias artifacts," where textures or features might remain static while the object itself moves <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>. For example, a person's hair texture might stay in place while their face rotates <a class="yt-timestamp" data-t="01:11:22">[01:11:22]</a>. Later advancements, like alias-free GANs, addressed this issue <a class="yt-timestamp" data-t="01:12:07">[01:12:07]</a>.

## DragGAN: Interactive Point-Based Manipulation

DragGAN is a recent GAN-based paper that introduces an interactive, point-based method for manipulating generative images <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Developed by institutions including Max Planck Institute, MIT CSAIL, and Google AR/VR, its demo showcases impressive capabilities <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### Core Functionality

DragGAN allows users to "drag" content in a generated image by selecting a "handle point" and a "target point" <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. The system then moves the handle point to precisely reach the target, while keeping the rest of the image contextually sensible <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This enables control over spatial attributes like pose, shape, expression, and layout across diverse object categories <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

Key features include:
*   **Semantic Consistency**: When moving a nose, the entire head moves, not just the nose. When pulling a mouth, it opens and generates the inside, including teeth <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This demonstrates the model's ability to hallucinate occluded content and deform shapes while maintaining object rigidity <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Interactive Control**: Users can specify multiple handle and target points <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.
*   **Region-Specific Editing**: An optional binary mask allows users to define a movable region, attempting to keep unmasked areas fixed <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. However, masking in feature space rather than image space can still lead to slight changes in unmasked regions <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>.

### Technical Approach

DragGAN consists of two main components, both leveraging the discriminative features of the GAN's intermediate layers:
1.  **Feature-based Motion Supervisor**: This component drives the handle points towards their target positions <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. It uses a motion supervision loss to optimize the latent code, specifically targeting the feature maps after the sixth block of the StyleGAN2 architecture for optimal balance between resolution and discriminativeness <a class="yt-timestamp" data-t="00:53:44">[00:53:44]</a>. This optimization is iterative, causing slight movements in each step <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>.
2.  **Point Tracking Approach**: This keeps localizing the position of the handle points as the image deforms <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. It updates the handle points by performing a nearest-neighbor search in the feature space for the closest corresponding feature <a class="yt-timestamp" data-t="01:12:29">[01:12:29]</a>. This avoids the need for additional neural networks like those used in [[techniques_used_in_ai_video_generation | optical flow]] estimation, contributing to efficiency <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a>.

The process is iterative, repeating motion supervision and point tracking until handle points reach their targets, typically taking 20 to 200 iterations <a class="yt-timestamp" data-t="00:51:12">[00:51:12]</a>. The approach runs in a few seconds on a single RTX 3090 GPU <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>.

#### StyleGAN2 Architecture and Latent Spaces

DragGAN is built upon the StyleGAN2 architecture <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>. StyleGAN2 uses a 512-dimensional latent code (Z) which is mapped to an intermediate latent code (W) <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a>. The W is then sent to the generator, which produces the output image <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.
*   **W Space**: The space of the W latent code.
*   **W+ Space**: Allows different W values to be fed to different layers of the generator, offering more expressiveness and enabling "out of distribution" manipulations (e.g., a blinking cat, which might not be in the training data distribution) <a class="yt-timestamp" data-t="01:55:51">[01:55:51]</a>. DragGAN uses the W+ space for better editability <a class="yt-timestamp" data-t="01:05:53">[01:05:53]</a>.

The layers at the bottom of the GAN's convolutional network deal with low-level concepts like texture and positioning, while higher layers handle more semantic, high-level features <a class="yt-timestamp" data-t="01:06:09">[01:06:09]</a>. DragGAN focuses on updating the W for the first six layers to control spatial attributes, while fixing others to preserve appearance <a class="yt-timestamp" data-t="01:07:27">[01:07:27]</a>.

### Comparison to Other Methods

DragGAN significantly outperforms previous approaches like "User Controllable LT" in terms of naturalness, precision, and image quality <a class="yt-timestamp" data-t="01:36:38">[01:36:38]</a>. While User Controllable LT might accidentally change background or semantic concepts (e.g., turning a dress into pants when posing an arm), DragGAN maintains the original semantic meaning of the image <a class="yt-timestamp" data-t="01:30:09">[01:30:09]</a>.

It also outperforms state-of-the-art point tracking methods like Raft and Pips, despite its "simplicity" (not requiring additional complex networks) <a class="yt-timestamp" data-t="01:09:57">[01:09:57]</a>.

## Applications and Future Work

DragGAN's flexible point-based manipulation can be applied to various scenarios, including:
*   Adjusting pose, shape, expression, and body parts of humans or animals in casual photos <a class="yt-timestamp" data-t="01:12:42">[01:12:42]</a>.
*   [[image_synthesis_and_editing_using_gans | Image synthesis and editing using GANs]] for professional movie pre-visualization or e-commerce <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>.
*   Manipulating real images by first performing GAN inversion to map them into the latent space <a class="yt-timestamp" data-t="01:24:57">[01:24:57]</a>.

Future work on DragGAN aims to extend point-based image editing to 3D generative models <a class="yt-timestamp" data-t="01:53:01">[01:53:01]</a>. Other potential extensions include applying the technique to [[innovations_in_generative_ai_from_gans_to_diffusion_models | diffusion models]] (though slower due to iterative denoising steps) <a class="yt-timestamp" data-t="01:35:31">[01:35:31]</a>, and incorporating speech-based control for more intuitive image editing <a class="yt-timestamp" data-t="01:19:57">[01:19:57]</a>.