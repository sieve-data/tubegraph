---
title: Scalable diffusion models with Transformers
videoId: eTBG17LANcI
---

From: [[hu-po]] <br/> 

A recent paper, "Scalable Diffusion Models with Transformers," introduces a new class of [[Transformer architecture in diffusion models | diffusion models]] called Diffusion Transformers (DiTs) <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. Published on December 19th, this research from UC Berkeley and New York University, with significant compute budget provided by Meta AI's FAIR team, showcases state-of-the-art image quality <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

The project has a GitHub repository with code, PyTorch models, and pre-trained weights, although it operates under a CC BY-NC license, meaning it cannot be used for commercial purposes <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>.

## Key Innovation: Replacing U-Nets with Transformers

Historically, [[conditional_diffusion_model_for_neural_networks | diffusion models]] have predominantly adopted the U-Net architecture as their de facto choice <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This paper demonstrates that the U-Net bias is not crucial for the performance of [[conditional_diffusion_model_for_neural_networks | diffusion models]] and can be effectively replaced with standard designs like [[Transformer architecture in diffusion models | Transformers]] <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

The core idea is to train [[latent_diffusion_model_for_neural_networks | latent diffusion models]] where the commonly used U-Net backbone is swapped out for a [[Transformer architecture in diffusion models | Transformer]] that operates on latent patches <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This shift allows [[conditional_diffusion_model_for_neural_networks | diffusion models]] to benefit from the recent trend of architecture unification seen across NLP and vision <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## Diffusion Transformer (DiT) Architecture

DiTs adhere to the best practices of Vision Transformers (ViTs) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Instead of convolving across an image like a traditional convolutional neural network (CNN), ViTs take an image, cut it into small patches, and feed each patch as a token into the [[Transformer architecture in diffusion models | Transformer]] <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

The input to a DiT is a spatial latent representation <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>. For instance, a 256x256x3 image is converted into a lower-dimensional latent embedding, such as 32x32x4 <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a>. This makes the [[Transformer architecture in diffusion models | Transformers]] operate on a smaller piece of data, improving efficiency <a class="yt-timestamp" data-t="00:29:23">[00:29:23]</a>.

DiTs use frequency-based positional embeddings, which provide spatial information for each patch <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>. The number of tokens (T) created from patches is determined by a patch size hyperparameter (P), with the paper experimenting with P values of 2, 4, and 8 <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>. Smaller patch sizes lead to more tokens and increased computational complexity but also better detail <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>.

### Conditioning and Normalization

DiTs are conditioned on:
*   **Noise time step**: Information about the current step in the diffusion process <a class="yt-timestamp" data-t="00:32:55">[00:32:55]</a>.
*   **Class labels**: E.g., 'dog' or 'cat' for ImageNet <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>.
*   **Natural language prompts**: Encoded text prompts, often using models like CLIP <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>.

These conditioning elements are introduced as additional tokens, processed separately from the image tokens, with a cross-attention layer linking them to the main image processing <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>. This cross-attention layer adds only about 15% overhead <a class="yt-timestamp" data-t="00:34:01">[00:34:01]</a>.

The models also heavily utilize adaptive normalization layers, such as adaptive layer normalization (AdaLN), which incorporate scale and shift parameters <a class="yt-timestamp" data-t="00:34:09">[00:34:09]</a>. These normalization techniques ensure activations remain well-distributed, aiding gradient flow and learning <a class="yt-timestamp" data-t="00:35:15">[00:35:15]</a>. They are applied within [[Transformer architecture in diffusion models | Transformer]] blocks and prior to any residual connections <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.

## [[performance_and_scalability_of_diffusion_models_with_transformers | Performance and Scalability]]

