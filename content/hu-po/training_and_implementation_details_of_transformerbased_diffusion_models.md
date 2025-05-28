---
title: Training and implementation details of Transformerbased diffusion models
videoId: eTBG17LANcI
---

From: [[hu-po]] <br/> 

A recent paper titled "[[Scalable diffusion models with Transformers | Scalable diffusion models with Transformers]]" introduces a new class of [[Diffusion Models and ControlNet | diffusion models]] called Diffusion Transformers (DiTs). These models leverage the [[Transformer architecture in diffusion models | Transformer architecture]] as their backbone, replacing the commonly used U-Net structure in [[latent_diffusion_model_for_neural_networks | latent diffusion models]] <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>. This approach aims to achieve [[Performance and scalability of diffusion models with Transformers | state-of-the-art image quality]] by benefiting from the scalability properties inherent in Transformers <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>.

## Architecture: Diffusion Transformers (DiTs)

DiTs are based on the [[Transformer architecture in diffusion models | Vision Transformer (ViT)]] architecture, which processes images as sequences of patches <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.

### Core Design Principles
*   **Latent Space Operation**: The diffusion process occurs in the latent space, meaning the Transformer operates on a lower-dimensional latent representation (Z) derived from the input image, rather than directly on high-resolution pixels <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. For instance, a 256x256x3 image is converted to a 32x32x4 latent vector <a class="yt-timestamp" data-t="29:10:00">[29:10:00]</a>. This significantly reduces computational load <a class="yt-timestamp" data-t="29:21:00">[29:21:00]</a>.
*   **Patching**: The latent representation is broken down into a sequence of patches, similar to how Vision Transformers process images <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>. The number of tokens (T) generated is determined by the patch size (P x P), with tested values of P=2, 4, and 8 <a class="yt-timestamp" data-t="30:51:00">[30:51:00]</a>. Smaller patch sizes lead to more tokens and increased G-flops, but generally better performance <a class="yt-timestamp" data-t="56:01:00">[56:01:00]</a>.
*   **Positional Embeddings**: Frequency-based positional embeddings are incorporated to provide the network with information about the original spatial location of each patch <a class="yt-timestamp" data-t="29:42:00">[29:42:00]</a>.

### Conditioning Information
DiTs can incorporate additional conditional information beyond the noise image input:
*   **Noise Time Step (T)**: The current time step of the diffusion process <a class="yt-timestamp" data-t="32:55:00">[32:55:00]</a>.
*   **Class Labels (C)**: Such as "dog" or "airplane" for [[Conditional diffusion model for neural networks | class-conditional image generation]] <a class="yt-timestamp" data-t="32:52:00">[32:52:52]</a>.
*   **Natural Language Prompts**: Encoded text prompts, often using models like CLIP <a class="yt-timestamp" data-t="33:01:00">[33:01:00]</a>.

### Conditioning Mechanisms
*   **Cross-Attention Block**: An additional multi-head cross-attention layer is included within the Transformer blocks. This layer specifically looks at the conditional labels (time step, class, language) and contributes only about 15% to the overhead <a class="yt-timestamp" data-t="33:39:00">[33:39:00]</a>.
*   **Adaptive Normalization Layers (AdaLN)**: Inspired by adaptive normalization layers, DiTs use standard layer normalization with adaptive scale and shift parameters to maintain numerical stability and aid training <a class="yt-timestamp" data-t="34:09:00">[34:09:00]</a>. This process normalizes activations within each layer, helping gradients flow more effectively <a class="yt-timestamp" data-t="35:21:00">[35:21:00]</a>. Normalization is applied immediately prior to any residual connections <a class="yt-timestamp" data-t="37:05:00">[37:05:05]</a>.

### Model Output
The DiT model outputs both the predicted noise (Epsilon Theta) and the variance of that noise, aiming to remove the noise from the latent vector <a class="yt-timestamp" data-t="40:41:00">[40:41:00]</a>.

## Model Scaling and Performance

The paper analyzes the [[Scaling and Training Techniques for Diffusion Models | scalability]] of DiTs by varying their depth (number of Transformer blocks), width (hidden dimension), and the number of input tokens (by changing patch size) <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.

### DiT Model Sizes
Different model sizes include:
*   **DiT-S (Small)**: 12 Transformer layers, 6 attention heads, hidden dimension of 384 <a class="yt-timestamp" data-t="42:01:00">[42:01:00]</a>.
*   **DiT-L (Large)**: 28 Transformer layers, 16 attention heads, hidden dimension of 1152 <a class="yt-timestamp" data-t="42:14:00">[42:14:00]</a>.
*   **DiT-XL2 (Extra Large, Patch Size 2)**: The largest model, featuring 28 total Transformer layers, 16 multi-attention heads, and a width of 1152 <a class="yt-timestamp" data-t="42:14:00">[42:14:00]</a>. It uses a patch factor of 2 (meaning 2x2 patches, or 4 total patches for the latent vector) <a class="yt-timestamp" data-t="43:28:00">[43:28:00]</a>.

