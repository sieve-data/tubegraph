---
title: Transformer architecture in diffusion models
videoId: eTBG17LANcI
---

From: [[hu-po]] <br/> 

Diffusion models are a class of generative models that have seen significant advancements, particularly in image generation <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>. Traditionally, these models have relied on [[Conditional diffusion model for neural networks | U-Net]] architectures as their backbone <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>. However, recent research demonstrates that Transformers can successfully replace the U-Net backbone, leading to state-of-the-art image quality <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>, <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>.

## Diffusion Transformers (DiTs)

A new class of diffusion models, termed Diffusion Transformers (DiTs), leverages the Transformer architecture <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>, <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>. This approach challenges the notion that the U-Net bias is crucial for diffusion model performance, suggesting that standard Transformer designs are viable alternatives <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.

### Core Principles

DiTs adhere to the best practices of Vision Transformers (ViTs) <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>. In a ViT, an image is divided into small patches, and each patch is treated as a token in a sequence, similar to how Transformers process words in a sentence <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>. This sequence of patches is then fed into the Transformer <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>.

### Latent Space Operation

[[Latent diffusion model for neural networks | Latent diffusion models]] (LDMs) perform the diffusion process in a lower-dimensional latent space to reduce computational costs <a class="yt-timestamp" data-t="27:28:00">[27:28:00]</a>, <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>. DiTs extend this by replacing the U-Net in LDMs with a Transformer that operates on these latent patches <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.

For instance, a 256x256x3 image is first encoded into a latent representation of 32x32x4 using an off-the-shelf convolutional VAE <a class="yt-timestamp" data-t="29:17:00">[29:17:00]</a>, <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>. The DiT then processes this lower-dimensional latent vector <a class="yt-timestamp" data-t="29:21:00">[29:21:00]</a>.

### Architectural Details

*   **Patchification**: The latent representation is "patchified" into smaller sub-regions. The paper investigates patch sizes (P) of 2, 4, and 8, which determine the number of input tokens (T) for the Transformer <a class="yt-timestamp" data-t="31:19:00">[31:19:00]</a>, <a class="yt-timestamp" data-t="43:51:00">[43:51:00]</a>. Smaller patch sizes lead to a quadrupling of tokens and GigaFLOPs (GFLOPs), increasing computational complexity <a class="yt-timestamp" data-t="31:52:00">[31:52:00]</a>.
*   **Positional Embeddings**: DiTs incorporate ViT frequency-based positional embeddings to inform the Transformer about the original spatial location of each patch <a class="yt-timestamp" data-t="29:42:00">[29:42:00]</a>, <a class="yt-timestamp" data-t="29:48:00">[29:48:00]</a>.
*   **Conditional Information**: Beyond the noisy latent input, DiTs can be conditioned on:
    *   Noise time step (T) <a class="yt-timestamp" data-t="32:25:00">[32:25:00]</a>
    *   Class labels (C) <a class="yt-timestamp" data-t="32:25:00">[32:25:00]</a>
    *   Natural language prompts (text prompts) <a class="yt-timestamp" data-t="32:57:00">[32:57:00]</a>

    This conditioning is achieved by introducing these as additional tokens <a class="yt-timestamp" data-t="33:14:00">[33:14:00]</a>. A dedicated multi-head cross-attention layer within the Transformer blocks processes these conditioning labels, adding approximately 15% computational overhead <a class="yt-timestamp" data-t="33:28:00">[33:28:00]</a>, <a class="yt-timestamp" data-t="33:58:00">[33:58:00]</a>.
