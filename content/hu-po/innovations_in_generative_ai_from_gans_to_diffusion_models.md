---
title: Innovations in generative AI From GANs to diffusion models
videoId: eTBG17LANcI
---

From: [[hu-po]] <br/> 

Generative AI has seen a significant "Renaissance" in recent years, with neural architectures like [[Challenges and innovations in AI model architecture and scaling | Transformers]] subsuming various domains including natural language processing and vision [00:07:04]. This article explores the progression from early generative models like [[Generative adversarial networks GANs | GANs]] to the highly impressive [[Techniques used in AI video generation | diffusion models]] currently achieving state-of-the-art image quality.

## Early Generative Models: GANs

[[Generative adversarial networks GANs | Generative Adversarial Networks (GANs)]] were a foundational development in generative AI, first proposed around 2014 [01:14:08]. While revolutionary for their time, the image quality produced by early [[Generative adversarial networks GANs | GANs]] was comparatively low, often appearing grainy and lacking detail [01:13:52].

## The Rise of Diffusion Models

[[Techniques used in AI video generation | Diffusion models]], officially known as Denoising Diffusion Probabilistic Models (DDPMs), have gained prominence [01:15:23, 01:15:26]. These models operate by progressively adding Gaussian noise to real data (the "forward noising process") and then learning to reverse this process to remove the noise [01:51:00, 02:18:50, 02:51:52].

Key improvements in [[Techniques used in AI video generation | diffusion models]] include:
*   Improved sampling techniques, such as classifier-free guidance [01:15:52, 01:16:07]. Classifier-free guidance involves randomly dropping out the conditioning class during training, allowing the model to learn both conditional and unconditional generation [02:21:05, 02:56:08].
*   Predicting noise parameters (mean and variance) instead of just the noise itself [01:36:33, 01:36:38, 02:40:46].
*   Using cascaded DDPM pipelines [01:16:12, 01:16:54].

### Latent Diffusion Models

Training [[Techniques used in AI video generation | diffusion models]] directly in high-resolution pixel space can be computationally prohibitive [02:30:52]. To address this, [[Generative 3D models using video diffusion | latent diffusion models]] perform the diffusion process in a lower-dimensional latent space [01:10:04, 01:10:07, 02:32:00, 02:37:35]. They utilize off-the-shelf convolutional variational autoencoders (VAEs) to convert images into latent vectors and vice-versa [02:48:07, 02:49:07]. For instance, a 256x256x3 image might be converted to a 32x32x4 latent embedding, significantly reducing computational load [02:52:19, 02:52:23, 02:52:25, 02:52:26].

## Diffusion Transformers (DiTs)

A recent and "incredibly impressive" innovation comes from UC Berkeley, New York University, and Meta AI (FAIR team) with their paper "Scalable Diffusion Models with Transformers" [01:14:04, 01:17:14, 01:36:00]. This work introduces Diffusion Transformers (DiTs), which replace the commonly used U-Net backbone in [[Techniques used in AI video generation | diffusion models]] with a [[Challenges and innovations in AI model architecture and scaling | Transformer]] architecture that operates on latent patches [00:59:09, 00:59:11, 00:59:19, 02:20:00].

### Architecture and Operation

DiTs adhere to the best practices of [[Techniques used in AI video generation | Vision Transformers]] (ViTs) [00:59:48, 00:59:52]. Instead of using convolutional kernels to process an image, a ViT takes an image, cuts it into small patches, and feeds each patch as a token into the [[Challenges and innovations in AI model architecture and scaling | Transformer]] [01:09:09, 01:09:11, 01:09:28, 01:09:33]. Each patch is combined with a positional embedding to inform the [[Challenges and innovations in AI model architecture and scaling | Transformer]] of its original location within the image [02:54:02, 02:54:08, 02:59:42].

The input to a DiT is a spatial latent representation, which is patchified (e.g., using 2x2, 4x4, or 8x8 patches) and fed into a sequence of [[Challenges and innovations in AI model architecture and scaling | Transformer]] blocks [02:57:08, 03:00:00, 03:19:00]. The network is conditioned on additional information such as the noise time step and class labels (e.g., "dog," "airplane") [02:24:00, 02:24:05, 02:29:22, 02:29:29, 03:02:25, 03:02:54, 03:05:07]. This conditioning is often done via an additional multi-head cross-attention layer within the [[Challenges and innovations in AI model architecture and scaling | Transformer]] blocks [03:03:57, 03:03:59, 03:04:02].