### Scaling Observations
*   **G-flops and FID**: Models with higher G-flops (indicating greater computational complexity) consistently achieve lower FID scores, signifying improved image quality <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.
*   **Compute Efficiency**: Larger DiT models are found to be more compute-efficient <a class="yt-timestamp" data-t="01:00:31">[01:00:31]</a>.
*   **Performance Comparison**: The largest model, [[Scalable diffusion models with Transformers | DiT-XL2]], outperforms all prior U-Net based diffusion models on the class-conditional ImageNet benchmarks <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>. This includes models like ADM, which despite being larger in terms of G-flops, did not perform as well as the architecturally superior DiT models <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>.

## Training Details

### Loss Function
DiTs are trained using a simple Mean Squared Error (MSE) between the predicted noise and the ground truth sampled Gaussian noise <a class="yt-timestamp" data-t="24:09:00">[24:09:00]</a>. For learning the reverse process covariance, the full KL divergence term is optimized <a class="yt-timestamp" data-t="24:36:00">[24:36:00]</a>.

### Optimization and Regularization
*   **Learning Rate**: A constant learning rate of `1 x 10^-4` is used <a class="yt-timestamp" data-t="45:05:00">[45:05:00]</a>.
*   **Weight Decay**: No explicit weight decay or learning rate warm-up is applied <a class="yt-timestamp" data-t="45:12:00">[45:12:00]</a>. However, an exponential moving average (EMA) of DiT weights is maintained <a class="yt-timestamp" data-t="47:26:00">[47:26:00]</a>.
*   **Hyperparameters**: Most training hyperparameters are retained from the ADM model, indicating that minimal tuning was required for this new architecture to show strong results <a class="yt-timestamp" data-t="48:18:00">[48:18:00]</a>.

### VAE and Diffusion Parameters
*   **VAE**: An off-the-shelf pre-trained VAE model from Stable Diffusion is used for encoding images into latent space and decoding them back <a class="yt-timestamp" data-t="49:03:00">[49:03:00]</a>. This VAE has a downsampling factor of 8 <a class="yt-timestamp" data-t="49:15:00">[49:15:00]</a>.
*   **T-Max**: The maximum number of diffusion steps (T-Max) is set to 1000 <a class="yt-timestamp" data-t="49:45:00">[49:45:00]</a>.

### Classifier-Free Guidance
The model incorporates [[Conditional diffusion model for neural networks | classifier-free guidance]], a technique where the conditioning label (C) is randomly dropped out during training <a class="yt-timestamp" data-t="27:01:00">[27:01:01]</a>. This allows for a balance between guided and unguided generation during inference.

### Computational Environment
*   **Framework**: All models are implemented in Jax <a class="yt-timestamp" data-t="51:15:00">[51:15:00]</a>.
*   **Hardware**: Training is conducted on Google's TPU V3 pods <a class="yt-timestamp" data-t="51:22:00">[51:22:00]</a>. For example, the DiT-XL2 model trained at 5.7 iterations per second on a 256-TPU V3 pod <a class="yt-timestamp" data-t="52:46:00">[52:46:00]</a>.
*   **Training Cost**: Training initial models for 400,000 steps on a 256-TPU V3 pod cost approximately $10,000 per model <a class="yt-timestamp" data-t="55:10:00">[55:10:00]</a>. The research involved training 12 different DiT models, implying over $100,000 in compute costs for that initial evaluation <a class="yt-timestamp" data-t="55:20:00">[55:20:00]</a>. Later, models were trained for up to 7 million steps <a class="yt-timestamp" data-t="01:01:47">[01:01:47]</a>.

## Evaluation and Results

### Metrics
*   **Fréchet Inception Distance (FID)**: The primary quantitative metric for image quality, with lower scores indicating better quality <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>.
*   **Other Metrics**: Inception Score, Precision, and Recall are also used for evaluation <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>.

### Sampling Steps
For evaluation, 250 sampling steps are used, a reduction compared to other papers that might use 1000 steps <a class="yt-timestamp" data-t="00:50:20">[00:50:20]</a>. While more sampling steps generally lead to slightly better results, there's a point of diminishing returns <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>.

### Image Quality
The models achieve [[Performance and scalability of diffusion models with Transformers | state-of-the-art image quality]], producing extremely crisp and semantically correct images with no visible artifacts at either texture or macro scales in the best examples <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. However, some semantic "weirdness" can still be observed in complex scenes, such as misconnected elements in a ship or unnatural limb positions in pandas <a class="yt-timestamp" data-t="01:10:51">[01:10:51]</a>.

## Future Outlook

The paper suggests that future work should continue to scale DiT models to even larger sizes and token counts, anticipating further improvements in generative capabilities <a class="yt-timestamp" data-t="01:13:19">[01:13:19]</a>. The rapid acceleration in [[Diffusion Models and ControlNet | diffusion model]] quality over recent years suggests a potential future where text prompts could generate 4K video on demand, fundamentally changing content creation <a class="yt-timestamp" data-t="01:14:56">[01:14:56]</a>. For production use cases, techniques like pruning and quantization would be applied to reduce model size and cost <a class="yt-timestamp" data-t="00:58:56">[00:58:56]</a>.