The paper analyzes the [[performance_and_scalability_of_diffusion_models_with_transformers | scalability]] of DiTs through their forward pass complexity, measured in Gigaflops <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Key findings include:
*   **Increased Depth and Width**: DiTs with higher Gigaflops (achieved through increased [[Transformer architecture in diffusion models | Transformer]] depth, width, or number of input tokens) consistently result in lower FID (Fréchet Inception Distance) scores, indicating better image quality <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This confirms the well-known machine learning principle: bigger models and more data lead to better results <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **State-of-the-Art Results**: The largest model, DiT-XL/2 (meaning DiT XL with a patch factor of 2), achieved a state-of-the-art FID of 2.27 on the 256x256 ImageNet generation benchmark <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   **Compute Efficiency**: DiT-XL/2 outperforms all prior U-Net based [[conditional_diffusion_model_for_neural_networks | diffusion models]] (e.g., LDM-A, LDM-4G, ADM-G), even models with higher Gigaflops, demonstrating superior compute efficiency <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. This suggests that while scaling is powerful, a better architecture can yield superior results even at a smaller scale <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

Different DiT model sizes (Small, Medium, Large, XL) are defined by their number of [[Transformer architecture in diffusion models | Transformer]] layers (N), hidden dimension size (D), and multi-attention heads. For example, DiT-S has 12 layers, 6 heads, and a hidden dimension of 384, while DiT-XL has 28 layers, 16 heads, and a hidden dimension of 1152 <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>.

## [[training_and_implementation_details_of_transformerbased_diffusion_models | Training and Implementation Details]]

### Loss Function and Guidance
The models are trained using a simple mean squared error between the predicted noise and the ground truth sampled Gaussian noise <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>. They also leverage [[Conditional diffusion model for neural networks | classifier-free guidance]], where conditioning labels (like class labels) are randomly dropped out during training <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.

### Hyperparameters and Initialization
DiTs use a constant learning rate of 1e-4 with no weight decay during initial training phases, though an exponential moving average of DiT weights is maintained <a class="yt-timestamp" data-t="00:45:05">[00:45:05]</a>. Many hyperparameters are retained from prior work (ADM) and were not extensively tuned, suggesting potential for further optimization <a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>. The final layer is initialized with zeros, and standard ViT weight initialization techniques are used otherwise <a class="yt-timestamp" data-t="00:44:55">[00:44:55]</a>.

### Hardware and Cost
Models were implemented in JAX and trained on Google TPU v3 pods <a class="yt-timestamp" data-t="00:51:19">[00:51:19]</a>. The largest model, DiT-XL/2, achieved 5.7 iterations per second on a TPU v3-256 pod <a class="yt-timestamp" data-t="00:52:46">[00:52:46]</a>.

To put this into perspective:
*   Training for 400,000 steps at 5.7 iterations/second takes approximately 19 hours <a class="yt-timestamp" data-t="00:54:01">[00:54:01]</a>.
*   Estimating TPU v3 pricing at $2 per hour per TPU, a 256-TPU pod for 19 hours costs roughly $10,000 per model <a class="yt-timestamp" data-t="00:54:46">[00:54:46]</a>.
*   Training 12 different DiT models for the reported experiments would therefore cost over $100,000 <a class="yt-timestamp" data-t="00:55:20">[00:55:20]</a>.

### Sampling Steps
While the paper reports results primarily with 250 sampling steps, experiments show that increasing sampling steps generally improves quality, though with diminishing returns beyond a certain point <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>.

## Generated Image Quality and Future Outlook

The DiTs produce images with exceptional crispness and semantic correctness, capturing subtle details like the wrist of a dog or wet fur on an otter <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a> <a class="yt-timestamp" data-t="01:12:14">[01:12:14]</a>. However, like many generative models, they can still exhibit inconsistencies at a higher semantic level, such as illogical connections in complex objects (e.g., a boat's mast appearing disconnected) <a class="yt-timestamp" data-t="01:10:40">[01:10:40]</a>.

The researchers note that additional model compute is a critical ingredient for improved DiT models, and larger DiT models are more compute-efficient <a class="yt-timestamp" data-t="01:00:22">[01:00:22]</a>. The paper concludes by suggesting future work should continue to [[scaling_and_training_techniques_for_diffusion_models | scale]] DiTs to larger models and token counts <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>.

The rapid progress in [[conditional_diffusion_model_for_neural_networks | diffusion models]], compared to earlier generative models like GANs, suggests that the speed of improvement is accelerating <a class="yt-timestamp" data-t="01:14:21">[01:14:21]</a>. This could lead to capabilities like generating 4K video from text prompts by the end of 2023, potentially transforming content creation <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>.