DiTs incorporate adaptive normalization layers, which are crucial for maintaining well-distributed and stable numerical values within the network, especially as models become deeper and wider [03:06:09, 03:09:20, 03:09:51, 03:14:00, 03:15:21, 03:15:32]. Residual connections are also used to facilitate information flow between different abstraction layers of the neural network [03:17:12, 03:17:14, 03:17:25].

### [[Performance and scalability of diffusion models with Transformers | Scaling and Performance]]

The paper investigates the [[Performance and scalability of diffusion models with Transformers | scalability]] of DiTs, finding a strong correlation between network complexity (measured in G-flops) and sample quality (measured by FID score) [01:05:26, 01:05:28, 01:11:16, 01:11:18, 01:11:20]. Larger models with increased [[Training and implementation details of Transformerbased diffusion models | Transformer]] depth and width, or more input tokens (smaller patch sizes), consistently achieve better FID scores [01:05:42, 01:05:43, 01:05:45, 01:05:51, 01:12:42, 01:12:54].

The largest model, DiT-XL/2 (meaning it uses a patch factor of two), achieved state-of-the-art results with a 2.27 FID score on the 256x256 ImageNet benchmark [01:16:15, 01:16:18, 01:16:19, 01:47:50, 01:47:52, 01:48:50, 01:49:24, 01:50:35]. This model is computationally efficient and outperforms prior U-Net based models like ADM [01:12:45, 01:12:48, 01:13:01]. The visual results demonstrate "extremely crisp" image quality, with correct semantic information and minimal artifacts across various scales [00:33:01, 00:33:02, 00:33:04, 00:33:07, 00:33:41, 00:34:44]. The ability to capture subtle details, like the wrist of a dog, highlights the model's sophistication [00:35:53, 00:35:56, 00:36:01, 00:36:04].

### [[Training and implementation details of Transformerbased diffusion models | Training and Implementation Details]]

DiT models were implemented in JAX (a Google framework) and trained on Google's TPU v3 pods [01:51:15, 01:51:19, 01:52:05, 01:52:08, 01:52:10]. Training the largest models, such as DiT-XL/2, involved 400,000 training steps [01:54:46]. On a 256-unit TPU v3 pod, this translates to approximately 19 hours of training, costing over $10,000 per model [01:54:50, 01:55:01, 01:55:06, 01:55:07, 01:55:10, 01:55:14, 01:55:20].

The paper also notes that while more sampling steps generally lead to slightly better results, there's a point of diminishing returns, with 256 steps being a sweet spot for the best trade-off between speed and performance [02:03:00, 02:03:04, 02:03:06, 02:03:09, 02:03:14, 02:03:15, 02:04:02, 02:04:04, 02:04:05, 02:04:07, 02:04:09, 02:04:12].

Remarkably, many of the training hyperparameters, such as learning rates, decay schedules, and optimizers, were adopted directly from prior work (ADM) without specific tuning for this paper [01:48:20, 01:48:22, 01:48:24, 01:48:25, 01:48:30, 01:48:32, 01:48:34]. This suggests that further optimization of these parameters could lead to even greater performance improvements [01:48:35, 01:48:36, 01:48:54, 01:48:57].

## Future Outlook

The rapid acceleration in the quality of generative AI, particularly with [[Techniques used in AI video generation | diffusion models]], suggests exciting possibilities [01:14:21, 01:14:31, 01:14:33, 01:14:36, 01:14:38, 01:14:40, 01:14:43, 01:14:45]. It is conceivable that within the next year, APIs capable of generating 4K video from text prompts could become available [01:15:02, 01:15:05]. This would fundamentally change content creation, making high-quality generative capabilities accessible to a wider audience and potentially turning "every single human" into an AI content generator [01:15:11, 01:15:13, 01:15:16, 01:15:17, 01:15:19, 01:15:20, 01:15:23, 01:15:25, 01:15:26, 01:15:28].