*   **Adaptive Normalization (AdaLN)**: DiTs utilize adaptive normalization layers, such as AdaLN, to ensure stable training of deep Transformers <a class="yt-timestamp" data-t="34:09:00">[34:09:00]</a>, <a class="yt-timestamp" data-t="34:20:00">[34:20:00]</a>. This technique applies scale and shift parameters to normalize activations within the network, aiding gradient flow and learning <a class="yt-timestamp" data-t="34:43:00">[34:43:00]</a>. This is especially important for deeper and larger architectures <a class="yt-timestamp" data-t="40:08:00">[40:08:00]</a>. AdaLN is applied immediately prior to any residual connections <a class="yt-timestamp" data-t="37:05:00">[37:05:00]</a>.
*   **Output**: After passing through multiple Transformer blocks, the output is used to predict the noise and its variance to be removed or added to the latent patch <a class="yt-timestamp" data-t="40:36:00">[40:36:00]</a>. The decoded tokens are then rearranged into their original spatial layout <a class="yt-timestamp" data-t="42:58:00">[42:58:00]</a>.

### Model Scaling

DiTs explore [[Scalable diffusion models with Transformers | scalability]] through increased Transformer depth and width <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>. Model sizes vary significantly:
*   **DiT-S (Small)**: 12 Transformer layers, 6 attention heads, hidden dimension of 384 <a class="yt-timestamp" data-t="42:01:00">[42:01:00]</a>, <a class="yt-timestamp" data-t="42:06:00">[42:06:00]</a>.
*   **DiT-XL/2 (Largest)**: 28 Transformer layers, 16 attention heads, hidden dimension of 1152 <a class="yt-timestamp" data-t="42:15:00">[42:15:00]</a>, <a class="yt-timestamp" data-t="42:20:00">[42:20:00]</a>. This "XL/2" nomenclature indicates the largest size (XL) with a patch factor of 2 <a class="yt-timestamp" data-t="43:16:00">[43:16:00]</a>.

Larger DiT models, as measured by GFLOPs, consistently achieve lower FID scores (a quantitative metric for image quality, where lower is better) <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>, <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>. The largest model, DiT-XL/2, achieved a state-of-the-art FID of 2.27 on the 256x256 ImageNet generation benchmark <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>.

DiTs with smaller patch sizes and larger Transformer sizes tend to yield the best results, as smaller patches allow for capturing finer details <a class="yt-timestamp" data-t="56:01:00">[56:01:00]</a>, <a class="yt-timestamp" data-t="56:17:00">[56:17:00]</a>.

### Training and Performance

[[Training and implementation details of Transformerbased diffusion models | Training details]] include:
*   **Learning Rate**: Constant learning rate of 1e-4 with no weight decay, though an exponential moving average of DiT weights is maintained <a class="yt-timestamp" data-t="45:05:00">[45:05:00]</a>, <a class="yt-timestamp" data-t="47:26:00">[47:26:00]</a>.
*   **Hardware**: Models are implemented in JAX and trained on Google TPU v3 pods (e.g., 256 TPUs) <a class="yt-timestamp" data-t="51:15:00">[51:15:00]</a>, <a class="yt-timestamp" data-t="52:46:00">[52:46:00]</a>.
*   **Training Cost**: Training a single DiT model for 400,000 steps on a TPU v3 256 pod (at 5.7 iterations/second) takes approximately 19 hours, costing roughly $10,000 USD <a class="yt-timestamp" data-t="53:57:00">[53:57:00]</a>.

DiT models consistently outperform prior U-Net-based diffusion models on class-conditional ImageNet benchmarks <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>, <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>. While larger models perform better, the efficiency gain from a better architecture means that a smaller DiT model can sometimes outperform a larger model of a different architecture (e.g., ADM) <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>, <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.

**Qualitative Observations**: DiTs produce extremely crisp images with correct semantic information at multiple scales <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. Details such as animal anatomy (e.g., a dog's wrist) are accurately rendered <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. However, some higher-level semantic inconsistencies, typical of generative models, can still appear (e.g., structural oddities in a boat) <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>.

### Future Work

Future research is expected to continue scaling DiT models to even larger sizes and token counts <a class="yt-timestamp" data-t="01:05:13">[01:05:13]</a>. The rapid acceleration of generative model quality suggests that [[causality in depth representation in diffusion models | complex capabilities]], such as generating 4K video from text prompts, could become feasible in the near future <a class="yt-timestamp" data-t="01:14:45">[01:14:45]</a>.